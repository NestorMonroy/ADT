#!/bin/bash
################################################################################
# Script: progreso_libro.sh
# Versión: 1.0.0
# Descripción: Calcular progreso de traducción de un libro
# Uso: ./scripts/progreso_libro.sh <ruta_libro>
# Ejemplo: ./scripts/progreso_libro.sh biblioteca/arc42
################################################################################

set -e

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

if [ $# -lt 1 ]; then
    echo -e "${RED}Uso: $0 <ruta_libro>${NC}"
    echo "Ejemplo: $0 biblioteca/arc42"
    exit 1
fi

RUTA_LIBRO="source/$1"

if [ ! -d "$RUTA_LIBRO" ]; then
    echo -e "${RED}❌ Error: La ruta ${RUTA_LIBRO} no existe${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}   PROGRESO DE TRADUCCIÓN${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""

# Contar total de capítulos (carpetas que NO son front_matter, back_matter, etc.)
TOTAL_CAPITULOS=$(find "$RUTA_LIBRO" -mindepth 1 -maxdepth 1 -type d \
    ! -name "front_matter" \
    ! -name "back_matter" \
    ! -name "sections" \
    ! -name ".*" | wc -l)

# Si usa subcarpeta sections/ (como arc42)
if [ -d "$RUTA_LIBRO/sections" ]; then
    TOTAL_CAPITULOS=$(find "$RUTA_LIBRO/sections" -mindepth 1 -maxdepth 1 -type d | wc -l)
    RUTA_CAPITULOS="$RUTA_LIBRO/sections"
else
    RUTA_CAPITULOS="$RUTA_LIBRO"
fi

# Contar capítulos con traducción (que tienen archivos .rst en traduccion/)
CAPITULOS_TRADUCIDOS=0
CAPITULOS_VACIOS=0

echo -e "${CYAN}Analizando capítulos...${NC}"
echo ""

# Listar capítulos y su estado
for capitulo in $(find "$RUTA_CAPITULOS" -mindepth 1 -maxdepth 1 -type d | sort); do
    NOMBRE_CAP=$(basename "$capitulo")
    
    # Verificar si tiene traducción
    if [ -d "$capitulo/traduccion" ]; then
        NUM_ARCHIVOS=$(find "$capitulo/traduccion" -name "*.rst" -type f ! -size 0 | wc -l)
        
        if [ $NUM_ARCHIVOS -gt 0 ]; then
            echo -e "  ${GREEN}✅ ${NOMBRE_CAP}${NC} - Traducido ($NUM_ARCHIVOS archivos)"
            CAPITULOS_TRADUCIDOS=$((CAPITULOS_TRADUCIDOS + 1))
        else
            echo -e "  ${YELLOW}🔄 ${NOMBRE_CAP}${NC} - En proceso (sin contenido)"
            CAPITULOS_VACIOS=$((CAPITULOS_VACIOS + 1))
        fi
    else
        echo -e "  ${RED}❌ ${NOMBRE_CAP}${NC} - Sin traducir"
    fi
done

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}RESUMEN${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Total de capítulos:      ${TOTAL_CAPITULOS}"
echo -e "  ${GREEN}Traducidos:              ${CAPITULOS_TRADUCIDOS}${NC}"
echo -e "  ${YELLOW}En proceso:              ${CAPITULOS_VACIOS}${NC}"
echo -e "  ${RED}Pendientes:              $((TOTAL_CAPITULOS - CAPITULOS_TRADUCIDOS - CAPITULOS_VACIOS))${NC}"
echo ""

# Calcular porcentaje
if [ $TOTAL_CAPITULOS -gt 0 ]; then
    PORCENTAJE=$((CAPITULOS_TRADUCIDOS * 100 / TOTAL_CAPITULOS))
    echo -e "  ${CYAN}Progreso:                ${PORCENTAJE}%${NC}"
    
    # Barra de progreso visual
    BARRAS=$((PORCENTAJE / 5))  # 20 barras = 100%
    BARRA_PROGRESO=""
    for i in $(seq 1 20); do
        if [ $i -le $BARRAS ]; then
            BARRA_PROGRESO="${BARRA_PROGRESO}█"
        else
            BARRA_PROGRESO="${BARRA_PROGRESO}░"
        fi
    done
    
    echo -e "  ${CYAN}[${BARRA_PROGRESO}] ${PORCENTAJE}%${NC}"
else
    PORCENTAJE=0
fi

echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════${NC}"
echo ""

# Actualizar metadata_libro.rst si existe
METADATA="$RUTA_LIBRO/metadata_libro.rst"
if [ -f "$METADATA" ]; then
    echo -e "${YELLOW}Actualizando metadata_libro.rst...${NC}"
    
    # Actualizar progreso
    if grep -q ":progreso:" "$METADATA"; then
        sed -i "s/:progreso:.*/:progreso: ${PORCENTAJE}%/" "$METADATA"
    else
        # Agregar si no existe
        sed -i "/^.. meta::/a\   :progreso: ${PORCENTAJE}%" "$METADATA"
    fi
    
    # Actualizar fecha de actualización
    sed -i "s/Última actualización:.*/Última actualización: $(date +%Y-%m-%d)/" "$METADATA"
    
    echo -e "${GREEN}✅ metadata_libro.rst actualizado${NC}"
else
    echo -e "${YELLOW}⚠️  metadata_libro.rst no encontrado${NC}"
fi

echo ""
