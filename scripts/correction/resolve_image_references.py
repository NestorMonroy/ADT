#!/usr/bin/env python3
"""Resuelve referencias de imágenes que no se encuentran.

Lote: L7 - Missing Images (142 WARNING issues)
"""

import argparse
import re
import sys
from pathlib import Path


def resolve_image_refs(content: str, base_path: Path) -> str:
    """Resuelve referencias de imágenes."""
    # Patrón para detectar directivas image y figure
    pattern = re.compile(r'^\.\. (image|figure)::\s*(.+)$', re.MULTILINE)
    
    def fix_path(match):
        directive = match.group(1)
        img_path = match.group(2).strip()
        
        # Eliminar variables de template
        if '{{' in img_path:
            img_path = re.sub(r'\{\{site\.(imageurl|baseurl|url)\}\}/', '', img_path)
        
        # Normalizar path
        img_path = img_path.replace('//', '/')
        
        return f'.. {directive}:: {img_path}'
    
    return pattern.sub(fix_path, content)


def main() -> int:
    parser = argparse.ArgumentParser(description='Resuelve referencias de imágenes')
    parser.add_argument('path', type=Path)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()
    
    files = [args.path] if args.path.is_file() else sorted(
        args.path.glob('**/*.rst' if args.recursive else '*.rst')
    )
    
    print(f"resolve_image_references.py - {'APLICANDO' if args.apply else 'DRY RUN'}")
    
    for file_path in files:
        content = file_path.read_text(encoding='utf-8')
        fixed = resolve_image_refs(content, file_path.parent)
        
        if content != fixed:
            print(f"📄 {file_path}")
            if args.apply:
                file_path.write_text(fixed, encoding='utf-8')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
