#!/bin/bash
# generate_checksums.sh v2.0.0
# Generar checksums MD5 de todas las partes
# Uso: bash generate_checksums.sh [prefijo] [backup_dir]

set -e

echo "=== GENERANDO CHECKSUMS MD5 ==="
echo ""

if [ -n "$1" ]; then
    PREFIX="$1"
    BACKUP_DIR="$2"
elif [ -f /tmp/bk/last_backup_dir.txt ]; then
    BACKUP_DIR=$(cat /tmp/bk/last_backup_dir.txt)
    PREFIX=$(cat "${BACKUP_DIR}/current_prefix.txt")
else
    echo "ERROR: Proporciona prefijo y directorio"
    exit 1
fi

echo "Prefijo: $PREFIX"
echo "Directorio: $BACKUP_DIR"
echo ""

cd "$BACKUP_DIR"

if ! ls ${PREFIX}-part*.tar 1>/dev/null 2>&1; then
    echo "ERROR: No se encuentran partes del backup"
    exit 1
fi

md5sum ${PREFIX}-part*.tar > ${PREFIX}-checksums.md5

echo "Checksums generados:"
cat ${PREFIX}-checksums.md5
