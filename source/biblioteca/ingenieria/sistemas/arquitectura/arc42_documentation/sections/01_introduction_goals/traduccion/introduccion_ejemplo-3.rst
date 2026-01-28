.. meta::
   :layout: post
   :title: Ejemplo de Vista General: Unidad de Persecución de Tráfico
   :tags: overview example 
   :category: overview
   :permalink: /examples/overview-example-3/

.. _introduccion-ejemplo-3:

===================================================================
Ejemplo de Vista General: Unidad de Persecución de Tráfico
===================================================================

.. note::
   **Ejemplo de arc42:**
   
   Después de un breve texto introductorio que explica el sistema bajo diseño, 
   se presenta una tabla de objetivos clave del proyecto y una vista general 
   de la funcionalidad mostrada como diagrama de casos de uso con tabla adjunta.

----

1. Introducción
===============

Este documento describe la Unidad de Persecución de Tráfico, en inglés Traffic 
Pursuit Unit (TPU), que es un dispositivo de medición de velocidad equipado con 
instalaciones de grabación de video que se instala dentro de un coche de policía. 
Se utiliza para medir y grabar el perfil de velocidad de un coche que conduce 
delante del coche de policía, de modo que las violaciones del límite de velocidad 
puedan probarse y se puedan tomar acciones legales basadas en la documentación y 
grabaciones de video producidas por el sistema.

El desarrollo actual se basa en una versión existente del sistema, que ha sido 
desarrollada por las mismas empresas, y debe llevar el producto a una nueva 
versión con características añadidas y mejoradas habilitadas por los últimos 
desarrollos en tecnología de hardware.

Se han establecido los siguientes objetivos para este sistema:

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Prioridad
     - Objetivo
   * - 1
     - El sistema debe ser mejorado con características que sean adecuadas para 
       mantener y fortalecer la posición como el actual líder del mercado
   * - 2
     - El sistema debe implementar resolución HD para clips de video y 
       almacenamiento de los clips en disco duro
   * - 3
     - Todas las partes del sistema que estén sujetas a aprobación legal deben 
       estar contenidas en una unidad (llamada MeasuringUnit), de modo que el 
       reemplazo de otras partes del sistema no requiera reaprobación del dispositivo
   * - 4
     - La MeasuringUnit debe ser capaz de funcionar de forma autónoma y 
       comercializarse como una variante de bajo costo de TPU sin prueba de video
   * - 5
     - El rango de temperatura operable debe ampliarse a un rango de al menos 
       -25 a 85 grados Celsius

----

1.1 Requisitos
==============

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/tpu-1-UseCases.jpg
   :alt: Introducción - Casos de Uso
   :align: center
   :width: 80%

   Diagrama de Casos de Uso del sistema TPU

.. list-table:: Requisitos Funcionales
   :header-rows: 1
   :widths: 10 30 60

   * - Id
     - Requisito
     - Explicación
   * - F1
     - Realizar calibración automática
     - Realizar una calibración automática por medio de información GPS
   * - F1.1
     - Imprimir protocolo de calibración
     - 
   * - F2
     - Realizar una persecución de un coche
     - Seguir un coche conduciendo a velocidad demasiado alta para crear 
       documentación probatoria
   * - F3
     - Mostrar lista de todas las persecuciones grabadas
     - 
   * - F4
     - Reproducir grabación de una persecución
     - Reproducir la documentación en video de un caso de persecución, 
       por ejemplo, para mostrársela al conductor del coche a cargo
   * - F5
     - Imprimir protocolo de una persecución
     - 
   * - F6
     - Mostrar información básica
     - En estado inactivo, el sistema debe mostrar información por defecto 
       como fecha y hora y la velocidad actual

----

.. note::
   **Información de traducción:**
   
   - Archivo original: 01-overview-example-3.md
   - Método: Peshitta (traducción literal)
   - Fecha: 2026-01-27
