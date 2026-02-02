.. _bloques_ejemplo_hsc:




Ejemplo de Vista de Bloques: HTML Sanity Checker
================================================

.. note::
   **Ejemplo arc42**
   
   Este ejemplo contiene varios niveles de la **vista de bloques de construcción** - desde el nivel de visión general 1 hasta el muy específico y bajo nivel 3.




5.1 Caja Blanca HtmlSanityChecker
=================================

.. .. figure:: ../figuras/5-whitebox-hsc-level-1.png
..       :alt: Caja blanca (HtmlSC)
..       :align: center
..       :width: 80%
   
..       Caja blanca HtmlSanityChecker - Nivel 1

Razonamiento
============

Usamos *descomposición funcional* para separar **responsabilidades**:

* ``HSC Core`` debe encapsular la lógica de verificación y el procesamiento/análisis de HTML.
* ``Plugins`` y ``GraphicalUI`` encapsulan todos los aspectos de *uso*

Cajas Negras Contenidas
=======================

.. list-table:: Bloques de Construcción Nivel 1
   :header-rows: 1
   :widths: 30 70
   
   * - **Bloque de construcción**
     - **Descripción**
   * - ``HSC Core``
     - Análisis de HTML y verificación de sanidad
   * - ``HSC Gradle Plugin``
     - Expone HtmlSC a través de un plugin Gradle estándar, como se describe en la guía de usuario de Gradle. Fuente: Paquete ``org.aim42.htmlsanitycheck``, clases: ``HtmlSanityCheckPlugin`` y ``HtmlSanityCheckTask``
   * - ``NetUtil``
     - Paquete ``org.aim42.inet``, verifica conectividad a internet, configuración de códigos de estado http
   * - ``FileUtil``
     - Paquete ``org.aim42.filesystem``, extensiones de archivo, etc.
   * - ``HSC Graphical UI``
     - (planificado, no implementado)




5.2 Bloques de Construcción - Nivel 2
=====================================

5.2.1 HSC Core (Caja Blanca)
============================

.. .. figure:: ../figuras/5-2-1-hsc-core.png
..       :alt: HSC-Core (Caja blanca)
..       :align: center
..       :width: 80%
   
..       Caja blanca HSC Core - Nivel 2

.. _hsc-core-razonamiento:

Razonamiento
============

La **estructura interna** de ``HSC Core`` sigue una **descomposición** funcional:

* Configuración
* Análisis y manejo de entrada HTML
* Verificación
* Creación de sugerencias
* Recolección de resultados de verificación

.. _hsc-core-cajas-negras:

Cajas Negras Contenidas
=======================

.. list-table:: Bloques de Construcción HSC Core
   :header-rows: 1
   :widths: 25 75
   
   * - **Bloque de construcción**
     - **Descripción**
   * - ``Checker``
     - Contiene la funcionalidad pura de verificación. Ver su descripción de **caja negra** abajo.
   * - ``AllChecksRunner``
     - Fachada hacia los Checkers. Proporciona una **interfaz** (configurable). Fuente: ``org.aim42.htmlsanitycheck.AllChecksRunner``. Llamado por ``HSC GradlePlugin``
   * - ``Configuration``
     - Maneja la configuración de ubicación de entrada y salida, timeouts, comportamiento de código de estado y tipos de verificaciones a realizar.
   * - ``Reporter``
     - Reporta resultados de verificación a consola o archivo.
   * - ``Suggester``
     - En caso de problemas de verificación, sugiere alternativas (*¿quisiste decir xyz?*). Las sugerencias se incluyen en los resultados.

5.2.1.1 Checker (Caja Negra)
============================

La clase abstracta ``Checker`` proporciona la **interfaz** uniforme (``public void check()``) a diferentes algoritmos de verificación.

Basado en polimorfismo, la verificación real es manejada por subclases de la clase abstracta ``Checker``, usa el patrón template-method. Usa el concepto de algoritmos de verificación extensibles.

5.2.1.2 Suggester (Caja Negra)
==============================

Para una entrada dada (*target*), ``Suggester`` busca dentro de un conjunto de valores posibles (*options*) para encontrar los n valores más similares. Por ejemplo:

* Target = "McDown"
* Options = {"McUp", "McDon", "Mickey"}
* La sugerencia resultante sería "McDon", porque tiene la mayor similitud con el target "McDown".

La implementación se basa en la `distancia Jaro-Winkler <https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance>`_, uno de los algoritmos para calcular similitud entre cadenas.

``Suggester`` se usa en los siguientes casos:

* Enlaces de imagen rotos: Compara el nombre de la imagen faltante con todos los nombres de archivo de imagen disponibles para encontrar la coincidencia más cercana.
* Referencias cruzadas faltantes (enlaces internos rotos): Compara el enlace roto con todos los objetivos de enlace disponibles (anclas).

Fuente: ``package org.aim42.htmlsanitycheck.suggest.Suggester``




5.3 Bloques de Construcción - Nivel 3
=====================================

5.3.1 ResultsCollector (Caja Blanca)
====================================

.. .. figure:: ../figuras/5-3-results-collector.png
..       :alt: Results Collector (Caja blanca)
..       :align: center
..       :width: 80%
   
..       Caja blanca ResultsCollector - Nivel 3

.. _resultscollector-razonamiento:

Razonamiento
============

Esta estructura sigue la jerarquía de verificaciones, administrando resultados para:

1. Un número de páginas/documentos (``PerRunResults``)
2. Una sola página HTML (``SinglePageResults``) y finalmente
3. Los resultados de una sola verificación, por ejemplo, el ``MissingImagesChecker`` (``SingleCheckResults``)

.. _resultscollector-cajas-negras:

Cajas Negras Contenidas
=======================

.. list-table:: Bloques de Construcción ResultsCollector
   :header-rows: 1
   :widths: 30 70
   
   * - **Bloque de construcción**
     - **Descripción**
   * - ``Per-Run Results``
     - Resultados agregados para potencialmente muchas páginas/documentos HTML.
   * - ``SinglePageResults``
     - Resultados agregados para una sola página HTML
   * - ``SingleCheckResults``
     - Resultados para un solo tipo de verificación (por ejemplo, verificación de imágenes faltantes o verificación de enlace interno roto)
   * - ``Finding``
     - Un solo hallazgo (por ejemplo, "imagen 'logo.png' faltante"). Puede contener sugerencias.




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Caja Blanca del Sistema General




:Ejemplo: HTML Sanity Checker
:Sistema: HtmlSC
:Niveles: 1, 2, 3
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
