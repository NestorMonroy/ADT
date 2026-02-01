#!/bin/bash
# Helper script para validación incremental de correcciones manuales
# Uso: ./validate_and_log.sh "mensaje de commit"

set -e

TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
BUILD_LOG=".mywork/build-logs/build-log-${TIMESTAMP}.txt"
ANALYSIS=".mywork/build-logs/analysis-${TIMESTAMP}.txt"

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║         VALIDACIÓN INCREMENTAL - ${TIMESTAMP}          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Limpiar build anterior
echo "1️⃣  Limpiando build anterior..."
make clean > /dev/null 2>&1

# Ejecutar build
echo "2️⃣  Ejecutando build..."
timeout 300 make html > "${BUILD_LOG}" 2>&1 || {
    echo "❌ Build falló o tomó más de 5 minutos"
    echo "   Log guardado en: ${BUILD_LOG}"
    exit 1
}

# Analizar resultado
echo "3️⃣  Analizando resultado..."
python scripts/analysis/analyze_build_log.py "${BUILD_LOG}" > "${ANALYSIS}"

# Mostrar resumen
echo "4️⃣  Resumen:"
echo ""
grep -A 4 "RESUMEN POR SEVERIDAD" "${ANALYSIS}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Archivos guardados:"
echo "  - Build log: ${BUILD_LOG}"
echo "  - Análisis:  ${ANALYSIS}"
echo ""

# Si se proporcionó mensaje de commit
if [ -n "$1" ]; then
    echo "5️⃣  Creando commit..."
    git add -A
    git commit -m "$1 [build: ${TIMESTAMP}]" || echo "⚠️  No hay cambios para commit"
    echo ""
fi

echo "✅ Validación completada"
echo ""
echo "Para ver detalles completos:"
echo "  cat ${ANALYSIS}"
