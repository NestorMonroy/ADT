.. _runtime_ejemplo_mama:




Ejemplo de Vista de Tiempo de Ejecución: MaMa
=============================================

.. admonition:: Ejemplo arc42
   
   Sistema CRM MaMa con proceso de importación de archivos en dos fases.




6. Vista de Tiempo de Ejecución




6.1 Importar Archivo
====================

Uno de los casos de uso principales es *Importar Archivo*, que puede ser tanto de mandante como de socio. Tales archivos siempre contienen datos relacionados con ``Client`` en formatos configurables (CSV, formatos fijos o XML).

Dividimos la explicación de *importar archivo* en dos fases:

1. Importar Archivo Raw Genérico (desde una fuente externa)
2. Validar los datos importados y actualizar la base de datos interna de ``Client``

6.1.1 Importar Raw Genérico
===========================

Primero explicamos la importación *genérica*, donde no se ejecutan actividades específicas de campaña. Esto concierne a las actividades ``configureReceiveChannel`` y especialmente ``instantiateFilterChain()``.

.. .. figure:: ../figuras/examples/mama/9-getRawFile.png
..       :alt: (Primera parte de importación de datos:) Importar archivo raw
..       :align: center
..       :width: 70%
   
..       Primera fase: Importar archivo raw

1. tryImport: ``ProcessControl`` inicia la importación. El ``activity`` es un ID único identificando el mandante, la campaña y la actividad.
2. ``importConfiguration`` obtiene toda la información de configuración requerida
3. ``configureReceiveChannel`` prepara todo lo necesario para obtener datos de una fuente externa. Por ejemplo, URL, nombres de archivo y credenciales de autenticación para un servidor ftp externo necesitan ser configurados aquí.
4. ``archive`` envía el archivo al sistema de archivo (configurado), usualmente un archivo de respaldo óptico de escritura única no borrable.
5. ``setup`` inicializa los filtros requeridos, por ejemplo unzip o decrypt.
6. ``filter`` ejecuta todos los filtros

Los pasos 5+6 son un subsistema de flujo de datos pipes-and-filter configurado dinámicamente. Encuentras algo más de información en el concepto de filtros en sección 8.

6.1.2 Validar Archivo
=====================

**Prerrequisito:** Los datos han sido importados desde una fuente externa, han sido filtrados exitosamente (es decir, desencriptados y descomprimidos). Ver sección previa (*Importar Raw Genérico*).

El diagrama debajo contiene manejo de errores. En *buenos casos* no habrá errores. ¡Las llamadas a ``ImportErrorHandler`` solo se ejecutan si ocurren errores!

.. .. figure:: ../figuras/examples/mama/9-validateRawData.png
..       :alt: (Segunda parte de importación de datos:) Validar datos importados
..       :align: center
..       :width: 70%
   
..       Segunda fase: Validar datos importados




.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * Sección 8 - Concepto de filtros pipes-and-filter




:Ejemplo: Runtime View MaMa CRM
:Sistema: MaMa CRM System
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1