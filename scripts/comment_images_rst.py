#!/usr/bin/env python3
"""
Script para comentar directivas de imagen en archivos RST

Ubicación: /tmp/ADT/scripts/comment_images_rst.py

Uso desde /tmp/ADT:
    python3 scripts/comment_images_rst.py source/path/to/file.rst
    python3 scripts/comment_images_rst.py source/**/*.rst

Comenta directivas de imagen que causan:
    WARNING: image file not readable

Directivas detectadas:
    - .. image:: ruta
    - .. figure:: ruta

Creado: 2026-01-31 (Corrección Imágenes - FASE 2)
"""
import sys
import re

def comment_image_directives(filepath):
    """Comenta directivas .. image:: y .. figure:: en RST"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        result = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Detectar directiva .. image:: o .. figure::
            if re.match(r'^\.\.\ (image|figure)::', line.strip()):
                # Comentar la directiva completa (directiva + opciones + contenido)
                result.append(f'.. {line.rstrip()}\n')
                modified = True
                i += 1
                
                # Comentar líneas de opciones y contenido (indentadas)
                while i < len(lines):
                    next_line = lines[i]
                    # Si la línea está indentada, es parte de la directiva
                    if next_line.strip() and not next_line.startswith(' '):
                        break
                    if next_line.strip():  # No comentar líneas vacías
                        result.append(f'..    {next_line.rstrip()}\n')
                        modified = True
                    else:
                        result.append(next_line)
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
        print("Uso: python3 comment_images_rst.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/comment_images_rst.py source/**/*.rst")
        sys.exit(1)
    
    files = sys.argv[1:]
    files_modified = 0
    
    print(f"\n🔧 Procesando {len(files)} archivos RST...\n")
    
    for filepath in files:
        if filepath.endswith('.rst'):
            print(f"📄 {filepath}")
            if comment_image_directives(filepath):
                print("  ✅ Directivas comentadas")
                files_modified += 1
            else:
                print("  ⏭️  Sin cambios")
        else:
            print(f"⏭️  {filepath} (no es RST)")
    
    print(f"\n✅ Resultado: {files_modified} archivos modificados")
    return 0

if __name__ == "__main__":
    sys.exit(main())
