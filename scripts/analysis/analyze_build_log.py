#!/usr/bin/env python3
"""Analiza logs de build de Sphinx y clasifica issues por severidad.

Este script procesa la salida de `make html` y genera estadísticas
detalladas de los errores y warnings encontrados.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


def parse_sphinx_log(log_content: str) -> Dict[str, List[Tuple[str, int, str]]]:
    """Parsea log de Sphinx y extrae issues.
    
    Args:
        log_content: Contenido del log
        
    Returns:
        Dict con estructura: {severity: [(file, line, message), ...]}
    """
    issues = defaultdict(list)
    
    # Patrón para detectar warnings/errors de Sphinx
    pattern = re.compile(
        r'(.+?\.rst):(\d+):\s*(WARNING|ERROR|CRITICAL):\s*(.+)',
        re.MULTILINE
    )
    
    for match in pattern.finditer(log_content):
        file_path = match.group(1)
        line_num = int(match.group(2))
        severity = match.group(3)
        message = match.group(4).strip()
        
        issues[severity].append((file_path, line_num, message))
    
    return dict(issues)


def categorize_issues(issues: Dict[str, List[Tuple[str, int, str]]]) -> Dict[str, Dict[str, int]]:
    """Categoriza issues por tipo de problema.
    
    Args:
        issues: Issues parseados
        
    Returns:
        Dict con categorización: {severity: {category: count}}
    """
    categories = defaultdict(lambda: defaultdict(int))
    
    category_patterns = {
        'section_structure': r'Unexpected section title',
        'title_underline': r'Title underline',
        'indentation': r'Unexpected indentation',
        'heading_levels': r'inconsistent with other.*heading',
        'content_parsing': r'Inline (strong|emphasis|literal)',
        'missing_content': r'Content block expected',
        'missing_images': r'image file not readable',
        'list_formatting': r'Bullet list ends without',
        'duplicate_labels': r'duplicate (label|explicit target)',
        'toctree': r'toctree',
    }
    
    for severity, issue_list in issues.items():
        for _, _, message in issue_list:
            categorized = False
            for category, pattern in category_patterns.items():
                if re.search(pattern, message, re.IGNORECASE):
                    categories[severity][category] += 1
                    categorized = True
                    break
            
            if not categorized:
                categories[severity]['other'] += 1
    
    return dict(categories)


def generate_report(issues: Dict, categories: Dict) -> str:
    """Genera reporte de issues.
    
    Args:
        issues: Issues parseados
        categories: Categorización de issues
        
    Returns:
        Reporte formateado
    """
    lines = []
    lines.append("=" * 70)
    lines.append("REPORTE DE ANÁLISIS DE BUILD SPHINX")
    lines.append("=" * 70)
    
    # Resumen por severidad
    lines.append("\n📊 RESUMEN POR SEVERIDAD")
    lines.append("-" * 70)
    total = 0
    for severity in ['CRITICAL', 'ERROR', 'WARNING']:
        count = len(issues.get(severity, []))
        total += count
        lines.append(f"{severity:12s}: {count:4d}")
    lines.append(f"{'TOTAL':12s}: {total:4d}")
    
    # Categorización
    lines.append("\n📋 CATEGORIZACIÓN")
    lines.append("-" * 70)
    for severity in ['CRITICAL', 'ERROR', 'WARNING']:
        if severity in categories and categories[severity]:
            lines.append(f"\n{severity}:")
            for category, count in sorted(categories[severity].items(), key=lambda x: -x[1]):
                lines.append(f"  {category:25s}: {count:4d}")
    
    # Top issues
    lines.append("\n🔝 TOP 10 ARCHIVOS CON MÁS ISSUES")
    lines.append("-" * 70)
    file_counts = defaultdict(int)
    for severity, issue_list in issues.items():
        for file_path, _, _ in issue_list:
            file_counts[file_path] += 1
    
    for file_path, count in sorted(file_counts.items(), key=lambda x: -x[1])[:10]:
        lines.append(f"{count:4d}  {file_path}")
    
    lines.append("\n" + "=" * 70)
    
    return "\n".join(lines)


def main() -> int:
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='Analiza logs de build de Sphinx'
    )
    parser.add_argument(
        'log_file',
        type=Path,
        nargs='?',
        help='Archivo de log (default: stdin)'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        help='Guardar reporte en archivo'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output en formato JSON'
    )
    
    args = parser.parse_args()
    
    # Leer log
    if args.log_file and args.log_file.exists():
        log_content = args.log_file.read_text(encoding='utf-8')
    else:
        log_content = sys.stdin.read()
    
    # Analizar
    issues = parse_sphinx_log(log_content)
    categories = categorize_issues(issues)
    
    # Generar reporte
    if args.json:
        import json
        report_data = {
            'summary': {sev: len(lst) for sev, lst in issues.items()},
            'categories': categories,
            'total': sum(len(lst) for lst in issues.values())
        }
        output = json.dumps(report_data, indent=2)
    else:
        output = generate_report(issues, categories)
    
    # Output
    if args.output:
        args.output.write_text(output, encoding='utf-8')
        print(f"✅ Reporte guardado en {args.output}")
    else:
        print(output)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
