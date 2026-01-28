#!/bin/bash
################################################################################
# Script: clonar_repo_arc42.sh
# Versión: 1.0.0
# Descripción: Clonar repositorio GitHub de arc42 a arc42_documentation/original/
# Uso: ./scripts/clonar_repo_arc42.sh [--dry-run] [--verbose]
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
REPO_URL="https://github.com/arc42/docs.arc42.org-site.git"
RUTA_BASE="/tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation"
RUTA_ORIGINAL="${RUTA_BASE}/original"
TEMP_CLONE="/tmp/arc42_clone_$$"

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
            echo "  Clona el repositorio oficial de arc42 desde GitHub"
            echo ""
            echo "Opciones:"
            echo "  --dry-run, -n    Modo simulación (muestra qué haría sin ejecutar)"
            echo "  --verbose, -v    Modo detallado"
            echo "  --help, -h       Muestra esta ayuda"
            echo ""
            echo "Ejemplos:"
            echo "  $0 --dry-run     # Ver qué haría"
            echo "  $0 --verbose     # Ejecutar con detalles"
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
echo -e "${BLUE}   CLONAR REPOSITORIO ARC42 v1.0.0${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   MODO: DRY-RUN (Simulación - no ejecuta)${NC}"
fi
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# PASO 1: Verificar requisitos
echo -e "${MAGENTA}[PASO 1/7]${NC} Verificar requisitos"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Verificaría que git está instalado"
else
    if ! command -v git &> /dev/null; then
        echo -e "${RED}❌ git no está instalado${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ git instalado${NC}"
fi

if [ ! -d "/tmp/ADT/source" ]; then
    echo -e "${RED}❌ No se encuentra /tmp/ADT/source${NC}"
    echo "¿Estás ejecutando desde la ubicación correcta?"
    exit 1
fi

# PASO 2: Crear estructura destino
echo ""
echo -e "${MAGENTA}[PASO 2/7]${NC} Crear estructura destino"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Crearía: mkdir -p ${RUTA_BASE}"
    echo -e "${CYAN}[DRY-RUN]${NC} Crearía: mkdir -p ${RUTA_ORIGINAL}"
else
    mkdir -p "${RUTA_BASE}"
    mkdir -p "${RUTA_ORIGINAL}"
    echo -e "${GREEN}✅ Estructura creada${NC}"
fi

# PASO 3: Verificar si original/ ya existe
echo ""
echo -e "${MAGENTA}[PASO 3/7]${NC} Verificar si original/ tiene contenido"
echo ""

if [ -d "$RUTA_ORIGINAL" ] && [ "$(ls -A $RUTA_ORIGINAL 2>/dev/null | wc -l)" -gt 0 ]; then
    echo -e "${YELLOW}⚠️  La carpeta original/ ya tiene contenido${NC}"
    
    if [ $DRY_RUN -eq 1 ]; then
        echo -e "${CYAN}[DRY-RUN]${NC} Preguntaría si sobrescribir"
        echo -e "${CYAN}[DRY-RUN]${NC} Opción: Eliminar y clonar de nuevo"
    else
        read -p "¿Eliminar y clonar de nuevo? [S/n]: " respuesta
        if [ "$respuesta" = "n" ] || [ "$respuesta" = "N" ]; then
            echo "Operación cancelada"
            exit 0
        fi
        echo -e "${YELLOW}Eliminando contenido existente...${NC}"
        rm -rf "${RUTA_ORIGINAL:?}"/*
    fi
else
    echo -e "${GREEN}✅ Carpeta original/ lista para usar${NC}"
fi

# PASO 4: Clonar repositorio
echo ""
echo -e "${MAGENTA}[PASO 4/7]${NC} Clonar repositorio desde GitHub"
echo ""
echo -e "${CYAN}Repositorio:${NC} ${REPO_URL}"
echo -e "${CYAN}Destino temporal:${NC} ${TEMP_CLONE}"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Ejecutaría: git clone --depth 1 ${REPO_URL} ${TEMP_CLONE}"
    echo -e "${CYAN}[DRY-RUN]${NC} Esto descargaría el repositorio completo de arc42"
else
    echo "Clonando repositorio..."
    git clone --depth 1 "$REPO_URL" "$TEMP_CLONE"
    echo -e "${GREEN}✅ Repositorio clonado${NC}"
fi

# PASO 5: Copiar contenido
echo ""
echo -e "${MAGENTA}[PASO 5/7]${NC} Copiar contenido a destino final"
echo ""
echo -e "${CYAN}Desde:${NC} ${TEMP_CLONE}"
echo -e "${CYAN}Hacia:${NC} ${RUTA_ORIGINAL}"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Copiaría todos los archivos:"
    echo -e "${CYAN}          cp -r ${TEMP_CLONE}/* ${RUTA_ORIGINAL}/${NC}"
    echo ""
    echo -e "${CYAN}Archivos que se copiarían (simulado):${NC}"
    echo "  - README.md"
    echo "  - src/"
    echo "  - docs/"
    echo "  - images/"
    echo "  - _config.yml"
    echo "  - ... (estructura completa del repo)"
else
    cp -r "${TEMP_CLONE}"/* "${RUTA_ORIGINAL}/"
    echo -e "${GREEN}✅ Contenido copiado${NC}"
fi

# PASO 6: Obtener información del commit
echo ""
echo -e "${MAGENTA}[PASO 6/7]${NC} Obtener información del commit"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    COMMIT_HASH="abc123def456789 (simulado)"
    COMMIT_DATE="2026-01-27 (simulado)"
    COMMIT_AUTHOR="Gernot Starke (simulado)"
    
    echo -e "${CYAN}[DRY-RUN]${NC} Obtendría información del último commit:"
else
    cd "${TEMP_CLONE}"
    COMMIT_HASH=$(git rev-parse HEAD)
    COMMIT_DATE=$(git log -1 --format=%cd --date=short)
    COMMIT_AUTHOR=$(git log -1 --format=%an)
    cd - > /dev/null
fi

echo -e "${GREEN}Información del commit:${NC}"
echo "  Hash:   ${COMMIT_HASH}"
echo "  Fecha:  ${COMMIT_DATE}"
echo "  Autor:  ${COMMIT_AUTHOR}"

# PASO 7: Crear README explicando origen
echo ""
echo -e "${MAGENTA}[PASO 7/7]${NC} Crear README_ORIGEN.md"
echo ""

README_CONTENT="# Repositorio arc42 - Copia Local

Este directorio contiene una copia completa del repositorio oficial de arc42.

## Información de Clonación

**Repositorio GitHub:**  
${REPO_URL}

**Commit Hash:**  
${COMMIT_HASH}

**Fecha del Commit:**  
${COMMIT_DATE}

**Autor del Commit:**  
${COMMIT_AUTHOR}

**Fecha de Clonación:**  
$(date +%Y-%m-%d\ %H:%M:%S)

**Clonado por:**  
$(whoami)@$(hostname)

## Estructura del Repositorio

Este repositorio contiene:
- Documentación completa de arc42
- Ejemplos prácticos
- Tips y guías de uso
- Imágenes y diagramas

## Distribución a Secciones

Los archivos de este repositorio se distribuyen a las secciones específicas
usando el script:

\`\`\`bash
./scripts/distribuir_archivos_arc42.sh
\`\`\`

Cada sección tendrá su carpeta \`original/\` con los archivos correspondientes.

## Actualización

Para actualizar a la última versión del repositorio:

\`\`\`bash
./scripts/clonar_repo_arc42.sh
\`\`\`

Esto clonará la versión más reciente del repositorio.

## Licencia

El contenido de arc42 está bajo licencia:
**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**

Más información: https://arc42.org/license

## Referencias

- Sitio web oficial: https://arc42.org
- Documentación: https://docs.arc42.org
- Repositorio GitHub: ${REPO_URL}
"

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Crearía: ${RUTA_ORIGINAL}/README_ORIGEN.md"
    echo ""
    echo -e "${CYAN}Contenido (primeras líneas):${NC}"
    echo "─────────────────────────────────────────"
    echo "$README_CONTENT" | head -20
    echo "..."
    echo "─────────────────────────────────────────"
else
    echo "$README_CONTENT" > "${RUTA_ORIGINAL}/README_ORIGEN.md"
    echo -e "${GREEN}✅ README_ORIGEN.md creado${NC}"
fi

# Limpiar temporal
echo ""
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Eliminaría directorio temporal: ${TEMP_CLONE}"
else
    if [ -d "$TEMP_CLONE" ]; then
        rm -rf "$TEMP_CLONE"
        echo -e "${GREEN}✅ Directorio temporal limpiado${NC}"
    fi
fi

# Resumen final
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   RESUMEN DRY-RUN (Simulación)${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${YELLOW}Lo que SE HARÍA al ejecutar:${NC}"
    echo ""
    echo "  1. ✅ Crear: ${RUTA_ORIGINAL}"
    echo "  2. ✅ Clonar: ${REPO_URL}"
    echo "  3. ✅ Copiar contenido del repositorio"
    echo "  4. ✅ Registrar commit: ${COMMIT_HASH}"
    echo "  5. ✅ Crear README_ORIGEN.md con información completa"
    echo "  6. ✅ Limpiar archivos temporales"
    echo ""
    echo -e "${GREEN}Para ejecutar realmente:${NC}"
    echo "  $0"
    echo ""
    echo -e "${GREEN}Para ver con más detalle:${NC}"
    echo "  $0 --verbose"
else
    echo -e "${GREEN}   ✅ CLONACIÓN COMPLETADA EXITOSAMENTE${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${GREEN}Repositorio clonado en:${NC}"
    echo "  ${RUTA_ORIGINAL}"
    echo ""
    echo -e "${GREEN}Archivos:${NC}"
    echo "  ✅ README_ORIGEN.md creado"
    echo "  ✅ Repositorio completo copiado"
    echo ""
    echo -e "${GREEN}Información registrada:${NC}"
    echo "  Commit: ${COMMIT_HASH}"
    echo "  Fecha:  ${COMMIT_DATE}"
    echo ""
    echo -e "${YELLOW}Próximo paso:${NC}"
    echo "  ./scripts/distribuir_archivos_arc42.sh --dry-run"
    echo ""
    echo "  Esto distribuirá los archivos a cada sección"
fi
echo ""
