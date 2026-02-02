.. _seccion_3_1:




3.1 Contexto de Negocio
=======================

.. note::
 **Plantilla arc42 - Traducción Arquitectónica (Paso 3.4)**

 Términos clave:
 * Business context -> Contexto de negocio
 * Communication partner -> Socio de comunicación
 * Domain interface -> Interfaz de dominio




Contenido
=========

Especificación de *todos* los socios de comunicación (usuarios, sistemas IT, ...) con explicaciones de entradas y salidas específicas del dominio o interfaces.

Opcionalmente puedes agregar formatos específicos del dominio o protocolos de comunicación.

Motivación
==========

Todos los stakeholders deben comprender qué datos se intercambian con el entorno del sistema.

Forma
=====

Todo tipo de diagramas que muestren el sistema como una **caja negra** y especifiquen las interfaces de dominio con los socios de comunicación.

Alternativamente (o adicionalmente) puedes usar una tabla. El título de la tabla es el nombre de tu sistema, las tres columnas contienen el nombre del socio de comunicación, las entradas, y las salidas.

.. seealso::
 Ver ejemplos de contexto de negocio en la sección de ejemplos




Plantilla
=========

.. code-block:: text

 3.1 Contexto de Negocio
========================

 **<inserta diagrama o tabla>**

 Descripción de socios de comunicación externos:

+------------------------+-------------------+-------------------+
| Socio de Comunicación  | Entradas          | Salidas           |
+========================+===================+===================+
| <nombre del socio 1>   | <datos recibidos> | <datos enviados>  |
+------------------------+-------------------+-------------------+
| <nombre del socio 2>   | <datos recibidos> | <datos enviados>  |
+------------------------+-------------------+-------------------+

 **(Opcional:) Explicación de las interfaces de dominio externas**

 **<nombre del socio>:**

 <Descripción detallada de la interfaz, formatos de datos,
 protocolos de comunicación específicos del dominio>




Referencias
===========

* :ref:`seccion_03` - Sección principal
* :ref:`seccion_3_2` - Contexto técnico
* Ejemplos de contexto de negocio

:Subsección: 3.1
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
