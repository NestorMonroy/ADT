.. _checklist_revision:

===============================================
Checklist de Revisión de Traducción
===============================================

:Sección: 03_estandares/calidad
:Base: Workflow v1.7.2 + Scripts de verificación arc42
:Aplicabilidad: Toda traducción ADT
:Última actualización: 2026-01-28

.. contents:: Contenido
 :depth: 3
 :local:

----

Introducción
============

Este documento provee **checklists accionables** para cada fase del proceso de traducción.

**Base empírica:**
 Checklists extraídos de la aplicación exitosa del Workflow v1.7.2 en arc42 (196 archivos, 0 omisiones en secciones 10-12).

**Propósito:**
 Asegurar que ningún paso crítico se omita durante traducción y verificación.

----

PASO 0: Pre-Traducción (CRÍTICO)
=================================

**Duración:** 5-10 minutos
**Importancia:** CRÍTICA
**Omitir este paso:** [ERROR] Causa omisiones de contenido

Checklist PASO 0
----------------

.. code-block:: text

 [ ] 1. Leer archivo principal COMPLETO (no solo inicio)

 ¿Cuántas líneas tiene? _____
 ¿Leí hasta la última línea? [ ] SÍ [ ] NO

 [ERROR] NO hacer: Leer solo primeras 50 líneas
 [OK] SÍ hacer: Leer de línea 1 a línea N

 [ ] 2. Identificar TODOS los componentes

 [ ] Título de sección
 [ ] Content
 [ ] Motivation
 [ ] Form
 [ ] Subsecciones (enumerar): _____________
 [ ] Further information
 [ ] Plantilla vacía (si aplica)

 [ ] 3. Identificar archivos asociados

 [ ] Tips: ¿Cuántos? _____
 [ ] Ejemplos: ¿Cuántos? _____
 [ ] Otros archivos: _____

 Total archivos: _____

 [ ] 4. Crear inventario exhaustivo

 Listar TODOS los archivos a traducir:
 1. ___________________________
 2. ___________________________
 3. ___________________________
 ...

 [ ] 5. Estimar complejidad

 Tamaño archivo principal: _____ líneas

 Clasificación:
 [ ] < 50 líneas (Baja complejidad)
 [ ] 50-100 líneas (Media complejidad)
 [ ] > 100 líneas (Alta complejidad)

 Enriquecimiento esperado: +_____ %

**Ejemplo Real - Sección 12:**

.. code-block:: text

 [OK] CORRECTO (Sección 12 de arc42):

 [OK] 1. Leído section-12.md completo: 44 líneas
 [OK] 2. Componentes identificados:
 [OK] Título: "12. Glossary"
 [OK] Content (líneas 12-15)
 [OK] Motivation (líneas 17-21)
 [OK] Form (líneas 23-30)
 [OK] Plantilla vacía (línea 37)
 [OK] Further info (líneas 40-43)

 [OK] 3. Archivos asociados:
 [OK] Tips: 6 (t-12-1 a t-12-6)
 [OK] Ejemplos: 1 (glossary-htmlsc)
 Total: 8 archivos

 [OK] 4. Inventario creado: 8 archivos listados
 [OK] 5. Complejidad: Baja (44 líneas)
 Enriquecimiento esperado: +200% a +300%

 Resultado: 0 omisiones, 8/8 archivos traducidos [OK]

**Contra-ejemplo - Sección 07 (versión inicial):**

.. code-block:: text

 [ERROR] INCORRECTO (Sección 07 inicial):

 [ ] 1. Solo leídas primeras 50 de 126 líneas
 [ ] 2. NO identificados todos los componentes
 [ ] 3. NO contados todos los archivos
 [ ] 4. NO creado inventario exhaustivo
 [ ] 5. NO estimada complejidad real

 Resultado: 6 omisiones, 8/14 archivos [ERROR]

 Corrección: Aplicar PASO 0 correctamente
 Resultado final: 0 omisiones, 14/14 archivos [OK]

----

PASO 1: Durante la Traducción
==============================

**Duración:** Variable según tamaño
**Importancia:** CRÍTICA
**Objetivo:** Traducir TODO sin omitir nada

Checklist por Lote
------------------

**Para cada lote de archivos:**

.. code-block:: text

 [ ] 1. Traducción COMPLETA

 [ ] TODO el contenido del original incluido
 [ ] 0% de omisiones
 [ ] Estructura preservada

 Verificar:
 [ ] Todos los párrafos
 [ ] Todas las listas
 [ ] Todas las tablas
 [ ] Todos los ejemplos de código
 [ ] Todas las imágenes referenciadas
 [ ] Todas las citas

 [ ] 2. Terminología consistente

 [ ] Usar glosario de términos
 [ ] Mismos términos que en archivos previos
 [ ] Términos técnicos conservados apropiadamente

 Consultar:
 [ ] Glosario del proyecto
 [ ] Archivos ya traducidos
 [ ] Matriz de decisión traducir/conservar

 [ ] 3. Enriquecimiento apropiado

 Tamaño original: _____ líneas
 Tamaño traducido: _____ líneas
 Enriquecimiento: _____ %

 [ ] ¿Está en rango apropiado?
 [ ] ¿Ejemplos agregados tienen valor?
 [ ] ¿Sin divagaciones innecesarias?

 [ ] 4. Formato RST correcto

 [ ] Títulos con líneas de igual longitud
 [ ] Listas con espaciado correcto
 [ ] Código con directivas apropiadas
 [ ] Tablas con formato consistente
 [ ] Referencias con sintaxis correcta

 [ ] 5. Referencias cruzadas

 [ ] Links internos con :ref:
 [ ] Links a secciones con :doc:
 [ ] Links externos con URL completa
 [ ] Toctrees completos

**Después de cada lote:**

.. code-block:: text

 [ ] Compilar con make html
 [ ] Revisar warnings nuevos
 [ ] Verificar HTML generado
 [ ] Corregir errores inmediatamente

----

PASO 2: Verificación Post-Traducción
=====================================

**Duración:** 30-60 minutos
**Importancia:** 🟡 ALTA
**Objetivo:** Asegurar calidad antes de considerar completo

Checklist de Verificación Automatizada
---------------------------------------

**Ejecutar script de verificación:**

.. code-block:: bash

 #!/bin/bash
 # verificar_traduccion.sh

 ORIGINAL="original/section-XX.md"
 TRADUCIDO="traduccion/seccion_XX.rst"

 echo "+======================================+"
 echo "| VERIFICACIÓN DE TRADUCCIÓN |"
 echo "+======================================+"
 echo ""

 # Verificar elementos críticos
 echo "1. Verificando elementos principales..."
 grep -q "Título" "$TRADUCIDO" && echo "[OK] Título" || echo "[ERROR] Título OMITIDO"
 grep -q "Content" "$TRADUCIDO" && echo "[OK] Content" || echo "[ERROR] Content OMITIDO"
 grep -q "Motivation" "$TRADUCIDO" && echo "[OK] Motivation" || echo "[ERROR] Motivation OMITIDO"
 grep -q "Form" "$TRADUCIDO" && echo "[OK] Form" || echo "[ERROR] Form OMITIDO"

 # Contar archivos
 ESPERADOS=$(find original/ -name "*-XX-*" | wc -l)
 TRADUCIDOS=$(find traduccion/ -name "*.rst" | wc -l)

 echo ""
 echo "2. Verificando archivos..."
 echo " Esperados: $ESPERADOS"
 echo " Traducidos: $TRADUCIDOS"

 if [ $TRADUCIDOS -eq $ESPERADOS ]; then
 echo " [OK] TODOS LOS ARCHIVOS COMPLETADOS"
 else
 echo " [ERROR] FALTAN $((ESPERADOS - TRADUCIDOS)) ARCHIVOS"
 fi

**Checklist Manual:**

.. code-block:: text

 [ ] 1. Ejecutar script de verificación

 Resultado: _____ / _____ elementos [OK]

 [ ] ¿100% elementos presentes? SÍ / NO

 [ ] 2. Verificación visual contra original

 [ ] Abrir original lado a lado con traducción
 [ ] Recorrer línea por línea
 [ ] Marcar cada elemento verificado

 Método:
 - Original en pantalla izquierda
 - Traducción en pantalla derecha
 - Marcar cada párrafo verificado con [OK]

 [ ] 3. Compilación Sphinx

 $ make clean && make html

 [ ] Build succeeded? SÍ / NO
 [ ] Errores: _____
 [ ] Warnings críticos: _____
 [ ] HTML generado correctamente? SÍ / NO

 [ ] 4. Revisión de HTML

 [ ] Abrir build/html/index.html
 [ ] Navegar a sección traducida
 [ ] Verificar:
 [ ] Formato visual correcto
 [ ] Tablas se ven bien
 [ ] Imágenes cargan
 [ ] Links funcionan
 [ ] Código tiene syntax highlighting

 [ ] 5. Búsqueda de placeholders

 $ grep -r "TODO\|FIXME\|XXX\|PENDIENTE" traduccion/

 Resultados: _____

 [ ] ¿Todos resueltos? SÍ / NO

Checklist de Completitud Específica
------------------------------------

**Para archivo principal:**

.. code-block:: text

 Verificar contra original línea por línea:

 [ ] Línea 1-10: _____________________
 [ ] Línea 11-20: _____________________
 [ ] Línea 21-30: _____________________
 ...
 [ ] Última línea: _____________________

 Elementos especiales:
 [ ] Front matter (YAML) procesado
 [ ] Includes ({% include %}) expandidos
 [ ] Variables sustituidas
 [ ] Plantillas llenadas

**Para tips:**

.. code-block:: text

 [ ] Título del tip completo
 [ ] Metadata (categoría, palabras clave)
 [ ] Contenido principal (100%)
 [ ] Ejemplos de código (todos)
 [ ] Listas (todas)
 [ ] Imágenes (todas referenciadas)
 [ ] Enlaces externos (todos)
 [ ] Seealso / Related (si aplica)

**Para ejemplos:**

.. code-block:: text

 [ ] Nombre del proyecto/sistema
 [ ] Contexto del ejemplo
 [ ] Diagrama/imagen principal
 [ ] Descripción textual
 [ ] Código fuente (si aplica)
 [ ] Explicación de elementos
 [ ] Lecciones aprendidas
 [ ] Referencias

----

PASO 3: Documentación Final
============================

**Duración:** 15-30 minutos
**Importancia:** 🟢 MEDIA
**Objetivo:** Documentar el trabajo realizado

Checklist de Checkpoint
------------------------

.. code-block:: text

 [ ] 1. Crear archivo CHECKPOINT.md

 Ubicación: sections/XX_nombre/SECCION_XX_FINAL_CHECKPOINT.md

 Contenido obligatorio:
 [ ] Fecha de finalización
 [ ] Sección y número
 [ ] Workflow aplicado (versión)
 [ ] Estado (% completado)
 [ ] Lista de archivos traducidos
 [ ] Tamaño total
 [ ] Métricas de enriquecimiento

 [ ] 2. Documentar métricas

 [ ] Total archivos: _____
 [ ] Tamaño total: _____ KB
 [ ] Enriquecimiento promedio: _____ %
 [ ] Tiempo invertido: _____ horas
 [ ] Velocidad: _____ archivos/hora

 [ ] 3. Listar archivos traducidos

 Formato:
 1. archivo_1.rst (X.X KB) - Descripción
 2. archivo_2.rst (X.X KB) - Descripción
 ...

 [ ] 4. Identificar referencias pendientes

 [ ] Referencias a secciones no traducidas: _____
 [ ] Warnings de compilación: _____
 [ ] Items para futuro: _____

 [ ] 5. Lecciones aprendidas

 [ ] ¿Qué funcionó bien?
 [ ] ¿Qué se podría mejorar?
 [ ] ¿Errores cometidos y corregidos?
 [ ] ¿Tiempo real vs estimado?

Plantilla de Checkpoint
------------------------

.. code-block:: markdown

 # CHECKPOINT FINAL - SECCIÓN XX NOMBRE - 100% COMPLETADA

 **Fecha:** YYYY-MM-DD
 **Sección:** XX - Nombre
 **Workflow:** vX.Y.Z
 **Estado:** [OK] COMPLETADA 100% (N/N archivos)

 ---

 ## ARCHIVOS COMPLETADOS

 ### Archivo Principal

 1. `seccion_XX_nombre.rst` (X.X KB)
 - Contenido completo
 - Toctrees
 - Referencias

 ### Tips (N archivos)

 1. `nombre_tip_1.rst` (X.X KB) - Descripción
 2. `nombre_tip_2.rst` (X.X KB) - Descripción
 ...

 ### Ejemplos (N archivos)

 1. `nombre_ejemplo_1.rst` (X.X KB) - Descripción
 ...

 **Tamaño total:** XX KB (N archivos)

 ---

 ## VERIFICACIÓN

 [OK] Checklist completado (N/N elementos)
 [OK] Compilación exitosa
 [OK] 0 omisiones detectadas

 ---

 ## MÉTRICAS

 - Enriquecimiento promedio: +XX%
 - Tiempo invertido: X horas
 - Velocidad: X archivos/hora

 ---

 ## LECCIONES APRENDIDAS

 [OK] Lo que funcionó bien:
 - Item 1
 - Item 2

 [WARNING] A mejorar:
 - Item 1
 - Item 2

----

Checklists por Tipo de Archivo
===============================

Tips Breves (< 20 líneas originales)
-------------------------------------

.. code-block:: text

 [ ] PASO 0
 [ ] Leer tip completo
 [ ] Identificar elementos (título, contenido, ejemplos)

 [ ] TRADUCCIÓN
 [ ] Título completo
 [ ] TODO el contenido
 [ ] Agregar ejemplos prácticos
 [ ] Agregar checklist si aplica
 [ ] Agregar tabla comparativa si ayuda

 [ ] ENRIQUECIMIENTO
 [ ] Objetivo: +300% a +1000%
 [ ] Ejemplos concretos agregados
 [ ] Contexto adicional
 [ ] Casos de uso

 [ ] VERIFICACIÓN
 [ ] Original 100% incluido
 [ ] Enriquecimiento en rango
 [ ] Compila correctamente

 [ ] SEEALSO
 [ ] Referencias a tips relacionados
 [ ] Referencias a secciones relevantes

Secciones Principales (40-100 líneas)
--------------------------------------

.. code-block:: text

 [ ] PASO 0
 [ ] Leer sección COMPLETA
 [ ] Identificar subsecciones (X.1, X.2, etc.)
 [ ] Contar tips asociados
 [ ] Contar ejemplos asociados

 [ ] TRADUCCIÓN
 [ ] Título sección
 [ ] Introducción/descripción
 [ ] Content
 [ ] Motivation
 [ ] Form
 [ ] Subsección X.1 completa
 [ ] Subsección X.2 completa
 [ ] ...
 [ ] Further information
 [ ] Plantilla vacía (si aplica)

 [ ] TOCTREES
 [ ] Toctree con todos los tips
 [ ] Toctree con todos los ejemplos
 [ ] Captions apropiados

 [ ] ENRIQUECIMIENTO
 [ ] Objetivo: +100% a +300%
 [ ] Tip inicial contextual
 [ ] Sección "Relación con otras secciones"
 [ ] Notas adicionales si ayudan

 [ ] VERIFICACIÓN
 [ ] Todos los elementos presentes
 [ ] Todas las subsecciones incluidas
 [ ] Toctrees completos
 [ ] Compila exitosamente

Ejemplos
--------

.. code-block:: text

 [ ] PASO 0
 [ ] Leer ejemplo completo
 [ ] Identificar diagrama/imagen
 [ ] Identificar código fuente

 [ ] TRADUCCIÓN
 [ ] Título del ejemplo
 [ ] Nombre del sistema/proyecto
 [ ] Contexto
 [ ] Descripción
 [ ] Diagrama referenciado
 [ ] Código fuente (si aplica)
 [ ] Explicación de elementos

 [ ] ENRIQUECIMIENTO
 [ ] Análisis del ejemplo
 [ ] Lecciones aprendidas
 [ ] Tabla de elementos (si ayuda)
 [ ] Versiones alternativas (opcional)

 [ ] VERIFICACIÓN
 [ ] Imagen visible en HTML
 [ ] Código con syntax highlighting
 [ ] Todos los elementos explicados

----

Checklist de Emergencia
========================

**Si encuentras problema durante verificación:**

Problema: Contenido Omitido
----------------------------

.. code-block:: text

 [ ] 1. DETENER traducción de archivos nuevos
 [ ] 2. Volver al archivo original
 [ ] 3. Identificar contenido faltante
 [ ] 4. Agregar contenido omitido
 [ ] 5. Re-verificar completitud
 [ ] 6. Re-compilar
 [ ] 7. Continuar solo si 100%

Problema: Compilación Falla
----------------------------

.. code-block:: text

 [ ] 1. Leer mensaje de error completo
 [ ] 2. Identificar archivo y línea
 [ ] 3. Abrir archivo problemático
 [ ] 4. Corregir sintaxis RST
 [ ] 5. Intentar compilar de nuevo
 [ ] 6. Repetir hasta make html exitoso

Problema: Warnings Excesivos
-----------------------------

.. code-block:: text

 [ ] 1. Categorizar warnings
 [ ] Críticos (errores de sintaxis)
 [ ] No-críticos (referencias futuras)
 [ ] 2. Corregir todos los críticos
 [ ] 3. Documentar no-críticos
 [ ] 4. Verificar que no-críticos son esperados

----

Resumen de Checklists
=====================

**Resumen por Fase:**

.. list-table::
 :header-rows: 1
 :widths: 20 15 15 50

 * - **Fase**
 - **Duración**
 - **Items**
 - **Objetivo**
 * - PASO 0
 - 5-10 min
 - 5
 - Identificar TODO antes de empezar
 * - Durante Traducción
 - Variable
 - 5 por lote
 - Traducir sin omitir nada
 * - Verificación
 - 30-60 min
 - 5
 - Asegurar calidad
 * - Documentación
 - 15-30 min
 - 5
 - Documentar trabajo realizado

**Total Items:** ~20 checks por proyecto

**Tiempo Total de Checklists:** ~1-2 horas adicionales

**Beneficio:** 0 omisiones, calidad garantizada

----

.. seealso::
 * :doc:`criterios_calidad` - Criterios de evaluación
 * :doc:`metricas_traduccion` - Métricas cuantitativas
 * :doc:`../../02_procedimientos/workflow_general` - Workflow completo v1.7.2

.. note::
 Estos checklists están basados en scripts de verificación reales usados en arc42. Actualizar según experiencia en cada proyecto.
