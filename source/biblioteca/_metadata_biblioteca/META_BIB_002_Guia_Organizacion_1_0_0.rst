==================================================================================
META_BIB_002: Guía de Organización Jerárquica por Libro Completo
==================================================================================

:Código: META_BIB_002
:Versión: 1.0.0
:Fecha: 2026-01-28
:Estado: NORMATIVO
:Tipo: Guía de Organización
:Autor: Sistema ADT
:Base: META_BIB_001 (Sistema de Clasificación)

.. contents:: Tabla de Contenido
   :depth: 3
   :local:

----

Principio Fundamental
=====================

**Un Libro = Una Carpeta Completa**

Cada libro traducido ocupa **exactamente una carpeta** que contiene:

- Todo el contenido original
- Toda la traducción
- Todos los glosarios
- Todas las figuras
- Toda la metadata

**NO** distribuir capítulos de un mismo libro en múltiples ubicaciones.

----

Metodología de Organización
============================

Nivel 1: Por Categoría
-----------------------

**Criterio:** Ámbito general del conocimiento

.. code-block:: text

   /biblioteca/
   ├── informatica/        ← Ciencias de la Computación
   ├── ingenieria/         ← Ingeniería de Software
   └── ciencias/           ← Ciencias Aplicadas

**Regla de Decisión:**

.. code-block:: rst

   ¿El libro trata principalmente de...?
   
   → Programación, algoritmos, IA, redes?
     CATEGORÍA: informatica/
   
   → Arquitectura, procesos, metodologías?
     CATEGORÍA: ingenieria/
   
   → Matemáticas, física, biología computacional?
     CATEGORÍA: ciencias/

Nivel 2: Por Subcategoría
--------------------------

**Criterio:** Área específica de conocimiento

**Ejemplo para Informática:**

.. code-block:: text

   informatica/
   ├── programacion/              ← Lenguajes y frameworks
   ├── inteligencia_artificial/   ← ML, DL, NLP
   ├── redes/                     ← Protocolos, comunicaciones
   ├── seguridad/                 ← Ciberseguridad
   ├── bases_datos/               ← SQL, NoSQL
   ├── sistemas_operativos/       ← Linux, Windows
   ├── desarrollo_web/            ← Web general
   ├── desarrollo_movil/          ← iOS, Android
   ├── devops/                    ← Docker, K8s, Cloud
   └── algoritmos/                ← Estructuras de datos

**Regla de Nomenclatura:**

- Usar **minúsculas**
- Usar **guiones bajos** para espacios (``inteligencia_artificial``)
- Nombres **descriptivos** en español
- Nombres **singulares** o **plurales** según convenga

Nivel 3: Por Especialidad
--------------------------

**Criterio:** Tecnología o framework específico

**Ejemplo para Programación:**

.. code-block:: text

   informatica/programacion/
   ├── full_stack/       ← Desarrollo completo
   ├── frontend/         ← Interfaces de usuario
   ├── backend/          ← Lado del servidor
   ├── python/           ← Lenguaje Python
   ├── javascript/       ← Lenguaje JavaScript
   ├── typescript/       ← Lenguaje TypeScript
   ├── react/            ← Framework React
   ├── vue/              ← Framework Vue.js
   ├── angular/          ← Framework Angular
   ├── nodejs/           ← Runtime Node.js
   ├── django/           ← Framework Django
   ├── flask/            ← Framework Flask
   └── general/          ← Múltiples tecnologías

**Regla de Nomenclatura:**

- Usar **minúsculas**
- Usar **guiones bajos** solo si necesario
- Nombres **cortos** (preferir ``react`` sobre ``react_framework``)
- Nombres **técnicos** originales (``nodejs`` no ``nodo_js``)

Nivel 4: Carpeta del Libro
---------------------------

**Criterio:** Nombre del libro + autor/edición

**Formato:**

.. code-block:: text

   [Titulo_Principal]_[Autor_Apellido]_[EdiciónOInfo]/

**Ejemplos:**

.. code-block:: text

   Modern_Full_Stack_Development_Zammetti_2ed/
   React_Advanced_Patterns_Lee_2024/
   Python_Complete_Guide_Van_Rossum_2025/
   Docker_Deep_Dive_Poulton_2024/
   Clean_Architecture_Martin_2017/

**Reglas de Nomenclatura:**

1. **Capitalización:** Cada palabra con mayúscula inicial (``Modern_Full_Stack``)
2. **Espacios:** Reemplazar con guión bajo (``_``)
3. **Autor:** Apellido del autor principal
4. **Edición:** Incluir si hay múltiples ediciones (``2ed``, ``3rd``, etc.)
5. **Año:** Incluir año de publicación si ayuda a diferenciar
6. **Caracteres especiales:** Eliminar (no usar ``:`` , ``/``, etc.)
7. **Longitud:** Mantener razonable (<80 caracteres)

**Ejemplos de Transformación:**

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Título Original
     - Nombre de Carpeta
   * - "Modern Full-Stack Development (2nd Edition)"
     - ``Modern_Full_Stack_Development_Zammetti_2ed/``
   * - "Clean Architecture: A Craftsman's Guide"
     - ``Clean_Architecture_Martin_2017/``
   * - "Python for Data Science"
     - ``Python_For_Data_Science_McKinney_2024/``
   * - "Docker: Up & Running"
     - ``Docker_Up_And_Running_Kane_2023/``

----

Estructura Interna del Libro
=============================

Archivos en la Raíz del Libro
------------------------------

**Obligatorios:**

.. code-block:: text

   Libro_Ejemplo/
   ├── metadata_libro.rst          ⭐ OBLIGATORIO - Info bibliográfica
   ├── index.rst                   ⭐ OBLIGATORIO - Índice navegable
   └── glosario_acumulativo.rst    ⭐ OBLIGATORIO - Todos los términos

**Opcionales pero Recomendados:**

.. code-block:: text

   ├── README.md                   ⚠️ Información rápida del libro
   ├── LICENSE.txt                 ⚠️ Licencia de traducción
   └── notas_generales.rst         ⚠️ Notas del equipo de traducción

Organización de Capítulos
--------------------------

**Nomenclatura de Carpetas de Capítulos:**

.. code-block:: text

   Chapter_[NN]_[Titulo_Corto]/
   
   Ejemplos:
   Chapter_01_Introduction/
   Chapter_02_Getting_Started/
   Chapter_03_Advanced_Concepts/
   Chapter_10_Best_Practices/

**Contenido de Cada Capítulo:**

.. code-block:: text

   Chapter_01_Introduction/
   │
   ├── original/                   ← Material original
   │   ├── chapter_01.pdf          ← PDF original (si disponible)
   │   ├── chapter_01.tex          ← LaTeX original (si disponible)
   │   └── chapter_01.md           ← Markdown original (si disponible)
   │
   ├── traduccion/                 ← Traducción en español
   │   └── capitulo_01.rst         ← Traducción RST
   │
   ├── glosario_capitulo.rst       ← Términos de este capítulo
   │
   ├── notas_traduccion.rst        ← Decisiones y notas
   │
   └── figuras/                    ← Imágenes del capítulo
       ├── fig_01_01.png
       ├── fig_01_02.svg
       └── diagram_01_03.png

**Reglas de Organización:**

1. **Separar original de traducción** (carpetas separadas)
2. **Preservar material original** completo
3. **Un archivo RST por capítulo** en traducción
4. **Figuras en carpeta propia** de cada capítulo
5. **Glosario por capítulo** para términos nuevos

Material Preliminar y Final
----------------------------

**Front Matter (Material Preliminar):**

.. code-block:: text

   front_matter/
   ├── about_author.rst            ← Sobre el autor
   ├── about_technical_reviewer.rst
   ├── acknowledgments.rst         ← Agradecimientos
   ├── foreword.rst                ← Prefacio
   ├── preface.rst                 ← Prólogo
   └── introduction.rst            ← Introducción general

**Back Matter (Material Final):**

.. code-block:: text

   back_matter/
   ├── appendix_A/
   ├── appendix_B/
   ├── bibliography.rst            ← Bibliografía
   ├── index_alfabetico.rst        ← Índice alfabético
   └── about_translator.rst        ← Sobre el traductor

**Apéndices:**

.. code-block:: text

   appendices/
   ├── appendix_A_Installation/
   ├── appendix_B_References/
   └── appendix_C_Glossary/

----

Ejemplos Completos
==================

Ejemplo 1: Libro de Full-Stack
-------------------------------

.. code-block:: text

   /biblioteca/informatica/programacion/full_stack/
       Modern_Full_Stack_Development_Zammetti_2ed/
       │
       ├── metadata_libro.rst
       ├── index.rst
       ├── glosario_acumulativo.rst
       ├── README.md
       │
       ├── Chapter_01_Server_Side_Action/
       │   ├── original/
       │   │   └── chapter_01.pdf
       │   ├── traduccion/
       │   │   └── capitulo_01.rst
       │   ├── glosario_capitulo.rst
       │   ├── notas_traduccion.rst
       │   └── figuras/
       │       ├── fig_01_01.png
       │       └── fig_01_02.png
       │
       ├── Chapter_02_Advanced_Node/
       │   └── [misma estructura]
       │
       ├── [... Chapters 03-14 ...]
       │
       ├── front_matter/
       │   ├── about_author.rst
       │   ├── acknowledgments.rst
       │   └── introduction.rst
       │
       ├── back_matter/
       │   └── index_alfabetico.rst
       │
       └── appendices/
           ├── appendix_A/
           └── appendix_B/

**Código de Clasificación:** ``INF.PRG.FST.001``

Ejemplo 2: Libro de arc42
--------------------------

.. code-block:: text

   /biblioteca/ingenieria/sistemas/arquitectura/
       arc42_documentation/
       │
       ├── metadata_libro.rst
       ├── index.rst
       ├── glosario_acumulativo.rst
       │
       ├── original/                ← Material original completo
       │   ├── _posts/
       │   ├── _includes/
       │   ├── _layouts/
       │   ├── images/
       │   └── [archivos Jekyll]
       │
       ├── traduccion/              ← Traducción organizada por secciones
       │   ├── seccion_01_introduccion/
       │   ├── seccion_02_restricciones/
       │   ├── seccion_03_contexto/
       │   └── [... secciones 04-12 ...]
       │
       └── glosarios/
           ├── glosario_seccion_01.rst
           ├── glosario_seccion_02.rst
           └── [... glosarios 03-12 ...]

**Código de Clasificación:** ``ING.SIS.ARC.001``

Ejemplo 3: Libro de Machine Learning
-------------------------------------

.. code-block:: text

   /biblioteca/informatica/inteligencia_artificial/machine_learning/
       Machine_Learning_Handbook_Smith_2025/
       │
       ├── metadata_libro.rst
       ├── index.rst
       ├── glosario_acumulativo.rst
       │
       ├── Part_I_Fundamentals/
       │   ├── Chapter_01_Introduction/
       │   ├── Chapter_02_Math_Foundations/
       │   └── Chapter_03_Statistics/
       │
       ├── Part_II_Algorithms/
       │   ├── Chapter_04_Linear_Regression/
       │   ├── Chapter_05_Decision_Trees/
       │   └── Chapter_06_Neural_Networks/
       │
       ├── Part_III_Applications/
       │   ├── Chapter_07_NLP/
       │   ├── Chapter_08_Computer_Vision/
       │   └── Chapter_09_Reinforcement_Learning/
       │
       └── datasets/               ← Datasets del libro
           ├── iris.csv
           ├── mnist/
           └── README.md

**Código de Clasificación:** ``INF.IAR.MLF.001``

----

Reglas de Mantenimiento
========================

Cuando Agregar un Libro Nuevo
------------------------------

**Checklist:**

.. code-block:: rst

   ☐ 1. Clasificar el libro (META_BIB_001)
   ☐ 2. Determinar ruta completa
   ☐ 3. Crear estructura de carpetas
   ☐ 4. Copiar material original
   ☐ 5. Crear metadata_libro.rst
   ☐ 6. Crear index.rst vacío
   ☐ 7. Crear glosario_acumulativo.rst vacío
   ☐ 8. Actualizar catalogo_completo.rst
   ☐ 9. Actualizar catalogo_numeros.txt
   ☐ 10. Actualizar estadisticas_biblioteca.rst

Cuando Reorganizar un Libro
----------------------------

**Proceso:**

1. **Justificar el cambio** (error de clasificación, nueva especialidad)
2. **Crear nueva ubicación** según nueva clasificación
3. **Mover carpeta completa** del libro
4. **Actualizar metadata_libro.rst** con nuevo código
5. **Actualizar catálogos** (completo y números)
6. **Documentar el cambio** en historial
7. **Notificar al equipo**

**Evitar reorganizaciones innecesarias.**

Cuando Eliminar un Libro
-------------------------

**Proceso:**

1. **Justificar eliminación** (obsoleto, reemplazado, error)
2. **Archivar antes de eliminar** (backup)
3. **Marcar como ELIMINADO** en catálogo (no borrar línea)
4. **NO reutilizar el número** asignado
5. **Documentar razón** de eliminación
6. **Actualizar estadísticas**

----

Herramientas de Soporte
========================

Script de Creación de Estructura
---------------------------------

Ver: ``clasificador_biblioteca.py`` (script funcional completo)

Funciones disponibles:

.. code-block:: python

   crear_estructura_libro(ruta_libro)
   validar_estructura_libro(ruta_libro)
   generar_metadata_plantilla(codigo, titulo, autor)
   actualizar_catalogos(codigo, titulo, autor)

Validación Automática
----------------------

.. code-block:: bash

   # Validar estructura de un libro
   python clasificador_biblioteca.py --validar /ruta/libro
   
   # Validar toda la biblioteca
   python clasificador_biblioteca.py --validar-todo

Generación de Reportes
-----------------------

.. code-block:: bash

   # Generar catálogo completo
   python clasificador_biblioteca.py --generar-catalogo
   
   # Generar estadísticas
   python clasificador_biblioteca.py --estadisticas

----

Referencias
===========

Documentos Relacionados
-----------------------

- :doc:`META_BIB_001_Sistema_Clasificacion_1_0_0` - Sistema de clasificación
- :doc:`META_BIB_003_Esquema_Codificacion_1_0_0` - Tabla de códigos
- :doc:`catalogo_completo` - Catálogo de libros
- :doc:`estadisticas_biblioteca` - Métricas

----

Historial de Versiones
=======================

.. list-table::
   :widths: 10 15 15 60
   :header-rows: 1

   * - Versión
     - Fecha
     - Autor
     - Cambios
   * - 1.0.0
     - 2026-01-28
     - Sistema ADT
     - Versión inicial de guía de organización

----

**Documento:** META_BIB_002_Guia_Organizacion_1_0_0.rst  
**Ubicación:** ``/biblioteca/_metadata_biblioteca/``  
**Estado:** NORMATIVO  
**Próxima revisión:** 2026-07-28
