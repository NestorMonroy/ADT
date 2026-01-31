#!/usr/bin/env python3
"""Script para corregir estructura de secciones (unexpected section title).

Este script corrige el error "WARNING: Unexpected section title" que ocurre
cuando un título no tiene una línea en blanco antes del underline.

Lote: L1 - Section Structure (25 CRITICAL issues)
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple, Optional

# Imports con fallback para ejecución directa o como módulo
try:
    from scripts.lib.regex_patterns import TITLE_WITH_UNDERLINE, is_valid_underline
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from scripts.lib.regex_patterns import TITLE_WITH_UNDERLINE, is_valid_underline


def detect_section_structure_issues(content: str) -> List[Tuple[int, str, str]]:
    """Detecta títulos sin línea en blanco antes.
    
    Args:
        content: Contenido del archivo RST
        
    Returns:
        Lista de tuplas (line_number, title, underline_char)
    """
    lines = content.split('\n')
    issues = []
    
    i = 0
    while i < len(lines) - 1:
        current_line = lines[i]
        next_line = lines[i + 1] if i + 1 < len(lines) else ''
        
        # Detectar si next_line es underline válido
        if is_valid_underline(next_line):
            # Verificar si hay línea en blanco antes
            if i > 0 and lines[i - 1].strip() != '':
                # Issue: no hay línea en blanco antes del título
                underline_char = next_line.strip()[0] if next_line.strip() else '-'
                issues.append((i + 1, current_line, underline_char))
        
        i += 1
    
    return issues


def fix_section_structure(content: str) -> str:
    """Corrige estructura de secciones añadiendo líneas en blanco.
    
    Args:
        content: Contenido original
        
    Returns:
        Contenido corregido
    """
    lines = content.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        current_line = lines[i]
        next_line = lines[i + 1] if i + 1 < len(lines) else ''
        
        # Detectar título con underline
        if is_valid_underline(next_line):
            # Verificar si hay línea en blanco antes
            if i > 0 and lines[i - 1].strip() != '':
                # Añadir línea en blanco antes del título
                result.append('')
        
        result.append(current_line)
        i += 1
    
    return '\n'.join(result)


def process_file(file_path: Path, dry_run: bool = True) -> Tuple[int, int]:
    """Procesa un archivo RST.
    
    Args:
        file_path: Ruta al archivo
        dry_run: Si True, solo muestra cambios sin aplicar
        
    Returns:
        Tupla (issues_encontrados, issues_corregidos)
    """
    if not file_path.exists():
        print(f"ERROR: Archivo no encontrado: {file_path}")
        return 0, 0
    
    content = file_path.read_text(encoding='utf-8')
    issues = detect_section_structure_issues(content)
    
    if not issues:
        return 0, 0
    
    print(f"\n📄 {file_path}")
    print(f"   Issues encontrados: {len(issues)}")
    
    for line_num, title, _ in issues:
        print(f"   L{line_num}: '{title}'")
    
    if not dry_run:
        fixed_content = fix_section_structure(content)
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"   ✅ Corregido")
        return len(issues), len(issues)
    else:
        print(f"   ⚠️  DRY RUN - no se aplicaron cambios")
        return len(issues), 0
    
    return len(issues), 0


def main() -> int:
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='Corrige estructura de secciones (unexpected section title)'
    )
    parser.add_argument(
        'path',
        type=Path,
        help='Archivo o directorio a procesar'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Aplicar cambios (default: dry-run)'
    )
    parser.add_argument(
        '--recursive',
        '-r',
        action='store_true',
        help='Procesar directorios recursivamente'
    )
    
    args = parser.parse_args()
    
    dry_run = not args.apply
    mode_str = "DRY RUN" if dry_run else "APLICANDO CAMBIOS"
    
    print(f"{'='*60}")
    print(f"fix_section_structure.py - {mode_str}")
    print(f"{'='*60}")
    
    # Recolectar archivos
    files_to_process = []
    if args.path.is_file():
        if args.path.suffix == '.rst':
            files_to_process.append(args.path)
    elif args.path.is_dir():
        pattern = '**/*.rst' if args.recursive else '*.rst'
        files_to_process = sorted(args.path.glob(pattern))
    
    if not files_to_process:
        print(f"⚠️  No se encontraron archivos RST en {args.path}")
        return 1
    
    print(f"\nArchivos a procesar: {len(files_to_process)}")
    
    # Procesar archivos
    total_issues = 0
    total_fixed = 0
    
    for file_path in files_to_process:
        found, fixed = process_file(file_path, dry_run)
        total_issues += found
        total_fixed += fixed
    
    # Resumen
    print(f"\n{'='*60}")
    print(f"RESUMEN")
    print(f"{'='*60}")
    print(f"Issues encontrados: {total_issues}")
    print(f"Issues corregidos:  {total_fixed}")
    
    if dry_run and total_issues > 0:
        print(f"\n💡 Ejecuta con --apply para aplicar los cambios")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
