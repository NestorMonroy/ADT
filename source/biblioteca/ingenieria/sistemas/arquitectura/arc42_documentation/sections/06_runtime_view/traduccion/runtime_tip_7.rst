.. _runtime_tip_7:

===============================================================
Tip 6-7: ¡Usa diagramas de actividad con carriles para describir o especificar escenarios de tiempo de ejecución!
===============================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Los **carriles** (swimlanes) son una opción estándar de UML para agrupar actividades por actor o **bloque de construcción**. Son muy fáciles de usar, incluso con papel y lápiz.

----

.. epigraph::

   Un carril (swimlane) es una manera de agrupar actividades realizadas por el mismo actor en un **diagrama de actividad** o para agrupar actividades en un único hilo
   
   -- Scott Ambler, `Agile Modeling <https://www.agilemodeling.com/style/activityDiagram.htm>`_

Los **carriles** (swimlanes) son una opción estándar (UML) para agrupar actividades por actor o **bloque de construcción** (o hilo, ver cita arriba). Conducen a **diagramas de actividad** *particionados*, ya sea horizontal o verticalmente.

Son muy fáciles de usar, incluso con papel y lápiz.

Encuentras un ejemplo debajo - donde las actividades realizadas por cada uno de los **bloques de construcción** están agrupadas por **carriles** (verticales).

.. figure:: ../figuras/06-activity-with-swimlane.png
   :alt: Diagrama de actividad con carriles
   :align: center
   :width: 50%
   
   Diagrama de actividad con swimlanes (carriles)

El diagrama de arriba fue renderizado por PlantUML con el siguiente código:

.. code-block:: plantuml

   @startuml
   |GUI|
   start
   :enter-data;
   |Core-Domain|
   :validate-address;
   :validate-credit-card;
   |Email-Provider|
   :send-optin-mail;
   :validate-smtp-return;
   |Core-Domain|
   :prepare-welcome-\npackage;
   |GUI|
   :display-success-message;
   stop
   @enduml

Una Nota sobre Herramientas
============================

PlantUML (a partir de febrero 2017) solo puede renderizar **carriles** verticales. Dependiendo de tus necesidades, **carriles** horizontales podrían ser mejor para entender - en cuyo caso necesitas herramientas diferentes.

----

.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_1` - Mapear bloques a actividades
   * :ref:`runtime_tip_8` - Diagramas de actividad con particiones

----

:Tip: 6-7
:Tema: Diagramas de actividad con swimlanes
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1