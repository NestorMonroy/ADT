#!/bin/bash
# restore_backup.sh v2.0.0
# Restaurar backup desde partes
# Uso: bash restore_backup.sh [prefijo] [directorio_destino]

set -e

echo "=== RESTAURANDO BACKUP ==="
echo ""

if [ -z "$1" ]; then
    echo "ERROR: Proporciona el prefijo del backup"
    echo "Uso: bash restore_backup.sh PREFIX [destino]"
    exit 1
fi

PREFIX="$1"
RESTORE_DIR="${2:-./restored}"

echo "Prefijo: $PREFIX"
echo "Directorio destino: $RESTORE_DIR"
echo ""

if ! ls ${PREFIX}-part*.tar 1>/dev/null 2>&1; then
    echo "ERROR: No se encuentran partes del backup"
    exit 1
fi

echo "PASO 1: Verificando checksums..."
if [ -f "${PREFIX}-checksums.md5" ]; then
    if md5sum -c ${PREFIX}-checksums.md5; then
        echo "Checksums correctos"
    else
        echo "ERROR: Checksums no coinciden"
        exit 1
    fi
else
    echo "ADVERTENCIA: Sin archivo de checksums"
fi

echo ""
echo "PASO 2: Reconstruyendo archivo..."
cat ${PREFIX}-part*.tar > ${PREFIX}-complete.tar.gz

if [ -f "${PREFIX}-complete.tar.gz" ]; then
    echo "Archivo reconstruido"
    ls -lh ${PREFIX}-complete.tar.gz
else
    echo "ERROR: No se pudo reconstruir"
    exit 1
fi

echo ""
echo "PASO 3: Creando directorio..."
mkdir -p "$RESTORE_DIR"
echo "Directorio: $RESTORE_DIR"

echo ""
echo "PASO 4: Extrayendo..."
tar -xzf ${PREFIX}-complete.tar.gz -C "$RESTORE_DIR"

echo ""
echo "PASO 5: Verificando..."
FILES=$(find "$RESTORE_DIR" -type f 2>/dev/null | wc -l)
SIZE=$(du -sh "$RESTORE_DIR" 2>/dev/null | cut -f1)

echo "Archivos restaurados: $FILES"
echo "Tamano total: $SIZE"
echo ""
echo "Restauracion completada"
echo "Ubicacion: $RESTORE_DIR"
