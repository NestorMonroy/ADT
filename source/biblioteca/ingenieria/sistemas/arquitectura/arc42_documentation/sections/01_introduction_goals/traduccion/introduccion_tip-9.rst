.. _introduccion-tip-9:

===================================================================
Consejo 1-9: ¡Usa texto (semi) formal!
===================================================================

.. meta::
   :layout: post
   :title: Consejo 1-9: ¡Usa texto (semi) formal para describir requisitos funcionales!
   :tags: requirement plantUML activity-diagram functional-requirement
   :category: requirements
   :permalink: /tips/1-9/

:Subtítulo: Para describir requisitos funcionales
:Tema: PlantUML y notación semi-formal
:Categoría: Requisitos
:Audiencia: Arquitectos, Desarrolladores

----

Recomendación
=============

Puede ser útil documentar algunas funciones, procesos o características 
importantes en una notación semi-formal.

Considera PlantUML de código abierto (https://plantuml.com/) como ejemplo.

Dada la siguiente descripción de actividad, puede crear una versión gráfica:

.. code-block:: plantuml

   @startuml
   start
     :authenticate;
   
     :select product;
   
     if (private customer?) then (yes)
       :add\\nVAT;
     else (no)
       :request\\nVAT_ID;
     endif
   
     :create invoice;
   stop
   
   @enduml

----

Ventajas
========

Las actividades se describen entre ``:`` y ``;``, las ramas se pueden leer como 
pseudocódigo y de esa manera combinas los beneficios del texto plano con la 
representación gráfica.

PlantUML renderiza el código anterior al siguiente diagrama:

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/01-simple-activity.png
   :alt: Diagrama generado por PlantUML
   :align: center
   :width: 40%

   Diagrama de actividad generado por PlantUML

----

.. note::
   **Información de traducción:**
   
   - Archivo original: 2016-03-01-t-1-9.md
   - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
   - Fecha: 2026-01-27
