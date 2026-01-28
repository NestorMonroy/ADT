.. _bloques_tip_10:

===============================================================
Tip 5-10: ¡Usa conceptos transversales para describir o especificar similitudes en bloques de construcción!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   En resumen: en lugar de repetir subestructuras recurrentes de **bloques de construcción**, factoriza esas en conceptos transversales.

----

En resumen: en lugar de repetir subestructuras recurrentes de **bloques de construcción**, factoriza esas en conceptos transversales.

Redundancia Problemática
=========================

Ver los siguientes diagramas de **bloques de construcción**: El nivel superior (**caja blanca** X) consiste de **cajas negras** A, B y D - que se refinan en tres diagramas.

Todos esos refinamientos se ven sorprendentemente similares - eso es demasiada redundancia.

.. figure:: ../figuras/05-similar-building-blocks.webp
   :alt: Diagrama de bloques de construcción con demasiada redundancia
   :align: center
   :width: 85%
   
   Problema: Demasiada redundancia en refinamientos similares

Conceptos Transversales al Rescate
===================================

Un enfoque algo más simple, basado en conceptos transversales, evita esta redundancia. En el siguiente diagrama, la **caja blanca** contiene **cajas negras** A, B y D - pero no hay refinamiento para esas. En su lugar, todas llevan el estereotipo «X-service», refiriéndose a un concepto transversal que explica cómo los elementos de tipo «X-service» deben ser construidos, creados o implementados.

.. figure:: ../figuras/05-concepts-instead.webp
   :alt: Diagrama de bloques de construcción, enfoque más simple
   :align: center
   :width: 85%
   
   Solución: Usar conceptos transversales en lugar de repetir estructura

.. important::
   Los conceptos transversales podrían describir principios, reglas o restricciones de implementación que deben cumplirse para tipos específicos de **bloques de construcción**. Ver sección 8 de arc42 para detalles.

Tips Relacionados
==================

* Explica conceptos en lugar de demasiados detalles de **bloques de construcción**, ver tip 5-28.
* Debes nombrar conceptos importantes, y usar estos nombres en **bloques de construcción**, ver tip 8-11.

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * Sección 8 de arc42 - Conceptos Transversales
   * :ref:`bloques_tip_28` - Conceptos vs detalles

----

:Tip: 5-10
:Tema: Conceptos transversales
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
