#!/usr/bin/env python3
"""
Analizador de logs de Sphinx build
Categoriza y cuenta errores, warnings y critical
"""

import re
from collections import defaultdict
from datetime import datetime

def analyze_log(log_file):
    """Analiza el archivo de log y genera estadísticas"""
    
    warnings = []
    errors = []
    criticals = []
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if 'WARNING:' in line:
                warnings.append(line.strip())
            elif 'ERROR:' in line:
                errors.append(line.strip())
            elif 'CRITICAL:' in line:
                criticals.append(line.strip())
    
    # Categorizar warnings
    warning_categories = defaultdict(list)
    for w in warnings:
        # Extraer categoría del warning
        if 'duplicate label' in w:
            warning_categories['Duplicate Labels'].append(w)
        elif 'Document headings start at' in w:
            warning_categories['Document Heading Levels'].append(w)
        elif 'image file not readable' in w:
            warning_categories['Missing Images'].append(w)
        elif 'Pygments lexer' in w:
            warning_categories['Pygments Lexer'].append(w)
        elif 'term not in glossary' in w:
            warning_categories['Glossary Terms'].append(w)
        elif 'Enumerated list ends' in w or 'Bullet list ends' in w:
            warning_categories['List Formatting'].append(w)
        elif 'toctree' in w:
            warning_categories['TOC Tree'].append(w)
        elif 'Title' in w and ('overline' in w or 'underline' in w):
            warning_categories['Title Formatting'].append(w)
        elif 'Non-consecutive header' in w:
            warning_categories['Header Levels'].append(w)
        elif 'Lexing literal_block' in w:
            warning_categories['Code Block Lexing'].append(w)
        elif 'Explicit markup ends' in w:
            warning_categories['Markup Formatting'].append(w)
        elif 'Block quote ends' in w:
            warning_categories['Quote Formatting'].append(w)
        elif 'Inline' in w and ('start-string' in w or 'end-string' in w):
            warning_categories['Inline Markup'].append(w)
        elif 'failed to reach any of the inventories' in w:
            warning_categories['Intersphinx'].append(w)
        else:
            warning_categories['Other'].append(w)
    
    # Categorizar errors
    error_categories = defaultdict(list)
    for e in errors:
        if 'Unknown directive' in e:
            error_categories['Unknown Directives'].append(e)
        elif 'Unknown interpreted text role' in e:
            error_categories['Unknown Roles'].append(e)
        elif 'Error parsing content block' in e:
            error_categories['Content Block Parsing'].append(e)
        elif 'Unexpected indentation' in e or 'Unexpected unindent' in e:
            error_categories['Indentation'].append(e)
        elif 'Document or section may not begin' in e:
            error_categories['Document Structure'].append(e)
        elif 'Unknown target name' in e:
            error_categories['Unknown Targets'].append(e)
        elif 'Content block expected' in e:
            error_categories['Missing Content'].append(e)
        else:
            error_categories['Other'].append(e)
    
    # Categorizar criticals
    critical_categories = defaultdict(list)
    for c in criticals:
        if 'Unexpected section title' in c:
            critical_categories['Section Title Issues'].append(c)
        elif 'Missing matching underline' in c:
            critical_categories['Title Underline'].append(c)
        else:
            critical_categories['Other'].append(c)
    
    return {
        'warnings': warnings,
        'errors': errors,
        'criticals': criticals,
        'warning_categories': warning_categories,
        'error_categories': error_categories,
        'critical_categories': critical_categories
    }

def generate_report(stats, output_file):
    """Genera reporte en formato markdown"""
    
    total_warnings = len(stats['warnings'])
    total_errors = len(stats['errors'])
    total_criticals = len(stats['criticals'])
    total_issues = total_warnings + total_errors + total_criticals
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Reporte de Build - Sphinx HTML\n\n")
        f.write(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Proyecto:** ADT Documentation\n\n")
        
        f.write("## Resumen Ejecutivo\n\n")
        f.write(f"- **Total de Issues:** {total_issues}\n")
        f.write(f"- **Errores (ERROR):** {total_errors}\n")
        f.write(f"- **Críticos (CRITICAL):** {total_criticals}\n")
        f.write(f"- **Advertencias (WARNING):** {total_warnings}\n")
        f.write(f"- **Estado del Build:** {'✅ EXITOSO' if total_errors == 0 else '❌ FALLIDO'}\n\n")
        
        # Warnings por categoría
        if stats['warning_categories']:
            f.write("## Warnings por Categoría\n\n")
            f.write("| Categoría | Cantidad |\n")
            f.write("|-----------|----------|\n")
            for cat, items in sorted(stats['warning_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"| {cat} | {len(items)} |\n")
            f.write("\n")
        
        # Errors por categoría
        if stats['error_categories']:
            f.write("## Errors por Categoría\n\n")
            f.write("| Categoría | Cantidad |\n")
            f.write("|-----------|----------|\n")
            for cat, items in sorted(stats['error_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"| {cat} | {len(items)} |\n")
            f.write("\n")
        
        # Criticals por categoría
        if stats['critical_categories']:
            f.write("## Criticals por Categoría\n\n")
            f.write("| Categoría | Cantidad |\n")
            f.write("|-----------|----------|\n")
            for cat, items in sorted(stats['critical_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"| {cat} | {len(items)} |\n")
            f.write("\n")
        
        # Detalles de Errors
        if stats['error_categories']:
            f.write("## Detalle de Errors\n\n")
            for cat, items in sorted(stats['error_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"### {cat} ({len(items)})\n\n")
                # Mostrar primeros 10 ejemplos
                for item in items[:10]:
                    f.write(f"```\n{item}\n```\n\n")
                if len(items) > 10:
                    f.write(f"*... y {len(items) - 10} más*\n\n")
        
        # Detalles de Criticals
        if stats['critical_categories']:
            f.write("## Detalle de Criticals\n\n")
            for cat, items in sorted(stats['critical_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"### {cat} ({len(items)})\n\n")
                for item in items[:10]:
                    f.write(f"```\n{item}\n```\n\n")
                if len(items) > 10:
                    f.write(f"*... y {len(items) - 10} más*\n\n")
        
        # Top 5 categorías de warnings con ejemplos
        f.write("## Top 5 Categorías de Warnings (con ejemplos)\n\n")
        sorted_warnings = sorted(stats['warning_categories'].items(), key=lambda x: len(x[1]), reverse=True)
        for cat, items in sorted_warnings[:5]:
            f.write(f"### {cat} ({len(items)})\n\n")
            # Mostrar primeros 5 ejemplos únicos
            unique_examples = []
            for item in items:
                # Extraer el mensaje sin la ruta del archivo
                msg = re.sub(r'^.*?WARNING:', 'WARNING:', item)
                if msg not in unique_examples:
                    unique_examples.append(msg)
                if len(unique_examples) >= 5:
                    break
            
            for ex in unique_examples:
                f.write(f"```\n{ex}\n```\n\n")
        
        # Recomendaciones
        f.write("## Recomendaciones\n\n")
        
        if total_errors > 0:
            f.write("### ⚠️ PRIORIDAD ALTA - Errores\n\n")
            f.write("Los siguientes errores deben corregirse:\n\n")
            for cat, items in sorted(stats['error_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"- **{cat}**: {len(items)} ocurrencias\n")
            f.write("\n")
        
        if total_criticals > 0:
            f.write("### ⚠️ PRIORIDAD ALTA - Críticos\n\n")
            f.write("Los siguientes problemas críticos deben corregirse:\n\n")
            for cat, items in sorted(stats['critical_categories'].items(), key=lambda x: len(x[1]), reverse=True):
                f.write(f"- **{cat}**: {len(items)} ocurrencias\n")
            f.write("\n")
        
        if total_warnings > 0:
            f.write("### 📝 PRIORIDAD MEDIA - Warnings\n\n")
            f.write("Se recomienda revisar y corregir los siguientes warnings:\n\n")
            sorted_warn = sorted(stats['warning_categories'].items(), key=lambda x: len(x[1]), reverse=True)
            for cat, items in sorted_warn[:5]:
                f.write(f"- **{cat}**: {len(items)} ocurrencias\n")
            f.write("\n")
        
        f.write("## Siguiente Paso\n\n")
        if total_errors == 0 and total_criticals == 0:
            f.write("✅ El build fue exitoso. Los warnings son opcionales pero se recomienda revisarlos.\n\n")
            f.write("Puedes proceder con el commit o continuar mejorando la documentación.\n")
        else:
            f.write("❌ El build tiene errores críticos que deben corregirse antes de continuar.\n\n")
            f.write("Revisa los detalles arriba y corrige los problemas indicados.\n")

if __name__ == '__main__':
    print("Analizando build_output.log...")
    stats = analyze_log('/tmp/build_output.log')
    
    print(f"\nEstadísticas:")
    print(f"  Warnings: {len(stats['warnings'])}")
    print(f"  Errors: {len(stats['errors'])}")
    print(f"  Criticals: {len(stats['criticals'])}")
    
    output_file = '/tmp/ADT/build_validation_report.md'
    generate_report(stats, output_file)
    print(f"\n✅ Reporte generado: {output_file}")
