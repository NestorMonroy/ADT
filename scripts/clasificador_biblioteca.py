#!/usr/bin/env python3
"""
=============================================================================
Clasificador de Biblioteca ADT - Programación Funcional
=============================================================================

Versión: 1.0.0
Fecha: 2026-01-28
Autor: Sistema ADT
Paradigma: Programación Funcional Pura

Descripción:
    Sistema completo de clasificación y gestión de libros técnicos
    traducidos usando programación funcional estricta.

Características:
    - Funciones puras (sin efectos secundarios)
    - Inmutabilidad de datos
    - Composición de funciones
    - Type hints completos
    - Map/Filter/Reduce
    - Monads (Result type)

Uso:
    python clasificador_biblioteca.py --clasificar "Modern Full-Stack Development"
    python clasificador_biblioteca.py --validar /ruta/libro
    python clasificador_biblioteca.py --generar-catalogo
    python clasificador_biblioteca.py --estadisticas

=============================================================================
"""

from __future__ import annotations
from typing import (
    TypeVar, Callable, List, Dict, Tuple, Optional, Union,
    NamedTuple, Literal, Any
)
from dataclasses import dataclass, field, replace
from functools import reduce, partial
from itertools import chain
from pathlib import Path
from enum import Enum
import re
import json
from datetime import datetime, date


# =============================================================================
# TIPOS Y ESTRUCTURAS DE DATOS INMUTABLES
# =============================================================================

class Categoria(Enum):
    """Categorías principales de la biblioteca."""
    INF = "Informática"
    ING = "Ingeniería"
    CIE = "Ciencias"


class EstadoLibro(Enum):
    """Estados posibles de un libro."""
    PLANIFICADO = "Planificado"
    PREPARACION = "Preparación"
    EN_PROCESO = "En Proceso"
    COMPLETADO = "Completado"
    OBSOLETO = "Obsoleto"


@dataclass(frozen=True)
class CodigoClasificacion:
    """Código de clasificación inmutable."""
    categoria: str  # 3 letras mayúsculas
    subcategoria: str  # 3 letras mayúsculas
    especialidad: str  # 3 letras mayúsculas
    numero: int  # 001-999
    
    def __str__(self) -> str:
        return f"{self.categoria}.{self.subcategoria}.{self.especialidad}.{self.numero:03d}"
    
    def __post_init__(self):
        """Validación inmutable en construcción."""
        if not all(len(x) == 3 and x.isupper() and x.isalpha() 
                   for x in [self.categoria, self.subcategoria, self.especialidad]):
            raise ValueError("Cada componente debe ser 3 letras mayúsculas")
        if not (1 <= self.numero <= 999):
            raise ValueError("Número debe estar entre 001 y 999")


@dataclass(frozen=True)
class MetadataLibro:
    """Metadata inmutable de un libro."""
    codigo: CodigoClasificacion
    titulo_original: str
    titulo_traducido: str
    autores: Tuple[str, ...]
    editorial: str
    año: int
    idioma_origen: str
    idioma_destino: str
    estado: EstadoLibro
    progreso: float  # 0.0-100.0
    paginas_total: int
    paginas_traducidas: int
    terminos_glosario: int
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    ruta: Optional[Path] = None
    
    def __post_init__(self):
        """Validación de invariantes."""
        if not (0.0 <= self.progreso <= 100.0):
            raise ValueError("Progreso debe estar entre 0 y 100")
        if not (0 <= self.paginas_traducidas <= self.paginas_total):
            raise ValueError("Páginas traducidas no puede exceder total")


@dataclass(frozen=True)
class Biblioteca:
    """Estado inmutable completo de la biblioteca."""
    libros: Tuple[MetadataLibro, ...]
    fecha_actualizacion: datetime
    
    @property
    def total_libros(self) -> int:
        return len(self.libros)
    
    @property
    def progreso_global(self) -> float:
        """Calcular progreso global de forma funcional."""
        if not self.libros:
            return 0.0
        total_pags = sum(libro.paginas_total for libro in self.libros)
        if total_pags == 0:
            return 0.0
        trad_pags = sum(libro.paginas_traducidas for libro in self.libros)
        return (trad_pags / total_pags) * 100.0


# Tipos genéricos para programación funcional
T = TypeVar('T')
U = TypeVar('U')
E = TypeVar('E')

@dataclass(frozen=True)
class Result:
    """Monad Result para manejo funcional de errores."""
    
    @dataclass(frozen=True)
    class Ok:
        """Resultado exitoso."""
        value: Any
        
        def is_ok(self) -> bool:
            return True
        
        def is_err(self) -> bool:
            return False
        
        def map(self, f: Callable) -> Result.Ok | Result.Err:
            """Functor map."""
            try:
                return Result.Ok(f(self.value))
            except Exception as e:
                return Result.Err(str(e))
        
        def flat_map(self, f: Callable) -> Result.Ok | Result.Err:
            """Monad bind."""
            try:
                return f(self.value)
            except Exception as e:
                return Result.Err(str(e))
        
        def unwrap(self) -> Any:
            return self.value
        
        def unwrap_or(self, default: Any) -> Any:
            return self.value
    
    @dataclass(frozen=True)
    class Err:
        """Resultado con error."""
        error: str
        
        def is_ok(self) -> bool:
            return False
        
        def is_err(self) -> bool:
            return True
        
        def map(self, f: Callable) -> Result.Err:
            """Functor map (no-op en error)."""
            return self
        
        def flat_map(self, f: Callable) -> Result.Err:
            """Monad bind (no-op en error)."""
            return self
        
        def unwrap(self) -> Any:
            raise ValueError(f"Called unwrap on Err: {self.error}")
        
        def unwrap_or(self, default: Any) -> Any:
            return default


# =============================================================================
# FUNCIONES PURAS DE VALIDACIÓN
# =============================================================================

def validar_formato_codigo(codigo: str) -> Result.Ok | Result.Err:
    """
    Valida formato de código de clasificación.
    
    Args:
        codigo: String con formato "XXX.XXX.XXX.NNN"
    
    Returns:
        Result.Ok(codigo) si válido, Result.Err(mensaje) si inválido
    """
    pattern = r'^[A-Z]{3}\.[A-Z]{3}\.[A-Z]{3}\.\d{3}$'
    
    if not isinstance(codigo, str):
        return Result.Err("Código debe ser string")
    
    if not re.match(pattern, codigo):
        return Result.Err(
            f"Formato inválido. Esperado: XXX.XXX.XXX.NNN, recibido: {codigo}"
        )
    
    return Result.Ok(codigo)


def parsear_codigo(codigo_str: str) -> Result.Ok | Result.Err:
    """
    Parsea string de código a CodigoClasificacion.
    
    Función pura que transforma string -> Result[CodigoClasificacion]
    """
    try:
        validacion = validar_formato_codigo(codigo_str)
        if validacion.is_err():
            return validacion
        
        partes = codigo_str.split('.')
        categoria, subcategoria, especialidad, numero_str = partes
        numero = int(numero_str)
        
        codigo = CodigoClasificacion(
            categoria=categoria,
            subcategoria=subcategoria,
            especialidad=especialidad,
            numero=numero
        )
        
        return Result.Ok(codigo)
    
    except Exception as e:
        return Result.Err(f"Error parseando código: {str(e)}")


def validar_estructura_libro(ruta: Path) -> Result.Ok | Result.Err:
    """
    Valida que un libro tenga la estructura correcta.
    
    Función pura (solo lectura, sin modificación).
    
    Args:
        ruta: Path al directorio del libro
    
    Returns:
        Result.Ok(True) si válido, Result.Err(mensaje) si inválido
    """
    archivos_obligatorios = [
        "metadata_libro.rst",
        "index.rst",
        "glosario_acumulativo.rst"
    ]
    
    try:
        if not ruta.is_dir():
            return Result.Err(f"Ruta no es directorio: {ruta}")
        
        faltantes = [
            archivo for archivo in archivos_obligatorios
            if not (ruta / archivo).exists()
        ]
        
        if faltantes:
            return Result.Err(
                f"Archivos obligatorios faltantes: {', '.join(faltantes)}"
            )
        
        return Result.Ok(True)
    
    except Exception as e:
        return Result.Err(f"Error validando estructura: {str(e)}")


# =============================================================================
# FUNCIONES PURAS DE CLASIFICACIÓN
# =============================================================================

def inferir_categoria_desde_titulo(titulo: str) -> Result.Ok | Result.Err:
    """
    Infiere categoría desde título del libro.
    
    Función pura basada en palabras clave.
    
    Args:
        titulo: Título del libro
    
    Returns:
        Result.Ok(Categoria) o Result.Err
    """
    titulo_lower = titulo.lower()
    
    # Palabras clave por categoría
    palabras_informatica = [
        'programming', 'python', 'javascript', 'react', 'docker',
        'machine learning', 'ai', 'artificial intelligence',
        'algorithm', 'data structures', 'web', 'mobile', 'app'
    ]
    
    palabras_ingenieria = [
        'architecture', 'software architecture', 'design patterns',
        'microservices', 'clean code', 'agile', 'scrum',
        'arc42', 'uml', 'requirements'
    ]
    
    palabras_ciencias = [
        'mathematics', 'linear algebra', 'calculus', 'statistics',
        'probability', 'physics', 'biology', 'bioinformatics'
    ]
    
    # Contar coincidencias
    score_inf = sum(1 for kw in palabras_informatica if kw in titulo_lower)
    score_ing = sum(1 for kw in palabras_ingenieria if kw in titulo_lower)
    score_cie = sum(1 for kw in palabras_ciencias if kw in titulo_lower)
    
    scores = {
        'INF': score_inf,
        'ING': score_ing,
        'CIE': score_cie
    }
    
    max_score = max(scores.values())
    
    if max_score == 0:
        return Result.Err(
            "No se pudo inferir categoría automáticamente. "
            "Clasificación manual requerida."
        )
    
    categoria = max(scores, key=scores.get)
    return Result.Ok(categoria)


def inferir_subcategoria_programacion(titulo: str) -> Result.Ok | Result.Err:
    """Infiere subcategoría para libros de programación."""
    titulo_lower = titulo.lower()
    
    keywords_map = {
        'PRG': ['programming', 'developer', 'coding'],
        'IAR': ['machine learning', 'deep learning', 'ai', 'neural'],
        'DVC': ['docker', 'kubernetes', 'devops', 'cloud', 'aws'],
        'BDD': ['database', 'sql', 'nosql', 'mongodb'],
        'ALG': ['algorithm', 'data structures'],
        'WEB': ['web development', 'html', 'css'],
        'MOV': ['mobile', 'ios', 'android', 'react native']
    }
    
    for subcat, keywords in keywords_map.items():
        if any(kw in titulo_lower for kw in keywords):
            return Result.Ok(subcat)
    
    return Result.Ok('PRG')  # Default


def inferir_especialidad_programacion(titulo: str) -> Result.Ok | Result.Err:
    """Infiere especialidad para libros de programación."""
    titulo_lower = titulo.lower()
    
    # Mapping directo de keywords a especialidades
    especialidades_map = {
        'FST': ['full-stack', 'full stack'],
        'PYT': ['python'],
        'JAV': ['javascript'],
        'TSC': ['typescript'],
        'REA': ['react'],
        'VUE': ['vue', 'vuejs'],
        'ANG': ['angular'],
        'NOD': ['node', 'nodejs', 'node.js'],
        'DJA': ['django'],
        'DOC': ['docker'],
        'KUB': ['kubernetes'],
    }
    
    for esp, keywords in especialidades_map.items():
        if any(kw in titulo_lower for kw in keywords):
            return Result.Ok(esp)
    
    return Result.Ok('GEN')  # General/Multitecnología


def generar_codigo_siguiente(
    categoria: str,
    subcategoria: str,
    especialidad: str,
    codigos_existentes: Tuple[CodigoClasificacion, ...]
) -> Result.Ok | Result.Err:
    """
    Genera el siguiente código secuencial disponible.
    
    Función pura: no modifica estado, solo calcula.
    
    Args:
        categoria: Código de categoría (3 letras)
        subcategoria: Código de subcategoría (3 letras)
        especialidad: Código de especialidad (3 letras)
        codigos_existentes: Tupla de códigos ya asignados
    
    Returns:
        Result.Ok(CodigoClasificacion) con próximo número
    """
    try:
        # Filtrar códigos de la misma especialidad
        codigos_filtrados = tuple(
            c for c in codigos_existentes
            if (c.categoria == categoria and
                c.subcategoria == subcategoria and
                c.especialidad == especialidad)
        )
        
        if not codigos_filtrados:
            # Primera asignación en esta especialidad
            numero = 1
        else:
            # Obtener máximo número existente
            max_numero = max(c.numero for c in codigos_filtrados)
            numero = max_numero + 1
        
        if numero > 999:
            return Result.Err(
                f"Límite de 999 libros alcanzado para "
                f"{categoria}.{subcategoria}.{especialidad}"
            )
        
        codigo = CodigoClasificacion(
            categoria=categoria,
            subcategoria=subcategoria,
            especialidad=especialidad,
            numero=numero
        )
        
        return Result.Ok(codigo)
    
    except Exception as e:
        return Result.Err(f"Error generando código: {str(e)}")


# =============================================================================
# FUNCIONES DE ALTO ORDEN Y COMPOSICIÓN
# =============================================================================

def compose(*functions: Callable) -> Callable:
    """
    Compone funciones de derecha a izquierda.
    
    compose(f, g, h)(x) = f(g(h(x)))
    """
    def composed(arg):
        return reduce(lambda acc, f: f(acc), reversed(functions), arg)
    return composed


def pipe(*functions: Callable) -> Callable:
    """
    Compone funciones de izquierda a derecha.
    
    pipe(f, g, h)(x) = h(g(f(x)))
    """
    def piped(arg):
        return reduce(lambda acc, f: f(acc), functions, arg)
    return piped


def map_result(f: Callable[[T], U]) -> Callable[[Result], Result]:
    """
    Transforma función normal en función que opera sobre Result.
    
    Permite: map_result(mi_funcion)(result)
    """
    def mapper(result: Result.Ok | Result.Err) -> Result.Ok | Result.Err:
        return result.map(f)
    return mapper


def filter_libros(
    predicate: Callable[[MetadataLibro], bool]
) -> Callable[[Tuple[MetadataLibro, ...]], Tuple[MetadataLibro, ...]]:
    """
    Crea función de filtrado de libros.
    
    Ejemplo:
        solo_completados = filter_libros(lambda l: l.estado == EstadoLibro.COMPLETADO)
        completados = solo_completados(biblioteca.libros)
    """
    def filterer(libros: Tuple[MetadataLibro, ...]) -> Tuple[MetadataLibro, ...]:
        return tuple(filter(predicate, libros))
    return filterer


def map_libros(
    transform: Callable[[MetadataLibro], T]
) -> Callable[[Tuple[MetadataLibro, ...]], Tuple[T, ...]]:
    """
    Crea función de transformación de libros.
    
    Ejemplo:
        obtener_titulos = map_libros(lambda l: l.titulo_original)
        titulos = obtener_titulos(biblioteca.libros)
    """
    def mapper(libros: Tuple[MetadataLibro, ...]) -> Tuple[T, ...]:
        return tuple(map(transform, libros))
    return mapper


def reduce_libros(
    reducer: Callable[[U, MetadataLibro], U],
    initial: U
) -> Callable[[Tuple[MetadataLibro, ...]], U]:
    """
    Crea función de reducción de libros.
    
    Ejemplo:
        contar_paginas = reduce_libros(
            lambda acc, l: acc + l.paginas_total,
            0
        )
        total_paginas = contar_paginas(biblioteca.libros)
    """
    def reducer_func(libros: Tuple[MetadataLibro, ...]) -> U:
        return reduce(reducer, libros, initial)
    return reducer_func


# =============================================================================
# FUNCIONES DE GENERACIÓN DE REPORTES
# =============================================================================

def generar_catalogo_por_categoria(
    biblioteca: Biblioteca
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Genera catálogo agrupado por categoría.
    
    Función pura que transforma Biblioteca -> Dict
    """
    # Agrupar por categoría usando funciones de alto orden
    categorias = ['INF', 'ING', 'CIE']
    
    def libros_de_categoria(cat: str) -> Tuple[MetadataLibro, ...]:
        return filter_libros(lambda l: l.codigo.categoria == cat)(biblioteca.libros)
    
    def libro_a_dict(libro: MetadataLibro) -> Dict[str, Any]:
        return {
            'codigo': str(libro.codigo),
            'titulo': libro.titulo_traducido,
            'autores': ', '.join(libro.autores),
            'año': libro.año,
            'estado': libro.estado.value,
            'progreso': f"{libro.progreso:.1f}%"
        }
    
    catalogo = {}
    for cat in categorias:
        libros_cat = libros_de_categoria(cat)
        catalogo[cat] = list(map(libro_a_dict, libros_cat))
    
    return catalogo


def calcular_estadisticas(biblioteca: Biblioteca) -> Dict[str, Any]:
    """
    Calcula estadísticas completas de la biblioteca.
    
    Función pura usando composición funcional.
    """
    libros = biblioteca.libros
    
    # Contadores usando reduce
    total_paginas = reduce_libros(
        lambda acc, l: acc + l.paginas_total,
        0
    )(libros)
    
    paginas_traducidas = reduce_libros(
        lambda acc, l: acc + l.paginas_traducidas,
        0
    )(libros)
    
    total_terminos = reduce_libros(
        lambda acc, l: acc + l.terminos_glosario,
        0
    )(libros)
    
    # Conteo por estado usando filter + len
    def contar_por_estado(estado: EstadoLibro) -> int:
        return len(filter_libros(lambda l: l.estado == estado)(libros))
    
    # Distribución por categoría
    def contar_por_categoria(cat: str) -> int:
        return len(filter_libros(lambda l: l.codigo.categoria == cat)(libros))
    
    return {
        'total_libros': len(libros),
        'total_paginas': total_paginas,
        'paginas_traducidas': paginas_traducidas,
        'total_terminos': total_terminos,
        'progreso_global': biblioteca.progreso_global,
        'por_estado': {
            'planificado': contar_por_estado(EstadoLibro.PLANIFICADO),
            'preparacion': contar_por_estado(EstadoLibro.PREPARACION),
            'en_proceso': contar_por_estado(EstadoLibro.EN_PROCESO),
            'completado': contar_por_estado(EstadoLibro.COMPLETADO),
        },
        'por_categoria': {
            'informatica': contar_por_categoria('INF'),
            'ingenieria': contar_por_categoria('ING'),
            'ciencias': contar_por_categoria('CIE'),
        },
        'fecha_actualizacion': biblioteca.fecha_actualizacion.isoformat()
    }


# =============================================================================
# FUNCIONES DE I/O (Side Effects Controlados)
# =============================================================================

def leer_biblioteca_desde_json(ruta: Path) -> Result.Ok | Result.Err:
    """
    Lee estado de biblioteca desde JSON.
    
    Side effect aislado en función específica.
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        libros = tuple(
            MetadataLibro(
                codigo=parsear_codigo(l['codigo']).unwrap(),
                titulo_original=l['titulo_original'],
                titulo_traducido=l['titulo_traducido'],
                autores=tuple(l['autores']),
                editorial=l['editorial'],
                año=l['año'],
                idioma_origen=l['idioma_origen'],
                idioma_destino=l['idioma_destino'],
                estado=EstadoLibro[l['estado']],
                progreso=l['progreso'],
                paginas_total=l['paginas_total'],
                paginas_traducidas=l['paginas_traducidas'],
                terminos_glosario=l['terminos_glosario'],
                fecha_inicio=date.fromisoformat(l['fecha_inicio']) if l.get('fecha_inicio') else None,
                ruta=Path(l['ruta']) if l.get('ruta') else None
            )
            for l in data['libros']
        )
        
        biblioteca = Biblioteca(
            libros=libros,
            fecha_actualizacion=datetime.fromisoformat(data['fecha_actualizacion'])
        )
        
        return Result.Ok(biblioteca)
    
    except Exception as e:
        return Result.Err(f"Error leyendo biblioteca: {str(e)}")


def escribir_biblioteca_a_json(
    biblioteca: Biblioteca,
    ruta: Path
) -> Result.Ok | Result.Err:
    """
    Escribe estado de biblioteca a JSON.
    
    Side effect aislado en función específica.
    """
    try:
        data = {
            'libros': [
                {
                    'codigo': str(l.codigo),
                    'titulo_original': l.titulo_original,
                    'titulo_traducido': l.titulo_traducido,
                    'autores': list(l.autores),
                    'editorial': l.editorial,
                    'año': l.año,
                    'idioma_origen': l.idioma_origen,
                    'idioma_destino': l.idioma_destino,
                    'estado': l.estado.name,
                    'progreso': l.progreso,
                    'paginas_total': l.paginas_total,
                    'paginas_traducidas': l.paginas_traducidas,
                    'terminos_glosario': l.terminos_glosario,
                    'fecha_inicio': l.fecha_inicio.isoformat() if l.fecha_inicio else None,
                    'ruta': str(l.ruta) if l.ruta else None
                }
                for l in biblioteca.libros
            ],
            'fecha_actualizacion': biblioteca.fecha_actualizacion.isoformat()
        }
        
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return Result.Ok(ruta)
    
    except Exception as e:
        return Result.Err(f"Error escribiendo biblioteca: {str(e)}")


def crear_estructura_directorio(ruta: Path) -> Result.Ok | Result.Err:
    """
    Crea estructura de directorios para un libro nuevo.
    
    Side effect aislado y controlado.
    """
    try:
        # Estructura de carpetas
        carpetas = [
            ruta,
            ruta / "original",
            ruta / "traduccion",
            ruta / "figuras",
            ruta / "front_matter",
            ruta / "back_matter",
            ruta / "appendices"
        ]
        
        # Crear carpetas
        for carpeta in carpetas:
            carpeta.mkdir(parents=True, exist_ok=True)
        
        # Crear archivos vacíos obligatorios
        archivos = [
            "metadata_libro.rst",
            "index.rst",
            "glosario_acumulativo.rst"
        ]
        
        for archivo in archivos:
            (ruta / archivo).touch()
        
        return Result.Ok(ruta)
    
    except Exception as e:
        return Result.Err(f"Error creando estructura: {str(e)}")


# =============================================================================
# CLI Y FUNCIONES PRINCIPALES
# =============================================================================

def clasificar_libro_interactivo(titulo: str) -> Result.Ok | Result.Err:
    """
    Clasifica un libro de forma interactiva.
    
    Esta es la función principal orquestadora.
    """
    print(f"\n{'='*70}")
    print(f"CLASIFICACIÓN DE LIBRO: {titulo}")
    print(f"{'='*70}\n")
    
    # PASO 1: Inferir categoría
    print("PASO 1: Determinando categoría...")
    resultado_cat = inferir_categoria_desde_titulo(titulo)
    
    if resultado_cat.is_err():
        return resultado_cat
    
    categoria = resultado_cat.unwrap()
    print(f"  → Categoría sugerida: {categoria}")
    
    # PASO 2: Inferir subcategoría (simplificado para demo)
    print("\nPASO 2: Determinando subcategoría...")
    if categoria == 'INF':
        resultado_sub = inferir_subcategoria_programacion(titulo)
    else:
        resultado_sub = Result.Ok('GEN')  # Simplificado
    
    if resultado_sub.is_err():
        return resultado_sub
    
    subcategoria = resultado_sub.unwrap()
    print(f"  → Subcategoría sugerida: {subcategoria}")
    
    # PASO 3: Inferir especialidad
    print("\nPASO 3: Determinando especialidad...")
    resultado_esp = inferir_especialidad_programacion(titulo)
    
    if resultado_esp.is_err():
        return resultado_esp
    
    especialidad = resultado_esp.unwrap()
    print(f"  → Especialidad sugerida: {especialidad}")
    
    # PASO 4: Generar código
    print("\nPASO 4: Generando código de clasificación...")
    
    # Para demo, asumimos sin códigos existentes
    codigos_existentes: Tuple[CodigoClasificacion, ...] = ()
    
    resultado_codigo = generar_codigo_siguiente(
        categoria,
        subcategoria,
        especialidad,
        codigos_existentes
    )
    
    if resultado_codigo.is_err():
        return resultado_codigo
    
    codigo = resultado_codigo.unwrap()
    
    print(f"\n{'='*70}")
    print(f"CÓDIGO ASIGNADO: {codigo}")
    print(f"{'='*70}\n")
    
    return Result.Ok(codigo)


def main():
    """Función principal del CLI."""
    import sys
    
    if len(sys.argv) < 2:
        print("""
Uso: python clasificador_biblioteca.py [comando]

Comandos:
    --clasificar "Título del Libro"    Clasificar un libro nuevo
    --validar /ruta/libro              Validar estructura de libro
    --demo                             Ejecutar demostración completa
    --help                             Mostrar esta ayuda
""")
        return
    
    comando = sys.argv[1]
    
    if comando == '--clasificar' and len(sys.argv) > 2:
        titulo = sys.argv[2]
        resultado = clasificar_libro_interactivo(titulo)
        
        if resultado.is_err():
            print(f"❌ ERROR: {resultado.error}")
            sys.exit(1)
        else:
            codigo = resultado.unwrap()
            print(f"✅ Clasificación completada exitosamente")
            print(f"   Código: {codigo}")
    
    elif comando == '--validar' and len(sys.argv) > 2:
        ruta = Path(sys.argv[2])
        resultado = validar_estructura_libro(ruta)
        
        if resultado.is_ok():
            print(f"✅ Estructura válida: {ruta}")
        else:
            print(f"❌ ERROR: {resultado.error}")
            sys.exit(1)
    
    elif comando == '--demo':
        ejecutar_demo()
    
    else:
        print("Comando no reconocido. Usa --help para ver ayuda.")
        sys.exit(1)


def ejecutar_demo():
    """Demostración completa del sistema."""
    print("\n" + "="*70)
    print(" DEMOSTRACIÓN DEL SISTEMA DE CLASIFICACIÓN ADT")
    print("="*70 + "\n")
    
    # Ejemplos de libros
    libros_ejemplo = [
        "Modern Full-Stack Development with TypeScript and React",
        "Machine Learning with Python: A Comprehensive Guide",
        "Docker Deep Dive",
        "Clean Architecture: A Craftsman's Guide to Software Structure",
        "Linear Algebra for Machine Learning"
    ]
    
    print("Clasificando libros de ejemplo...\n")
    
    for titulo in libros_ejemplo:
        resultado = clasificar_libro_interactivo(titulo)
        if resultado.is_ok():
            codigo = resultado.unwrap()
            print(f"✅ {titulo}")
            print(f"   → {codigo}\n")
        else:
            print(f"❌ {titulo}")
            print(f"   → ERROR: {resultado.error}\n")
    
    # Demostrar composición funcional
    print("\n" + "="*70)
    print(" DEMOSTRACIÓN DE PROGRAMACIÓN FUNCIONAL")
    print("="*70 + "\n")
    
    # Crear biblioteca de ejemplo
    codigos_ejemplo = [
        parsear_codigo("INF.PRG.FST.001").unwrap(),
        parsear_codigo("INF.IAR.MLF.001").unwrap(),
        parsear_codigo("ING.ARQ.CLE.001").unwrap(),
    ]
    
    libros = tuple(
        MetadataLibro(
            codigo=cod,
            titulo_original="Example Book",
            titulo_traducido="Libro de Ejemplo",
            autores=("Autor Ejemplo",),
            editorial="Editorial",
            año=2024,
            idioma_origen="en",
            idioma_destino="es",
            estado=EstadoLibro.EN_PROCESO,
            progreso=45.0,
            paginas_total=500,
            paginas_traducidas=225,
            terminos_glosario=150
        )
        for cod in codigos_ejemplo
    )
    
    biblioteca = Biblioteca(
        libros=libros,
        fecha_actualizacion=datetime.now()
    )
    
    # Demostrar funciones de alto orden
    print("1. Filtrar libros de Informática:")
    informatica = filter_libros(
        lambda l: l.codigo.categoria == 'INF'
    )(biblioteca.libros)
    print(f"   {len(informatica)} libros encontrados\n")
    
    print("2. Obtener todos los títulos:")
    titulos = map_libros(lambda l: l.titulo_traducido)(biblioteca.libros)
    for titulo in titulos:
        print(f"   - {titulo}")
    print()
    
    print("3. Calcular total de páginas:")
    total_pags = reduce_libros(
        lambda acc, l: acc + l.paginas_total,
        0
    )(biblioteca.libros)
    print(f"   {total_pags} páginas totales\n")
    
    print("4. Estadísticas completas:")
    stats = calcular_estadisticas(biblioteca)
    print(json.dumps(stats, indent=2))
    
    print("\n" + "="*70)
    print(" FIN DE LA DEMOSTRACIÓN")
    print("="*70 + "\n")


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    main()
