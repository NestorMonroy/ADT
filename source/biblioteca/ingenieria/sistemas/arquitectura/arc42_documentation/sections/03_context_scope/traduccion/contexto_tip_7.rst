.. _contexto_tip_7:




Tip 3-7: ¡Si hay muchos sistemas externos involucrados, agrégalos (agrúpalos) por criterios explícitos!
=======================================================================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Si tu sistema interactúa con muchos sistemas externos, puedes combinar varios de estos sistemas externos por criterios explícitos. Debes declarar explícitamente estos criterios.




Tales criterios pueden incluir sistemas que:

* Comparten datos comunes o similares
* Se comunican dentro del mismo caso de uso o al mismo tiempo
* Se comunican usando tecnologías idénticas o similares (por ejemplo, categorizados por ftp- y WebService)
* Pertenecen a la misma organización o similar, tales como: todos los sistemas de garajes, aseguradoras, fabricación de vidrio y asesores fiscales
* Tienen tareas de dominio o técnicas similares a resolver (todos los sistemas que imprimen documentos, que tratan con tarjetas chip, etc.)

Ejemplos: Con y Sin Agregación
==============================

El siguiente diagrama (la versión detallada) muestra tres **sistemas vecinos** específicos, todos estereotipados con la categoría << logística >>.

.. .. figure:: ../figuras/03-context-extensive.png
..       :alt: Diagrama de contexto extensivo
..       :align: center
..       :width: 80%
   
..       Versión detallada: tres sistemas de logística separados

El siguiente diagrama agrupa estos **vecinos** en un solo sistema externo "Logistics" a la izquierda, estereotipado como << categoría >>.

.. .. figure:: ../figuras/03-context-compact.png
..       :alt: Diagrama de contexto compacto
..       :align: center
..       :width: 80%
   
..       Versión compacta: sistemas de logística agrupados en categoría única




.. seealso::
   * :ref:`seccion_03` - Contexto y Alcance
   * :ref:`contexto_tip_6` - Categorización
   * :ref:`contexto_tip_8` - Puertos para agrupar




:Tip: 3-7
:Tema: Agregación por criterios
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
