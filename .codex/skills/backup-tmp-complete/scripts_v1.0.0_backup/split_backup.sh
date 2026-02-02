#!/bin/bash
# split_backup.sh
# Dividir backup en partes de 49 MB
# Uso: bash split_backup.sh [prefijo]
# Ejemplo: bash split_backup.sh tmp-20260201-175701

set -e

echo "=== DIVIDIENDO BACKUP EN PARTES DE 49 MB ==="
echo ""

# Leer prefijo del argumento o del archivo
if [ -n "$1" ]; then
    PREFIX="$1"
elif [ -f /tmp/bk/current_prefix.txt ]; then
    PREFIX=$(cat /tmp/bk/current_prefix.txt)
else
    echo "ERROR: Proporciona el prefijo del backup"
    echo "Uso: bash split_backup.sh tmp-YYYYMMDD-HHMMSS"
    exit 1
fi

echo "Prefijo: $PREFIX"
echo ""

# Verificar que existe el archivo completo
if [ ! -f /tmp/bk/${PREFIX}-complete.tar.gz ]; then
    echo "ERROR: No se encuentra /tmp/bk/${PREFIX}-complete.tar.gz"
    exit 1
fi

cd /tmp/bk

echo "Dividiendo ${PREFIX}-complete.tar.gz..."
echo ""

# Dividir en partes de 49MB
split -b 49M -d ${PREFIX}-complete.tar.gz ${PREFIX}-part

echo "Backup dividido en partes"
echo ""

# Renombrar partes a formato .tar
echo "Renombrando partes a formato .tar..."
for file in ${PREFIX}-part*; do
    if [ ! -f "${file}.tar" ]; then
        mv "$file" "${file}.tar"
    fi
done

echo "Partes renombradas"
echo ""

# Listar partes
echo "Partes creadas:"
ls -lh ${PREFIX}-part*.tar | nl
echo ""

# Contar partes
PARTS=$(ls ${PREFIX}-part*.tar | wc -l)
echo "Total de partes: $PARTS"
echo ""

# Guardar informacion
echo "$PARTS" > ${PREFIX}-parts_count.txt
echo "Informacion guardada en ${PREFIX}-parts_count.txt"
