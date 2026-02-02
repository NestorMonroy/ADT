.. _runtime_ejemplo_htmlsc:




Ejemplo de Vista de Tiempo de Ejecución: HTML Sanity Checker
============================================================

.. admonition:: Ejemplo arc42
   
   Un diagrama simple con una breve explicación textual.




6. Vista de Tiempo de Ejecución




6.1 Ejecutar Todas las Verificaciones
=====================================

Un **escenario** típico dentro de HtmlSC es la **ejecución** de *todos* los algoritmos de verificación disponibles sobre un conjunto de páginas HTML.

.. .. figure:: ../figuras/examples/htmlsc/6-main-loop.png
..       :alt: Bucle principal
..       :align: center
..       :width: 70%
   
..       Bucle principal de verificación

**Explicación:**

0. El usuario o la construcción llama al objetivo de construcción ``htmlSanityCheck``.
1. Gradle (desde dentro de la construcción) llama ``sanityCheckHtml``
2. HSC configura los archivos de entrada y el directorio de salida
3. HSC crea una **instancia** de ``AllChecksRunner``
4. Obtiene todos los archivos configurados en ``allFiles``
5. (Planeado) Obtiene todas las clases Checker disponibles basándose en anotaciones
6. Realiza las verificaciones, recolectando los resultados

6.2 Reportar Resultados de Verificación
=======================================

.. .. figure:: ../figuras/examples/htmlsc/6-2-1-report-results.png
..       :alt: Diagrama de secuencia: Reportar resultados
..       :align: center
..       :width: 70%
   
..       Secuencia de reporte de resultados

El reporte se realiza en la jerarquía natural de resultados (ver el concepto correspondiente en sección 8.2.1 para un reporte de ejemplo).

1. Por "ejecución" (``PerRunResults``): fecha/hora de esta **ejecución**, archivos verificados, algo de información de configuración, resumen de resultados
2. Por "página" (``SinglePageResults``):
   
   1. Crear encabezado de resultado de página con resumen del nombre de página y resultados
   2. Para cada verificación realizada en esta página crear una sección con ``SingleCheckResults``
   3. Por "verificación única en esta página" reportar los resultados para esta verificación particular




.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * Sección 8.2.1 - Concepto de jerarquía de resultados




:Ejemplo: Runtime View HTML Sanity Checker
:Sistema: HTML Sanity Checker (HSC)
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1