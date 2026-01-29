.. _metricas_traduccion:

===============================================
Métricas de Traducción ADT
===============================================

:Sección: 03_estandares/calidad
:Base: Análisis cuantitativo de arc42 (196 archivos)
:Aplicabilidad: Evaluación de traducciones
:Última actualización: 2026-01-28

.. contents:: Contenido
 :depth: 3
 :local:

----

Introducción
============

Este documento define las **métricas cuantitativas** para evaluar traducciones en el proyecto ADT.

**Base empírica:**
 Análisis estadístico de 12 secciones de arc42 traducidas (196 archivos, 6 secciones con checkpoints documentados).

**Propósito:**
 Proveer rangos numéricos objetivos para evaluar calidad y consistencia de traducciones.

----

Métrica 1: Enriquecimiento por Tamaño
======================================

Definición
----------

**Enriquecimiento:**
 Porcentaje de expansión del contenido traducido respecto al original.

**Fórmula:**

.. code-block:: text

 Enriquecimiento% = ((Líneas_Traducido - Líneas_Original) / Líneas_Original) × 100

**Ejemplo:**

.. code-block:: text

 Original: 44 líneas
 Traducido: 164 líneas

 Enriquecimiento = ((164 - 44) / 44) × 100
 = (120 / 44) × 100
 = 273%

Rangos Estándar por Tamaño
---------------------------

**Basado en arc42:**

.. list-table::
 :header-rows: 1
 :widths: 20 20 20 40

 * - **Tamaño Original**
 - **Rango Óptimo**
 - **Promedio arc42**
 - **Ejemplos Reales**
 * - **< 20 líneas**
 - +300% a +1000%
 - +771%
 - Tips 12-1 a 12-6 (11-26 líneas)
 * - **20-50 líneas**
 - +100% a +300%
 - +273%
 - section-12.md (44 líneas)
 * - **50-100 líneas**
 - +80% a +150%
 - +95%
 - section-11.md (72 líneas)
 * - **> 100 líneas**
 - +50% a +100%
 - +80%
 - section-10.md (123 líneas)

Datos Detallados por Sección de arc42
--------------------------------------

**Sección 10: Quality Requirements (123 líneas originales)**

.. list-table::
 :header-rows: 1
 :widths: 40 20 20 20

 * - **Archivo**
 - **Original**
 - **Traducido**
 - **Enriquecimiento**
 * - section-10.md (principal)
 - 123 líneas
 - 222 líneas
 - +80%
 * - quality_tip_1.rst
 - 15 líneas
 - 48 líneas
 - +220%
 * - quality_tip_2.rst
 - 37 líneas
 - 88 líneas
 - +138%
 * - quality_tip_3.rst
 - 18 líneas
 - 56 líneas
 - +211%
 * - quality_tip_4.rst
 - 28 líneas
 - 103 líneas
 - +268%
 * - quality_tip_5.rst
 - 21 líneas
 - 68 líneas
 - +224%
 * - quality_tip_6.rst
 - 26 líneas
 - 77 líneas
 - +196%
 * - quality_tip_7.rst
 - 32 líneas
 - 94 líneas
 - +194%
 * - quality_tip_8.rst
 - 42 líneas
 - 120 líneas
 - +186%

**Promedio Sección 10:** +207%

**Sección 11: Risks and Technical Debt (72 líneas originales)**

.. list-table::
 :header-rows: 1
 :widths: 40 20 20 20

 * - **Archivo**
 - **Original**
 - **Traducido**
 - **Enriquecimiento**
 * - section-11.md (principal)
 - 34 líneas
 - 154 líneas
 - +353%
 * - risks_tip_1.rst
 - 15 líneas
 - 79 líneas
 - +427%
 * - risks_tip_2.rst
 - 14 líneas
 - 117 líneas
 - +736%
 * - risks_tip_3.rst
 - 11 líneas
 - 121 líneas
 - +1000%
 * - risks_tip_4.rst
 - 14 líneas
 - 127 líneas
 - +807%
 * - risks_tip_5.rst
 - 15 líneas
 - 109 líneas
 - +627%
 * - risks_tip_6.rst
 - 11 líneas
 - 122 líneas
 - +1009%

**Promedio Sección 11:** +616%

**Sección 12: Glossary (44 líneas originales)**

.. list-table::
 :header-rows: 1
 :widths: 40 20 20 20

 * - **Archivo**
 - **Original**
 - **Traducido**
 - **Enriquecimiento**
 * - section-12.md (principal)
 - 44 líneas
 - 164 líneas
 - +273%
 * - glossary_tip_1.rst
 - 12 líneas
 - 140 líneas
 - +1067%
 * - glossary_tip_2.rst
 - 26 líneas
 - 168 líneas
 - +546%
 * - glossary_tip_3.rst
 - 18 líneas
 - 175 líneas
 - +872%
 * - glossary_tip_4.rst
 - 26 líneas
 - 165 líneas
 - +535%
 * - glossary_tip_5.rst
 - 17 líneas
 - 220 líneas
 - +1194%
 * - glossary_tip_6.rst
 - 11 líneas
 - 162 líneas
 - +1373%

**Promedio Sección 12:** +771%

Análisis de Tendencias
----------------------

**Observación clave:**

.. code-block:: text

 Correlación inversa entre tamaño original y enriquecimiento:

 A menor tamaño original -> Mayor enriquecimiento

 Evidencia:
 - Tips 11-26 líneas: +771% a +1373%
 - Secciones 40-50 líneas: +273% a +353%
 - Secciones 100+ líneas: +80%

**Justificación:**

.. code-block:: text

 Tips muy breves (10-20 líneas):
 - Usualmente presentan solo idea básica
 - Necesitan ejemplos para ser accionables
 - Requieren contexto adicional
 - Benefician de checklists y tablas

 Secciones extensas (>100 líneas):
 - Ya contienen ejemplos y contexto
 - Enriquecimiento es mayormente formato
 - Agregar mucho contenido puede diluir mensaje

----

Métrica 2: Completitud
======================

Definición
----------

**Completitud:**
 Porcentaje de elementos del original presentes en la traducción.

**Fórmula:**

.. code-block:: text

 Completitud% = (Elementos_Traducidos / Elementos_Totales) × 100

**Umbral de Aprobación:** 100% (no se permite omitir contenido)

Mediciones Reales de arc42
---------------------------

**Sección 12: Glossary**

.. code-block:: text

 Elementos verificados: 13
 Elementos presentes: 13
 Completitud: 13/13 = 100% [OK]

**Sección 11: Risks and Technical Debt**

.. code-block:: text

 Elementos verificados: 13
 Elementos presentes: 13
 Completitud: 13/13 = 100% [OK]

**Sección 10: Quality Requirements**

.. code-block:: text

 Elementos verificados: 18
 Elementos presentes: 18
 Completitud: 18/18 = 100% [OK]

**Sección 07: Deployment View (versión corregida)**

.. code-block:: text

 Versión inicial: 8/14 = 57% [ERROR] (6 omisiones)
 Versión corregida: 14/14 = 100% [OK]

**Resultado Global arc42:**

.. code-block:: text

 Secciones con 100% completitud: 12/12 [OK]

 Lección: PASO 0 es crítico para lograr 100%

Checklist de Elementos Típicos
-------------------------------

**Para archivo principal de sección:**

.. code-block:: text

 [ ] Título de sección
 [ ] Content (descripción)
 [ ] Motivation (motivación)
 [ ] Form (forma/estructura)
 [ ] Todas las subsecciones (X.1, X.2, etc.)
 [ ] Todas las tablas
 [ ] Todas las imágenes referenciadas
 [ ] Plantilla vacía (si aplica)
 [ ] Further information
 [ ] Referencias externas
 [ ] Toctree con todos los tips
 [ ] Toctree con todos los ejemplos

**Para tips:**

.. code-block:: text

 [ ] Título del tip
 [ ] Todo el contenido textual
 [ ] Ejemplos de código (si hay)
 [ ] Imágenes (si hay)
 [ ] Listas (todas)
 [ ] Énfasis (negrita, cursiva)
 [ ] Referencias cruzadas

----

Métrica 3: Tamaño Total
=======================

Definición
----------

**Tamaño Total:**
 Volumen total del contenido traducido en KB.

Datos por Sección de arc42
---------------------------

.. list-table::
 :header-rows: 1
 :widths: 15 15 15 15 40

 * - **Sección**
 - **Archivos**
 - **Tamaño**
 - **Promedio**
 - **Observaciones**
 * - 01
 - 32
 - 78 KB
 - 2.4 KB/archivo
 - Sección compleja, muchos archivos
 * - 02
 - 8
 - 19 KB
 - 2.4 KB/archivo
 - Sección corta
 * - 03
 - 28
 - 61 KB
 - 2.2 KB/archivo
 - Contexto y alcance
 * - 04
 - 9
 - 25 KB
 - 2.8 KB/archivo
 - Estrategia de solución
 * - 05
 - 36
 - 103 KB
 - 2.9 KB/archivo
 - Sección más grande
 * - 06
 - 15
 - 44 KB
 - 2.9 KB/archivo
 - Vista de runtime
 * - 07
 - 14
 - 38 KB
 - 2.7 KB/archivo
 - Vista de deployment
 * - 08
 - 12
 - 24 KB
 - 2.0 KB/archivo
 - Conceptos transversales
 * - 09
 - 14
 - 25 KB
 - 1.8 KB/archivo
 - Decisiones arquitectónicas
 * - 10
 - 11
 - 48 KB
 - 4.4 KB/archivo
 - Tips muy enriquecidos
 * - 11
 - 9
 - 55 KB
 - 6.1 KB/archivo
 - Máximo enriquecimiento
 * - 12
 - 8
 - 62 KB
 - 7.8 KB/archivo
 - Tips extremadamente enriquecidos

**Total arc42:** 196 archivos, ~582 KB, promedio 3.0 KB/archivo

Distribución de Tamaños
-----------------------

.. code-block:: text

 Archivos pequeños (< 2 KB): 42% (principalmente tips breves)
 Archivos medianos (2-5 KB): 38% (secciones principales)
 Archivos grandes (> 5 KB): 20% (tips muy enriquecidos)

----

Métrica 4: Velocidad de Traducción
===================================

Definición
----------

**Velocidad:**
 Archivos traducidos por unidad de tiempo.

Datos Empíricos de arc42
-------------------------

**Por Sección:**

.. list-table::
 :header-rows: 1
 :widths: 20 20 20 20 20

 * - **Sección**
 - **Archivos**
 - **Tiempo**
 - **Velocidad**
 - **Complejidad**
 * - 10
 - 11
 - ~3 horas
 - 3.7 arch/hora
 - Media
 * - 11
 - 9
 - ~2.5 horas
 - 3.6 arch/hora
 - Media-Alta
 * - 12
 - 8
 - ~3 horas
 - 2.7 arch/hora
 - Baja (tips muy enriquecidos)

**Promedio:** ~3.3 archivos/hora

**Factores que Afectan Velocidad:**

.. code-block:: text

 Velocidad MAYOR (> 4 arch/hora):
 - Archivos cortos (<20 líneas)
 - Terminología ya establecida
 - Formato simple
 - Poco enriquecimiento necesario

 Velocidad MENOR (< 2 arch/hora):
 - Archivos largos (>100 líneas)
 - Terminología compleja nueva
 - Muchas tablas/diagramas
 - Alto enriquecimiento requerido

----

Métrica 5: Calidad de Compilación
==================================

Definición
----------

**Calidad de Compilación:**
 Relación entre warnings y tamaño del proyecto.

Datos de arc42 Completo
-----------------------

.. code-block:: text

 Proyecto: arc42 (12 secciones, 196 archivos)

 Compilación: make clean && make html

 Resultado:
 - Build: succeeded [OK]
 - Errores: 0
 - Warnings: 1693
 - HTML generado: build/html/

 Ratio: 1693 warnings / 196 archivos = 8.6 warnings/archivo

**Tipos de Warnings:**

.. code-block:: text

 Distribución de warnings:

 60% - Referencias a secciones no traducidas
 (ej: tips apuntan a secciones futuras)

 20% - Pygments lexer no conocido
 (ej: PlantUML, ATL no instalados)

 15% - Referencias externas no verificadas
 (ej: links a sitios web)

 5% - Otros (documentos duplicados, etc.)

**Warnings Críticos vs No-Críticos:**

.. code-block:: text

 [OK] NO-CRÍTICOS (no bloquean, 95%):
 - Referencias a contenido futuro
 - Lexers opcionales
 - Links externos

 [ERROR] CRÍTICOS (deben corregirse, 5%):
 - Sintaxis RST incorrecta
 - Referencias internas rotas
 - Imágenes faltantes

 arc42: 0 warnings críticos [OK]

----

Métrica 6: Consistencia Terminológica
======================================

Definición
----------

**Consistencia:**
 Porcentaje de términos técnicos usados consistentemente.

Medición en arc42
-----------------

**Términos Técnicos Clave:**

.. list-table::
 :header-rows: 1
 :widths: 30 30 20 20

 * - **Término Original**
 - **Traducción**
 - **Variaciones**
 - **Consistencia**
 * - Stakeholder
 - Stakeholder
 - 0
 - 100%
 * - Building Block
 - Bloque de Construcción
 - 0
 - 100%
 * - Quality Requirement
 - Requisito de Calidad
 - 0
 - 100%
 * - Technical Debt
 - Deuda Técnica
 - 0
 - 100%
 * - Deployment
 - Despliegue
 - 0
 - 100%
 * - Runtime
 - Runtime
 - 0
 - 100%
 * - API
 - API
 - 0
 - 100%

**Resultado:** 100% consistencia en todos los términos clave [OK]

**Método de Lograr Consistencia:**

.. code-block:: text

 1. Crear glosario de términos al inicio
 2. Usar glosario como referencia obligatoria
 3. Búsqueda global antes de cambiar término
 4. Revisar consistencia en checkpoints
 5. Herramientas: grep, búsqueda en IDE

----

Métricas Comparativas
=====================

Comparación entre Secciones
----------------------------

**Enriquecimiento Promedio:**

.. code-block:: text

 Sección 12 (Glossary): +771% Más enriquecida
 Sección 11 (Risks): +616%
 Sección 10 (Quality): +207%
 ...

 Tendencia: Secciones recientes más enriquecidas

**Razón de la Tendencia:**

.. code-block:: text

 - Más experiencia con Workflow v1.7.2
 - Mejor entendimiento de enriquecimiento apropiado
 - Tips más breves en secciones finales
 - Lecciones aprendidas aplicadas

Comparación con Estándares de Industria
----------------------------------------

**Traducción Técnica Estándar:**

.. code-block:: text

 Industria (traducción literal):
 - Enriquecimiento: +5% a +20%
 - Completitud: 98-99%
 - Velocidad: 5-10 páginas/hora

 ADT (traducción con enriquecimiento):
 - Enriquecimiento: +200% a +800%
 - Completitud: 100%
 - Velocidad: 3-4 archivos/hora

 Diferencia:
 ADT agrega valor sustancial vs traducción literal

----

Uso de las Métricas
===================

Caso 1: Planificación de Proyecto
----------------------------------

**Estimar tiempo necesario:**

.. code-block:: text

 Proyecto: Traducir documentación de 50 archivos

 Distribución estimada:
 - 20 archivos < 20 líneas (tips)
 - 20 archivos 20-50 líneas (secciones)
 - 10 archivos > 100 líneas (principales)

 Tiempo estimado:
 - Tips: 20 archivos ÷ 2.7 arch/hora = 7.4 horas
 - Secciones: 20 archivos ÷ 3.7 arch/hora = 5.4 horas
 - Principales: 10 archivos ÷ 2.5 arch/hora = 4 horas

 Total: ~17 horas de traducción pura
 + 30% para verificación y correcciones
 = ~22 horas totales

Caso 2: Evaluación de Calidad
------------------------------

**Evaluar traducción completada:**

.. code-block:: text

 Traducción recibida:
 - 15 archivos
 - Original promedio: 30 líneas
 - Traducido promedio: 60 líneas
 - Enriquecimiento: +100%

 Evaluación:
 [OK] Dentro de rango (20-50 líneas: +100% a +300%)
 [OK] Apropiado para tamaño

 Completitud:
 [ ] Verificar 100% elementos presentes
 [ ] Ejecutar checklist

 Compilación:
 [ ] make html -> ¿éxito?
 [ ] Revisar warnings

Caso 3: Mejora Continua
-----------------------

**Comparar con proyectos anteriores:**

.. code-block:: text

 Proyecto A:
 - Enriquecimiento: +150%
 - Completitud: 100%
 - Warnings: 5/archivo

 Proyecto B:
 - Enriquecimiento: +300%
 - Completitud: 100%
 - Warnings: 3/archivo

 Observación:
 Proyecto B mejora en enriquecimiento y warnings

 Acción:
 Analizar qué cambió para replicar en futuro

----

Resumen de Métricas Clave
==========================

**Tabla de Referencia Rápida:**

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Métrica**
 - **Rango Objetivo**
 - **arc42 Real**
 - **Umbral**
 * - Enriquecimiento (<20 líneas)
 - +300% a +1000%
 - +771%
 - Variable
 * - Enriquecimiento (20-50 líneas)
 - +100% a +300%
 - +273%
 - Variable
 * - Enriquecimiento (>100 líneas)
 - +50% a +100%
 - +80%
 - Variable
 * - Completitud
 - 100%
 - 100%
 - Obligatorio
 * - Velocidad
 - 3-4 arch/hora
 - 3.3 arch/hora
 - Referencia
 * - Consistencia Terminológica
 - 100%
 - 100%
 - Obligatorio
 * - Warnings Críticos
 - 0
 - 0
 - Obligatorio

----

.. seealso::
 * :doc:`criterios_calidad` - Criterios cualitativos de traducción
 * :doc:`checklist_revision` - Lista de verificación
 * :doc:`../../02_procedimientos/workflow_general` - Workflow v1.7.2

.. note::
 Estas métricas están basadas en datos reales de 196 archivos traducidos. Se actualizan con cada proyecto nuevo para refinar los rangos.
