.. _error_omisiones:

===============================================
Error Común: Omisiones en Traducción
===============================================

:Caso: EC-001
:Tipo: Error y Corrección
:Sección: arc42 - Sección 07 (Deployment View)
:Problema: 6 secciones omitidas (57% completitud)
:Causa: NO aplicar PASO 0 correctamente
:Resultado: [OK] Corregido (14/14 archivos, 100%)

.. contents:: Contenido
 :depth: 3
 :local:

----

Resumen Ejecutivo
=================

**Error Cometido:**
 Omitir 6 secciones al traducir Sección 07 de arc42.

**Causa Raíz:**
 NO leer archivo completo antes de traducir (PASO 0 incompleto).

**Impacto:**
 Solo 8/14 archivos traducidos (57% completitud).

**Corrección:**
 Aplicar PASO 0 correctamente -> 14/14 archivos (100%).

**Lección:**
 [WARNING] **PASO 0 ES CRÍTICO Y NO NEGOCIABLE**

----

Contexto del Error
==================

Situación Inicial
-----------------

**Tarea:**

.. code-block:: text

 Traducir Sección 07 "Deployment View" de arc42

 Archivo principal: section-07.md
 Ubicación: arc42/sections/07_deployment_view/
 Complejidad: Media

**Estado Mental del Traductor:**

.. code-block:: text

 [ERROR] "Ya traduje 6 secciones, conozco el patrón"
 [ERROR] "Este archivo parece corto, será rápido"
 [ERROR] "Voy a empezar a traducir directamente"

 Resultado: OMISIONES

Información del Archivo
-----------------------

**section-07.md (126 líneas):**

.. code-block:: text

 LÍNEAS 1-10: Front matter YAML
 LÍNEAS 12-50: Introducción y secciones principales
 LÍNEAS 51-126: Subsecciones y detalles adicionales [WARNING]

**Problema:**

.. code-block:: text

 El traductor solo leyó líneas 1-50 [ERROR]

 Pensó: "Ya vi el patrón, esto es suficiente"

 Omitió: Líneas 51-126 (60% del archivo)

----

El Error: Versión Inicial
==========================

PASO 0 Incompleto
-----------------

**[ERROR] Lo que se hizo INCORRECTAMENTE:**

.. code-block:: text

 1. Abrir section-07.md
 2. Leer primeras 50 líneas
 3. Ver estructura familiar:
 - Título "7. Deployment View"
 - Content
 - Motivation
 - Form
 4. Pensar: "Ok, ya sé qué traducir"
 5. Empezar a traducir INMEDIATAMENTE

 [PENDING] Tiempo en "PASO 0": 3 minutos [ERROR]

 Resultado: INVENTARIO INCOMPLETO

**Inventario Creado (INCORRECTO):**

.. code-block:: text

 Archivos identificados:
 1. [OK] section-07.md (principal)
 2. [OK] 10 tips (t-7-1 a t-7-10)
 3. [OK] 3 ejemplos

 Total: 14 archivos

 [ERROR] PERO: No identificó TODO el contenido del principal

Traducción Inicial
-------------------

**Archivos traducidos:**

.. code-block:: text

 [OK] seccion_07_vista_despliegue.rst (parcial)
 [OK] deployment_tip_1.rst a deployment_tip_10.rst
 [OK] deployment_ejemplo_1.rst a deployment_ejemplo_3.rst

 Total: 14 archivos aparentemente completos

**Contenido del archivo principal (INCOMPLETO):**

.. code-block:: rst

 ================================
 7. Vista de Despliegue
 ================================

 Introducción
 ============
 [Traducido]

 Content
 =======
 [Traducido]

 Motivation
 ==========
 [Traducido]

 Form
 ====
 [Traducido]

 .. toctree::
 :caption: Tips
 [10 tips]

 .. toctree::
 :caption: Ejemplos
 [3 ejemplos]

 Referencias
 ===========
 [Traducido]

 # FIN [ERROR]

**Problema:** Archivo "completo" pero faltaban 6 subsecciones.

Compilación Inicial
-------------------

.. code-block:: bash

 $ make html

 Running Sphinx...
 building [html]: targets for 14 source files
 ...
 build succeeded.

 [OK] Compilación exitosa

 [ERROR] PERO: Contenido incompleto no detectado

**Por qué compiló:**

.. code-block:: text

 - Sintaxis RST correcta [OK]
 - Toctrees completos [OK]
 - Referencias válidas [OK]

 PERO:
 - Contenido omitido [ERROR]
 - Subsecciones faltantes [ERROR]

 Sphinx no detecta omisiones de contenido

----

Detección del Error
===================

Verificación Manual
-------------------

**Días después, revisión de calidad:**

.. code-block:: bash

 $ diff -u original/section-07.md traduccion/seccion_07_vista_despliegue.rst

 [Muchas diferencias...]

**Lectura lado a lado:**

.. code-block:: text

 Original (pantalla izquierda): Traducido (pantalla derecha):

 7. Deployment View 7. Vista de Despliegue
 Content... Content... [OK]
 Motivation... Motivation... [OK]
 Form... Form... [OK]

 7.1 Infrastructure Level 1 [OMITIDO] [ERROR]
 Content...
 Motivation...

 7.1.1 Subsection [OMITIDO] [ERROR]
 ...

 7.2 Infrastructure Level 2 [OMITIDO] [ERROR]
 ...

**Descubrimiento:**

.. code-block:: text

 [ERROR] 7.1 Infrastructure Level 1 - OMITIDO
 [ERROR] 7.1.1 Subsection - OMITIDO
 [ERROR] 7.1.2 Subsection - OMITIDO
 [ERROR] 7.2 Infrastructure Level 2 - OMITIDO
 [ERROR] 7.2.1 Subsection - OMITIDO
 [ERROR] 7.2.2 Subsection - OMITIDO

 Total: 6 secciones omitidas

Script de Verificación
----------------------

**Script creado para confirmar:**

.. code-block:: bash

 #!/bin/bash
 # verificar_seccion_07_INICIAL.sh

 echo "Verificando section-07.md..."

 # Buscar subsecciones en original
 echo ""
 echo "Subsecciones en original:"
 grep "^### " original/section-07.md | nl

 echo ""
 echo "Subsecciones en traducción:"
 grep -E "^-{4,}$" -B 1 traduccion/seccion_07_vista_despliegue.rst | grep -v "^--$" | nl

**Resultado:**

.. code-block:: text

 Subsecciones en original:
 1 ### 7.1 Infrastructure Level 1
 2 ### 7.1.1 Subsection
 3 ### 7.1.2 Subsection
 4 ### 7.2 Infrastructure Level 2
 5 ### 7.2.1 Subsection
 6 ### 7.2.2 Subsection

 Subsecciones en traducción:
 (vacío)

 [ERROR] 0/6 subsecciones traducidas

Análisis de Causa Raíz
-----------------------

**5 Porqués:**

.. code-block:: text

 1. ¿Por qué se omitieron 6 secciones?
 -> Porque no estaban en el inventario inicial

 2. ¿Por qué no estaban en el inventario?
 -> Porque el traductor no leyó el archivo completo

 3. ¿Por qué no leyó el archivo completo?
 -> Porque asumió conocer el patrón por secciones previas

 4. ¿Por qué asumió conocer el patrón?
 -> Porque no aplicó PASO 0 metódicamente

 5. ¿Por qué no aplicó PASO 0?
 -> Porque subestimó su importancia

 CAUSA RAÍZ: Subestimar importancia de PASO 0

**Factores Contribuyentes:**

.. code-block:: text

 [ERROR] Exceso de confianza (6 secciones ya traducidas)
 [ERROR] Impaciencia (querer empezar rápido)
 [ERROR] Asumir sin verificar (patrón conocido)
 [ERROR] No usar checklist de PASO 0
 [ERROR] No leer hasta última línea

----

La Corrección
=============

PASO 0 Correcto
---------------

**[OK] Lo que se hizo CORRECTAMENTE:**

.. code-block:: text

 1. Abrir section-07.md
 2. Leer desde línea 1 hasta línea 126 (COMPLETO) [OK]
 3. Marcar cada elemento encontrado [OK]
 4. Crear inventario exhaustivo [OK]
 5. Contar líneas para verificar [OK]

 [PENDING] Tiempo en PASO 0: 15 minutos [OK]

 Resultado: INVENTARIO COMPLETO

**Inventario Corregido (CORRECTO):**

.. code-block:: text

 ARCHIVO PRINCIPAL (126 líneas):

 [OK] Líneas 1-10: Front matter
 [OK] Línea 12: Título "7. Deployment View"
 [OK] Líneas 14-18: Content
 [OK] Líneas 20-24: Motivation
 [OK] Líneas 26-35: Form

 [OK] Líneas 40-55: 7.1 Infrastructure Level 1
 [OK] Líneas 42-44: Content
 [OK] Líneas 46-48: Motivation
 [OK] Líneas 50-52: Form

 [OK] Líneas 58-70: 7.1.1 Subsection
 [Detalles...]

 [OK] Líneas 73-85: 7.1.2 Subsection
 [Detalles...]

 [OK] Líneas 90-102: 7.2 Infrastructure Level 2
 [OK] Content
 [OK] Motivation
 [OK] Form

 [OK] Líneas 105-115: 7.2.1 Subsection
 [Detalles...]

 [OK] Líneas 118-126: 7.2.2 Subsection
 [Detalles...]

 ARCHIVOS ASOCIADOS:
 [OK] 10 tips (t-7-1 a t-7-10)
 [OK] 3 ejemplos

 TOTAL: 14 archivos
 ELEMENTOS en principal: 13 (no 7)

**Diferencia Crítica:**

.. code-block:: text

 INICIAL (incorrecto):
 - Identificó 7 elementos
 - Líneas leídas: 50/126 (40%)

 CORREGIDO:
 - Identificó 13 elementos
 - Líneas leídas: 126/126 (100%)

 Diferencia: 6 elementos omitidos

Traducción Corregida
--------------------

**Archivo principal actualizado:**

.. code-block:: rst

 ================================
 7. Vista de Despliegue
 ================================

 Introducción
 ============
 [Ya existía]

 Content
 =======
 [Ya existía]

 Motivation
 ==========
 [Ya existía]

 Form
 ====
 [Ya existía]

 7.1 Infrastructure Level 1
 ===========================
 [AGREGADO] [OK]

 Content
 -------
 [AGREGADO] [OK]

 Motivation
 ----------
 [AGREGADO] [OK]

 Form
 ----
 [AGREGADO] [OK]

 7.1.1 Subsección
 ^^^^^^^^^^^^^^^^
 [AGREGADO] [OK]

 7.1.2 Subsección
 ^^^^^^^^^^^^^^^^
 [AGREGADO] [OK]

 7.2 Infrastructure Level 2
 ===========================
 [AGREGADO] [OK]

 Content
 -------
 [AGREGADO] [OK]

 Motivation
 ----------
 [AGREGADO] [OK]

 Form
 ----
 [AGREGADO] [OK]

 7.2.1 Subsección
 ^^^^^^^^^^^^^^^^
 [AGREGADO] [OK]

 7.2.2 Subsección
 ^^^^^^^^^^^^^^^^
 [AGREGADO] [OK]

 .. toctree::
 :caption: Tips
 [10 tips - ya existían]

 .. toctree::
 :caption: Ejemplos
 [3 ejemplos - ya existían]

 Referencias
 ===========
 [Ya existía]

**Cambios:**

.. code-block:: text

 Agregadas: 6 secciones completas
 Agregadas: ~80 líneas de contenido
 Estructura: Ahora completa

Verificación Final
------------------

**Script de verificación (corregido):**

.. code-block:: bash

 $ bash verificar_seccion_07_CORREGIDO.sh

 Verificando section-07.md...

 [OK] 1. Título "7. Deployment View"
 [OK] 2. Content principal
 [OK] 3. Motivation principal
 [OK] 4. Form principal
 [OK] 5. Sección 7.1 Infrastructure Level 1
 [OK] 6. Sección 7.1.1 Subsection
 [OK] 7. Sección 7.1.2 Subsection
 [OK] 8. Sección 7.2 Infrastructure Level 2
 [OK] 9. Sección 7.2.1 Subsection
 [OK] 10. Sección 7.2.2 Subsection
 [OK] 11. Toctree tips (10)
 [OK] 12. Toctree ejemplos (3)
 [OK] 13. Referencias

 Resultado: 13/13 elementos [OK] PRESENTE (100%)

 Archivos: 14/14 [OK]

**Compilación final:**

.. code-block:: bash

 $ make clean && make html

 build succeeded.

 The HTML pages are in build/html.

[OK] **Sección 07 ahora 100% completa**

----

Impacto del Error
=================

Comparación Antes/Después
--------------------------

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Métrica**
   - **Versión Inicial**
   - **Versión Corregida**
 * - Archivos
   - 14/14
   - 14/14
 * - Contenido principal
   - 57% completo [ERROR]
   - 100% completo [OK]
 * - Elementos presentes
   - 7/13
   - 13/13
 * - Subsecciones
   - 0/6 [ERROR]
   - 6/6 [OK]
 * - Tiempo PASO 0
   - 3 min
   - 15 min
 * - Tiempo re-trabajo
   - 0
   - 2 horas [ERROR]

**Costo del Error:**

.. code-block:: text

 Tiempo ahorrado (PASO 0 rápido): 12 minutos
 Tiempo perdido (re-trabajo): 2 horas

 Pérdida neta: 1h 48min [ERROR]

 Ratio: Ahorrar 12 min costó 108 min

Impacto en Calidad
------------------

**Versión Inicial:**

.. code-block:: text

 Criterio: Completitud (100% requerido)
 Logrado: 57%

 [ERROR] NO APROBADO

 Razón: 43% del contenido omitido

**Versión Corregida:**

.. code-block:: text

 Criterio: Completitud (100% requerido)
 Logrado: 100%

 [OK] APROBADO

Impacto en Proyecto
-------------------

**Si no se hubiera detectado:**

.. code-block:: text

 Usuarios leyendo documentación:
 [ERROR] "¿Dónde está la sección 7.1?"
 [ERROR] "Esto está incompleto"
 [ERROR] "No puedo usar esta documentación"

 Reputación del proyecto:
 [ERROR] Documentación de baja calidad
 [ERROR] Desconfianza en traducción
 [ERROR] Pérdida de credibilidad

----

Lecciones Aprendidas
====================

[OK] Lección Principal
--------------------

**PASO 0 ES CRÍTICO Y NO NEGOCIABLE**

.. code-block:: text

 [WARNING] SIEMPRE:

 1. Leer archivo COMPLETO (línea 1 a línea N)
 2. Marcar cada elemento encontrado
 3. Crear inventario exhaustivo
 4. Verificar líneas totales
 5. NO asumir conocer el patrón

 Tiempo: 10-15 minutos
 Beneficio: Previene 100% omisiones

**Fórmula del Éxito:**

.. code-block:: text

 PASO 0 Completo (15 min)
 +
 Traducción sin omisiones (2 horas)
 =
 Resultado perfecto [OK]

 vs

 PASO 0 Incompleto (3 min)
 +
 Traducción con omisiones (2 horas)
 +
 Re-trabajo (2 horas)
 =
 Resultado correcto pero 2 horas perdidas [ERROR]

Señales de Advertencia
-----------------------

**[ALERT] Estás en riesgo de omisiones si:**

.. code-block:: text

 [ERROR] "Ya conozco el patrón, no necesito leer todo"
 [ERROR] "Este archivo parece corto"
 [ERROR] "Voy a leer solo el inicio"
 [ERROR] "No tengo tiempo para PASO 0 completo"
 [ERROR] "La verificación es opcional"

 Resultado probable: OMISIONES

**[OK] Estás seguro si:**

.. code-block:: text

 [OK] "Voy a leer hasta la última línea"
 [OK] "Voy a marcar cada elemento"
 [OK] "Voy a crear checklist exhaustivo"
 [OK] "PASO 0 es inversión, no gasto"
 [OK] "Verificación es obligatoria"

 Resultado probable: 100% COMPLETITUD

Prevención de Errores
----------------------

**Checklist Anti-Omisiones:**

.. code-block:: text

 ANTES de traducir:

 [ ] 1. ¿Leí archivo COMPLETO? (línea 1 a N)
 [ ] 2. ¿Verifiqué número total de líneas?
 [ ] 3. ¿Identifiqué TODAS las secciones?
 [ ] 4. ¿Identifiqué TODAS las subsecciones?
 [ ] 5. ¿Creé inventario escrito?
 [ ] 6. ¿Conté archivos esperados?

 Si alguno es NO -> DETENER y completar

**Script de Prevención:**

.. code-block:: bash

 #!/bin/bash
 # prevenir_omisiones.sh

 ORIGINAL="$1"

 if [ ! -f "$ORIGINAL" ]; then
 echo "[ERROR] Archivo no existe: $ORIGINAL"
 exit 1
 fi

 LINEAS=$(wc -l < "$ORIGINAL")
 SECCIONES=$(grep -c "^### " "$ORIGINAL")

 echo "+======================================+"
 echo "| CHECKLIST ANTI-OMISIONES |"
 echo "+======================================+"
 echo ""
 echo "Archivo: $ORIGINAL"
 echo "Líneas totales: $LINEAS"
 echo "Secciones (###): $SECCIONES"
 echo ""
 echo "¿Leíste las $LINEAS líneas? (s/n)"
 read respuesta

 if [ "$respuesta" != "s" ]; then
 echo ""
 echo "[ERROR] DETENTE: Lee el archivo COMPLETO primero"
 exit 1
 fi

 echo ""
 echo "[OK] Bien. Crea inventario de $SECCIONES secciones"
 echo "[OK] Marca cada elemento mientras lees"

**Uso:**

.. code-block:: bash

 $ bash prevenir_omisiones.sh original/section-07.md

 Archivo: original/section-07.md
 Líneas totales: 126
 Secciones (###): 6

 ¿Leíste las 126 líneas? (s/n)
 n

 [ERROR] DETENTE: Lee el archivo COMPLETO primero

Casos Similares
----------------

**Este error es común en:**

.. code-block:: text

 [WARNING] Documentación estructurada (arc42, ISO, RFC)
 [WARNING] Archivos con subsecciones anidadas
 [WARNING] Contenido donde "patrón" puede engañar
 [WARNING] Traducciones bajo presión de tiempo
 [WARNING] Traductores con exceso de confianza

**Menos común en:**

.. code-block:: text

 [OK] Documentación narrativa lineal
 [OK] Archivos muy cortos (< 20 líneas)
 [OK] Contenido sin estructura anidada
 [OK] Traducciones con verificación automática

----

Aplicabilidad a Otros Proyectos
================================

Documentación Estructurada
---------------------------

**Este error puede ocurrir en:**

.. code-block:: text

 [WARNING] Estándares ISO (secciones, subsecciones, anexos)
 [WARNING] RFCs técnicos (múltiples niveles)
 [WARNING] Documentación API (endpoints anidados)
 [WARNING] Manuales técnicos (capítulos, apéndices)
 [WARNING] Especificaciones formales

**Prevención:**

.. code-block:: text

 [OK] SIEMPRE aplicar PASO 0 completo
 [OK] Crear índice de contenido antes de traducir
 [OK] Usar herramientas de diff para verificar
 [OK] Script de verificación automático
 [OK] Revisión por pares

Traducción Colaborativa
------------------------

**Riesgo Mayor:**

.. code-block:: text

 Equipo de 5 traductores
 Cada uno traduce 2-3 secciones

 Sin PASO 0 completo:
 [ERROR] Probabilidad omisiones: 60%+
 [ERROR] Inconsistencias: Altas
 [ERROR] Re-trabajo: Significativo

**Mitigación:**

.. code-block:: text

 [OK] Checklist obligatorio por traductor
 [OK] Script de verificación común
 [OK] Revisión cruzada entre traductores
 [OK] Compilación frecuente del proyecto completo

----

Conclusión
==========

**Resumen del Error:**

.. code-block:: text

 Problema: 6 secciones omitidas (43% contenido faltante)
 Causa: NO leer archivo completo (PASO 0 incompleto)
 Costo: 2 horas de re-trabajo
 Prevención: 15 minutos en PASO 0 completo

**Mensaje Clave:**

.. attention::
 **PASO 0 NO ES OPCIONAL**

 - Leer archivo COMPLETO (línea 1 a N)
 - Crear inventario exhaustivo
 - Verificar sistemáticamente

 15 minutos de PASO 0 previenen 2 horas de re-trabajo

**Regla de Oro:**

.. code-block:: text

 "Mide dos veces, corta una vez"

 Aplicado a traducción:

 "Lee completamente, traduce una vez"

**Verificabilidad:**

Este error y su corrección son verificables en:

- Checkpoint inicial de Sección 07 (incompleto)
- Checkpoint final de Sección 07 (completo)
- Commits Git mostrando correcciones
- Historial de builds de Sphinx

----

.. seealso::
 * :doc:`../../02_procedimientos/workflow_general` - PASO 0 detallado
 * :doc:`../../03_estandares/calidad/checklist_revision` - Checklist completo
 * :doc:`../../03_estandares/calidad/criterios_calidad` - Criterio de completitud
 * :doc:`caso_01_seccion_breve` - Ejemplo de aplicación correcta

.. warning::
 Este es el error #1 más común en traducción de documentación estructurada. PASO 0 completo es la única prevención efectiva.
