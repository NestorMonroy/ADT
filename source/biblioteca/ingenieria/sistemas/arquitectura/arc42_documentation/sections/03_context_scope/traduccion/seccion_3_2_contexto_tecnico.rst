.. _seccion_3_2:

=====================================
3.2 Contexto Técnico
=====================================

.. note::
 **Plantilla arc42 - Traducción Arquitectónica (Paso 3.4)**

 Términos clave:
 * Technical context -> Contexto técnico
 * Channel -> Canal
 * Transmission media -> Medio de transmisión
 * Technical interface -> Interfaz técnica

----

Contenidos
==========

Interfaces técnicas (canales y medios de transmisión) que vinculan tu sistema con su entorno.

Además, un mapeo de entrada/salida específica del dominio a los canales, es decir, una explicación de qué E/S usa qué canal.

Motivación
==========

Muchos stakeholders toman decisiones arquitectónicas basadas en las interfaces técnicas entre el sistema y su contexto. Especialmente los diseñadores de infraestructura o hardware deciden estas interfaces técnicas.

Forma
=====

Por ejemplo, un diagrama de despliegue UML que describe los canales hacia sistemas vecinos, junto con una tabla de mapeo que muestra las relaciones entre canales y entrada/salida.

.. seealso::
 Ver ejemplos de contexto técnico en la sección de ejemplos

----

Plantilla
=========

.. code-block:: text

 3.2 Contexto Técnico
 ====================

 **<inserta diagrama o tabla>**

 Descripción de canales técnicos:

 +-------------------+----------------------+---------------------------+
 | Canal | Tipo/Protocolo | Descripción |
 +===================+======================+===========================+
 | <nombre canal 1> | <HTTP/REST/MQTT/etc> | <descripción del canal> |
 +-------------------+----------------------+---------------------------+
 | <nombre canal 2> | <protocolo> | <descripción> |
 +-------------------+----------------------+---------------------------+

 **Mapeo de Entrada/Salida a Canales:**

 +------------------------+----------------+---------------------------+
 | Entrada/Salida | Canal | Observaciones |
 +========================+================+===========================+
 | <datos de negocio 1> | <canal 1> | <detalles técnicos> |
 +------------------------+----------------+---------------------------+
 | <datos de negocio 2> | <canal 2> | <detalles técnicos> |
 +------------------------+----------------+---------------------------+

 **(Opcional:) Explicación de las interfaces técnicas**

 **<nombre del canal>:**

 <Descripción detallada de la interfaz técnica, protocolos,
 puertos, formatos de serialización, seguridad, etc.>

----

Referencias
===========

* :ref:`seccion_03` - Sección principal
* :ref:`seccion_3_1` - Contexto de negocio
* Ejemplos de contexto técnico

:Subsección: 3.2
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
