.. _seccion_5_3:

=====================================
5.3 Nivel 3
=====================================

.. note::
 **Plantilla arc42 - Traducción Arquitectónica (Paso 3.4)**

 Términos clave:
 * Level 3 -> Nivel 3
 * White box -> Caja blanca
 * Building block -> Bloque de construcción
 * Additional levels -> Niveles adicionales

----

Aquí puedes especificar la **estructura interna** de (algunos) **bloques de construcción** del nivel 2 como **cajas blancas**.

Cuando necesites niveles más detallados de tu arquitectura, por favor copia esta parte de arc42 para niveles adicionales.

----

Plantilla Nivel 3
=================

.. code-block:: text

 5.3 Nivel 3
 ===========

 5.3.1 Caja Blanca <bloque de construcción x.1>
 -----------------------------------------------

 Especifica la estructura interna de _bloque de construcción x.1_.

 _<inserta plantilla de caja blanca del bloque de construcción x.1>_


 5.3.2 Caja Blanca <bloque de construcción x.2>
 -----------------------------------------------

 _<inserta plantilla de caja blanca del bloque de construcción x.2>_


 5.3.3 Caja Blanca <bloque de construcción y.1>
 -----------------------------------------------

 _<inserta plantilla de caja blanca del bloque de construcción y.1>_

----

Subsecciones
============

Para cada **bloque de construcción** del nivel 2 que se descompone en nivel 3, crea una subsección 5.3.x como:

5.3.1 Caja Blanca _<bloque de construcción x.1>_
-------------------------------------------------

Especifica la **estructura interna** de *bloque de construcción x.1*.

**<inserta plantilla de caja blanca del bloque de construcción x.1>**

5.3.2 Caja Blanca _<bloque de construcción x.2>_
-------------------------------------------------

**<inserta plantilla de caja blanca del bloque de construcción x.2>**

5.3.3 Caja Blanca _<bloque de construcción y.1>_
-------------------------------------------------

**<inserta plantilla de caja blanca del bloque de construcción y.1>**

----

Niveles Adicionales
===================

**Cuándo agregar más niveles:**

Agrega niveles 4, 5, etc., cuando:

* Los **bloques de construcción** del nivel 3 aún son muy complejos
* Necesitas mostrar detalles de implementación específicos
* La **descomposición** ayuda a la comprensión del sistema
* Los stakeholders lo requieren para su trabajo

**Cómo agregar más niveles:**

1. Copia la estructura de esta sección (5.3)
2. Renombra a 5.4 Nivel 4, 5.5 Nivel 5, etc.
3. Aplica la misma **plantilla de caja blanca**
4. Mantén la consistencia en la documentación

**Advertencia:**

Ten cuidado de no crear demasiados niveles de **descomposición**. Usualmente, 2-3 niveles son suficientes. Más niveles pueden:

* Hacer la documentación difícil de mantener
* Confundir a los lectores
* Mezclar arquitectura con detalles de implementación
* Volverse obsoletos rápidamente

----

Guía de Profundidad
===================

**Nivel 1:** Sistema completo (obligatorio)
 Visión general del sistema como **caja blanca** con sus **bloques de construcción** principales como **cajas negras**.

**Nivel 2:** Descomposición de bloques importantes (recomendado)
 **Estructura interna** de **bloques de construcción** críticos o complejos del nivel 1.

**Nivel 3:** Detalles adicionales (opcional)
 **Descomposición** de **bloques de construcción** del nivel 2 cuando sea necesario.

**Nivel 4+:** Casos especiales (raro)
 Solo cuando sea absolutamente necesario para sistemas muy complejos.

----

Referencias
===========

* :ref:`seccion_05` - Sección principal
* :ref:`seccion_5_1` - Caja Blanca del Sistema General
* :ref:`seccion_5_2` - Nivel 2

:Subsección: 5.3
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
