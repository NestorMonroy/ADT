#!/usr/bin/env python3
"""
Script para encontrar entradas duplicadas en toctree de archivos RST

Ubicación: /tmp/ADT/scripts/find_duplicate_toctree.py

Uso desde /tmp/ADT:
    python3 scripts/find_duplicate_toctree.py source/**/*.rst
    python3 scripts/find_duplicate_toctree.py $(rg -l ".. toctree::" source)

Detecta referencias duplicadas en directivas toctree que causan:
    WARNING: toctree contains reference to document 'X' more than once

Creado: 2026-01-30 (Auditoría de scripts)
"""
import sys
import re
from collections import defaultdict

def find_duplicate_toctree(filepaths):
    """Encuentra entradas duplicadas en toctree"""
    
    duplicates_found = []
    
    for filepath in filepaths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Buscar bloques toctree
            toctree_pattern = re.compile(
                r'\.\. toctree::\s*\n((?:\s+:[^\n]+\n)*)((?:\s+[^\n]+\n)*)',
                re.MULTILINE
            )
            
            for match in toctree_pattern.finditer(content):
                options = match.group(1)
                entries = match.group(2)
                
                # Extraer entradas (líneas con indentación que no son opciones)
                entry_list = []
                for line in entries.split('\n'):
                    line = line.strip()
                    if line and not line.startswith(':'):
                        entry_list.append(line)
                
                # Buscar duplicados
                seen = {}
                for entry in entry_list:
                    if entry in seen:
                        duplicates_found.append({
                            'file': filepath,
                            'entry': entry,
                            'first': seen[entry],
                            'duplicate': entry_list.index(entry, seen[entry] + 1)
                        })
                    else:
                        seen[entry] = entry_list.index(entry)
                        
        except Exception as e:
            print(f"⚠️  Error leyendo {filepath}: {e}", file=sys.stderr)
    
    return duplicates_found

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 find_duplicate_toctree.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/find_duplicate_toctree.py $(rg -l '.. toctree::' source)")
        sys.exit(1)
    
    files = sys.argv[1:]
    duplicates = find_duplicate_toctree(files)
    
    if not duplicates:
        print("✅ No se encontraron entradas duplicadas en toctree")
        return 0
    
    print(f"\n⚠️  Encontradas {len(duplicates)} entradas duplicadas en toctree:\n")
    
    for dup in duplicates:
        print(f"Archivo: {dup['file']}")
        print(f"  Entrada duplicada: '{dup['entry']}'")
        print()
    
    print(f"Total: {len(duplicates)} duplicados")
    return 1

if __name__ == "__main__":
    sys.exit(main())
