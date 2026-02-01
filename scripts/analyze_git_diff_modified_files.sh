#!/bin/bash
# ============================================================
# Script: analyze_git_diff_modified_files.sh
# Purpose: Analizar git diff de los 6 archivos modificados
# Date: 2026-02-01
# ============================================================

set -o pipefail

SCRIPT_NAME="$(basename "$0")"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# Output directory
OUTPUT_DIR="${REPO_ROOT}/.mywork/changes/20260131-230456"
OUTPUT_FILE="${OUTPUT_DIR}/GIT_DIFF_ANALISIS_fix_critical_titles.txt"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

# Archivos modificados según git status
MODIFIED_FILES=(
    "source/01_fundamentos/_metodologias/metodo_por_defecto.rst"
    "source/01_fundamentos/index.rst"
    "source/02_procedimientos/workflow_general.rst"
    "source/06_casos_practicos/errores_comunes/error_01_omisiones.rst"
    "source/07_guias_uso/guia_rapida.rst"
    "source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/traduccion/seccion_1_2_quality_goals.rst"
)

echo "======================================================================" > "$OUTPUT_FILE"
echo "ANÁLISIS GIT DIFF - Archivos Modificados por fix_critical_titles.sh" >> "$OUTPUT_FILE"
echo "======================================================================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Fecha: $(date)" >> "$OUTPUT_FILE"
echo "Script: fix_critical_titles.sh v2.0.0" >> "$OUTPUT_FILE"
echo "Archivos analizados: ${#MODIFIED_FILES[@]}" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Procesar cada archivo
for file in "${MODIFIED_FILES[@]}"; do
    echo "======================================================================" >> "$OUTPUT_FILE"
    echo "ARCHIVO: $(basename "$file")" >> "$OUTPUT_FILE"
    echo "Path: $file" >> "$OUTPUT_FILE"
    echo "======================================================================" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # Verificar que el archivo existe
    if [ ! -f "$REPO_ROOT/$file" ]; then
        echo "[ERROR] Archivo no encontrado: $file" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        continue
    fi
    
    # Ejecutar git diff
    cd "$REPO_ROOT"
    git diff "$file" >> "$OUTPUT_FILE" 2>&1
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] git diff falló para: $file" >> "$OUTPUT_FILE"
    fi
    
    echo "" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done

# Resumen final
echo "======================================================================" >> "$OUTPUT_FILE"
echo "RESUMEN DE ANÁLISIS" >> "$OUTPUT_FILE"
echo "======================================================================" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

cd "$REPO_ROOT"

# Contar líneas cambiadas
TOTAL_ADDITIONS=$(git diff --numstat "${MODIFIED_FILES[@]}" 2>/dev/null | awk '{sum+=$1} END {print sum}')
TOTAL_DELETIONS=$(git diff --numstat "${MODIFIED_FILES[@]}" 2>/dev/null | awk '{sum+=$2} END {print sum}')

echo "Líneas agregadas (+): ${TOTAL_ADDITIONS:-0}" >> "$OUTPUT_FILE"
echo "Líneas eliminadas (-): ${TOTAL_DELETIONS:-0}" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Estadísticas por archivo
echo "Estadísticas por archivo:" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
git diff --stat "${MODIFIED_FILES[@]}" >> "$OUTPUT_FILE" 2>&1

echo "" >> "$OUTPUT_FILE"
echo "Análisis completo guardado en: $OUTPUT_FILE" >> "$OUTPUT_FILE"
echo "Fecha de generación: $(date)" >> "$OUTPUT_FILE"

# Mostrar resultado
echo "======================================================================="
echo "ANÁLISIS COMPLETADO"
echo "======================================================================="
echo ""
echo "Archivo generado: $OUTPUT_FILE"
echo "Tamaño: $(wc -l < "$OUTPUT_FILE") líneas"
echo ""
echo "Vista previa:"
head -50 "$OUTPUT_FILE"
echo ""
echo "======================================================================="
echo "Archivo completo disponible en:"
echo "$OUTPUT_FILE"
echo "======================================================================="
