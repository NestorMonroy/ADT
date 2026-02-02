#!/bin/bash
# generate_checksums.sh
# Generar checksums MD5 de todas las partes
# Uso: bash generate_checksums.sh [prefijo]
# Ejemplo: bash generate_checksums.sh tmp-20260201-175701

set -e

echo "=== GENERANDO CHECKSUMS MD5 ==="
echo ""

# Leer prefijo del argumento o del archivo
if [ -n "$1" ]; then
    PREFIX="$1"
elif [ -f /tmp/bk/current_prefix.txt ]; then
    PREFIX=$(cat /tmp/bk/current_prefix.txt)
else
    echo "ERROR: Proporciona el prefijo del backup"
    echo "Uso: bash generate_checksums.sh tmp-YYYYMMDD-HHMMSS"
    exit 1
fi

echo "Prefijo: $PREFIX"
echo ""

cd /tmp/bk

# Verificar que existen partes
if ! ls ${PREFIX}-part*.tar 1>/dev/null 2>&1; then
    echo "ERROR: No se encuentran partes del backup ${PREFIX}"
    exit 1
fi

# Generar checksums
echo "Generando checksums..."
md5sum ${PREFIX}-part*.tar > ${PREFIX}-checksums.md5

echo "Checksums generados exitosamente"
echo ""

# Mostrar checksums
echo "Archivo: ${PREFIX}-checksums.md5"
cat ${PREFIX}-checksums.md5
