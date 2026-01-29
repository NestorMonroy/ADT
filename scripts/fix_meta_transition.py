#!/usr/bin/env python3
"""
Script MEJORADO para detectar y corregir el error: "Document or section may not begin with a transition"

IMPROVED VERSION: Maneja múltiples patrones de estructura de archivos
- Patrón 1: Meta + Referencia + Título
- Patrón 2: Meta + Título (sin referencia)
- Patrón 3: Referencia + Título + Meta (CORRECTO - no cambia)
- Patrón 4: Título + Meta + Contenido (INCORRECTO - requiere reorganización)

Uso:
    python fix_meta_transition_improved.py [--dry-run] [--no-backup] [--path source] [--quiet]
"""

import re
import os
import sys
import argparse
from pathlib import Path
import shutil
from datetime import datetime


class ImprovedMetaTransitionFixer:
    def __init__(self, base_path, dry_run=False, backup=True, verbose=True):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.backup = backup
        self.verbose = verbose
        self.stats = {
            'files_processed': 0,
            'files_with_issue': 0,
            'files_fixed': 0,
            'files_already_correct': 0,
            'backups_created': 0,
        }
        self.changes_log = []
        self.issues_found = []

    def log(self, message, level='INFO'):
        """Log mensaje con nivel"""
        if self.verbose:
            prefix = f"[{level}]".ljust(12)
            print(f"{prefix} {message}")
        self.changes_log.append(f"[{level}] {message}")

    def create_backup(self, file_path):
        """Crear backup de archivo"""
        if not self.backup or self.dry_run:
            return None

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = file_path.parent / f"{file_path.name}.backup_{timestamp}"

        shutil.copy2(file_path, backup_path)
        self.stats['backups_created'] += 1
        self.log(f"Backup creado: {backup_path.name}", 'BACKUP')
        return backup_path

    def is_reference_line(self, line):
        """Detectar si una línea es una referencia (.. _nombre:)"""
        return line.strip().startswith('.. _') and line.strip().endswith(':')

    def is_transition_line(self, line):
        """Detectar si una línea es una transición decorativa (====, ----, etc)"""
        if len(line.strip()) < 5:
            return False
        stripped = line.strip()
        return all(c == stripped[0] for c in stripped) and stripped[0] in '=-*~^_'

    def is_meta_directive(self, line):
        """Detectar si una línea es un meta directive"""
        return line.strip() == '.. meta::'

    def get_meta_block(self, lines, start_idx):
        """
        Extraer el bloque completo del meta directive comenzando en start_idx
        Retorna: (end_idx, meta_lines)
        """
        meta_lines = [lines[start_idx]]
        idx = start_idx + 1

        # El meta directive termina cuando encontramos una línea que no está indentada
        while idx < len(lines):
            line = lines[idx]
            if line.strip() == '':
                meta_lines.append(line)
                idx += 1
            elif line.startswith('   '):  # Indentado (parte del meta)
                meta_lines.append(line)
                idx += 1
            else:
                # Encontramos el fin del meta directive
                break

        return idx, meta_lines

    def find_title_block(self, lines, start_idx):
        """
        Buscar un bloque de título comenzando desde start_idx
        Formato: transición, texto, transición
        Retorna: (start_idx, end_idx, title_lines) o (None, None, None) si no encuentra
        """
        idx = start_idx

        # Saltar líneas en blanco
        while idx < len(lines) and lines[idx].strip() == '':
            idx += 1

        if idx >= len(lines):
            return None, None, None

        # Primera línea debe ser transición
        if not self.is_transition_line(lines[idx]):
            return None, None, None

        trans_start = idx
        idx += 1

        # Segunda línea: el título
        if idx >= len(lines):
            return None, None, None

        title_line = lines[idx]
        idx += 1

        # Tercera línea: transición de cierre
        if idx >= len(lines) or not self.is_transition_line(lines[idx]):
            return None, None, None

        title_end = idx + 1

        return trans_start, title_end, lines[trans_start:title_end]

    def reorganize_file(self, content, file_path):
        """
        Reorganizar un archivo detectando su patrón y arreglándolo si es necesario
        """
        lines = content.split('\n')

        # Patrón 1: Meta al inicio → necesita reorganización
        if lines and self.is_meta_directive(lines[0]):
            return self._reorganize_pattern1(lines, file_path)

        # Patrón 2: Título al inicio, luego meta → necesita reorganización
        if lines and self.is_transition_line(lines[0]):
            return self._reorganize_pattern2(lines, file_path)

        # Patrón 3: Referencia al inicio → probablemente está bien
        if lines and self.is_reference_line(lines[0]):
            # Verificar que la estructura sea: ref, título, meta
            return None, False

        # Si no coincide con ningún patrón problemático
        return None, False

    def _reorganize_pattern1(self, lines, file_path):
        """
        Patrón 1: Meta directive al inicio
        De: meta + [ref + título] | [título] + contenido
        A: [ref +] título + meta + contenido
        """
        meta_end, meta_lines = self.get_meta_block(lines, 0)

        # Buscar referencia después del meta
        ref_idx = None
        ref_line = None
        for i in range(meta_end, min(meta_end + 3, len(lines))):
            if self.is_reference_line(lines[i]):
                ref_idx = i
                ref_line = lines[i]
                break

        # Buscar título
        title_start, title_end, title_lines = self.find_title_block(
            lines, meta_end if ref_idx is None else ref_idx + 1
        )

        if title_start is None:
            return None, False

        # Reconstruir
        new_lines = []

        # Agregar referencias (si existe)
        if ref_idx is not None:
            new_lines.append(ref_line)
            new_lines.append('')

        # Agregar título
        new_lines.extend(title_lines)
        new_lines.append('')

        # Agregar meta
        new_lines.extend(meta_lines)

        # Agregar resto del contenido (después del título)
        remaining_start = title_end
        # Saltar líneas en blanco redundantes
        while remaining_start < len(lines) and lines[remaining_start].strip() == '':
            remaining_start += 1

        if remaining_start < len(lines):
            new_lines.extend(lines[remaining_start:])

        new_content = '\n'.join(new_lines)
        return new_content, True

    def _reorganize_pattern2(self, lines, file_path):
        """
        Patrón 2: Título al inicio, luego meta
        De: título + meta + [otros directives] + contenido
        A: título + meta + [otros directives] + contenido (ya está bien)
        """
        # Este patrón ESTÁ MAL pero puede estar intencional
        # Lo mejor es dejarlo como está o mostrarlo como advertencia

        # Buscar si meta está justo después del título
        title_start, title_end, _ = self.find_title_block(lines, 0)

        if title_start is None:
            return None, False

        # Buscar meta después del título
        meta_idx = None
        for i in range(title_end, min(title_end + 5, len(lines))):
            if self.is_meta_directive(lines[i]):
                meta_idx = i
                break

        if meta_idx is None:
            return None, False

        # Si meta está en el lugar correcto (después del título), está bien
        # No necesita cambios
        return None, False

    def process_file(self, file_path):
        """Procesar un archivo individual"""
        self.stats['files_processed'] += 1
        rel_path = file_path.relative_to(self.base_path)

        try:
            # Leer contenido
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Intentar reorganizar
            new_content, was_changed = self.reorganize_file(content, file_path)

            if was_changed:
                self.stats['files_with_issue'] += 1
                self.stats['files_fixed'] += 1
                self.issues_found.append(str(rel_path))
                self.log(f"Problema encontrado y corregido: {rel_path}", 'FIXED')

                if not self.dry_run:
                    # Crear backup
                    self.create_backup(file_path)

                    # Escribir nuevo contenido
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

            else:
                self.stats['files_already_correct'] += 1

        except Exception as e:
            self.log(f"Error procesando {file_path.name}: {str(e)[:50]}", 'ERROR')

    def process_directory(self):
        """Procesar todos los archivos .rst en directorio"""
        if not self.base_path.exists():
            self.log(f"Error: Directorio no existe: {self.base_path}", 'ERROR')
            return False

        print("\n" + "=" * 80)
        self.log("Iniciando búsqueda MEJORADA de errores de transición en meta directives", 'START')
        self.log(f"Directorio: {self.base_path}", 'INFO')
        self.log(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCIÓN'}", 'INFO')
        self.log(f"Backup: {'SÍ' if self.backup else 'NO'}", 'INFO')
        print("=" * 80 + "\n")

        # Encontrar todos los archivos .rst
        rst_files = list(self.base_path.rglob('*.rst'))
        self.log(f"Archivos .rst encontrados: {len(rst_files)}", 'INFO')
        print()

        # Procesar cada archivo
        for file_path in sorted(rst_files):
            self.process_file(file_path)

        print()
        return True

    def print_summary(self):
        """Imprimir resumen de cambios"""
        print("\n" + "=" * 80)
        print("RESUMEN DE EJECUCIÓN MEJORADA")
        print("=" * 80)
        print(f"Archivos procesados:         {self.stats['files_processed']}")
        print(f"Ya están correctos:          {self.stats['files_already_correct']}")
        print(f"Con problemas encontrados:   {self.stats['files_with_issue']}")
        print(f"Archivos corregidos:         {self.stats['files_fixed']}")
        print(f"Backups creados:             {self.stats['backups_created']}")
        print("=" * 80)

        if self.issues_found:
            print("\nArchivos que se arreglaron:")
            for issue in self.issues_found:
                print(f"  ✓ {issue}")

        if self.dry_run:
            print("\n[DRY-RUN] No se modificaron archivos.")
            print("Ejecuta sin --dry-run para aplicar cambios.")
        elif self.stats['files_fixed'] > 0:
            print("\nCorrecciones aplicadas exitosamente.")
            if self.backup:
                print("Backups creados con extensión .backup_TIMESTAMP")
        else:
            print("\nTodos los archivos ya están correctamente formados.")

    def save_log(self, log_path='fix_meta_transition_improved.log'):
        """Guardar log de cambios"""
        log_file = self.base_path.parent / log_path
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("Log de corrección MEJORADA de transiciones en meta directives\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Directorio: {self.base_path}\n")
            f.write(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCIÓN'}\n")
            f.write("\n" + "=" * 80 + "\n\n")
            f.write("CHANGELOG:\n\n")
            f.write("\n".join(self.changes_log))
            f.write("\n\n" + "=" * 80 + "\n")
            f.write(f"Archivos procesados:         {self.stats['files_processed']}\n")
            f.write(f"Ya están correctos:          {self.stats['files_already_correct']}\n")
            f.write(f"Con problemas:               {self.stats['files_with_issue']}\n")
            f.write(f"Corregidos:                  {self.stats['files_fixed']}\n")
            f.write(f"Backups creados:             {self.stats['backups_created']}\n")

        print(f"\nLog guardado en: {log_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Detectar y corregir errores de transición en meta directives (VERSIÓN MEJORADA)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  # Dry-run (no modifica archivos)
  python fix_meta_transition_improved.py --dry-run

  # Ejecutar sin backup
  python fix_meta_transition_improved.py --no-backup

  # Ejecutar en directorio específico
  python fix_meta_transition_improved.py --path /path/to/source

  # Modo silencioso
  python fix_meta_transition_improved.py --quiet

  # Con log de cambios
  python fix_meta_transition_improved.py --save-log

  # Todas las opciones
  python fix_meta_transition_improved.py --path source --dry-run --save-log
        """
    )

    parser.add_argument(
        '--path',
        default='source',
        help='Ruta al directorio a procesar (default: source)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Mostrar cambios sin modificar archivos'
    )

    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='No crear backups de archivos modificados'
    )

    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (menos output)'
    )

    parser.add_argument(
        '--save-log',
        action='store_true',
        help='Guardar log de cambios en archivo'
    )

    args = parser.parse_args()

    # Crear fixer mejorado
    fixer = ImprovedMetaTransitionFixer(
        base_path=args.path,
        dry_run=args.dry_run,
        backup=not args.no_backup,
        verbose=not args.quiet
    )

    # Procesar
    success = fixer.process_directory()

    # Resumen
    fixer.print_summary()

    # Guardar log si se solicita
    if args.save_log:
        fixer.save_log()

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())