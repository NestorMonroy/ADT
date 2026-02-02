#!/bin/bash
# verify_backup.sh v2.0.0
# Verificar integridad del backup
# Uso: bash verify_backup.sh [prefijo] [backup_dir]

set -e

echo "=== VERIFICANDO BACKUP ==="
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

echo "Verificando checksums MD5..."
if [ -f "${PREFIX}-checksums.md5" ]; then
    if md5sum -c ${PREFIX}-checksums.md5; then
        echo ""
        echo "Checksums correctos"
    else
        echo "ERROR: Checksums no coinciden"
        exit 1
    fi
else
    echo "ERROR: Archivo de checksums no encontrado"
    exit 1
fi

echo ""
echo "Verificando numero de partes..."
ACTUAL=$(ls ${PREFIX}-part*.tar 2>/dev/null | wc -l)
echo "Partes encontradas: $ACTUAL"

if [ -f "${PREFIX}-parts_count.txt" ]; then
    EXPECTED=$(cat ${PREFIX}-parts_count.txt)
    echo "Partes esperadas: $EXPECTED"
    
    if [ "$ACTUAL" -eq "$EXPECTED" ]; then
        echo "OK: Todas las partes presentes"
    else
        echo "ERROR: Faltan partes"
        exit 1
    fi
fi

echo ""
du -ch ${PREFIX}-part*.tar | tail -1
echo ""
echo "Verificacion completada"
