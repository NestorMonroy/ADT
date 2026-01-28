.. meta::
   :artefacto: PROC_002_Workflow_General
   :tipo: Procedimiento
   :dominio: procedimientos
   :estado: Aprobado
   :version: 1.1.0
   :fecha_creacion: 2026-01-27
   :ultimo_cambio: 2026-01-27
   :autor: Equipo ADT
   :clasificacion: Interno

.. _proc-002-workflow-general:

=============================
Workflow General de Traducción
=============================

:Versión: 1.1.0
:Categoría: Procedimientos
:Ubicación: 02_procedimientos/
:Tipo: Procedimiento Operativo Principal
:Base: Método Peshitta + ADT

**Registro de Cambios:**

- **v1.1.0 (2026-01-27):** MINOR - Corrección de estructura biblioteca/, integración con Guía Metodológica Clasificación
- **v1.0.0 (2026-01-27):** MAJOR - Versión inicial

.. contents:: Contenido
   :depth: 3
   :local:

----

Introducción
============

Este documento describe el **workflow completo** para traducir documentación
técnica de LaTeX a RST/Sphinx usando la metodología ADT.

**Audiencia:**
   Cualquier persona que vaya a realizar traducciones en el proyecto ADT.

**Prerrequisitos:**
   - Haber leído :doc:`/01_fundamentos/principios_fundamentales`
   - Familiaridad con LaTeX y RST básico
   - Sphinx instalado y configurado

----

Integración con Biblioteca y Clasificación
===========================================

**IMPORTANTE:** Este workflow trabaja con la estructura de **biblioteca/** y utiliza
la **Guía Metodológica de Clasificación Documental**.

Estructura Base
---------------

.. code-block:: text

   /tmp/ADT/source/biblioteca/
   ├── _metadata_biblioteca/           # Guías de clasificación
   │   ├── META_BIB_001_Sistema_Clasificacion_1_0_0.rst
   │   ├── META_BIB_002_Guia_Organizacion_Jerarquica_1_0_0.rst
   │   └── META_BIB_003_Esquema_Codificacion_1_0_0.rst
   │
   ├── informatica/                    # Categoría
   │   └── programacion/               # Subcategoría
   │       └── full_stack/             # Especialidad
   │           └── Nombre_Libro/       # Libro completo
   │               ├── metadata_libro.rst
   │               ├── index.rst
   │               ├── glosario_acumulativo.rst
   │               └── nombre_capitulo/    # Sin números
   │                   ├── original/
   │                   ├── traduccion/
   │                   ├── glosario_capitulo.rst
   │                   ├── notas_traduccion.rst
   │                   └── figuras/

Sistema de Clasificación
-------------------------

**Código:** CATEGORÍA.SUBCATEGORÍA.ESPECIALIDAD.NÚMERO

**Ejemplos:**

- **INF.PRG.FST.001** = Informática > Programación > Full-Stack > Libro #1
- **ING.SIS.UML.002** = Ingeniería > Sistemas > UML > Libro #2
- **CIE.BIO.SYS.001** = Ciencias > Biología > Sistemas > Libro #1

**Documentos de Referencia:**

- :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT` (sección 10)
- :doc:`/docs_maestros/ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta`
- :doc:`/biblioteca/_metadata_biblioteca/META_BIB_001_Sistema_Clasificacion_1_0_0`

----

Visión General del Workflow
============================

Diagrama de Flujo
-----------------

.. code-block:: text

   WORKFLOW ADT - 7 FASES
   ═══════════════════════════════════════════════════════════
   
   FASE 1: PREPARACIÓN
   ├─ Análisis del documento fuente
   ├─ Configuración del entorno
   └─ Planificación de la traducción
   
   FASE 2: ANÁLISIS ESTRUCTURAL
   ├─ Identificar estructura jerárquica
   ├─ Mapear elementos especiales
   └─ Detectar inconsistencias
   
   FASE 3: TRADUCCIÓN INICIAL (Método por Defecto)
   ├─ Segmentación: Nivel de sección
   ├─ Rendición: Comando por comando
   └─ Preferencia: Signifié sobre Signifiant
   
   FASE 4: APLICACIÓN DE TÁCTICAS
   ├─ Identificar objetivos (Domesticación, Claridad, etc.)
   ├─ Aplicar tácticas apropiadas
   └─ Documentar decisiones
   
   FASE 5: VALIDACIÓN
   ├─ Compilar Sphinx (make html)
   ├─ Verificar preservación semántica
   └─ Revisar calidad visual
   
   FASE 6: REVISIÓN Y MEJORA
   ├─ Revisar enlaces y referencias
   ├─ Optimizar redacción
   └─ Aplicar feedback
   
   FASE 7: PUBLICACIÓN
   ├─ Compilación final
   ├─ Control de calidad
   └─ Despliegue

Tiempo Estimado
---------------

**Por capítulo de libro** (en estructura biblioteca/):

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Fase
     - Tiempo
     - Observaciones
   * - Preparación
     - 15-30 min
     - Una vez por libro completo
   * - Análisis
     - 5-10 min
     - Por capítulo
   * - Traducción Inicial
     - 20-40 min
     - Depende de complejidad del capítulo
   * - Aplicación Tácticas
     - 10-20 min
     - Si es necesario
   * - Validación
     - 5-10 min
     - Por capítulo
   * - Revisión
     - 10-15 min
     - Por capítulo
   * - Publicación
     - 15-30 min
     - Al completar libro completo

**Total por capítulo:** ~70-130 min (1-2 horas)

**Total por libro típico (10-15 capítulos):** 15-30 horas

----

FASE 1: Preparación
===================

Paso 1.1: Análisis del Documento Fuente y Clasificación
---------------------------------------------------------

**Objetivo:**
   Entender qué vamos a traducir y clasificarlo según la Guía Metodológica.

**Tareas:**

1. **Leer el documento fuente completo** (o capítulo)
   
   .. code-block:: bash
   
      # Abrir y leer el documento original
      less documento_original.pdf

2. **Clasificar el documento según Guía Metodológica:**
   
   Ver: :doc:`/biblioteca/_metadata_biblioteca/META_BIB_001_Sistema_Clasificacion`
   
   .. code-block:: text
   
      [ ] Categoría Principal (informatica/ingenieria/ciencias)
      [ ] Subcategoría (programacion/sistemas/biologia)
      [ ] Especialidad (full_stack/python/uml)
      [ ] Código de clasificación (ej: INF.PRG.FST.001)

3. **Identificar características del contenido:**
   
   .. code-block:: text
   
      [ ] Número de capítulos
      [ ] ¿Tiene figuras? ¿Cuántas?
      [ ] ¿Tiene tablas? ¿Cuántas?
      [ ] ¿Tiene ecuaciones matemáticas?
      [ ] ¿Tiene código fuente?
      [ ] ¿Tiene referencias bibliográficas?
      [ ] ¿Usa paquetes especiales LaTeX?
      [ ] ¿Tiene comandos custom (\newcommand)?

4. **Evaluar complejidad:**
   
   - **Baja:** Solo texto, secciones, énfasis básico
   - **Media:** + figuras, tablas, ecuaciones simples
   - **Alta:** + código, ecuaciones complejas, paquetes custom

**Ejemplo de Clasificación:**

.. code-block:: text

   Libro: "Modern Full-Stack Development" (Zammetti, 2024)
   
   Categoría: informatica/
   Subcategoría: programacion/
   Especialidad: full_stack/
   Código: INF.PRG.FST.001
   
   Ubicación final:
   biblioteca/informatica/programacion/full_stack/
   └── Modern_Full_Stack_Development_Zammetti_2ed/

Paso 1.2: Configuración de Estructura en Biblioteca
----------------------------------------------------

**Objetivo:**
   Crear estructura correcta en ``biblioteca/`` según clasificación.

**Tareas:**

1. **Crear estructura base del libro:**
   
   Ver: :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT` sección 10
   
   .. code-block:: bash
   
      # Ejemplo: Libro Full-Stack Development
      cd /tmp/ADT/source/biblioteca
      
      # Crear jerarquía según clasificación
      mkdir -p informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed
      
      cd informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed
      
      # Crear archivos base del libro
      touch metadata_libro.rst
      touch index.rst
      touch glosario_acumulativo.rst

2. **Crear estructura para el capítulo:**
   
   **Importante:** Sin números en nombres de carpeta (cumple NOM_001)
   
   .. code-block:: bash
   
      # Nombre descriptivo del capítulo (SIN número)
      mkdir -p server_side_action_node_npm/{original,traduccion,figuras}
      
      # Crear archivos del capítulo
      touch server_side_action_node_npm/glosario_capitulo.rst
      touch server_side_action_node_npm/notas_traduccion.rst

3. **Copiar/Convertir recursos originales:**
   
   .. code-block:: bash
   
      # Copiar PDF/LaTeX original
      cp ~/original/chapter_01.pdf server_side_action_node_npm/original/
      
      # Copiar figuras del capítulo
      cp ~/original/figures/*.{png,jpg} server_side_action_node_npm/figuras/
      
      # Si hay PDFs en figuras, convertir a PNG
      cd server_side_action_node_npm/figuras
      for f in *.pdf; do
          convert "$f" "${f%.pdf}.png"
      done

4. **Crear metadata del libro:**
   
   .. code-block:: bash
   
      # Editar metadata_libro.rst
      cat > metadata_libro.rst << 'EOF'
      .. meta::
         :libro_id: LIB_INF_FST_001
         :tipo: Libro_Tecnico
         :estado: En_Traduccion
         :progreso: 0%
         :clasificacion: INF.PRG.FST.001
      
      ========================================
      Modern Full-Stack Development (2nd Ed)
      ========================================
      
      Título Original
         Modern Full-Stack Development
      
      Autor
         Frank Zammetti
      
      Editorial
         Apress
      
      Año
         2024
      
      Clasificación
         INF.PRG.FST.001
         (Informática > Programación > Full-Stack)
      EOF

**Estructura Resultante:**

.. code-block:: text

   biblioteca/informatica/programacion/full_stack/
   └── Modern_Full_Stack_Development_Zammetti_2ed/
       ├── metadata_libro.rst
       ├── index.rst
       ├── glosario_acumulativo.rst
       │
       └── server_side_action_node_npm/      # Capítulo 1
           ├── original/
           │   └── chapter_01.pdf
           ├── traduccion/
           │   └── capitulo_01.rst          # A crear en FASE 3
           ├── glosario_capitulo.rst
           ├── notas_traduccion.rst
           └── figuras/
               ├── fig_01_01.png
               └── fig_01_02.png

5. **Verificar configuración Sphinx:**
   
   Asegurar que ``conf.py`` tiene extensiones necesarias:
   
   .. code-block:: python
   
      extensions = [
          'sphinx.ext.autodoc',
          'sphinx.ext.mathjax',        # Para ecuaciones
          'sphinx.ext.napoleon',
          'sphinx.ext.viewcode',
          'sphinxcontrib.bibtex',      # Para bibliografía
      ]

Paso 1.3: Planificación
------------------------

**Objetivo:**
   Decidir estrategia de traducción.

**Decisiones clave:**

1. **¿Modo 1 (Alta Fidelidad) o Modo 2 (Marcado Visual)?**
   
   .. list-table::
      :widths: 50 50
      :header-rows: 1
   
      * - Modo 1: Alta Fidelidad
        - Modo 2: Marcado Visual
      * - Preserva estructura original
        - Añade marcadores visuales
      * - Mínimas adaptaciones
        - Más adaptaciones para claridad
      * - Para: Libros formales, papers
        - Para: Tutoriales, material didáctico

2. **¿Qué objetivos son prioritarios?**
   
   .. code-block:: text
   
      Prioridad Alta:
      [ ] Domesticación (siempre)
      [ ] Claridad (si audiencia es amplia)
      [ ] Consistencia (si original es inconsistente)
      [ ] Simplificación (si original es verboso)

3. **¿Traducir todo o por secciones?**
   
   **Recomendación:** Sección por sección, compilando frecuentemente.

----

FASE 2: Análisis Estructural
=============================

Paso 2.1: Identificar Jerarquía y Ubicación en Biblioteca
-----------------------------------------------------------

**Objetivo:**
   Mapear estructura del documento y planificar ubicación en biblioteca.

**Proceso:**

1. **Extraer estructura del documento:**
   
   .. code-block:: bash
   
      # Para LaTeX: ver estructura de capítulos
      grep -E '\\(chapter|section|subsection)' original.tex
      
      # Para PDF: revisar tabla de contenidos

2. **Crear mapa jerárquico del libro:**
   
   .. code-block:: text
   
      Libro: Modern Full-Stack Development
      ├─ Chapter 01: Server-Side Action: Node and NPM
      │  ├─ Sección 1.1: Setting Up Node
      │  ├─ Sección 1.2: Working with NPM
      │  └─ Sección 1.3: Building First Server
      ├─ Chapter 02: Advanced Node and NPM
      │  ├─ Sección 2.1: Async Programming
      │  └─ Sección 2.2: Modules and Packages
      └─ Chapter 03: Client-Side Adventures: React
         └─ Sección 3.1: JSX Fundamentals

3. **Planificar nombres de carpetas (sin números, descriptivos):**
   
   Ver: :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT` sección 10.2
   
   .. code-block:: text
   
      Capítulo Original → Nombre Carpeta (snake_case, sin números)
      ═══════════════════════════════════════════════════════════
      Chapter 01: Server-Side Action  → server_side_action_node_npm/
      Chapter 02: Advanced Node       → advanced_node_npm/
      Chapter 03: Client-Side React   → client_side_react/
      Chapter 04: Advanced React      → advanced_react/
      Chapter 05: TypeScript          → typescript_foundation/
      Chapter 12: Docker              → docker_deployment/

4. **Verificar clasificación y ubicación:**
   
   .. code-block:: text
   
      Clasificación: INF.PRG.FST.001
      
      Ubicación completa:
      biblioteca/
         informatica/              # Categoría
            programacion/          # Subcategoría
               full_stack/         # Especialidad
                  Modern_Full_Stack_Development_Zammetti_2ed/  # Libro
                     ├── metadata_libro.rst
                     ├── index.rst
                     ├── server_side_action_node_npm/
                     ├── advanced_node_npm/
                     ├── client_side_react/
                     └── ... (otros capítulos)

Paso 2.2: Mapear Elementos Especiales
--------------------------------------

**Objetivo:**
   Identificar elementos que requieren atención especial.

**Checklist:**

.. code-block:: text

   FIGURAS:
   [ ] Listar todas las figuras
   [ ] Verificar que imágenes existen
   [ ] Planificar conversión si es necesario
   
   TABLAS:
   [ ] Identificar tipo (simple/compleja)
   [ ] Planificar formato RST apropiado
   
   ECUACIONES:
   [ ] Verificar compatibilidad con MathJax
   [ ] Identificar ecuaciones numeradas vs inline
   
   CÓDIGO:
   [ ] Identificar lenguaje
   [ ] Verificar si hay syntax highlighting
   
   REFERENCIAS:
   [ ] Listar \ref{} y planificar :ref:
   [ ] Listar \cite{} y verificar .bib
   
   COMANDOS CUSTOM:
   [ ] Identificar \newcommand
   [ ] Planificar equivalente RST/Sphinx

Paso 2.3: Detectar Inconsistencias
-----------------------------------

**Objetivo:**
   Identificar problemas del original que corregiremos.

**Buscar:**

1. **Terminología inconsistente:**
   
   .. code-block:: bash
   
      # Buscar variaciones del mismo término
      grep -i "base de datos\|BD\|database" original.tex

2. **Estilos de énfasis variados:**
   
   .. code-block:: bash
   
      # ¿Usa \textbf y \emph para lo mismo?
      grep -E '\\(textbf|emph)' original.tex

3. **Referencias inconsistentes:**
   
   .. code-block:: bash
   
      # Buscar diferentes estilos de referencia
      grep -E '(ver|véase|como se mostró|antes)' original.tex

**Documentar:**

.. code-block:: rst

   .. note::
      **Inconsistencias detectadas:**
      
      1. Términos: "base de datos" vs "BD" usados sin patrón
         → Decisión: Unificar a "base de datos" (primera vez) + BD
      
      2. Énfasis: \textbf y \emph usados indistintamente
         → Decisión: \textbf → **, \emph → *
      
      3. Referencias: Algunas con \ref, otras textuales
         → Decisión: Todas con :ref: explícito

----

FASE 3: Traducción Inicial (Método por Defecto)
================================================

Paso 3.1: Segmentación
-----------------------

**Nivel de trabajo:** CAPÍTULO (dentro de biblioteca/)

**Proceso:**

1. **Seleccionar un capítulo completo:**
   
   .. code-block:: text
   
      # Estructura del capítulo en biblioteca/
      biblioteca/.../Nombre_Libro/
         └── server_side_action_node_npm/    # Capítulo completo
             ├── original/
             │   └── chapter_01.pdf
             ├── traduccion/
             │   └── capitulo_01.rst         # A crear aquí
             ├── glosario_capitulo.rst
             ├── notas_traduccion.rst
             └── figuras/

2. **NO traducir:**
   - Todo el libro de una vez (demasiado)
   - Palabra por palabra (muy granular)
   - Solo títulos (muy superficial)

3. **SÍ traducir:**
   - Capítulo completo con todas sus secciones
   - Preservando estructura jerárquica
   - Creando archivo en ``traduccion/capitulo_XX.rst``

Paso 3.2: Rendición (Comando por Comando)
------------------------------------------

**Nivel de mapeo:** COMANDO LaTeX → ELEMENTO RST

**Tabla de rendición básica:**

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - LaTeX
     - RST
     - Notas
   * - ``\section{X}``
     - | ``X``
       | ``===``
     - Nivel 1
   * - ``\subsection{X}``
     - | ``X``
       | ``---``
     - Nivel 2
   * - ``\subsubsection{X}``
     - | ``X``
       | ``~~~``
     - Nivel 3
   * - ``\textbf{X}``
     - ``**X**``
     - Énfasis fuerte
   * - ``\emph{X}``
     - ``*X*``
     - Énfasis moderado
   * - ``\texttt{X}``
     - ````X````
     - Código inline
   * - ``\begin{itemize}``
     - ``-``
     - Lista no numerada
   * - ``\begin{enumerate}``
     - ``1. 2. 3.``
     - Lista numerada
   * - ``\ref{label}``
     - ``:ref:`label```
     - Referencia interna
   * - ``\cite{key}``
     - ``:cite:`key```
     - Citación
   * - ``\label{x}``
     - ``.. _x:``
     - Etiqueta
   * - ``\begin{figure}``
     - ``.. figure::``
     - Figura
   * - ``\begin{table}``
     - ``.. list-table::``
     - Tabla
   * - ``\begin{equation}``
     - ``.. math::``
     - Ecuación
   * - ``\begin{verbatim}``
     - ``.. code-block::``
     - Código

**Proceso:**

.. code-block:: text

   Para cada comando LaTeX:
   1. Buscar en tabla de rendición
   2. Si existe mapeo directo → aplicar
   3. Si NO existe → marcar para revisión

Paso 3.3: Preferencia (Signifié sobre Signifiant)
--------------------------------------------------

**Principio:**
   Preservar CONTENIDO (función semántica), adaptar FORMA (sintaxis).

**Ejemplos de aplicación:**

1. **Listas:**
   
   .. code-block:: latex
   
      % LaTeX (Signifiant específico)
      \begin{enumerate}
      \item Primero
      \item Segundo
      \end{enumerate}
   
   .. code-block:: rst
   
      # RST (Signifiant adaptado, Signifié preservado)
      1. Primero
      2. Segundo

2. **Espaciado vertical:**
   
   .. code-block:: latex
   
      % LaTeX
      Párrafo 1
      \vspace{2cm}
      Párrafo 2
   
   .. code-block:: rst
   
      # RST (omitir \vspace - no semántico)
      Párrafo 1
      
      Párrafo 2

3. **Código fuente:**
   
   .. code-block:: latex
   
      % LaTeX
      \begin{verbatim}
      def foo():
          pass
      \end{verbatim}
   
   .. code-block:: rst
   
      # RST (preservar EXACTAMENTE - forma = contenido)
      .. code-block:: python
      
         def foo():
             pass

**Validación Signifié:**

.. code-block:: text

   Después de traducir cada elemento, preguntar:
   
   ¿El lector obtiene la MISMA INFORMACIÓN?
   
   SI SÍ: ✅ Signifié preservado
   SI NO: ⚠️ Revisar traducción

----

FASE 4: Aplicación de Tácticas
===============================

Paso 4.1: Identificar Necesidad de Divergencia
-----------------------------------------------

**Pregunta:**
   ¿El método por defecto es suficiente o necesitamos desviarnos?

**Criterios para divergir:**

.. code-block:: text

   Divergir SI:
   [ ] Original usa construcción no idiomática para RST
   [ ] Contenido necesita aclaración
   [ ] Hay inconsistencias en el original
   [ ] Hay complejidad innecesaria
   
   NO divergir SI:
   [ ] Método por defecto funciona bien
   [ ] No hay objetivo claro para divergencia

Paso 4.2: Seleccionar Objetivo
-------------------------------

**Los 4 objetivos:**

1. **Domesticación** → ¿Necesita adaptarse a RST/Sphinx?
2. **Claridad** → ¿Necesita ser más comprensible?
3. **Consistencia** → ¿Hay inconsistencias que resolver?
4. **Simplificación** → ¿Hay complejidad innecesaria?

**Seleccionar UNO (máximo dos) más relevante.**

Paso 4.3: Aplicar Táctica Apropiada
------------------------------------

**Consultar:** :doc:`/01_fundamentos/objetivos_tacticas`

**Matriz resumida:**

.. code-block:: text

   DOMESTICACIÓN → Sustitución, Normalización, Modulación
   CLARIDAD → Adición, Especificación, Explicación
   CONSISTENCIA → Normalización, Generalización
   SIMPLIFICACIÓN → Omisión, Condensación

**Ejemplo práctico:**

.. code-block:: latex

   % Original (problema: referencia vaga)
   Como se mencionó anteriormente...

**Análisis:**

- Método por defecto: Traducir literal
- Problema: Vago (¿dónde exactamente?)
- Objetivo: Claridad
- Táctica: Especificación

**Traducción:**

.. code-block:: rst

   # RST (táctica aplicada)
   Como se mencionó en :ref:`seccion-introduccion`...

Paso 4.4: Documentar Decisión
------------------------------

**SIEMPRE documentar divergencias significativas:**

.. code-block:: rst

   .. note::
      **Decisión de traducción:**
      
      Original: "Como se mencionó anteriormente"
      Problema: Referencia vaga
      Objetivo: Claridad
      Táctica: Especificación
      Resultado: :ref:`seccion-introduccion` (explícito)

----

FASE 5: Validación
==================

Paso 5.1: Compilación
---------------------

**Después de traducir cada capítulo:**

.. code-block:: bash

   # Navegar a raíz del proyecto
   cd /tmp/ADT
   
   # Limpiar compilación anterior
   make clean
   
   # Compilar
   make html
   
   # Verificar resultado del capítulo específico
   firefox build/html/biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed/server_side_action_node_npm/capitulo_01.html

**Verificar:**

.. code-block:: text

   [ ] Compila sin errores
   [ ] Sin warnings críticos
   [ ] HTML generado existe en ruta correcta biblioteca/
   [ ] Glosario del capítulo se generó
   [ ] Figuras se muestran correctamente

Paso 5.2: Preservación Semántica
---------------------------------

**Checklist de completitud:**

.. code-block:: text

   CONTENIDO:
   [ ] Todas las secciones presentes
   [ ] Todos los párrafos traducidos
   [ ] Todas las figuras incluidas
   [ ] Todas las tablas presentes
   [ ] Todas las ecuaciones convertidas
   
   REFERENCIAS:
   [ ] Todos los \ref convertidos a :ref:
   [ ] Todos los \cite convertidos a :cite:
   [ ] Todas las etiquetas (\label) como .. _etiqueta:
   [ ] Referencias funcionan (clic va al destino)
   
   EXACTITUD:
   [ ] Código fuente sin cambios
   [ ] Ecuaciones matemáticas correctas
   [ ] Nombres propios preservados
   [ ] Números/datos exactos

Paso 5.3: Calidad Visual
-------------------------

**Revisar HTML generado:**

.. code-block:: text

   TIPOGRAFÍA:
   [ ] Títulos con jerarquía correcta
   [ ] Énfasis visible
   [ ] Código formateado correctamente
   
   LAYOUT:
   [ ] Figuras con buen tamaño
   [ ] Tablas legibles
   [ ] Ecuaciones bien renderizadas
   [ ] Espaciado apropiado
   
   NAVEGACIÓN:
   [ ] TOC (tabla de contenidos) completo
   [ ] Enlaces internos funcionan
   [ ] Enlaces externos (si hay) funcionan

----

FASE 6: Revisión y Mejora
==========================

Paso 6.1: Revisión de Enlaces
------------------------------

**Verificar todos los enlaces:**

.. code-block:: bash

   # Buscar todos los :ref: en el documento
   grep -r ':ref:' source/capitulo_X/
   
   # Probar manualmente en HTML que funcionan

**Arreglar rotos:**

.. code-block:: rst

   # Si referencia no funciona:
   # 1. Verificar que etiqueta existe
   # 2. Verificar ortografía
   # 3. Verificar que está en un archivo incluido en toctree

Paso 6.2: Optimización de Redacción
------------------------------------

**Mejorar sin cambiar contenido:**

1. **Claridad:**
   - ¿Hay frases confusas que podemos aclarar?
   - ¿Conviene agregar ``.. note::`` en algún lugar?

2. **Concisión:**
   - ¿Hay redundancia que podemos condensar?
   - ¿Verbosidad que podemos simplificar?

3. **Consistencia:**
   - ¿Terminología consistente en todo el capítulo?
   - ¿Estilo consistente?

Paso 6.3: Aplicar Feedback
---------------------------

**Si hay revisión por pares:**

.. code-block:: text

   Para cada comentario de revisor:
   1. ¿Es válido? → Implementar cambio
   2. ¿Es debatible? → Discutir
   3. ¿Es erróneo? → Explicar por qué no se implementa

**Documentar cambios:**

.. code-block:: rst

   .. note::
      **Feedback implementado:**
      
      Revisor sugirió aclarar término "API"
      → Agregado: API (Application Programming Interface)

----

FASE 7: Publicación
===================

Paso 7.1: Compilación Final
----------------------------

**Compilación completa y limpia:**

.. code-block:: bash

   # Limpieza total
   make clean
   
   # Compilación final
   make html
   
   # Verificar warnings
   # Objetivo: 0 errors, mínimos warnings

Paso 7.2: Control de Calidad Final
-----------------------------------

**Checklist pre-publicación:**

.. code-block:: text

   COMPILACIÓN:
   [ ] 0 errores
   [ ] Warnings revisados y justificados
   [ ] HTML generado completo
   
   CONTENIDO:
   [ ] Todo el capítulo/documento traducido
   [ ] Sin secciones "TODO" pendientes
   [ ] Figuras/tablas completas
   
   CALIDAD:
   [ ] Enlaces funcionan
   [ ] Navegación correcta
   [ ] Formato visual apropiado
   [ ] Sin errores tipográficos obvios
   
   DOCUMENTACIÓN:
   [ ] Decisiones importantes documentadas
   [ ] Cambios significativos registrados

Paso 7.3: Despliegue
--------------------

**Publicar libro en biblioteca:**

.. code-block:: bash

   # Si es documentación web:
   rsync -avz build/html/biblioteca/ servidor:/docs/biblioteca/
   
   # O si es repositorio Git:
   cd /tmp/ADT
   git add source/biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed/
   git commit -m "Traducción completa: Modern Full-Stack Development - Capítulo 5"
   git push

**Actualizar catálogos:**

.. code-block:: bash

   # Actualizar índices de biblioteca
   # Ver: biblioteca/catalogo/
   
   # Actualizar metadata del libro
   vim biblioteca/.../Modern_Full_Stack_Development_Zammetti_2ed/metadata_libro.rst
   # Cambiar :progreso: y :estado:

**Notificar:**

- Actualizar changelog del proyecto
- Notificar a equipo de revisión
- Agregar a catálogo de libros completados

----

Plantillas y Herramientas
=========================

Template de Sección
-------------------

.. code-block:: rst

   ================
   Título de Sección
   ================
   
   .. Metadata
   :Autor: [Nombre]
   :Fecha: [YYYY-MM-DD]
   :Original: [archivo.tex]
   :Estado: [Borrador/Revisión/Aprobado]
   
   .. Notas de traducción
   .. note::
      **Decisiones de traducción:**
      
      - [Decisión 1]
      - [Decisión 2]
   
   ----
   
   [Contenido aquí]
   
   ----
   
   Referencias
   ===========
   
   .. [#] Referencia 1
   .. [#] Referencia 2

Scripts Útiles
--------------

**Verificar compilación:**

.. code-block:: bash

   #!/bin/bash
   # check_build.sh
   
   make clean
   make html 2>&1 | tee build.log
   
   if grep -q "ERROR" build.log; then
       echo "❌ ERRORES en compilación"
       exit 1
   else
       echo "✅ Compilación exitosa"
   fi

**Contar progreso de libro:**

.. code-block:: bash

   #!/bin/bash
   # progreso_libro.sh
   
   # Ruta al libro
   LIBRO="biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed"
   
   # Contar capítulos totales (carpetas con traduccion/)
   total_capitulos=$(find "$LIBRO" -maxdepth 1 -type d -name "*" | grep -v "^$LIBRO$" | grep -v "front_matter" | grep -v "back_matter" | wc -l)
   
   # Contar capítulos con traducción
   traducidos=$(find "$LIBRO" -name "traduccion" -type d | wc -l)
   
   echo "Progreso del libro:"
   echo "  Traducidos: $traducidos / $total_capitulos capítulos"
   echo "  Porcentaje: $(($traducidos * 100 / $total_capitulos))%"
   
   # Actualizar metadata_libro.rst
   sed -i "s/:progreso:.*/:progreso: $(($traducidos * 100 / $total_capitulos))%/" "$LIBRO/metadata_libro.rst"

----

Troubleshooting Común
=====================

Problema 1: No Compila
-----------------------

**Síntoma:**
   ``make html`` falla con error.

**Diagnóstico:**

.. code-block:: bash

   # Ver error específico
   make html 2>&1 | grep -A 5 "ERROR"

**Soluciones comunes:**

- Error de sintaxis RST → Revisar indentación, directivas
- Referencia rota → Verificar etiquetas con ``.. _``
- Archivo faltante → Verificar paths en ``.. figure::``

Problema 2: Referencias No Funcionan
-------------------------------------

**Síntoma:**
   Clic en referencia no va a destino.

**Diagnóstico:**

.. code-block:: bash

   # Buscar etiqueta
   grep -r ".. _mi-etiqueta:" source/

**Soluciones:**

- Etiqueta no existe → Crear con ``.. _mi-etiqueta:``
- Etiqueta en archivo no incluido → Agregar a ``toctree``
- Ortografía → Verificar mayúsculas/guiones

Problema 3: Figuras No Aparecen
--------------------------------

**Síntoma:**
   Espacio en blanco donde debería estar figura.

**Diagnóstico:**

.. code-block:: bash

   # Verificar path
   ls -la source/capitulo_X/figuras/mi_figura.png

**Soluciones:**

- Archivo no existe → Copiar desde original
- Path incorrecto → Ajustar en ``.. figure::``
- Formato no soportado → Convertir a PNG/JPG

----

Métricas de Calidad
===================

**Objetivo:** Medir calidad de la traducción

Métrica 1: Tasa de Compilación
-------------------------------

.. code-block:: text

   Tasa de Compilación = Secciones que compilan sin errores / Total secciones
   
   Objetivo: 100%

Métrica 2: Preservación de Contenido
-------------------------------------

.. code-block:: text

   Completitud = Elementos traducidos / Total elementos
   
   Elementos: secciones, figuras, tablas, ecuaciones, referencias
   
   Objetivo: 100%

Métrica 3: Calidad Visual
--------------------------

.. code-block:: text

   Checklist de 20 ítems visuales
   
   Puntuación = Ítems OK / 20
   
   Objetivo: ≥ 95% (19/20)

Métrica 4: Tiempo por Sección
------------------------------

.. code-block:: text

   Tiempo Promedio = Σ(tiempo por sección) / N secciones
   
   Benchmark: 1-2 horas por sección estándar
   
   Objetivo: Mejorar eficiencia con experiencia

----

Conclusión
==========

**Este workflow de 7 fases proporciona:**

✅ Proceso sistemático y repetible  
✅ Checkpoints de calidad en cada fase  
✅ Documentación de decisiones  
✅ Métricas de progreso  
✅ Troubleshooting integrado

**Resultado esperado:**

   Traducciones de alta calidad, consistentes, y verificables.

**Próximo paso:**

   Aplicar este workflow en un libro real usando la estructura de biblioteca/.
   
   Ver ejemplos en:
   - :doc:`/biblioteca/arc42/index` (ejemplo en progreso)
   - :doc:`/docs_maestros/ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta`

----

Referencias
===========

- :doc:`/01_fundamentos/principios_fundamentales`
- :doc:`/01_fundamentos/objetivos_tacticas`
- :doc:`/01_fundamentos/_metodologias/metodo_por_defecto`
- :doc:`modo_alta_fidelidad/index`
- :doc:`modo_marcado_visual/index`

----

**Versión:** 1.0  
**Fecha:** 2026-01-27  
**Estado:** Aprobado - Procedimiento operativo principal
