.. _deployment_tip_3:

===============================================================
Tip 7-3: ¡Documenta los varios entornos!
===============================================================

.. tip::
   **Consejo de Vista de Despliegue arc42**
   
   Si el sistema es desarrollado, probado y operado en diferentes **entornos** de **hardware**, documenta estos **entornos** más las posibles diferencias entre ellos.

----

En caso de que el sistema sea desarrollado, probado y operado en diferentes **entornos** de **hardware** (es decir, DEV para desarrollo, CI para construcción/integración, TEST para pruebas de sistema y manuales y PROD para **producción**), deberías documentar estos **entornos** más las posibles diferencias entre ellos.

El estereotipo «**executionEnvironment**» simboliza tales **entornos**. El pequeño símbolo "infinito" en la esquina inferior derecha (es decir, en Development) significa que hay un diagrama refinado disponible (ese símbolo "infinito" es una especialidad de Sparx EnterpriseArchitect®).

.. figure:: ../figuras/07-deployment-overview.png
   :alt: Vista general de despliegue
   :align: center
   :width: 70%
   
   Vista general de despliegue con múltiples entornos

----

.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`deployment_tip_1` - Documentar infraestructura técnica
   * :ref:`deployment_tip_4` - Vista jerárquica

----

:Tip: 7-3
:Tema: Documentar varios entornos
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1