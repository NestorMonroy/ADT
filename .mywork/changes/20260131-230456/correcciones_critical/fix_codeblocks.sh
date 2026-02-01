#!/bin/bash
# Script para indentar code-blocks en error_01_omisiones.rst

FILE=".mywork/changes/20260131-230456/correcciones_critical/error_01_omisiones.rst.CORREGIDO"

# BLOQUE 1: Líneas 152-179
# Indentar +2 espacios (de 1 a 3) desde línea 152 hasta antes de la siguiente línea en blanco

# BLOQUE 2: Líneas 429-504  
# Similar

# Usar awk para procesar
awk '
NR >= 152 && NR <= 179 && /^ [^ ]/ {
    # Líneas que empiezan con exactamente 1 espacio
    sub(/^ /, "   ")
    print
    next
}
NR >= 152 && NR <= 179 && /^ =/ {
    # Líneas con espacio + signos =
    sub(/^ /, "   ")
    print
    next
}
NR >= 429 && NR <= 504 && /^ [^ ]/ {
    sub(/^ /, "   ")
    print
    next
}
NR >= 429 && NR <= 504 && /^ =/ {
    sub(/^ /, "   ")
    print
    next
}
{print}
' "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"

echo "✅ Code-blocks indentados"
