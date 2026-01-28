#!/bin/bash
################################################################################
# Script: validar_estructura.sh
# Versión: 1.0.0
# Descripción: Validar que un libro cumple con la Guía Metodológica
# Uso: ./scripts/validar_estructura.sh <ruta_libro>
################################################################################

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ $# -lt 1 ]; then
    echo -e "${RED}Uso: $0 <ruta_libro>${NC}"
    exit 1
fi

RUTA_LIBRO="source/$1"

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}   VALIDACIÓN DE ESTRUCTURA - v1.0.0${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""
echo "Validando: $1"
echo ""

ERRORES=0
WARNINGS=0

# 1. Verificar que existe metadata_libro.rst
echo -e "${YELLOW}[1/8] metadata_libro.rst...${NC}"
if [ -f "$RUTA_LIBRO/metadata_libro.rst" ]; then
    echo -e "  ${GREEN}✅ Existe${NC}"
    
    # Verificar campos obligatorios
    if grep -q ":libro_id:" "$RUTA_LIBRO/metadata_libro.rst"; then
        echo -e "  ${GREEN}✅ Tiene libro_id${NC}"
    else
        echo -e "  ${RED}❌ Falta libro_id${NC}"
        ERRORES=$((ERRORES + 1))
    fi
    
    if grep -q ":clasificacion:" "$RUTA_LIBRO/metadata_libro.rst"; then
        echo -e "  ${GREEN}✅ Tiene clasificación${NC}"
    else
        echo -e "  ${RED}❌ Falta clasificación${NC}"
        ERRORES=$((ERRORES + 1))
    fi
    
    if grep -q ":progreso:" "$RUTA_LIBRO/metadata_libro.rst"; then
        echo -e "  ${GREEN}✅ Tiene progreso${NC}"
    else
        echo -e "  ${YELLOW}⚠️  Falta progreso${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "  ${RED}❌ metadata_libro.rst NO EXISTE${NC}"
    ERRORES=$((ERRORES + 1))
fi

# 2. Verificar index.rst
echo ""
echo -e "${YELLOW}[2/8] index.rst...${NC}"
if [ -f "$RUTA_LIBRO/index.rst" ]; then
    echo -e "  ${GREEN}✅ Existe${NC}"
else
    echo -e "  ${RED}❌ index.rst NO EXISTE${NC}"
    ERRORES=$((ERRORES + 1))
fi

# 3. Verificar glosario_acumulativo.rst
echo ""
echo -e "${YELLOW}[3/8] glosario_acumulativo.rst...${NC}"
if [ -f "$RUTA_LIBRO/glosario_acumulativo.rst" ]; then
    echo -e "  ${GREEN}✅ Existe${NC}"
else
    echo -e "  ${YELLOW}⚠️  glosario_acumulativo.rst no existe${NC}"
    WARNINGS=$((WARNINGS + 1))
fi

# 4. Verificar estructura de capítulos
echo ""
echo -e "${YELLOW}[4/8] Estructura de capítulos...${NC}"

# Buscar carpeta de capítulos
if [ -d "$RUTA_LIBRO/sections" ]; then
    RUTA_CAPS="$RUTA_LIBRO/sections"
elif [ -d "$RUTA_LIBRO/chapters" ]; then
    RUTA_CAPS="$RUTA_LIBRO/chapters"
else
    RUTA_CAPS="$RUTA_LIBRO"
fi

CAPITULOS=$(find "$RUTA_CAPS" -mindepth 1 -maxdepth 1 -type d \
    ! -name "front_matter" \
    ! -name "back_matter" \
    ! -name ".*" | wc -l)

if [ $CAPITULOS -gt 0 ]; then
    echo -e "  ${GREEN}✅ ${CAPITULOS} capítulos encontrados${NC}"
else
    echo -e "  ${RED}❌ No se encontraron capítulos${NC}"
    ERRORES=$((ERRORES + 1))
fi

# 5. Verificar que capítulos tengan estructura correcta
echo ""
echo -e "${YELLOW}[5/8] Validando estructura interna de capítulos...${NC}"

CAPS_VALIDOS=0
for capitulo in $(find "$RUTA_CAPS" -mindepth 1 -maxdepth 1 -type d \
    ! -name "front_matter" \
    ! -name "back_matter" \
    ! -name ".*"); do
    
    NOMBRE_CAP=$(basename "$capitulo")
    
    # Verificar nomenclatura
    # NOTA: Los números en sections/ están PERMITIDOS (ej: sections/01_introduction/)
    # NOM_001 solo prohíbe números al inicio del nombre del LIBRO, no de las secciones
    if [[ "$NOMBRE_CAP" =~ ^[0-9] ]]; then
        # Números están permitidos en nombres de secciones
        echo -e "  ${GREEN}✅ ${NOMBRE_CAP} - nombre correcto (con número)${NC}"
    else
        echo -e "  ${GREEN}✅ ${NOMBRE_CAP} - nombre correcto${NC}"
    fi
    
    # Verificar subcarpetas
    TIENE_ORIGINAL=0
    TIENE_TRADUCCION=0
    
    [ -d "$capitulo/original" ] && TIENE_ORIGINAL=1
    [ -d "$capitulo/traduccion" ] && TIENE_TRADUCCION=1
    
    if [ $TIENE_ORIGINAL -eq 1 ] && [ $TIENE_TRADUCCION -eq 1 ]; then
        CAPS_VALIDOS=$((CAPS_VALIDOS + 1))
    else
        if [ $TIENE_ORIGINAL -eq 0 ]; then
            echo -e "     ${YELLOW}⚠️  Falta carpeta original/${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
        if [ $TIENE_TRADUCCION -eq 0 ]; then
            echo -e "     ${YELLOW}⚠️  Falta carpeta traduccion/${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done

# 6. Verificar nombres en snake_case
echo ""
echo -e "${YELLOW}[6/8] Validando nomenclatura snake_case...${NC}"

CAPS_INCORRECTOS=0
for capitulo in $(find "$RUTA_CAPS" -mindepth 1 -maxdepth 1 -type d \
    ! -name "front_matter" \
    ! -name "back_matter" \
    ! -name ".*"); do
    
    NOMBRE_CAP=$(basename "$capitulo")
    
    # Verificar que solo tenga letras minúsculas, números y guiones bajos
    if [[ "$NOMBRE_CAP" =~ ^[a-z0-9_]+$ ]]; then
        : # Correcto
    else
        echo -e "  ${RED}❌ ${NOMBRE_CAP} - no es snake_case válido${NC}"
        CAPS_INCORRECTOS=$((CAPS_INCORRECTOS + 1))
        ERRORES=$((ERRORES + 1))
    fi
done

if [ $CAPS_INCORRECTOS -eq 0 ]; then
    echo -e "  ${GREEN}✅ Todos los nombres en snake_case${NC}"
fi

# 7. Verificar que haya al menos 1 capítulo traducido
echo ""
echo -e "${YELLOW}[7/8] Verificando contenido traducido...${NC}"

CAPS_CON_CONTENIDO=0
for capitulo in $(find "$RUTA_CAPS" -mindepth 1 -maxdepth 1 -type d); do
    if [ -d "$capitulo/traduccion" ]; then
        NUM_RST=$(find "$capitulo/traduccion" -name "*.rst" -type f ! -size 0 | wc -l)
        if [ $NUM_RST -gt 0 ]; then
            CAPS_CON_CONTENIDO=$((CAPS_CON_CONTENIDO + 1))
        fi
    fi
done

if [ $CAPS_CON_CONTENIDO -gt 0 ]; then
    echo -e "  ${GREEN}✅ ${CAPS_CON_CONTENIDO} capítulos con contenido${NC}"
else
    echo -e "  ${YELLOW}⚠️  No hay capítulos con contenido traducido${NC}"
    WARNINGS=$((WARNINGS + 1))
fi

# 8. Verificar clasificación documental
echo ""
echo -e "${YELLOW}[8/8] Verificando clasificación documental...${NC}"

if [ -f "$RUTA_LIBRO/metadata_libro.rst" ]; then
    CLASIFICACION=$(grep ":clasificacion:" "$RUTA_LIBRO/metadata_libro.rst" | awk '{print $2}')
    
    if [ ! -z "$CLASIFICACION" ]; then
        # Verificar formato CAT.SUB.ESP.NUM
        if [[ "$CLASIFICACION" =~ ^[A-Z]{3}\.[A-Z]{3}\.[A-Z]{3}\.[0-9]{3}$ ]]; then
            echo -e "  ${GREEN}✅ Clasificación válida: ${CLASIFICACION}${NC}"
        else
            echo -e "  ${RED}❌ Formato de clasificación incorrecto: ${CLASIFICACION}${NC}"
            echo -e "     Formato esperado: XXX.XXX.XXX.NNN"
            ERRORES=$((ERRORES + 1))
        fi
    fi
fi

# RESUMEN FINAL
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}   RESUMEN DE VALIDACIÓN${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""
echo -e "  Libro: $1"
echo -e "  Capítulos encontrados: ${CAPITULOS}"
echo -e "  Capítulos válidos: ${CAPS_VALIDOS}"
echo -e "  Capítulos traducidos: ${CAPS_CON_CONTENIDO}"
echo ""

if [ $ERRORES -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ VALIDACIÓN EXITOSA - Sin errores ni advertencias${NC}"
    exit 0
elif [ $ERRORES -eq 0 ]; then
    echo -e "${YELLOW}⚠️  VALIDACIÓN CON ADVERTENCIAS${NC}"
    echo -e "  Advertencias: ${WARNINGS}"
    echo ""
    exit 0
else
    echo -e "${RED}❌ VALIDACIÓN FALLIDA${NC}"
    echo -e "  Errores: ${ERRORES}"
    echo -e "  Advertencias: ${WARNINGS}"
    echo ""
    exit 1
fi
