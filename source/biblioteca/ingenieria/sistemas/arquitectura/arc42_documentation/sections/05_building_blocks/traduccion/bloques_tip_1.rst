.. _bloques_tip_1:

===============================================================
Tip 5-1: ¡Usa estructuras comunes para las secciones de la vista de bloques de construcción!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Independientemente del nivel de detalle o nivel de abstracción que estés documentando o especificando actualmente: Usa representaciones uniformes de **caja blanca** y **caja negra**.

----

Independientemente del nivel de detalle o nivel de abstracción que estés documentando o especificando actualmente: Usa uniformes:

* Representaciones de **caja blanca** para explicar (gráficamente) estructuras y funcionamiento interno
* Representaciones de **caja negra** para explicar **responsabilidad** e **interfaces** de **bloques de construcción** individuales

Descripciones de Caja Blanca
=============================

Cada **caja blanca** explica la **estructura interna** e **interfaces** internas de una "**caja negra** de nivel superior", usualmente mediante un diagrama y alguna explicación textual.

Podrías usar UML o cualquier tipo de diagrama de cajas/flechas.

Descripciones de Caja Negra
============================

Las descripciones de **caja negra**:

* Explican **responsabilidades** e **interfaces** de un **bloque de construcción**
* Respetan el principio de ocultamiento de información, evitando así la divulgación de detalles internos
* Pueden ser tabulares o gráficas

Otros tips en esta sección se refieren tanto a **cajas negras** como a **cajas blancas**.

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Plantillas whitebox/blackbox

----

:Tip: 5-1
:Tema: Estructuras comunes whitebox/blackbox
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
