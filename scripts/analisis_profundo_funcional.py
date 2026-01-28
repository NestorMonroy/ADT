#!/usr/bin/env python3
"""
Análisis Profundo de Fuentes - arc42 Sections
Usando Programación Funcional

Ubicación: /tmp/ADT/scripts/analisis_profundo_funcional.py
Salida: Raíz de la sección analizada (OPCIÓN A)

Autor: Sistema de Traducción ADT
Fecha: 2026-01-27
Paradigma: Funcional (pure functions, map, filter, reduce)
"""

from functools import reduce, partial
from pathlib import Path
from typing import Dict, List, Tuple, Callable, Any
from dataclasses import dataclass
from collections import Counter
import re
import json
import sys

# ============================================================================
# ESTRUCTURAS DE DATOS INMUTABLES
# ============================================================================

@dataclass(frozen=True)
class ArchivoMD:
    """Estructura inmutable para archivo Markdown"""
    ruta: Path
    nombre: str
    lineas: int
    contenido: str
    front_matter: Dict[str, Any]
    cuerpo: str
    tipo: str  # 'tip', 'ejemplo', 'otro'

@dataclass(frozen=True)
class EstadisticasArchivo:
    """Estadísticas de un archivo"""
    nombre: str
    palabras: int
    lineas: int
    caracteres: int
    tiene_imagenes: bool
    num_imagenes: int
    tiene_codigo: bool
    tiene_tablas: bool
    tiene_listas: bool

@dataclass(frozen=True)
class ComparacionContenido:
    """Comparación entre original y traducción"""
    archivo: str
    completo: bool
    elementos_faltantes: List[str]
    similitud: float

# ============================================================================
# FUNCIONES PURAS - LECTURA Y PARSING
# ============================================================================

def leer_archivo(ruta: Path) -> str:
    """Función pura: lee contenido de archivo"""
    try:
        return ruta.read_text(encoding='utf-8')
    except:
        return ""

def extraer_front_matter(contenido: str) -> Tuple[Dict[str, Any], str]:
    """
    Función pura: extrae YAML front matter y cuerpo
    
    Args:
        contenido: Texto completo del archivo
        
    Returns:
        (front_matter_dict, cuerpo)
    """
    if not contenido.startswith('---'):
        return ({}, contenido)
    
    partes = contenido.split('---', 2)
    if len(partes) < 3:
        return ({}, contenido)
    
    # Parseo simple de YAML (solo key: value)
    fm_text = partes[1]
    front_matter = {}
    
    for linea in fm_text.strip().split('\n'):
        if ':' in linea:
            key, value = linea.split(':', 1)
            front_matter[key.strip()] = value.strip().strip('"')
    
    cuerpo = partes[2].strip()
    return (front_matter, cuerpo)

def clasificar_archivo(nombre: str) -> str:
    """Función pura: clasifica tipo de archivo"""
    if re.match(r'2016-03-\d+-t-\d+-\d+\.md', nombre):
        return 'tip'
    elif re.match(r'\d+-\w+-.*\.md', nombre):
        return 'ejemplo'
    else:
        return 'otro'

def crear_archivo_md(ruta: Path) -> ArchivoMD:
    """Función pura: crea estructura ArchivoMD desde ruta"""
    contenido = leer_archivo(ruta)
    front_matter, cuerpo = extraer_front_matter(contenido)
    
    return ArchivoMD(
        ruta=ruta,
        nombre=ruta.name,
        lineas=len(contenido.split('\n')),
        contenido=contenido,
        front_matter=front_matter,
        cuerpo=cuerpo,
        tipo=clasificar_archivo(ruta.name)
    )

# ============================================================================
# FUNCIONES PURAS - ANÁLISIS DE CONTENIDO
# ============================================================================

def contar_palabras(texto: str) -> int:
    """Función pura: cuenta palabras en texto"""
    return len(re.findall(r'\w+', texto))

def detectar_imagenes(texto: str) -> List[str]:
    """Función pura: detecta referencias a imágenes"""
    return re.findall(r'!\[.*?\]\((.*?)\)', texto)

def detectar_codigo(texto: str) -> bool:
    """Función pura: detecta bloques de código"""
    return bool(re.search(r'```|`[^`]+`', texto))

def detectar_tablas(texto: str) -> bool:
    """Función pura: detecta tablas markdown"""
    return bool(re.search(r'\|.*\|', texto))

def detectar_listas(texto: str) -> bool:
    """Función pura: detecta listas"""
    return bool(re.search(r'^\s*[\*\-\+]\s+', texto, re.MULTILINE))

def calcular_estadisticas(archivo: ArchivoMD) -> EstadisticasArchivo:
    """Función pura: calcula estadísticas de un archivo"""
    imagenes = detectar_imagenes(archivo.cuerpo)
    
    return EstadisticasArchivo(
        nombre=archivo.nombre,
        palabras=contar_palabras(archivo.cuerpo),
        lineas=archivo.lineas,
        caracteres=len(archivo.cuerpo),
        tiene_imagenes=len(imagenes) > 0,
        num_imagenes=len(imagenes),
        tiene_codigo=detectar_codigo(archivo.cuerpo),
        tiene_tablas=detectar_tablas(archivo.cuerpo),
        tiene_listas=detectar_listas(archivo.cuerpo)
    )

# ============================================================================
# FUNCIONES DE ORDEN SUPERIOR
# ============================================================================

def aplicar_a_archivos(funcion: Callable, archivos: List[ArchivoMD]) -> List[Any]:
    """
    Función de orden superior: aplica función a lista de archivos
    Equivalente funcional a map
    """
    return list(map(funcion, archivos))

def filtrar_por_tipo(tipo: str) -> Callable:
    """
    Función de orden superior: retorna función filtro por tipo
    Currying
    """
    return lambda archivo: archivo.tipo == tipo

def componer(*funciones):
    """
    Composición de funciones: f(g(h(x)))
    """
    def composicion(x):
        return reduce(lambda acc, f: f(acc), reversed(funciones), x)
    return composicion

# ============================================================================
# FUNCIONES PURAS - COMPARACIÓN
# ============================================================================

def extraer_elementos_clave(texto: str) -> set:
    """Función pura: extrae elementos clave de un texto"""
    elementos = set()
    
    # Extraer headings
    headings = re.findall(r'^#+\s+(.+)$', texto, re.MULTILINE)
    elementos.update(f"heading:{h.lower()}" for h in headings)
    
    # Extraer listas principales
    listas = re.findall(r'^\s*[\*\-]\s+(.+?)[:.]', texto, re.MULTILINE)
    elementos.update(f"lista:{l.lower()[:20]}" for l in listas)
    
    # Extraer primeras palabras de párrafos
    parrafos = [p.strip() for p in texto.split('\n\n') if p.strip()]
    elementos.update(f"parrafo:{p[:30].lower()}" for p in parrafos[:5])
    
    return elementos

def calcular_similitud(elementos1: set, elementos2: set) -> float:
    """Función pura: calcula similitud entre dos conjuntos"""
    if not elementos1 and not elementos2:
        return 1.0
    if not elementos1 or not elementos2:
        return 0.0
    
    interseccion = len(elementos1 & elementos2)
    union = len(elementos1 | elementos2)
    
    return interseccion / union if union > 0 else 0.0

def comparar_contenidos(original: ArchivoMD, traducido_texto: str) -> ComparacionContenido:
    """Función pura: compara contenido original vs traducido"""
    elementos_orig = extraer_elementos_clave(original.cuerpo)
    elementos_trad = extraer_elementos_clave(traducido_texto)
    
    faltantes = elementos_orig - elementos_trad
    similitud = calcular_similitud(elementos_orig, elementos_trad)
    
    return ComparacionContenido(
        archivo=original.nombre,
        completo=similitud > 0.8,
        elementos_faltantes=list(faltantes)[:5],  # Solo primeros 5
        similitud=similitud
    )

# ============================================================================
# FUNCIONES DE AGREGACIÓN
# ============================================================================

def agrupar_por_tipo(archivos: List[ArchivoMD]) -> Dict[str, List[ArchivoMD]]:
    """Función pura: agrupa archivos por tipo usando reduce"""
    def agregar(acc, archivo):
        tipo = archivo.tipo
        return {**acc, tipo: acc.get(tipo, []) + [archivo]}
    
    return reduce(agregar, archivos, {})

def estadisticas_globales(estadisticas: List[EstadisticasArchivo]) -> Dict[str, Any]:
    """Función pura: calcula estadísticas globales"""
    return {
        'total_archivos': len(estadisticas),
        'total_palabras': sum(e.palabras for e in estadisticas),
        'total_lineas': sum(e.lineas for e in estadisticas),
        'archivos_con_imagenes': sum(1 for e in estadisticas if e.tiene_imagenes),
        'total_imagenes': sum(e.num_imagenes for e in estadisticas),
        'archivos_con_codigo': sum(1 for e in estadisticas if e.tiene_codigo),
        'archivos_con_tablas': sum(1 for e in estadisticas if e.tiene_tablas),
        'archivos_con_listas': sum(1 for e in estadisticas if e.tiene_listas),
        'promedio_palabras': sum(e.palabras for e in estadisticas) / len(estadisticas) if estadisticas else 0,
        'promedio_lineas': sum(e.lineas for e in estadisticas) / len(estadisticas) if estadisticas else 0,
    }

# ============================================================================
# ANÁLISIS ESTRUCTURAL
# ============================================================================

def analizar_estructura_front_matter(archivos: List[ArchivoMD]) -> Dict[str, Any]:
    """Función pura: analiza estructura de front matter"""
    # Obtener todos los keys únicos
    todos_keys = reduce(
        lambda acc, arch: acc | set(arch.front_matter.keys()),
        archivos,
        set()
    )
    
    # Contar frecuencia de cada key
    frecuencias = {
        key: sum(1 for arch in archivos if key in arch.front_matter)
        for key in todos_keys
    }
    
    return {
        'keys_unicos': sorted(todos_keys),
        'frecuencias': frecuencias,
        'total_archivos': len(archivos)
    }

def analizar_patrones_imagenes(archivos: List[ArchivoMD]) -> Dict[str, Any]:
    """Función pura: analiza patrones en URLs de imágenes"""
    todas_imagenes = reduce(
        lambda acc, arch: acc + detectar_imagenes(arch.cuerpo),
        archivos,
        []
    )
    
    # Clasificar por tipo de URL
    con_site_imageurl = [img for img in todas_imagenes if 'site.imageurl' in img]
    con_http = [img for img in todas_imagenes if img.startswith('http')]
    relativas = [img for img in todas_imagenes if not img.startswith('http') and 'site.imageurl' not in img]
    
    return {
        'total_imagenes': len(todas_imagenes),
        'con_site_imageurl': len(con_site_imageurl),
        'con_http': len(con_http),
        'relativas': len(relativas),
        'ejemplos_site_imageurl': con_site_imageurl[:3],
        'ejemplos_http': con_http[:3],
        'ejemplos_relativas': relativas[:3]
    }

# ============================================================================
# FUNCIÓN PRINCIPAL DE ANÁLISIS
# ============================================================================

def analizar_seccion_completa(directorio: Path) -> Dict[str, Any]:
    """
    Función principal: análisis completo usando programación funcional
    """
    # 1. Leer todos los archivos .md (map)
    archivos_md = list(map(
        crear_archivo_md,
        filter(lambda p: p.suffix == '.md' and p.name != 'README.md', directorio.glob('*.md'))
    ))
    
    # 2. Calcular estadísticas individuales (map)
    estadisticas = list(map(calcular_estadisticas, archivos_md))
    
    # 3. Agrupar por tipo (reduce)
    agrupados = agrupar_por_tipo(archivos_md)
    
    # 4. Análisis de front matter
    fm_analysis = analizar_estructura_front_matter(archivos_md)
    
    # 5. Análisis de patrones de imágenes
    img_analysis = analizar_patrones_imagenes(archivos_md)
    
    # 6. Estadísticas globales
    stats_globales = estadisticas_globales(estadisticas)
    
    # 7. Análisis por tipo
    stats_por_tipo = {
        tipo: estadisticas_globales(
            list(map(calcular_estadisticas, archivos))
        )
        for tipo, archivos in agrupados.items()
    }
    
    return {
        'total_archivos': len(archivos_md),
        'agrupacion_por_tipo': {tipo: len(archs) for tipo, archs in agrupados.items()},
        'estadisticas_globales': stats_globales,
        'estadisticas_por_tipo': stats_por_tipo,
        'front_matter_analysis': fm_analysis,
        'imagenes_analysis': img_analysis,
        'archivos_individuales': [
            {
                'nombre': a.nombre,
                'tipo': a.tipo,
                'lineas': a.lineas,
                'palabras': calcular_estadisticas(a).palabras,
                'tiene_imagenes': bool(detectar_imagenes(a.cuerpo)),
                'tiene_tablas': detectar_tablas(a.cuerpo)
            }
            for a in archivos_md
        ]
    }

# ============================================================================
# COMPARACIÓN CON TRADUCCIONES
# ============================================================================

def crear_mapeo_nombres(seccion: str) -> Dict[str, str]:
    """Crea mapeo de nombres original -> traducido por sección"""
    mapeos = {
        '09': {
            'section-9.md': 'seccion_09_decisiones_arquitectonicas.rst',
            '2016-03-01-t-9-1.md': 'decision_tip_1.rst',
            '2016-03-01-t-9-2.md': 'decision_tip_2.rst',
            '2016-03-01-t-9-3.md': 'decision_tip_3.rst',
            '2016-03-01-t-9-4.md': 'decision_tip_4.rst',
            '2016-03-01-t-9-5.md': 'decision_tip_5.rst',
            '2016-03-01-t-9-6.md': 'decision_tip_6.rst',
            '2016-03-01-t-9-7.md': 'decision_tip_7.rst',
            '2022-01-14-t-9-8.md': 'decision_tip_8.rst',
            '2022-01-28-t-9-9.md': 'decision_tip_9.rst',
            '2022-01-29-t-9-10.md': 'decision_tip_10.rst',
            '09-decision-example-adr.md': 'decision_ejemplo_adr.rst',
            '09-decision-example-htmlsc-1.md': 'decision_ejemplo_htmlsc_1.rst',
            '09-decision-example-tpu-2.md': 'decision_ejemplo_tpu_2.rst',
        },
        '08': {
            'section-8.md': 'seccion_08_conceptos_transversales.rst',
            '2016-03-01-t-8-1.md': 'crosscutting_tip_1.rst',
            '2016-03-01-t-8-2.md': 'crosscutting_tip_2.rst',
            '2016-03-01-t-8-3.md': 'crosscutting_tip_3.rst',
            '2016-03-01-t-8-4.md': 'crosscutting_tip_4.rst',
            '2016-03-01-t-8-5.md': 'crosscutting_tip_5.rst',
            '2016-03-01-t-8-6.md': 'crosscutting_tip_6.rst',
            '2016-03-01-t-8-7.md': 'crosscutting_tip_7.rst',
            '2016-03-01-t-8-8.md': 'crosscutting_tip_8.rst',
            '2016-03-01-t-8-9.md': 'crosscutting_tip_9.rst',
            '2016-03-02-t-8-10.md': 'crosscutting_tip_10.rst',
            '2022-07-01-t-8-11.md': 'crosscutting_tip_11.rst',
        },
        '07': {
            '2016-03-01-t-7-1.md': 'deployment_tip_1.rst',
            '2016-03-01-t-7-2.md': 'deployment_tip_2.rst',
            '2016-03-01-t-7-3.md': 'deployment_tip_3.rst',
            '2016-03-01-t-7-4.md': 'deployment_tip_4.rst',
            '2016-03-01-t-7-5.md': 'deployment_tip_5.rst',
            '2016-03-01-t-7-6.md': 'deployment_tip_6.rst',
            '2016-03-01-t-7-7.md': 'deployment_tip_7.rst',
            '2016-03-01-t-7-8.md': 'deployment_tip_8.rst',
            '2016-03-01-t-7-9.md': 'deployment_tip_9.rst',
            '2016-03-02-t-7-10.md': 'deployment_tip_10.rst',
            '07-deployment-example-tpu-1.md': 'deployment_ejemplo_tpu_1.rst',
            '07-deployment-sample-htmlsc-1.md': 'deployment_ejemplo_htmlsc.rst',
            '07-deployment-sample-tpu-2.md': 'deployment_ejemplo_tpu_2.rst',
        }
    }
    
    return mapeos.get(seccion, {})

def verificar_traducciones(dir_original: Path, dir_traduccion: Path, seccion: str) -> Dict[str, Any]:
    """
    Verifica completitud de traducciones usando programación funcional
    """
    # Leer originales
    originales = list(map(
        crear_archivo_md,
        filter(lambda p: p.suffix == '.md' and p.name != 'README.md', dir_original.glob('*.md'))
    ))
    
    # Obtener mapeo de nombres
    mapeo = crear_mapeo_nombres(seccion)
    
    # Función para encontrar traducción correspondiente
    def encontrar_traduccion(original: ArchivoMD) -> Tuple[ArchivoMD, str]:
        nombre_traduccion = original.nombre.replace('.md', '.rst')
        nombre_rst = mapeo.get(original.nombre, nombre_traduccion)
        ruta_traduccion = dir_traduccion / nombre_rst
        
        if ruta_traduccion.exists():
            return (original, leer_archivo(ruta_traduccion))
        else:
            return (original, "")
    
    # Mapear originales a sus traducciones
    pares = list(map(encontrar_traduccion, originales))
    
    # Comparar contenidos
    comparaciones = [
        comparar_contenidos(orig, trad)
        for orig, trad in pares
        if trad  # Solo si existe traducción
    ]
    
    return {
        'total_originales': len(originales),
        'total_traducciones': sum(1 for _, trad in pares if trad),
        'traducciones_faltantes': [orig.nombre for orig, trad in pares if not trad],
        'comparaciones': [
            {
                'archivo': c.archivo,
                'completo': c.completo,
                'similitud': f"{c.similitud:.2%}",
                'elementos_faltantes': c.elementos_faltantes[:3]
            }
            for c in comparaciones
        ],
        'estadisticas_completitud': {
            'completas': sum(1 for c in comparaciones if c.completo),
            'incompletas': sum(1 for c in comparaciones if not c.completo),
            'similitud_promedio': f"{sum(c.similitud for c in comparaciones) / len(comparaciones):.2%}" if comparaciones else "N/A"
        }
    }

# ============================================================================
# GENERACIÓN DE REPORTES
# ============================================================================

def generar_reporte_json(analisis: Dict[str, Any], archivo_salida: Path):
    """Genera reporte en formato JSON"""
    archivo_salida.write_text(
        json.dumps(analisis, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

def generar_reporte_texto(analisis: Dict[str, Any], seccion: str) -> str:
    """Genera reporte en formato texto legible"""
    lineas = [
        "=" * 80,
        f"ANÁLISIS PROFUNDO - SECCIÓN {seccion.upper()}",
        "Programación Funcional en Python",
        "=" * 80,
        "",
        f"📊 RESUMEN GENERAL",
        "-" * 80,
        f"Total de archivos analizados: {analisis['analisis_originales']['total_archivos']}",
        "",
        "Agrupación por tipo:",
    ]
    
    for tipo, cantidad in analisis['analisis_originales']['agrupacion_por_tipo'].items():
        lineas.append(f"  • {tipo}: {cantidad} archivos")
    
    lineas.extend([
        "",
        f"📈 ESTADÍSTICAS GLOBALES",
        "-" * 80,
    ])
    
    stats = analisis['analisis_originales']['estadisticas_globales']
    for key, value in stats.items():
        lineas.append(f"  {key}: {value}")
    
    lineas.extend([
        "",
        f"🏷️  ANÁLISIS FRONT MATTER",
        "-" * 80,
        f"Keys únicos: {', '.join(analisis['analisis_originales']['front_matter_analysis']['keys_unicos'])}",
        "",
        "Frecuencias:",
    ])
    
    for key, freq in analisis['analisis_originales']['front_matter_analysis']['frecuencias'].items():
        lineas.append(f"  {key}: {freq} archivos")
    
    lineas.extend([
        "",
        f"🖼️  ANÁLISIS DE IMÁGENES",
        "-" * 80,
    ])
    
    img = analisis['analisis_originales']['imagenes_analysis']
    for key, value in img.items():
        if not key.startswith('ejemplos_'):
            lineas.append(f"  {key}: {value}")
    
    lineas.extend([
        "",
        f"🔄 VERIFICACIÓN DE TRADUCCIONES",
        "-" * 80,
        f"Total originales: {analisis['verificacion_traducciones']['total_originales']}",
        f"Total traducciones: {analisis['verificacion_traducciones']['total_traducciones']}",
        f"Similitud promedio: {analisis['verificacion_traducciones']['estadisticas_completitud']['similitud_promedio']}",
        "",
        "=" * 80,
        "FIN DEL REPORTE",
        "=" * 80,
    ])
    
    return '\n'.join(lineas)

# ============================================================================
# FUNCIÓN MAIN
# ============================================================================

def main():
    """Función principal"""
    print("🔍 Iniciando análisis profundo con programación funcional...")
    print()
    
    # Determinar sección a analizar (puede pasarse como argumento)
    if len(sys.argv) > 1:
        seccion = sys.argv[1]
    else:
        seccion = '07'  # Por defecto
    
    # Construir paths
    base_sections = Path('/tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections')
    
    # Mapeo de secciones
    secciones_dirs = {
        '09': '09_architecture_decisions',
        '08': '08_crosscutting_concepts',
        '07': '07_deployment_view',
        '06': '06_runtime_view',
        '05': '05_building_block_view',
        # Agregar más según necesidad
    }
    
    seccion_dir_name = secciones_dirs.get(seccion)
    if not seccion_dir_name:
        print(f"❌ Sección {seccion} no configurada")
        sys.exit(1)
    
    base_dir = base_sections / seccion_dir_name
    dir_original = base_dir / 'original'
    dir_traduccion = base_dir / 'traduccion'
    
    if not dir_original.exists():
        print(f"❌ Directorio no encontrado: {dir_original}")
        sys.exit(1)
    
    print(f"📂 Analizando Sección {seccion}: {seccion_dir_name}")
    print(f"   Original: {dir_original}")
    print(f"   Traducción: {dir_traduccion}")
    print()
    
    # Análisis completo
    print("📊 Analizando archivos originales...")
    analisis = analizar_seccion_completa(dir_original)
    
    print("🔄 Verificando traducciones...")
    verificacion = verificar_traducciones(dir_original, dir_traduccion, seccion)
    
    # Combinar análisis
    analisis_completo = {
        'seccion': seccion,
        'analisis_originales': analisis,
        'verificacion_traducciones': verificacion
    }
    
    # Generar reportes en la raíz de la sección (OPCIÓN A)
    print("📝 Generando reportes en raíz de sección...")
    
    archivo_json = base_dir / 'ANALISIS_PROFUNDO_FUNCIONAL.json'
    generar_reporte_json(analisis_completo, archivo_json)
    print(f"✅ JSON: {archivo_json}")
    
    archivo_txt = base_dir / 'ANALISIS_PROFUNDO_FUNCIONAL.txt'
    reporte_texto = generar_reporte_texto(analisis_completo, seccion)
    archivo_txt.write_text(reporte_texto, encoding='utf-8')
    print(f"✅ TXT: {archivo_txt}")
    
    # Mostrar resumen
    print()
    print("=" * 80)
    print("RESUMEN")
    print("=" * 80)
    print(f"\nSección: {seccion}")
    print(f"Archivos originales: {analisis['total_archivos']}")
    print(f"Traducciones: {verificacion['total_traducciones']}")
    print(f"Similitud promedio: {verificacion['estadisticas_completitud']['similitud_promedio']}")
    print()
    print("✅ Análisis completado")
    print(f"   Archivos generados en: {base_dir}/")

if __name__ == '__main__':
    main()
