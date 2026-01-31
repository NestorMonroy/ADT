#!/bin/bash

# Configuración
PROYECTO="ADT"
RUTA_PROYECTO="/e/Proyectos/Translate/ADT"
RUTA_DESTINO="."  # Directorio donde se guardarán los backups
TIMESTAMP=$(date +%y%m%d%H%M)
NOMBRE_BASE="backup_${PROYECTO}_${TIMESTAMP}_part"

# Carpetas a excluir
EXCLUSIONES=(
    ".git"
    ".idea"
    ".venv"
    "_build"
)

# Validar que existe el proyecto
if [ ! -d "$RUTA_PROYECTO" ]; then
    echo "ERROR: No existe el directorio $RUTA_PROYECTO"
    exit 1
fi

# Limpiar backups parciales anteriores con el mismo timestamp (idempotencia)
if ls ${RUTA_DESTINO}/${NOMBRE_BASE}* 1> /dev/null 2>&1; then
    echo "Limpiando archivos parciales existentes..."
    rm -f ${RUTA_DESTINO}/${NOMBRE_BASE}*
fi

# Construir argumentos de exclusión
EXCLUDE_ARGS=""
for excl in "${EXCLUSIONES[@]}"; do
    EXCLUDE_ARGS="$EXCLUDE_ARGS --exclude='$excl'"
done

# Crear backup
echo "Creando backup de $RUTA_PROYECTO..."
echo "Excluyendo: ${EXCLUSIONES[*]}"

eval tar -czf - $EXCLUDE_ARGS "$RUTA_PROYECTO" | split -b 50M - "${RUTA_DESTINO}/${NOMBRE_BASE}"

# Renombrar partes
echo "Renombrando partes..."
for file in ${RUTA_DESTINO}/${NOMBRE_BASE}*; do
    if [ -f "$file" ]; then
        mv "$file" "${file}.tar.gz"
    fi
done

# Verificar resultado
echo ""
echo "Backup completado:"
ls -lh ${RUTA_DESTINO}/${NOMBRE_BASE}*.tar.gz

# Mostrar información
TOTAL_SIZE=$(du -sh ${RUTA_DESTINO}/${NOMBRE_BASE}*.tar.gz | awk '{sum+=$1} END {print sum}')
NUM_PARTES=$(ls ${RUTA_DESTINO}/${NOMBRE_BASE}*.tar.gz | wc -l)

echo ""
echo "Partes generadas: $NUM_PARTES"
echo "Timestamp: $TIMESTAMP"