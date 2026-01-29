.. _runtime_tip_8:

===============================================================
Tip 6-8: ¡Usa diagramas de actividad con particiones para describir o especificar escenarios de tiempo de ejecución!
===============================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Las particiones son otra forma de organizar **diagramas de actividad**, mostrando la modularización de un **proceso**.

----

Echa un vistazo al siguiente ejemplo - que muestra la *modularización* o *particionamiento* de un **diagrama de actividad**.

.. figure:: ../figuras/06-activity-with-partition.png
   :alt: Diagrama de actividad con particiones
   :align: center
   :width: 40%
   
   Diagrama de actividad con particiones

El diagrama de arriba fue renderizado por PlantUML con el siguiente código:

.. code-block:: plantuml

   @startuml
   partition Checker {
     (*)  -> "check input"
       -->If "verbose?" then

     }
   
     partition Verbalizer {
        -> [Yes] "turn on\n verbosity"

     }
   
     partition Runner 
      --> "run\n command"
   
   
      else
        ->  [no] "run\n command"
        -> "finalize"

      Endif
        ->(*)
   
   @enduml

----

.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_7` - Diagramas de actividad con swimlanes
   * :ref:`runtime_tip_1` - Mapear bloques a actividades

----

:Tip: 6-8
:Tema: Diagramas de actividad con particiones
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1