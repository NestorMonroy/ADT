================================================
Framework Universal de Transformación
================================================

:Tipo: Metamodelo
:Ubicación: 01_fundamentos/metamodelos/
:Aplicabilidad: Trans-dominio
:Base: Método Peshitta + MDA/MDE

.. contents:: Contenido
 :depth: 2
 :local:

----

Introducción
============

Este documento define el **Framework Universal de Transformación**, un metamodelo
aplicable a CUALQUIER proceso de transformación que preserve contenido esencial
mientras adapta forma a nuevo contexto.

**Dominios de aplicación:**

[OK] Traducción lingüística (hebreo -> siríaco, español -> inglés)
[OK] Transformación de modelos (PIM -> PSM)
[OK] Compilación (C -> Assembly)
[OK] Refactoring (código A -> código B)
[OK] Migración de plataforma (Python 2 -> Python 3)
[OK] Traducción técnica (LaTeX -> RST)

----

El Framework en 5 Componentes
==============================

1. Entrada (Source)
-------------------

**Definición:**
 El artefacto de partida que contiene el contenido a preservar.

**Propiedades:**

.. code-block:: text

 - Forma específica (Signifiant)
 - Contenido semántico (Signifié)
 - Contexto de origen
 - Plataforma/Idioma de origen

**Ejemplos multi-dominio:**

.. list-table::
 :widths: 30 70
 :header-rows: 1

 * - Dominio
   - Entrada (Source)
 * - Peshitta
   - Texto hebreo del libro de Zacarías
 * - MDA
   - Platform-Independent Model (PIM)
 * - ADT
   - Documento LaTeX original
 * - Compilación
   - Código fuente en C
 * - Refactoring
   - Código antes de refactorizar

2. Salida (Target)
------------------

**Definición:**
 El artefacto resultante que preserva el contenido pero adapta la forma.

**Propiedades:**

.. code-block:: text

 - Forma adaptada (nuevo Signifiant)
 - Contenido preservado (mismo Signifié)
 - Contexto de destino
 - Plataforma/Idioma de destino

**Ejemplos multi-dominio:**

.. list-table::
 :widths: 30 70
 :header-rows: 1

 * - Dominio
   - Salida (Target)
 * - Peshitta
   - Texto siríaco de Zacarías
 * - MDA
   - Platform-Specific Model (PSM)
 * - ADT
   - Documento RST/Sphinx
 * - Compilación
   - Código Assembly
 * - Refactoring
   - Código después de refactorizar

3. Método por Defecto
---------------------

**Definición:**
 El procedimiento estándar aplicado en ausencia de condiciones especiales.

**Componentes:**

a) **Segmentación:**
 ¿A qué nivel de granularidad trabajar?

b) **Rendición:**
 ¿Cómo mapear elementos básicos?

c) **Preferencia:**
 ¿Forma o contenido cuando hay conflicto?

**Tabla comparativa:**

.. list-table::
 :widths: 20 25 25 30
 :header-rows: 1

 * - Dominio
   - Segmentación
   - Rendición
   - Preferencia
 * - Peshitta
   - Frase
   - Palabra
   - Signifié
 * - ADT
   - Sección
   - Comando
   - Signifié
 * - MDA
   - Paquete/Clase
   - Elemento
   - Semántica
 * - Compilación
   - Función
   - Instrucción
   - Comportamiento

4. Objetivos (Goals)
--------------------

**Definición:**
 Razones explícitas para desviarse del método por defecto.

**Los 4 Objetivos Universales:**

1. **Domesticación (Adaptation):**
 Adaptar al contexto/plataforma destino

2. **Claridad (Clarity):**
 Hacer comprensible para audiencia destino

3. **Consistencia (Consistency):**
 Resolver inconsistencias del original

4. **Simplificación (Simplification):**
 Reducir complejidad innecesaria

**Aplicación en dominios:**

.. list-table::
 :widths: 20 80
 :header-rows: 1

 * - Objetivo
   - Ejemplo ADT
 * - Domesticación
   - ``\textbf{}`` -> ``**`` (sintaxis natural RST)
 * - Claridad
   - Agregar ``.. note::`` para aclarar
 * - Consistencia
   - Unificar ``\textbf{}`` y ``\emph{}`` a un solo estilo
 * - Simplificación
   - Omitir ``\vspace{}`` (no semántico en RST)

5. Tácticas (Tactics)
---------------------

**Definición:**
 Operaciones concretas para lograr objetivos.

**Las 14+ Tácticas Universales:**

.. list-table::
 :widths: 20 40 40
 :header-rows: 1

 * - Táctica
   - Descripción
   - Ejemplo ADT
 * - **Adición**
   - Agregar contenido
   - ``.. note::`` para claridad
 * - **Omisión**
   - Eliminar contenido
   - Omitir ``\noindent``
 * - **Sustitución**
   - Cambiar elemento
   - ``\ref{}`` -> ``:ref:``
 * - **Cambio orden**
   - Reordenar
   - Mover figura cerca de ref
 * - **Especificación**
   - Hacer más específico
   - "[1]" -> "Smith (2020)"
 * - **Generalización**
   - Hacer más general
   - Unificar variantes
 * - **Explicación**
   - Expandir
   - Agregar contexto
 * - **Normalización**
   - Estandarizar
   - Unificar nomenclatura
 * - **Transposición**
   - Cambiar categoría
   - Verbo -> Sustantivo
 * - **Modulación**
   - Cambiar perspectiva
   - Activa -> Pasiva
 * - **Compensación**
   - Recuperar pérdida
   - Info en nota al pie
 * - **Amplificación**
   - Expandir implícito
   - Hacer explícito
 * - **Condensación**
   - Comprimir
   - Resumir verboso
 * - **Literalización**
   - Preservar forma
   - Código fuente

----

Proceso de Aplicación
======================

Paso 1: Análisis de Entrada
----------------------------

.. code-block:: text

 1. Identificar estructura
 2. Mapear elementos
 3. Detectar casos especiales
 4. Documentar contexto

Paso 2: Aplicar Método por Defecto
-----------------------------------

.. code-block:: text

 1. Segmentar según nivel definido
 2. Renderizar según tabla de mapeo
 3. Preferir contenido sobre forma
 4. Validar preservación básica

Paso 3: Identificar Necesidad de Divergencia
---------------------------------------------

.. code-block:: text

 ¿El método por defecto es suficiente?

 SI SÍ:
 -> Listo

 SI NO:
 -> ¿Qué objetivo requiere divergencia?
 -> Ir a Paso 4

Paso 4: Aplicar Tácticas según Objetivos
-----------------------------------------

.. code-block:: text

 Para cada objetivo:
 1. Seleccionar táctica(s) apropiada(s)
 2. Aplicar táctica
 3. Documentar decisión
 4. Validar preservación

Paso 5: Validación Final
-------------------------

.. code-block:: text

 1. ¿Contenido semántico preservado?
 2. ¿Forma adaptada correctamente?
 3. ¿Objetivos logrados?
 4. ¿Funciona en plataforma destino?

----

Propiedades Formales
====================

Preservación Semántica
----------------------

**Propiedad fundamental:**

.. math::

 \forall x \in \text{Entrada}: \text{Signifié}(x) = \text{Signifié}(T(x))

Donde :math:`T` es la función de transformación.

Adaptación Sintáctica
---------------------

.. math::

 \forall x \in \text{Entrada}: \text{Signifiant}(x) \neq \text{Signifiant}(T(x))

(En general, con excepciones para literalización)

Trazabilidad
------------

.. math::

 \forall y \in \text{Salida}: \exists x \in \text{Entrada}: T(x) \rightarrow y

----

Aplicación Trans-Dominio
========================

Tabla Maestra de Aplicabilidad
-------------------------------

.. list-table::
 :widths: 20 20 20 20 20
 :header-rows: 1

 * - Dominio
   - Framework
   - Método Defecto
   - Objetivos
   - Tácticas
 * - **Traducción**
   - [OK] 100%
   - [OK] 100%
   - [OK] 100%
   - [OK] 100%
 * - **MDA/MDE**
   - [OK] 100%
   - [OK] 95%
   - [OK] 90%
   - [OK] 85%
 * - **Compilación**
   - [OK] 100%
   - [OK] 95%
   - [OK] 70%
   - [OK] 60%
 * - **Refactoring**
   - [OK] 100%
   - [OK] 90%
   - [OK] 85%
   - [OK] 80%
 * - **Migración**
   - [OK] 100%
   - [OK] 95%
   - [OK] 90%
   - [OK] 85%

----

Conclusión
==========

**Síntesis:**

Este framework es **universal** porque captura la esencia de CUALQUIER
transformación preservadora de contenido:

1. **Entrada** con forma y contenido
2. **Método por defecto** sistemático
3. **Objetivos** explícitos para divergencias
4. **Tácticas** concretas para lograr objetivos
5. **Salida** con contenido preservado, forma adaptada

**Valor:**

- [OK] Aplicable a múltiples dominios
- [OK] Base en 50+ años de investigación
- [OK] Riguroso y sistemático
- [OK] Práctico y operacional
- [OK] Mejora iterativa posible

----

Referencias
===========

- :doc:`/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS`
- :doc:`/docs_maestros/SINTESIS_METODOLOGICA_ADT`
- :doc:`../_fundamentos_conceptuales/traduccion_como_transformacion`
- :doc:`comparacion_mda_traduccion`
- :doc:`isomorfismo_metodologico`

----

**Versión:** 1.0
**Fecha:** 2026-01-27
**Estado:** Aprobado
