#!/bin/bash
# copy_to_outputs.sh v2.0.0
# Copiar backup a outputs para descarga
# Uso: bash copy_to_outputs.sh [prefijo] [backup_dir]

set -e

echo "=== COPIANDO BACKUP A OUTPUTS ==="
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

cd "$BACKUP_DIR"

PARTS=$(ls ${PREFIX}-part*.tar 2>/dev/null | wc -l)
echo "Copiando $PARTS partes..."
echo ""

COPIED=0
for file in ${PREFIX}-part*.tar; do
    if [ -f "$file" ]; then
        cp "$file" /mnt/user-data/outputs/
        COPIED=$((COPIED + 1))
        echo "  Copiado: $file"
    fi
done

echo ""
echo "Partes copiadas: $COPIED"
echo ""

if [ -f "${PREFIX}-checksums.md5" ]; then
    cp ${PREFIX}-checksums.md5 /mnt/user-data/outputs/
    echo "  Copiado: checksums.md5"
fi

if [ -f "${PREFIX}-README.md" ]; then
    cp ${PREFIX}-README.md /mnt/user-data/outputs/
    echo "  Copiado: README.md"
fi

echo ""
TOTAL=$(ls /mnt/user-data/outputs/${PREFIX}* 2>/dev/null | wc -l)
SIZE=$(du -ch /mnt/user-data/outputs/${PREFIX}* 2>/dev/null | tail -1 | cut -f1)
echo "Archivos en outputs: $TOTAL"
echo "Tamano total: $SIZE"
