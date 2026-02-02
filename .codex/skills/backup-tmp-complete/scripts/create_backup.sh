#!/bin/bash
# create_backup.sh v2.0.0
# Crear backup completo de cualquier directorio
# Uso: bash create_backup.sh [directorio_origen]

set -e

echo "=== CREANDO BACKUP COMPLETO ==="
echo ""

SOURCE_DIR="${1:-/tmp}"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "ERROR: El directorio '$SOURCE_DIR' no existe"
    exit 1
fi

SOURCE_DIR="${SOURCE_DIR%/}"
echo "Directorio origen: $SOURCE_DIR"
echo ""

BASENAME=$(basename "$SOURCE_DIR")
SUBDIR_NAME="bk-${BASENAME}"
BACKUP_BASE="/tmp/bk"
BACKUP_DIR="${BACKUP_BASE}/${SUBDIR_NAME}"

echo "Subdirectorio de backup: $SUBDIR_NAME"
echo ""

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Directorio creado: $BACKUP_DIR"
else
    echo "Directorio existente: $BACKUP_DIR"
fi

echo ""

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
PREFIX="${SUBDIR_NAME}-${TIMESTAMP}"

echo "Prefijo: $PREFIX"
echo ""

EXCLUDE_OPTS=""
if [ "$SOURCE_DIR" = "/tmp" ]; then
    EXCLUDE_OPTS="--exclude='/tmp/bk'"
    echo "Exclusion: /tmp/bk"
fi

echo "Creando backup de $SOURCE_DIR..."
echo ""

if [ -n "$EXCLUDE_OPTS" ]; then
    eval tar $EXCLUDE_OPTS \
        --ignore-failed-read \
        --warning=no-file-changed \
        -czf "${BACKUP_DIR}/${PREFIX}-complete.tar.gz" \
        "$SOURCE_DIR" 2>&1 | \
        grep -v "Removing leading" | \
        grep -v "file changed" | \
        head -20
else
    tar --ignore-failed-read \
        --warning=no-file-changed \
        -czf "${BACKUP_DIR}/${PREFIX}-complete.tar.gz" \
        "$SOURCE_DIR" 2>&1 | \
        grep -v "Removing leading" | \
        grep -v "file changed" | \
        head -20
fi

echo ""

if [ -f "${BACKUP_DIR}/${PREFIX}-complete.tar.gz" ]; then
    echo "Backup completo creado"
    ls -lh "${BACKUP_DIR}/${PREFIX}-complete.tar.gz"
    echo ""
    du -sh "${BACKUP_DIR}/${PREFIX}-complete.tar.gz"
    echo ""
    
    echo "$PREFIX" > "${BACKUP_DIR}/current_prefix.txt"
    echo "$SOURCE_DIR" > "${BACKUP_DIR}/source_dir.txt"
    echo "$BACKUP_DIR" > /tmp/bk/last_backup_dir.txt
    
    echo "Informacion guardada en $BACKUP_DIR"
else
    echo "ERROR: No se pudo crear el backup"
    exit 1
fi
