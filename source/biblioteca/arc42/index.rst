============================
arc42: Arquitectura de Software
============================

.. note::
   arc42 es una plantilla para documentación de arquitectura de software.
   Esta sección contiene la traducción al español de la documentación oficial.

Introducción
============

arc42 proporciona una plantilla clara y práctica para documentar arquitecturas
de software. Esta biblioteca contiene la traducción completa de la documentación
al español, organizada en 12 secciones.

Estado de la Traducción
========================

.. list-table::
   :header-rows: 1
   :widths: 10 40 15 35

   * - Sección
     - Título
     - Estado
     - Contenido
   * - 01
     - Introduction and Goals
     - ✅ Completa
     - :doc:`sections/01_introduction_goals/traduccion/seccion_01_introduccion_objetivos`
   * - 02
     - Architecture Constraints
     - ✅ Completa
     - :doc:`sections/02_constraints/traduccion/seccion_02_restricciones`
   * - 03
     - Context and Scope
     - ✅ Completa
     - :doc:`sections/03_context/traduccion/seccion_03_contexto_alcance`
   * - 04
     - Solution Strategy
     - ⏳ Pendiente
     - Estructura creada
   * - 05
     - Building Block View
     - ⏳ Pendiente
     - Estructura creada
   * - 06
     - Runtime View
     - ⏳ Pendiente
     - Estructura creada
   * - 07
     - Deployment View
     - ⏳ Pendiente
     - Estructura creada
   * - 08
     - Cross-cutting Concepts
     - ⏳ Pendiente
     - Estructura creada
   * - 09
     - Architecture Decisions
     - ⏳ Pendiente
     - Estructura creada
   * - 10
     - Quality Requirements
     - ⏳ Pendiente
     - Estructura creada
   * - 11
     - Risks and Technical Debt
     - ⏳ Pendiente
     - Estructura creada
   * - 12
     - Glossary
     - ⏳ Pendiente
     - Estructura creada

Progreso: **3/12 secciones (25%)** ✅

Secciones Traducidas
=====================

Sección 01: Introduction and Goals
-----------------------------------

.. toctree::
   :maxdepth: 1

   sections/01_introduction_goals/traduccion/seccion_01_introduccion_objetivos

Objetivos, restricciones de negocio y visión general del sistema.

Sección 02: Architecture Constraints
-------------------------------------

.. toctree::
   :maxdepth: 1

   sections/02_constraints/traduccion/seccion_02_restricciones

Restricciones técnicas y organizacionales que afectan el diseño.

Sección 03: Context and Scope
------------------------------

.. toctree::
   :maxdepth: 1

   sections/03_context/traduccion/seccion_03_contexto_alcance

Contexto del sistema y sus límites. Incluye 7 diagramas PlantUML.

Sobre arc42
===========

**arc42** es una plantilla de código abierto para documentación de arquitectura
de software creada por Dr. Gernot Starke y Dr. Peter Hruschka.

**Sitio oficial:** https://arc42.org

**Licencia:** Creative Commons (CC BY-SA 4.0)

Estructura de Cada Sección
===========================

Cada sección de arc42 en esta biblioteca contiene:

.. code-block:: text

   sections/XX_nombre/
   ├── original/              Texto original en inglés
   ├── traduccion/            Traducción al español
   ├── diagramas/             Diagramas PlantUML (.puml + .png)
   ├── glosario_seccion.rst   Términos específicos
   └── notas_traduccion.rst   Notas del traductor

Referencias
===========

- :doc:`/docs_maestros/ESTRUCTURA_DE_BIBLIOTECA` - Organización de la biblioteca
- :doc:`/docs_maestros/ARQUITECTURA_DOCUMENTAL_TRADUCCION` - Arquitectura documental
- `Documentación oficial arc42 <https://docs.arc42.org/>`_

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Secciones arc42

   sections/01_introduction_goals/traduccion/seccion_01_introduccion_objetivos
   sections/02_constraints/traduccion/seccion_02_restricciones
   sections/03_context/traduccion/seccion_03_contexto_alcance
