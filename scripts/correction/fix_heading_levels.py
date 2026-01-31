#!/usr/bin/env python3
"""Normaliza niveles de encabezados.

Lote: L6 - Heading Levels (339 WARNING issues)
"""

import argparse
import sys
from pathlib import Path

try:
    from scripts.lib.regex_patterns import is_valid_underline, HEADING_CHARS
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from scripts.lib.regex_patterns import is_valid_underline, HEADING_CHARS


def get_underline_char_for_level(level: int) -> str:
    """Retorna el carácter de underline para un nivel."""
    return HEADING_CHARS.get(level, '-')


def normalize_heading_levels(content: str) -> str:
    """Normaliza niveles comenzando desde H1."""
    lines = content.split('\n')
    result = []
    current_level = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        next_line = lines[i + 1] if i + 1 < len(lines) else ''
        
        if is_valid_underline(next_line):
            # Incrementar nivel
            if current_level == 0:
                current_level = 1
            
            # Reescribir con underline correcto
            char = get_underline_char_for_level(current_level)
            underline = char * len(line.rstrip())
            
            result.append(line)
            result.append(underline)
            i += 2
            continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)


def main() -> int:
    parser = argparse.ArgumentParser(description='Normaliza niveles de encabezados')
    parser.add_argument('path', type=Path)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()
    
    files = [args.path] if args.path.is_file() else sorted(
        args.path.glob('**/*.rst' if args.recursive else '*.rst')
    )
    
    print(f"fix_heading_levels.py - {'APLICANDO' if args.apply else 'DRY RUN'}")
    
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        fixed = normalize_heading_levels(content)
        
        if content != fixed:
            print(f"📄 {file_path}")
            if args.apply:
                file_path.write_text(fixed, encoding='utf-8')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
