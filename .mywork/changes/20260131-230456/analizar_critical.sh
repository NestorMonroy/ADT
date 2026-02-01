#!/bin/bash

FILE="/tmp/ADT/source/06_casos_practicos/errores_comunes/error_01_omisiones.rst"

# Líneas con CRITICAL (las 22)
LINES=(155 159 163 167 179 432 436 440 444 448 452 456 460 464 468 472 476 480 484 488 492 504)

echo "=== ANÁLISIS SISTEMÁTICO DE 22 CRITICAL ==="
echo ""

for i in "${!LINES[@]}"; do
    LINE=${LINES[$i]}
    NUM=$((i + 1))
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "CRITICAL $NUM/22 - Línea $LINE"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Obtener título (línea anterior)
    TITLE_LINE=$((LINE - 1))
    TITLE=$(sed -n "${TITLE_LINE}p" "$FILE")
    
    # Obtener underline (línea actual)
    UNDERLINE=$(sed -n "${LINE}p" "$FILE")
    
    # Contar caracteres del título (quitando newline)
    TITLE_LEN=$(echo -n "$TITLE" | wc -c)
    
    # Contar signos = del underline (quitando newline)
    UNDERLINE_LEN=$(echo -n "$UNDERLINE" | wc -c)
    
    # Mostrar
    echo "Línea $TITLE_LINE (TÍTULO):"
    echo "  Contenido: '$TITLE'"
    echo "  Longitud: $TITLE_LEN caracteres"
    echo ""
    echo "Línea $LINE (UNDERLINE):"
    echo "  Contenido: '$UNDERLINE'"
    echo "  Longitud: $UNDERLINE_LEN caracteres"
    echo ""
    
    # Análisis
    DIFF=$((UNDERLINE_LEN - TITLE_LEN))
    
    if [ $DIFF -eq 0 ]; then
        echo "✅ LONGITUDES IGUALES - Posible espacio inicial en ambos"
    elif [ $DIFF -gt 0 ]; then
        echo "❌ UNDERLINE TIENE $DIFF CARÁCTER(ES) DE MÁS"
    else
        DIFF_ABS=$((-DIFF))
        echo "❌ UNDERLINE TIENE $DIFF_ABS CARÁCTER(ES) DE MENOS"
    fi
    
    # Verificar espacios iniciales
    FIRST_CHAR_TITLE=$(echo -n "$TITLE" | cut -c1)
    FIRST_CHAR_UNDER=$(echo -n "$UNDERLINE" | cut -c1)
    
    if [ "$FIRST_CHAR_TITLE" = " " ]; then
        echo "⚠️  TÍTULO tiene espacio inicial"
    fi
    
    if [ "$FIRST_CHAR_UNDER" = " " ]; then
        echo "⚠️  UNDERLINE tiene espacio inicial"
    fi
    
    echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ANÁLISIS COMPLETADO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
