#!/usr/bin/env python3
"""
Script para corregir espaciado antes de listas en RST

Ubicación: /tmp/ADT/scripts/fix_list_spacing.py

Uso desde /tmp/ADT:
    python3 scripts/fix_list_spacing.py source/**/*.rst

Añade línea en blanco antes de listas que siguen a un párrafo con ':'

Problema:
    Some text:
    - Item 1  ← falta línea en blanco
    
Solución:
    Some text:
    
    - Item 1  ← línea en blanco añadida

Creado: 2026-01-30 (Auditoría de scripts)
"""
import sys
import re

def fix_list_spacing(filepath):
    """Añade blank line antes de listas RST"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        result = []
        
        for i, line in enumerate(lines):
            result.append(line)
            
            # Detectar: línea termina con ':' y siguiente es una lista
            if i < len(lines) - 1:
                current_stripped = line.strip()
                next_stripped = lines[i + 1].strip()
                
                # Línea actual termina con ':' y no está vacía
                if current_stripped and current_stripped.endswith(':'):
                    # Siguiente línea es un item de lista (-, *, +, o numerado)
                    if (next_stripped.startswith(('-', '*', '+')) or 
                        re.match(r'^\d+\.', next_stripped)):
                        # Añadir línea en blanco si no existe
                        if line.strip() != '':  # Asegurar que no añadimos duplicados
                            result.append('\n')
                            modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(result)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 fix_list_spacing.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/fix_list_spacing.py source/**/*.rst")
        sys.exit(1)
    
    files = sys.argv[1:]
    files_modified = 0
    
    print(f"\n🔧 Procesando {len(files)} archivos...\n")
    
    for filepath in files:
        if filepath.endswith('.rst'):
            print(f"📄 {filepath}")
            if fix_list_spacing(filepath):
                print("  ✅ Espaciado corregido")
                files_modified += 1
            else:
                print("  ⏭️  Sin cambios")
        else:
            print(f"⏭️  {filepath} (no es RST)")
    
    print(f"\n✅ Resultado: {files_modified} archivos modificados")
    return 0

if __name__ == "__main__":
    sys.exit(main())
