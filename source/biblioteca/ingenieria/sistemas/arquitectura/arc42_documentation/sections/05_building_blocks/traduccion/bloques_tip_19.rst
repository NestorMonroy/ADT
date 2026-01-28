.. _bloques_tip_19:

===============================================================
Tip 5-19: ¡En casos excepcionales incluye software de terceros en la vista de bloques de construcción!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   *Usualmente* la **vista de bloques de construcción** debe contener solo elementos creados específicamente para el sistema.

----

*Usualmente* la **vista de bloques de construcción** debe contener solo aquellos elementos que son creados específicamente para el sistema.

En ciertos casos puede ser útil (es decir, para mejor comprensibilidad) incluir software de terceros (es decir, middleware, bases de datos, librerías, frameworks, utilidades) en la **vista de bloques de construcción**.

El siguiente diagrama muestra una **caja blanca** de un software analizador semántico HTML, donde el parser HTML (open-source, de terceros) es absolutamente esencial para el sistema. Por lo tanto, está incluido en la **vista de bloques de construcción** (esquina inferior izquierda).

(De acuerdo con el tip 5-20 (indicar elementos de terceros), ha sido marcado con el estereotipo ``library`` para distinguirlo mejor de los **bloques de construcción** específicos para el sistema mismo.)

.. figure:: ../figuras/05-third-party-element.png
   :alt: Caja blanca de software analizador semántico HTML con elemento de terceros
   :align: center
   :width: 85%
   
   Parser HTML de terceros incluido en vista de bloques

Ver También
===========

* Tip 5-20 (indicar elementos de terceros)

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_20` - Indicar terceros

----

:Tip: 5-19
:Tema: Incluir software de terceros
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
