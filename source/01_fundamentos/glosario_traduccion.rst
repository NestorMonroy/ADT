=======================================
Glosario de Términos de Traducción ADT
=======================================

:Categoría: Fundamentos
:Ubicación: 01_fundamentos/
:Tipo: Glosario General
:Base: Método Peshitta + ISO 1087

.. contents:: Contenido
 :depth: 2
 :local:






----

Introducción
============

Este glosario define los términos fundamentales utilizados en el proyecto ADT.

**Base metodológica:**
 - Método Peshitta (Micheli, 2014)
 - ISO 1087:2019 (Terminology work)
 - Translation Studies

----

Conceptos Fundamentales
=======================

.. glossary::

  Signifiant
    **Significante.** La FORMA externa observable del signo.

    En LaTeX: ``\textbf{texto}`` (el comando específico)

    En RST: ``**texto**`` (la sintaxis específica)

    Ver: :doc:`_fundamentos_conceptuales/signifiant_vs_signifie`

  Signifié
    **Significado.** El CONTENIDO conceptual al que apunta el signo.

    Ejemplo: "Énfasis fuerte" (función semántica)

    En ADT: Preferimos preservar Signifié sobre Signifiant

    Ver: :doc:`_fundamentos_conceptuales/signifiant_vs_signifie`

  Texto Fuente
    Source Text
    El documento original a traducir.

    En ADT: Documento LaTeX original

    Equivalente MDA: Platform-Independent Model (PIM)

  Texto Destino
    Target Text
    El documento resultante de la traducción.

    En ADT: Documento RST/Sphinx compilado a HTML

    Equivalente MDA: Platform-Specific Model (PSM)

  Vorlage
    Término alemán para el texto base del cual se traduce.

    En estudios bíblicos: El texto hebreo original

    En ADT: El LaTeX original proporcionado por el autor

Método por Defecto
===================

.. glossary::

  Segmentación
    El nivel de granularidad al que trabajamos.

    **En Peshitta:** Nivel de frase

    **En ADT:** Nivel de sección

    Ver: :doc:`_metodologias/metodo_por_defecto`

  Rendición
    Cómo traducimos cada elemento dentro de la segmentación.

    **En Peshitta:** Palabra por palabra

    **En ADT:** Comando por comando (LaTeX -> RST)

  Preferencia
    Qué preservamos cuando hay conflicto.

    **En ADT:** Signifié (contenido) sobre Signifiant (forma)

    Excepción: Código fuente (forma = contenido)

Objetivos de Traducción
========================

.. glossary::

  Domesticación
    Adaptation
    Adaptar el texto al contexto destino.

    Ejemplo: ``\begin{enumerate}`` -> ``1. 2. 3.`` (natural en RST)

    Opuesto: Extranjerización (preservar extrañeza del original)

  Claridad
    Clarity
    Hacer el texto comprensible para la audiencia destino.

    Táctica común: Agregar ``.. note::`` para aclaraciones

    Balance: No sobre-explicar

  Consistencia
    Consistency
    Resolver inconsistencias del original.

    Ejemplo: Unificar ``\textbf{}`` y ``\emph{}`` cuando se usan para lo mismo

    Decisión: Documentar en notas de traducción

  Simplificación
    Simplification
    Reducir complejidad innecesaria.

    Ejemplo: Omitir ``\vspace{}`` (no semántico en RST)

    Criterio: ¿Añade valor semántico?

Tácticas de Traducción
=======================

.. glossary::

  Adición
    Addition
    Agregar contenido no presente en el original.

    Uso: Para claridad o domesticación

    Ejemplo: ``.. note::`` explicativa

  Omisión
    Omission
    Eliminar contenido del original.

    Uso: Cuando no es semántico o es redundante

    Ejemplo: Omitir ``\noindent``

  Sustitución
    Substitution
    Reemplazar un elemento por otro.

    Uso: Mapeo comando LaTeX -> elemento RST

    Ejemplo: ``\ref{}`` -> ``:ref:``

  Cambio de Orden
    Transposition
    Reordenar elementos.

    Uso: Mejorar legibilidad o flujo

    Ejemplo: Mover figura cerca de referencia

  Especificación
    Specification
    Hacer más específico un elemento vago.

    Uso: Para claridad

    Ejemplo: "[1]" -> "Smith (2020) :cite:`smith2020`"

  Generalización
    Generalization
    Hacer más general un elemento específico.

    Uso: Unificar variantes

    Ejemplo: Múltiples estilos de énfasis -> uno solo

  Explicación
    Explicitation
    Hacer explícito lo implícito.

    Uso: Claridad

    Ejemplo: "como se dijo" -> :ref:`seccion-anterior`

  Normalización
    Normalization
    Estandarizar variaciones.

    Uso: Consistencia

    Ejemplo: Unificar nomenclatura de términos

  Modulación
    Modulation
    Cambiar perspectiva o punto de vista.

    Uso: Naturalización al idioma destino

    Ejemplo: Voz activa -> voz pasiva

  Compensación
    Compensation
    Recuperar pérdida de información en otro lugar.

    Uso: Cuando traducción directa pierde matiz

    Ejemplo: Nota al pie explicativa

  Amplificación
    Amplification
    Expandir contenido comprimido.

    Uso: Claridad

    Ejemplo: Sigla -> nombre completo + sigla

  Condensación
    Condensation
    Comprimir contenido verboso.

    Uso: Simplificación

    Ejemplo: Resumir explicación redundante

  Literalización
    Literalization
    Preservar forma exacta.

    Uso: Código fuente, ecuaciones

    Ejemplo: Código Python sin cambios

  Adaptación Cultural
    Cultural Adaptation
    Adaptar referencias culturales.

    Uso: En traducciones entre culturas

    En ADT: Menos relevante (documentación técnica)

Niveles de Análisis
====================

.. glossary::

  Global Translation Technique
    Técnica Global
    Decisiones estratégicas del documento completo.

    Ejemplos:
    
    - ¿Modo 1 (Alta Fidelidad) o Modo 2 (Marcado Visual)?
    - ¿Preservar todos los espacios verticales?
    - ¿Audiencia técnica o general?

  Local Translation Technique
    Técnica Local
    Decisiones tácticas elemento por elemento.

    Ejemplos:
    
    - ¿Este ``\emph{}`` es semántico o estilístico?
    - ¿Preservar este ``\vspace{}`` específico?
    - ¿Esta figura necesita adaptación?

Tipos de Divergencias
======================

.. glossary::

  Divergencia Intencional
    Intentional Divergence
    Desviación del método por defecto para lograr un objetivo.

    Características:
    
    - Consciente y documentada
    - Justificada por objetivo específico
    - Mejora la traducción

    Opuesto: Error

  Error
    Unintentional Divergence
    Desviación no intencional del método por defecto.

    Tipos:
    
    - Error de lectura
    - Incomprensión del original
    - Error de tipeo
    - Pérdida accidental de contenido

    Solución: Corrección en revisión

Elementos de Documento
=======================

.. glossary::

  Sección
    Section
    Unidad estructural principal en LaTeX y RST.

    LaTeX: ``\section{Título}``

    RST:

    .. code-block:: rst

       Título
       ======

  Subsección
    Subsection
    Unidad subordinada a sección.

    LaTeX: ``\subsection{Título}``

    RST:

    .. code-block:: rst

       Título
       ------

  Figura
    Figure
    Imagen con caption y label.

    LaTeX: ``\begin{figure}...\end{figure}``

    RST: ``.. figure::``

  Tabla
    Table
    Datos tabulares.

    LaTeX: ``\begin{table}...\end{table}``

    RST: ``.. list-table::`` o tabla simple

  Ecuación
    Equation
    Expresión matemática.

    LaTeX: ``\begin{equation}...\end{equation}``

    RST: ``.. math::``

  Lista
    List
    Enumeración de ítems.

    Tipos:
    
    - Numerada (enumerate/``1. 2. 3.``)
    - No numerada (itemize/``- - -``)
    - Descriptiva (description/``term : definition``)

  Referencia Cruzada
    Cross-reference
    Enlace a otra parte del documento.

    LaTeX: ``\ref{label}``

    RST: ``:ref:`label```

  Citación
    Citation
    Referencia bibliográfica.

    LaTeX: ``\cite{key}``

    RST: ``:cite:`key```

Formatos y Medios
=================

.. glossary::

  LaTeX
    Sistema de composición tipográfica.

    En ADT: Formato fuente común

    Características: Alto control tipográfico, sintaxis compleja

  RST
    reStructuredText
    Lenguaje de marcado ligero.

    En ADT: Formato destino

    Características: Legible, extensible vía Sphinx

  Sphinx
    Generador de documentación basado en RST.

    En ADT: Motor de compilación

    Output: HTML, PDF, ePub, etc.

  Markdown
    Lenguaje de marcado simple.

    En ADT: Formato alternativo

    Relación con RST: Más simple, menos potente

Calidad y Validación
=====================

.. glossary::

  Preservación Semántica
    Semantic Preservation
    Mantener el contenido significativo del original.

    Métrica: ¿El lector obtiene la misma información?

    Prioridad: ALTA (fundamental en ADT)

  Fidelidad Formal
    Formal Fidelity
    Mantener la forma del original.

    Métrica: ¿Qué tan similar es la sintaxis?

    Prioridad: BAJA (excepto en código fuente)

  Compilación
    Build
    Proceso de generar HTML desde RST.

    Comando: ``make html``

    Validación: Debe compilar sin errores

  Revisión de Calidad
    Quality Review
    Verificación sistemática de la traducción.

    Aspectos:
    
    - Completitud
    - Preservación semántica
    - Calidad visual
    - Enlaces funcionales

Métodos y Modos
===============

.. glossary::

  Modo Alta Fidelidad
    Mode 1
    Traducción preservando máxima estructura.

    Características:
    
    - Preserva espaciado
    - Preserva orden exacto
    - Mínimas adaptaciones

    Uso: Documentos formales, libros

  Modo Marcado Visual
    Mode 2
    Traducción con marcadores visuales.

    Características:
    
    - Marca conceptos clave
    - Añade claridad visual
    - Más adaptaciones

    Uso: Material didáctico, tutoriales

  Workflow
    Flujo de Trabajo
    Secuencia de pasos para traducir.

    Pasos típicos:
    
    1. Análisis
    2. Traducción
    3. Validación
    4. Revisión
    5. Publicación

Conceptos Avanzados
===================

.. glossary::

  Isomorfismo Metodológico
    Methodological Isomorphism
    Correspondencia estructural entre dominios.

    En ADT: Traducción ≈ Transformación de modelos

    Ver: :doc:`metamodelos/framework_universal_transformacion`

  PIM
    Platform-Independent Model
    Modelo independiente de plataforma (MDA).

    Equivalente: Texto fuente (LaTeX)

  PSM
    Platform-Specific Model
    Modelo específico de plataforma (MDA).

    Equivalente: Texto destino (RST/HTML)

  Transformación
    Transformation
    Proceso de convertir modelo en otro.

    En ADT: Traducción como transformación

    Ver: :doc:`_fundamentos_conceptuales/traduccion_como_transformacion`





----

Uso de Este Glosario
=====================

**En documentación:**

Para referenciar términos del glosario:

.. code-block:: rst

 :term:`Signifiant` vs :term:`Signifié`

 El :term:`método por defecto` consiste en...

**En código:**

Los términos están organizados alfabéticamente dentro de categorías temáticas.

**Expansión:**

Este glosario se actualiza conforme se desarrolla el proyecto.

----

Referencias
===========

- :doc:`_fundamentos_conceptuales/signifiant_vs_signifie`
- :doc:`_metodologias/metodo_por_defecto`
- :doc:`/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS`
- ISO 1087:2019 - Terminology work and terminology science

----

**Versión:** 1.0
**Fecha:** 2026-01-27
**Términos:** 50+
**Estado:** Base completa, en expansión
