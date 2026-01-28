.. _MD_001_modo_1_vs_modo_2:

===============================================
MD-001: Modo 1 vs Modo 2
===============================================

:ID: MD-001
:Tipo: Matriz de Decisión
:Pregunta: ¿Qué modo de traducción debo usar?
:Frecuencia: Una vez por proyecto
:Impacto: Alto (define workflow completo)

.. contents:: Contenido
   :depth: 3
   :local:

----

Pregunta Central
================

**¿Qué modo de traducción debo usar para este proyecto?**

Esta es la **primera decisión** que debes tomar en cualquier proyecto de traducción.

**Impacto:**
- Define el workflow completo
- Afecta tiempo de ejecución
- Determina formato de salida
- Influye en calidad final

----

Los Dos Modos
=============

Modo 1: Alta Fidelidad (Preservación)
--------------------------------------

**Filosofía:**

Preservar **exactamente** la estructura y formato del documento original.

**Características:**

.. code-block:: text

   ✅ Mantiene formato nativo (LaTeX, Markdown, etc.)
   ✅ Preserva estructura 1:1
   ✅ Fidelidad absoluta
   ✅ Ideal para documentos académicos
   ✅ Compilación directa

**Ejemplo:**

Original LaTeX:

.. code-block:: latex

   \section{Introducción}
   
   Este documento describe \textbf{arquitectura}.
   
   \begin{itemize}
     \item Componente A
     \item Componente B
   \end{itemize}

Traducido LaTeX (Modo 1):

.. code-block:: latex

   \section{Introducción}
   
   Este documento describe la \textbf{arquitectura}.
   
   \begin{itemize}
     \item Componente A
     \item Componente B
   \end{itemize}

**Nota:** Se traduce SOLO el texto, formato intacto.

Modo 2: Transformación (Conversión)
------------------------------------

**Filosofía:**

Transformar el documento a un **nuevo formato** (típicamente reStructuredText/Sphinx).

**Características:**

.. code-block:: text

   ✅ Convierte a nuevo formato (RST, etc.)
   ✅ Adapta estructura según medio destino
   ✅ Enriquecimiento permitido
   ✅ Ideal para documentación técnica
   ✅ Mayor flexibilidad

**Ejemplo:**

Original LaTeX:

.. code-block:: latex

   \section{Introducción}
   
   Este documento describe \textbf{arquitectura}.

Traducido RST (Modo 2):

.. code-block:: rst

   ==============
   Introducción
   ==============
   
   Este documento describe la **arquitectura**.

**Nota:** Se traduce Y se transforma el formato.

----

Matriz de Decisión
==================

Decisión por Tipo de Documento
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 25 25 20

   * - **Tipo de Documento**
     - **Modo 1**
     - **Modo 2**
     - **Recomendado**
   * - Libro académico LaTeX
     - ✅ Excelente
     - ⚠️ Posible
     - **Modo 1**
   * - Paper científico
     - ✅ Excelente
     - ❌ No recomendado
     - **Modo 1**
   * - Documentación técnica
     - ⚠️ Posible
     - ✅ Excelente
     - **Modo 2**
   * - Manual de usuario
     - ⚠️ Posible
     - ✅ Excelente
     - **Modo 2**
   * - Tutorial/Guía
     - ❌ No recomendado
     - ✅ Excelente
     - **Modo 2**
   * - Tesis doctoral
     - ✅ Excelente
     - ❌ No recomendado
     - **Modo 1**
   * - Blog técnico
     - ❌ No aplicable
     - ✅ Excelente
     - **Modo 2**
   * - Especificación ISO
     - ✅ Excelente
     - ⚠️ Con cuidado
     - **Modo 1**

Decisión por Objetivo
----------------------

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - **Objetivo**
     - **Modo 1**
     - **Modo 2**
   * - Publicación académica
     - ✅ Preferido
     - ❌
   * - Documentación web
     - ❌
     - ✅ Preferido
   * - Impresión física
     - ✅ Preferido
     - ⚠️ Posible
   * - Consulta online
     - ⚠️ Posible
     - ✅ Preferido
   * - Versionado continuo
     - ⚠️ Difícil
     - ✅ Fácil
   * - Colaboración múltiple
     - ⚠️ Complejo
     - ✅ Simple

Decisión por Restricciones
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - **Restricción**
     - **Favorece Modo 1**
     - **Favorece Modo 2**
   * - Debe compilar en LaTeX
     - ✅ Sí
     - ❌ No
   * - Requiere búsqueda web
     - ❌ No
     - ✅ Sí
   * - Formato original crítico
     - ✅ Sí
     - ❌ No
   * - Necesita enriquecimiento
     - ⚠️ Limitado
     - ✅ Sí
   * - Múltiples formatos salida
     - ❌ No
     - ✅ Sí

----

Árbol de Decisión
=================

Proceso Paso a Paso
-------------------

.. code-block:: text

   INICIO: ¿Qué modo usar?
        ↓
   PASO 1: ¿Es documento académico formal?
        ├─ SÍ → ¿Requiere compilación LaTeX?
        │       ├─ SÍ → MODO 1 ✅
        │       └─ NO → Continuar a PASO 2
        │
        └─ NO → Continuar a PASO 2
   
   PASO 2: ¿Se publicará SOLO en web?
        ├─ SÍ → MODO 2 ✅
        └─ NO → Continuar a PASO 3
   
   PASO 3: ¿El formato original es crítico?
        ├─ SÍ → MODO 1 ✅
        └─ NO → Continuar a PASO 4
   
   PASO 4: ¿Necesitas enriquecer contenido?
        ├─ SÍ (mucho) → MODO 2 ✅
        └─ NO → Continuar a PASO 5
   
   PASO 5: ¿Múltiples formatos de salida?
        ├─ SÍ → MODO 2 ✅
        └─ NO → MODO 1 por defecto ✅

**Regla de oro:** Cuando dudes, usa **Modo 2** (más flexible).

Ejemplos de Decisión
--------------------

**Caso 1: Libro de BPM en LaTeX**

.. code-block:: text

   Tipo: Libro académico
   Original: LaTeX con paquetes específicos
   Objetivo: Publicación impresa + PDF
   Restricción: Formato LaTeX requerido
   
   Decisión: MODO 1 ✅
   
   Razón: Publicación académica requiere
          compilación LaTeX nativa

**Caso 2: Documentación arc42**

.. code-block:: text

   Tipo: Framework de documentación
   Original: Markdown
   Objetivo: Documentación web interactiva
   Restricción: Búsqueda y navegación web
   
   Decisión: MODO 2 ✅
   
   Razón: Mejor experiencia en Sphinx/RST
          para documentación técnica web

**Caso 3: Manual de usuario**

.. code-block:: text

   Tipo: Manual técnico
   Original: Word/Markdown
   Objetivo: Web + PDF + impresión
   Restricción: Múltiples formatos
   
   Decisión: MODO 2 ✅
   
   Razón: Sphinx genera múltiples formatos
          desde una sola fuente

**Caso 4: Tesis doctoral**

.. code-block:: text

   Tipo: Tesis académica
   Original: LaTeX con plantilla universidad
   Objetivo: Entrega institucional
   Restricción: Formato específico requerido
   
   Decisión: MODO 1 ✅
   
   Razón: Cumplimiento de formato
          institucional obligatorio

----

Comparación Detallada
=====================

Ventajas y Desventajas
----------------------

**Modo 1: Alta Fidelidad**

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - **Ventajas ✅**
     - **Desventajas ❌**
   * - Fidelidad absoluta
     - Menos flexible
   * - Formato original preservado
     - Difícil enriquecer
   * - Compilación directa
     - Un solo formato salida
   * - Ideal para académico
     - Navegación web limitada
   * - Menor transformación
     - Requiere conocer formato original

**Modo 2: Transformación**

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - **Ventajas ✅**
     - **Desventajas ❌**
   * - Múltiples formatos salida
     - Requiere conversión
   * - Enriquecimiento fácil
     - Pierde formato nativo
   * - Excelente para web
     - Más tiempo inicial
   * - Búsqueda integrada
     - Curva aprendizaje RST
   * - Navegación superior
     - No para todos los tipos

Tiempo de Ejecución
-------------------

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - **Fase**
     - **Modo 1**
     - **Modo 2**
   * - Configuración inicial
     - Rápida (15 min)
     - Media (1-2 horas)
   * - Traducción por página
     - Rápida
     - Media (+ conversión)
   * - Enriquecimiento
     - Limitado
     - Extensivo
   * - Verificación
     - Simple
     - Más compleja
   * - **Total proyecto**
     - **Menor**
     - **Mayor inicial, menor a largo plazo**

Calidad de Salida
-----------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - **Aspecto**
     - **Modo 1**
     - **Modo 2**
   * - Fidelidad al original
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐⭐
   * - Experiencia web
     - ⭐⭐⭐
     - ⭐⭐⭐⭐⭐
   * - Búsqueda
     - ⭐⭐
     - ⭐⭐⭐⭐⭐
   * - Navegación
     - ⭐⭐
     - ⭐⭐⭐⭐⭐
   * - Impresión
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐⭐
   * - Flexibilidad
     - ⭐⭐⭐
     - ⭐⭐⭐⭐⭐

----

Casos Especiales
================

Modo Híbrido (Ambos)
---------------------

**Cuándo usar:**

.. code-block:: text

   ✅ Proyecto grande con múltiples audiencias
   ✅ Necesidad de formato original Y web
   ✅ Recursos suficientes

**Proceso:**

.. code-block:: text

   1. Traducción Modo 1 (LaTeX nativo)
   2. Conversión automática a RST (Pandoc)
   3. Refinamiento manual Modo 2
   4. Mantener ambas versiones

**Ejemplo:** Libro académico que también quiere presencia web premium

**Costo:** 1.5x-2x el tiempo de un solo modo

Cambio de Modo Durante Proyecto
--------------------------------

**Posible pero costoso:**

.. code-block:: text

   De Modo 1 a Modo 2:
   ✅ Relativamente fácil (Pandoc)
   ⏱️ Tiempo: 20-30% del original
   
   De Modo 2 a Modo 1:
   ⚠️ Difícil (pérdida de enriquecimiento)
   ⏱️ Tiempo: 50-70% del original

**Recomendación:** Decidir modo ANTES de iniciar proyecto

----

Recomendaciones Finales
========================

Guía Rápida de Decisión
------------------------

**Usa Modo 1 si:**

.. code-block:: text

   ✅ Documento académico formal
   ✅ Requiere compilación LaTeX
   ✅ Formato original es crítico
   ✅ Una sola salida (PDF impreso)
   ✅ Fidelidad absoluta requerida

**Usa Modo 2 si:**

.. code-block:: text

   ✅ Documentación técnica
   ✅ Publicación web primaria
   ✅ Necesitas búsqueda/navegación
   ✅ Múltiples formatos de salida
   ✅ Enriquecimiento importante
   ✅ Colaboración continua

**Cuando dudes:**

.. code-block:: text

   → Pregunta: ¿Quién leerá esto y cómo?
   
   Si respuesta incluye "web", "búsqueda", "navegación":
   → MODO 2 ✅
   
   Si respuesta es "impresión académica formal":
   → MODO 1 ✅

Errores Comunes
---------------

**Error 1: Elegir Modo 1 por familiaridad**

.. code-block:: text

   Situación: "Conozco LaTeX, usaré Modo 1"
   Problema: Documentación web necesita Modo 2
   
   Lección: Basar decisión en OBJETIVO, no en familiaridad

**Error 2: Elegir Modo 2 siempre**

.. code-block:: text

   Situación: "Sphinx es mejor, siempre Modo 2"
   Problema: Tesis doctoral requiere LaTeX nativo
   
   Lección: Cada proyecto es diferente

**Error 3: Cambiar de modo a mitad**

.. code-block:: text

   Situación: Empezar Modo 1, cambiar a Modo 2
   Problema: Re-trabajo significativo
   
   Lección: Decidir ANTES de comenzar

Checklist de Decisión
----------------------

.. code-block:: text

   Antes de elegir modo, verificar:
   
   ☐ Tipo de documento identificado
   ☐ Objetivo de publicación claro
   ☐ Audiencia definida
   ☐ Restricciones conocidas
   ☐ Formatos de salida decididos
   ☐ Recursos disponibles evaluados
   
   Después de elegir:
   
   ☐ Decisión documentada
   ☐ Equipo alineado (si aplica)
   ☐ Herramientas preparadas
   ☐ Workflow definido

----

Casos Reales
============

Proyecto arc42 → Modo 2
------------------------

**Contexto:**

.. code-block:: text

   Original: Markdown
   Objetivo: Documentación web interactiva
   Audiencia: Desarrolladores/arquitectos
   Resultado: 196 archivos traducidos

**Decisión: Modo 2** ✅

**Razones:**

.. code-block:: text

   1. Documentación técnica (no académica)
   2. Búsqueda crítica para usuarios
   3. Navegación entre secciones importante
   4. Enriquecimiento deseado
   5. Sphinx ideal para este tipo

**Resultado:** ✅ Éxito total (100% completitud)

Libro BPM Académico → Modo 1
-----------------------------

**Contexto:**

.. code-block:: text

   Original: LaTeX con paquetes académicos
   Objetivo: Publicación impresa + PDF
   Audiencia: Académicos/estudiantes
   Resultado: Libro completo traducido

**Decisión: Modo 1** ✅

**Razones:**

.. code-block:: text

   1. Libro académico formal
   2. Compilación LaTeX requerida
   3. Formato específico del publisher
   4. Impresión física primaria
   5. Fidelidad absoluta crítica

**Resultado:** ✅ Publicación exitosa

----

Conclusión
==========

**Mensaje clave:**

.. important::
   La elección entre Modo 1 y Modo 2 es la **decisión más importante** de tu proyecto de traducción.
   
   Tómate el tiempo necesario para decidir correctamente **ANTES** de comenzar.

**Regla de oro:**

.. code-block:: text

   Académico formal + LaTeX → Modo 1
   Documentación técnica + Web → Modo 2
   
   Cuando dudes → Modo 2 (más flexible)

**Próximos pasos:**

Una vez decidido el modo:

- Modo 1: Seguir :doc:`../../02_procedimientos/modo_alta_fidelidad/index`
- Modo 2: Seguir :doc:`../../02_procedimientos/workflow_general`

----

.. seealso::
   * :doc:`../../02_procedimientos/workflow_general` - Workflow Modo 2
   * :doc:`../../02_procedimientos/modo_alta_fidelidad/index` - Workflow Modo 1
   * :doc:`../../06_casos_practicos/antes_despues/caso_01_seccion_breve` - Ejemplo Modo 2
   * :doc:`../../07_guias_uso/guia_rapida` - Guía rápida

.. note::
   Esta matriz se basa en experiencia real de múltiples proyectos. Tu contexto específico puede tener consideraciones adicionales.
