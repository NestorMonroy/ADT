.. _runtime_tip_10:

===============================================================
Tip 6-10: ¡Usa bloques de construcción tanto pequeños como grandes en escenarios!
===============================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Puedes mezclar **bloques de construcción** de varios niveles de abstracción (o tamaños) en **escenarios** únicos, en lugar de mostrar todas las interacciones de bajo nivel.

----

Para ahorrar esfuerzo, puedes mezclar **bloques de construcción** de varios niveles de abstracción (o tamaños) en **escenarios** únicos, en lugar de mostrar todas las interacciones de bajo nivel.

Ve el siguiente ejemplo (jerarquía de **bloques de construcción** a la izquierda, un **escenario** a la derecha)

.. figure:: ../figuras/06-mixed-abstraction-levels.webp
   :alt: Jerarquía de bloques de construcción a la izquierda, un escenario a la derecha
   :align: center
   :width: 70%
   
   Mezclando niveles de abstracción en un escenario

Mezclar Niveles de Abstracción Ahorra Esfuerzo
===============================================

Como muestras algunos **bloques de construcción** grandes o más abstractos, ocultas su funcionamiento interno o **procesos** internos dentro del **escenario**. En el ejemplo de arriba, ocultas completamente el funcionamiento interno del **bloque de construcción** ``B``... simplemente no describes o especificas qué y cómo ``B`` está realizando sus tareas.

----

.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`runtime_tip_1` - Mapear bloques a actividades
   * :ref:`runtime_tip_3` - Escenarios esquemáticos

----

:Tip: 6-10
:Tema: Bloques grandes y pequeños en escenarios
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1