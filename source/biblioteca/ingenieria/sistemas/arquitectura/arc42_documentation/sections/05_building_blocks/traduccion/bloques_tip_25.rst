.. _bloques_tip_25:




Tip 5-25: ¡Si es útil, refina varios bloques de construcción a la vez!
======================================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Puedes refinar varias **cajas negras** a la vez en una **caja blanca** mutua. Eso podría ser útil si estos **bloques de construcción** interactúan intensamente, cooperan o proporcionan **interfaces** similares.




Puedes refinar varias **cajas negras** a la vez en una **caja blanca** mutua. Eso podría ser útil si estos **bloques de construcción** interactúan intensamente, cooperan o proporcionan **interfaces** similares.

Encuentras un ejemplo en el diagrama abajo: En la parte izquierda de este diagrama encuentras una **caja blanca** (nivel 1) que contiene dos **cajas negras** ``Foo`` y ``Bar``.

Ambas son refinadas en una sola **caja blanca** en el lado derecho del diagrama. Consistentemente, todas las **interfaces** del nivel 1 están contenidas en el nivel 2.

El *origen* de las **cajas negras** refinadas (nivel 2) se da mediante prefijos.

.. .. figure:: ../figuras/05-mutual-refinement.webp
..       :alt: Caja blanca con dos cajas negras refinadas a una sola caja blanca
..       :align: center
..       :width: 85%
   
..       Refinamiento mutuo: Dos cajas negras refinadas juntas

.. warning::
   Aplica este tip con cuidado, ya que viola la **descomposición** jerárquica limpia usualmente aplicada en la **vista de bloques de construcción**.

Cuándo Usar Refinamiento Mutuo
==============================

**Es apropiado cuando:**

* Los **bloques de construcción** tienen alta cohesión funcional
* Comparten muchas **interfaces** o datos
* La separación artificial crearía complejidad innecesaria
* El acoplamiento entre ellos es inevitable y significativo

**Evitar cuando:**

* Los **bloques de construcción** son independientes
* La **jerarquía** limpia es más importante
* La claridad de estructura se vería comprometida




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_2` - Jerarquía de bloques
   * :ref:`bloques_tip_12` - Refinamiento consistente




:Tip: 5-25
:Tema: Refinamiento mutuo de bloques
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
