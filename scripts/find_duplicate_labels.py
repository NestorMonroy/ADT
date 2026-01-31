#!/usr/bin/env python3
"""
Script para encontrar labels duplicados en archivos RST/MD

Ubicación: /tmp/ADT/scripts/find_duplicate_labels.py

Uso desde /tmp/ADT:
    python3 scripts/find_duplicate_labels.py source/**/*.rst
    python3 scripts/find_duplicate_labels.py $(rg -l "^.. _" source)

Detecta labels duplicados que causan:
    WARNING: duplicate label [label_name]

Creado: 2026-01-30 (Auditoría de scripts)
"""
import sys
import re
from collections import defaultdict

def find_duplicate_labels(filepaths):
    """Encuentra labels duplicados en archivos RST/MD"""
    
    labels = defaultdict(list)
    
    # Patrón para labels RST: .. _label:
    rst_label_pattern = re.compile(r'^\.\. _([a-zA-Z0-9_-]+):')
    
    # Patrón para labels MyST (Markdown): (label)=
    myst_label_pattern = re.compile(r'^\(([a-zA-Z0-9_-]+)\)=')
    
    for filepath in filepaths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    # Buscar labels RST
                    rst_match = rst_label_pattern.match(line)
                    if rst_match:
                        label = rst_match.group(1)
                        labels[label].append((filepath, line_num, 'RST'))
                    
                    # Buscar labels MyST
                    myst_match = myst_label_pattern.match(line)
                    if myst_match:
                        label = myst_match.group(1)
                        labels[label].append((filepath, line_num, 'MyST'))
                        
        except Exception as e:
            print(f"⚠️  Error leyendo {filepath}: {e}", file=sys.stderr)
    
    return labels

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 find_duplicate_labels.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/find_duplicate_labels.py $(rg -l '^.. _' source)")
        sys.exit(1)
    
    files = sys.argv[1:]
    labels = find_duplicate_labels(files)
    
    # Encontrar duplicados
    duplicates = {label: locations for label, locations in labels.items() if len(locations) > 1}
    
    if not duplicates:
        print("✅ No se encontraron labels duplicados")
        return 0
    
    print(f"\n⚠️  Encontrados {len(duplicates)} labels duplicados:\n")
    
    for label, locations in sorted(duplicates.items()):
        print(f"Label: '{label}' ({len(locations)} ocurrencias)")
        for filepath, line_num, label_type in locations:
            print(f"  - {filepath}:{line_num} ({label_type})")
        print()
    
    print(f"Total: {len(duplicates)} labels duplicados")
    return 1

if __name__ == "__main__":
    sys.exit(main())
