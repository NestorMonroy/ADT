#!/bin/bash
# create_backup.sh
# Crear backup completo de /tmp excluyendo /tmp/bk
# Uso: bash create_backup.sh

set -e

echo "=== CREANDO BACKUP COMPLETO DE /tmp ==="
echo ""

# Crear directorio de destino si no existe
mkdir -p /tmp/bk

# Generar timestamp y prefijo
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
PREFIX="tmp-${TIMESTAMP}"

echo "Prefijo: $PREFIX"
echo "Timestamp: $TIMESTAMP"
echo ""

# Eliminar backup parcial anterior si existe
if [ -f /tmp/bk/${PREFIX}-base.tar.gz ]; then
    rm -f /tmp/bk/${PREFIX}-base.tar.gz
    echo "Backup parcial anterior eliminado"
fi

echo "Creando backup COMPLETO de /tmp excluyendo solo /tmp/bk..."
echo "(Esto incluira TODOS los archivos y subdirectorios)"
echo ""

# Crear tar completo con compresion gzip
tar --exclude='/tmp/bk' \
    --ignore-failed-read \
    --warning=no-file-changed \
    -czf /tmp/bk/${PREFIX}-complete.tar.gz \
    /tmp 2>&1 | \
    grep -v "Removing leading" | \
    grep -v "file changed as we read it" | \
    head -20

echo ""

# Verificar que se creo el backup
if [ -f /tmp/bk/${PREFIX}-complete.tar.gz ]; then
    echo "Backup completo creado exitosamente"
    ls -lh /tmp/bk/${PREFIX}-complete.tar.gz
    echo ""
    echo "Tamano del backup:"
    du -sh /tmp/bk/${PREFIX}-complete.tar.gz
    echo ""
    echo "Prefijo guardado en: /tmp/bk/current_prefix.txt"
    echo "$PREFIX" > /tmp/bk/current_prefix.txt
else
    echo "ERROR: No se pudo crear el backup completo"
    exit 1
fi
