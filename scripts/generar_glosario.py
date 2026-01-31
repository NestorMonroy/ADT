#!/usr/bin/env python3
"""
Script para generar glosario automático desde archivos RST

Ubicación: /tmp/ADT/scripts/generar_glosario.py

Uso desde /tmp/ADT:
    python3 scripts/generar_glosario.py source/**/*.rst -o source/glosario.rst

Extrae términos del glossary existentes y genera un glosario consolidado

Creado: 2026-01-30 (Auditoría de scripts)
"""
import sys
import re
import argparse
from collections import OrderedDict

def extract_glossary_terms(filepath):
    """Extrae términos de glossary de un archivo RST"""
    terms = OrderedDict()
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Detectar inicio de glossary
            if '.. glossary::' in line:
                i += 1
                
                # Saltar línea en blanco
                if i < len(lines) and lines[i].strip() == '':
                    i += 1
                
                current_term = None
                current_definition = []
                
                # Procesar términos
                while i < len(lines):
                    current = lines[i]
                    
                    # Fin del glossary
                    if current.strip() and not current.startswith(' '):
                        if current_term:
                            terms[current_term] = ' '.join(current_definition)
                        break
                    
                    if current.strip() == '':
                        i += 1
                        continue
                    
                    indent = len(current) - len(current.lstrip())
                    content = current.strip()
                    
                    if indent <= 2:
                        # Guardar término anterior
                        if current_term:
                            terms[current_term] = ' '.join(current_definition)
                        
                        # Nuevo término
                        current_term = content
                        current_definition = []
                    else:
                        # Definición
                        current_definition.append(content)
                    
                    i += 1
                
                # Guardar último término
                if current_term:
                    terms[current_term] = ' '.join(current_definition)
                
                continue
            
            i += 1
    
    except Exception as e:
        print(f"⚠️  Error leyendo {filepath}: {e}", file=sys.stderr)
    
    return terms

def generate_glossary(input_files, output_file):
    """Genera glosario consolidado"""
    all_terms = OrderedDict()
    
    print(f"\n📚 Extrayendo términos de {len(input_files)} archivos...\n")
    
    for filepath in input_files:
        terms = extract_glossary_terms(filepath)
        if terms:
            print(f"  📄 {filepath}: {len(terms)} términos")
            # Merge terms (último gana si hay duplicados)
            all_terms.update(terms)
    
    if not all_terms:
        print("\n⚠️  No se encontraron términos de glosario")
        return 0
    
    # Generar archivo de salida
    print(f"\n✍️  Generando glosario en {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Glosario\n")
        f.write("========\n\n")
        f.write(".. glossary::\n\n")
        
        for term, definition in sorted(all_terms.items()):
            f.write(f"  {term}\n")
            f.write(f"    {definition}\n\n")
    
    print(f"✅ Glosario generado: {len(all_terms)} términos únicos")
    return 0

def main():
    parser = argparse.ArgumentParser(
        description='Generar glosario consolidado desde archivos RST'
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='Archivos RST a procesar'
    )
    parser.add_argument(
        '-o', '--output',
        default='glosario.rst',
        help='Archivo de salida (default: glosario.rst)'
    )
    
    args = parser.parse_args()
    
    return generate_glossary(args.files, args.output)

if __name__ == "__main__":
    sys.exit(main())
