.. _bloques_tip_18:

===============================================================
Tip 5-18: ¡Asegura que **cada** pieza de código fuente pueda localizarse en la vista de bloques de construcción!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   La **vista de bloques de construcción** debe tener un *lugar* apropiado para **cada** pieza de código fuente.

----

La **vista de bloques de construcción** debe tener un *lugar* apropiado para **cada** pieza de código fuente. En otras palabras:

Debe haber un **bloque de construcción** de arquitectura para cada línea única de código fuente que se crea específicamente para ese sistema.

Podrías diferir herramientas de infraestructura (como sistemas de construcción específicos, generadores de código o cosas similares) a la sección 8 (conceptos transversales) - pero a menudo es una buena idea al menos mencionarlos en el nivel 1 de la **vista de bloques de construcción**.

Esta es la única llamada a completitud que proponemos para documentación (ya que la completitud es de otra manera excesivamente costosa de lograr - y **no** debes esforzarte por completitud en nada más)

Ver el siguiente diagrama para un ejemplo:

.. figure:: ../figuras/05-infrastructure-in-building-block-view.jpg
   :alt: Infraestructura en vista de bloques de construcción
   :align: center
   :width: 80%
   
   Generador de código como bloque de construcción

El ``Code Generator`` (sombreado en color amarillo en la esquina inferior izquierda) genera otro **bloque de construcción** arquitectónico ("Campaign Data Management").

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción

----

:Tip: 5-18
:Tema: Completitud del código
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
