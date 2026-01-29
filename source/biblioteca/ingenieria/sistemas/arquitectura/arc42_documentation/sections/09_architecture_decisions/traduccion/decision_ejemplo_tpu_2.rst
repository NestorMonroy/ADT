=====================================================
Ejemplo de Decisión: TrafficPursuitUnit
=====================================================

.. meta::
   :layout: post
   :title: Ejemplo de Decisión: TrafficPursuitUnit
   :tags: decisión, ejemplo
   :category: decisiones
   :permalink: /examples/decision-tpu-1/

9. Decisiones de Arquitectura
==============================

Cálculo eficiente
-----------------

Para realizar cálculos lo más rápido posible y ahorrar poder de CPU, todos los cálculos se realizan con enteros (punto fijo). Los cálculos con flotantes solo se usan si son inevitables (por ejemplo, extracción de raíz para el teorema de Pitágoras).

Buffering de información de video
----------------------------------

La propagación de datos de medición desde la MeasuringUnit a través de la VideoUnit al VideoSubsystem tiene que pasar por líneas seriales y puede sufrir retrasos variables durante el procesamiento dentro de los diferentes nodos. Decidimos lograr un retraso fijo, de manera que los datos renderizados en la pantalla representen exactamente el comportamiento en tiempo real desplazado por un retraso de tiempo fijo. 

Esto se logra manteniendo un buffer de información de video a mostrar en el software insertador de video. La visualización de la primera pieza de información se retrasa hasta que el buffer ha acumulado una reserva de 5 elementos de datos. Esta precaución asegura que cada cuadro de video pueda ser suministrado con datos actuales en el momento correcto. 

El sistema tiene un retraso constante de 200 milisegundos (5 cuadros × 40 ms tiempo por cuadro), por lo que los datos exactos correspondientes al cuadro de video número n se pueden encontrar en los datos insertados en el cuadro número n + 5.

Ajuste de rendimiento en la interfaz al controlador de codec
-------------------------------------------------------------

El software para controlar el codec de video existía inicialmente como un proceso separado externo con una interfaz de comandos. Para mejorar el tiempo de respuesta después de los comandos, se creó una interfaz funcional y el software de control se integró en su propio proceso.
