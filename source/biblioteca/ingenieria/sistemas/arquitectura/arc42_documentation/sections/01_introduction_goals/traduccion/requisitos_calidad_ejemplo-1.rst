.. meta::
   :layout: post
   :title: Ejemplo de Requisitos de Calidad: HTML Sanity Checker
   :tags: quality-requirements example 
   :category: quality-goals
   :permalink: /examples/quality-requirements-1/

.. _requisitos-calidad-ejemplo-1:

===================================================================
Ejemplo de Requisitos de Calidad: HTML Sanity Checker
===================================================================

.. note::
   **Ejemplo de arc42:**
   
   Este ejemplo ha sido creado con Enterprise Architect(TM) como un diagrama 
   de flujo de datos.

----

1.2 (ejemplo) Requisitos de Calidad para HTML Sanity Checker
=============================================================

.. list-table:: Atributos de Calidad Objetivo
   :header-rows: 1
   :widths: 10 20 70

   * - Prioridad
     - Objetivo de Calidad
     - Escenario
   * - 1
     - Corrección
     - Cada enlace interno roto (referencia cruzada) es encontrado.
   * - 1
     - Corrección
     - Cada error semántico potencial es encontrado y reportado. En caso de 
       duda [#duda]_, reportar y dejar que el usuario decida.
   * - 1
     - Seguridad
     - El contenido de los archivos a verificar *nunca* es alterado.
   * - 2
     - Flexibilidad
     - Múltiples algoritmos de verificación, formatos de informe y clientes. 
       Al menos Gradle y línea de comandos deben ser soportados.
   * - 2
     - Corrección
     - La corrección de cada verificador es probada automáticamente para 
       casos positivos Y negativos.
   * - 3
     - Rendimiento
     - Verificación de archivo html de 100kB realizada en menos de 10 
       segundos (excluyendo inicio de Gradle)

----

.. [#duda] Especialmente al verificar enlaces externos, la corrección de los 
   enlaces depende de factores externos, como disponibilidad de red, latencia 
   o configuración del servidor, donde HtmlSC no siempre puede identificar la 
   causa raíz de problemas potenciales.

----

.. note::
   **Información de traducción:**
   
   - Archivo original: 01-quality-reqs-example-1.md
   - Método: Peshitta (traducción literal)
   - Fecha: 2026-01-27
