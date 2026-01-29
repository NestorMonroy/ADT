============================================
Traducción como Transformación de Modelos
============================================

:Categoría: Fundamentos Conceptuales
:Ubicación: 01_fundamentos/_fundamentos_conceptuales/
:Base Metodológica: Método Peshitta (Micheli, 2014)
:Conexión: MDA/MDE, Translation Studies

.. contents:: Contenido
 :depth: 2
 :local:

----

Introducción
============

Este documento establece el **isomorfismo fundamental** entre traducción de textos
y transformación de modelos, base teórica del proyecto ADT.

**Tesis central:**
 La traducción de documentación técnica ES una transformación de modelos,
 donde preservamos contenido semántico mientras adaptamos forma sintáctica.

----

El Isomorfismo Básico
======================

Mapeo Conceptual
----------------

.. list-table::
 :header-rows: 1
 :widths: 35 30 35

 * - Concepto
   - Translation Studies
   - MDA/MDE
 * - **Entrada**
   - Texto fuente (source text)
   - Platform-Independent Model (PIM)
 * - **Salida**
   - Texto destino (target text)
   - Platform-Specific Model (PSM)
 * - **Proceso**
   - Técnica de traducción
   - Reglas de transformación
 * - **Unidad básica**
   - Palabra/Frase
   - Elemento de modelo
 * - **Preservación**
   - Significado semántico
   - Semántica del modelo
 * - **Adaptación**
   - Forma sintáctica
   - Sintaxis de plataforma

Aplicación a ADT
----------------

En el contexto ADT:

.. code-block:: text

 TEXTO FUENTE (LaTeX) ≈ PIM (Platform-Independent)
 v v
 TÉCNICA TRADUCCIÓN ≈ REGLAS TRANSFORMACIÓN
 v v
 TEXTO DESTINO (RST) ≈ PSM (Platform-Specific)

**Ejemplo Concreto:**

.. code-block:: latex

 % LaTeX (Texto Fuente / PIM)
 \section{Introducción}
 Este es un \textbf{concepto importante}.

.. code-block:: rst

 # RST (Texto Destino / PSM)
 Introducción
 ============
 Este es un **concepto importante**.

**Preservado (Semántica):**
- Estructura: Sección con título "Introducción"
- Jerarquía: Nivel 1
- Énfasis: "concepto importante" con énfasis fuerte

**Adaptado (Sintaxis):**
- ``\section{}`` -> Título subrayado con ``=``
- ``\textbf{}`` -> Marcadores ``**``

----

Niveles de Abstracción
=======================

Nivel Meta (M3): Framework Universal
-------------------------------------

**Concepto abstracto de transformación:**

.. code-block:: text

 CUALQUIER transformación preservadora de contenido:

 Entrada -> [Proceso de transformación] -> Salida

 Donde:
 - Entrada y Salida tienen DIFERENTES formas
 - Entrada y Salida tienen EL MISMO contenido esencial

**Ejemplos multi-dominio:**

- **Traducción lingüística:** Hebreo -> Siríaco (Peshitta)
- **Compilación:** C -> Assembly
- **Refactoring:** Código A -> Código B (mismo comportamiento)
- **Migración:** Python 2 -> Python 3
- **Transformación MDA:** PIM -> PSM

Nivel de Modelo (M2): Técnica de Traducción
--------------------------------------------

**Método por defecto + Divergencias:**

1. **Método por defecto:**

 - Segmentación: ¿A qué nivel trabajar? (palabra/frase/párrafo)
 - Rendición: ¿Cómo mapear elementos básicos?
 - Preferencia: ¿Forma o contenido?

2. **Divergencias para objetivos:**

 - Domesticación (adaptar a destino)
 - Claridad (hacer comprensible)
 - Consistencia (resolver inconsistencias)
 - Simplificación (reducir complejidad)

Nivel de Instancia (M1): Transformación Específica
---------------------------------------------------

**Aplicación concreta en ADT:**

Para traducir un libro LaTeX -> RST/Sphinx:

1. **Análisis del fuente:**

 - Identificar estructura (capítulos, secciones)
 - Mapear comandos LaTeX
 - Detectar inconsistencias

2. **Aplicar método por defecto:**

 - Segmentación: Nivel de sección
 - Rendición: Mapeo comando por comando
 - Preferencia: Signifié (semántica) sobre Signifiant (forma)

3. **Aplicar tácticas según objetivos:**

 - Si objetivo es claridad -> Agregar ``.. note::``
 - Si objetivo es consistencia -> Unificar nomenclatura
 - Si objetivo es simplificación -> Eliminar no-semántico

4. **Validar:**

 - Compilar Sphinx
 - Verificar preservación semántica
 - Revisar calidad visual

----

Propiedades del Isomorfismo
============================

Inyectividad (One-to-One)
--------------------------

**Pregunta:** ¿Cada elemento fuente mapea a exactamente un elemento destino?

**Respuesta:** **NO siempre** (y está bien)

**Ejemplos:**

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - Caso
   - Fuente
   - Destino
 * - **Inyectivo**
   - ``\textbf{x}``
   - ``**x**``
 * - **No inyectivo**
   - ``\emph{x}`` (contexto A)
   - ``:term:`x```
 * - **No inyectivo**
   - ``\emph{x}`` (contexto B)
   - ``*x*``

**Razón:** Contexto determina mapeo apropiado.

Suryectividad (Onto)
--------------------

**Pregunta:** ¿Cada elemento destino viene de algún elemento fuente?

**Respuesta:** **NO siempre** (adiciones permitidas)

**Ejemplos de adiciones legítimas:**

.. code-block:: rst

 .. note::
 Este concepto es fundamental.

 # Agregado para CLARIDAD (objetivo 2)
 # NO existe en LaTeX original

Preservación Estructural
-------------------------

**Propiedad clave:** Relaciones estructurales se preservan

.. code-block:: text

 Si en LaTeX: Section A contiene Subsection B

 Entonces en RST: Sección A contiene Subsección B

**Formalización:**

.. math::

 \text{Si } A \subseteq B \text{ en fuente}

 \text{Entonces } T(A) \subseteq T(B) \text{ en destino}

Donde :math:`T` es la función de transformación.

----

Aplicaciones Prácticas
=======================

Diseño de Procedimientos
-------------------------

**Template basado en isomorfismo:**

.. code-block:: rst

 PROC_XXX: [Nombre Procedimiento]
 =================================

 1. Análisis del Fuente (PIM)
 =============================
 - Identificar estructura
 - Mapear elementos
 - Detectar casos especiales

 2. Aplicar Transformación
 =========================
 - Método por defecto: [...]
 - Tácticas: [...]

 3. Validación del Destino (PSM)
 ===============================
 - Compilar
 - Verificar preservación
 - Revisar calidad

Detección de Errores
--------------------

**Errores por violación del isomorfismo:**

1. **Pérdida de contenido:**

 .. code-block:: text

 LaTeX: \section{Importante}
 RST: [omitido por error]

 -> Violación: Contenido no preservado

2. **Introducción de ruido:**

 .. code-block:: text

 LaTeX: x + y
 RST: x + y (esta suma representa...)

 -> Violación: Contenido agregado sin justificación

3. **Cambio de semántica:**

 .. code-block:: text

 LaTeX: \emph{importante} (énfasis)
 RST: `importante` (código)

 -> Violación: Semántica alterada

Optimización de Flujo
----------------------

**Usando el isomorfismo para eficiencia:**

.. code-block:: python

 # Pseudo-código
 def traducir_documento(doc_latex):
 # Nivel M2: Aplicar método por defecto
 doc_rst = aplicar_metodo_defecto(doc_latex)

 # Nivel M2: Aplicar tácticas según objetivos
 for objetivo in objetivos_traduccion:
 doc_rst = aplicar_tacticas(doc_rst, objetivo)

 # Nivel M1: Validar
 validar_preservacion(doc_latex, doc_rst)

 return doc_rst

----

Conexión con Literatura
========================

Translation Studies
-------------------

**Autores clave:**

- **Micheli (2014):** Método Peshitta Zacarías
- **Toury (1995):** Descriptive Translation Studies
- **Nida (1964):** Formal vs Dynamic Equivalence

**Conceptos aplicables:**

- Equivalencia formal ≈ Preservar Signifiant (forma)
- Equivalencia dinámica ≈ Preservar Signifié (contenido)

MDA/MDE
-------

**Estándares:**

- OMG MDA Guide v1.0.1
- MOF (Meta Object Facility)
- QVT (Query/View/Transformation)

**Conceptos aplicables:**

- PIM/PSM
- Model transformations
- Traceability

----

Conclusión
==========

**Síntesis:**

La traducción de documentación técnica NO es solo "copiar y cambiar sintaxis".
Es una **transformación de modelos** rigurosa que:

1. Preserva contenido semántico (Signifié)
2. Adapta forma sintáctica (Signifiant)
3. Sigue método sistemático (defecto + divergencias)
4. Persigue objetivos explícitos (domesticación, claridad, etc.)
5. Valida preservación de propiedades

**Implicación para ADT:**

Podemos aprovechar 50+ años de investigación en Translation Studies
Y 20+ años de desarrollo en MDA/MDE para crear una metodología
de traducción técnica de clase mundial.

----

Referencias
===========

- :doc:`/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS`
- :doc:`/docs_maestros/SINTESIS_METODOLOGICA_ADT`
- Micheli, D. (2014). Translation Technique in Peshitta Zechariah
- OMG (2003). MDA Guide v1.0.1

----

**Versión:** 1.0
**Fecha:** 2026-01-27
**Estado:** Aprobado
