#!/usr/bin/env python3
"""
Script para corregir lexers desconocidos en code-blocks RST y Markdown

Ubicación: /tmp/ADT/scripts/fix_unknown_lexers.py

Uso desde /tmp/ADT:
    python3 scripts/fix_unknown_lexers.py source/**/*.rst
    python3 scripts/fix_unknown_lexers.py source/**/*.md

Corrige WARNING:
    Pygments lexer name 'plantuml' is not known

Convierte lexers desconocidos a 'text':
    - plantuml → text
    - PlantUML → text
    - atl → text
    - ocl → text

Creado: 2026-01-30 (Auditoría de scripts)
Basado en: Corrección manual Lexers (Commits 42-45)
"""
import sys
import re

# Lexers conocidos problemáticos
UNKNOWN_LEXERS = ['plantuml', 'PlantUML', 'atl', 'ocl', 'ATL', 'OCL']

def fix_unknown_lexers_rst(filepath):
    """Corrige lexers desconocidos en archivos RST"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        # Patrón: .. code-block:: lexer_desconocido
        for lexer in UNKNOWN_LEXERS:
            pattern = re.compile(
                r'\.\. code-block:: ' + re.escape(lexer) + r'\b',
                re.IGNORECASE
            )
            matches = len(pattern.findall(content))
            if matches > 0:
                content = pattern.sub('.. code-block:: text', content)
                changes += matches
                print(f"  {lexer} → text: {matches} cambios")
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        
        return 0
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return 0

def fix_unknown_lexers_md(filepath):
    """Corrige lexers desconocidos en archivos Markdown"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        # Patrón: ```lexer_desconocido
        for lexer in UNKNOWN_LEXERS:
            pattern = re.compile(
                r'^```' + re.escape(lexer) + r'\b',
                re.MULTILINE | re.IGNORECASE
            )
            matches = len(pattern.findall(content))
            if matches > 0:
                content = pattern.sub('```text', content)
                changes += matches
                print(f"  {lexer} → text: {matches} cambios")
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        
        return 0
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return 0

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 fix_unknown_lexers.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/fix_unknown_lexers.py source/**/*.rst")
        print("  python3 scripts/fix_unknown_lexers.py source/**/*.md")
        sys.exit(1)
    
    files = sys.argv[1:]
    total_changes = 0
    files_modified = 0
    
    print(f"\n🔧 Procesando {len(files)} archivos...\n")
    
    for filepath in files:
        print(f"📄 {filepath}")
        
        if filepath.endswith('.rst'):
            changes = fix_unknown_lexers_rst(filepath)
        elif filepath.endswith('.md'):
            changes = fix_unknown_lexers_md(filepath)
        else:
            print("  ⏭️  Tipo de archivo no soportado")
            continue
        
        if changes > 0:
            print(f"  ✅ {changes} lexers corregidos")
            total_changes += changes
            files_modified += 1
        else:
            print("  ⏭️  Sin cambios")
    
    print(f"\n✅ Resultado: {files_modified} archivos modificados, {total_changes} lexers corregidos")
    return 0

if __name__ == "__main__":
    sys.exit(main())
