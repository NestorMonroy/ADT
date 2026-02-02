.. _runtime_tip_2:




Tip 6-2: ¡Documenta solo unos pocos escenarios de tiempo de ejecución!
======================================================================

.. tip::
   **Consejo de Vista de Tiempo de Ejecución arc42**
   
   Los **escenarios de tiempo de ejecución** consumen mucho tiempo para crear y mantener. Enfócate en los importantes y mantén solo unos pocos en tu documentación.




Los Escenarios Consumen Tiempo para Crear
=========================================

Como los **escenarios de tiempo de ejecución** son bastante consumidores de tiempo para crear y mantener, enfócate en:

* Los importantes, que son *realmente* específicos, complejos, riesgosos o de otra manera interesantes.
* **Escenarios** que ayudan a *diseñar* **bloques de construcción** o desafían decisiones de diseño correspondientes.

.. important::
   Usa **escenarios** primariamente para identificar y discutir comportamiento de **bloques de construcción**, y mantén **solo unos pocos escenarios para tu documentación**.

Mantén Solo Unos Pocos Escenarios en tu Documentación
=====================================================

Documenta solo **escenarios** que:

* Son cruciales para entender el procesamiento general dentro del sistema, es decir, para las funciones, características o casos de uso más importantes,
* Son críticos para las metas de calidad principales del sistema,
* Son especialmente riesgosos en su implementación,
* Involucran **interfaces** externas críticas, volátiles o inestables,
* Han sido muy difíciles de implementar,
* Necesitan atención especial por algunos stakeholders
* etc.

En mi (Gernot) experiencia, está perfectamente bien mantener solo 1-3 **escenarios** en tu documentación - pero usa varias docenas durante el diseño y desarrollo del sistema.

Ver También
===========

* Tip 6-3 (escenarios esquemáticos)
* Tip 6-5 (escenarios para discusión)




.. seealso::
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`runtime_tip_3` - Escenarios esquemáticos
   * :ref:`runtime_tip_5` - Escenarios para descubrir bloques




:Tip: 6-2
:Tema: Documentar pocos escenarios
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1