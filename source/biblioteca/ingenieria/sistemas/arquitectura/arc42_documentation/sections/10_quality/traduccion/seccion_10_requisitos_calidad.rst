.. _seccion_10:

===============================================================
Sección 10: Requisitos de Calidad (Quality Requirements)
===============================================================

.. tip::
   **Requisitos de Calidad arc42**
   
   Los **requisitos de calidad** son fundamentales para las **decisiones arquitectónicas**. Esta sección captura todos los **requisitos de calidad** relevantes, desde los críticos (ya descritos en objetivos de calidad) hasta los deseables.

----

Introducción
============

Esta sección contiene todos los **requisitos de calidad** relevantes para el sistema.

Contenido
=========

Esta sección contiene todos los **requisitos de calidad** relevantes.

Los más importantes de estos requisitos ya han sido descritos en la sección 1.2 (objetivos de calidad), por lo tanto solo deben ser referenciados aquí.

En esta sección 10 también deberías capturar **requisitos de calidad** de menor importancia, que no crearán riesgos altos cuando no se logren completamente (pero podrían ser *nice-to-have*).

Motivación
==========

Dado que los **requisitos de calidad** tendrán mucha influencia en las **decisiones arquitectónicas**, debes saber qué cualidades son realmente importantes para tus **stakeholders**, de una manera específica y medible.

Información Adicional
=====================

Ver el extenso `modelo de calidad Q42 en https://quality.arc42.org <https://quality.arc42.org>`_.

----

10.1 Resumen de Requisitos de Calidad
======================================

Contenido
---------

Un resumen u overview de los **requisitos de calidad**.

Motivación
----------

A menudo encontramos docenas (o incluso cientos) de **requisitos de calidad** detallados.

En esta sección de resumen deberías intentar resumir, por ejemplo describiendo categorías o temas (como sugiere `ISO 25010:2023 <https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:ed-2:v1:en>`_ o `Q42 <https://quality.arc42.org>`_).

Si estas descripciones resumidas ya son suficientemente precisas, específicas y medibles, puedes omitir la sección 10.2.

Forma
-----

Usa una tabla simple en la cual cada línea contiene una categoría o tema y una breve descripción del **requisito de calidad**.

Alternativamente, puedes usar un **mindmap** para estructurar estos **requisitos de calidad**.

En la literatura, también se ha descrito la idea de un *quality attribute tree* (árbol de atributos de calidad), que coloca el término genérico "calidad" como la raíz y usa un refinamiento tipo árbol del término "calidad".

[Bass+21] introdujo el término "**Quality Attribute Utility Tree**" para este propósito.

**Plantilla:**

*< Proporciona aquí un resumen de requisitos de calidad >*

----

10.2 Escenarios de Calidad
===========================

Contenido
---------

Los **escenarios de calidad** hacen concretos los **requisitos de calidad** y permiten decidir si se cumplen (en el sentido de criterios de aceptación).

Asegúrate de que tus escenarios sean específicos y medibles.

Dos tipos de escenarios son especialmente útiles:

* **Escenarios de uso** (también llamados escenarios de aplicación o escenarios de caso de uso) describen la reacción en tiempo de ejecución del sistema a cierto estímulo. Esto también incluye escenarios que describen la eficiencia o **rendimiento** del sistema. **Ejemplo:** El sistema reacciona a una solicitud del usuario en un segundo.

* **Escenarios de cambio** describen el efecto deseado de una modificación o extensión del sistema o de su entorno inmediato. **Ejemplo:** Se implementa funcionalidad adicional o cambian los requisitos para un atributo de calidad, y se mide el esfuerzo o duración del cambio.

Forma
-----

La información típica para escenarios detallados incluye lo siguiente:

**Forma corta** (favorecida en el modelo Q42):

* **Contexto/Antecedentes**: ¿Qué tipo de sistema o componente, cuál es el entorno o situación?
* **Fuente/Estímulo**: ¿Quién o qué inicia o desencadena un comportamiento, reacción o acción?
* **Métrica/Criterios de Aceptación**: Una respuesta incluyendo una *medida* o *métrica*

**Forma larga** de escenarios (favorecida por el SEI y [Bass+21]) es más detallada e incluye la siguiente información:

* **ID del Escenario**: Un identificador único para el escenario.
* **Nombre del Escenario**: Un nombre corto y descriptivo para el escenario.
* **Fuente**: La entidad (usuario, sistema o evento) que inicia el escenario.
* **Estímulo**: El evento desencadenante o condición que el sistema debe abordar.
* **Entorno**: El contexto operacional o condición bajo la cual el sistema experimenta el estímulo.
* **Artefacto**: Los **bloques de construcción** u otros elementos del sistema afectados por el estímulo.
* **Respuesta**: El resultado o comportamiento que el sistema exhibe en reacción al estímulo.
* **Medida de Respuesta**: Los criterios o métrica por los cuales se evalúa la respuesta del sistema.

Ejemplos
--------

Ver `el sitio web del modelo de calidad Q42 <https://quality.arc42.org>`_ para ejemplos detallados de **requisitos de calidad**.

Información Adicional
---------------------

* Len Bass, Paul Clements, Rick Kazman: "Software Architecture in Practice", 4th Edition, Addison-Wesley, 2021.

**Plantilla:**

*< Describe aquí los escenarios de calidad >*

----

Ver También
===========

Desde enero de 2023, arc42 proporciona un `modelo de calidad pragmático <https://quality.arc42.org>`_ que propone *etiquetar* **requisitos de calidad** con *hashtags* o *etiquetas* como #flexible, #efficient, #usable, #operable, #testable, #secure, #safe y #reliable.

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/figuras/arc42-system-qualities-overview.svg
   :alt: Q42, el modelo de calidad arc42, con ocho etiquetas para cualidades del sistema
   :align: center
   :width: 80%
   
   Q42, el modelo de calidad arc42, con ocho etiquetas para cualidades del sistema

----

Relación con Otras Secciones
=============================

* **Sección 1.2 (Objetivos de Calidad):** Los **requisitos de calidad** más importantes ya están descritos allí
* **Sección 3 (Alcance del Sistema y Contexto):** El contexto influye en los **requisitos de calidad**
* **Sección 11 (Riesgos y Deuda Técnica):** Los **requisitos de calidad** no cumplidos pueden convertirse en riesgos

----

Tips y Consejos
===============

.. toctree::
   :maxdepth: 1
   :caption: Tips para Requisitos de Calidad
   
   quality_tip_1
   quality_tip_2
   quality_tip_3
   quality_tip_4
   quality_tip_5
   quality_tip_6
   quality_tip_7
   quality_tip_8

----

Ejemplos de Aplicación
======================

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos de Escenarios de Calidad
   
   quality_ejemplo_htmlsc_2
   quality_ejemplo_tpu_1

----

Referencias
===========

* `Modelo de Calidad Q42 <https://quality.arc42.org>`_
* `ISO 25010:2023 - Software Product Quality <https://www.iso.org/obp/ui/#iso:std:iso-iec:25010:ed-2:v1:en>`_
* Bass, Len; Clements, Paul; Kazman, Rick: "Software Architecture in Practice", 4th Edition, Addison-Wesley, 2021
* `FAQ arc42 - Sección 10 <https://faq.arc42.org/category_c/#c-sec-10>`_
