.. _runtime_tip_9:

===============================================================
Tip 6-9: ¡Usa una notación textual para describir escenarios de tiempo de ejecución!
===============================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Usa `PlantUML <https://plantuml.com/>`_ para describir o especificar **escenarios de tiempo de ejecución**. Tiene una sintaxis textual ligera (DSL) para **diagramas de secuencia** y **diagramas de actividad**.

----

Nuestra sugerencia para equipos de desarrollo: Usa `PlantUML <https://plantuml.com/>`_ para describir o especificar **escenarios de tiempo de ejecución**. Tiene una sintaxis textual ligera (DSL) para **diagramas de secuencia** y **diagramas de actividad** - fácil de entender y una opción ligera para discutir y visualizar actividades y **procesos**.

.. code-block:: plantuml

   @startuml
   skinparam componentStyle uml2
   
   actor Admin
   participant "Import\nHandler" as IH
   participant "ftp-in" as ftp
   participant "Optical\nArchive" as OA
   participant "Data\nManagement" as DM
   participant "Error\nHandler" as EH
   
   Admin -> IH: import( m )
   IH -> Configuration: getMandatorCfg
   IH -> ftp: readFile
   ftp --> IH: file
   IH -> OA : storeFile(file)
   IH -> IH: setupFilterChain
   IH -> IH: unzip(file)
   IH -> IH: decrypt(uzFile)
   
   alt parse file
   loop all records
   IH -> IH: parse record
   IH -> DM : store client
   else record error
   IH -> EH: log record error
   end
   else file error
   IH -> EH: log file error
   end
   
   @enduml

El diagrama (renderizado) de esta descripción textual se muestra debajo:

.. figure:: ../figuras/06-textual-sequence.png
   :alt: Diagrama de secuencia renderizado desde descripción textual
   :align: center
   :width: 50%
   
   Diagrama de secuencia generado desde notación textual

El Texto es Más Fácil para Desarrolladores
===========================================

Tales descripciones textuales (un DSL para **escenarios**) se asemejan a código fuente - lo cual es a menudo fácil para desarrolladores crear y mantener.

Pueden:

* Usar este DSL para esbozar y discutir variantes de **escenarios**
* Mantener las representaciones textuales en herramientas comunes de versionamiento (git, subversion etc), con las opciones establecidas de ramificación y fusión
* En caso de que tales **escenarios** sean (después...) implementados en código fuente, los diagramas podrían ser eliminados, lo cual resultará en documentación más ligera (ver tip 6-5 (escenarios para discusión, no documentación)).

----

.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_5` - PlantUML para escenarios
   * :ref:`runtime_tip_11` - Diagramas de secuencia

----

:Tip: 6-9
:Tema: Notación textual para escenarios
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1