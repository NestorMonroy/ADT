.. _runtime_tip_1:

===============================================================
Tip 6-1: ¡Siempre mapea los bloques de construcción existentes a las actividades dentro de los escenarios de tiempo de ejecución!
===============================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Los **escenarios de tiempo de ejecución** muestran la **interacción** de **bloques de construcción**. Siempre usa elementos de tu **vista de bloques de construcción** dentro de estos **escenarios**.

----

Los **escenarios de tiempo de ejecución** muestran (documentan o especifican) la **interacción** de **bloques de construcción** o sus **instancias**. Siempre debes usar elementos de tu **vista de bloques de construcción** (o sus contrapartes de tiempo de ejecución, como **instancias** de clases) dentro de estos **escenarios**. Describen *cómo el sistema cumple ciertas **responsabilidades*** o tareas, qué **bloques de construcción** están involucrados.

Por favor contrasta esos **escenarios de tiempo de ejecución** con *funciones requeridas*: Esas describen un **proceso** requerido o secuencia de pasos que el sistema de alguna manera necesita ejecutar o realizar (pero sin importar qué elemento del sistema realmente lo hace).

Es una tarea arquitectónica importante mapear desde las últimas (requisitos) a los **bloques de construcción**. En otras palabras: Necesitas asignar **responsabilidades** a tus **bloques de construcción**.

Para este mapeo tienes varias opciones:

* **Diagramas de secuencia** UML, que inmediatamente muestran el mapeo de actividades a **bloques de construcción** (ver tip de diagramas de secuencia).
* **Diagramas de actividad** o **diagramas de flujo** con *carriles* (swimlanes) mostrando este mapeo.
* Descripciones textuales o listas numeradas: Ahí tienes que cuidar manualmente el mapeo...

----

.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`runtime_tip_11` - Diagramas de secuencia

----

:Tip: 6-1
:Tema: Mapeo de bloques a actividades
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1