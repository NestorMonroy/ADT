.. _deployment_ejemplo_htmlsc:




Ejemplo de Vista de Despliegue: HTML Sanity Checker
===================================================

.. admonition:: Ejemplo arc42
   
   Vista de **despliegue** del sistema HTML Sanity Checker mostrando **nodos**, **artefactos** y sus conexiones.




7. Vista de Despliegue




.. .. figure:: ../figuras/examples/htmlsc/7_1-deployment.png
..       :alt: Vista general de despliegue de HTML Sanity Checker
..       :align: center
..       :width: 70%
   
..       Vista general de despliegue de HTML Sanity Checker

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - **Nodo / Artefacto**
     - **Descripción**
   * - hsc plugin binary
     - Versión compilada de HtmlSC, incluyendo dependencias requeridas.
   * - hsc-development
     - **Entorno** de desarrollo
   * - artifact repository
     - Repositorio **nube** global público para **artefactos** binarios, similar a `mavenCentral <https://mvnrepository.com/>`_. Los binarios de HtmlSC son subidos a este **servidor**.
   * - hsc user computer
     - Donde la documentación es creada y compilada a HTML.
   * - build.gradle
     - Script de construcción Gradle configurando (entre otras cosas) el plugin HtmlSC.

Los tres **nodos** (*computadoras*) mostrados en el diagrama arriba están conectados vía Internet.

**Prerrequisitos**:

* Los desarrolladores de HtmlSC necesitan un kit de desarrollo Java, Groovy, Gradle más el parser HTML JSoup.
* Los usuarios de HtmlSC necesitan un runtime de Java (> 1.6) más un archivo de construcción llamado ``build.gradle``. (dentro de este ejemplo de documentación omitimos el listado del script de construcción).




.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`deployment_tip_7` - Tablas para mapeo
   * :ref:`deployment_tip_8` - Explicar nodos




:Ejemplo: Deployment View HTML Sanity Checker
:Sistema: HTML Sanity Checker (HSC)
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1