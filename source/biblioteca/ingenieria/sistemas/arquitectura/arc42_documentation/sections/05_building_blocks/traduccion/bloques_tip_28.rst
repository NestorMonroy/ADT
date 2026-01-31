.. _bloques_tip_28:




Tip 5-28: ¡Explica conceptos en lugar de bloques de construcción!
=================================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Este tip podría sonar extraño en contexto con **bloques de construcción** - pero a veces es fácil o útil explicar los conceptos fundamentales o transversales (otros términos son *principios*, *estilos*, *estereotipos* o *patrones*) en lugar de todos los **bloques de construcción**.




Este tip podría sonar extraño en contexto con **bloques de construcción** - pero a veces es fácil o útil explicar los conceptos fundamentales o transversales (otros términos son *principios*, *estilos*, *estereotipos* o *patrones*) en lugar de todos los **bloques de construcción**.

Por ejemplo, si construyes un sistema basado en microservicios o construiste un sistema como una arquitectura de tubos-y-filtros (pipe-and-filter), la explicación de los principios fundamentales podría ser más útil que la discusión elaborada de **bloques de construcción** individuales.

Cuándo Usar Este Enfoque
========================

Este enfoque es particularmente efectivo cuando:

* Tu sistema sigue un patrón arquitectónico bien definido
* Los **bloques de construcción** individuales son similares entre sí
* El concepto o patrón es más importante que los detalles
* La arquitectura es homogénea

**Ejemplos:**

* **Arquitectura de microservicios:** Explica el patrón de microservicio una vez, en lugar de documentar 50 servicios similares individualmente
* **Pipe-and-filter:** Describe el concepto de filtros y pipes, no cada filtro
* **Arquitectura en capas:** Explica el principio de capas, no cada capa
* **Event-driven:** Documenta el patrón de eventos, no cada productor/consumidor

Pero: Debes Tener una Vista de Bloques de Construcción Nivel 1
==============================================================

Por favor, ten en mente el tip 5-3 (el nivel 1 es tu amigo).

Incluso cuando uses conceptos para explicar la estructura general, el **nivel 1** de la **vista de bloques de construcción** sigue siendo obligatorio. Proporciona la visión general esencial del sistema.

Balance Entre Conceptos y Bloques
=================================

**Enfoque ideal:**

1. **Nivel 1:** Siempre documenta (obligatorio)
2. **Conceptos transversales:** Explica patrones y principios comunes
3. **Niveles 2-3:** Solo para **bloques de construcción** especiales/críticos

Este enfoque:

* Evita redundancia
* Reduce esfuerzo de mantenimiento
* Mantiene documentación concisa
* Enfoca en lo importante

Tips Relacionados
=================

* Debes denotar qué conceptos se aplican en ciertos **bloques de construcción**, ver tip 5-10.
* Debes nombrar conceptos importantes, y usar estos nombres en **bloques de construcción**, ver tip 8-11.




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_3` - Nivel 1 es tu amigo
   * :ref:`bloques_tip_10` - Conceptos transversales
   * Sección 8 de arc42 - Conceptos Transversales




:Tip: 5-28
:Tema: Conceptos vs bloques individuales
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
