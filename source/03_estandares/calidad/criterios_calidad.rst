.. _criterios_calidad:

===============================================
Criterios de Calidad de Traducción ADT
===============================================

:Sección: 03_estandares/calidad
:Base: Experiencia real con arc42 (196 archivos traducidos)
:Aplicabilidad: Todo proyecto de traducción ADT
:Última actualización: 2026-01-28

.. contents:: Contenido
 :depth: 3
 :local:

----

Introducción
============

Este documento define los **criterios de calidad** que aseguran traducciones profesionales y consistentes en el proyecto ADT.

**Base empírica:**
 Estos criterios están basados en la traducción exitosa de **12 secciones de arc42** (196 archivos, ~582 KB), aplicando el Workflow v1.7.2.

**Propósito:**
 Proveer estándares claros y verificables para evaluar la calidad de cualquier traducción en ADT.

----

Los 5 Criterios Fundamentales
==============================

Criterio 1: Completitud (100%)
-------------------------------

**Definición:**
 TODO el contenido del documento original debe estar presente en la traducción.

**Verificación:**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **Aspecto**
   - **Verificación**
 * - Todas las secciones incluidas
   - [OK] Checklist contra original
 * - Todos los párrafos traducidos
   - [OK] Conteo de elementos
 * - Todas las tablas presentes
   - [OK] Inventario de tablas
 * - Todas las imágenes referenciadas
   - [OK] Referencias de figuras
 * - Todos los ejemplos incluidos
   - [OK] Código y ejemplos verificados
 * - Todas las referencias cruzadas
   - [OK] Links internos funcionales

**Ejemplos Reales de Cumplimiento:**

**Sección 12 de arc42 (Glossary):**

.. code-block:: text

 Verificación realizada:
 [OK] 1. Título '12. Glossary' -> PRESENTE
 [OK] 2. Content (líneas 12-15) -> PRESENTE
 [OK] 3. Content - multi-language -> PRESENTE
 [OK] 4. Motivation (líneas 18-21) -> PRESENTE
 [OK] 5. Motivation - sinónimos/homónimos -> PRESENTE
 [OK] 6. Form - tabla simple -> PRESENTE
 [OK] 7. Form - traducciones -> PRESENTE
 [OK] 8. Ejemplo de tabla -> PRESENTE
 [OK] 9. Plantilla vacía -> PRESENTE
 [OK] 10. Toctree 6 tips -> PRESENTE
 [OK] 11. Toctree 1 ejemplo -> PRESENTE
 [OK] 12. Tips 1-6 -> 6/6 COMPLETOS
 [OK] 13. Ejemplo -> 1/1 COMPLETO

 Resultado: 13/13 elementos (100%)

**Sección 10 de arc42 (Quality Requirements):**

.. code-block:: text

 Verificación realizada:
 [OK] 1. Título '10. Quality Requirements' -> PRESENTE
 [OK] 2. Content sección principal -> PRESENTE
 [OK] 3. Motivation sección principal -> PRESENTE
 [OK] 4. Further Information Q42 -> PRESENTE
 [OK] 5. Subsección 10.1 completa -> PRESENTE
 [OK] 6. Content de 10.1 -> PRESENTE
 [OK] 7. Motivation de 10.1 -> PRESENTE
 [OK] 8. Form de 10.1 (tabla/mindmap/tree) -> PRESENTE
 [OK] 9. Subsección 10.2 completa -> PRESENTE
 [OK] 10. Content de 10.2 -> PRESENTE
 ... (8 elementos más)

 Resultado: 18/18 elementos (100%)

**Consecuencias de Incumplimiento:**

[ERROR] **Caso real - Sección 07 (versión inicial):**

.. code-block:: text

 Problema:
 - 6 secciones OMITIDAS por no leer archivo completo
 - Solo se tradujeron primeras 50 líneas de 126

 Causa:
 - NO aplicar PASO 0 correctamente
 - NO inventario exhaustivo previo

 Impacto:
 - Traducción incompleta (8/14 archivos)
 - Pérdida de contenido crítico
 - Re-trabajo necesario

 Solución:
 - Aplicar PASO 0: Leer COMPLETO antes de traducir
 - Crear checklist exhaustivo
 - Verificar 100% elementos

----

Criterio 2: Precisión Técnica (100%)
-------------------------------------

**Definición:**
 La terminología técnica y los conceptos deben traducirse con **precisión absoluta**.

**Sub-criterios:**

1. **Terminología Consistente**

 .. list-table::
 :header-rows: 1
 :widths: 30 35 35

 * - **Aspecto**
   - **Correcto**
   - **Incorrecto**
 * - Mismo término siempre igual
   - "Stakeholder" en todo el doc
   - "Stakeholder" / "Interesado" mezclados
 * - Términos técnicos conservados
   - "API", "Microservicio", "ATAM"
   - "IPA", "Micro-servicio", "MTAA"
 * - Traducciones normativas
   - "Building Block" -> "Bloque de Construcción"
   - "Building Block" -> "Módulo" / "Componente"

2. **Conceptos Traducidos Correctamente**

 **Ejemplos de traducciones precisas en arc42:**

 .. code-block:: text

 [OK] CORRECTO:
 - Quality Attribute -> Atributo de Calidad
 - Technical Debt -> Deuda Técnica
 - Deployment View -> Vista de Despliegue
 - Runtime View -> Vista de Tiempo de Ejecución
 - Cross-cutting Concern -> Concepto Transversal

 [ERROR] INCORRECTO (evitar):
 - Quality Attribute -> "Característica de Calidad"
 - Technical Debt -> "Deuda Tecnológica"
 - Deployment View -> "Vista de Implementación"
 - Runtime View -> "Vista de Ejecución"

3. **Referencias Cruzadas Funcionales**

 .. code-block:: text

 [OK] Verificar que links internos funcionen:

 Original: "See section 5.1"
 Traducido: "Ver :ref:`seccion_5_1`"
 Verificación: [ ] Link funciona en Sphinx

**Casos Reales de Precisión:**

**Terminología Conservada (arc42):**

.. code-block:: text

 Términos CONSERVADOS (no traducidos):

 [OK] Stakeholders -> Stakeholders
 [OK] Product Owner -> Product Owner
 [OK] Scrum Master -> Scrum Master
 [OK] ATAM -> ATAM
 [OK] Circuit Breaker -> Circuit Breaker
 [OK] API -> API
 [OK] REST -> REST
 [OK] UML -> UML

 Razón: Términos técnicos establecidos internacionalmente

**Terminología Traducida (arc42):**

.. code-block:: text

 Términos TRADUCIDOS:

 [OK] Building Block -> Bloque de Construcción
 [OK] Quality Requirements -> Requisitos de Calidad
 [OK] Risk -> Riesgo
 [OK] Technical Debt -> Deuda Técnica
 [OK] Glossary -> Glosario
 [OK] Constraint -> Restricción
 [OK] Deployment -> Despliegue

 Razón: Conceptos generales con traducción estándar

----

Criterio 3: Enriquecimiento Apropiado
--------------------------------------

**Definición:**
 El enriquecimiento debe ser **proporcional a la complejidad** del original y **agregar valor real**.

**Matriz de Enriquecimiento Estándar:**

.. list-table::
 :header-rows: 1
 :widths: 20 20 20 40

 * - **Tamaño Original**
   - **Enriquecimiento**
   - **Rango**
   - **Justificación**
 * - < 20 líneas
   - +300% a +1000%
   - Alto
   - Tips breves requieren contexto y ejemplos
 * - 20-50 líneas
   - +100% a +300%
   - Medio-Alto
   - Secciones cortas necesitan expansión
 * - 50-100 líneas
   - +80% a +150%
   - Medio
   - Balance entre fidelidad y claridad
 * - > 100 líneas
   - +50% a +100%
   - Bajo-Medio
   - Secciones extensas ya completas

**Evidencia Empírica de arc42:**

**Caso 1: Tips de Glosario (originales muy breves)**

.. code-block:: text

 Tip 12-1: "Tomarse el glosario en serio"
 - Original: 12 líneas
 - Traducido: 140 líneas
 - Enriquecimiento: +1067%

 Agregado:
 [OK] Tabla comparativa (con/sin glosario)
 [OK] Ejemplos de problemas reales
 [OK] Casos de uso (3 escenarios)
 [OK] Cómo tomarse en serio (4 pasos)
 [OK] Métricas de éxito

 Justificación: Original demasiado breve, necesita ser accionable

**Caso 2: Sección 12 (archivo principal corto)**

.. code-block:: text

 section-12.md: "Glossary"
 - Original: 44 líneas
 - Traducido: 164 líneas
 - Enriquecimiento: +273%

 Agregado:
 [OK] Tip inicial contextual
 [OK] Tabla multi-idioma adicional
 [OK] Relación con otras secciones
 [OK] Mejores prácticas

 Justificación: Sección breve necesita contexto adicional

**Caso 3: Sección 10 (archivo principal extenso)**

.. code-block:: text

 section-10.md: "Quality Requirements"
 - Original: 123 líneas
 - Traducido: 222 líneas
 - Enriquecimiento: +80%

 Agregado:
 [OK] Aclaraciones en conceptos complejos
 [OK] Formato mejorado de tablas
 [OK] Ejemplos inline selectivos

 Justificación: Original ya extenso, enriquecimiento moderado

**Promedio Global arc42:**

.. code-block:: text

 Sección 10: +207% promedio
 Sección 11: +616% promedio
 Sección 12: +771% promedio

 Observación: A menor tamaño original, mayor enriquecimiento

**Qué NO es Enriquecimiento Apropiado:**

[ERROR] **Evitar:**

.. code-block:: text

 [ERROR] Divagaciones sin propósito
 [ERROR] Repetir conceptos ya claros
 [ERROR] Agregar información no relacionada
 [ERROR] Crear subsecciones innecesarias
 [ERROR] Duplicar contenido existente
 [ERROR] Explicar obviedades

[OK] **Preferir:**

.. code-block:: text

 [OK] Ejemplos prácticos concretos
 [OK] Tablas comparativas útiles
 [OK] Checklists accionables
 [OK] Casos de uso reales
 [OK] Contexto que facilita comprensión
 [OK] Aclaraciones de puntos ambiguos

----

Criterio 4: Formato y Compilación (100%)
-----------------------------------------

**Definición:**
 El documento debe compilar correctamente en Sphinx y seguir estándares RST.

**Sub-criterios:**

1. **Compilación Exitosa**

 .. code-block:: bash

 make clean && make html

 Resultado esperado:
 [OK] build succeeded
 [OK] HTML generado en build/html/

2. **Warnings Permitidos**

 .. code-block:: text

 [OK] ACEPTABLES (no bloquean):
 - Referencias a secciones no traducidas aún
 - Lexer de Pygments no conocido (ej: PlantUML)
 - Enlaces externos no verificados

 [ERROR] INACEPTABLES (deben corregirse):
 - Errores de sintaxis RST
 - Referencias internas rotas
 - Archivos no encontrados
 - Imágenes faltantes

3. **Formato RST Correcto**

 **Estándares de formato:**

 .. code-block:: rst

 [OK] Títulos con líneas de igual longitud:

 ==================
 Título de Sección
 ==================

 [ERROR] NO hacer:

 ==================
 Título
 ==================

 .. code-block:: rst

 [OK] Listas con espaciado correcto:

 - Item 1
 - Item 2

 Explicación del item 2
 con múltiples líneas

 - Item 3

 .. code-block:: rst

 [OK] Código con directivas apropiadas:

 .. code-block:: python

 def funcion():
 return True

**Caso Real de Compilación Exitosa:**

.. code-block:: text

 Proyecto arc42 completo:
 - 12 secciones
 - 196 archivos .rst
 - ~582 KB

 Compilación:
 [OK] make html -> EXITOSA
 [OK] 1693 warnings (solo referencias externas)
 [OK] 0 errores
 [OK] HTML generado correctamente

 Tiempo de compilación: ~30 segundos

----

Criterio 5: Verificación Sistemática (100%)
--------------------------------------------

**Definición:**
 Aplicar **checklist de verificación** contra el original antes de considerar completa la traducción.

**Proceso de Verificación Estándar:**

**PASO 1: Inventario Pre-traducción**

.. code-block:: text

 [ ] Leer archivo principal COMPLETO
 [ ] Identificar TODOS los archivos asociados
 [ ] Crear lista exhaustiva (tips, ejemplos, subsecciones)
 [ ] Estimar tamaño total

**PASO 2: Checklist Durante Traducción**

.. code-block:: text

 [ ] Traducir TODO el contenido (0% omitido)
 [ ] Mantener estructura del original
 [ ] Aplicar enriquecimiento apropiado
 [ ] Crear toctrees completos
 [ ] Referencias cruzadas funcionales

**PASO 3: Verificación Post-traducción**

.. code-block:: text

 [ ] Ejecutar script de verificación
 [ ] Comprobar todos los elementos del checklist
 [ ] Verificar compilación Sphinx
 [ ] Revisar warnings
 [ ] Leer salida HTML generada

**PASO 4: Documentación Final**

.. code-block:: text

 [ ] Crear checkpoint con métricas
 [ ] Documentar archivos traducidos
 [ ] Listar referencias pendientes
 [ ] Calcular enriquecimiento aplicado

**Herramienta de Verificación:**

**Script de verificación automatizado:**

.. code-block:: bash

 #!/bin/bash
 # verificar_traduccion.sh

 ORIGINAL="original/section-XX.md"
 TRADUCIDO="traduccion/seccion_XX.rst"

 echo "Verificando traducción..."

 # Verificar elementos críticos
 grep -q "Título" "$TRADUCIDO" && echo "[OK] Título" || echo "[ERROR] Título"
 grep -q "Content" "$TRADUCIDO" && echo "[OK] Content" || echo "[ERROR] Content"
 grep -q "Motivation" "$TRADUCIDO" && echo "[OK] Motivation" || echo "[ERROR] Motivation"

 # Contar archivos
 ESPERADOS=$(find original/ -name "*-XX-*" | wc -l)
 TRADUCIDOS=$(find traduccion/ -name "*.rst" | wc -l)

 echo "Archivos: $TRADUCIDOS/$ESPERADOS"

**Ejemplo Real de Verificación (Sección 12):**

.. code-block:: bash

 $ bash verificacion_seccion_12.sh

 +======================================================+
 | VERIFICACIÓN SISTEMÁTICA - SECCIÓN 12 |
 +======================================================+

 1. [OK] Título '12. Glossary'
 [OK] PRESENTE

 2. [OK] Content (líneas 12-15 del original)
 [OK] PRESENTE

 3. [OK] Content - multi-language (línea 15)
 [OK] PRESENTE

 ...

 13. [OK] Ejemplo traducido
 [OK] PRESENTE



 RESUMEN FINAL:
 Total archivos traducidos: 8/8
 [OK] TODOS LOS ARCHIVOS COMPLETADOS

 Resultado: 13/13 elementos [OK] PRESENTE (100%)

----

Matriz de Evaluación de Calidad
================================

**Evaluación Global:**

.. list-table::
 :header-rows: 1
 :widths: 30 15 15 40

 * - **Criterio**
   - **Peso**
   - **Umbral**
   - **Verificación**
 * - Completitud
   - 30%
   - 100%
   - Checklist contra original
 * - Precisión Técnica
   - 25%
   - 100%
   - Revisión terminológica
 * - Enriquecimiento
   - 20%
   - Apropiado
   - Rango según tamaño
 * - Formato/Compilación
   - 15%
   - 100%
   - make html exitoso
 * - Verificación
   - 10%
   - 100%
   - Script + checklist

**Cálculo de Calidad Total:**

.. code-block:: text

 Calidad Total = (Completitud × 0.30) +
 (Precisión × 0.25) +
 (Enriquecimiento × 0.20) +
 (Formato × 0.15) +
 (Verificación × 0.10)

 Umbral de Aprobación: ≥ 95%

 Ejemplo arc42 Sección 12:
 = (100% × 0.30) + (100% × 0.25) + (100% × 0.20) +
 (100% × 0.15) + (100% × 0.10)
 = 30 + 25 + 20 + 15 + 10
 = 100% [OK] APROBADA

----

Casos de Uso de los Criterios
==============================

Caso 1: Evaluación de Traducción Nueva
---------------------------------------

**Escenario:**
 Acabas de terminar de traducir una nueva sección.

**Aplicación de criterios:**

.. code-block:: text

 PASO 1: Completitud
 [ ] Checklist: ¿Todos los elementos presentes?
 [ ] Script: Ejecutar verificación automatizada
 -> Si 100% -> Continuar
 -> Si <100% -> CORREGIR omisiones

 PASO 2: Precisión Técnica
 [ ] Revisar terminología contra glosario
 [ ] Verificar conceptos técnicos
 -> Si preciso -> Continuar
 -> Si impreciso -> CORREGIR términos

 PASO 3: Enriquecimiento
 [ ] Calcular % enriquecimiento
 [ ] Verificar contra matriz estándar
 -> Si en rango -> Continuar
 -> Si fuera de rango -> AJUSTAR

 PASO 4: Formato
 [ ] make html
 -> Si compila -> Continuar
 -> Si errores -> CORREGIR sintaxis

 PASO 5: Checkpoint
 [ ] Documentar métricas
 [ ] Crear checkpoint final
 -> Traducción COMPLETA

Caso 2: Revisión de Traducción Existente
-----------------------------------------

**Escenario:**
 Revisar calidad de traducción hecha hace tiempo.

**Aplicación de criterios:**

.. code-block:: text

 AUDITORÍA:

 1. Ejecutar script de verificación
 2. Comparar contra original línea por línea
 3. Revisar warnings de Sphinx
 4. Calcular métricas actuales
 5. Identificar gaps
 6. Priorizar correcciones
 7. Re-traducir si necesario

Caso 3: Traducción Colaborativa
--------------------------------

**Escenario:**
 Múltiples personas traducen secciones diferentes.

**Aplicación de criterios:**

.. code-block:: text

 ESTÁNDARES COMUNES:

 [OK] Todos aplican mismos criterios
 [OK] Mismo umbral de aprobación (≥95%)
 [OK] Misma matriz de enriquecimiento
 [OK] Misma terminología (glosario compartido)
 [OK] Mismo proceso de verificación

 Resultado: Calidad consistente entre traductores

----

Lecciones Aprendidas de arc42
==============================

**De 196 archivos traducidos:**

1. **PASO 0 es crítico**

 .. code-block:: text

 [ERROR] Sección 07 (inicial): NO aplicar PASO 0 -> 6 omisiones
 [OK] Secciones 10-12: SÍ aplicar PASO 0 -> 0 omisiones

 Lección: Siempre leer COMPLETO antes de traducir

2. **Verificación sistemática previene errores**

 .. code-block:: text

 [OK] Sección 12: Script 13 checks -> 13/13 [OK]
 [OK] Sección 11: Script 13 checks -> 13/13 [OK]
 [OK] Sección 10: Script 18 checks -> 18/18 [OK]

 Lección: Automatizar verificación

3. **Enriquecimiento debe ser proporcional**

 .. code-block:: text

 [OK] Tips breves (10-25 líneas): +771% promedio
 [OK] Secciones medias (40-50 líneas): +273%
 [OK] Secciones extensas (100+ líneas): +80%

 Lección: Ajustar enriquecimiento al tamaño

4. **Terminología consistente es clave**

 .. code-block:: text

 [OK] arc42: Mismos términos en 196 archivos

 Stakeholder (conservado) - 0 variaciones
 Building Block -> Bloque de Construcción - 0 variaciones

 Lección: Crear glosario y seguirlo religiosamente

5. **Compilación frecuente detecta problemas temprano**

 .. code-block:: text

 [OK] Compilar después de cada lote

 Detecta:
 - Errores de sintaxis
 - Referencias rotas
 - Imágenes faltantes

 Lección: No esperar al final para compilar

----

Resumen Ejecutivo
=================

**Los 5 Criterios de Calidad ADT:**

1. [OK] **Completitud (100%)** - Todo el contenido presente
2. [OK] **Precisión Técnica (100%)** - Terminología correcta
3. [OK] **Enriquecimiento Apropiado** - Según tamaño original
4. [OK] **Formato y Compilación (100%)** - Sphinx exitoso
5. [OK] **Verificación Sistemática (100%)** - Checklist completo

**Umbral de Aprobación:** ≥ 95%

**Evidencia:** 196 archivos de arc42 cumplen 100% los criterios

**Próximos Pasos:**

- Consultar: :doc:`metricas_traduccion` para rangos de enriquecimiento
- Usar: :doc:`checklist_revision` para verificación
- Ver: :doc:`../casos_practicos/casos_exito/exito_01_arc42_completo` para ejemplos

----

.. seealso::
 * :doc:`metricas_traduccion` - Métricas cuantitativas detalladas
 * :doc:`checklist_revision` - Lista de verificación paso a paso
 * :doc:`../../02_procedimientos/workflow_general` - Workflow v1.7.2
 * :doc:`../../06_casos_practicos/antes_despues/caso_01_seccion_breve` - Ejemplo práctico

.. note::
 Este documento está basado en experiencia real y evoluciona con cada proyecto de traducción. Última actualización basada en arc42 completado el 2026-01-28.
