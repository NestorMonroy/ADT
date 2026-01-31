Objetivos y Tácticas de Traducción
==================================

:Categoría: Fundamentos
:Ubicación: 01_fundamentos/
:Base: Método Peshitta (Micheli, 2014)
:Aplicación: Decisiones de traducción en ADT

.. contents:: Contenido
 :depth: 3
 :local:




Introducción
============

Este documento presenta los **4 objetivos** y **14+ tácticas** que guían las
decisiones de traducción en ADT.

**Concepto clave:**
 El método por defecto cubre el 80-90% de casos.

 Para el 10-20% restante, usamos OBJETIVOS y TÁCTICAS.




Los Cuatro Objetivos de Traducción
==================================

Objetivo 1: Domesticación
=========================

**Definición:**
 Adaptar el contenido al medio/contexto destino (RST/Sphinx).

**¿Cuándo aplicar?**
 - Cuando LaTeX usa construcciones que no existen naturalmente en RST
 - Cuando queremos aprovechar características específicas de Sphinx
 - Cuando la traducción literal resultaría en RST no idiomático

**Ejemplos:**

.. list-table::
 :widths: 40 40 20
 :header-rows: 1

 * - LaTeX (Fuente)
   - RST (Domesticado)
   - Táctica
 * - ``\begin{enumerate}``
   - ``1. 2. 3.``
   - Sustitución
 * - ``\textbf{}``
   - ``**``
   - Sustitución
 * - ``\ref{sec:intro}``
   - ``:ref:`intro```
   - Sustitución
 * - ``\begin{verbatim}``
   - ``.. code-block::``
   - Sustitución

**Tácticas comunes:**
 - Sustitución (cambiar a equivalente RST)
 - Normalización (usar convenciones RST)

**Métrica de éxito:**
 El RST resultante es idiomático y natural para usuarios de Sphinx.

Objetivo 2: Claridad
====================

**Definición:**
 Hacer el contenido más comprensible para el lector.

**¿Cuándo aplicar?**
 - Cuando el original es ambiguo o confuso
 - Cuando referencias son vagas
 - Cuando se puede beneficiar de aclaraciones
 - Cuando terminología necesita explicación

**Ejemplos:**

.. list-table::
 :widths: 40 40 20
 :header-rows: 1

 * - LaTeX (Vago)
   - RST (Claro)
   - Táctica
 * - "Ver antes"
   - "Ver :ref:`seccion-anterior`"
   - Especificación
 * - "[1]"
   - "Smith (2020) [smith2020]"
   - Especificación
 * - "Este concepto..."
   - ".. note:: Este concepto es fundamental..."
   - Adición
 * - "API"
   - "API (Application Programming Interface)"
   - Amplificación

**Tácticas comunes:**
 - Adición (agregar ``.. note::``, ``.. important::``)
 - Especificación (hacer referencias explícitas)
 - Explicación (expandir implícito)
 - Amplificación (expandir siglas/términos)

**Métrica de éxito:**
 Un lector sin contexto previo puede entender el contenido.

**Precaución:**
 No sobre-explicar. Balance entre claridad y concisión.

Objetivo 3: Consistencia
========================

**Definición:**
 Resolver inconsistencias del documento original.

**¿Cuándo aplicar?**
 - Cuando el autor usa múltiples términos para el mismo concepto
 - Cuando hay variaciones de estilo sin razón semántica
 - Cuando nomenclatura es inconsistente
 - Cuando estructura varía sin justificación

**Ejemplos:**

.. list-table::
 :widths: 25 25 30 20
 :header-rows: 1

 * - Problema Original
   - Variante 1
   - Variante 2
   - Solución
 * - Énfasis inconsistente
   - ``\textbf{}``
   - ``\emph{}`` (mismo uso)
   - Unificar a ``**``
 * - Terminología
   - "base de datos"
   - "BD"
   - Usar "base de datos" + ``BD`` primera vez
 * - Referencias
   - "sección anterior"
   - "antes"
   - Usar ``:ref:`` explícito siempre
 * - Estilo de listas
   - itemize en cap. 1
   - enumerate cap. 2 (mismo contenido)
   - Unificar criterio

**Tácticas comunes:**
 - Normalización (estandarizar)
 - Generalización (unificar variantes)
 - Sustitución (cambiar a forma consistente)

**Métrica de éxito:**
 El documento resultante usa terminología y estilo consistentes.

**Documentación:**
 SIEMPRE documentar decisiones de consistencia en notas de traducción.

Objetivo 4: Simplificación
==========================

**Definición:**
 Reducir complejidad innecesaria del original.

**¿Cuándo aplicar?**
 - Cuando LaTeX tiene complejidad puramente estilística
 - Cuando elementos no aportan valor semántico
 - Cuando RST/Sphinx maneja automáticamente algo
 - Cuando verbosidad puede reducirse sin pérdida

**Ejemplos:**

.. list-table::
 :widths: 40 40 20
 :header-rows: 1

 * - LaTeX (Complejo)
   - RST (Simple)
   - Táctica
 * - ``\noindent``
   - [omitir]
   - Omisión
 * - ``\vspace{1cm}``
   - [omitir]
   - Omisión
 * - ``\begin{center}\textbf{X}\end{center}``
   - ``**X**``
   - Condensación
 * - Explicación redundante (3 párrafos)
   - Explicación concisa (1 párrafo)
   - Condensación

**Tácticas comunes:**
 - Omisión (eliminar no-semántico)
 - Condensación (comprimir verboso)

**Métrica de éxito:**
 El RST es más simple pero preserva TODO el contenido semántico.

**Precaución:**
 NUNCA omitir contenido semántico. Solo complejidad innecesaria.




Las 14+ Tácticas de Traducción
==============================

Táctica 1: Adición (Addition)
=============================

**Definición:**
 Agregar contenido NO presente en el original.

**Uso:**
 Para objetivos de **Claridad** principalmente.

**Ejemplos:**

.. code-block:: rst

 # Original (LaTeX)
 Este concepto es importante.

 # Traducción con Adición (RST)
 .. important::
 Este concepto es fundamental para entender el capítulo.

**Cuándo usar:**
 - Agregar notas explicativas (``.. note::``)
 - Agregar advertencias (``.. warning::``)
 - Agregar referencias cruzadas
 - Agregar contexto que ayuda al lector

**Precaución:**
 No cambiar el mensaje del autor. Solo aclarar.

Táctica 2: Omisión (Omission)
=============================

**Definición:**
 Eliminar contenido presente en el original.

**Uso:**
 Para objetivo de **Simplificación**.

**Ejemplos:**

.. code-block:: latex

 % Original (LaTeX)
 \noindent
 Párrafo...

 \vspace{2cm}

.. code-block:: rst

 # Traducción con Omisión (RST)
 Párrafo...

 # Se omite \noindent (no semántico en RST)
 # Se omite \vspace (Sphinx maneja espaciado)

**Cuándo usar:**
 - Comandos puramente estilísticos (``\noindent``, ``\vspace``)
 - Contenido redundante
 - Elementos que RST/Sphinx manejan automáticamente

**Precaución:**
 NUNCA omitir contenido semántico.

Táctica 3: Sustitución (Substitution)
=====================================

**Definición:**
 Reemplazar un elemento por su equivalente.

**Uso:**
 Para **Domesticación** (mapeo LaTeX -> RST).

**Ejemplos:**

.. list-table::
 :widths: 45 45 10
 :header-rows: 1

 * - LaTeX
   - RST
   - Objetivo
 * - ``\textbf{x}``
   - ``**x**``
   - Domesticación
 * - ``\ref{label}``
   - ``:ref:`label```
   - Domesticación
 * - ``\cite{key}``
   - ``:cite:`key```
   - Domesticación

**Cuándo usar:**
 Casi siempre - es la táctica MÁS COMÚN.

Táctica 4: Cambio de Orden (Transposition)
==========================================

**Definición:**
 Reordenar elementos.

**Uso:**
 Para **Claridad** o **Domesticación**.

**Ejemplos:**

.. code-block:: latex

 % Original (LaTeX)
 Como se muestra en Figura~\ref{fig:resultado}, los datos...

 \begin{figure}
 % Figura está 2 páginas después
 \end{figure}

.. code-block:: rst

 # Traducción con Reordenamiento (RST)
 Como se muestra en :numref:`fig-resultado`, los datos...

 .. _fig-resultado:
 .. figure:: resultado.png

 # Figura CERCA de la referencia (mejor en HTML)

**Cuándo usar:**
 - Mover figuras/tablas cerca de referencias
 - Reorganizar para mejor flujo en HTML
 - Adaptar a convenciones del medio destino

Táctica 5: Especificación (Specification)
=========================================

**Definición:**
 Hacer más específico un elemento vago.

**Uso:**
 Para **Claridad**.

**Ejemplos:**

.. code-block:: latex

 % Original (vago)
 Como se mencionó antes...
 Ver [1]

.. code-block:: rst

 # Traducción especificada
 Como se mencionó en :ref:`seccion-introduccion`...
 Ver Smith (2020) :cite:`smith2020`

**Cuándo usar:**
 - Referencias vagas
 - Citas sin contexto
 - Pronombres ambiguos

Táctica 6: Generalización (Generalization)
==========================================

**Definición:**
 Hacer más general un elemento específico.

**Uso:**
 Para **Consistencia** (unificar variantes).

**Ejemplos:**

.. code-block:: latex

 % Capítulo 1
 \textbf{importante}

 % Capítulo 5
 \emph{importante} % Mismo uso, diferente comando

.. code-block:: rst

 # Traducción generalizada (consistente)
 **importante** # En ambos capítulos

**Cuándo usar:**
 - Unificar variantes sin diferencia semántica
 - Estandarizar terminología

Táctica 7: Explicación (Explicitation)
======================================

**Definición:**
 Hacer explícito lo implícito.

**Uso:**
 Para **Claridad**.

**Ejemplos:**

.. code-block:: latex

 % Original (implícito)
 El algoritmo tiene complejidad O(n log n).

.. code-block:: rst

 # Traducción explicada
 El algoritmo tiene complejidad :math:`O(n \log n)`, es decir,
 su tiempo de ejecución crece proporcionalmente a :math:`n \log n`
 donde :math:`n` es el tamaño de la entrada.

**Cuándo usar:**
 - Conceptos técnicos que pueden ser desconocidos
 - Notación matemática
 - Jerga del dominio

**Precaución:**
 Solo si la audiencia lo necesita. No sobre-explicar.

Táctica 8: Normalización (Normalization)
========================================

**Definición:**
 Estandarizar variaciones.

**Uso:**
 Para **Consistencia**.

**Ejemplos:**

.. code-block:: latex

 % Variaciones en el original
 base de datos
 BD
 database
 DB

.. code-block:: rst

 # Normalizado
 base de datos (primera mención)
 BD (menciones subsecuentes)

 # Nunca: database, DB (anglicismos)

**Cuándo usar:**
 - Terminología inconsistente
 - Variaciones de estilo
 - Convenciones locales vs internacionales

Táctica 9: Modulación (Modulation)
==================================

**Definición:**
 Cambiar perspectiva o punto de vista.

**Uso:**
 Para **Domesticación** (naturalización).

**Ejemplos:**

.. code-block:: latex

 % Original (voz pasiva, común en inglés técnico)
 The results were obtained by running...

.. code-block:: rst

 # Traducción modulada (voz activa, más natural en español)
 Obtuvimos los resultados ejecutando...

**Cuándo usar:**
 - Adaptación a convenciones del idioma destino
 - Naturalización de construcciones extrañas

Táctica 10: Compensación (Compensation)
=======================================

**Definición:**
 Recuperar pérdida de información en otro lugar.

**Uso:**
 Cuando traducción directa pierde matiz.

**Ejemplos:**

.. code-block:: latex

 % Original (juego de palabras intraducible)
 The server serves data to clients.

.. code-block:: rst

 # Traducción con compensación
 El servidor provee [#servidor]_ datos a los clientes.

 .. [#servidor] En inglés "server" significa tanto "servidor"
 como "el que sirve", jugando con el doble sentido.

**Cuándo usar:**
 - Juegos de palabras
 - Matices culturales
 - Información que se pierde en traducción

Táctica 11: Amplificación (Amplification)
=========================================

**Definición:**
 Expandir contenido comprimido.

**Uso:**
 Para **Claridad**.

**Ejemplos:**

.. code-block:: latex

 % Original (comprimido)
 API

.. code-block:: rst

 # Traducción amplificada
 API (Application Programming Interface, interfaz de programación
 de aplicaciones)

**Cuándo usar:**
 - Siglas no conocidas
 - Términos técnicos especializados
 - Referencias que necesitan contexto

Táctica 12: Condensación (Condensation)
=======================================

**Definición:**
 Comprimir contenido verboso.

**Uso:**
 Para **Simplificación**.

**Ejemplos:**

.. code-block:: latex

 % Original (verboso - 3 párrafos repitiendo lo mismo)
 Como se explicó anteriormente, el algoritmo...
 Retomando lo mencionado antes, el algoritmo...
 Recordando la explicación previa, el algoritmo...

.. code-block:: rst

 # Traducción condensada (1 párrafo)
 El algoritmo, como se explicó en :ref:`seccion-algoritmo`...

**Cuándo usar:**
 - Redundancia en el original
 - Verbosidad excesiva
 - Repeticiones innecesarias

**Precaución:**
 Preservar TODO el contenido semántico.

Táctica 13: Literalización (Literalization)
===========================================

**Definición:**
 Preservar forma exacta del original.

**Uso:**
 Cuando forma = contenido.

**Ejemplos:**

.. code-block:: latex

 % Original (código fuente)
 \begin{verbatim}
 def factorial(n):
 return 1 if n == 0 else n * factorial(n-1)
 \end{verbatim}

.. code-block:: rst

 # Traducción literal
 .. code-block:: python

 def factorial(n):
 return 1 if n == 0 else n * factorial(n-1)

**Cuándo usar:**
 - Código fuente
 - Ecuaciones matemáticas
 - Datos técnicos exactos
 - Ejemplos que deben replicarse exactamente

Táctica 14: Adaptación Cultural (Cultural Adaptation)
=====================================================

**Definición:**
 Adaptar referencias culturales.

**Uso:**
 En traducciones entre culturas diferentes.

**Ejemplos:**

.. code-block:: latex

 % Original (referencia cultural estadounidense)
 This is as American as apple pie.

.. code-block:: rst

 # Adaptación cultural (para audiencia española)
 Esto es tan español como la tortilla de patatas.

**Cuándo usar:**
 - Referencias culturales específicas
 - Idiomatismos
 - Ejemplos culturalmente ligados

**En ADT:**
 Menos relevante (documentación técnica es más universal).




Matriz de Decisión: Objetivos × Tácticas
========================================

Tabla de Compatibilidad
=======================

.. list-table::
 :widths: 20 15 15 15 15 20
 :header-rows: 1

 * - Táctica
   - Domesticación
   - Claridad
   - Consistencia
   - Simplificación
   - Uso Principal
 * - Adición
   - [WARNING]
   - [OK][OK][OK]
   - [WARNING]
   - [ERROR]
   - Claridad
 * - Omisión
   - [WARNING]
   - [ERROR]
   - [WARNING]
   - [OK][OK][OK]
   - Simplificación
 * - Sustitución
   - [OK][OK][OK]
   - [OK]
   - [OK]
   - [WARNING]
   - Domesticación
 * - Cambio orden
   - [OK]
   - [OK]
   - [WARNING]
   - [WARNING]
   - Domesticación
 * - Especificación
   - [WARNING]
   - [OK][OK][OK]
   - [WARNING]
   - [ERROR]
   - Claridad
 * - Generalización
   - [WARNING]
   - [ERROR]
   - [OK][OK][OK]
   - [OK]
   - Consistencia
 * - Explicación
   - [WARNING]
   - [OK][OK][OK]
   - [WARNING]
   - [ERROR]
   - Claridad
 * - Normalización
   - [OK]
   - [WARNING]
   - [OK][OK][OK]
   - [WARNING]
   - Consistencia
 * - Modulación
   - [OK][OK]
   - [WARNING]
   - [WARNING]
   - [WARNING]
   - Domesticación
 * - Compensación
   - [WARNING]
   - [OK]
   - [WARNING]
   - [ERROR]
   - Claridad
 * - Amplificación
   - [WARNING]
   - [OK][OK]
   - [WARNING]
   - [ERROR]
   - Claridad
 * - Condensación
   - [WARNING]
   - [WARNING]
   - [WARNING]
   - [OK][OK][OK]
   - Simplificación
 * - Literalización
   - [ERROR]
   - [OK]
   - [WARNING]
   - [ERROR]
   - Código/Ecuaciones
 * - Adapt. Cultural
   - [OK][OK]
   - [OK]
   - [WARNING]
   - [WARNING]
   - Domesticación

**Leyenda:**
- [OK][OK][OK] = Uso principal y frecuente
- [OK][OK] = Uso común
- [OK] = Uso ocasional
- [WARNING] = Uso posible pero raro
- [ERROR] = Generalmente incompatible




Proceso de Aplicación
=====================

Paso 1: Identificar Necesidad
=============================

.. code-block:: text

 ¿El método por defecto es suficiente?

 SI SÍ:
 -> Usar método por defecto
 -> Fin

 SI NO:
 -> Ir a Paso 2

Paso 2: Seleccionar Objetivo
============================

.. code-block:: text

 ¿QUÉ objetivo justifica la divergencia?

 [ ] Domesticación - Adaptar a RST/Sphinx
 [ ] Claridad - Hacer comprensible
 [ ] Consistencia - Resolver inconsistencias
 [ ] Simplificación - Reducir complejidad

 -> Seleccionar UNO (o máximo dos)

Paso 3: Elegir Táctica(s)
=========================

.. code-block:: text

 Según objetivo, consultar tabla de compatibilidad

 Para DOMESTICACIÓN -> Sustitución, Modulación
 Para CLARIDAD -> Adición, Especificación, Explicación
 Para CONSISTENCIA -> Normalización, Generalización
 Para SIMPLIFICACIÓN -> Omisión, Condensación

Paso 4: Aplicar Táctica
=======================

.. code-block:: text

 Aplicar táctica seleccionada

 Verificar:
 - ¿Se logró el objetivo?
 - ¿Se preservó contenido semántico?
 - ¿No se introdujeron nuevos problemas?

Paso 5: Documentar
==================

.. code-block:: rst

 .. note::
 **Decisión de traducción:**

 Objetivo: [Domesticación/Claridad/Consistencia/Simplificación]
 Táctica: [nombre de táctica]
 Razón: [explicación breve]




Ejemplos Integrados
===================

Ejemplo 1: Figura Lejana (Objetivo: Claridad)
=============================================

**Original (LaTeX):**

.. code-block:: latex

 Como muestra la Figura~\ref{fig:resultado}, los datos...

 % [100 líneas de texto]

 \begin{figure}
 \includegraphics{resultado.png}
 \caption{Resultado experimental}
 \label{fig:resultado}
 \end{figure}

**Problema:**
 Figura está muy lejos de la referencia (mala experiencia en HTML).

**Objetivo:**
 Claridad (lector ve figura cuando se menciona)

**Táctica:**
 Cambio de orden (mover figura cerca)

**Traducción (RST):**

.. code-block:: rst

 Como muestra :numref:`fig-resultado`, los datos...

 .. _fig-resultado:
 .. figure:: resultado.png
 :scale: 80%

 Resultado experimental

 % [Texto continúa aquí]

**Documentación:**

.. code-block:: rst

 .. note::
 **Decisión:** Figura movida cerca de primera referencia.
 Objetivo: Claridad. Táctica: Cambio de orden.

Ejemplo 2: Énfasis Inconsistente (Objetivo: Consistencia)
=========================================================

**Original (LaTeX):**

.. code-block:: latex

 % Capítulo 1
 Este punto es \textbf{importante}.

 % Capítulo 3
 Este punto es \emph{importante}. % Mismo uso semántico

**Problema:**
 Inconsistencia sin razón semántica.

**Objetivo:**
 Consistencia

**Táctica:**
 Generalización (unificar a un solo estilo)

**Traducción (RST):**

.. code-block:: rst

 # Capítulos 1 y 3
 Este punto es **importante**.

**Documentación:**

.. code-block:: rst

 .. note::
 **Decisión:** Original usa \textbf y \emph intercambiablemente
 para énfasis. Unificado a **énfasis** para consistencia.
 Objetivo: Consistencia. Táctica: Generalización.

Ejemplo 3: Espacio Vertical (Objetivo: Simplificación)
======================================================

**Original (LaTeX):**

.. code-block:: latex

 Párrafo 1...

 \vspace{3cm}

 Párrafo 2...

**Problema:**
 ``\vspace{}`` es puramente estilístico, no semántico.

**Objetivo:**
 Simplificación

**Táctica:**
 Omisión

**Traducción (RST):**

.. code-block:: rst

 Párrafo 1...

 Párrafo 2...

 # Sphinx maneja espaciado automáticamente

**Documentación:**

.. code-block:: rst

 .. note::
 **Decisión:** Omitidos \vspace (no semánticos).
 Sphinx maneja espaciado automáticamente.
 Objetivo: Simplificación. Táctica: Omisión.




Checklist de Aplicación
=======================

.. code-block:: text

 ANTES de divergir del método por defecto:

 [ ] ¿He intentado el método por defecto?
 [ ] ¿Hay un objetivo claro? (Domesticación/Claridad/Consistencia/Simplificación)
 [ ] ¿He seleccionado táctica apropiada?
 [ ] ¿La táctica es compatible con el objetivo?

 DESPUÉS de aplicar táctica:

 [ ] ¿Se logró el objetivo?
 [ ] ¿Se preservó contenido semántico?
 [ ] ¿Documenté la decisión?
 [ ] ¿Compiló sin errores?
 [ ] ¿Se ve bien en HTML?




Conclusión
==========

**Síntesis:**

- **4 Objetivos** claros para divergencias
- **14+ Tácticas** probadas y catalogadas
- **Matriz de compatibilidad** para guiar decisiones
- **Proceso sistemático** de 5 pasos
- **Documentación** de decisiones importantes

**Resultado:**

 Traducciones consistentes, justificadas, y mejorables.




Referencias
===========

- :doc:`principios_fundamentales`
- :doc:`_metodologias/metodo_por_defecto`
- :doc:`/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS`
- Micheli, D. (2014). Translation Technique in Peshitta Zechariah




**Versión:** 1.0
**Fecha:** 2026-01-27
**Estado:** Aprobado - Base táctica del proyecto
