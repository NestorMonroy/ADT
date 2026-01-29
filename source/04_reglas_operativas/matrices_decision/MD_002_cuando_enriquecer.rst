.. _md_cuando_enriquecer:

===============================================
MD-002: Cuándo y Cuánto Enriquecer
===============================================

:Tipo: Matriz de Decisión
:Código: MD-002
:Prioridad: CRÍTICA
:Aplicabilidad: Toda traducción ADT
:Base: 196 archivos de arc42 traducidos

.. contents:: Contenido
 :depth: 3
 :local:

----

Pregunta de Decisión
====================

**Pregunta:**
 ¿Cuánto debo enriquecer este contenido que estoy traduciendo?

**Importancia:**
 Esta es la decisión más frecuente durante traducción. Hacerlo mal resulta en:

 [ERROR] **Muy poco enriquecimiento** -> Traducción literal sin valor agregado
 [ERROR] **Demasiado enriquecimiento** -> Divagación, pérdida de foco

**Objetivo:**
 Proveer guía objetiva basada en datos reales de 196 archivos.

----

Matriz de Decisión Principal
=============================

**Basado en tamaño del contenido original:**

.. list-table::
 :header-rows: 1
 :widths: 15 20 15 20 30

 * - **Tamaño**
 - **Rango Óptimo**
 - **Promedio arc42**
 - **Tipo Contenido**
 - **Ejemplo Real**
 * - **< 20 líneas**
 - +300% a +1000%
 - +771%
 - Tips breves
 - Tips 12-1 a 12-6
 * - **20-50 líneas**
 - +100% a +300%
 - +273%
 - Secciones cortas
 - section-12.md
 * - **50-100 líneas**
 - +80% a +150%
 - +95%
 - Secciones medianas
 - section-11.md
 * - **> 100 líneas**
 - +50% a +100%
 - +80%
 - Secciones extensas
 - section-10.md

**Fórmula de Enriquecimiento:**

.. code-block:: text

 Enriquecimiento% = ((Líneas_Traducido - Líneas_Original) / Líneas_Original) × 100

 Ejemplo:
 Original: 44 líneas
 Traducido: 164 líneas
 Enriquecimiento = ((164 - 44) / 44) × 100 = 273%

----

Decisión por Tamaño: Casos Detallados
======================================

Caso 1: Tips Muy Breves (< 20 líneas)
--------------------------------------

**Características del original:**

.. code-block:: text

 - Tamaño: 10-20 líneas
 - Contenido: Idea básica, consejo breve
 - Estructura: 1-2 párrafos, posiblemente lista
 - Ejemplos: Generalmente NO incluye
 - Profundidad: Superficial

**¿Por qué enriquecer tanto (+300% a +1000%)?**

.. code-block:: text

 Razón 1: ACCIONABILIDAD
 - Original solo presenta idea
 - Necesita ejemplos para ser útil
 - Requiere checklist para aplicar

 Razón 2: CONTEXTO
 - Sin contexto, difícil entender cuándo aplicar
 - Casos de uso ayudan a identificar situaciones

 Razón 3: COMPARACIÓN
 - Tablas comparativas (con/sin aplicar consejo)
 - Ventajas y desventajas

 Razón 4: COMPLETITUD
 - Pasos concretos (1, 2, 3...)
 - Herramientas específicas
 - Métricas de éxito

**Ejemplo Real - Tip 12-1: "Tomarse el glosario en serio"**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **Original (12 líneas)**
 - **Traducido (140 líneas)**
 * - ::

 You should take the glossary
 seriously. Terms must be defined
 and used consistently.

 Having different terms for the
 same concept or using one term
 for different concepts will
 confuse people.

 Therefore: Take care of your
 glossary. Seriously.
 - **Introducción** (contexto)

 **Problema** (tabla comparativa):
 - Con glosario vs sin glosario

 **Regla "Mejor explícito que implícito"**

 **Ejemplos de problemas** (3 casos):
 - Término ambiguo
 - Múltiples sinónimos
 - Homónimos

 **Cómo tomarse en serio** (4 pasos):
 1. Crear glosario desde inicio
 2. Revisión en cada sprint
 3. Asignar responsable
 4. Educar al equipo

 **Métricas de éxito**:
 - % términos documentados
 - Tiempo resolver ambigüedades

 **Herramientas**: Confluence, Notion

**Qué agregar:**

.. code-block:: text

 [OK] SIEMPRE agregar:
 - Ejemplos prácticos concretos (2-3)
 - Checklist accionable
 - Tabla comparativa (antes/después)
 - Casos de uso (cuándo aplicar)
 - Pasos numerados (1, 2, 3...)
 - Herramientas específicas
 - Métricas de éxito

 [ERROR] EVITAR agregar:
 - Teoría excesiva
 - Información no relacionada
 - Divagaciones filosóficas
 - Repetición de conceptos

**Casos Reales de arc42:**

.. code-block:: text

 Tip 12-1: 12 líneas -> 140 líneas (+1067%)
 - Agregado: Tabla, 3 ejemplos, 4 pasos, métricas

 Tip 12-2: 26 líneas -> 168 líneas (+546%)
 - Agregado: Estructura tabla, ejemplo completo, mejores prácticas

 Tip 12-3: 18 líneas -> 175 líneas (+872%)
 - Agregado: Tipos de diagramas, ejemplo completo, PlantUML

 Tip 12-5: 17 líneas -> 220 líneas (+1194%)
 - Agregado: Criterios inclusión, tamaños recomendados, ejemplo

 Tip 12-6: 11 líneas -> 162 líneas (+1373%)
 - Agregado: Responsabilidades, proceso gestión, RACI matrix

**Promedio Tips Sección 12:** +771%

----

Caso 2: Secciones Cortas (20-50 líneas)
----------------------------------------

**Características del original:**

.. code-block:: text

 - Tamaño: 20-50 líneas
 - Contenido: Concepto + descripción básica
 - Estructura: Varios párrafos, 1-2 tablas
 - Ejemplos: Algunos, pero básicos
 - Profundidad: Media

**¿Por qué enriquecer moderadamente (+100% a +300%)?**

.. code-block:: text

 Razón 1: EQUILIBRIO
 - Ya tiene estructura básica
 - Necesita expansión, no creación

 Razón 2: CLARIFICACIÓN
 - Conceptos clave requieren elaboración
 - Ejemplos adicionales ayudan

 Razón 3: NAVEGACIÓN
 - Agregar tip inicial contextual
 - Sección "Relación con otras secciones"

**Ejemplo Real - section-12.md: "Glossary"**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **Original (44 líneas)**
 - **Traducido (164 líneas)**
 * - ::

 # 12. Glossary

 ## Content
 Terms, definitions
 Multi-language translations

 ## Motivation
 Identical understanding
 Avoid synonyms/homonyms

 ## Form
 Simple table
 Term | Definition

 [Example table]

 [Template]

 ## Further Information
 FAQ link
 - **Título y metadata**

 **Introducción** (tip contextual):
 - Por qué glosario es crítico

 **Content** (expandido):
 - Términos de dominio
 - Términos técnicos
 - Traducciones multi-idioma

 **Motivation** (expandido):
 - Entendimiento idéntico
 - Evitar sinónimos
 - Evitar homónimos
 - Cita de Tim Lister

 **Form** (expandido):
 - Tabla simple (ejemplo básico)
 - Tabla multi-idioma (ejemplo)
 - Formato recomendado

 **Plantilla** (incluida)

 **Relación con otras secciones**:
 - Sección 1, 3, 8

 **Toctree** (6 tips + 1 ejemplo)

 **Referencias**:
 - FAQ arc42

 **Nota**: Mejores prácticas

**Qué agregar:**

.. code-block:: text

 [OK] SIEMPRE agregar:
 - Tip inicial contextual
 - Ejemplos adicionales (1-2)
 - Sección "Relación con otras secciones"
 - Mejores prácticas
 - Formato mejorado de tablas

 [WARNING] CONSIDERAR agregar:
 - Tabla comparativa (si ayuda)
 - Subsecciones adicionales (si clarifica)
 - Diagrama (si simplifica)

 [ERROR] EVITAR agregar:
 - Subsecciones innecesarias
 - Duplicación de contenido
 - Información marginal

**Casos Reales de arc42:**

.. code-block:: text

 section-12.md: 44 líneas -> 164 líneas (+273%)
 - Agregado: Tip contextual, ejemplo multi-idioma, relaciones

 section-11.md: 34 líneas -> 154 líneas (+353%)
 - Agregado: Ejemplos, contexto, mejores prácticas

**Promedio Secciones 40-50 líneas:** +273% a +353%

----

Caso 3: Secciones Medianas (50-100 líneas)
-------------------------------------------

**Características del original:**

.. code-block:: text

 - Tamaño: 50-100 líneas
 - Contenido: Concepto + ejemplos + detalles
 - Estructura: Múltiples secciones, tablas
 - Ejemplos: Varios, algunos detallados
 - Profundidad: Media-Alta

**¿Por qué enriquecimiento moderado (+80% a +150%)?**

.. code-block:: text

 Razón 1: BALANCE
 - Original ya bastante completo
 - Enriquecimiento es refinamiento

 Razón 2: FORMATO
 - Mejorar presentación
 - Aclarar estructura

 Razón 3: FIDELIDAD
 - Mantener mensaje del original
 - No diluir con exceso

**Ejemplo Real - section-11.md: "Risks and Technical Debt"**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **Original (72 líneas)**
 - **Traducido (variable por archivo)**
 * - Contenido ya estructurado:

 - Introducción
 - Content
 - Motivation
 - Form
 - Subsecciones 11.1, 11.2
 - Ejemplos
 - Referencias
 - Enriquecimiento por archivo:

 - Principal: +353%
 - Tips: +427% a +1009%
 - Promedio: +616%

 Nota: Tips muy breves explican
 el promedio alto

**Qué agregar:**

.. code-block:: text

 [OK] SIEMPRE agregar:
 - Aclaraciones en puntos ambiguos
 - Formato mejorado
 - Ejemplos inline selectivos

 [WARNING] CONSIDERAR agregar:
 - Nota explicativa (si concepto complejo)
 - Referencia adicional (si relevante)

 [ERROR] EVITAR agregar:
 - Contenido redundante
 - Explicaciones obvias
 - Subsecciones innecesarias

----

Caso 4: Secciones Extensas (> 100 líneas)
------------------------------------------

**Características del original:**

.. code-block:: text

 - Tamaño: > 100 líneas
 - Contenido: Completo, detallado
 - Estructura: Múltiples subsecciones
 - Ejemplos: Varios, detallados
 - Profundidad: Alta

**¿Por qué enriquecimiento bajo (+50% a +100%)?**

.. code-block:: text

 Razón 1: COMPLETITUD ORIGINAL
 - Ya contiene ejemplos
 - Ya contiene contexto
 - Ya detallado

 Razón 2: RIESGO DE DILUCIÓN
 - Agregar mucho puede confundir
 - Mensaje puede perderse

 Razón 3: RESPETO AL ORIGINAL
 - Autor ya dedicó espacio
 - Estructura bien pensada

**Ejemplo Real - section-10.md: "Quality Requirements"**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **Original (123 líneas)**
 - **Traducido (222 líneas)**
 * - Contenido extenso:

 - Introducción (16 líneas)
 - Content
 - Motivation
 - Further Information
 - 10.1 completo (23 líneas)
 * Content
 * Motivation
 * Form
 - 10.2 completo (50 líneas)
 * Content
 * Forma corta
 * Forma larga
 * Referencias
 - Enriquecimiento: +80%

 Agregado:
 - Formato mejorado de tablas
 - Aclaraciones puntuales
 - Toctrees completos
 - Relaciones con otras secciones

 NO agregado:
 - Ejemplos extensos (ya hay)
 - Subsecciones nuevas
 - Contenido redundante

**Qué agregar:**

.. code-block:: text

 [OK] SIEMPRE agregar:
 - Formato RST apropiado
 - Toctrees completos
 - Metadata y referencias

 [WARNING] CONSIDERAR agregar:
 - Aclaración puntual (si concepto muy complejo)
 - Nota al pie (si información crítica)

 [ERROR] EVITAR agregar:
 - Ejemplos extensos (ya hay)
 - Explicaciones redundantes
 - Contenido marginal

**Casos Reales de arc42:**

.. code-block:: text

 section-10.md: 123 líneas -> 222 líneas (+80%)
 - Agregado: Formato, toctrees, aclaraciones selectivas

----

Árbol de Decisión Visual
=========================

**Proceso paso a paso:**

.. code-block:: text

 1. ¿Cuántas líneas tiene el original?
 +- < 20 líneas
 | +- Objetivo: +300% a +1000%
 | +- Agregar ejemplos prácticos [OK]
 | +- Agregar checklist [OK]
 | +- Agregar tabla comparativa [OK]
 | +- Agregar casos de uso [OK]
 |
 +- 20-50 líneas
 | +- Objetivo: +100% a +300%
 | +- Agregar tip contextual [OK]
 | +- Agregar 1-2 ejemplos [OK]
 | +- Mejorar formato [OK]
 |
 +- 50-100 líneas
 | +- Objetivo: +80% a +150%
 | +- Aclarar puntos ambiguos [OK]
 | +- Mejorar formato [OK]
 | +- Ejemplos inline selectivos [OK]
 |
 +- > 100 líneas
 +- Objetivo: +50% a +100%
 +- Formato RST [OK]
 +- Toctrees [OK]
 +- Aclaraciones mínimas [OK]

----

Casos Especiales
================

Caso Especial 1: Tips con Código
---------------------------------

**Decisión:**

.. code-block:: text

 ¿El tip incluye código fuente?

 SÍ -> Enriquecimiento MAYOR

 Razón:
 - Código necesita explicación línea por línea
 - Contexto de uso
 - Alternativas
 - Mejores prácticas

 Ejemplo:
 Original: 25 líneas (15 texto + 10 código)
 Traducido: 120 líneas
 - 30 líneas traducción literal
 - 40 líneas explicación código
 - 30 líneas contexto
 - 20 líneas alternativas

 Enriquecimiento: +380%

Caso Especial 2: Contenido con Diagramas
-----------------------------------------

**Decisión:**

.. code-block:: text

 ¿El contenido incluye diagrama complejo?

 SÍ -> Enriquecimiento MENOR

 Razón:
 - Diagrama ya comunica mucho
 - Exceso de texto compite con diagrama
 - Explicación breve del diagrama suficiente

 Ejemplo:
 Original: 30 líneas + diagrama
 Traducido: 60 líneas + diagrama

 Enriquecimiento: +100% (moderado)

Caso Especial 3: Listas Largas
-------------------------------

**Decisión:**

.. code-block:: text

 ¿El contenido es principalmente lista (>10 items)?

 SÍ -> Enriquecimiento MÍNIMO

 Razón:
 - Lista ya es contenido denso
 - Cada item debe ser conciso
 - Agregar mucho rompe flujo

 Acción:
 - Traducir lista completa
 - Agregar contexto breve antes
 - Agregar nota después (opcional)

 Enriquecimiento: +20% a +50%

----

Verificación de Decisión
=========================

**Checklist después de decidir:**

.. code-block:: text

 [ ] 1. ¿Calculé enriquecimiento esperado?
 Líneas original: _____
 Rango objetivo: _____ % a _____ %

 [ ] 2. ¿Identifiqué qué agregar?
 [ ] Ejemplos: _____
 [ ] Checklists: _____
 [ ] Tablas: _____
 [ ] Contexto: _____

 [ ] 3. ¿Verifiqué NO agregar?
 [ ] Sin divagaciones
 [ ] Sin información no relacionada
 [ ] Sin duplicación

 [ ] 4. ¿Mi decisión está justificada?
 Razón: _________________________

----

Errores Comunes y Correcciones
===============================

Error 1: Enriquecer Muy Poco
-----------------------------

**Síntoma:**

.. code-block:: text

 Original: 15 líneas
 Traducido: 25 líneas
 Enriquecimiento: +67% [ERROR]

 Esperado: +300% a +1000%

**Problema:**
 Traducción literal sin valor agregado.

**Corrección:**

.. code-block:: text

 Agregar:
 [OK] 2-3 ejemplos prácticos
 [OK] Checklist de pasos
 [OK] Tabla comparativa
 [OK] Casos de uso

 Resultado:
 Traducido: 100 líneas
 Enriquecimiento: +567% [OK]

Error 2: Enriquecer Demasiado
------------------------------

**Síntoma:**

.. code-block:: text

 Original: 120 líneas (sección extensa)
 Traducido: 400 líneas
 Enriquecimiento: +233% [ERROR]

 Esperado: +50% a +100%

**Problema:**
 Dilución del mensaje, pérdida de foco.

**Corrección:**

.. code-block:: text

 Remover:
 [ERROR] Ejemplos redundantes
 [ERROR] Explicaciones obvias
 [ERROR] Subsecciones innecesarias

 Mantener:
 [OK] Formato mejorado
 [OK] Aclaraciones puntuales
 [OK] Toctrees

 Resultado:
 Traducido: 200 líneas
 Enriquecimiento: +67% [OK]

Error 3: Enriquecimiento Inconsistente
---------------------------------------

**Síntoma:**

.. code-block:: text

 Tip 1 (15 líneas): +50% [ERROR]
 Tip 2 (14 líneas): +800% [OK]
 Tip 3 (16 líneas): +100% [ERROR]

 Inconsistencia evidente

**Problema:**
 Sin criterio claro aplicado.

**Corrección:**

.. code-block:: text

 Aplicar matriz consistentemente:

 Todos los tips 14-16 líneas:
 -> Objetivo: +300% a +1000%

 Re-trabajar Tip 1 y Tip 3
 para alcanzar rango

----

Resumen Ejecutivo
=================

**Tabla de Referencia Rápida:**

.. list-table::
 :header-rows: 1
 :widths: 20 20 20 40

 * - **Tamaño**
 - **Rango**
 - **arc42**
 - **Acción Principal**
 * - < 20 líneas
 - +300% a +1000%
 - +771%
 - Agregar ejemplos, checklists, tablas
 * - 20-50 líneas
 - +100% a +300%
 - +273%
 - Contexto, ejemplos, relaciones
 * - 50-100 líneas
 - +80% a +150%
 - +95%
 - Aclaraciones, formato mejorado
 * - > 100 líneas
 - +50% a +100%
 - +80%
 - Formato, toctrees, mínimo

**Regla de Oro:**

.. code-block:: text

 A MENOR tamaño original -> MAYOR enriquecimiento
 A MAYOR tamaño original -> MENOR enriquecimiento

 Correlación inversa verificada en 196 archivos [OK]

----

.. seealso::
 * :doc:`../../03_estandares/calidad/metricas_traduccion` - Métricas detalladas
 * :doc:`../../03_estandares/calidad/criterios_calidad` - Criterios de calidad
 * :doc:`MD_004_traducir_vs_conservar` - Decisiones de terminología

.. note::
 Esta matriz está basada en datos reales de 196 archivos traducidos. Los rangos son guías, no reglas absolutas. Usa criterio profesional.
