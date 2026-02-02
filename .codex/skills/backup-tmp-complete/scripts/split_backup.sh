#!/bin/bash
# split_backup.sh v2.0.0
# Dividir backup en partes de 49 MB
# Uso: bash split_backup.sh [prefijo] [backup_dir]

set -e

echo "=== DIVIDIENDO BACKUP EN PARTES DE 49 MB ==="
echo ""

if [ -n "$1" ]; then
    PREFIX="$1"
    BACKUP_DIR="$2"
elif [ -f /tmp/bk/last_backup_dir.txt ]; then
    BACKUP_DIR=$(cat /tmp/bk/last_backup_dir.txt)
    if [ -f "${BACKUP_DIR}/current_prefix.txt" ]; then
        PREFIX=$(cat "${BACKUP_DIR}/current_prefix.txt")
    else
        echo "ERROR: No se encuentra current_prefix.txt"
        exit 1
    fi
else
    echo "ERROR: Proporciona el prefijo y directorio"
    echo "Uso: bash split_backup.sh PREFIX BACKUP_DIR"
    exit 1
fi

echo "Prefijo: $PREFIX"
echo "Directorio: $BACKUP_DIR"
echo ""

if [ ! -f "${BACKUP_DIR}/${PREFIX}-complete.tar.gz" ]; then
    echo "ERROR: No se encuentra ${BACKUP_DIR}/${PREFIX}-complete.tar.gz"
    exit 1
fi

cd "$BACKUP_DIR"

echo "Dividiendo archivo..."
split -b 49M -d ${PREFIX}-complete.tar.gz ${PREFIX}-part

echo "Renombrando partes..."
for file in ${PREFIX}-part*; do
    if [ ! -f "${file}.tar" ]; then
        mv "$file" "${file}.tar"
    fi
done

echo ""
echo "Partes creadas:"
ls -lh ${PREFIX}-part*.tar | nl

PARTS=$(ls ${PREFIX}-part*.tar | wc -l)
echo ""
echo "Total de partes: $PARTS"

echo "$PARTS" > ${PREFIX}-parts_count.txt
