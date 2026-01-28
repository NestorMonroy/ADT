.. _contexto_tip_15:

===============================================================
Tip 3-15: ¡Muestra el contexto técnico (en caso de que el hardware sea central para tu sistema)!
===============================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Si hardware, procesadores, red, **canales** de transmisión o buses son centrales para tu sistema, debes documentar o especificar este hardware e infraestructura de tu sistema en el **contexto técnico**.

----

Especialmente para sistemas integrados hardware/software (sistemas embebidos) casi siempre necesitas un diagrama de **contexto técnico**.

.. figure:: ../figuras/03-technical-context-automotive.png
   :alt: Contexto técnico de un sistema automotriz
   :align: center
   :width: 90%
   
   Contexto técnico de sistema automotriz (especialmente lado derecho)

El diagrama de contexto de sistemas embebidos arriba (especialmente en el lado derecho) es tal ejemplo.

Sin embargo, también puede ser importante para sistemas de información mostrar algunos aspectos de hardware e infraestructura ya en el **contexto**, por ejemplo, para cuestiones de seguridad (ver el ejemplo de tienda web en el tip 3-10).

   Para sistemas de información o web, data-warehouse o business-intelligence, la vista de **despliegue** (sección 7 de arc42) es usualmente suficiente y un **contexto técnico** raramente se necesita.

Ver También
===========

* Tip 3-10 (contexto de negocio y técnico)

----

.. seealso::
   * :ref:`seccion_3_2` - Contexto Técnico
   * :ref:`contexto_tip_10` - Diferenciación business/technical

----

:Tip: 3-15
:Tema: Contexto técnico para hardware
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
