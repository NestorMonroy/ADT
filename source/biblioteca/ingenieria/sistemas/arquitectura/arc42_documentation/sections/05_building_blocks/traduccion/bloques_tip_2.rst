.. _bloques_tip_2:

===============================================================
Tip 5-2: ¡Organiza la vista de bloques de construcción jerárquicamente!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Explica la estructura de tu código fuente como una **jerarquía** de **cajas blancas** y **cajas negras**, comenzando desde la vista de **contexto** (sección 3 de arc42).

----

Explica la estructura de tu código fuente como una **jerarquía** de **cajas blancas** y **cajas negras**, comenzando desde la vista de **contexto** (sección 3 de arc42).

El **contexto** muestra el sistema completo como una **caja negra**, que la **vista de bloques de construcción** nivel 1 refina como **caja blanca**.

El diagrama abajo muestra esquemáticamente esta **jerarquía**:

.. figure:: ../figuras/05-building-block-hierarchy.webp
   :alt: Diagrama jerárquico de bloques de construcción
   :align: center
   :width: 80%
   
   Jerarquía de bloques de construcción: Niveles 1, 2, 3

Niveles de la Jerarquía
========================

* **Nivel 1** es la descripción de **caja blanca** del sistema general junto con descripciones de **caja negra** de todos los **bloques de construcción** contenidos.
* **Nivel 2** hace zoom en algunos **bloques de construcción** del nivel 1. Así contiene la descripción de **caja blanca** de **bloques de construcción** seleccionados del nivel 1, junto con descripciones de **caja negra** de sus **bloques de construcción** internos.
* **Nivel 3** hace zoom en **bloques de construcción** seleccionados del nivel 2, y así sucesivamente.

.. important::
   En el diagrama arriba, cada **rectángulo redondeado** representa una sola **caja blanca**, que debe ser documentada por una instancia de la plantilla de caja blanca.
   ¡No tendrás la **jerarquía** en un solo diagrama en tu documentación concreta!

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Nivel 1
   * :ref:`seccion_5_2` - Nivel 2
   * :ref:`seccion_5_3` - Nivel 3

----

:Tip: 5-2
:Tema: Organización jerárquica
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
