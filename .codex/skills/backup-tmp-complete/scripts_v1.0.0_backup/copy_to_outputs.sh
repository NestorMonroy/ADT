#!/bin/bash
# copy_to_outputs.sh
# Copiar backup completo a /mnt/user-data/outputs para descarga
# Uso: bash copy_to_outputs.sh [prefijo]
# Ejemplo: bash copy_to_outputs.sh tmp-20260201-175701

set -e

echo "=== COPIANDO BACKUP A OUTPUTS ==="
echo ""

# Leer prefijo del argumento o del archivo
if [ -n "$1" ]; then
    PREFIX="$1"
elif [ -f /tmp/bk/current_prefix.txt ]; then
    PREFIX=$(cat /tmp/bk/current_prefix.txt)
else
    echo "ERROR: Proporciona el prefijo del backup"
    echo "Uso: bash copy_to_outputs.sh tmp-YYYYMMDD-HHMMSS"
    exit 1
fi

echo "Prefijo: $PREFIX"
echo ""

cd /tmp/bk

# Contar partes
PARTS=$(ls ${PREFIX}-part*.tar 2>/dev/null | wc -l)
echo "Copiando $PARTS partes..."
echo ""

# Copiar todas las partes
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

# Copiar archivos auxiliares
echo "Copiando archivos auxiliares..."

if [ -f "${PREFIX}-checksums.md5" ]; then
    cp ${PREFIX}-checksums.md5 /mnt/user-data/outputs/
    echo "  Copiado: checksums.md5"
fi

if [ -f "${PREFIX}-README.md" ]; then
    cp ${PREFIX}-README.md /mnt/user-data/outputs/
    echo "  Copiado: README.md"
fi

echo ""
echo "Todos los archivos copiados a outputs"
echo ""

# Verificar en outputs
echo "Verificando en outputs..."
TOTAL=$(ls /mnt/user-data/outputs/${PREFIX}* 2>/dev/null | wc -l)
echo "Archivos totales: $TOTAL"

SIZE=$(du -ch /mnt/user-data/outputs/${PREFIX}* 2>/dev/null | tail -1 | cut -f1)
echo "Tamano total: $SIZE"
