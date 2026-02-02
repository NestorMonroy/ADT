#!/bin/bash
# verify_backup.sh
# Verificar integridad del backup (checksums y partes)
# Uso: bash verify_backup.sh [prefijo]
# Ejemplo: bash verify_backup.sh tmp-20260201-175701

set -e

echo "=== VERIFICANDO BACKUP COMPLETO ==="
echo ""

# Leer prefijo del argumento o del archivo
if [ -n "$1" ]; then
    PREFIX="$1"
elif [ -f /tmp/bk/current_prefix.txt ]; then
    PREFIX=$(cat /tmp/bk/current_prefix.txt)
else
    echo "ERROR: Proporciona el prefijo del backup"
    echo "Uso: bash verify_backup.sh tmp-YYYYMMDD-HHMMSS"
    exit 1
fi

echo "Prefijo: $PREFIX"
echo ""

cd /tmp/bk

# Verificar checksums
echo "Verificando checksums MD5..."
if [ -f "${PREFIX}-checksums.md5" ]; then
    if md5sum -c ${PREFIX}-checksums.md5; then
        echo ""
        echo "Todos los checksums son correctos"
    else
        echo ""
        echo "ERROR: Algunos checksums no coinciden"
        exit 1
    fi
else
    echo "ERROR: Archivo de checksums no encontrado"
    exit 1
fi

echo ""

# Contar partes
echo "Verificando numero de partes..."
ACTUAL=$(ls ${PREFIX}-part*.tar 2>/dev/null | wc -l)
echo "Partes encontradas: $ACTUAL"

if [ -f "${PREFIX}-parts_count.txt" ]; then
    EXPECTED=$(cat ${PREFIX}-parts_count.txt)
    echo "Partes esperadas: $EXPECTED"
    
    if [ "$ACTUAL" -eq "$EXPECTED" ]; then
        echo "OK: Todas las partes estan presentes"
    else
        echo "ERROR: Faltan partes del backup"
        exit 1
    fi
fi

echo ""

# Calcular tamano total
echo "Tamano total del backup:"
du -ch ${PREFIX}-part*.tar | tail -1

echo ""
echo "Verificacion completada exitosamente"
