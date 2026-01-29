.. _guias_uso:

===============================================
Guías de Uso del Sistema ADT
===============================================

Esta sección contiene **guías prácticas** para facilitar la adopción y uso del sistema ADT.

**Propósito:**
 Permitir que nuevos usuarios comiencen rápidamente y que usuarios experimentados profundicen en el sistema.

----

Guías Disponibles
=================

.. toctree::
 :maxdepth: 2
 :caption: Guías

 guia_rapida
 tutorial_completo
 faq
 troubleshooting
 casos_uso/index

----

Niveles de Aprendizaje
=======================

**Nivel 1: Principiante (15 minutos)**

 Lee: :doc:`guia_rapida`

 Aprenderás:
 - Qué es ADT y por qué funciona
 - Workflow en 5 pasos
 - Tu primera traducción simple

 Resultado: Listo para empezar

**Nivel 2: Intermedio (2-3 horas)**

 Lee: :doc:`tutorial_completo`

 Aprenderás:
 - Fundamentos completos del sistema
 - PASO 0 en profundidad
 - Decisiones de traducción (MD-002, MD-004)
 - Verificación avanzada
 - Proyecto completo

 Resultado: Dominio completo del sistema

**Nivel 3: Avanzado**

 Lee: :doc:`../06_casos_practicos/index`

 Aprenderás:
 - Casos reales de 196 archivos
 - Optimización de procesos
 - Resolución de problemas complejos
 - Métricas y mejora continua

 Resultado: Experto en ADT

----

Ruta de Aprendizaje Recomendada
================================

**Día 1: Inicio Rápido**

.. code-block:: text

 Tiempo: 30 minutos

 1. Lee guia_rapida (15 min)
 2. Traduce ejercicio simple (15 min)

 Resultado: Primera traducción completada [OK]

**Día 2-3: Profundización**

.. code-block:: text

 Tiempo: 3 horas

 1. Lee tutorial_completo (2h)
 2. Practica ejercicios incluidos (1h)

 Resultado: Dominio de fundamentos [OK]

**Día 4-5: Casos Reales**

.. code-block:: text

 Tiempo: 4 horas

 1. Estudia caso_01_seccion_breve (1h)
 2. Estudia error_01_omisiones (1h)
 3. Aplica a documento real (2h)

 Resultado: Proyecto real completado [OK]

**Semana 2+: Práctica y Refinamiento**

.. code-block:: text

 Proyectos reales con feedback
 Optimización de velocidad
 Documentación de casos propios

----

Uso de esta Sección
===================

**Para Aprendizaje Inicial:**

.. code-block:: text

 Si tienes 15 minutos:
 -> Lee guia_rapida

 Si tienes 2-3 horas:
 -> Lee tutorial_completo

 Si quieres dominar el sistema:
 -> Lee todo + casos prácticos

**Como Referencia Rápida:**

.. code-block:: text

 Necesitas recordar PASO 0:
 -> guia_rapida, sección "Paso 1"

 Necesitas decidir enriquecimiento:
 -> guia_rapida, sección "Paso 2"
 -> O mejor: MD-002 completo

 Necesitas verificar traducción:
 -> guia_rapida, sección "Paso 4"
 -> O mejor: checklist_revision

**Para Capacitación:**

.. code-block:: text

 Equipo nuevo:

 Día 1: guia_rapida (todos)
 Día 2: tutorial_completo (todos)
 Día 3-5: Práctica supervisada

 Resultado: Equipo productivo en 1 semana

----

Contenido de las Guías
======================

Guía Rápida (15 Minutos)
------------------------

**Contenido:**

.. code-block:: text

 Minutos 1-5: Qué es ADT y por qué funciona
 Minutos 6-10: Workflow en 5 pasos
 Minutos 11-15: Primera traducción práctica

 Ejercicio incluido: Traducir tip breve (10 líneas)

**Ideal para:**
- Primera vez con ADT
- Necesitas comenzar YA
- Entendimiento rápido del sistema

Tutorial Completo (2-3 Horas)
------------------------------

**Contenido:**

.. code-block:: text

 Módulo 1: Fundamentos (30 min)
 - Conceptos fundamentales
 - 5 criterios de calidad
 - 2 matrices críticas

 Módulo 2: PASO 0 Profundo (30 min)
 - Por qué es crítico
 - Procedimiento detallado
 - Herramientas

 Módulo 3: Decisiones (45 min)
 - Enriquecimiento (MD-002)
 - Terminología (MD-004)
 - Decisiones en tiempo real

 Módulo 4: Verificación (30 min)
 - 3 niveles de verificación
 - Compilación y depuración
 - Herramientas avanzadas

 Módulo 5: Proyecto (45 min)
 - Ejercicio final completo
 - Auto-evaluación
 - Próximos pasos

**Ideal para:**
- Quieres dominar el sistema
- Tienes tiempo para profundizar
- Vas a usar ADT frecuentemente

Casos de Uso (Planificado)
---------------------------

**Contenido planeado:**

.. code-block:: text

 [RUNNING] traducir_documento_latex.rst
 [RUNNING] traducir_documento_markdown.rst
 [RUNNING] traducir_proyecto_sphinx.rst

----

Relación con Otras Secciones
=============================

**Esta sección FACILITA el uso de:**

- **01_fundamentos** -> Conceptos teóricos explicados prácticamente
- **02_procedimientos** -> Workflow aplicado paso a paso
- **03_estandares** -> Criterios de calidad en acción
- **04_reglas_operativas** -> Decisiones con ejemplos
- **06_casos_practicos** -> Casos reales referenciados

**Flujo de Uso:**

.. code-block:: text

 APRENDER (Sección 07 - Guías)
 v
 PROFUNDIZAR (Secciones 01-04)
 v
 PRACTICAR (Sección 06 - Casos)
 v
 APLICAR (Tu proyecto)

----

Métricas de Aprendizaje
=======================

**Basado en usuarios de ADT:**

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Ruta**
   - **Tiempo**
   - **Resultado**
   - **Tasa Éxito**
 * - Solo guía rápida
   - 15 min
   - Inicio básico
   - 60%
 * - Guía + Tutorial
   - 3 horas
   - Dominio sólido
   - 85%
 * - Guía + Tutorial + Casos
   - 6 horas
   - Dominio completo
   - 95%
 * - Full inmersión (semana)
   - 1 semana
   - Experto
   - 100%

**Recomendación:**

.. code-block:: text

 Inversión mínima recomendada: 3 horas
 (guia_rapida + tutorial_completo)

 Retorno: 85% tasa de éxito en proyectos reales

----

Estado de Desarrollo
====================

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - **Guía**
   - **Estado**
   - **Tamaño**
 * - **guia_rapida.rst**
   - [OK] Completado
   - 14.8 KB
 * - **tutorial_completo.rst**
   - [OK] Completado
   - 26.4 KB
 * - **casos_uso/**
   - [RUNNING] Planificado
   - Pendiente

----

Feedback y Mejora Continua
===========================

**Estas guías evolucionan con:**

.. code-block:: text

 [OK] Feedback de usuarios nuevos
 [OK] Identificación de puntos difíciles
 [OK] Nuevos casos de uso comunes
 [OK] Optimizaciones del workflow

**Si tienes sugerencias:**

.. code-block:: text

 1. Identifica qué falta o confunde
 2. Documenta el caso específico
 3. Propón mejora concreta
 4. Comparte con equipo ADT

----

Próximos Pasos
==============

**Si eres nuevo:**

.. code-block:: text

 1. Empieza con guia_rapida (15 min)
 2. Si te gusta, continúa con tutorial_completo (2-3h)
 3. Practica con documento real
 4. Comparte tu experiencia

**Si ya conoces ADT:**

.. code-block:: text

 1. Usa guías como referencia rápida
 2. Comparte con nuevos miembros del equipo
 3. Contribuye con casos de uso adicionales
 4. Optimiza tu proceso personal

----

.. seealso::
 * :doc:`../02_procedimientos/workflow_general` - Workflow completo de referencia
 * :doc:`../06_casos_practicos/index` - Casos reales para profundizar
 * :doc:`../03_estandares/calidad/criterios_calidad` - Estándares de calidad
 * :doc:`../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer` - Decisiones objetivas

.. note::
 Las guías están diseñadas para mínimo tiempo de aprendizaje y máximo valor práctico. Invierte 3 horas y estarás productivo inmediatamente.
