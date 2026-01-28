#!/bin/bash
###############################################################################
# ADT - Sistema de Traducción Técnica
# Script: translate_web_content.sh
# Versión: 1.0.0
# Descripción: Traduce contenido web técnico a español mexicano
###############################################################################

set -euo pipefail

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuración
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/tmp/ADT"
CACHE_DIR="${PROJECT_ROOT}/.cache"
LOG_FILE="${PROJECT_ROOT}/logs/traduccion_$(date +%Y%m%d_%H%M%S).log"

# Crear directorios si no existen
mkdir -p "${CACHE_DIR}"
mkdir -p "${PROJECT_ROOT}/logs"

###############################################################################
# FUNCIONES DE UTILIDAD
###############################################################################

log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $*" | tee -a "${LOG_FILE}"
}

error() {
    echo -e "${RED}[ERROR]${NC} $*" | tee -a "${LOG_FILE}" >&2
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $*" | tee -a "${LOG_FILE}"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $*" | tee -a "${LOG_FILE}"
}

###############################################################################
# FUNCIONES DE DETECCIÓN DE HERRAMIENTAS
###############################################################################

check_dependencies() {
    local missing_deps=()
    
    # Herramientas básicas
    command -v curl >/dev/null 2>&1 || missing_deps+=("curl")
    command -v jq >/dev/null 2>&1 || missing_deps+=("jq")
    
    # Herramientas opcionales (dan warnings)
    if ! command -v node >/dev/null 2>&1; then
        warning "Node.js no encontrado - algunas funciones limitadas"
    fi
    
    if ! command -v python3 >/dev/null 2>&1; then
        warning "Python3 no encontrado - algunas funciones limitadas"
    fi
    
    if [ ${#missing_deps[@]} -gt 0 ]; then
        error "Dependencias faltantes: ${missing_deps[*]}"
        error "Instala con: sudo apt-get install ${missing_deps[*]}"
        return 1
    fi
    
    log "✓ Todas las dependencias esenciales están instaladas"
    return 0
}

###############################################################################
# FUNCIONES DE OBTENCIÓN DE CONTENIDO WEB
###############################################################################

fetch_html() {
    local url="$1"
    local output_file="$2"
    local cache_key
    cache_key=$(echo -n "$url" | md5sum | cut -d' ' -f1)
    local cache_file="${CACHE_DIR}/${cache_key}.html"
    
    # Verificar cache
    if [ -f "$cache_file" ]; then
        info "Usando versión en cache de: $url"
        cp "$cache_file" "$output_file"
        return 0
    fi
    
    log "Descargando: $url"
    
    if curl -s -L -A "Mozilla/5.0" "$url" > "$output_file"; then
        # Guardar en cache
        cp "$output_file" "$cache_file"
        log "✓ Descarga exitosa"
        return 0
    else
        error "Error al descargar: $url"
        return 1
    fi
}

extract_text_from_html() {
    local input_file="$1"
    local output_file="$2"
    
    # Método 1: usando grep y sed (básico)
    grep -oP '(?<=>)[^<]+(?=<)' "$input_file" | \
        sed '/^[[:space:]]*$/d' | \
        sed 's/^[[:space:]]*//;s/[[:space:]]*$//' > "$output_file"
    
    log "✓ Texto extraído de HTML"
}

###############################################################################
# FUNCIONES DE TRADUCCIÓN
###############################################################################

translate_text_basic() {
    local input_file="$1"
    local output_file="$2"
    local source_lang="${3:-en}"
    local target_lang="${4:-es}"
    
    info "Modo: Traducción básica (preservación de términos técnicos)"
    
    # Aquí se implementaría la lógica de traducción
    # Por ahora, copiamos el archivo como ejemplo
    cp "$input_file" "$output_file"
    
    warning "Traducción automática no implementada - se requiere revisión manual"
    info "Aplica los procedimientos de ADT:"
    info "  1. Alta fidelidad"
    info "  2. Marcado visual"
    info "  3. Preservación de términos técnicos"
}

###############################################################################
# FUNCIONES DE FORMATO SPHINX
###############################################################################

convert_to_rst() {
    local input_file="$1"
    local output_file="$2"
    local title="$3"
    
    {
        echo "$(echo "$title" | sed 's/.//g' | tr '[:print:]' '=')"
        echo "$title"
        echo "$(echo "$title" | sed 's/.//g' | tr '[:print:]' '=')"
        echo ""
        echo ".. meta::"
        echo "   :traducido: $(date +%Y-%m-%d)"
        echo "   :idioma: es-MX"
        echo ""
        echo "Contenido"
        echo "========="
        echo ""
        cat "$input_file"
    } > "$output_file"
    
    log "✓ Convertido a formato reStructuredText"
}

###############################################################################
# FUNCIÓN PRINCIPAL DE TRADUCCIÓN
###############################################################################

translate_url() {
    local url="$1"
    local output_dir="$2"
    local title="$3"
    
    log "======================================"
    log "Iniciando traducción de URL"
    log "======================================"
    log "URL: $url"
    log "Destino: $output_dir"
    log "Título: $title"
    
    # Crear directorio de salida
    mkdir -p "$output_dir"
    
    # Archivos temporales
    local html_file="${output_dir}/original.html"
    local text_file="${output_dir}/extracted_text.txt"
    local translated_file="${output_dir}/translated.txt"
    local rst_file="${output_dir}/$(echo "$title" | tr ' ' '_' | tr '[:upper:]' '[:lower:]').rst"
    
    # Paso 1: Descargar HTML
    if ! fetch_html "$url" "$html_file"; then
        error "Fallo en descarga"
        return 1
    fi
    
    # Paso 2: Extraer texto
    extract_text_from_html "$html_file" "$text_file"
    
    # Paso 3: Traducir (manual o semiautomático)
    translate_text_basic "$text_file" "$translated_file"
    
    # Paso 4: Convertir a RST
    convert_to_rst "$translated_file" "$rst_file" "$title"
    
    log "======================================"
    log "✓ Traducción completada"
    log "======================================"
    log "Archivos generados:"
    log "  - Original HTML: $html_file"
    log "  - Texto extraído: $text_file"
    log "  - Texto traducido: $translated_file"
    log "  - Documento RST: $rst_file"
    log ""
    log "Siguiente paso: Revisar y refinar $rst_file"
}

###############################################################################
# FUNCIÓN PRINCIPAL
###############################################################################

main() {
    log "======================================"
    log "ADT - Sistema de Traducción Técnica"
    log "Versión 1.0.0"
    log "======================================"
    
    # Verificar dependencias
    if ! check_dependencies; then
        exit 1
    fi
    
    # Verificar argumentos
    if [ $# -lt 3 ]; then
        error "Uso: $0 <URL> <DIRECTORIO_SALIDA> <TITULO>"
        error ""
        error "Ejemplo:"
        error "  $0 'https://arc42.org/overview' './traduccion/source/arc42' 'Visión General de arc42'"
        exit 1
    fi
    
    local url="$1"
    local output_dir="$2"
    local title="$3"
    
    # Ejecutar traducción
    translate_url "$url" "$output_dir" "$title"
    
    log ""
    log "✓ Proceso completado exitosamente"
    log "Ver log completo en: $LOG_FILE"
}

# Ejecutar función principal
main "$@"
