.. _seccion_06:

===============================================================
Sección 06: Vista de Tiempo de Ejecución (Runtime View)
===============================================================

.. tip::
   **Vista de Tiempo de Ejecución arc42**
   
   La **vista de tiempo de ejecución** describe el comportamiento dinámico del sistema: cómo interactúan los **bloques de construcción** en **escenarios de tiempo de ejecución** concretos.

----

Introducción
============

La **vista de tiempo de ejecución** (o **runtime view**) muestra el comportamiento y la **interacción** de los **bloques de construcción** del sistema como **escenarios**.

Los **escenarios** típicos incluyen:

* El caso de uso más importante o crítico
* Interacciones en **interfaces** externas clave
* Operaciones en el centro de datos del sistema
* **Procesos** de inicio y apagado del sistema
* Comportamiento ante errores y excepciones

----

Contenido de la Sección
========================

Esta sección contiene:

**Tips de Vista de Tiempo de Ejecución (11 tips)**
   Consejos prácticos para documentar **escenarios de tiempo de ejecución**

**Ejemplos de Aplicación (3 ejemplos)**
   Casos reales de **vistas de tiempo de ejecución** en sistemas

----

Tips de Vista de Tiempo de Ejecución
=====================================

.. toctree::
   :maxdepth: 1
   :caption: Consejos para Runtime View
   
   runtime_tip_1
   runtime_tip_2
   runtime_tip_3
   runtime_tip_4
   runtime_tip_5
   runtime_tip_6
   runtime_tip_7
   runtime_tip_8
   runtime_tip_9
   runtime_tip_10
   runtime_tip_11

----

Ejemplos de Runtime View
=========================

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos de Aplicación
   
   runtime_ejemplo_htmlsc
   runtime_ejemplo_mama
   runtime_ejemplo_tpu

----

Motivación
==========

Debes documentar **escenarios de tiempo de ejecución** si:

* Los stakeholders necesitan entender cómo el sistema ejecuta sus funciones principales
* La **interacción** de **bloques de construcción** no es obvia
* El comportamiento dinámico es crítico para la calidad del sistema
* Necesitas validar decisiones arquitectónicas contra requisitos funcionales

----

Forma y Notación
================

Existen varias notaciones para describir **escenarios**:

**Diagramas UML:**
  * **Diagramas de secuencia** - Muestran **interacción** temporal entre **componentes**
  * **Diagramas de actividad** - Muestran flujos de control y datos
  * Diagramas de comunicación
  * Diagramas de tiempos

**Otras notaciones:**
  * Numeración de pasos
  * **Diagramas de flujo** con **carriles** (swimlanes)
  * BPMN (Business Process Model and Notation)
  * Descripciones textuales

----

Relación con Otras Secciones
=============================

**Sección 05 (Building Block View)**
   Los **escenarios de tiempo de ejecución** usan **bloques de construcción** definidos en la vista estática

**Sección 08 (Conceptos Transversales)**
   Los **escenarios** pueden ilustrar la aplicación de conceptos transversales

**Sección 10 (Requisitos de Calidad)**
   Los **escenarios** ayudan a validar el cumplimiento de requisitos de calidad

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_08` - Conceptos Transversales
   * :ref:`seccion_10` - Requisitos de Calidad

----

:Sección: 06
:Título: Vista de Tiempo de Ejecución
:Nombre Original: Runtime View
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1
:Total archivos: 15 (1 principal + 11 tips + 3 ejemplos)