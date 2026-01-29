.. _bloques_ejemplo_tpu_nivel_1:

===============================================================
Ejemplo Vista de Bloques Nivel 1: Traffic Pursuit Unit
===============================================================

.. note::
   **Ejemplo arc42**
   
   Este diagrama de Nivel 1 ha sido creado con Enterprise Architect(TM) como un diagrama de **componentes**. Está aumentado por una lista de descripciones de **caja negra** para cada **bloque de construcción**.

----

5.1 Vista de Bloques de Construcción Nivel 1
=============================================

La siguiente figura muestra la **descomposición** de nivel superior interno de la Traffic Pursuit Unit. La **descomposición** está principalmente impulsada por el **despliegue** de estos **bloques de construcción** de nivel superior en diferentes hardware (cf. capítulo 7). Note que las cajas azules son bloques de software puros, mientras que la blanca es todavía una mezcla de funcionalidad de hardware y software.

.. figure:: ../figuras/51-tpu-BuildingBlocks.jpg
   :alt: Vista de Bloques de Construcción Nivel 1 de Traffic Pursuit Unit
   :align: center
   :width: 90%
   
   Vista de Bloques de Construcción Nivel 1 de Traffic Pursuit Unit

----

Bloques de Construcción Nivel 1
================================

1. Measuring Unit (Unidad de Medición)

---------------------------------------

Es responsable de todas las mediciones (velocidad, tiempo, datos GPS, temperatura, datos de persecución) y del cálculo y almacenamiento de todos los datos legalmente relevantes.

Puede ejecutarse standalone, sin estar conectada a la VideoUnit, realizando persecuciones simples sin video. En este caso implementa su propia **interfaz** de usuario simple mediante un teclado con pantalla alfanumérica.

2. VideoUnit (Unidad de Video)

-------------------------------

Controla la operación de la MeasuringUnit (cuando no está operando standalone). Recolecta todos los datos actuales de la MeasuringUnit, los formatea y los despacha al UserInserter y el LegalInserter para visualización.

También implementa la **interfaz** gráfica de usuario y la funcionalidad para crear, almacenar y administrar videos.

Al comunicarse con el **módulo** PowerControl, realiza un apagado seguro cuando se apaga el encendido.

3. Video Subsystem (Subsistema de Video)

-----------------------------------------

Resume toda la funcionalidad de hardware y software que se ejecuta en las placas de video. Maneja todas las operaciones de video desde los cuadros de video entrantes hasta su visualización en la pantalla, incluyendo todas las transiciones entre señales de video analógicas y digitales. Contiene el codec que comprime el flujo de video de la grabación y decodifica videoclips grabados para reproducción.

4. PowerControl (Control de Energía)

-------------------------------------

Es responsable del monitoreo del estado del encendido, para soportar un apagado regular del Sistema Linux. Después del apagado, la TPU puede apagarse de forma segura para evitar que drene la batería del automóvil.

Cuando se apaga el encendido, este **componente** comunica este hecho a la VideoUnit para solicitar el apagado, y espera la información de que el sistema se ha apagado de forma segura. Luego apaga la TPU.

----

Interfaces Importantes
======================

MeasuringUnit-If
----------------

Esta **interfaz** proporciona toda la funcionalidad para controlar y acceder a la funcionalidad de medición de la Measuring Unit. Está implementada mediante llamada a procedimiento remoto, y puede accederse tanto internamente como externamente por otro nodo.

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Caja Blanca del Sistema General
   * :ref:`bloques_ejemplo_tpu_nivel_2` - TPU Nivel 2

----

:Ejemplo: Traffic Pursuit Unit
:Sistema: TPU
:Nivel: 1
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
