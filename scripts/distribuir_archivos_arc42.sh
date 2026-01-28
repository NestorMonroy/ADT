#!/bin/bash
################################################################################
# Script: distribuir_archivos_arc42.sh
# Versión: 1.0.0
# Descripción: Distribuir archivos del repo clonado a las 12 secciones de arc42
# Uso: ./scripts/distribuir_archivos_arc42.sh [--dry-run] [--verbose]
#
# SECCIONES OFICIALES DE ARC42:
# 1 - Introduction and Goals
# 2 - Constraints
# 3 - Context and scope
# 4 - Solution strategy
# 5 - Building block view
# 6 - Runtime view
# 7 - Deployment view
# 8 - Concepts
# 9 - Architecture decisions
# 10 - Quality
# 11 - Risks and technical debt
# 12 - Glossary
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
VERBOSE=0
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
        --verbose|-v)
            VERBOSE=1
            shift
            ;;
        --help|-h)
            echo "Uso: $0 [opciones]"
            echo ""
            echo "Descripción:"
            echo "  Distribuye archivos del repositorio clonado (original/) a las"
            echo "  12 secciones oficiales de arc42"
            echo ""
            echo "Opciones:"
            echo "  --dry-run, -n    Modo simulación (muestra qué haría sin ejecutar)"
            echo "  --verbose, -v    Modo detallado"
            echo "  --help, -h       Muestra esta ayuda"
            echo ""
            echo "Secciones arc42:"
            echo "  01 - Introduction and Goals"
            echo "  02 - Constraints"
            echo "  03 - Context and scope"
            echo "  04 - Solution strategy"
            echo "  05 - Building block view"
            echo "  06 - Runtime view"
            echo "  07 - Deployment view"
            echo "  08 - Concepts"
            echo "  09 - Architecture decisions"
            echo "  10 - Quality"
            echo "  11 - Risks and technical debt"
            echo "  12 - Glossary"
            echo ""
            echo "Ejemplos:"
            echo "  $0 --dry-run     # Ver qué archivos se distribuirían"
            echo "  $0               # Ejecutar normalmente"
            exit 0
            ;;
        *)
            echo -e "${RED}Opción desconocida: $1${NC}"
            exit 1
            ;;
    esac
done

# Banner
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}   DISTRIBUIR ARCHIVOS ARC42 A SECCIONES v1.0.0${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   MODO: DRY-RUN (Simulación - no ejecuta)${NC}"
fi
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# PASO 1: Verificar que existe original/
echo -e "${MAGENTA}[PASO 1/4]${NC} Verificar repositorio clonado"
echo ""

if [ ! -d "$ORIGINAL_REPO" ]; then
    echo -e "${RED}❌ Error: No existe ${ORIGINAL_REPO}${NC}"
    echo ""
    echo "Ejecutar primero: ./scripts/clonar_repo_arc42.sh"
    exit 1
fi

echo -e "${GREEN}✅ Repositorio encontrado en: ${ORIGINAL_REPO}${NC}"

# PASO 2: Definir mapeo de secciones (NOMBRES CORRECTOS)
echo ""
echo -e "${MAGENTA}[PASO 2/4]${NC} Definir mapeo de secciones"
echo ""

# Lista de secciones con nombres CORRECTOS según arc42 oficial
declare -a SECCIONES=(
    "01_introduction_goals"
    "02_constraints"
    "03_context_scope"
    "04_solution_strategy"
    "05_building_blocks"
    "06_runtime_view"
    "07_deployment_view"
    "08_concepts"              # ⭐ CORREGIDO: NO "crosscutting_concepts"
    "09_architecture_decisions"
    "10_quality"               # ⭐ CORREGIDO: NO "quality_requirements"
    "11_risks_tech_debt"
    "12_glossary"
)

# Mapeo de patrones de búsqueda → sección
# Formato: "patron|seccion_destino"
declare -a MAPEOS=(
    "01|01_introduction_goals"
    "introduction|01_introduction_goals"
    "goals|01_introduction_goals"
    "02|02_constraints"
    "constraint|02_constraints"
    "03|03_context_scope"
    "context|03_context_scope"
    "scope|03_context_scope"
    "04|04_solution_strategy"
    "solution|04_solution_strategy"
    "strategy|04_solution_strategy"
    "05|05_building_blocks"
    "building|05_building_blocks"
    "block|05_building_blocks"
    "06|06_runtime_view"
    "runtime|06_runtime_view"
    "07|07_deployment_view"
    "deployment|07_deployment_view"
    "08|08_concepts"
    "concept|08_concepts"
    "crosscutting|08_concepts"
    "09|09_architecture_decisions"
    "decision|09_architecture_decisions"
    "adr|09_architecture_decisions"
    "10|10_quality"
    "quality|10_quality"
    "11|11_risks_tech_debt"
    "risk|11_risks_tech_debt"
    "debt|11_risks_tech_debt"
    "12|12_glossary"
    "glossary|12_glossary"
)

echo -e "${CYAN}Secciones oficiales de arc42:${NC}"
for i in "${!SECCIONES[@]}"; do
    printf "  %2d. %s\n" $((i+1)) "${SECCIONES[$i]}"
done

# Función para determinar sección de un archivo
determinar_seccion() {
    local archivo="$1"
    local nombre_archivo=$(basename "$archivo")
    local nombre_lower=$(echo "$nombre_archivo" | tr '[:upper:]' '[:lower:]')
    
    # 1. Buscar por número al inicio (más específico)
    if [[ $nombre_lower =~ ^0*([0-9]+)[_-] ]]; then
        local num="${BASH_REMATCH[1]}"
        case $num in
            1)  echo "01_introduction_goals"; return ;;
            2)  echo "02_constraints"; return ;;
            3)  echo "03_context_scope"; return ;;
            4)  echo "04_solution_strategy"; return ;;
            5)  echo "05_building_blocks"; return ;;
            6)  echo "06_runtime_view"; return ;;
            7)  echo "07_deployment_view"; return ;;
            8)  echo "08_concepts"; return ;;
            9)  echo "09_architecture_decisions"; return ;;
            10) echo "10_quality"; return ;;
            11) echo "11_risks_tech_debt"; return ;;
            12) echo "12_glossary"; return ;;
        esac
    fi
    
    # 2. Buscar por patrón en el nombre
    for mapeo in "${MAPEOS[@]}"; do
        IFS='|' read -r patron seccion <<< "$mapeo"
        if [[ $nombre_lower == *"$patron"* ]]; then
            echo "$seccion"
            return
        fi
    done
    
    # 3. No se pudo determinar
    echo "desconocido"
}

# PASO 3: Analizar y mapear archivos
echo ""
echo -e "${MAGENTA}[PASO 3/4]${NC} Analizar archivos y mapear a secciones"
echo ""

declare -A ARCHIVOS_POR_SECCION
TOTAL_ARCHIVOS=0
TOTAL_DESCONOCIDOS=0

echo -e "${CYAN}Buscando archivos .md y .adoc en: ${ORIGINAL_REPO}${NC}"
echo ""

# Buscar archivos relevantes
while IFS= read -r archivo; do
    if [ -f "$archivo" ]; then
        seccion=$(determinar_seccion "$archivo")
        nombre=$(basename "$archivo")
        
        if [ "$seccion" != "desconocido" ]; then
            ARCHIVOS_POR_SECCION[$seccion]="${ARCHIVOS_POR_SECCION[$seccion]} $archivo"
            TOTAL_ARCHIVOS=$((TOTAL_ARCHIVOS + 1))
            
            if [ $VERBOSE -eq 1 ]; then
                echo -e "${GREEN}  ✅ ${nombre}${NC} → ${seccion}"
            fi
        else
            TOTAL_DESCONOCIDOS=$((TOTAL_DESCONOCIDOS + 1))
            if [ $VERBOSE -eq 1 ]; then
                echo -e "${YELLOW}  ⚠️  ${nombre}${NC} → no mapeado"
            fi
        fi
    fi
done < <(find "$ORIGINAL_REPO" -type f \( -name "*.md" -o -name "*.adoc" \) 2>/dev/null)

echo -e "${GREEN}Archivos mapeados por sección:${NC}"
echo ""

for seccion in "${SECCIONES[@]}"; do
    archivos="${ARCHIVOS_POR_SECCION[$seccion]}"
    count=$(echo "$archivos" | wc -w)
    
    if [ $count -gt 0 ]; then
        echo -e "  ${GREEN}✅ ${seccion}:${NC} ${count} archivos"
    else
        echo -e "  ${YELLOW}⚠️  ${seccion}:${NC} 0 archivos"
    fi
done

echo ""
echo -e "${CYAN}Resumen:${NC}"
echo "  Total mapeados:     ${TOTAL_ARCHIVOS}"
echo "  Total no mapeados:  ${TOTAL_DESCONOCIDOS}"

# PASO 4: Distribuir archivos
echo ""
echo -e "${MAGENTA}[PASO 4/4]${NC} Distribuir archivos a secciones"
echo ""

if [ $DRY_RUN -eq 0 ]; then
    read -p "¿Continuar con la distribución? [S/n]: " CONFIRMAR
    if [ "$CONFIRMAR" = "n" ] || [ "$CONFIRMAR" = "N" ]; then
        echo "Operación cancelada"
        exit 0
    fi
fi

ARCHIVOS_COPIADOS=0

for seccion in "${SECCIONES[@]}"; do
    archivos="${ARCHIVOS_POR_SECCION[$seccion]}"
    
    if [ ! -z "$archivos" ] && [ "$archivos" != " " ]; then
        DEST_DIR="${SECTIONS_BASE}/${seccion}/original"
        
        # Crear directorio
        if [ $DRY_RUN -eq 1 ]; then
            echo -e "${CYAN}[DRY-RUN]${NC} Crearía: ${seccion}/original/"
        else
            mkdir -p "$DEST_DIR"
        fi
        
        # Copiar archivos
        for archivo in $archivos; do
            nombre_archivo=$(basename "$archivo")
            
            if [ $DRY_RUN -eq 1 ]; then
                echo -e "${CYAN}[DRY-RUN]${NC} Copiaría: ${nombre_archivo} → ${seccion}/original/"
            else
                cp "$archivo" "$DEST_DIR/"
                if [ $VERBOSE -eq 1 ]; then
                    echo -e "${GREEN}  ✅ Copiado: ${nombre_archivo}${NC}"
                fi
                ARCHIVOS_COPIADOS=$((ARCHIVOS_COPIADOS + 1))
            fi
        done
        
        # Crear README en cada sección
        README_FILE="${DEST_DIR}/README.md"
        count=$(echo "$archivos" | wc -w)
        
        README_CONTENT="# Original: ${seccion}

**Sección:** $(echo $seccion | sed 's/_/ /g' | sed 's/\b\(.\)/\u\1/g')  
**Origen:** Repositorio arc42 (GitHub)  
**URL:** https://github.com/arc42/docs.arc42.org-site/  
**Archivos:** ${count} archivos  
**Fecha distribución:** $(date +%Y-%m-%d)

## Archivos en esta sección

"
        for archivo in $archivos; do
            nombre=$(basename "$archivo")
            README_CONTENT="${README_CONTENT}- \`${nombre}\`
"
        done
        
        README_CONTENT="${README_CONTENT}
## Fuente original

Estos archivos fueron copiados desde:
\`arc42_documentation/original/\`

Para actualizar:
\`\`\`bash
./scripts/clonar_repo_arc42.sh
./scripts/distribuir_archivos_arc42.sh
\`\`\`

## Licencia

Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"
        
        if [ $DRY_RUN -eq 1 ]; then
            echo -e "${CYAN}[DRY-RUN]${NC} Crearía README: ${seccion}/original/README.md"
        else
            echo "$README_CONTENT" > "$README_FILE"
            if [ $VERBOSE -eq 1 ]; then
                echo -e "${GREEN}  ✅ README creado${NC}"
            fi
        fi
    fi
done

# Resumen final
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   RESUMEN DRY-RUN (Simulación)${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${YELLOW}Lo que SE HARÍA al ejecutar:${NC}"
    echo ""
    echo "  📁 Archivos a distribuir: ${TOTAL_ARCHIVOS}"
    echo "  📂 Secciones a poblar: 12"
    echo "  📄 READMEs a crear: 12"
    echo ""
    echo -e "${YELLOW}Distribución por sección:${NC}"
    for seccion in "${SECCIONES[@]}"; do
        count=$(echo "${ARCHIVOS_POR_SECCION[$seccion]}" | wc -w)
        if [ $count -gt 0 ]; then
            printf "    %2d archivos → %s\n" "$count" "$seccion"
        fi
    done
    echo ""
    echo -e "${GREEN}Para ejecutar realmente:${NC}"
    echo "  $0"
    echo ""
    echo -e "${GREEN}Para ver detalles de cada archivo:${NC}"
    echo "  $0 --verbose"
else
    echo -e "${GREEN}   ✅ DISTRIBUCIÓN COMPLETADA EXITOSAMENTE${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${GREEN}Archivos distribuidos: ${ARCHIVOS_COPIADOS}${NC}"
    echo -e "${GREEN}Secciones pobladas: 12${NC}"
    echo -e "${GREEN}READMEs creados: 12${NC}"
    echo ""
    echo -e "${YELLOW}Ubicación:${NC}"
    echo "  ${SECTIONS_BASE}/"
    echo ""
    echo -e "${YELLOW}Próximos pasos:${NC}"
    echo "  1. Revisar archivos: ls ${SECTIONS_BASE}/01_*/original/"
    echo "  2. Comenzar traducción siguiendo: 02_procedimientos/workflow_general.rst"
    echo "  3. Validar estructura: ./scripts/validar_estructura.sh biblioteca/..."
fi
echo ""
