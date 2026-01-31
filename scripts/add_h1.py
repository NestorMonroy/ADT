#!/usr/bin/env python3
"""
Script para añadir H1 a archivos Markdown que solo tienen frontmatter

Ubicación: /tmp/ADT/scripts/add_h1.py

Uso desde /tmp/ADT:
    python3 scripts/add_h1.py source/path/to/file.md
    python3 scripts/add_h1.py source/**/*.md

El script:
- Extrae el 'title' del frontmatter YAML
- Añade un H1 (#) después del frontmatter con ese título
- Acepta rutas relativas desde /tmp/ADT o absolutas

Ejemplo:
    python3 scripts/add_h1.py source/biblioteca/.../home.md

Creado: 2026-01-30 (Headers correction - FASE 2)
"""
import sys
import re

def add_h1_to_md(filepath):
    """Añade H1 después del frontmatter si no existe"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si ya tiene H1 (# título)
        if re.search(r'\n# .+\n', content):
            print(f"  ⏭️  Ya tiene H1: {filepath}")
            return False
        
        # Extraer frontmatter y encontrar title
        frontmatter_match = re.match(r'^---\n(.+?)\n---\n', content, re.DOTALL)
        if not frontmatter_match:
            print(f"  ❌ Sin frontmatter: {filepath}")
            return False
        
        frontmatter = frontmatter_match.group(1)
        
        # Buscar title en frontmatter
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)
        if not title_match:
            print(f"  ❌ Sin title en frontmatter: {filepath}")
            return False
        
        title = title_match.group(1).strip('"\'')
        
        # Añadir H1 después del frontmatter
        new_content = re.sub(
            r'^(---\n.+?\n---\n)',
            r'\1\n# ' + title + '\n',
            content,
            count=1,
            flags=re.DOTALL
        )
        
        # Guardar archivo modificado
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ H1 añadido: {filepath}")
        print(f"     Título: {title}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error procesando {filepath}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 add_h1.py <archivo1> [archivo2] ...")
        sys.exit(1)
    
    files = sys.argv[1:]
    total = len(files)
    success = 0
    
    print(f"\n📝 Procesando {total} archivos...\n")
    
    for filepath in files:
        if add_h1_to_md(filepath):
            success += 1
    
    print(f"\n✅ Resultado: {success}/{total} archivos modificados")
