#!/usr/bin/env python3
"""
Script para comentar directivas de imagen en archivos Markdown

Ubicación: /tmp/ADT/scripts/comment_images.py

Uso desde /tmp/ADT:
    python3 scripts/comment_images.py source/path/to/file.md
    python3 scripts/comment_images.py source/**/*.md

Comenta líneas con imágenes que causan:
    WARNING: image file not readable

Patrones detectados:
    - ![...](...) con {{site.imageurl}}
    - ![...](...) con rutas %7B%7B
    - Otras imágenes con rutas no existentes

Creado: 2026-01-31 (Corrección Imágenes - FASE 2)
"""
import sys
import re

def comment_image_lines(filepath):
    """Comenta líneas con imágenes problemáticas en Markdown"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        result = []
        
        for line in lines:
            # Detectar líneas con imágenes Markdown
            # Patrón: ![alt](ruta)
            if re.search(r'!\[.*?\]\(.*?\)', line):
                # Verificar si contiene patrones problemáticos
                if any(pattern in line for pattern in [
                    '{{site.imageurl}}',
                    '%7B%7B',
                    'images/',  # Rutas relativas problemáticas
                ]):
                    # Comentar la línea
                    if not line.strip().startswith('<!--'):
                        result.append(f'<!-- {line.rstrip()} -->\n')
                        modified = True
                    else:
                        result.append(line)
                else:
                    result.append(line)
            else:
                result.append(line)
        
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
        print("Uso: python3 comment_images.py <archivo1> [archivo2] ...")
        print("\nEjemplo:")
        print("  python3 scripts/comment_images.py source/**/*.md")
        sys.exit(1)
    
    files = sys.argv[1:]
    files_modified = 0
    
    print(f"\n🔧 Procesando {len(files)} archivos...\n")
    
    for filepath in files:
        if filepath.endswith('.md'):
            print(f"📄 {filepath}")
            if comment_image_lines(filepath):
                print("  ✅ Imágenes comentadas")
                files_modified += 1
            else:
                print("  ⏭️  Sin cambios")
        else:
            print(f"⏭️  {filepath} (no es MD)")
    
    print(f"\n✅ Resultado: {files_modified} archivos modificados")
    return 0

if __name__ == "__main__":
    sys.exit(main())
