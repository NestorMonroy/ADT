#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_blanklines_and_listtable_fp.py

Objetivo
- Normalizar bloques ".. list-table::" para que tengan "exactly one bullet list expected"
  (corrigiendo la indentación y el patrón "* - /   -")
- Insertar líneas en blanco donde Docutils suele marcar:
  "Bullet list ends without a blank line; unexpected unindent."
- Soportar DRY-RUN / APPLY
- Crear backups (por defecto) y excluir archivos BACKUP/backup/bak/~ del procesamiento
- Evitar fallas por archivos Read-only (Windows) usando ensure_writable()

Uso
  python scripts/fix_blanklines_and_listtable_fp.py --path /e/Proyectos/Translate/ADT/source --dry-run
  python scripts/fix_blanklines_and_listtable_fp.py --path /e/Proyectos/Translate/ADT/source
  python scripts/fix_blanklines_and_listtable_fp.py --path /e/Proyectos/Translate/ADT/source --no-backup
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import stat
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


# -----------------------------
# Utilidades de IO
# -----------------------------

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def ensure_writable(p: Path) -> None:
    """
    Garantiza que el archivo sea escribible.
    En Windows elimina el atributo Read-only si existe.
    Fail-safe: no rompe el flujo si falla.
    """
    try:
        mode = os.stat(p).st_mode
        if not (mode & stat.S_IWRITE):
            os.chmod(p, mode | stat.S_IWRITE)
    except Exception:
        pass


def write_text(p: Path, content: str) -> None:
    p.write_text(content, encoding="utf-8", newline="\n")


def make_backup(p: Path, backup_suffix: str) -> Path:
    """
    Crea backup junto al archivo:
      archivo.rst -> archivo.rst.BACKUP_YYYYMMDD_HHMMSS
    """
    backup_path = p.with_name(p.name + backup_suffix)
    shutil.copy2(p, backup_path)
    return backup_path


# -----------------------------
# Filtrado de archivos
# -----------------------------

def is_backup_name(name: str) -> bool:
    n = name.lower()
    return (
        "backup" in n or
        ".backup_" in n or
        n.endswith(".bak") or
        n.endswith("~")
    )


def iter_rst_files(base: Path) -> List[Path]:
    return sorted(
        p for p in base.rglob("*.rst")
        if p.is_file() and not is_backup_name(p.name)
    )


# -----------------------------
# Fix 1: list-table
# -----------------------------

_LIST_TABLE_START_RE = re.compile(r"^\s*\.\.\s+list-table::\s*.*$")
_DIRECTIVE_OPT_RE = re.compile(r"^\s*:\w[\w-]*:\s*.*$")


def _leading_spaces(s: str) -> int:
    return len(s) - len(s.lstrip(" "))


def _is_blank(line: str) -> bool:
    return line.strip() == ""


def _is_bullet_row(line: str) -> bool:
    # "* - ..." (row start)
    return bool(re.match(r"^\s*\*\s+-\s+.*$", line))


def _is_cell_line(line: str) -> bool:
    # "  - ..." (cell continuation)
    return bool(re.match(r"^\s*-\s+.*$", line)) and not _is_bullet_row(line)


def _normalize_list_table_block(block_lines: List[str]) -> Tuple[List[str], int]:
    """
    Normaliza un bloque list-table.

    Problema típico (mal):
      * - **Col1**
        - **Col2**
      - **Col3**

    Lo correcto:
      * - **Col1**
        - **Col2**
        - **Col3**

    Regla: Dentro de list-table, todas las celdas (excepto el inicio de fila "* -")
    deben tener indentación consistente (al menos 2 espacios más que "*").
    """
    if not block_lines:
        return block_lines, 0

    replacements = 0

    # Detectar indent base del ".. list-table::"
    start_indent = _leading_spaces(block_lines[0])

    # Encontrar dónde terminan opciones ":header-rows:" etc.
    # Se asume que block_lines incluye desde ".. list-table::" hasta antes de que
    # termine el bloque (corte por indent o EOF) ya lo maneja el extractor.
    i = 1
    while i < len(block_lines) and (_is_blank(block_lines[i]) or _DIRECTIVE_OPT_RE.match(block_lines[i])):
        i += 1

    # A partir de i, esperamos bullets "* -"
    # Definimos indentaciones objetivo:
    row_indent = start_indent + 1  # típico: 1 espacio después del inicio (pero flexible)
    # Mejor: si la primera fila "* - " existe, usar su indent real.
    first_row_idx = None
    for j in range(i, len(block_lines)):
        if _is_bullet_row(block_lines[j]):
            first_row_idx = j
            break
        if not _is_blank(block_lines[j]):
            break

    if first_row_idx is None:
        return block_lines, 0

    row_indent = _leading_spaces(block_lines[first_row_idx])
    cell_indent = row_indent + 2  # mínimo recomendado (consistente)

    # Normalización:
    out = block_lines[:]
    for k in range(first_row_idx, len(out)):
        line = out[k]
        if _is_blank(line):
            continue

        # Si aparece un "-" de celda con indent <= row_indent, lo subimos a cell_indent.
        if _is_cell_line(line):
            cur = _leading_spaces(line)
            if cur <= row_indent:
                out[k] = (" " * cell_indent) + line.lstrip(" ")
                replacements += 1
                continue

            # Si aparece indent demasiado grande, no tocamos (podría ser sublista intencional)
            # excepto si es exactamente 1 espacio más que row_indent (frecuente)
            if cur == row_indent + 1:
                out[k] = (" " * cell_indent) + line.lstrip(" ")
                replacements += 1
                continue

        # Asegurar que "* - " tenga indent al menos row_indent (si no coincide)
        if _is_bullet_row(line):
            cur = _leading_spaces(line)
            if cur != row_indent:
                out[k] = (" " * row_indent) + line.lstrip(" ")
                replacements += 1

    return out, replacements


def fix_list_table_blocks(lines: List[str]) -> Tuple[List[str], int]:
    """
    Encuentra y normaliza todos los bloques list-table.
    """
    out: List[str] = []
    i = 0
    replacements = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if not _LIST_TABLE_START_RE.match(line):
            out.append(line)
            i += 1
            continue

        # Capturar bloque completo: desde ".. list-table::" hasta que la indentación
        # vuelva a ser < start_indent o EOF, ignorando líneas en blanco iniciales.
        start_indent = _leading_spaces(line)
        block: List[str] = [line]
        i += 1

        while i < n:
            nxt = lines[i]
            if _is_blank(nxt):
                block.append(nxt)
                i += 1
                continue

            cur_indent = _leading_spaces(nxt)

            # La directiva list-table y su contenido viven con indent > start_indent,
            # excepto que docutils tolera algunas líneas al mismo indent si son parte,
            # pero en práctica: contenido debe estar indentado más que start_indent.
            # Criterio de corte: si indent <= start_indent y no es opción, terminó bloque.
            if cur_indent <= start_indent and not _DIRECTIVE_OPT_RE.match(nxt):
                break

            block.append(nxt)
            i += 1

        fixed_block, rep = _normalize_list_table_block(block)
        out.extend(fixed_block)
        replacements += rep

        # No consumir la línea de corte (la procesará el loop)
        continue

    return out, replacements


# -----------------------------
# Fix 2: blank lines / listas
# -----------------------------

_BULLET_RE = re.compile(r"^\s*([-*+]|\d+\.)\s+.+$")
_UNINDENT_END_RE = re.compile(r"^\S")  # línea sin indent (posible unindent)
_DIRECTIVE_RE = re.compile(r"^\s*\.\.\s+\w+::.*$")


def _needs_blank_between(prev: str, cur: str) -> bool:
    """
    Heurística conservadora:
    - Si prev es bullet y cur es una línea "no indentada" que NO es bullet,
      suele requerir blank line entre ellos.
    - Si prev es un bloque/directiva y cur es texto normal sin línea en blanco, también.
    """
    if _is_blank(prev):
        return False

    prev_is_bullet = bool(_BULLET_RE.match(prev))
    cur_is_bullet = bool(_BULLET_RE.match(cur))
    cur_is_directive = bool(_DIRECTIVE_RE.match(cur))

    # Caso clásico: lista termina y viene párrafo sin blank line
    if prev_is_bullet and (not cur_is_bullet) and (cur.strip() != ""):
        # si cur tiene indent, probablemente sigue en lista; no insertamos
        if _leading_spaces(cur) == 0 and not cur_is_directive:
            return True

    # Directiva seguida de texto sin blank line: en general ya debería estar bien
    # pero si la directiva no consume nada, docutils se queja; esto es complejo.
    return False


def fix_blanklines(lines: List[str]) -> Tuple[List[str], int]:
    out: List[str] = []
    replacements = 0

    for idx, line in enumerate(lines):
        if out:
            prev = out[-1]
            if _needs_blank_between(prev, line):
                out.append("\n")
                replacements += 1
        out.append(line)

    return out, replacements


# -----------------------------
# Pipeline de transformación
# -----------------------------

def process_content(content: str) -> Tuple[str, int]:
    """
    Aplica fixers en orden:
    1) list-table
    2) blanklines
    """
    # Conservar saltos de línea originales por línea
    raw_lines = content.splitlines(keepends=True)
    lines1, rep1 = fix_list_table_blocks(raw_lines)
    lines2, rep2 = fix_blanklines(lines1)
    updated = "".join(lines2)
    return updated, (rep1 + rep2)


# -----------------------------
# Config y ejecución
# -----------------------------

@dataclass(frozen=True)
class Config:
    base_path: Path
    dry_run: bool
    do_backup: bool


@dataclass
class FileResult:
    path: Path
    changed: bool
    replacements: int
    error: Optional[str] = None
    backup_path: Optional[Path] = None


def apply_one_file(cfg: Config, p: Path, backup_suffix: str) -> FileResult:
    try:
        original = read_text(p)
    except Exception as e:
        return FileResult(path=p, changed=False, replacements=0, error=f"read_error: {e}")

    updated, replacements = process_content(original)

    if updated == original or replacements == 0:
        return FileResult(path=p, changed=False, replacements=0)

    if cfg.dry_run:
        return FileResult(path=p, changed=True, replacements=replacements)

    backup_path = None
    if cfg.do_backup:
        try:
            backup_path = make_backup(p, backup_suffix)
        except Exception as e:
            # Si el backup falla, mejor no escribir para evitar pérdida.
            return FileResult(path=p, changed=False, replacements=0, error=f"backup_error: {e}")

    try:
        ensure_writable(p)
        write_text(p, updated)
    except PermissionError as e:
        return FileResult(
            path=p,
            changed=False,
            replacements=0,
            error=f"PermissionError: {e}",
            backup_path=backup_path,
        )
    except Exception as e:
        return FileResult(
            path=p,
            changed=False,
            replacements=0,
            error=f"write_error: {e}",
            backup_path=backup_path,
        )

    return FileResult(path=p, changed=True, replacements=replacements, backup_path=backup_path)


def print_header(cfg: Config) -> None:
    mode = "DRY-RUN" if cfg.dry_run else "APLICAR"
    backup = "SÍ" if cfg.do_backup else "NO"
    print("=" * 80)
    print("[START] Reparación de blanks + list-table")
    print(f"[INFO]  Directorio: {cfg.base_path}")
    print(f"[INFO]  Modo: {mode}")
    print(f"[INFO]  Backup: {backup}")
    print("=" * 80)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Reparación de blanks + list-table en .rst")
    parser.add_argument("--path", required=True, help="Ruta base a procesar (source)")
    parser.add_argument("--dry-run", action="store_true", help="No modifica archivos, solo reporta cambios")
    parser.add_argument("--no-backup", action="store_true", help="No crear backups")
    args = parser.parse_args(argv)

    base_path = Path(args.path).expanduser()
    # Si te pasan /e/... desde Git Bash, Path lo interpreta literal; asumimos que ya existe.
    if not base_path.exists():
        # Intento defensivo: si viene /e/..., convertir a E:\...
        m = re.match(r"^/([a-zA-Z])/(.*)$", str(base_path))
        if m:
            drive = m.group(1).upper()
            rest = m.group(2).replace("/", "\\")
            win_path = Path(f"{drive}:\\{rest}")
            if win_path.exists():
                base_path = win_path

    cfg = Config(
        base_path=base_path,
        dry_run=bool(args.dry_run),
        do_backup=not bool(args.no_backup),
    )

    print_header(cfg)

    if not cfg.base_path.exists() or not cfg.base_path.is_dir():
        print(f"[ERROR] Ruta inválida: {cfg.base_path}")
        return 2

    rst_files = iter_rst_files(cfg.base_path)

    # Nota: el log del usuario mostraba 308/303 según exclusiones.
    # Aquí imprimimos el total real encontrado.
    print(f"[INFO] Archivos .rst encontrados: {len(rst_files)}")

    backup_suffix = f".BACKUP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    processed = 0
    changed_files = 0
    total_replacements = 0
    fixed_files = 0
    backups_created = 0
    failed_files: List[FileResult] = []
    changed_list: List[Tuple[Path, int]] = []

    for p in rst_files:
        processed += 1
        fr = apply_one_file(cfg, p, backup_suffix)

        if fr.error:
            failed_files.append(fr)
            print(f"[FAIL] {p.as_posix()} -> {fr.error}")
            continue

        if fr.changed:
            changed_files += 1
            total_replacements += fr.replacements
            changed_list.append((p, fr.replacements))

            if cfg.dry_run:
                print(f"[CHANGE] [DRY-RUN] {p.relative_to(cfg.base_path).as_posix()} -> {fr.replacements} correcciones")
            else:
                print(f"[CHANGE] {p.relative_to(cfg.base_path).as_posix()} -> {fr.replacements} correcciones")
                fixed_files += 1
                if fr.backup_path is not None:
                    backups_created += 1

    print("\n" + "=" * 80)
    print("RESUMEN")
    print("=" * 80)
    print(f"Archivos procesados:     {processed}")
    print(f"Archivos con cambios:    {changed_files}")
    print(f"Reemplazos totales:      {total_replacements}")
    print(f"Archivos arreglados:     {0 if cfg.dry_run else fixed_files}")
    print(f"Backups creados:         {0 if cfg.dry_run else backups_created}")
    if failed_files:
        print(f"Archivos fallidos:       {len(failed_files)}")
    print("=" * 80)

    if changed_list:
        print("\nArchivos afectados:")
        for p, reps in changed_list:
            rel = p.relative_to(cfg.base_path).as_posix()
            print(f"  - {rel} ({reps} correcciones)")

    if failed_files:
        print("\nArchivos fallidos:")
        for fr in failed_files:
            rel = fr.path.relative_to(cfg.base_path).as_posix()
            print(f"  - {rel} -> {fr.error}")

    if cfg.dry_run:
        print("\n[DRY-RUN] No se modificaron archivos.")
    else:
        if failed_files:
            print("\n[WARN] Corrida completada con fallos. Revisa los archivos fallidos.")
        else:
            print("\n[OK] Corrida completada sin fallos.")

    # Código de salida: 0 si ok, 1 si hubo fallos de permisos/escritura/backup
    return 1 if failed_files else 0


if __name__ == "__main__":
    raise SystemExit(main())
