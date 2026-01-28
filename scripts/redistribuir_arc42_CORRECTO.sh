#!/bin/bash
################################################################################
# Script: redistribuir_arc42_CORRECTO.sh
# Versión: 2.0.0 (CORREGIDO)
# Descripción: Redistribuir archivos arc42 usando estructura REAL del repositorio
#
# CORRECCIÓN: El repo YA está organizado en _posts/XX-seccion/
# No necesitamos buscar por palabras clave, solo copiar las carpetas
################################################################################

set -e

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Variables
DRY_RUN=0
LIBRO_BASE="/tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation"
ORIGINAL_REPO="${LIBRO_BASE}/original"
SECTIONS_BASE="${LIBRO_BASE}/sections"

# Procesar argumentos
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run|-n)
            DRY_RUN=1
            shift
            ;;
        --help|-h)
            echo "Uso: $0 [--dry-run]"
            echo ""
            echo "Redistribuye archivos arc42 CORRECTAMENTE usando la estructura"
            echo "real del repositorio (_posts/XX-seccion/)"
            echo ""
            echo "CORRIGE el error del script anterior que buscaba por palabras clave"
            exit 0
            ;;
        *)
            echo -e "${RED}Opción desconocida: $1${NC}"
            exit 1
            ;;
    esac
done

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}   REDISTRIBUIR ARCHIVOS ARC42 (VERSIÓN CORREGIDA) v2.0.0${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   MODO: DRY-RUN${NC}"
fi
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Mapeo correcto: carpeta en _posts/ → carpeta en sections/
declare -A MAPEO=(
    ["01-requirements"]="01_introduction_goals"
    ["02-constraints"]="02_constraints"
    ["03-context"]="03_context_scope"
    ["04-strategy"]="04_solution_strategy"
    ["05-buildingblocks"]="05_building_blocks"
    ["06-runtime"]="06_runtime_view"
    ["07-deployment"]="07_deployment_view"
    ["08-concepts"]="08_concepts"
    ["09-decisions"]="09_architecture_decisions"
    ["10-quality"]="10_quality"
    ["11-risks"]="11_risks_tech_debt"
    ["12-glossary"]="12_glossary"
)

echo -e "${MAGENTA}[PASO 1/3]${NC} Limpiar distribución anterior incorrecta"
echo ""

for seccion in "${!MAPEO[@]}"; do
    seccion_destino="${MAPEO[$seccion]}"
    dest_dir="${SECTIONS_BASE}/${seccion_destino}/original"
    
    if [ -d "$dest_dir" ]; then
        # Contar archivos actuales
        count_actual=$(find "$dest_dir" -name "*.md" ! -name "README.md" | wc -l)
        
        if [ $count_actual -gt 0 ]; then
            echo -e "${YELLOW}⚠️  ${seccion_destino}: ${count_actual} archivos${NC}"
            
            if [ $DRY_RUN -eq 0 ]; then
                # Eliminar solo archivos .md, NO README.md
                find "$dest_dir" -name "*.md" ! -name "README.md" -delete
                echo -e "${GREEN}   Limpiado${NC}"
            fi
        fi
    fi
done

echo ""
echo -e "${MAGENTA}[PASO 2/3]${NC} Copiar archivos desde _posts/"
echo ""

TOTAL_COPIADOS=0

for seccion in "${!MAPEO[@]}"; do
    seccion_destino="${MAPEO[$seccion]}"
    source_dir="${ORIGINAL_REPO}/_posts/${seccion}"
    dest_dir="${SECTIONS_BASE}/${seccion_destino}/original"
    
    if [ ! -d "$source_dir" ]; then
        echo -e "${YELLOW}⚠️  No existe: ${source_dir}${NC}"
        continue
    fi
    
    # Contar archivos a copiar
    count=$(find "$source_dir" -name "*.md" | wc -l)
    
    echo -e "${CYAN}${seccion_destino}:${NC} ${count} archivos desde _posts/${seccion}/"
    
    if [ $DRY_RUN -eq 0 ]; then
        # Copiar todos los .md
        find "$source_dir" -name "*.md" -exec cp {} "$dest_dir/" \;
        TOTAL_COPIADOS=$((TOTAL_COPIADOS + count))
    fi
done

echo ""
echo -e "${MAGENTA}[PASO 3/3]${NC} Copiar ejemplos desde _examples/"
echo ""

if [ -d "${ORIGINAL_REPO}/_examples" ]; then
    # Copiar ejemplos por número de sección
    for ejemplo in "${ORIGINAL_REPO}/_examples"/*-*.md; do
        if [ -f "$ejemplo" ]; then
            nombre=$(basename "$ejemplo")
            
            # Extraer número de sección (ej: "02-constraint-example-1.md" → "02")
            if [[ $nombre =~ ^([0-9]{2})- ]]; then
                num_seccion="${BASH_REMATCH[1]}"
                
                # Mapear a carpeta destino
                case $num_seccion in
                    01) seccion_dest="01_introduction_goals" ;;
                    02) seccion_dest="02_constraints" ;;
                    03) seccion_dest="03_context_scope" ;;
                    04) seccion_dest="04_solution_strategy" ;;
                    05) seccion_dest="05_building_blocks" ;;
                    06) seccion_dest="06_runtime_view" ;;
                    07) seccion_dest="07_deployment_view" ;;
                    08) seccion_dest="08_concepts" ;;
                    09) seccion_dest="09_architecture_decisions" ;;
                    10) seccion_dest="10_quality" ;;
                    11) seccion_dest="11_risks_tech_debt" ;;
                    12) seccion_dest="12_glossary" ;;
                    *) continue ;;
                esac
                
                dest_dir="${SECTIONS_BASE}/${seccion_dest}/original"
                
                if [ -d "$dest_dir" ]; then
                    echo -e "${CYAN}${nombre}${NC} → ${seccion_dest}/"
                    
                    if [ $DRY_RUN -eq 0 ]; then
                        cp "$ejemplo" "$dest_dir/"
                        TOTAL_COPIADOS=$((TOTAL_COPIADOS + 1))
                    fi
                fi
            fi
        fi
    done
fi

# Resumen
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   RESUMEN DRY-RUN${NC}"
else
    echo -e "${GREEN}   ✅ REDISTRIBUCIÓN COMPLETADA${NC}"
fi
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

if [ $DRY_RUN -eq 0 ]; then
    echo -e "${GREEN}Archivos redistribuidos: ${TOTAL_COPIADOS}${NC}"
    echo ""
    echo "Conteo por sección:"
    for seccion_dest in $(ls -d "${SECTIONS_BASE}"/*/ | sort); do
        nombre=$(basename "$seccion_dest")
        count=$(find "$seccion_dest/original" -name "*.md" ! -name "README.md" | wc -l)
        printf "  %-30s %3d archivos\n" "$nombre" "$count"
    done
else
    echo -e "${YELLOW}Para ejecutar:${NC}"
    echo "  $0"
fi

echo ""
