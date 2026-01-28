#!/bin/bash
################################################################################
# Script: init_capitulo.sh
# Versión: 1.0.0
# Descripción: Crear estructura de un capítulo/sección nuevo en un libro
# Uso: ./scripts/init_capitulo.sh <ruta_libro> <nombre_capitulo>
# Ejemplo: ./scripts/init_capitulo.sh biblioteca/arc42 introduction_goals
################################################################################

set -e

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Verificar argumentos
if [ $# -lt 1 ]; then
    echo -e "${RED}Uso: $0 <ruta_libro> [nombre_capitulo]${NC}"
    echo "Ejemplo: $0 biblioteca/arc42 introduction_goals"
    exit 1
fi

RUTA_LIBRO="$1"
NOMBRE_CAPITULO="${2:-}"

# Si no se proporciona nombre, preguntar
if [ -z "$NOMBRE_CAPITULO" ]; then
    echo -e "${YELLOW}Crear capítulo en: ${RUTA_LIBRO}${NC}"
    read -p "Nombre del capítulo (snake_case, sin números): " NOMBRE_CAPITULO
fi

# Verificar que la ruta del libro existe
if [ ! -d "source/${RUTA_LIBRO}" ]; then
    echo -e "${RED}❌ Error: La ruta source/${RUTA_LIBRO} no existe${NC}"
    exit 1
fi

RUTA_CAPITULO="source/${RUTA_LIBRO}/${NOMBRE_CAPITULO}"

echo ""
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo -e "${BLUE}   CREAR CAPÍTULO: ${NOMBRE_CAPITULO}${NC}"
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo ""

# Crear estructura
mkdir -p "${RUTA_CAPITULO}/original"
mkdir -p "${RUTA_CAPITULO}/traduccion"
mkdir -p "${RUTA_CAPITULO}/figuras"
mkdir -p "${RUTA_CAPITULO}/diagramas"

# Crear archivos base
cat > "${RUTA_CAPITULO}/glosario_capitulo.rst" << 'EOF'
.. glossary::
   :sorted:

   [Términos del capítulo - agregar conforme se traducen]
EOF

cat > "${RUTA_CAPITULO}/notas_traduccion.rst" << 'EOF'
Notas de Traducción
===================

Decisiones Importantes
----------------------

[Documentar decisiones de traducción importantes]

Divergencias del Método por Defecto
------------------------------------

[Documentar cuando se diverge del método por defecto]

Objetivo: [Domesticación/Claridad/Consistencia/Simplificación]
Táctica: [Nombre de la táctica]
Razón: [Explicación]

Problemas Encontrados
---------------------

[Documentar problemas y cómo se resolvieron]
EOF

# Crear README en original/
cat > "${RUTA_CAPITULO}/original/README.md" << EOF
# Original: ${NOMBRE_CAPITULO}

Colocar aquí los archivos originales del capítulo:
- PDF
- LaTeX (.tex)
- Markdown (.md)
- Otros formatos

## Archivos

- [\`original.pdf\`] - Documento original
EOF

# Crear plantilla de traducción
TITULO_CAPITULO=$(echo "${NOMBRE_CAPITULO}" | tr '_' ' ' | sed 's/.*/\L&/; s/[a-z]*/\u&/g')

cat > "${RUTA_CAPITULO}/traduccion/capitulo.rst" << EOF
========================================
${TITULO_CAPITULO}
========================================

.. note::
   **Estado:** Borrador
   **Fecha inicio:** $(date +%Y-%m-%d)

----

[Contenido de la traducción]

----

Referencias
===========

.. seealso::
   - :doc:`../glosario_capitulo`
   - :doc:`../notas_traduccion`
EOF

echo -e "${GREEN}✅ Estructura creada en:${NC}"
echo "   ${RUTA_CAPITULO}"
echo ""
echo -e "${GREEN}Archivos creados:${NC}"
echo "   ✅ glosario_capitulo.rst"
echo "   ✅ notas_traduccion.rst"
echo "   ✅ original/README.md"
echo "   ✅ traduccion/capitulo.rst"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "   1. Copiar archivos originales a ${NOMBRE_CAPITULO}/original/"
echo "   2. Editar ${NOMBRE_CAPITULO}/traduccion/capitulo.rst"
echo "   3. Actualizar ${NOMBRE_CAPITULO}/glosario_capitulo.rst"
echo "   4. Documentar decisiones en ${NOMBRE_CAPITULO}/notas_traduccion.rst"
echo ""
