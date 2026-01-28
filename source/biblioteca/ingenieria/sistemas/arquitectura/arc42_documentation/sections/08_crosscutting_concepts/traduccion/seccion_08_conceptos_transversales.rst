.. meta::
   :category: arc42-doc-section
   :layout: seccion
   :title: 8 - Conceptos
   :permalink: /seccion-8/
   :order: 12

.. _seccion-8:

================================
8. Conceptos Transversales
================================

.. rst-class:: arc42-help

Contenido
=========

Esta sección describe conceptos transversales (prácticas, patrones, regulaciones o ideas de solución).
Tales conceptos están frecuentemente relacionados con múltiples bloques de construcción.
Pueden incluir muchos temas diferentes, como los temas mostrados en el siguiente diagrama:

.. figure:: {{ site.imageurl }}/8-concepts/08-concepts-EN.drawio.png
   :alt: Diagrama de conceptos transversales

   Diagrama de conceptos transversales

Motivación
==========

Los conceptos forman la base para la *integridad conceptual* (consistencia, homogeneidad) de la arquitectura.
Por lo tanto, son una contribución importante para lograr las cualidades internas de su sistema.

Este es el lugar en la plantilla que proporcionamos para una especificación cohesiva de tales conceptos.

Muchos de estos conceptos se relacionan con o influyen en varios de sus bloques de construcción.

Forma
=====

La forma puede ser variada:

* documentos de concepto con cualquier tipo de estructura
* implementaciones de ejemplo, especialmente para conceptos técnicos
* extractos de modelos transversales o escenarios usando notaciones de las vistas de arquitectura

Estructura de esta Sección
===========================

Elija **solo** los temas más necesarios para su sistema y asigne a cada uno un encabezado de nivel 2 en esta sección (por ejemplo, 8.1, 8.2, etc.).

.. warning::
   NO INTENTE cubrir todos los temas del diagrama mencionado anteriormente.

Antecedentes
============

Algunos temas dentro de los sistemas a menudo conciernen a múltiples bloques de construcción, elementos de hardware o procesos de desarrollo.
Podría ser más fácil comunicar o documentar tales temas *transversales* en una ubicación central, en lugar de repetirlos en la descripción de los bloques de construcción, elementos de hardware o procesos de desarrollo concernidos.

Ciertos conceptos podrían concernir a **todos** los elementos de un sistema, otros podrían ser relevantes solo para algunos.
En el diagrama anterior, el logging concierne a los tres componentes, mientras que la seguridad es relevante solo para dos componentes.

Algunos ejemplos de la vida real:

* Dentro de un sistema, se debe establecer un formato común para los mensajes de log, combinado con una convención común para elegir el destino de log apropiado.
  Estas decisiones, junto con ejemplos de implementación, podrían describirse como "concepto de logging".
* Un sistema tiene numerosos servicios backend, que se comunican entre sí basándose en llamadas a procedimientos remotos o REST basado en https.

  * Los servicios llamantes ("consumidores") siempre necesitan autenticarse ante el servicio llamado ("proveedor").
  * Para esta autenticación, se debe usar un servicio de autorización central común.
  * Los detalles técnicos y organizacionales de tal autenticación podrían describirse como "concepto de autenticación backend".

* (tomado del HTML Sanity Checker, ver abajo):
  Todos los (7+) componentes checker dentro del sistema están estructurados según el patrón estrategia.

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos
   :glob:

   traduccion/crosscutting_*ejemplo*

.. note::
   **Información adicional**
   
   Para más información sobre conceptos transversales y/o conceptos técnicos, consulte:
   
   * Categoría de conceptos en arc42
   * FAQ de arc42: https://faq.arc42.org/category_c/#c-sec-8

_<describa los conceptos aquí>_
