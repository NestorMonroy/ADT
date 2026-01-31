#!/usr/bin/env python3
"""
Script para ajustar headers consecutivos en archivos Markdown después de añadir H1

Ubicación: /tmp/ADT/scripts/adjust_headers.py

Problema que resuelve:
    Después de añadir H1, puede haber saltos no consecutivos:
    # H1 Título
    ### H3 Subsección  ← Salta de H1 a H3 (WARNING)

Solución:
    Convierte H3 → H2, H4 → H3 para hacer headers consecutivos

Uso desde /tmp/ADT:
    python3 scripts/adjust_headers.py source/path/to/file.md
    python3 scripts/adjust_headers.py source/**/*.md

El script acepta rutas relativas desde /tmp/ADT o absolutas.

Ejemplo:
    python3 scripts/adjust_headers.py source/biblioteca/.../section-10.md

Creado: 2026-01-30 (Headers correction - FASE 2)
"""
import sys
import re

def adjust_headers(filepath):
    """Ajusta headers para que sean consecutivos después de H1"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si tiene H1
        if not re.search(r'^# .+', content, re.MULTILINE):
            print(f"  ⏭️  Sin H1: {filepath}")
            return False
        
        original_content = content
        
        # Estrategia: Reducir un nivel a todos los headers
        # H4 (####) → H3 (###)
        # H3 (###) → H2 (##)
        # H2 (##) se mantiene como H2
        # H1 (#) se mantiene como H1
        
        lines = content.split('\n')
        adjusted_lines = []
        
        for line in lines:
            # Si es un header de Markdown (empieza con #)
            if re.match(r'^#{2,4} ', line):
                # Contar cuántos # tiene
                hash_count = len(re.match(r'^#+', line).group())
                
                if hash_count == 4:
                    # #### → ###
                    line = line.replace('####', '###', 1)
                elif hash_count == 3:
                    # ### → ##
                    line = line.replace('###', '##', 1)
                # H2 (##) se mantiene
                # H1 (#) se mantiene
            
            adjusted_lines.append(line)
        
        new_content = '\n'.join(adjusted_lines)
        
        if new_content == original_content:
            print(f"  ⏭️  Sin cambios: {filepath}")
            return False
        
        # Guardar archivo modificado
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Headers ajustados: {filepath}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error procesando {filepath}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 adjust_headers.py <archivo1> [archivo2] ...")
        sys.exit(1)
    
    files = sys.argv[1:]
    total = len(files)
    success = 0
    
    print(f"\n📝 Procesando {total} archivos...\n")
    
    for filepath in files:
        if adjust_headers(filepath):
            success += 1
    
    print(f"\n✅ Resultado: {success}/{total} archivos modificados")
