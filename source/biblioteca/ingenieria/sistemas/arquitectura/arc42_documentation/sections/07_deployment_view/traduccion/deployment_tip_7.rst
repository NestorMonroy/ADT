.. _deployment_tip_7:




Tip 7-7: ¡¡Usa tablas para documentar el mapeo software/hardware!!
==================================================================

.. tip::
   **Consejo de Vista de Despliegue arc42**
   
   Como alternativa (simple) a **mapeo** gráfico con **diagramas de despliegue**, podrías usar tablas para documentar o especificar el **despliegue** de software en **hardware**.




Como una alternativa (simple) a **mapeo** gráfico con **diagramas de despliegue** (ver tip 7-6 (diagramas de despliegue)), podrías usar tablas para documentar o especificar el **despliegue** de software en **hardware**.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - **Servidor**
     - **Artefacto**
     - **Observación**
   * - OneServer
     - 
     - Un **contenedor** docker, requiriendo al menos Docker V 12.1
   * - 
     - DomainServices
     - Auto-desplegado por script de construcción Gradle
   * - 
     - 
     - 
   * - OtherServer
     - 
     - **Servidor** Dell(c), CPU Quad-Core i7, 64GB RAM, ejecutando RH Enterprise Linux
   * - 
     - Articles
     - Ejecutable Unix, construido por make, ejecutado vía cron
   * - 
     - FooBar
     - Jar Java, construido, desplegado y ejecutado vía script de construcción Gradle
   * - 
     - CassandraDB
     - Base de datos open source, iniciada vía cron

Por favor encuentra el diagrama correspondiente debajo:

.. .. figure:: ../figuras/07-deployment-diagram.png
..       :alt: Diagrama de despliegue
..       :align: center
..       :width: 60%
   
..       Diagrama de despliegue correspondiente




.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`deployment_tip_6` - Diagramas UML de despliegue
   * :ref:`deployment_tip_5` - Mapeo bloques a hardware




:Tip: 7-7
:Tema: Tablas para mapeo software/hardware
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1