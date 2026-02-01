.. _seccion_5_1:




5.1 Caja Blanca del Sistema General
===================================

.. note::
 **Plantilla arc42 - Traducción Arquitectónica (Paso 3.4)**

 Términos clave:
 * White box -> Caja blanca
 * Black box -> Caja negra
 * Building block -> Bloque de construcción
 * Decomposition -> Descomposición




Aquí describes la **descomposición** del sistema general usando la siguiente **plantilla de caja blanca**.
Contiene:

* Un diagrama de visión general
* Una motivación para la **descomposición**
* Descripciones de **caja negra** de los **bloques de construcción** contenidos. Para estos te ofrecemos alternativas:

 * Usa *una* tabla para una visión general corta y pragmática de todos los **bloques de construcción** contenidos y sus **interfaces**
 * Usa una lista de descripciones de **caja negra** de los **bloques de construcción** según la plantilla de caja negra (ver abajo). Dependiendo de tu elección de herramienta, esta lista podría ser subcapítulos (en archivos de texto), subpáginas (en un Wiki) o elementos anidados (en una herramienta de modelado).

* (Opcional:) **Interfaces** importantes, que no se explican en las plantillas de caja negra de un **bloque de construcción**, pero son muy importantes para entender la caja blanca.

Dado que hay muchas formas de especificar **interfaces**, no proporcionamos una plantilla específica para ellas.

En el mejor de los casos, te irá bien con ejemplos o firmas simples.




Plantilla de Caja Blanca
========================

.. code-block:: text

 5.1 Caja Blanca del Sistema General
====================================

 **<inserta diagrama de visión general del sistema general>**

 Motivación
===========

 **<describe motivación/razonamiento para la descomposición del sistema general>**

 Bloques de Construcción Contenidos
===================================

 **<describe bloques de construcción contenidos (cajas negras)>**

Insertar tus explicaciones de cajas negras del nivel 1:

Si usas forma tabular, solo describirás tus cajas negras con nombre y **responsabilidad** según el siguiente esquema:

.. list-table:: Bloques de Construcción Nivel 1
 :header-rows: 1
 :widths: 30 70

 * - **Nombre**
   - **Responsabilidad**
 * - *<caja negra 1>*
   - *<Texto>*
 * - *<caja negra 2>*
   - *<Texto>*

Su encabezado es el nombre de la caja negra.
Si usas una lista de descripciones de caja negra, entonces llenas una plantilla de caja negra separada para cada **bloque de construcción** importante.

A veces puede ser útil complementar la tabla con columnas adicionales:

.. list-table:: Bloques de Construcción con Información Adicional
 :header-rows: 1
 :widths: 25 35 20 20

 * - **Nombre**
   - **Responsabilidad**
   - **Interfaces**
   - **Código**
 * - *<caja negra 1>*
   - *<Texto>*
   - ¿Cuáles son las **interfaces** principales de este bloque?
   - ¿Dónde está ubicado el código?
 * - *<caja negra 2>*
   - *<Texto>*
   - ---"---
   - ---"---

Interfaces Importantes (Opcional)
=================================

**<(opcional) describe interfaces importantes>**




Plantilla de Caja Negra
=======================

Aquí describes <caja negra 1> según la siguiente **plantilla de caja negra**:

Elementos de la Plantilla
=========================

* **Propósito/Responsabilidad**
* **Interfaz(ces)**, cuando no se extraen como párrafos separados. Estas **interfaces** pueden incluir cualidades y características de rendimiento.
* (Opcional) Características de Calidad/Rendimiento de la caja negra, por ejemplo, disponibilidad, comportamiento en tiempo de ejecución, ...
* (Opcional) Ubicación de directorio/archivo
* (Opcional) Requisitos cumplidos (si necesitas trazabilidad a requisitos).
* (Opcional) Problemas/asuntos/riesgos abiertos

Puedes usar una tabla o texto.

Ejemplo de Plantilla
====================

.. code-block:: text

 _<Nombre Caja Negra 1>_

 Propósito/Responsabilidad:
 _<Propósito/Responsabilidad>_

 Interfaz(ces):
 _<Interfaz(ces)>_

 (Opcional) Características de Calidad/Rendimiento:
 _<(Opcional) Características de Calidad/Rendimiento>_

 (Opcional) Ubicación de Directorio/Archivo:
 _<(Opcional) Ubicación de Directorio/Archivo>_

 (Opcional) Requisitos Cumplidos:
 _<(Opcional) Requisitos Cumplidos>_

 (Opcional) Problemas/Asuntos/Riesgos Abiertos:
 _<(opcional) Problemas/Asuntos/Riesgos Abiertos>_

Repetir para Cada Caja Negra
============================

.. code-block:: text

 _<Nombre caja negra 2>_

 _<plantilla de caja negra>_

 _<Nombre caja negra n>_

 _<plantilla de caja negra>_

Interfaces Opcionales
=====================

.. code-block:: text

 _<Nombre interfaz 1>_




 _<Nombre interfaz m>_




Referencias
===========

* :ref:`seccion_05` - Sección principal
* :ref:`seccion_5_2` - Nivel 2
* :ref:`seccion_5_3` - Nivel 3

:Subsección: 5.1
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
