.. _latex_rst_equivalencias:

===============================================
Equivalencias LaTeX -> reStructuredText
===============================================

:Tipo: Tabla de Referencia
:Aplicabilidad: Traducción de documentación LaTeX a RST
:Base: Patrones identificados en traducción de arc42
:Última actualización: 2026-01-28

.. contents:: Contenido
 :depth: 3
 :local:

----

Introducción
============

Esta tabla provee **equivalencias directas** entre construcciones LaTeX y reStructuredText.

**Uso:**

.. code-block:: text

 1. Identifica construcción LaTeX en original
 2. Busca en esta tabla
 3. Usa equivalente RST en traducción
 4. Compila para verificar

**Nota sobre Signifiant vs Signifié:**

.. important::
 El objetivo es preservar el **Signifié** (significado), no el **Signifiant** (forma).

 LaTeX: ``\textbf{importante}`` -> Signifié: "énfasis fuerte"
 RST: ``**importante**`` -> Mismo Signifié, diferente Signifiant

----

Categoría 1: Estructura del Documento
======================================

1.1 Secciones y Títulos
------------------------

.. list-table::
 :header-rows: 1
 :widths: 40 40 20

 * - **LaTeX**
   - **reStructuredText**
   - **Nivel**
 * - ``\part{Parte}``
   - ::

 #######
 Parte
 #######
   - 0
 * - ``\chapter{Capítulo}``
   - ::

 *********
 Capítulo
 *********
   - 1
 * - ``\section{Sección}``
   - ::

 =========
 Sección
 =========
   - 2
 * - ``\subsection{Subsección}``
   - ::

 Subsección
 ==========
   - 3
 * - ``\subsubsection{Sub-sub}``
   - ::

 Sub-sub
 -------
   - 4

**Ejemplo completo:**

.. code-block:: latex

 % LaTeX
 \section{Arquitectura del Sistema}

 \subsection{Componentes Principales}

.. code-block:: rst

 # RST
 ============================
 Arquitectura del Sistema
 ============================

 Componentes Principales
 ========================

1.2 Listas
----------

**Listas No Numeradas:**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ::

 \begin{itemize}
 \item Primero
 \item Segundo
 \end{itemize}
   - ::

   - Primero
   - Segundo

**Listas Numeradas:**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ::

 \begin{enumerate}
 \item Primero
 \item Segundo
 \end{enumerate}
   - ::

 1. Primero
 2. Segundo

1.3 Tablas
----------

**Tabla Simple:**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ::

 \begin{tabular}{|l|c|r|}
 \hline
 Izq & Centro & Der \\
 \hline
 A & B & C \\
 \hline
 \end{tabular}
   - ::

 .. list-table::
 :header-rows: 1

 * - Izq
   - Centro
   - Der
 * - A
   - B
   - C

----

Categoría 2: Formato de Texto
==============================

2.1 Énfasis y Formato
----------------------

.. list-table::
 :header-rows: 1
 :widths: 40 40 20

 * - **LaTeX**
   - **reStructuredText**
   - **Significado**
 * - ``\textbf{negrita}``
   - ``**negrita**``
   - Énfasis fuerte
 * - ``\emph{énfasis}``
   - ``*énfasis*``
   - Énfasis (cursiva)
 * - ``\texttt{código}``
   - ````código````
   - Monoespaciado

2.2 Código y Verbatim
---------------------

**Bloques de Código:**

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ::

 \begin{verbatim}
 def funcion():
 return True
 \end{verbatim}
   - ::

 .. code-block:: python

 def funcion():
 return True

----

Categoría 3: Referencias y Enlaces
===================================

3.1 Referencias Cruzadas
-------------------------

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ::

 \label{sec:intro}
 \section{Introducción}
   - ::

 .. _sec_intro:

 Introducción
 ============
 * - ::

 Ver sección \ref{sec:intro}
   - ::

 Ver :ref:`sec_intro`

3.2 Enlaces URL
---------------

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ``\url{https://example.com}``
   - ``https://example.com``
 * - ``\href{https://example.com}{Texto}``
   - ```Texto <https://example.com>`_``

----

Categoría 4: Figuras e Imágenes
================================

4.1 Figuras con Caption
-----------------------

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ::

 \begin{figure}[h]
 \includegraphics{img.png}
 \caption{Descripción}
 \label{fig:nombre}
 \end{figure}
   - ::

 .. _fig_nombre:

 .. figure:: img.png
 :align: center

 Descripción

----

Categoría 5: Matemáticas
=========================

5.1 Modo Matemático
--------------------

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - ``$E = mc^2$``
   - ``:math:`E = mc^2```
 * - ::

 \[
 E = mc^2
 \]
   - ::

 .. math::

 E = mc^2

----

Categoría 6: Bloques Especiales
================================

6.1 Notas y Advertencias
-------------------------

.. list-table::
 :header-rows: 1
 :widths: 50 50

 * - **LaTeX**
   - **reStructuredText**
 * - Sin equivalente directo
   - ::

 .. note::
 Esto es una nota
 * - Sin equivalente directo
   - ::

 .. warning::
 Advertencia

----

Guía de Traducción Sistemática
===============================

Proceso Paso a Paso
-------------------

.. code-block:: text

 PASO 1: Identificar estructura
 [ ] Contar secciones
 [ ] Identificar listas
 [ ] Identificar tablas

 PASO 2: Traducir secciones
 [ ] Convertir \section{} a títulos RST
 [ ] Verificar longitud de subrayado

 PASO 3: Traducir contenido
 [ ] Convertir formato (negrita, cursiva)
 [ ] Convertir listas
 [ ] Convertir tablas

 PASO 4: Verificar
 [ ] Compilar con make html
 [ ] Corregir errores

----

Herramientas de Conversión
===========================

Pandoc (Recomendado)
--------------------

.. code-block:: bash

 # Convertir LaTeX a RST
 pandoc input.tex -f latex -t rst -o output.rst

.. warning::
 Los conversores son punto de partida, no resultado final.
 Siempre requieren revisión manual.

----

Errores Comunes
===============

Error 1: Título Mal Subrayado
------------------------------

.. code-block:: text

 [ERROR] INCORRECTO:
 ===============
 Título Muy Largo
 ===============

 [OK] CORRECTO:
 =========================
 Título Muy Largo
 =========================

----

.. seealso::
 * :doc:`../../01_fundamentos/_fundamentos_conceptuales/signifiant_vs_signifie`
 * :doc:`../../07_guias_uso/guia_rapida`
