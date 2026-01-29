#!/bin/bash
################################################################################
# Script: setup_java.sh
# Versión: 1.0.1
# Descripción: Descarga e instala Java portable (OpenJDK 17) dentro del proyecto
# Destino: tools/java/jdk-17
# Uso: ./scripts/setup_java.sh [--dry-run] [--force] [--verbose]
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
JAVA_MAJOR="17"
JAVA_URL="https://aka.ms/download-jdk/microsoft-jdk-17-windows-x64.zip"

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JAVA_BASE="${REPO_ROOT}/tools/java"
JAVA_HOME="${JAVA_BASE}/jdk-17"
JAVA_BIN="${JAVA_HOME}/bin/java.exe"

DOWNLOAD_DIR="${REPO_ROOT}/tools/_downloads"
ZIP_PATH="${DOWNLOAD_DIR}/microsoft-jdk-17-windows-x64.zip"

TMP_DIR="/tmp/java_portable_$$"

DRY_RUN=0
FORCE=0
VERBOSE=0

log() {
    echo -e "[ $(date '+%Y-%m-%d %H:%M:%S') ] $1"
}

run() {
    if [ $DRY_RUN -eq 1 ]; then
        echo -e "${CYAN}[DRY-RUN]${NC} $*"
        return 0
    fi
    [ $VERBOSE -eq 1 ] && echo -e "${CYAN}[EXEC]${NC} $*"
    eval "$@"
}

java_works() {
    [ -x "$JAVA_BIN" ] || return 1
    "$JAVA_BIN" -version >/tmp/java_test.out 2>&1 || return 1
    grep -qi "openjdk\|version" /tmp/java_test.out
}

# Procesar argumentos
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run|-n) DRY_RUN=1; shift ;;
        --force|-f)   FORCE=1; shift ;;
        --verbose|-v) VERBOSE=1; shift ;;
        --help|-h)
            echo "Uso: $0 [opciones]"
            echo ""
            echo "Opciones:"
            echo "  --dry-run, -n    Simula la ejecución sin hacer cambios"
            echo "  --force, -f      Reinstala Java aunque ya exista"
            echo "  --verbose, -v    Muestra comandos ejecutados"
            echo "  --help, -h       Muestra esta ayuda"
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
echo -e "${BLUE}   SETUP JAVA PORTABLE (OpenJDK ${JAVA_MAJOR}) v1.0.1${NC}"
if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}   MODO: DRY-RUN (Simulación)${NC}"
fi
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

log "Repositorio raíz: ${REPO_ROOT}"
log "Destino Java: ${JAVA_HOME}"

# PASO 1: Verificar instalación existente
echo ""
echo -e "${MAGENTA}[PASO 1/6]${NC} Verificar instalación existente"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Verificaría si existe y funciona: ${JAVA_BIN}"
else
    if [ $FORCE -eq 0 ] && java_works; then
        log "Java ya está instalado y funcional."
        "$JAVA_BIN" -version 2>&1
        log "No se requiere acción."
        exit 0
    fi
fi

if [ $FORCE -eq 1 ]; then
    log "Modo force activo: se reinstalará Java."
fi

# PASO 2: Preparar directorios
echo ""
echo -e "${MAGENTA}[PASO 2/6]${NC} Preparar directorios"
echo ""

run "mkdir -p \"$DOWNLOAD_DIR\""
run "mkdir -p \"$JAVA_BASE\""

# PASO 3: Descargar ZIP
echo ""
echo -e "${MAGENTA}[PASO 3/6]${NC} Descargar OpenJDK ${JAVA_MAJOR}"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Si no existe ZIP, descargaría a: $ZIP_PATH"
    run "curl -L \"$JAVA_URL\" -o \"$ZIP_PATH\""
else
    if [ ! -f "$ZIP_PATH" ]; then
        run "curl -L \"$JAVA_URL\" -o \"$ZIP_PATH\""
    else
        log "ZIP ya existe, se reutiliza: $ZIP_PATH"
    fi
fi

# PASO 4: Extraer ZIP
echo ""
echo -e "${MAGENTA}[PASO 4/6]${NC} Extraer Java"
echo ""

run "rm -rf \"$TMP_DIR\""
run "mkdir -p \"$TMP_DIR\""
run "unzip -q \"$ZIP_PATH\" -d \"$TMP_DIR\""

# En dry-run NO intentamos inspeccionar un directorio que no existe
if [ $DRY_RUN -eq 1 ]; then
    JDK_DIR="${TMP_DIR}/<carpeta_jdk_extraida>"
    log "Directorio JDK detectado (simulado): $JDK_DIR"
else
    JDK_DIR="$(find "$TMP_DIR" -type f -path '*/bin/java.exe' -print -quit | xargs -r dirname | xargs -r dirname)"
    if [ -z "$JDK_DIR" ]; then
        echo -e "${RED}No se pudo localizar bin/java.exe dentro del ZIP${NC}"
        exit 1
    fi
    log "Directorio JDK detectado: $JDK_DIR"
fi

# PASO 5: Instalar en ruta estable
echo ""
echo -e "${MAGENTA}[PASO 5/6]${NC} Instalar Java portable"
echo ""

if [ $FORCE -eq 1 ]; then
    run "rm -rf \"$JAVA_HOME\""
fi

run "rm -rf \"$JAVA_HOME\""
run "cp -R \"$JDK_DIR\" \"$JAVA_HOME\""

# PASO 6: Validación final
echo ""
echo -e "${MAGENTA}[PASO 6/6]${NC} Validar Java instalado"
echo ""

if [ $DRY_RUN -eq 1 ]; then
    echo -e "${CYAN}[DRY-RUN]${NC} Validaría ejecución: ${JAVA_BIN} -version"
else
    if ! java_works; then
        echo -e "${RED}Java no se ejecuta correctamente desde ${JAVA_BIN}${NC}"
        exit 1
    fi
    log "Java portable instalado correctamente."
    "$JAVA_BIN" -version 2>&1
fi

# Limpieza
run "rm -rf \"$TMP_DIR\""

echo ""
echo -e "${GREEN}Proceso completado.${NC}"
echo ""
