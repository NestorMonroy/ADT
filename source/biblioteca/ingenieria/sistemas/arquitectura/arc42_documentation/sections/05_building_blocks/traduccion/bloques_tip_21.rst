.. _bloques_tip_21:

===============================================================
Tip 5-21: ¡Describe o especifica interfaces internas con esfuerzo mínimo!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Describe o especifica **interfaces** internas con esfuerzo mínimo: Puedes encontrar detalles arbitrarios de **interfaz** en el código fuente, si lo necesitas.

----

Describe o especifica **interfaces** internas con esfuerzo mínimo: Puedes encontrar detalles arbitrarios de **interfaz** en el código fuente, si lo necesitas.

Ten especial cuidado con las descripciones gráficas de **interfaces** (como UML).

Echa un vistazo al siguiente diagrama, donde ``Blurp`` proporciona un método/servicio ``blurp`` para el consumidor ``FooBar``.

.. figure:: ../figuras/05-interface-simple-variant.png
   :alt: Diagrama de descripción de interfaz simple
   :align: center
   :width: 55%
   
   Interfaz simple: Blurp proporciona servicio blurp a FooBar

Puedes agregar más detalles a este modelo gráfico simple, algunas opciones dadas abajo (con esfuerzo creciente).

Niveles de Detalle de Interfaz
===============================

1. **No explicas esta interfaz**, ya que sabes que el código fuente correspondiente es comprensible o suficientemente simple

2. **Explicas la semántica** de usar esta **interfaz**, es decir:
   
   * Procesos de negocio manejados por la **interfaz**
   * Consecuencias de negocio o técnicas de esta **interfaz**
   * Efectos secundarios potenciales

3. **Explicas tipo de retorno y parámetros** de la llamada (asumiendo interacción síncrona)

4. **Adicionalmente describes atributos de calidad** que son requeridos o proporcionados en esta **interfaz**, por ejemplo:
   
   * ``Blurp`` puede procesar 10 solicitudes por segundo, o
   * ``Blurp`` solo puede ser invocado secuencialmente.
   * Llamar a ``Blurp`` por múltiples clientes llevará a excepciones de tiempo de ejecución.

Recomendación
=============

Comienza con el nivel de detalle más bajo (nivel 1) y solo agrega más detalles si realmente se necesitan. El código fuente suele ser la documentación más actualizada y precisa de **interfaces** técnicas.

Ver También
===========

* Tip 5-22 (documenta interfaces con pruebas unitarias)

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_22` - Interfaces con unit tests

----

:Tip: 5-21
:Tema: Interfaces internas con esfuerzo mínimo
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
