.. _runtime_tip_11:




Tip 6-11: ¡Usa diagramas de secuencia para describir o especificar escenarios de tiempo de ejecución!
=====================================================================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Usa **diagramas de secuencia** (UML) para **escenarios de tiempo de ejecución**. Denotan claramente la **responsabilidad** de todos los **bloques de construcción** participantes.




Usa **diagramas de secuencia** (UML) para **escenarios de tiempo de ejecución**. Denotan claramente la **responsabilidad** de todos los **bloques de construcción** participantes - lo cual puede ayudar en la discusión de **bloques de construcción**.

Ejemplo
=======

Ve el siguiente ejemplo:

.. .. figure:: ../figuras/06-short-and-interesting.png
..       :alt: Diagrama de secuencia UML corto e interesante
..       :align: center
..       :width: 30%
   
..       Diagrama de secuencia UML conciso

Desventaja (y una Sugerencia)
=============================

Cuando usas herramientas de modelado gráfico, crear y gestionar **diagramas de secuencia** podría tomar mucho esfuerzo. Podrías acelerar ese **proceso** usando un DSL textual (lenguaje específico de dominio) para describir las secuencias y tener alguna herramienta renderizar los diagramas por ti.

El diagrama de arriba fue renderizado usando `PlantUML <https://plantuml.com/>`_ (gratis y código abierto) con la siguiente entrada:

.. code-block:: text

   @startuml
   note right of F: before start, a1-a5 have completed
   F -> G : start
   G -> G : init
   G -> H : create()
   G <--H : X
   G -> I : authorize( X )
   I -> L : check(X)
   I <--H : ok
   G -> I : foo(X, H)
   I --> G : completed
   note right of G: G return result to A
   
   @enduml

Ver También
===========

Ver también tip 6-5.




.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_5` - PlantUML para escenarios
   * :ref:`runtime_tip_9` - Notación textual
   * :ref:`runtime_tip_1` - Mapear bloques a actividades




:Tip: 6-11
:Tema: Diagramas de secuencia UML
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1