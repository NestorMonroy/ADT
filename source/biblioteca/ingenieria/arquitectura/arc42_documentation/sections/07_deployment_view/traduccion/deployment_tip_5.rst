.. _deployment_tip_5:




Tip 7-5: ¡Documenta el mapeo de bloques de construcción a hardware!
===================================================================

.. tip::
   **Consejo de Vista de Despliegue arc42**
   
   Si tu sistema requiere diferentes **nodos** o procesadores para ejecutarse, debes explicar el **mapeo** de tus **bloques de construcción** a ese **hardware**.




En caso de que tu sistema requiera diferentes **nodos** o procesadores para ejecutarse, debes explicar el **mapeo** de tus **bloques de construcción** a ese **hardware**.

Documenta o especifica el **mapeo** de los **bloques de construcción** (ver sección arc42 5) en el **hardware** (más específicamente - el **mapeo** de los *artefactos* generados/compilados/creados desde los **bloques de construcción** de código fuente reales). Eso se llama ***despliegue***. En muchos casos eso puede ser un **mapeo** m:n, con varias variantes de **artefactos** de **despliegue**

Recuerda explicar estas variantes de **despliegue**.

En el siguiente diagrama encuentras tres variantes diferentes de cómo los tres **bloques de construcción** de arquitectura ``A``, ``B`` y ``C`` pueden ser desplegados en diferentes **entornos** de **hardware**.

.. .. figure:: ../figuras/07-deployment-options.webp
..       :alt: Tres variantes diferentes de cómo los bloques A, B y C pueden ser desplegados
..       :align: center
..       :width: 70%
   
..       Tres opciones de despliegue diferentes




.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`deployment_tip_6` - Diagramas UML de despliegue
   * :ref:`deployment_tip_7` - Tablas para mapeo




:Tip: 7-5
:Tema: Mapeo bloques a hardware
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1