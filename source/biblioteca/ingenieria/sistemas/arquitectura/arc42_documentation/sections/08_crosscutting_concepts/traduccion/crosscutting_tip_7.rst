=========================================================================
Tip 8-7: ¡Documente (al menos) el modelo de datos (de negocio o dominio)!
=========================================================================

.. meta::
   :layout: post
   :title: Tip 8-7: ¡Documente (al menos) el modelo de datos (de negocio o dominio)!
   :tags: concepto, dominio, esencial, plantUML
   :category: conceptos
   :permalink: /tips/8-7/

.. epigraph::

   Sí, sabemos que DDD es mucho más que solo un modelo de datos,
   pero si no tiene al menos sus datos correctos, es probable que su sistema falle...

En caso de que no cree y documente un modelo completo de 'diseño dirigido por el dominio'
que contenga aspectos tanto estáticos como dinámicos, al menos debe crear y documentar
un modelo de datos (de negocio o dominio).

Tal modelo de datos proporciona una visión general de las estructuras de datos fundamentales del sistema
y sus relaciones relevantes.

Tome lo siguiente como un ejemplo breve (basado en una idea de `uml-diagrams.org <https://www.uml-diagrams.org/>`_).
Carece de definiciones o explicaciones adicionales de las entidades y sus relaciones... 
en realidad, debería ser más minucioso...

.. figure:: {{ site.imageurl }}/08-hospital-domain-EN.png
   :width: 70%
   :alt: Ejemplo breve de un modelo de datos, dominio hospitalario
   
   Ejemplo breve de un modelo de datos, dominio hospitalario

Fuente PlantUML
===============

El diagrama anterior se generó automáticamente a partir de la siguiente fuente PlantUML:

.. code-block:: text

   @startuml
   
   interface Person {
   title: String
   lastName: String
   firstname: String
   birthData: Date
   gender: Gender
   postalAddress: Address
   }
   
   Person "1" -left- "1..*" Phone
   
   Person <|-- Patient
   Person <|-- Staff
   
   Person "*" --right-- "*" Hospital
   
   class Hospital {
   name: String
   address: Address
   }
   
   class Department {
   name: String
   location: String
   }
   
   Department "*" -down-* "1" Hospital
   Department "1" -- "1..*" Staff
   
   @enduml

.. note::
   **PlantUML para modelos de datos**
   
   PlantUML es una excelente herramienta para crear diagramas de modelos de datos
   que pueden ser versionados junto con su código.
