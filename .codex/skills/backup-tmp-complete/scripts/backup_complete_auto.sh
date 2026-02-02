#!/bin/bash
# backup_complete_auto.sh v2.0.0
# Script maestro: proceso completo de backup
# Uso: bash backup_complete_auto.sh [directorio_origen]
# Ejemplo: bash backup_complete_auto.sh /tmp
# Ejemplo: bash backup_complete_auto.sh /tmp/ADT/.codex

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SOURCE_DIR="${1:-/tmp}"

echo "============================================"
echo "  BACKUP COMPLETO AUTOMATICO"
echo "============================================"
echo ""
echo "Directorio origen: $SOURCE_DIR"
echo ""

echo "[FASE 1/5] Creando backup completo..."
bash "$SCRIPT_DIR/create_backup.sh" "$SOURCE_DIR"
echo ""

BACKUP_DIR=$(cat /tmp/bk/last_backup_dir.txt)
PREFIX=$(cat "${BACKUP_DIR}/current_prefix.txt")

echo "Prefijo generado: $PREFIX"
echo "Directorio backup: $BACKUP_DIR"
echo ""

echo "[FASE 2/5] Dividiendo en partes..."
bash "$SCRIPT_DIR/split_backup.sh"
echo ""

echo "[FASE 3/5] Generando checksums..."
bash "$SCRIPT_DIR/generate_checksums.sh"
echo ""

echo "[FASE 4/5] Verificando integridad..."
bash "$SCRIPT_DIR/verify_backup.sh"
echo ""

echo "[FASE 5/5] Copiando a outputs..."
bash "$SCRIPT_DIR/copy_to_outputs.sh"
echo ""

echo "============================================"
echo "  BACKUP COMPLETADO"
echo "============================================"
echo ""
echo "Prefijo: $PREFIX"
echo "Origen: $SOURCE_DIR"
echo "Backup en: $BACKUP_DIR"
echo "Disponible en: /mnt/user-data/outputs/"
echo ""

PARTS=$(cat "${BACKUP_DIR}/${PREFIX}-parts_count.txt" 2>/dev/null || echo "N/A")
SIZE=$(du -ch "${BACKUP_DIR}/${PREFIX}-part*.tar" 2>/dev/null | tail -1 | cut -f1)

echo "Estadisticas:"
echo "  Partes: $PARTS"
echo "  Tamano: $SIZE"
echo ""

echo "Para restaurar:"
echo "  bash restore_backup.sh $PREFIX [destino]"
