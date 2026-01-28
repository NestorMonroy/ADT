#!/bin/bash
################################################################################
# Script: init_libro.sh
# Versión: 1.0.0
# Descripción: Inicializar estructura completa de un libro nuevo en biblioteca/
# Autor: Equipo ADT
# Fecha: 2026-01-27
################################################################################

set -e  # Exit on error

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}   INICIALIZACIÓN DE LIBRO NUEVO EN BIBLIOTECA v1.0.0      ${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

# Verificar que estamos en la raíz del proyecto
if [ ! -d "source/biblioteca" ]; then
    echo -e "${RED}❌ Error: Ejecutar desde la raíz del proyecto ADT${NC}"
    exit 1
fi

# ==============================================================================
# PASO 1: Solicitar información del libro
# ==============================================================================

echo -e "${YELLOW}PASO 1: Información del Libro${NC}"
echo ""

read -p "Título del libro (ej: Modern Full Stack Development): " TITULO
read -p "Autor(es): " AUTOR
read -p "Editorial: " EDITORIAL
read -p "Año de publicación: " ANIO
read -p "Edición (ej: 2ed, 3ed): " EDICION
read -p "ISBN (opcional): " ISBN

echo ""
echo -e "${YELLOW}PASO 2: Clasificación Documental${NC}"
echo ""
echo "Categorías disponibles:"
echo "  1) informatica"
echo "  2) ingenieria"
echo "  3) ciencias"
read -p "Seleccionar categoría [1-3]: " CAT_NUM

case $CAT_NUM in
    1) CATEGORIA="informatica" ;;
    2) CATEGORIA="ingenieria" ;;
    3) CATEGORIA="ciencias" ;;
    *) echo -e "${RED}Opción inválida${NC}"; exit 1 ;;
esac

read -p "Subcategoría (ej: programacion, sistemas, biologia): " SUBCATEGORIA
read -p "Especialidad (ej: full_stack, python, uml): " ESPECIALIDAD

# Generar código de clasificación
# Formato: CAT.SUB.ESP.NUM
PREFIJO_CAT=$(echo "$CATEGORIA" | cut -c1-3 | tr '[:lower:]' '[:upper:]')
PREFIJO_SUB=$(echo "$SUBCATEGORIA" | cut -c1-3 | tr '[:lower:]' '[:upper:]')
PREFIJO_ESP=$(echo "$ESPECIALIDAD" | cut -c1-3 | tr '[:lower:]' '[:upper:]')

# Contar libros existentes en esta especialidad
RUTA_ESPECIALIDAD="source/biblioteca/$CATEGORIA/$SUBCATEGORIA/$ESPECIALIDAD"
if [ -d "$RUTA_ESPECIALIDAD" ]; then
    NUM_LIBROS=$(find "$RUTA_ESPECIALIDAD" -maxdepth 1 -type d ! -path "$RUTA_ESPECIALIDAD" | wc -l)
    NUM_LIBRO=$(printf "%03d" $((NUM_LIBROS + 1)))
else
    NUM_LIBRO="001"
fi

CODIGO_CLASIFICACION="${PREFIJO_CAT}.${PREFIJO_SUB}.${PREFIJO_ESP}.${NUM_LIBRO}"
LIBRO_ID="LIB_${PREFIJO_CAT}_${PREFIJO_ESP}_${NUM_LIBRO}"

echo ""
echo -e "${GREEN}Código de clasificación: ${CODIGO_CLASIFICACION}${NC}"
echo -e "${GREEN}Libro ID: ${LIBRO_ID}${NC}"

# ==============================================================================
# PASO 3: Generar nombre de carpeta del libro
# ==============================================================================

echo ""
echo -e "${YELLOW}PASO 3: Nombre de Carpeta del Libro${NC}"
echo ""

# Convertir título a snake_case
NOMBRE_CARPETA=$(echo "$TITULO" | \
    tr '[:upper:]' '[:lower:]' | \
    tr -s ' ' '_' | \
    tr -cd '[:alnum:]_')

# Agregar autor y edición si existe
AUTOR_CORTO=$(echo "$AUTOR" | awk '{print $NF}' | tr '[:upper:]' '[:lower:]')
if [ ! -z "$EDICION" ]; then
    NOMBRE_CARPETA="${NOMBRE_CARPETA}_${AUTOR_CORTO}_${EDICION}"
else
    NOMBRE_CARPETA="${NOMBRE_CARPETA}_${AUTOR_CORTO}"
fi

echo "Nombre sugerido: ${NOMBRE_CARPETA}"
read -p "¿Usar este nombre? [S/n]: " CONFIRMAR

if [ "$CONFIRMAR" = "n" ] || [ "$CONFIRMAR" = "N" ]; then
    read -p "Ingresar nombre personalizado (snake_case): " NOMBRE_CARPETA
fi

# ==============================================================================
# PASO 4: Crear estructura de directorios
# ==============================================================================

echo ""
echo -e "${YELLOW}PASO 4: Creando Estructura...${NC}"
echo ""

RUTA_LIBRO="source/biblioteca/$CATEGORIA/$SUBCATEGORIA/$ESPECIALIDAD/$NOMBRE_CARPETA"

# Crear jerarquía
mkdir -p "$RUTA_LIBRO"

echo -e "${GREEN}✅ Carpeta del libro creada:${NC}"
echo "   $RUTA_LIBRO"

# Crear archivos base del libro
touch "$RUTA_LIBRO/index.rst"
touch "$RUTA_LIBRO/metadata_libro.rst"
touch "$RUTA_LIBRO/glosario_acumulativo.rst"

# Crear carpetas adicionales
mkdir -p "$RUTA_LIBRO/front_matter"
mkdir -p "$RUTA_LIBRO/back_matter"

echo -e "${GREEN}✅ Archivos base creados${NC}"

# ==============================================================================
# PASO 5: Generar metadata_libro.rst
# ==============================================================================

echo ""
echo -e "${YELLOW}PASO 5: Generando metadata_libro.rst...${NC}"
echo ""

cat > "$RUTA_LIBRO/metadata_libro.rst" << EOF
.. meta::
   :libro_id: ${LIBRO_ID}
   :tipo: Libro_Tecnico
   :estado: Iniciado
   :progreso: 0%
   :clasificacion: ${CODIGO_CLASIFICACION}
   :fecha_inicio: $(date +%Y-%m-%d)
   :version: 1.0.0

.. _libro-${LIBRO_ID}:

========================================
${TITULO}
========================================

Información Bibliográfica
==========================

Título Original
   ${TITULO}

Autor(es)
   ${AUTOR}

Editorial
   ${EDITORIAL}

Año de Publicación
   ${ANIO}

${ISBN:+ISBN
   ${ISBN}
}
Edición
   ${EDICION:-Primera edición}

Idiomas
   - Fuente: [Especificar idioma original]
   - Destino: Español (es)

Clasificación según Guía Metodológica
======================================

Código de Clasificación
   ${CODIGO_CLASIFICACION}

Categoría Principal
   ${CATEGORIA^}

Subcategoría
   ${SUBCATEGORIA^}

Especialidad
   ${ESPECIALIDAD^}

Nivel
   [Básico/Intermedio/Avanzado]

Público Objetivo
   [Especificar audiencia]

Palabras Clave
   [Agregar palabras clave separadas por comas]

Estado de Traducción
=====================

Progreso Global
   0% completado (0 capítulos)

Capítulos Completados
   (Ninguno aún)

Capítulos En Proceso
   (Ninguno aún)

Fecha Inicio
   $(date +%Y-%m-%d)

Fecha Estimada Finalización
   [A determinar]

Equipo de Traducción
====================

Traductor Principal
   [Nombre]

Revisores Técnicos
   - [Revisor 1]
   - [Revisor 2]

Procedimientos Aplicados
=========================

- :doc:`/02_procedimientos/workflow_general`
- [Otros procedimientos según necesidad]

Notas Adicionales
=================

[Agregar notas específicas del libro]

----

**Versión:** 1.0.0  
**Fecha Creación:** $(date +%Y-%m-%d)  
**Estado:** Iniciado
EOF

echo -e "${GREEN}✅ metadata_libro.rst creado${NC}"

# ==============================================================================
# PASO 6: Generar index.rst del libro
# ==============================================================================

echo ""
echo -e "${YELLOW}PASO 6: Generando index.rst...${NC}"
echo ""

cat > "$RUTA_LIBRO/index.rst" << EOF
.. _libro-${NOMBRE_CARPETA}:

========================================
${TITULO}
========================================

.. include:: metadata_libro.rst

----

Contenido del Libro
===================

.. toctree::
   :maxdepth: 2
   :caption: Front Matter

   front_matter/about_author
   front_matter/acknowledgments
   front_matter/introduction

.. toctree::
   :maxdepth: 2
   :caption: Capítulos

   [A agregar según se traduzcan]

.. toctree::
   :maxdepth: 2
   :caption: Back Matter

   back_matter/index_alfabetico
   glosario_acumulativo

----

Progreso de Traducción
=======================

Ver :doc:`metadata_libro` para detalles completos.

----

Referencias
===========

- :doc:`/biblioteca/_metadata_biblioteca/META_BIB_001_Sistema_Clasificacion_1_0_0`
- :doc:`/02_procedimientos/workflow_general`
EOF

echo -e "${GREEN}✅ index.rst creado${NC}"

# ==============================================================================
# PASO 7: Generar glosario_acumulativo.rst (vacío inicial)
# ==============================================================================

cat > "$RUTA_LIBRO/glosario_acumulativo.rst" << EOF
.. _glosario-${NOMBRE_CARPETA}:

========================================
Glosario Acumulativo: ${TITULO}
========================================

Este glosario se genera automáticamente consolidando todos los 
\`\`glosario_capitulo.rst\`\` de cada capítulo.

.. glossary::
   :sorted:

   [Los términos se agregarán automáticamente]

----

**Última actualización:** $(date +%Y-%m-%d)  
**Total de términos:** 0
EOF

echo -e "${GREEN}✅ glosario_acumulativo.rst creado${NC}"

# ==============================================================================
# PASO 8: Resumen final
# ==============================================================================

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ LIBRO INICIALIZADO EXITOSAMENTE${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}Información del Libro:${NC}"
echo "  Título: $TITULO"
echo "  Autor: $AUTOR"
echo "  Clasificación: $CODIGO_CLASIFICACION"
echo "  Libro ID: $LIBRO_ID"
echo ""
echo -e "${YELLOW}Ubicación:${NC}"
echo "  $RUTA_LIBRO"
echo ""
echo -e "${YELLOW}Archivos creados:${NC}"
echo "  ✅ metadata_libro.rst"
echo "  ✅ index.rst"
echo "  ✅ glosario_acumulativo.rst"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "  1. Editar metadata_libro.rst (completar información)"
echo "  2. Crear capítulos con: ./scripts/init_capitulo.sh"
echo "  3. Seguir workflow en: 02_procedimientos/workflow_general.rst"
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
