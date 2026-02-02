#!/bin/bash
# backup_complete_auto.sh
# Script maestro: ejecuta todo el proceso de backup automaticamente
# Uso: bash backup_complete_auto.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "============================================"
echo "  BACKUP COMPLETO AUTOMATICO DE /tmp"
echo "============================================"
echo ""

# FASE 1: Crear backup completo
echo "[FASE 1/5] Creando backup completo..."
bash "$SCRIPT_DIR/create_backup.sh"
echo ""

# Leer el prefijo generado
PREFIX=$(cat /tmp/bk/current_prefix.txt)
echo "Prefijo generado: $PREFIX"
echo ""

# FASE 2: Dividir en partes
echo "[FASE 2/5] Dividiendo en partes de 49MB..."
bash "$SCRIPT_DIR/split_backup.sh" "$PREFIX"
echo ""

# FASE 3: Generar checksums
echo "[FASE 3/5] Generando checksums MD5..."
bash "$SCRIPT_DIR/generate_checksums.sh" "$PREFIX"
echo ""

# FASE 4: Verificar integridad
echo "[FASE 4/5] Verificando integridad..."
bash "$SCRIPT_DIR/verify_backup.sh" "$PREFIX"
echo ""

# FASE 5: Copiar a outputs
echo "[FASE 5/5] Copiando a outputs para descarga..."
bash "$SCRIPT_DIR/copy_to_outputs.sh" "$PREFIX"
echo ""

# Resumen final
echo "============================================"
echo "  BACKUP COMPLETADO EXITOSAMENTE"
echo "============================================"
echo ""
echo "Prefijo: $PREFIX"
echo "Ubicacion: /tmp/bk/"
echo "Disponible en: /mnt/user-data/outputs/"
echo ""

# Obtener estadisticas
PARTS=$(cat /tmp/bk/${PREFIX}-parts_count.txt 2>/dev/null || echo "N/A")
SIZE=$(du -ch /tmp/bk/${PREFIX}-part*.tar 2>/dev/null | tail -1 | cut -f1)

echo "Estadisticas:"
echo "  Partes generadas: $PARTS"
echo "  Tamano total: $SIZE"
echo ""

echo "Archivos listos para descarga:"
ls -1 /mnt/user-data/outputs/${PREFIX}* 2>/dev/null | head -15
TOTAL_FILES=$(ls /mnt/user-data/outputs/${PREFIX}* 2>/dev/null | wc -l)
if [ "$TOTAL_FILES" -gt 15 ]; then
    echo "... y $((TOTAL_FILES - 15)) archivos mas"
fi

echo ""
echo "Para restaurar, usa: bash restore_backup.sh $PREFIX"
