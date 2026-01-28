#!/usr/bin/env python3
"""
Analizador de Sección Markdown para arc42
==========================================

Analiza archivos .md de una sección arc42 e identifica:
- Estructura jerárquica (headings)
- Elementos especiales (imágenes, tablas, código, enlaces)
- Front matter YAML
- Estadísticas de contenido

Uso:
    python analizar_seccion.py <ruta_seccion>
    
Ejemplo:
    python analizar_seccion.py sections/02_constraints
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field
import yaml
import json

@dataclass
class ArchivoAnalisis:
    """Resultado del análisis de un archivo markdown"""
    ruta: str
    nombre: str
    lineas: int = 0
    palabras: int = 0
    caracteres: int = 0
    
    # Front matter
    tiene_frontmatter: bool = False
    frontmatter: Dict = field(default_factory=dict)
    
    # Estructura
    headings: List[Tuple[int, str]] = field(default_factory=list)  # (nivel, texto)
    
    # Elementos especiales
    imagenes: List[str] = field(default_factory=list)
    tablas: int = 0
    bloques_codigo: List[str] = field(default_factory=list)  # tipo/lenguaje
    enlaces: List[Tuple[str, str]] = field(default_factory=list)  # (texto, url)
    
    # HTML/divs
    divs_html: List[str] = field(default_factory=list)  # clases de divs
    
    # Listas
    listas_bullet: int = 0
    listas_numeradas: int = 0

def extraer_frontmatter(contenido: str) -> Tuple[Dict, str]:
    """
    Extrae front matter YAML y retorna (frontmatter_dict, contenido_sin_frontmatter)
    """
    # Buscar front matter entre --- ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', contenido, re.DOTALL)
    
    if match:
        try:
            frontmatter_text = match.group(1)
            contenido_resto = match.group(2)
            frontmatter_dict = yaml.safe_load(frontmatter_text)
            return frontmatter_dict or {}, contenido_resto
        except yaml.YAMLError:
            return {}, contenido
    
    return {}, contenido

def analizar_archivo(ruta: Path) -> ArchivoAnalisis:
    """
    Analiza un archivo markdown y retorna ArchivoAnalisis
    """
    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    resultado = ArchivoAnalisis(
        ruta=str(ruta),
        nombre=ruta.name
    )
    
    # Extraer front matter
    frontmatter, contenido_sin_fm = extraer_frontmatter(contenido)
    if frontmatter:
        resultado.tiene_frontmatter = True
        resultado.frontmatter = frontmatter
    
    # Estadísticas básicas
    lineas = contenido.split('\n')
    resultado.lineas = len(lineas)
    resultado.palabras = len(contenido.split())
    resultado.caracteres = len(contenido)
    
    # Headings (# ## ### etc)
    for linea in lineas:
        match = re.match(r'^(#{1,6})\s+(.+)$', linea)
        if match:
            nivel = len(match.group(1))
            texto = match.group(2).strip()
            resultado.headings.append((nivel, texto))
    
    # Imágenes ![alt](url)
    imagenes = re.findall(r'!\[([^\]]*)\]\(([^\)]+)\)', contenido)
    resultado.imagenes = [url for alt, url in imagenes]
    
    # Tablas (markdown tables con |)
    for linea in lineas:
        if linea.strip().startswith('|') and '|' in linea[1:]:
            resultado.tablas += 1
    
    # Bloques de código ```lang o ~~~lang
    bloques = re.findall(r'```(\w*)', contenido) + re.findall(r'~~~(\w*)', contenido)
    resultado.bloques_codigo = [b if b else 'sin_lenguaje' for b in bloques]
    
    # Enlaces [text](url)
    enlaces = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', contenido)
    # Filtrar imágenes (que empiezan con !)
    resultado.enlaces = [(texto, url) for texto, url in enlaces 
                         if not contenido[contenido.find(f'[{texto}]')-1:contenido.find(f'[{texto}]')] == '!']
    
    # DIVs HTML
    divs = re.findall(r'<div\s+class=["\']([^"\']+)["\']', contenido)
    resultado.divs_html = divs
    
    # Listas
    for linea in lineas:
        stripped = linea.strip()
        # Bullet lists (*, -, +)
        if re.match(r'^[\*\-\+]\s+', stripped):
            resultado.listas_bullet += 1
        # Numbered lists (1., 2., etc)
        if re.match(r'^\d+\.\s+', stripped):
            resultado.listas_numeradas += 1
    
    return resultado

def analizar_seccion(ruta_seccion: Path) -> Dict:
    """
    Analiza todos los archivos .md de una sección
    """
    ruta_original = ruta_seccion / 'original'
    
    if not ruta_original.exists():
        raise ValueError(f"No existe: {ruta_original}")
    
    archivos_md = list(ruta_original.glob('*.md'))
    
    # Filtrar README.md para análisis separado
    readme = [f for f in archivos_md if f.name == 'README.md']
    contenido = [f for f in archivos_md if f.name != 'README.md']
    
    resultados = {
        'seccion': ruta_seccion.name,
        'ruta': str(ruta_seccion),
        'total_archivos': len(archivos_md),
        'archivos_contenido': len(contenido),
        'tiene_readme': len(readme) > 0,
        'archivos': []
    }
    
    # Analizar cada archivo
    for archivo in archivos_md:
        analisis = analizar_archivo(archivo)
        resultados['archivos'].append(analisis)
    
    # Estadísticas agregadas
    resultados['estadisticas'] = {
        'total_lineas': sum(a.lineas for a in resultados['archivos']),
        'total_palabras': sum(a.palabras for a in resultados['archivos']),
        'total_headings': sum(len(a.headings) for a in resultados['archivos']),
        'total_imagenes': sum(len(a.imagenes) for a in resultados['archivos']),
        'total_tablas': sum(a.tablas for a in resultados['archivos']),
        'total_codigo': sum(len(a.bloques_codigo) for a in resultados['archivos']),
        'total_enlaces': sum(len(a.enlaces) for a in resultados['archivos']),
        'total_divs': sum(len(a.divs_html) for a in resultados['archivos']),
    }
    
    return resultados

def imprimir_reporte(resultados: Dict):
    """
    Imprime un reporte legible del análisis
    """
    print("═" * 70)
    print(f"ANÁLISIS DE SECCIÓN: {resultados['seccion']}")
    print("═" * 70)
    print()
    
    print(f"📁 Ubicación: {resultados['ruta']}")
    print(f"📄 Total archivos: {resultados['total_archivos']}")
    print(f"   - Contenido: {resultados['archivos_contenido']}")
    print(f"   - README: {'Sí' if resultados['tiene_readme'] else 'No'}")
    print()
    
    print("📊 ESTADÍSTICAS GENERALES")
    print("─" * 70)
    stats = resultados['estadisticas']
    print(f"  Líneas totales:     {stats['total_lineas']:>6}")
    print(f"  Palabras totales:   {stats['total_palabras']:>6}")
    print(f"  Headings:           {stats['total_headings']:>6}")
    print(f"  Imágenes:           {stats['total_imagenes']:>6}")
    print(f"  Tablas:             {stats['total_tablas']:>6}")
    print(f"  Bloques de código:  {stats['total_codigo']:>6}")
    print(f"  Enlaces:            {stats['total_enlaces']:>6}")
    print(f"  DIVs HTML:          {stats['total_divs']:>6}")
    print()
    
    print("📝 ARCHIVOS DETALLADOS")
    print("─" * 70)
    
    for archivo in resultados['archivos']:
        if archivo.nombre == 'README.md':
            continue  # Saltar README en detalle
        
        print()
        print(f"📄 {archivo.nombre}")
        print(f"   Líneas: {archivo.lineas}, Palabras: {archivo.palabras}")
        
        if archivo.tiene_frontmatter:
            print(f"   ✅ Front matter YAML:")
            for key, value in archivo.frontmatter.items():
                print(f"      - {key}: {value}")
        
        if archivo.headings:
            print(f"   📑 Estructura ({len(archivo.headings)} headings):")
            for nivel, texto in archivo.headings:
                indent = "  " * (nivel - 1)
                print(f"      {indent}{'#' * nivel} {texto}")
        
        if archivo.imagenes:
            print(f"   🖼️  Imágenes ({len(archivo.imagenes)}):")
            for img in archivo.imagenes:
                print(f"      - {img}")
        
        if archivo.tablas > 0:
            print(f"   📊 Tablas: {archivo.tablas}")
        
        if archivo.bloques_codigo:
            print(f"   💻 Código ({len(archivo.bloques_codigo)} bloques):")
            from collections import Counter
            conteo = Counter(archivo.bloques_codigo)
            for lang, count in conteo.items():
                print(f"      - {lang}: {count}")
        
        if archivo.divs_html:
            print(f"   🏷️  DIVs HTML: {', '.join(set(archivo.divs_html))}")
        
        if archivo.listas_bullet > 0:
            print(f"   • Listas bullet: {archivo.listas_bullet} items")
        
        if archivo.listas_numeradas > 0:
            print(f"   1. Listas numeradas: {archivo.listas_numeradas} items")

def recomendar_estructura(resultados: Dict):
    """
    Recomienda estructura de archivos RST basada en el análisis
    """
    print()
    print("═" * 70)
    print("💡 RECOMENDACIÓN DE ESTRUCTURA DE TRADUCCIÓN")
    print("═" * 70)
    print()
    
    num_contenido = resultados['archivos_contenido']
    seccion = resultados['seccion']
    
    print("Principio fundamental:")
    print("  📌 \"Un archivo original → Un archivo traducido\" (1:1)")
    print()
    
    print(f"✅ ESTRUCTURA RECOMENDADA para traduccion/:")
    print("─" * 70)
    print()
    print(f"Crear {num_contenido + 1} archivos .rst:")
    print()
    print("  1️⃣  Archivo índice (con toctree)")
    print(f"      - {seccion.replace('_', '-')}.rst")
    print(f"      o index.rst")
    print()
    print(f"  2️⃣  {num_contenido} archivos de contenido (1:1 con originales)")
    
    # Listar archivos originales como ejemplo
    for i, archivo in enumerate(resultados['archivos'], 1):
        if archivo.nombre == 'README.md':
            continue
        nombre_base = archivo.nombre.replace('.md', '')
        nombre_rst = f"{seccion.replace('_', '-')}_{nombre_base}.rst"
        print(f"      - {nombre_rst}")
        if i >= 6:  # Mostrar máximo 6 ejemplos
            resto = num_contenido - 6
            if resto > 0:
                print(f"      - ... ({resto} archivos más)")
            break
    
    print()
    print("Ventajas de estructura 1:1:")
    print("  ✅ Facilita mantenimiento")
    print("  ✅ Permite trabajar en archivos individuales")
    print("  ✅ Clara trazabilidad al original")
    print("  ✅ Mejor organización y navegación")
    print("  ✅ Compatible con toctree de Sphinx")
    print()
    
    print("❌ NO RECOMENDADO:")
    print("─" * 70)
    print()
    print(f"  ❌ Crear un solo archivo monolítico:")
    print(f"      - {seccion}.rst (con todo el contenido mezclado)")
    print()
    print("  Razón: Dificulta mantenimiento y viola principio 1:1")
    print()
    
    print("📝 Ejemplo de toctree en archivo índice:")
    print("─" * 70)
    print()
    print("  .. toctree::")
    print("     :maxdepth: 2")
    print()
    for i, archivo in enumerate(resultados['archivos'], 1):
        if archivo.nombre == 'README.md':
            continue
        nombre_base = archivo.nombre.replace('.md', '')
        nombre_rst = f"{seccion.replace('_', '-')}_{nombre_base}"
        print(f"     {nombre_rst}")
        if i >= 4:  # Mostrar máximo 4 ejemplos en toctree
            resto = num_contenido - 4
            if resto > 0:
                print(f"     ... ({resto} más)")
            break
    print()
    print("═" * 70)
    print()

def generar_json(resultados: Dict, archivo_salida: Path):
    """
    Genera archivo JSON con los resultados
    """
    # Convertir dataclasses a dict
    resultados_json = {
        'seccion': resultados['seccion'],
        'ruta': resultados['ruta'],
        'total_archivos': resultados['total_archivos'],
        'archivos_contenido': resultados['archivos_contenido'],
        'tiene_readme': resultados['tiene_readme'],
        'estadisticas': resultados['estadisticas'],
        'archivos': []
    }
    
    for archivo in resultados['archivos']:
        resultados_json['archivos'].append({
            'nombre': archivo.nombre,
            'lineas': archivo.lineas,
            'palabras': archivo.palabras,
            'caracteres': archivo.caracteres,
            'tiene_frontmatter': archivo.tiene_frontmatter,
            'frontmatter': archivo.frontmatter,
            'headings': archivo.headings,
            'imagenes': archivo.imagenes,
            'tablas': archivo.tablas,
            'bloques_codigo': archivo.bloques_codigo,
            'enlaces': archivo.enlaces,
            'divs_html': archivo.divs_html,
            'listas_bullet': archivo.listas_bullet,
            'listas_numeradas': archivo.listas_numeradas,
        })
    
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(resultados_json, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Resultados guardados en: {archivo_salida}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python analizar_seccion.py <ruta_seccion>")
        print("Ejemplo: python analizar_seccion.py sections/02_constraints")
        sys.exit(1)
    
    ruta_seccion = Path(sys.argv[1])
    
    if not ruta_seccion.exists():
        print(f"❌ Error: No existe {ruta_seccion}")
        sys.exit(1)
    
    try:
        # Analizar
        resultados = analizar_seccion(ruta_seccion)
        
        # Imprimir reporte
        imprimir_reporte(resultados)
        
        # Recomendar estructura de traducción
        recomendar_estructura(resultados)
        
        # Generar JSON
        archivo_json = ruta_seccion / 'analisis_seccion.json'
        generar_json(resultados, archivo_json)
        
        print()
        print("═" * 70)
        print("✅ ANÁLISIS COMPLETADO")
        print("═" * 70)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
