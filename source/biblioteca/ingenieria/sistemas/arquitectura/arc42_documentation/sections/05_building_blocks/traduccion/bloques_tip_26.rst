.. _bloques_tip_26:

===============================================================
Tip 5-26: ¡Haz explícito el origen de bloques de construcción de nivel inferior!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   En caso de que refines mutuamente varios **bloques de construcción** a la vez (como se propone en el tip 5-25), debes documentar explícitamente el *origen* (también conocido como ancestro o raíz) de los **bloques de construcción** refinados.

----

En caso de que refines mutuamente varios **bloques de construcción** a la vez (como se propone en el tip 5-25, refinar mutuamente), debes documentar explícitamente el *origen* (también conocido como ancestro o raíz) de los **bloques de construcción** refinados.

Debe ser explícito para cada elemento dentro de una **caja blanca** *refinada* de dónde está originándose (es decir, desde dónde es refinado).

Encuentras dos ejemplos abajo:

Documenta el Origen por Convención de Nombres
==============================================

.. figure:: ../figuras/05-mutual-refinement.webp
   :alt: Caja blanca con dos cajas negras refinadas a una sola caja blanca
   :align: center
   :width: 85%
   
   Origen indicado por prefijos en nombres (Foo-X, Bar-Y)

En este ejemplo, los prefijos "Foo-" y "Bar-" indican de qué **caja negra** de nivel 1 proviene cada **bloque de construcción** de nivel 2.

Documenta el Origen por Medios Gráficos
========================================

En el siguiente diagrama, el origen de los **bloques de construcción** refinados se muestra mediante un rectángulo nombrado alrededor de los bloques refinados (mostrado en color rosa para propósitos de ilustración...)

.. figure:: ../figuras/05-mutual-refinement-graphical.png
   :alt: Bloques de construcción refinados
   :align: center
   :width: 85%
   
   Origen indicado por agrupamiento visual con color/borde

Este enfoque visual hace aún más explícita la relación entre los **bloques de construcción** del nivel superior y sus refinamientos.

Métodos para Indicar Origen
============================

**Convenciones de nombres:**

* Prefijos: ``Foo-Component``, ``Bar-Service``
* Sufijos: ``Component-Foo``, ``Service-Bar``
* Notación de punto: ``Foo.Component``, ``Bar.Service``

**Medios gráficos:**

* Color de fondo o borde
* Agrupamiento con rectángulos
* Iconos o símbolos
* Estereotipos UML

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_25` - Refinamiento mutuo

----

:Tip: 5-26
:Tema: Origen explícito en refinamiento
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
