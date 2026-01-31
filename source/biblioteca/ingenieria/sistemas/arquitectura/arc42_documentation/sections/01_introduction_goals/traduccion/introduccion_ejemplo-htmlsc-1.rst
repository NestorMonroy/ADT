.. _introduccion-ejemplo-htmlsc-1:




Ejemplo de Vista General: HTML Sanity Checker
=============================================

.. meta::
   :layout: post
   :title: Ejemplo de Vista General: HTML Sanity Checker
   :tags: overview example 
   :category: overview
   :permalink: /examples/overview-example-htmlsc-1/

.. note::
   **Ejemplo de arc42:**
   
   El *HTML Sanity Checker* es un sistema extremadamente simple y pequeño.
   La vista general se presenta como un diagrama informal con una breve 
   explicación textual.




1. Introducción




HtmlSanityCheck (HtmlSC) verifica errores semánticos en HTML, como enlaces rotos 
e imágenes faltantes. Ha sido creado para apoyar a autores que crean HTML como 
formato de salida.

El objetivo principal es apoyar a los autores en evitar errores dentro de su 
HTML (generado).




1.1 Vista General para HTML Sanity Checker
==========================================

1. Los autores escriben en formatos como `AsciiDoc <https://asciidoctor.org/docs/what-is-asciidoc/>`_, 
   `Markdown <https://www.daringfireball.net/projects/markdown/syntax>`_ u otros 
   formatos, que son transformados a HTML por generadores correspondientes.

2. HtmlSC verifica el HTML generado en busca de enlaces rotos, imágenes faltantes 
   y otros problemas semánticos.

3. HtmlSC crea un informe de prueba, similar al conocido informe de pruebas 
   unitarias (ver abajo).

.. .. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/htmlsc-1-1-overview.png
..       :alt: Objetivo de HtmlSC: Verificación semántica de páginas HTML
..       :align: center
..       :width: 80%

..       Objetivo de HtmlSC: Verificación semántica de páginas HTML

El objetivo general de HtmlSC es crear informes limpios y claros, mostrando 
errores dentro de archivos HTML. Abajo se encuentra un informe de ejemplo.

.. .. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/htmlsc-1-1-sample-report.jpg
..       :alt: Informe de ejemplo
..       :align: center
..       :width: 80%

..       Informe de ejemplo de HtmlSC




.. note::
   **Información de traducción:**
   
   - Archivo original: 01-overview-example-htmlsc-1.md
   - Método: Peshitta (traducción literal)
   - Fecha: 2026-01-27
