.. _contexto_ejemplo_tecnico_1:

============================================================
Ejemplo de Contexto Técnico: HTML Sanity Checker
============================================================

.. note::
   **Ejemplo arc42**
   
   Este es un ejemplo muy simple, creado con Enterprise Architect™.

----

3. Vista de Contexto

====================

3.2 Contexto Técnico
--------------------

El siguiente diagrama muestra las computadoras participantes (nodos) con sus conexiones técnicas más los artefactos principales de HtmlSC, el hsc-plugin-binary.

.. figure:: ../figuras/3-hsc-technical-context.png
   :alt: Contexto técnico
   :align: center
   :width: 80%
   
   Diagrama de contexto técnico del HTML Sanity Checker

Nodos y Artefactos
==================

.. list-table::
   :header-rows: 1
   :widths: 35 65
   
   * - Nodo / Artefacto
     - Descripción
   * - **hsc-development**
     - Donde se realiza el desarrollo de HtmlSC
   * - **hsc-plugin-binary**
     - Versión compilada y empaquetada de HtmlSC incluyendo las dependencias requeridas.
   * - **repositorio de artefactos**
     - Un repositorio *cloud* público global para artefactos binarios, similar a `MavenCentral <https://search.maven.org/>`_, el `Gradle Plugin Portal <https://plugins.gradle.com>`_ o similares. Los binarios de HtmlSC se suben a este servidor.
   * - **computadora del usuario hsc**
     - Donde se realiza la documentación arbitraria con HTML como formato de salida.
   * - **build.gradle**
     - Script de construcción Gradle que configura (entre otras cosas) el plugin HtmlSC para realizar la verificación HTML.

----

Observaciones
=============

Este ejemplo muestra un **contexto técnico** donde:

* Se identifican los **nodos** (computadoras) involucrados
* Se especifican las **conexiones técnicas** entre nodos
* Se documentan los **artefactos** principales del sistema
* Se indican los **canales** de comunicación (repositorio cloud)

Para detalles ver la vista de despliegue.

.. seealso::
   * :ref:`seccion_3_2` - Plantilla de Contexto Técnico
   * :ref:`seccion_03` - Contexto y Alcance completo

----

:Ejemplo: Contexto Técnico
:Sistema: HTML Sanity Checker
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
