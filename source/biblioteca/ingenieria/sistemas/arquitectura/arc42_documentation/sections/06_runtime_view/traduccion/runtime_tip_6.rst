.. _runtime_tip_6:

===============================================================
Tip 6-6: ¡Describe extractos de escenarios (escenarios parciales)!
===============================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Describe solo extractos o partes de **escenarios**. Enfócate en partes riesgosas, difíciles, complicadas o interesantes. No dudes en comenzar en medio de un **proceso** más largo.

----

Hemos visto demasiados **diagramas de secuencia** que se asemejan al de abajo: **Escenarios** que solo propagan datos sobre varios participantes - usualmente material no interesante.

.. figure:: ../figuras/06-long-and-mostly-boring.png
   :alt: Diagrama de secuencia aburrido
   :align: center
   :width: 40%
   
   Diagrama de secuencia largo y mayormente aburrido

Más Efectivo: Escenarios Parciales
===================================

Describe solo extractos o partes de tales **escenarios**.

* Enfócate en partes riesgosas, difíciles, complicadas o interesantes.
* No dudes en comenzar justo en el medio de un **proceso** más largo (general)
* Corta material aburrido, estándar, simple o directo

Compara el diagrama (compacto) debajo con la versión (aburrida y mucho más larga) de arriba.

.. figure:: ../figuras/06-short-and-interesting.png
   :alt: Diagrama de secuencia parcial
   :align: center
   :width: 30%
   
   Diagrama de secuencia corto e interesante (parcial)

Por cierto: ambos diagramas fueron generados desde una descripción textual PlantUML, el código para el último se da debajo:

.. code-block:: plantuml

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

----

.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_2` - Documentar pocos escenarios
   * :ref:`runtime_tip_3` - Escenarios esquemáticos
   * :ref:`runtime_tip_5` - PlantUML para escenarios

----

:Tip: 6-6
:Tema: Escenarios parciales
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1