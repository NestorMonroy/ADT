
Método por Defecto de ADT
=========================

:Categoría: Metodologías
:Ubicación: 01_fundamentos/_metodologias/
:Base: Método Peshitta (Micheli, 2014)
:Aplicación: Workflow estándar de traducción

.. contents:: Contenido
 :depth: 2
 :local:







Introducción
============

El **Método por Defecto** es el procedimiento estándar que se aplica a TODA
traducción en ADT, a menos que haya razón específica para desviarse.

**Inspiración:**
 Basado en el análisis de Micheli (2014) del método de traducción en
 Peshitta Zacarías, adaptado a traducción técnica LaTeX->RST.




Los Tres Pilares del Método
===========================

1. Segmentación




**Definición:**
 El nivel de granularidad al que trabajamos.

**En ADT:**

.. code-block:: text

 NIVEL PRIMARIO: Sección

 Procesamos el documento sección por sección, preservando
 la estructura jerárquica del original.

**Jerarquía de segmentación:**

.. list-table::
 :header-rows: 1
 :widths: 20 40 40

 * - Nivel
   - LaTeX
   - RST
 * - **Libro**
   - Todo el documento
   - Todo el documento
 * - **Capítulo**
   - ``\chapter{}``
   - Archivo .rst separado
 * - **Sección** [STAR]
   - ``\section{}``
   - Título con ``====``
 * - **Subsección**
   - ``\subsection{}``
   - Título con ``----``
 * - **Párrafo**
   - Bloques de texto
   - Bloques de texto
 * - **Frase**
   - Oraciones
   - Oraciones
 * - **Palabra**
   - Términos individuales
   - Términos individuales




**Decisión de segmentación:**

.. important::
 Trabajamos a nivel de **SECCIÓN**, pero respetamos la jerarquía completa.

 NO traducimos palabra por palabra NI documento completo de una vez.




**Ejemplo:**

.. code-block:: latex

 \section{Introducción}
 Párrafo 1...
 Párrafo 2...
 \subsection{Contexto}
 Párrafo 3...

**Procesamiento:**

1. Identificar sección "Introducción"
2. Traducir contenido de sección
3. Identificar subsección "Contexto"
4. Traducir contenido de subsección
5. etc.

2. Rendición




**Definición:**
 Cómo traducimos cada elemento dentro de la segmentación.

**En ADT:**

.. code-block:: text

 NIVEL PRIMARIO: Comando LaTeX

 Mapeamos cada comando LaTeX a su equivalente semántico en RST,
 elemento por elemento.

**Tabla de rendición básica:**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - LaTeX
   - RST
   - Signifié
 * - ``\textbf{}``
   - ``**...**``
   - Énfasis fuerte
 * - ``\emph{}``
   - ``*...*``
   - Énfasis moderado
 * - ``\texttt{}``
   - ````...````
   - Código inline
 * - ``\textit{}``
   - ``*...*``
   - Itálica
 * - ``\ref{}``
   - ``:ref:``
   - Referencia
 * - ``\cite{}``
   - ``:cite:``
   - Citación




**Decisión de rendición:**

.. important::
 Nivel de COMANDO: Cada comando LaTeX se mapea a equivalente RST.

 NO copiamos texto literal NI reescribimos completamente.




3. Preferencia




**Definición:**
 Cuando hay conflicto entre preservar forma vs contenido, ¿qué elegimos?

**En ADT:**

.. code-block:: text

 PREFERENCIA: Signifié (CONTENIDO) sobre Signifiant (FORMA)

 Preservamos la FUNCIÓN semántica, adaptamos la SINTAXIS.

**Ejemplos de aplicación:**

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - Situación
   - Opción A (Signifiant)
   - Opción B (Signifié) [OK]
 * - Lista numerada
   - ``\begin{enumerate}``
   - ``1. 2. 3.``
 * - Énfasis
   - ``\textbf{}``
   - ``**``
 * - Espaciado
   - ``\vspace{}`` literal
   - Confiar en RST
 * - Referencia
   - ``\ref{label}``
   - ``:ref:label``




**Decisión de preferencia:**

.. important::
 En caso de duda: **Preservar contenido semántico**, adaptar forma.

 Excepción: Código fuente (donde forma = contenido).






Aplicación del Método
=====================

Paso 1: Análisis del Segmento
=============================

**Para cada sección LaTeX:**

1. Identificar estructura jerárquica
2. Detectar comandos especiales
3. Identificar elementos que requieren atención especial

**Checklist:**

.. code-block:: text

 [ ] ¿Qué nivel de sección es? (section, subsection, etc.)
 [ ] ¿Hay figuras/tablas?
 [ ] ¿Hay ecuaciones matemáticas?
 [ ] ¿Hay código fuente?
 [ ] ¿Hay referencias cruzadas?
 [ ] ¿Hay citas bibliográficas?

Paso 2: Aplicar Rendición Estándar
==================================

**Mapeo automático:**

.. code-block:: text

 Para cada comando LaTeX:
 1. Buscar en tabla de rendición
 2. Si existe mapeo directo -> aplicar
 3. Si NO existe -> marcar para revisión manual

**Ejemplo:**

.. code-block:: latex

 % LaTeX
 \textbf{importante}

.. code-block:: rst

 # RST (aplicando rendición estándar)
 **importante**

Paso 3: Verificar Preferencia
=============================

**Para cada decisión:**

.. code-block:: text

 ¿El mapeo preserva el Signifié (contenido)?

 SI SÍ:
 [OK] Mapeo correcto

 SI NO:
 [WARNING] Necesita táctica especial
 -> Ver Objetivos de Traducción

Paso 4: Validación del Segmento
===============================

**Después de traducir sección:**

1. **Compilar:** ``make html``
2. **Revisar visual:** ¿Se ve correcto en HTML?
3. **Verificar semántica:** ¿Preserva el contenido original?
4. **Comprobar enlaces:** ¿Referencias cruzadas funcionan?




Cuándo Desviarse del Método por Defecto
=======================================

El método por defecto se aplica en el 80-90% de los casos.

**Situaciones que requieren divergencia:**

Objetivo 1: Domesticación
=========================

**Cuándo:** El original usa construcciones que no existen en RST

**Ejemplo:**

.. code-block:: latex

 % LaTeX: Comando custom
 \mycommand{contenido}

**Divergencia:** Interpretar función semántica y mapear a RST apropiado

Objetivo 2: Claridad
====================

**Cuándo:** El original es ambiguo o confuso

**Ejemplo:**

.. code-block:: latex

 % LaTeX: Referencia vaga
 Como se mencionó anteriormente...

**Divergencia:** Agregar referencia explícita

.. code-block:: rst

 # RST
 Como se mencionó en :ref:`seccion-anterior`...

Objetivo 3: Consistencia
========================

**Cuándo:** El original tiene inconsistencias

**Ejemplo:**

.. code-block:: latex

 % Capítulo 1: usa \textbf{}
 \textbf{importante}

 % Capítulo 5: usa \emph{} para lo mismo
 \emph{importante}

**Divergencia:** Unificar a un solo estilo

Objetivo 4: Simplificación
==========================

**Cuándo:** El original tiene complejidad innecesaria

**Ejemplo:**

.. code-block:: latex

 % LaTeX: Complicado
 \begin{center}\textbf{Título}\end{center}

**Divergencia:** Simplificar

.. code-block:: rst

 # RST: Simple
 **Título**




Plantilla de Aplicación
=======================

**Template para cada sección:**

.. code-block:: rst

 # 1. ANÁLISIS
 Sección: [nombre]
 Nivel: [section/subsection/subsubsection]
 Elementos especiales: [figuras/tablas/ecuaciones/código]

 # 2. RENDICIÓN ESTÁNDAR
 [Aplicar tabla de mapeo comando por comando]

 # 3. VERIFICAR PREFERENCIA
 ¿Signifié preservado? [SÍ/NO]
 Si NO: ¿Qué táctica aplicar? [...]

 # 4. VALIDACIÓN
 [ ] Compila sin errores
 [ ] HTML se ve correcto
 [ ] Semántica preservada
 [ ] Enlaces funcionan




Casos de Uso
============

Caso 1: Sección Simple
======================

**Input LaTeX:**

.. code-block:: latex

 \section{Introducción}
 Este es un texto \textbf{importante} con \emph{énfasis}.

**Aplicación del método:**

1. **Segmentación:** Sección "Introducción"
2. **Rendición:**
 - ``\section{}`` -> Título con ``====``
 - ``\textbf{}`` -> ``**...**``
 - ``\emph{}`` -> ``*...*``

3. **Preferencia:** Signifié preservado [OK]

**Output RST:**

.. code-block:: rst

 Introducción
 ============

 Este es un texto **importante** con *énfasis*.

Caso 2: Sección con Figura
==========================

**Input LaTeX:**

.. code-block:: latex

 \section{Resultados}
 Ver Figura~\ref{fig:resultado}.

 \begin{figure}
 \includegraphics{imagen.png}
 \caption{Resultado}
 \label{fig:resultado}
 \end{figure}

**Aplicación del método:**

1. **Segmentación:** Sección "Resultados"
2. **Rendición:**
 - ``\section{}`` -> Título
 - ``\ref{}`` -> ``:ref:``
 - ``figure`` -> ``.. figure::``

3. **Preferencia:** Signifié (referencia funciona)

**Output RST:**

.. code-block:: rst

 Resultados
 ===========

 Ver :numref:`fig-resultado`.

 .. _fig-resultado:
 .. figure:: imagen.png

 Resultado




Métricas de Calidad
===================

**¿Cómo saber si aplicamos bien el método?**

Métrica 1: Tasa de Compilación
==============================

.. code-block:: text

 Objetivo: 100% de las secciones compilan sin errores

Métrica 2: Preservación Semántica
=================================

.. code-block:: text

 Verificar: ¿El HTML resultante expresa el mismo contenido?

 Método: Revisión manual o automática

Métrica 3: Naturalidad en RST
=============================

.. code-block:: text

 ¿El RST generado es idiomático?
 ¿O parece "traducción automática"?

Métrica 4: Tasa de Divergencias
===============================

.. code-block:: text

 Objetivo: <20% de divergencias del método por defecto

 Si >20%: Revisar si método por defecto es apropiado




Conclusión
==========

**Síntesis:**

El método por defecto de ADT consta de:





1. **Segmentación:** Nivel de sección
2. **Rendición:** Nivel de comando
3. **Preferencia:** Signifié (contenido) sobre Signifiant (forma)

**Aplicación:**

.. code-block:: text

 Para el 80-90% de las traducciones:
 -> Aplicar método por defecto
 -> Validar
 -> Listo

 Para el 10-20% restante:
 -> Identificar objetivo que requiere divergencia
 -> Aplicar táctica apropiada
 -> Documentar decisión
 -> Validar

**Valor:**

Este método proporciona:




- [OK] Consistencia entre traducciones
- [OK] Eficiencia (no reinventar cada vez)
- [OK] Calidad predecible
- [OK] Base para mejora iterativa




Referencias
===========

- :doc:`/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS`
- :doc:`/docs_maestros/SINTESIS_METODOLOGICA_ADT`
- :doc:`../_fundamentos_conceptuales/signifiant_vs_signifie`
- :doc:`objetivos_tacticas`




**Versión:** 1.0
**Fecha:** 2026-01-27
**Estado:** Aprobado
