.. _runtime_ejemplo_tpu:




Ejemplo de Vista de Tiempo de Ejecución: TrafficPursuitUnit
===========================================================

.. admonition:: Ejemplo arc42
   
   Un diagrama simple con una breve explicación textual.




6. Vista de Tiempo de Ejecución




6.1 Procesamiento y Propagación de Datos de Medición
====================================================

Los siguientes cuatro diagramas muestran cuatro diagramas UML diferentes para el mismo **escenario** (es decir, el procesamiento y propagación de todos los datos de medición: pulsos del velocímetro, ...)

Los pasos clave en este **escenario** son los siguientes:

1. TPU recibe señales continuas del velocímetro.
2. Cada 40ms (es decir, 25 veces por segundo) el sistema mide la distancia recorrida y actualiza la línea inferior en la pantalla vía el insertador legal.
3. Cada segundo los datos completos de persecución son calculados y mostrados en el área inferior y superior de la pantalla vía insertador legal e insertador de usuario.

El siguiente **diagrama de secuencia** muestra este **proceso**: la medición repetida de pulsos del velocímetro cada 40ms (en la parte superior del diagrama) y la actualización completa cada segundo (en la parte inferior del diagrama).

.. .. figure:: ../figuras/examples/tpu/III61_MeasurementPropagationSD.webp
..       :alt: Fig. 6.1: Diagrama de Secuencia
..       :align: center
..       :width: 70%
   
..       Fig. 6.1: Diagrama de Secuencia

El diagrama de comunicación se usa en el estilo de un **diagrama de flujo** de datos, mostrando la entrada original (pulsos del velocímetro) en la esquina inferior izquierda y todos los resultados intermedios calculados en su camino a los dos insertadores.

La medición continua de los pulsos del velocímetro está marcada como paso 1 (en negro), la propagación de la distancia por cuadro al insertador legal se muestra con números rojos. El cálculo final cada segundo se muestra con números verdes.

.. .. figure:: ../figuras/examples/tpu/III61_MeasurementPropagationCD.jpg
..       :alt: Fig. 6.2: Diagrama de Comunicación
..       :align: center
..       :width: 70%
   
..       Fig. 6.2: Diagrama de Comunicación

El siguiente **diagrama de actividad** muestra el **escenario** - ignorando la concurrencia. Muestra los flujos de datos entre actividades en los **bloques de construcción**. Los nombres de los **bloques de construcción** se denotan debajo de los nombres de actividad en llaves.

.. .. figure:: ../figuras/examples/tpu/III61_MeasurementPropagationAD.jpg
..       :alt: Fig. 6.3: Diagrama de Actividad
..       :align: center
..       :width: 70%
   
..       Fig. 6.3: Diagrama de Actividad

Este **diagrama de actividad** extendido incluye la concurrencia mostrando **diagramas de actividad** comunicándose asincrónicamente (usando los símbolos "send-signal-action" y "accept-event-action" del UML). El diagrama está sobrepuesto con **carriles** (swim lanes) de los **bloques de construcción** de nivel 1.

.. .. figure:: ../figuras/examples/tpu/III61_MeasurementPropagationAD-EXT.webp
..       :alt: Fig. 6.4: Diagrama de Actividad Extendido
..       :align: center
..       :width: 70%
   
..       Fig. 6.4: Diagrama de Actividad Extendido con concurrencia




.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_11` - Diagramas de secuencia
   * :ref:`runtime_tip_7` - Diagramas de actividad con swimlanes




:Ejemplo: Runtime View Traffic Pursuit Unit
:Sistema: TrafficPursuitUnit (TPU)
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1