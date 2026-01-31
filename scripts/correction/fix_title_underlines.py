#!/usr/bin/env python3
"""Corrige underlines de títulos que no coinciden en longitud.

Lote: L2 - Title Underlines (8 CRITICAL issues)
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple

try:
    from scripts.lib.regex_patterns import is_valid_underline
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from scripts.lib.regex_patterns import is_valid_underline


def fix_title_underlines(content: str) -> str:
    """Corrige underlines para que coincidan con títulos."""
    lines = content.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        current = lines[i]
        next_line = lines[i + 1] if i + 1 < len(lines) else ''
        
        if is_valid_underline(next_line):
            title_len = len(current.rstrip())
            underline_char = next_line.strip()[0]
            correct_underline = underline_char * title_len
            
            result.append(current)
            result.append(correct_underline)
            i += 2
            continue
        
        result.append(current)
        i += 1
    
    return '\n'.join(result)


def process_file(file_path: Path, dry_run: bool = True) -> int:
    """Procesa archivo."""
    content = file_path.read_text(encoding='utf-8')
    fixed = fix_title_underlines(content)
    
    if content != fixed:
        print(f"📄 {file_path} - CAMBIOS DETECTADOS")
        if not dry_run:
            file_path.write_text(fixed, encoding='utf-8')
            print("   ✅ Corregido")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Corrige underlines de títulos')
    parser.add_argument('path', type=Path)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()
    
    files = [args.path] if args.path.is_file() else sorted(
        args.path.glob('**/*.rst' if args.recursive else '*.rst')
    )
    
    print(f"fix_title_underlines.py - {'APLICANDO' if args.apply else 'DRY RUN'}")
    changed = sum(process_file(f, not args.apply) for f in files)
    print(f"\nArchivos con cambios: {changed}/{len(files)}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
