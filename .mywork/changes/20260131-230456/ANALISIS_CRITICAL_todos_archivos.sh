#!/bin/bash
# Análisis de TODOS los archivos con CRITICAL

REPO="/tmp/ADT"
OUTPUT="ANALISIS_CRITICAL_todos_archivos.md"

cat > "$OUTPUT" << 'EOFMD'
# Análisis de CRITICAL - Todos los Archivos

**Fecha**: 2026-02-01 02:40
**Archivos analizados**: 5
**Total CRITICAL**: 31

---

EOFMD

# Archivo 1: error_01_omisiones.rst (22 CRITICAL)
echo "## ARCHIVO 1: error_01_omisiones.rst" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**CRITICAL reportados**: 22" >> "$OUTPUT"
echo "**Líneas**: 155, 159, 163, 167, 179, 432, 436, 440, 444, 448, 452, 456, 460, 464, 468, 472, 476, 480, 484, 488, 492, 504" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# Analizar primeras 3 líneas de ejemplo
for LINE in 155 432 504; do
    echo "### Línea $LINE" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    echo '```' >> "$OUTPUT"
    # Contexto: 10 líneas antes hasta 5 después
    START=$((LINE - 10))
    END=$((LINE + 5))
    sed -n "${START},${END}p" "$REPO/source/06_casos_practicos/errores_comunes/error_01_omisiones.rst" >> "$OUTPUT"
    echo '```' >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

# Archivo 2: workflow_general.rst (5 CRITICAL)
echo "## ARCHIVO 2: workflow_general.rst" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**CRITICAL reportados**: 5" >> "$OUTPUT"
echo "**Líneas**: 1363, 3080, 3083, 3407, 3409" >> "$OUTPUT"
echo "" >> "$OUTPUT"

for LINE in 1363 3080 3407; do
    echo "### Línea $LINE" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    echo '```' >> "$OUTPUT"
    START=$((LINE - 10))
    END=$((LINE + 5))
    sed -n "${START},${END}p" "$REPO/source/02_procedimientos/workflow_general.rst" >> "$OUTPUT"
    echo '```' >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

# Archivo 3: WORKFLOW_v1_6_0_ACTUALIZACION.rst (1 CRITICAL)
echo "## ARCHIVO 3: WORKFLOW_v1_6_0_ACTUALIZACION.rst" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**CRITICAL reportados**: 1" >> "$OUTPUT"
echo "**Línea**: 634" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "### Línea 634" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
sed -n "624,644p" "$REPO/source/02_procedimientos/WORKFLOW_v1_6_0_ACTUALIZACION.rst" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
echo "" >> "$OUTPUT"

# Archivo 4: guia_rapida.rst (1 CRITICAL)
echo "## ARCHIVO 4: guia_rapida.rst" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**CRITICAL reportados**: 1" >> "$OUTPUT"
echo "" >> "$OUTPUT"

# Buscar línea exacta
LINE=$(grep -n "CRITICAL:" "$REPO/.mywork/changes/20260131-230456/critical.txt" | grep "guia_rapida.rst" | cut -d: -f1 | head -1)
echo "### Contexto" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
# Buscar alrededor de línea 307 (estimado)
sed -n "297,317p" "$REPO/source/07_guias_uso/guia_rapida.rst" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
echo "" >> "$OUTPUT"

# Archivo 5: GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst (2 CRITICAL)
echo "## ARCHIVO 5: GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**CRITICAL reportados**: 2" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "### Contexto" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
# Buscar alrededor de donde podrían estar
sed -n "1,50p" "$REPO/source/docs_maestros/GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst" >> "$OUTPUT"
echo '```' >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "**Análisis completado**: $(date)" >> "$OUTPUT"

