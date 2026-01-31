#!/usr/bin/env python3
"""
Script para corregir indentación en directivas glossary

Ubicación: /tmp/ADT/scripts/fix_glossary_indentation.py

Uso desde /tmp/ADT:
    python3 scripts/fix_glossary_indentation.py source/**/*.rst

Corrige indentación en glossary:
    - Términos: 2 espacios
    - Definiciones: 4 espacios

Problema:
    .. glossary::
    
    Term
     Definition  ← indentación incorrecta

Solución:
    .. glossary::
    
      Term          ← 2 espacios
          Definition ← 4 espacios

Creado: 2026-01-30 (Auditoría de scripts)
"""
import sys
import re

def fix_glossary_indentation(filepath):
    """Corrige indentación en directivas glossary"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        result = []
        i = 0
        in_glossary = False
        
        while i < len(lines):
            line = lines[i]
            
            # Detectar inicio de glossary
            if '.. glossary::' in line:
                result.append(line)
                in_glossary = True
                i += 1
                
                # Saltar línea en blanco después de glossary
                if i < len(lines) and lines[i].strip() == '':
                    result.append(lines[i])
                    i += 1
                
                # Procesar términos y definiciones
                while i < len(lines):
                    current = lines[i]
                    
                    # Fin del glossary (línea sin indentación o nueva directiva)
                    if current.strip() and not current.startswith(' '):
                        in_glossary = False
                        break
                    
                    if current.strip() == '':
                        result.append(current)
                        i += 1
                        continue
                    
                    # Detectar si es término o definición
                    indent = len(current) - len(current.lstrip())
                    content = current.strip()
                    
                    if indent == 0 or (indent > 0 and indent < 3):
                        # Es un término - debe tener 2 espacios
                        result.append('  ' + content + '\n')
                        modified = True if indent != 2 else modified
                    else:
                        # Es una definición - debe tener 4 espacios
                        result.append('    ' + content + '\n')
                        modified = True if indent != 4 else modified
                    
                    i += 1
                
                continue
            
            result.append(line)
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
        print("Uso: python3 fix_glossary_indentation.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/fix_glossary_indentation.py source/**/*.rst")
        sys.exit(1)
    
    files = sys.argv[1:]
    files_modified = 0
    
    print(f"\n🔧 Procesando {len(files)} archivos...\n")
    
    for filepath in files:
        if filepath.endswith('.rst'):
            print(f"📄 {filepath}")
            if fix_glossary_indentation(filepath):
                print("  ✅ Indentación corregida")
                files_modified += 1
            else:
                print("  ⏭️  Sin cambios")
        else:
            print(f"⏭️  {filepath} (no es RST)")
    
    print(f"\n✅ Resultado: {files_modified} archivos modificados")
    return 0

if __name__ == "__main__":
    sys.exit(main())
