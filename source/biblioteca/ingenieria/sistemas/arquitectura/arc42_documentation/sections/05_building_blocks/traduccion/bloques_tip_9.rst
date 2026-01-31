.. _bloques_tip_9:




Tip 5-9: ¡Usa vistas de tiempo de ejecución para explicar o especificar cajas blancas!
======================================================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   En caso de que quieras influenciar la **estructura interna** de una **caja blanca**, pero no quieras especificar todos los detalles, puedes aplicar técnicas de la vista de tiempo de ejecución.




En caso de que quieras influenciar la **estructura interna** de una **caja blanca**, pero no quieras especificar todos los detalles, puedes aplicar técnicas de la vista de tiempo de ejecución:

Describe el comportamiento (de tiempo de ejecución) requerido de la **caja blanca**, por ejemplo con:

* Pseudo-código
* Diagramas de actividad o diagramas de flujo
* Diagramas de estado o máquinas de estado

Tal información proporciona a arquitectos o desarrolladores *algo* de información de *cómo* esta **caja blanca** debe ser construida o creada, pero no especifica todos los detalles contenidos.

Ventajas de Este Enfoque
========================

* **Flexibilidad:** Permites diferentes implementaciones mientras mantienes el comportamiento deseado
* **Abstracción apropiada:** No sobre-especificas los detalles de implementación
* **Comunicación clara:** El comportamiento dinámico a menudo es más fácil de entender que estructuras estáticas




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Plantilla de caja blanca
   * Sección 6 de arc42 - Vista de Tiempo de Ejecución




:Tip: 5-9
:Tema: Vistas de tiempo de ejecución
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
