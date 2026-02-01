.. _contexto_ejemplo_negocio_1:




Ejemplo de Contexto de Negocio: HTML Sanity Checker
===================================================

.. note::
   **Ejemplo arc42**
   
   Este es un ejemplo muy simple, creado con Enterprise Architect™.




3. Vista de Contexto




.. .. figure:: ../figuras/3-hsc-business-context.png
..       :alt: Contexto de negocio
..       :align: center
..       :width: 80%
   
..       Diagrama de contexto de negocio del HTML Sanity Checker

Socios de Comunicación
======================

.. list-table:: 
   :header-rows: 1
   :widths: 30 70
   
   * - Vecino
     - Descripción
   * - **usuario**
     - Documenta software con una cadena de herramientas que genera HTML. Quiere asegurar que los enlaces dentro de este HTML sean válidos.
   * - **sistema de construcción**
     - Principalmente `Gradle <https://gradle.org>`_
   * - **archivos HTML locales**
     - HtmlSC lee y analiza archivos HTML locales y realiza verificaciones de sanidad dentro de ellos.
   * - **archivos de imagen locales**
     - HtmlSC verifica si las imágenes enlazadas existen como archivos (locales).
   * - **recursos web externos**
     - HtmlSC puede configurarse para verificar opcionalmente la existencia de recursos web externos.
       
       **Riesgo:** Debido a la naturaleza de los sistemas web y las operaciones de red remota involucradas, esta verificación podría necesitar tiempo significativo y podría arrojar resultados inválidos debido a problemas de red y latencia.




Observaciones
=============

Este ejemplo muestra un **contexto de negocio** simple donde:

* El sistema se representa como una **caja negra**
* Se identifican claramente los **socios de comunicación** externos
* Se especifican las **interfaces de dominio** (entradas/salidas)
* Se documentan **riesgos** asociados con interfaces específicas

.. seealso::
   * :ref:`seccion_3_1` - Plantilla de Contexto de Negocio
   * :ref:`seccion_03` - Contexto y Alcance completo




:Ejemplo: Contexto de Negocio
:Sistema: HTML Sanity Checker
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
