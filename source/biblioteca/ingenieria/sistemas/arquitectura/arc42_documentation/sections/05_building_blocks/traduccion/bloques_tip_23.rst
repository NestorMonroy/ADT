.. _bloques_tip_23:

===============================================================
Tip 5-23: ¡Documenta o especifica interfaces con escenarios de tiempo de ejecución!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Algunas **interfaces** requieren varias interacciones entre **bloques de construcción** participantes (handshakes, protocolos de negocio o técnicos).

----

Algunas **interfaces** requieren varias interacciones entre **bloques de construcción** participantes (handshakes, **protocolos** de negocio o técnicos).

Puedes describir o especificar tales interacciones mediante escenarios de tiempo de ejecución, sección 6 de arc42.

Debes referenciar tales escenarios desde la documentación de los **bloques de construcción** participantes.

Cuándo Usar Este Enfoque
=========================

Este enfoque es especialmente útil cuando:

* La **interfaz** involucra múltiples pasos de comunicación
* Existe un **protocolo** o secuencia específica que debe seguirse
* Las interacciones tienen aspectos temporales importantes
* Los handshakes o negociaciones son complejos
* Se requiere sincronización entre **bloques de construcción**

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * Sección 6 de arc42 - Vista de Tiempo de Ejecución
   * :ref:`bloques_tip_9` - Vistas de tiempo de ejecución para cajas blancas

----

:Tip: 5-23
:Tema: Interfaces con escenarios de runtime
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
