#!/usr/bin/env python3
"""Corrige errores de indentación en listas y bloques.

Lote: L3 - Indentation (28 ERROR issues)
"""

import argparse
import re
import sys
from pathlib import Path


def fix_indentation(content: str) -> str:
    """Corrige indentación en continuaciones de items de lista."""
    lines = content.split('\n')
    result = []
    
    list_pattern = re.compile(r'^(\s*)([*\-+]|\d+\.)\s+')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        match = list_pattern.match(line)
        
        if match:
            # Item de lista encontrado
            indent = len(match.group(1))
            result.append(line)
            
            # Procesar líneas siguientes (continuación)
            i += 1
            while i < len(lines) and lines[i] and not list_pattern.match(lines[i]):
                continuation = lines[i]
                if continuation.strip() and not continuation.startswith(' ' * (indent + 2)):
                    # Corregir indentación de continuación
                    continuation = ' ' * (indent + 2) + continuation.lstrip()
                result.append(continuation)
                i += 1
            continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)


def main() -> int:
    parser = argparse.ArgumentParser(description='Corrige errores de indentación')
    parser.add_argument('path', type=Path)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()
    
    files = [args.path] if args.path.is_file() else sorted(
        args.path.glob('**/*.rst' if args.recursive else '*.rst')
    )
    
    print(f"fix_indentation_errors.py - {'APLICANDO' if args.apply else 'DRY RUN'}")
    
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        fixed = fix_indentation(content)
        
        if content != fixed:
            print(f"📄 {file_path}")
            if args.apply:
                file_path.write_text(fixed, encoding='utf-8')
                print("   ✅ Corregido")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
