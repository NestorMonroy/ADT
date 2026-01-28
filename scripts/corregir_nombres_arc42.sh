#!/bin/bash
################################################################################
# Script: corregir_nombres_arc42.sh
# Versión: 1.0.0
# Descripción: Renombrar carpetas de arc42 para cumplir con NOM_001
#              (eliminar números del inicio)
################################################################################

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

RUTA_ARC42="source/biblioteca/arc42/sections"

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo -e "${BLUE}   CORREGIR NOMBRES ARC42 - v1.0.0${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════${NC}"
echo ""
echo "Renombrando carpetas para cumplir con NOM_001"
echo "(Eliminar números del inicio, mantener orden con metadata)"
echo ""

if [ ! -d "$RUTA_ARC42" ]; then
    echo "❌ Error: $RUTA_ARC42 no existe"
    exit 1
fi

cd "$RUTA_ARC42"

# Mapeo de nombres antiguos -> nuevos
declare -A RENOMBRES=(
    ["01_introduction_goals"]="introduction_goals"
    ["02_constraints"]="constraints"
    ["03_context"]="context_scope"
    ["04_solution_strategy"]="solution_strategy"
    ["05_building_blocks"]="building_blocks"
    ["06_runtime"]="runtime_view"
    ["07_deployment"]="deployment_view"
    ["08_concepts"]="crosscutting_concepts"
    ["09_decisions"]="architecture_decisions"
    ["10_quality"]="quality_requirements"
    ["11_risks_tech_debt"]="risks_tech_debt"
    ["12_glossary"]="glossary"
)

echo -e "${YELLOW}Renombramientos a realizar:${NC}"
for ANTIGUO in "${!RENOMBRES[@]}"; do
    NUEVO="${RENOMBRES[$ANTIGUO]}"
    if [ -d "$ANTIGUO" ]; then
        echo "  $ANTIGUO → $NUEVO"
    fi
done

echo ""
read -p "¿Continuar con el renombramiento? [S/n]: " CONFIRMAR

if [ "$CONFIRMAR" = "n" ] || [ "$CONFIRMAR" = "N" ]; then
    echo "Operación cancelada"
    exit 0
fi

echo ""
echo -e "${YELLOW}Renombrando...${NC}"

# Renombrar carpetas
for ANTIGUO in "${!RENOMBRES[@]}"; do
    NUEVO="${RENOMBRES[$ANTIGUO]}"
    if [ -d "$ANTIGUO" ]; then
        mv "$ANTIGUO" "$NUEVO"
        echo -e "  ${GREEN}✅ $ANTIGUO → $NUEVO${NC}"
        
        # Actualizar metadata en traducción si existe
        if [ -f "$NUEVO/traduccion/seccion_"*".rst" ]; then
            # Agregar metadata con número de sección
            NUMERO=$(echo "$ANTIGUO" | grep -o '^[0-9]*')
            if [ ! -z "$NUMERO" ]; then
                # Buscar archivo .rst y agregar metadata al inicio
                for RST in "$NUEVO/traduccion"/*.rst; do
                    if [ -f "$RST" ]; then
                        # Crear temp con metadata
                        cat > /tmp/temp_meta.rst << EOF
.. meta::
   :seccion_numero: $NUMERO
   :orden: $NUMERO

EOF
                        # Verificar si ya tiene metadata
                        if ! grep -q ".. meta::" "$RST"; then
                            cat /tmp/temp_meta.rst "$RST" > /tmp/temp_full.rst
                            mv /tmp/temp_full.rst "$RST"
                            echo -e "     ${GREEN}✅ Metadata agregada${NC}"
                        fi
                    fi
                done
            fi
        fi
    fi
done

echo ""
echo -e "${GREEN}✅ Renombramiento completado${NC}"
echo ""
echo -e "${YELLOW}IMPORTANTE:${NC}"
echo "  - Los números de sección se preservan en metadata"
echo "  - Actualizar referencias en index.rst si es necesario"
echo "  - Ejecutar ./scripts/validar_estructura.sh para verificar"
echo ""
