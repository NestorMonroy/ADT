#!/bin/bash
# restore_backup.sh
# Restaurar backup desde partes descargadas
# Uso: bash restore_backup.sh [prefijo] [directorio_destino]
# Ejemplo: bash restore_backup.sh tmp-20260201-175701 /path/to/restore

set -e

echo "=== RESTAURANDO BACKUP DESDE PARTES ==="
echo ""

# Verificar argumentos
if [ -z "$1" ]; then
    echo "ERROR: Proporciona el prefijo del backup"
    echo "Uso: bash restore_backup.sh tmp-YYYYMMDD-HHMMSS [directorio_destino]"
    exit 1
fi

PREFIX="$1"
RESTORE_DIR="${2:-./tmp-restored}"

echo "Prefijo: $PREFIX"
echo "Directorio destino: $RESTORE_DIR"
echo ""

# Verificar que existen las partes
if ! ls ${PREFIX}-part*.tar 1>/dev/null 2>&1; then
    echo "ERROR: No se encuentran partes del backup ${PREFIX}"
    echo "Asegurate de estar en el directorio con las partes descargadas"
    exit 1
fi

# PASO 1: Verificar checksums
echo "PASO 1: Verificando checksums..."
if [ -f "${PREFIX}-checksums.md5" ]; then
    if md5sum -c ${PREFIX}-checksums.md5; then
        echo ""
        echo "Checksums verificados correctamente"
    else
        echo ""
        echo "ERROR: Algunos checksums no coinciden"
        echo "Re-descarga las partes corruptas antes de continuar"
        exit 1
    fi
else
    echo "ADVERTENCIA: Archivo de checksums no encontrado"
    echo "Continuando sin verificacion..."
fi

echo ""

# PASO 2: Reconstruir archivo completo
echo "PASO 2: Reconstruyendo archivo completo..."
cat ${PREFIX}-part*.tar > ${PREFIX}-complete.tar.gz

if [ -f "${PREFIX}-complete.tar.gz" ]; then
    echo "Archivo completo reconstruido"
    ls -lh ${PREFIX}-complete.tar.gz
else
    echo "ERROR: No se pudo reconstruir el archivo"
    exit 1
fi

echo ""

# PASO 3: Crear directorio destino
echo "PASO 3: Creando directorio destino..."
mkdir -p "$RESTORE_DIR"
echo "Directorio creado: $RESTORE_DIR"

echo ""

# PASO 4: Extraer contenido
echo "PASO 4: Extrayendo contenido..."
echo "(Esto puede tomar varios minutos)"
tar -xzf ${PREFIX}-complete.tar.gz -C "$RESTORE_DIR"

echo ""
echo "Extraccion completada"

echo ""

# PASO 5: Verificar contenido
echo "PASO 5: Verificando contenido..."
if [ -d "$RESTORE_DIR/tmp" ]; then
    FILES=$(find "$RESTORE_DIR/tmp" -type f 2>/dev/null | wc -l)
    SIZE=$(du -sh "$RESTORE_DIR/tmp" 2>/dev/null | cut -f1)
    
    echo "Archivos restaurados: $FILES"
    echo "Tamano total: $SIZE"
    echo ""
    echo "Contenido restaurado en: $RESTORE_DIR/tmp/"
else
    echo "ADVERTENCIA: No se encuentra el directorio /tmp en la restauracion"
fi

echo ""
echo "Restauracion completada exitosamente"
