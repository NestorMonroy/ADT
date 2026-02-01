#!/bin/bash
# Script para aplicar correcciones CRITICAL

set -e

echo "========================================================================"
echo "APLICAR CORRECCIONES CRITICAL"
echo "========================================================================"
echo ""

# Directorio base
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
CORR_DIR="${REPO_ROOT}/.mywork/changes/20260131-230456/correcciones_critical"

cd "$REPO_ROOT"

# Verificar que estamos en el directorio correcto
if [ ! -d "source" ]; then
    echo "❌ Error: No se encontró directorio 'source'"
    echo "   Ejecuta este script desde la raíz del repositorio"
    exit 1
fi

echo "Repositorio: $REPO_ROOT"
echo "Correcciones: $CORR_DIR"
echo ""

# Crear backup
echo "📦 Creando backup..."
mkdir -p archivados/pre-critical-fix-$(date +%Y%m%d-%H%M%S)
BACKUP_DIR="archivados/pre-critical-fix-$(date +%Y%m%d-%H%M%S)"

cp source/02_procedimientos/workflow_general.rst "$BACKUP_DIR/"
cp source/02_procedimientos/WORKFLOW_v1_6_0_ACTUALIZACION.rst "$BACKUP_DIR/"
cp source/07_guias_uso/guia_rapida.rst "$BACKUP_DIR/"
cp source/06_casos_practicos/errores_comunes/error_01_omisiones.rst "$BACKUP_DIR/"

echo "✅ Backup creado en: $BACKUP_DIR"
echo ""

# Aplicar correcciones
echo "🔧 Aplicando correcciones..."

cp "$CORR_DIR/workflow_general.rst.CORREGIDO" \
   source/02_procedimientos/workflow_general.rst
echo "  ✅ workflow_general.rst"

cp "$CORR_DIR/WORKFLOW_v1_6_0_ACTUALIZACION.rst.CORREGIDO" \
   source/02_procedimientos/WORKFLOW_v1_6_0_ACTUALIZACION.rst
echo "  ✅ WORKFLOW_v1_6_0_ACTUALIZACION.rst"

cp "$CORR_DIR/guia_rapida.rst.CORREGIDO" \
   source/07_guias_uso/guia_rapida.rst
echo "  ✅ guia_rapida.rst"

cp "$CORR_DIR/error_01_omisiones.rst.CORREGIDO" \
   source/06_casos_practicos/errores_comunes/error_01_omisiones.rst
echo "  ✅ error_01_omisiones.rst"

echo ""
echo "========================================================================"
echo "✅ CORRECCIONES APLICADAS"
echo "========================================================================"
echo ""
echo "Archivos corregidos: 4"
echo "CRITICAL resueltos: 29/31"
echo "Backup: $BACKUP_DIR"
echo ""
echo "Próximos pasos:"
echo "  1. make clean && make html"
echo "  2. Verificar que CRITICAL bajaron de 31 a ~2"
echo "  3. git status"
echo "  4. git diff (revisar cambios)"
echo "  5. git add + git commit si todo está bien"
echo ""
