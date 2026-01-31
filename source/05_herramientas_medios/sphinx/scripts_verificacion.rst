.. _scripts_verificacion:




Scripts de Verificación Automatizada
====================================

Scripts bash para verificar la calidad de tus traducciones automáticamente.

.. contents:: Contenido
 :depth: 2
 :local:




Script Principal: verificar_traduccion.sh
=========================================

Descripción
===========

Script completo que verifica:
- Completitud del contenido
- Enriquecimiento apropiado
- Compilación exitosa
- Referencias cruzadas
- Calidad general

Código Completo
===============

.. code-block:: bash

 #!/bin/bash
 # verificar_traduccion.sh
 # Script de verificación completa de traducción ADT

 VERSION="1.0.0"

 # Colores para output
 GREEN='\033[0;32m'
 YELLOW='\033[1;33m'
 RED='\033[0;31m'
 NC='\033[0m' # No Color

 echo "+============================================+"
 echo "| Verificador ADT v$VERSION |"
 echo "+============================================+"
 echo ""

 # Verificar argumentos
 if [ $# -lt 2 ]; then
 echo "Uso: $0 <archivo_original> <archivo_traducido>"
 echo ""
 echo "Ejemplo:"
 echo " $0 original/section-12.md traduccion/seccion_12.rst"
 exit 1
 fi

 ORIGINAL="$1"
 TRADUCIDO="$2"

 # Verificar que archivos existen
 if [ ! -f "$ORIGINAL" ]; then
 echo -e "${RED}[ERROR] Error: Archivo original no existe: $ORIGINAL${NC}"
 exit 1
 fi

 if [ ! -f "$TRADUCIDO" ]; then
 echo -e "${RED}[ERROR] Error: Archivo traducido no existe: $TRADUCIDO${NC}"
 exit 1
 fi

 SCORE_TOTAL=0
 CHECKS_TOTAL=0

 # ============================================
 # CHECK 1: Conteo de Líneas y Enriquecimiento
 # ============================================

 echo "==========================================="
 echo "CHECK 1: Enriquecimiento"
 echo "==========================================="

 ORIG_LINES=$(wc -l < "$ORIGINAL")
 TRAD_LINES=$(wc -l < "$TRADUCIDO")

 echo "[TABLE] Líneas:"
 echo " Original: $ORIG_LINES"
 echo " Traducido: $TRAD_LINES"

 if [ $ORIG_LINES -gt 0 ]; then
 ENRIQUECIMIENTO=$(( (TRAD_LINES - ORIG_LINES) * 100 / ORIG_LINES ))
 echo " Enriquecimiento: +$ENRIQUECIMIENTO%"

 # Determinar rango esperado según MD-002
 if [ $ORIG_LINES -lt 20 ]; then
 MIN_ENRIQ=300
 MAX_ENRIQ=1000
 TIPO="A (<20 líneas)"
 elif [ $ORIG_LINES -lt 50 ]; then
 MIN_ENRIQ=100
 MAX_ENRIQ=300
 TIPO="B (20-50 líneas)"
 elif [ $ORIG_LINES -lt 100 ]; then
 MIN_ENRIQ=80
 MAX_ENRIQ=150
 TIPO="C (50-100 líneas)"
 else
 MIN_ENRIQ=50
 MAX_ENRIQ=100
 TIPO="D (>100 líneas)"
 fi

 echo ""
 echo "[LIST] Tipo de documento: $TIPO"
 echo " Rango esperado: +$MIN_ENRIQ% a +$MAX_ENRIQ%"

 if [ $ENRIQUECIMIENTO -ge $MIN_ENRIQ ] && [ $ENRIQUECIMIENTO -le $MAX_ENRIQ ]; then
 echo -e " ${GREEN}[OK] Enriquecimiento apropiado${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 20))
 elif [ $ENRIQUECIMIENTO -lt $MIN_ENRIQ ]; then
 echo -e " ${YELLOW}[WARNING] Enriquecimiento bajo (agregar más contenido)${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 10))
 else
 echo -e " ${YELLOW}[WARNING] Enriquecimiento alto (verificar si es apropiado)${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 15))
 fi
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 20))

 echo ""

 # ============================================
 # CHECK 2: Elementos Estructurales
 # ============================================

 echo "==========================================="
 echo "CHECK 2: Elementos Estructurales"
 echo "==========================================="

 # Contar secciones
 ORIG_SECTIONS=$(grep -c "^#" "$ORIGINAL" 2>/dev/null || echo "0")
 TRAD_SECTIONS=$(grep -c "^=" "$TRADUCIDO" 2>/dev/null || echo "0")

 echo " Secciones/Títulos:"
 echo " Original: $ORIG_SECTIONS"
 echo " Traducido: $TRAD_SECTIONS"

 if [ $ORIG_SECTIONS -eq $TRAD_SECTIONS ] || [ $TRAD_SECTIONS -ge $ORIG_SECTIONS ]; then
 echo -e " ${GREEN}[OK] Secciones OK${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 15))
 else
 echo -e " ${RED}[ERROR] Faltan secciones${NC}"
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 15))

 # Contar listas
 ORIG_LISTS=$(grep -c "^[-*]" "$ORIGINAL" 2>/dev/null || echo "0")
 TRAD_LISTS=$(grep -c "^[-*]" "$TRADUCIDO" 2>/dev/null || echo "0")

 echo ""
 echo "[NOTE] Items de lista:"
 echo " Original: $ORIG_LISTS"
 echo " Traducido: $TRAD_LISTS"

 if [ $TRAD_LISTS -ge $ORIG_LISTS ]; then
 echo -e " ${GREEN}[OK] Listas OK${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 10))
 else
 echo -e " ${YELLOW}[WARNING] Menos items en traducción${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 5))
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 10))

 echo ""

 # ============================================
 # CHECK 3: Bloques de Código
 # ============================================

 echo "==========================================="
 echo "CHECK 3: Bloques de Código"
 echo "==========================================="

 ORIG_CODE=$(grep -c "^\`\`\`" "$ORIGINAL" 2>/dev/null || echo "0")
 TRAD_CODE=$(grep -c "code-block::" "$TRADUCIDO" 2>/dev/null || echo "0")

 echo "[COMPUTER] Bloques de código:"
 echo " Original: $ORIG_CODE"
 echo " Traducido: $TRAD_CODE"

 if [ $TRAD_CODE -ge $ORIG_CODE ]; then
 echo -e " ${GREEN}[OK] Código preservado${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 10))
 else
 echo -e " ${RED}[ERROR] Faltan bloques de código${NC}"
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 10))

 echo ""

 # ============================================
 # CHECK 4: Compilación
 # ============================================

 echo "==========================================="
 echo "CHECK 4: Compilación Sphinx"
 echo "==========================================="

 # Buscar directorio del proyecto Sphinx
 SPHINX_DIR=$(dirname "$TRADUCIDO")
 while [ "$SPHINX_DIR" != "/" ]; do
 if [ -f "$SPHINX_DIR/conf.py" ]; then
 break
 fi
 SPHINX_DIR=$(dirname "$SPHINX_DIR")
 done

 if [ -f "$SPHINX_DIR/conf.py" ]; then
 echo "[BUILD] Compilando..."
 cd "$SPHINX_DIR/.." || exit

 COMPILE_OUTPUT=$(make html 2>&1)
 COMPILE_EXIT=$?

 ERRORS=$(echo "$COMPILE_OUTPUT" | grep -c "ERROR" || echo "0")
 WARNINGS=$(echo "$COMPILE_OUTPUT" | grep -c "WARNING" || echo "0")

 echo " Errores: $ERRORS"
 echo " Warnings: $WARNINGS"

 if [ $COMPILE_EXIT -eq 0 ] && [ $ERRORS -eq 0 ]; then
 echo -e " ${GREEN}[OK] Compilación exitosa${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 25))
 elif [ $ERRORS -eq 0 ]; then
 echo -e " ${YELLOW}[WARNING] Compilación con warnings${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 20))
 else
 echo -e " ${RED}[ERROR] Errores de compilación${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 5))
 fi
 else
 echo -e " ${YELLOW}[WARNING] No se encontró conf.py (saltando check)${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 25))
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 25))

 echo ""

 # ============================================
 # CHECK 5: Referencias y Links
 # ============================================

 echo "==========================================="
 echo "CHECK 5: Referencias"
 echo "==========================================="

 TRAD_REFS=$(grep -c ":ref:\|:doc:\|.. _" "$TRADUCIDO" 2>/dev/null || echo "0")

 echo "[LINK] Referencias encontradas: $TRAD_REFS"

 if [ $TRAD_REFS -gt 0 ]; then
 echo -e " ${GREEN}[OK] Referencias presentes${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 10))
 else
 echo -e " ${YELLOW}[WARNING] Sin referencias (verificar si son necesarias)${NC}"
 SCORE_TOTAL=$((SCORE_TOTAL + 5))
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 10))

 echo ""

 # ============================================
 # CHECK 6: Terminología Consistente
 # ============================================

 echo "==========================================="
 echo "CHECK 6: Terminología"
 echo "==========================================="

 # Términos que deben conservarse
 TERMINOS_CONSERVAR=("API" "REST" "JSON" "Stakeholder" "Product Owner")
 PROBLEMAS=0

 for TERMINO in "${TERMINOS_CONSERVAR[@]}"; do
 COUNT=$(grep -i -o "$TERMINO" "$TRADUCIDO" | wc -l)
 if [ $COUNT -gt 0 ]; then
 # Verificar que esté en inglés, no traducido
 COUNT_TRAD=$(grep -i -o "$(echo $TERMINO | tr 'A-Z' 'a-z')" "$TRADUCIDO" | wc -l)
 if [ $COUNT -eq $COUNT_TRAD ]; then
 echo -e " ${GREEN}[OK] '$TERMINO' conservado correctamente${NC}"
 fi
 fi
 done

 if [ $PROBLEMAS -eq 0 ]; then
 SCORE_TOTAL=$((SCORE_TOTAL + 10))
 else
 SCORE_TOTAL=$((SCORE_TOTAL + 5))
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 10))

 echo ""

 # ============================================
 # RESULTADO FINAL
 # ============================================

 echo "+============================================+"
 echo "| RESULTADO FINAL |"
 echo "+============================================+"
 echo ""

 PORCENTAJE=$((SCORE_TOTAL * 100 / CHECKS_TOTAL))

 echo "[TABLE] Puntuación: $SCORE_TOTAL / $CHECKS_TOTAL"
 echo "[CHART] Porcentaje: $PORCENTAJE%"
 echo ""

 if [ $PORCENTAJE -ge 95 ]; then
 echo -e "${GREEN}[OK] EXCELENTE - Calidad aprobada${NC}"
 echo " Traducción lista para entrega"
 EXIT_CODE=0
 elif [ $PORCENTAJE -ge 85 ]; then
 echo -e "${YELLOW}[WARNING] BUENO - Revisar y mejorar${NC}"
 echo " Algunos ajustes menores recomendados"
 EXIT_CODE=1
 elif [ $PORCENTAJE -ge 70 ]; then
 echo -e "${YELLOW}[WARNING] ACEPTABLE - Necesita mejoras${NC}"
 echo " Revisar puntos marcados en amarillo/rojo"
 EXIT_CODE=2
 else
 echo -e "${RED}[ERROR] INSUFICIENTE - Re-trabajar${NC}"
 echo " Calidad por debajo del estándar ADT"
 EXIT_CODE=3
 fi

 echo ""
 echo "==========================================="

 exit $EXIT_CODE

Uso
===

**Básico:**

.. code-block:: bash

 chmod +x verificar_traduccion.sh

 ./verificar_traduccion.sh \
 original/section-12.md \
 traduccion/seccion_12_glosario.rst

**Salida esperada:**

.. code-block:: text

   +============================================+
   | Verificador ADT v1.0.0 |
   +============================================+

   CHECK 1: Enriquecimiento
   =========================
   [TABLE] Líneas:
   Original: 44
   Traducido: 164
   Enriquecimiento: +273%

   [LIST] Tipo de documento: B (20-50 líneas)
   Rango esperado: +100% a +300%
 [OK] Enriquecimiento apropiado




 +============================================+
 | RESULTADO FINAL |
 +============================================+

 [TABLE] Puntuación: 95 / 100
 [CHART] Porcentaje: 95%

 [OK] EXCELENTE - Calidad aprobada
 Traducción lista para entrega




Script Auxiliar: verificar_lote.sh
==================================

Para verificar múltiples archivos

Código
======

.. code-block:: bash

 #!/bin/bash
 # verificar_lote.sh
 # Verificar un lote completo de traducciones

 ORIGINAL_DIR="$1"
 TRADUCCION_DIR="$2"

 if [ $# -lt 2 ]; then
 echo "Uso: $0 <dir_original> <dir_traduccion>"
 exit 1
 fi

 echo "Verificando lote completo..."
 echo ""

 TOTAL=0
 APROBADOS=0
 RECHAZADOS=0

 for ORIG in "$ORIGINAL_DIR"/*.md; do
 NOMBRE=$(basename "$ORIG" .md)
 TRAD="$TRADUCCION_DIR/${NOMBRE}.rst"

 if [ -f "$TRAD" ]; then
 echo "Verificando: $NOMBRE"
 ./verificar_traduccion.sh "$ORIG" "$TRAD" > /dev/null
 EXIT_CODE=$?

 if [ $EXIT_CODE -eq 0 ]; then
 echo "[OK] $NOMBRE - Aprobado"
 APROBADOS=$((APROBADOS + 1))
 else
 echo "[ERROR] $NOMBRE - Necesita revisión"
 RECHAZADOS=$((RECHAZADOS + 1))
 fi

 TOTAL=$((TOTAL + 1))
 fi
 done

 echo ""
 echo "==========================================="
 echo "RESUMEN DEL LOTE"
 echo "==========================================="
 echo "Total archivos: $TOTAL"
 echo "Aprobados: $APROBADOS"
 echo "Por revisar: $RECHAZADOS"
 echo "Tasa de éxito: $(( APROBADOS * 100 / TOTAL ))%"




Script Auxiliar: prevenir_omisiones.sh
======================================

Verificación específica de PASO 0

Código
======

.. code-block:: bash

 #!/bin/bash
 # prevenir_omisiones.sh
 # Ayuda a verificar que leíste TODO el archivo

 ARCHIVO="$1"

 if [ ! -f "$ARCHIVO" ]; then
 echo "Uso: $0 <archivo_original>"
 exit 1
 fi

 TOTAL_LINES=$(wc -l < "$ARCHIVO")

 echo "+============================================+"
 echo "| Checklist PASO 0 |"
 echo "+============================================+"
 echo ""
 echo "Archivo: $ARCHIVO"
 echo "Total de líneas: $TOTAL_LINES"
 echo ""
 echo "IMPORTANTE: Debes leer TODAS las $TOTAL_LINES líneas"
 echo ""

 # Mostrar mapa del archivo
 echo "Mapa del archivo (cada X = 10 líneas):"
 DECENAS=$((TOTAL_LINES / 10))
 for ((i=0; i<DECENAS; i++)); do
 echo -n "X"
 done
 echo ""
 echo ""

 # Preguntas de verificación
 echo "Preguntas de verificación:"
 echo ""

 read -p "¿Leíste desde línea 1? (s/n): " resp1
 read -p "¿Leíste hasta línea $TOTAL_LINES? (s/n): " resp2
 read -p "¿Identificaste TODOS los elementos? (s/n): " resp3
 read -p "¿Creaste un inventario completo? (s/n): " resp4

 echo ""

 if [ "$resp1" = "s" ] && [ "$resp2" = "s" ] && [ "$resp3" = "s" ] && [ "$resp4" = "s" ]; then
 echo "[OK] PASO 0 COMPLETO - Listo para traducir"
 exit 0
 else
 echo "[ERROR] PASO 0 INCOMPLETO - NO comenzar traducción todavía"
 echo ""
 echo "Vuelve al archivo y completa la lectura."
 exit 1
 fi




Integración con Make
====================

Agregar a Makefile
==================

.. code-block:: makefile

 .PHONY: verificar verificar-lote

 verificar:
 @echo "Verificando traducción..."
 @./scripts/verificar_traduccion.sh $(ORIG) $(TRAD)

 verificar-lote:
 @echo "Verificando lote completo..."
 @./scripts/verificar_lote.sh $(ORIG_DIR) $(TRAD_DIR)

**Uso:**

.. code-block:: bash

 make verificar ORIG=original/file.md TRAD=traduccion/file.rst
 make verificar-lote ORIG_DIR=original/ TRAD_DIR=traduccion/




Personalización
===============

Ajustar Umbrales
================

En ``verificar_traduccion.sh``, modifica:

.. code-block:: bash

 # Línea ~150 - Ajustar umbrales de enriquecimiento
 if [ $ORIG_LINES -lt 20 ]; then
 MIN_ENRIQ=300 # Cambiar aquí
 MAX_ENRIQ=1000 # Y aquí
 fi

 # Línea ~350 - Ajustar calificación final
 if [ $PORCENTAJE -ge 95 ]; then # Cambiar umbral
 echo "[OK] EXCELENTE"
 fi

Agregar Checks Personalizados
=============================

.. code-block:: bash

 # Agregar después de CHECK 6

 echo "==========================================="
 echo "CHECK 7: Mi Check Personalizado"
 echo "==========================================="

 # Tu lógica aquí
 MI_METRICA=$(grep -c "patrón" "$TRADUCIDO")

 if [ $MI_METRICA -gt 0 ]; then
 echo "[OK] Check OK"
 SCORE_TOTAL=$((SCORE_TOTAL + 10))
 fi
 CHECKS_TOTAL=$((CHECKS_TOTAL + 10))




Instalación
===========

Paso a Paso
===========

.. code-block:: bash

 # 1. Crear directorio de scripts
 mkdir -p ~/adt-scripts
 cd ~/adt-scripts

 # 2. Copiar scripts
 # (copiar contenido de arriba a archivos .sh)

 # 3. Dar permisos de ejecución
 chmod +x verificar_traduccion.sh
 chmod +x verificar_lote.sh
 chmod +x prevenir_omisiones.sh

 # 4. Agregar al PATH (opcional)
 echo 'export PATH="$HOME/adt-scripts:$PATH"' >> ~/.bashrc
 source ~/.bashrc

 # 5. Probar
 verificar_traduccion.sh --help




.. seealso::
 * :doc:`../../03_estandares/calidad/checklist_revision` - Checklists manuales
 * :doc:`../../06_casos_practicos/errores_comunes/error_01_omisiones` - Por qué verificar
 * :doc:`../../07_guias_uso/troubleshooting` - Solución de problemas

.. note::
 Estos scripts son herramientas de apoyo. La verificación manual sigue siendo importante para calidad óptima.
