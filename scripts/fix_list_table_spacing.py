#!/usr/bin/env python3
"""
Script para corregir espaciado en directivas list-table

Ubicación: /tmp/ADT/scripts/fix_list_table_spacing.py

Uso desde /tmp/ADT:
    python3 scripts/fix_list_table_spacing.py source/**/*.rst

Añade línea en blanco entre opciones y contenido de list-table

Problema:
    .. list-table::
       :header-rows: 1
       * - Col1  ← falta línea en blanco
       
Solución:
    .. list-table::
       :header-rows: 1
       
       * - Col1  ← línea en blanco añadida

Creado: 2026-01-30 (Auditoría de scripts)
"""
import sys
import re

def fix_list_table_spacing(filepath):
    """Añade blank line entre opciones y contenido de list-table"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        result = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            result.append(line)
            
            # Detectar inicio de list-table
            if '.. list-table::' in line:
                i += 1
                
                # Procesar opciones (líneas que empiezan con :)
                while i < len(lines) and lines[i].strip().startswith(':'):
                    result.append(lines[i])
                    i += 1
                
                # Si la siguiente línea no está vacía y es contenido (* -)
                if i < len(lines):
                    next_line = lines[i].strip()
                    if next_line and next_line.startswith('*'):
                        # Añadir blank line antes del contenido
                        if result[-1].strip() != '':
                            result.append('\n')
                            modified = True
                continue
            
            i += 1
        
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
        print("Uso: python3 fix_list_table_spacing.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/fix_list_table_spacing.py source/**/*.rst")
        sys.exit(1)
    
    files = sys.argv[1:]
    files_modified = 0
    
    print(f"\n🔧 Procesando {len(files)} archivos...\n")
    
    for filepath in files:
        if filepath.endswith('.rst'):
            print(f"📄 {filepath}")
            if fix_list_table_spacing(filepath):
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
