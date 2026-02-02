.. _contexto_tip_8:




Tip 3-8: ¡Agrega (agrupa) sistemas vecinos similares con puertos!
=================================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Si tu sistema interactúa con muchos sistemas externos, podrías usar símbolos de puerto UML para denotar categorías (o clusters) de tales **vecinos**, en lugar de mostrar todos los sistemas externos como símbolos separados.




Eso se ve similar al tip 3-7 (categorías de sistemas externos), pero no requiere el uso de estereotipos y podría ahorrar algo de esfuerzo de dibujo.

Los puertos tienen la gran ventaja de que conectan el interior y el exterior: Puedes representar qué **caja negra** interna se comunica con cuál de los **vecinos** externos.

Ver los ejemplos a continuación: Primero ves un **contexto** con puertos, abajo encuentras la versión más extensiva con puertos y **sistemas vecinos** explícitos.

.. .. figure:: ../figuras/03-context-with-ports.png
..       :alt: Contexto con puertos
..       :align: center
..       :width: 80%
   
..       Contexto usando puertos para agrupar vecinos

.. .. figure:: ../figuras/03-big-context.png
..       :alt: Contexto grande con puertos y sistemas explícitos
..       :align: center
..       :width: 80%
   
..       Versión extensiva: puertos con sistemas vecinos explícitos




.. seealso::
   * :ref:`seccion_03` - Contexto y Alcance
   * :ref:`contexto_tip_7` - Agregación por criterios




:Tip: 3-8
:Tema: Puertos UML para agrupar
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
