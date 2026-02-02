.. _runtime_tip_5:




Tip 6-5: ¡Usa escenarios primariamente para 'descubrir' bloques de construcción, no tanto para documentación!
=============================================================================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Puedes clarificar, comunicar o especificar las **responsabilidades** de **bloques de construcción** usando **escenarios**. Úsalos para crear entendimiento común dentro de los equipos.




Puedes clarificar, comunicar o especificar las **responsabilidades** de **bloques de construcción** usando **escenarios**.

Al visualizar **escenarios** o **procesos** puedes crear entendimiento común de **bloques de construcción** dentro de los equipos.

Usa herramientas ligeras - es decir, papel o herramientas basadas en texto. Con herramientas de modelado a escala completa puedes lograr resultados visualmente estéticos - al precio de mayor esfuerzo de creación y mantenimiento.

Ejemplo: Renderizar Diagramas de Secuencia con PlantUML
=======================================================

`PlantUML <https://plantuml.com/>`_ es una herramienta gratuita que puede renderizar **diagramas de secuencia** desde una descripción textual.

Considera un ejemplo: En el siguiente listado encuentras la descripción de una secuencia simple, mostrada en la figura debajo:

.. code-block:: text

   @startuml
   G -> G : init
   G -> H : sendEmail()
   G <--H : reply X
   G -> I : blabla( X )
   I -> H : check( X )
   I <--H : ok
   @enduml

.. .. figure:: ../figuras/06-plantuml-example.png
..       :alt: Ejemplo de diagrama de secuencia PlantUML
..       :align: center
..       :width: 30%
   
..       Diagrama de secuencia generado con PlantUML

Encantador: ¡Tales descripciones textuales pueden ser fusionadas y versionadas como cualquier otro código fuente!

PlantUML soporta la mayoría de los constructos de diagramas de secuencia UML, como referencias de **interacción**, bucles, alternativas y demás. Puedes aplicar *algunos* estilos a diagramas y exportar en varios formatos gráficos (png, jpg, svg). Hay numerosos plugins disponibles para wikis, entornos de desarrollo, herramientas de construcción o la línea de comandos.

.. note::
   Desde mi (Gernot) experiencia, PlantUML es muy amigable para desarrolladores y por lo tanto bien adecuado para discutir alternativas de **escenarios** entre el equipo de desarrollo.




.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_2` - Documentar pocos escenarios
   * :ref:`runtime_tip_11` - Usar diagramas de secuencia




:Tip: 6-5
:Tema: Escenarios para descubrir bloques
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1