.. _deployment_ejemplo_tpu_1:




Ejemplo de Vista de Despliegue: Traffic Pursuit Unit
====================================================

.. admonition:: Ejemplo arc42
   
   El ejemplo muestra un diagrama de **despliegue** de Enterprise Architect (TM) para mostrar los procesadores usados para implementar la funcionalidad completa de la Traffic Pursuit Unit. Nota las decisiones de diseño (es decir, la tecnología) para los canales conectando los procesadores.




7.1 Vista de Despliegue Nivel 1 (Traffic Pursuit Unit)
======================================================

La siguiente imagen muestra el interior del **hardware** TPU, un rack industrial con la placa PC principal y varias otras Placas de Circuito Impreso (PCBs).

.. .. figure:: ../figuras/examples/tpu/71-HardwareVonOben.webp
..       :alt: Vista de Despliegue Nivel 1 de Traffic Pursuit Unit
..       :align: center
..       :width: 70%
   
..       Hardware interno de TPU

7.1 Nivel de Despliegue 1
=========================

El siguiente diagrama UML muestra esta estructura de **hardware**.

.. .. figure:: ../figuras/examples/tpu/71-Infrastructure.webp
..       :alt: Vista de Despliegue Nivel 1 de Traffic Pursuit Unit
..       :align: center
..       :width: 70%
   
..       Diagrama UML de infraestructura TPU

1. Nodo MeasuringUnit




Este **nodo** consiste principalmente de un PCB base en el cual el MU-CPU-BOARD, el módulo receptor GPS y el multiplexor están montados.

**MU-CPU-Board**

* CPU: Procesador ARM 200 MIIPS a 180 Mhz
* Múltiples líneas RS232 con velocidades hasta 115Kbaud

**Keyboard Switch**

Reenvía la entrada de teclado ya sea al MU-CPU-Board o al PC-board, dependiendo del modo de operación del MeasuringUnit. En modo autónomo (stand-alone) la entrada del usuario es manejada en el MeasuringUnit. En modo video es manejada por el PC-Board.

**GPS receiver**

Transforma la señal de la antena GPS en información de ubicación reenviada al MU-CPU-Board.

* Protocolo binario SIRF o protocolo NMEA

2. PC-Board




Es el procesador central del TPU, principalmente controlando todas las funciones de video del sistema y almacenando resultados relevantes.

* CPU: Intel CPU xx cores
* Ejecutando RT debian Linux
* Múltiples líneas RS232 con velocidades hasta 115Kbaud

3. Video Cards




Este **nodo** contiene todo el **hardware** para procesamiento de video. Sus detalles son descritos en el siguiente capítulo.




.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`deployment_ejemplo_tpu_2` - TPU Nivel 2
   * :ref:`deployment_tip_8` - Explicar nodos




:Ejemplo: Deployment View Traffic Pursuit Unit
:Sistema: TrafficPursuitUnit (TPU)
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1