.. _deployment_tip_2:

===============================================================
Tip 7-2: ¡Explica las decisiones de hardware e infraestructura!
===============================================================

.. tip::
   **Consejo de Vista de Despliegue arc42**
   
   Los diagramas de **despliegue** o **infraestructura** soportan el entendimiento general del **hardware** subyacente. Además, es útil entender el razonamiento detrás de las decisiones.

----

Los diagramas de **despliegue** o **infraestructura** soportan el entendimiento general del **hardware** subyacente.

Además de esta vista general, es útil entender el razonamiento detrás de las decisiones de **hardware**, la selección de máquinas específicas, procesadores u otros **dispositivos**.

Si el **hardware** juega un rol importante en la arquitectura, puedes incluso usar una plantilla de **nodo** para ese propósito, similar a la siguiente tabla:

Nodo <nombre-nodo>
==================

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Responsabilidad**
     - ¿Cuál es el rol de este elemento de **hardware**, qué está haciendo?
   * - **Características (técnicas)**
     - Es decir, número de cpus/cores, memoria, throughput, número de puertos, vendor, modelo...
   * - **Bloques de construcción asociados**
     - ¿Qué parte del software se ejecuta en este **hardware**?
   * - **Razón para la selección**
     - ¿Por qué fue este **hardware** particular seleccionado?

----

.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`deployment_tip_1` - Documentar infraestructura técnica
   * :ref:`deployment_tip_8` - Explicar nodos

----

:Tip: 7-2
:Tema: Explicar decisiones de hardware
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1