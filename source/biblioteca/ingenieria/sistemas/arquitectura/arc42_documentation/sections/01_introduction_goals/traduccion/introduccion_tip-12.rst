.. meta::
   :layout: post
   :title: Consejo 1-12: ¡Explica los requisitos de calidad mediante escenarios!
   :tags: requirement quality scenario essential 
   :category: requirements
   :permalink: /tips/1-12/

.. _introduccion-tip-12:

===================================================================
Consejo 1-12: ¡Explica requisitos mediante escenarios!
===================================================================

:Subtítulo: Requisitos de calidad mediante escenarios
:Tema: Escenarios de calidad
:Categoría: Requisitos
:Audiencia: Arquitectos, Stakeholders

----

Recomendación
=============

Los escenarios de calidad explican en oraciones cortas cómo debe reaccionar el 
sistema en ciertas situaciones ante ciertos eventos.

Hay varias categorías de estos escenarios:

- **Escenarios de uso:** ¿Cómo reacciona el sistema en ciertos tipos de uso? En 
  el ejemplo a continuación: El tiempo de ejecución de una validación HTML no 
  debe exceder 5 segundos.

- **Escenarios de cambio:** ¿Cómo se comporta el sistema cuando lo cambias o 
  extiendes? Esto te permite identificar qué tan rápido se pueden realizar 
  ciertos tipos de cambios o extensiones, o cuánto esfuerzo probablemente se 
  necesita.

- **Escenarios de falla o tiempo de inactividad:** ¿Cómo se comporta el sistema 
  cuando ocurre un problema grave, como la falla de componentes de hardware o 
  software centrales?

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/01-quality-scenarios-schematic.png
   :alt: Esquema de escenarios de requisitos de calidad
   :align: center
   :width: 80%

   Esquema de escenarios de requisitos de calidad

Los escenarios pueden relacionarse con una variedad de posibles atributos de 
calidad, que están estructurados jerárquicamente por modelos de calidad actuales 
(por ejemplo, ISO-25010).

----

Ejemplos de Escenarios
======================

Escenarios de cambio
--------------------

- Un nuevo algoritmo para el enrutamiento de robots en un almacén de gran altura 
  necesita ser integrado. Un desarrollador puede realizar este cambio dentro de 
  4 horas, incluyendo las modificaciones de la compilación y las pruebas unitarias 
  e de integración.

- Al final del año, el formato de salida de los informes (anuales) debe ajustarse 
  para cumplir con nuevos requisitos legales. Todos los datos requeridos ya están 
  en la base de datos y los cambios afectan el diseño, el formato y las agregaciones. 
  Estos cambios se pueden implementar completamente en un máximo de 60 horas-persona.

Escenarios de uso
-----------------

- El sistema selecciona los datos necesarios para el proceso XY en 1 segundo (hasta 
  100 usuarios concurrentes) o en 3 segundos (hasta 1,000 usuarios concurrentes).

- Después de encender, toma como máximo 4 segundos hasta que el sistema de navegación 
  acepta entrada desde la GUI.

----

.. note::
   **Información de traducción:**
   
   - Archivo original: 2016-03-02-t-1-12.md
   - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
   - Paso 3.4 aplicado: "quality scenarios", "quality attributes"
   - Fecha: 2026-01-27
