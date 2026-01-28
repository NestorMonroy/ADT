.. _bloques_ejemplo_tpu_nivel_2:

===============================================================
Ejemplo Vista de Bloques Nivel 2: Traffic Pursuit Unit
===============================================================

.. note::
   **Ejemplo arc42**
   
   Este diagrama (creado con Enterprise Architect(TM) como un modelo de **componentes**) muestra el refinamiento de la caja de medición incluyendo las descripciones de **caja negra** del nivel 2.

----

5.2 Measuring Unit (Vista de Bloques de Construcción Nivel 2)
==============================================================

La siguiente figura muestra la **estructura interna** de la Measuring Unit.

.. figure:: ../figuras/52-tpu-BuildingBlocks.jpg
   :alt: Vista de Bloques de Construcción Nivel 2 de Traffic Pursuit Unit
   :align: center
   :width: 90%
   
   Vista de Bloques de Construcción Nivel 2 de Traffic Pursuit Unit - Measuring Unit

----

Bloques de Construcción Nivel 2
================================

1.1 MuServices
--------------

Contiene los servicios ofrecidos por la MeasuringUnit y ofrece estos a través de una **interfaz** RPC. Estos servicios son:

* Entregar actualizaciones periódicas de datos ambientales y de medición
* Realizar una persecución
* Realizar una calibración automática
* Realizar una calibración manual
* Imprimir protocolo de persecución
* Imprimir datos de calibración

1.2 Pursuit
-----------

Implementa la lógica operacional, todos los cálculos y almacenamiento de los datos de una persecución.

1.3 Calibrate
-------------

Implementa todas las funciones para realizar una calibración automática y verificar permanentemente la validez de los datos de calibración actuales.

1.4 PrintService
----------------

Maneja el diseño y formateo de documentos que describen persecuciones o calibraciones y los renderiza según el tipo de impresoras conectadas. Implementa una cola de impresión para imprimir los documentos en la impresora conectada.

1.5 SimpleTPU
-------------

Implementa la **interfaz** de usuario y la lógica de control para ejecutar una TPU sin funcionalidad de video basada solo en el hardware y software de la Measuring Unit.

1.6 Config
----------

Contiene todos los datos de configuración concernientes al comportamiento y los parámetros legales para las mediciones.

1.7 MuInit
----------

Se ejecuta solo una vez para inicializar y arrancar todos los servicios dentro de la MeasuringUnit.

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_2` - Nivel 2
   * :ref:`bloques_ejemplo_tpu_nivel_1` - TPU Nivel 1

----

:Ejemplo: Traffic Pursuit Unit - Measuring Unit
:Sistema: TPU
:Nivel: 2
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
