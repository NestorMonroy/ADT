.. _seccion_5_2:




5.2 Nivel 2
===========

.. note::
 **Plantilla arc42 - Traducción Arquitectónica (Paso 3.4)**

 Términos clave:
 * Level 2 -> Nivel 2
 * White box -> Caja blanca
 * Building block -> Bloque de construcción
 * Internal structure -> Estructura interna




Aquí puedes especificar la **estructura interna** de (algunos) **bloques de construcción** del nivel 1 como **cajas blancas**.

Debes decidir cuáles **bloques de construcción** de tu sistema son lo suficientemente importantes como para justificar tal descripción detallada. Por favor, prefiere relevancia sobre completitud. Especifica **bloques de construcción** importantes, sorprendentes, riesgosos, complejos o volátiles. Deja fuera partes normales, simples, aburridas o estandarizadas de tu sistema.




Plantilla Nivel 2
=================

.. code-block:: text

 5.2 Nivel 2
============

 5.2.1 Caja Blanca <bloque de construcción 1>
=============================================

 Especifica la estructura interna de *bloque de construcción 1*.

 Usa la plantilla de caja blanca (ver arriba).

 *<inserta plantilla de caja blanca del bloque de construcción 1>*


 5.2.2 Caja Blanca <bloque de construcción 2>
=============================================

 _<inserta plantilla de caja blanca para el bloque de construcción 2>_




 5.2.n Caja Blanca <bloque de construcción n>
=============================================

 _<inserta plantilla de caja blanca para el bloque de construcción n>_




Subsecciones
============

Para cada **bloque de construcción** del nivel 1 que se descompone en nivel 2, crea una subsección 5.2.x como:

5.2.1 Caja Blanca _<bloque de construcción 1>_
==============================================

Especifica la **estructura interna** de *bloque de construcción 1*.

Usa la **plantilla de caja blanca** (ver :ref:`seccion_5_1`).

**<inserta plantilla de caja blanca del bloque de construcción 1>**

5.2.2 Caja Blanca _<bloque de construcción 2>_
==============================================

**<inserta plantilla de caja blanca para el bloque de construcción 2>**




5.2.n Caja Blanca _<bloque de construcción n>_
==============================================

**<inserta plantilla de caja blanca para el bloque de construcción n>**




Guía de Uso
===========

**Cuándo usar Nivel 2:**

Usa el nivel 2 para **bloques de construcción** que:

* Son complejos y requieren explicación adicional
* Tienen una **descomposición** interna significativa
* Son críticos para la arquitectura
* Son riesgosos o innovadores
* Necesitan comunicarse claramente a los stakeholders

**Cuándo NO usar Nivel 2:**

No descompongas **bloques de construcción** que:

* Son simples y auto-explicativos
* Son componentes estándar o frameworks conocidos
* No agregan valor arquitectónico al documentarse
* Son detalles de implementación




Referencias
===========

* :ref:`seccion_05` - Sección principal
* :ref:`seccion_5_1` - Caja Blanca del Sistema General
* :ref:`seccion_5_3` - Nivel 3

:Subsección: 5.2
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
