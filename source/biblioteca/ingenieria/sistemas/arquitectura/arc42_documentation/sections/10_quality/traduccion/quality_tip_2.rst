.. _quality_tip_2:

===============================================================
Tip 10-2: ¡Documenta y explica el quality tree específico! (¡deprecado!)
===============================================================

:Tema: Quality tree
:Palabras clave: quality, quality-tree
:Estado: Deprecado - se favorece tabla simple sobre gráfico

----

.. warning::
   **Este tip está deprecado**
   
   En versiones previas de este tip, proponíamos un **quality tree** gráfico.
   
   Ahora, algunos años después, favorecemos una **tabla simple** en lugar de los gráficos.
   
   Una discusión de nuestras razones está más allá del alcance de esta documentación.
   
   En resumen: Nuestro propio modelo pragmático de calidad `Q42 <https://quality.arc42.org>`_ hace uso de tags/etiquetas en lugar de una jerarquía estricta. Esto demostró ser una mejora importante sobre los gráficos.

----

Propuesta Actual
================

Proponemos mantener la sección 1.2 de arc42 (**objetivos de calidad**) corta; allí muestras solo los top 3-5 **objetivos de calidad**, con prioridades.

Aquí, en la sección 10 de arc42, entramos en más detalle:

* Muestra tus **objetivos de calidad** y **requisitos** más importantes (si eres fanático de mindmaps o gráficos, usa una versión gráfica)

Contexto Histórico
==================

.. note::
   En la literatura de ingeniería de software, por ejemplo del Software Engineering Institute, tales estructuras de árbol han sido nombradas ***Quality Attribute Utility Tree***.
   
   Son parte integral del método de análisis y evaluación de arquitectura `ATAM <https://www.sei.cmu.edu/architecture/tools/evaluate/atam.cfm>`_, que muchas personas consideran excesivamente formal y lento.

Ejemplo de Quality Tree Gráfico
================================

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/figuras/10-quality-tree-example.png
   :alt: Ejemplo de quality tree gráfico
   :align: center
   :width: 80%
   
   Ejemplo de quality tree gráfico (enfoque histórico)

Tal árbol *puede* proporcionar una buena visión general de las cualidades requeridas, puede documentar puntos de enfoque. Si crece más, toda visión general se pierde - y una **tabla simple** ganará.

----

**Evolución del Enfoque:**

.. list-table::
   :header-rows: 1
   :widths: 30 35 35
   
   * - Enfoque
     - Ventajas
     - Desventajas
   * - **Quality Tree Gráfico**
     - Visualmente atractivo
     - Pierde claridad con >20 items
   * - **Tabla Simple**
     - Escalable a 100+ items
     - Menos visualmente atractivo
   * - **Tags/Etiquetas (Q42)**
     - Flexible, no jerárquico
     - Requiere nuevo paradigma

----

Referencias Adicionales
=======================

* Arnon Rotem-Gal-Oz ha escrito una `explicación más detallada del quality tree <https://arnon.me/2010/05/utility-trees-hatching-quality-attributes/>`_
* El modelo pragmático de calidad: `quality.arc42.org <https://quality.arc42.org>`_

----

.. seealso::
   * **Tip 10-1** - Mantener objetivos de calidad cortos
   * **Tip 10-3** - Usar mind-map como quality tree
   * **Modelo Q42** - https://quality.arc42.org
