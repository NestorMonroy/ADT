#!/usr/bin/env python3
"""
Fixer FP para reparar contenido de bloques `.. list-table::` en RST.

Qué arregla:
- Dentro de `.. list-table::`, convierte celdas mal formadas:
    (misma indentación de fila) "- texto"  -> "  - texto"
  usando el indent real detectado de la fila "* -".

- Se limita estrictamente a bloques list-table (no toca listas fuera).

Uso:
  python fix_list_table_blocks_fp.py --path source --dry-run
  python fix_list_table_blocks_fp.py --path source
  python fix_list_table_blocks_fp.py --path source --no-backup --save-log
"""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from datetime import datetime
from functools import reduce
from pathlib import Path
from typing import Callable, List, Tuple, Optional


# ============================================================================
# Tipos inmutables
# ============================================================================

@dataclass(frozen=True)
class Config:
    base_path: Path
    dry_run: bool
    backup: bool
    verbose: bool
    save_log: bool


@dataclass(frozen=True)
class Stats:
    files_processed: int = 0
    files_with_changes: int = 0
    files_fixed: int = 0
    replacements_made: int = 0
    backups_created: int = 0

    def add_file_processed(self) -> "Stats":
        return Stats(
            files_processed=self.files_processed + 1,
            files_with_changes=self.files_with_changes,
            files_fixed=self.files_fixed,
            replacements_made=self.replacements_made,
            backups_created=self.backups_created,
        )

    def add_changes(self, replacements: int) -> "Stats":
        return Stats(
            files_processed=self.files_processed,
            files_with_changes=self.files_with_changes + 1,
            files_fixed=self.files_fixed,
            replacements_made=self.replacements_made + replacements,
            backups_created=self.backups_created,
        )

    def add_fixed(self) -> "Stats":
        return Stats(
            files_processed=self.files_processed,
            files_with_changes=self.files_with_changes,
            files_fixed=self.files_fixed + 1,
            replacements_made=self.replacements_made,
            backups_created=self.backups_created,
        )

    def add_backup(self) -> "Stats":
        return Stats(
            files_processed=self.files_processed,
            files_with_changes=self.files_with_changes,
            files_fixed=self.files_fixed,
            replacements_made=self.replacements_made,
            backups_created=self.backups_created + 1,
        )


@dataclass(frozen=True)
class FileResult:
    path: Path
    original: str
    updated: str
    replacements: int


@dataclass(frozen=True)
class ProcessResult:
    stats: Stats
    logs: List[str]
    fixed_files: List[Tuple[str, int]]


# ============================================================================
# Utilidades FP
# ============================================================================

def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def log_add(config: Config, logs: List[str], msg: str, level: str = "INFO") -> List[str]:
    line = f"[{level}] {msg}"
    if config.verbose:
        print(line)
    return logs + [line]


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, content: str) -> None:
    p.write_text(content, encoding="utf-8")


def backup_path(p: Path, stamp: str) -> Path:
    return p.parent / f"{p.name}.backup_{stamp}"


def copy_file(src: Path, dst: Path) -> None:
    shutil.copy2(src, dst)


def rst_files(base: Path) -> List[Path]:
    return sorted(
        p for p in base.rglob("*.rst")
        if "BACKUP" not in p.name and "backup" not in p.name
    )

# ============================================================================
# Núcleo: reparación de list-table por “bloques”
# ============================================================================

def is_list_table_directive(line: str) -> bool:
    s = line.lstrip()
    return s.startswith(".. list-table::")


def leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def is_option_line(line: str, directive_indent: int) -> bool:
    # Opciones tipo ":header-rows: 1" deben ir indentadas más que la directiva
    if not line.strip():
        return False
    return leading_spaces(line) > directive_indent and line.lstrip().startswith(":")


def is_block_line(line: str, directive_indent: int) -> bool:
    # El contenido del bloque debe ir indentado más que la directiva
    return bool(line.strip()) and leading_spaces(line) > directive_indent


def fix_list_table_block(lines: List[str], start_i: int) -> Tuple[List[str], int, int]:
    """
    Procesa un bloque list-table desde start_i.
    Retorna:
      - nuevas líneas
      - índice final (exclusive)
      - reemplazos hechos
    """
    directive_line = lines[start_i]
    d_indent = leading_spaces(directive_line)

    i = start_i + 1

    # Consumir opciones (:header-rows:, :widths:, etc.)
    while i < len(lines) and (is_option_line(lines[i], d_indent) or (lines[i].strip() == "" and i < len(lines))):
        # Permitimos líneas en blanco entre opciones, Sphinx lo tolera bien.
        # Ojo: si hay una línea en blanco y luego contenido, sigue siendo parte del bloque.
        # No “cortamos” el bloque aquí.
        i += 1

    # Ahora debe venir el contenido del list-table (bullet list indentada)
    replacements = 0
    out = lines[:start_i + 1]  # hasta la directiva incluida

    # Copiar lo que consumimos (opciones + blanks)
    out.extend(lines[start_i + 1:i])

    current_row_indent: Optional[int] = None

    # Consumir contenido del bloque hasta que dedente o EOF
    while i < len(lines):
        line = lines[i]

        # Fin del bloque: dedent (línea no vacía con indent <= d_indent)
        if line.strip() and leading_spaces(line) <= d_indent:
            break

        # Línea vacía: se conserva
        if not line.strip():
            out.append(line)
            i += 1
            continue

        # Dentro del bloque: detectar inicio de fila "* -"
        stripped = line.lstrip()
        if stripped.startswith("* - "):
            current_row_indent = leading_spaces(line)
            out.append(line)
            i += 1
            continue

        # Dentro del bloque: si ya vimos fila, arreglar celdas mal formadas
        # Caso problemático típico:
        #   (mismo indent de fila) "- **Modo 2**"
        # Debe ser:
        #   (indent de fila + 2 espacios) "- **Modo 2**"
        if current_row_indent is not None:
            # Mismo indent exacto que "* -", pero con "- " en vez de "  -"
            if line.startswith(" " * current_row_indent + "- "):
                fixed = (" " * current_row_indent) + "  - " + line[len(" " * current_row_indent + "- "):]
                out.append(fixed)
                replacements += 1
                i += 1
                continue

            # Variante: alguien puso " - " (un espacio extra) al nivel de fila
            if line.startswith(" " * current_row_indent + " - "):
                fixed = (" " * current_row_indent) + "  - " + line[len(" " * current_row_indent + " - "):]
                out.append(fixed)
                replacements += 1
                i += 1
                continue

        # Si no es caso a corregir, dejar tal cual
        out.append(line)
        i += 1

    # Añadir el resto del archivo (desde fin del bloque)
    out.extend(lines[i:])
    return out, i, replacements


def fix_content(content: str) -> Tuple[str, int]:
    lines = content.splitlines(keepends=True)
    i = 0
    total_repl = 0
    out_lines = lines

    # Escaneo incremental; cada fix rehace la lista completa
    while i < len(out_lines):
        if is_list_table_directive(out_lines[i]):
            out_lines, new_i, repl = fix_list_table_block(out_lines, i)
            total_repl += repl
            # Avanzar: no quedarnos pegados
            i = max(new_i, i + 1)
        else:
            i += 1

    return "".join(out_lines), total_repl


# ============================================================================
# Pipeline FP por archivo
# ============================================================================

def process_file(config: Config) -> Callable[[Path], FileResult]:
    def inner(p: Path) -> FileResult:
        original = read_text(p)
        updated, repl = fix_content(original)
        return FileResult(path=p, original=original, updated=updated, replacements=repl)
    return inner


def apply_result(config: Config) -> Callable[[FileResult], FileResult]:
    def inner(r: FileResult) -> FileResult:
        if r.replacements <= 0:
            return r
        if config.dry_run:
            return r
        if config.backup:
            b = backup_path(r.path, now_stamp())
            copy_file(r.path, b)
        write_text(r.path, r.updated)
        return r
    return inner


def update_stats(stats: Stats, r: FileResult, config: Config) -> Stats:
    s = stats.add_file_processed()
    if r.replacements > 0:
        s = s.add_changes(r.replacements)
        # Si no es dry-run, consideramos "fixed"
        if not config.dry_run:
            s = s.add_fixed()
            if config.backup:
                s = s.add_backup()
    return s


def run(config: Config) -> ProcessResult:
    files = rst_files(config.base_path)
    logs: List[str] = []
    logs = log_add(config, logs, f"Archivos .rst encontrados: {len(files)}")

    proc = process_file(config)
    results = list(map(proc, files))

    changer = apply_result(config)
    changed = list(map(changer, filter(lambda r: r.replacements > 0, results)))

    # Stats (reduce)
    stats = reduce(lambda acc, r: update_stats(acc, r, config), results, Stats())

    fixed_files = [(str(r.path.relative_to(config.base_path)), r.replacements) for r in changed]

    for r in results:
        if r.replacements > 0:
            rel = r.path.relative_to(config.base_path)
            if config.dry_run:
                logs = log_add(config, logs, f"[DRY-RUN] {rel} -> {r.replacements} correcciones", "CHANGE")
            else:
                logs = log_add(config, logs, f"Arreglado: {rel} -> {r.replacements} correcciones", "FIXED")

    return ProcessResult(stats=stats, logs=logs, fixed_files=fixed_files)


def save_log_file(config: Config, logs: List[str], stats: Stats) -> None:
    if not config.save_log:
        return
    out = config.base_path.parent / "fix_list_table_blocks_fp.log"
    header = [
        "Log de reparación list-table (FP)",
        f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Directorio: {config.base_path}",
        f"Modo: {'DRY-RUN' if config.dry_run else 'EJECUCIÓN'}",
        "",
        "=" * 80,
        "",
        *logs,
        "",
        "=" * 80,
        f"Archivos procesados:     {stats.files_processed}",
        f"Archivos con cambios:    {stats.files_with_changes}",
        f"Reemplazos totales:      {stats.replacements_made}",
        f"Archivos arreglados:     {stats.files_fixed}",
        f"Backups creados:         {stats.backups_created}",
        "",
    ]
    out.write_text("\n".join(header), encoding="utf-8")
    if config.verbose:
        print(f"[INFO] Log guardado en: {out}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Reparar bloques list-table en RST (FP).")
    ap.add_argument("--path", default="source", help="Ruta base (default: source)")
    ap.add_argument("--dry-run", action="store_true", help="No modifica archivos, solo reporta")
    ap.add_argument("--no-backup", action="store_true", help="No crear backups")
    ap.add_argument("--quiet", action="store_true", help="Modo silencioso")
    ap.add_argument("--save-log", action="store_true", help="Guardar log en archivo")
    args = ap.parse_args()

    config = Config(
        base_path=Path(args.path),
        dry_run=args.dry_run,
        backup=not args.no_backup,
        verbose=not args.quiet,
        save_log=args.save_log,
    )

    if not config.base_path.exists():
        print(f"[ERROR] Directorio no existe: {config.base_path}")
        return 1

    if config.verbose:
        print("=" * 80)
        print("[START] Reparación de bloques list-table")
        print(f"[INFO]  Directorio: {config.base_path}")
        print(f"[INFO]  Modo: {'DRY-RUN' if config.dry_run else 'EJECUCIÓN'}")
        print(f"[INFO]  Backup: {'SÍ' if config.backup else 'NO'}")
        print("=" * 80)

    result = run(config)

    if config.verbose:
        print("\n" + "=" * 80)
        print("RESUMEN")
        print("=" * 80)
        print(f"Archivos procesados:     {result.stats.files_processed}")
        print(f"Archivos con cambios:    {result.stats.files_with_changes}")
        print(f"Reemplazos totales:      {result.stats.replacements_made}")
        print(f"Archivos arreglados:     {result.stats.files_fixed}")
        print(f"Backups creados:         {result.stats.backups_created}")
        print("=" * 80)

        if result.fixed_files:
            print("\nArchivos afectados:")
            for p, c in result.fixed_files:
                print(f"  - {p} ({c} correcciones)")

        if config.dry_run:
            print("\n[DRY-RUN] No se modificaron archivos.")

    save_log_file(config, result.logs, result.stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
