.. _seccion_07:

===============================================================
Sección 07: Vista de Despliegue (Deployment View)
===============================================================

.. tip::
   **Vista de Despliegue arc42**
   
   La **vista de despliegue** describe el **entorno** técnico en el cual el sistema se ejecuta: **hardware**, **infraestructura**, **nodos** y **mapeo** de **bloques de construcción** al **hardware**.

----

Introducción
============

La **vista de despliegue** (o **deployment view**) muestra la **infraestructura** técnica donde el sistema reside y se ejecuta.

Contenido
=========

La **vista de despliegue** describe:

* La **infraestructura** técnica usada para ejecutar tu sistema, con elementos de **infraestructura** como ubicaciones geográficas, **entornos**, computadoras, procesadores, canales y topologías de **red** así como otros elementos de **infraestructura** y
* El **mapeo** de **bloques de construcción** (software) a esos elementos de **infraestructura**.

A menudo los sistemas son ejecutados en diferentes **entornos**, por ejemplo **entorno** de desarrollo, **entorno** de pruebas, **entorno** de **producción**. En tales casos deberías documentar todos los **entornos** relevantes.

Especialmente documenta la **vista de despliegue** cuando tu software es ejecutado como sistema distribuido con más de una computadora, procesador, **servidor** o **contenedor** o cuando diseñas y construyes tus propios procesadores y chips de **hardware**.

Desde una perspectiva de software es suficiente capturar aquellos elementos de la **infraestructura** que son necesarios para mostrar el **despliegue** de tus **bloques de construcción**. Los arquitectos de **hardware** pueden ir más allá de eso y describir la **infraestructura** a cualquier nivel de detalle que necesiten capturar.

Los elementos típicos incluyen:

* **Nodos** de **hardware** (servidores, dispositivos, etc.)
* **Infraestructura** de red
* **Entornos** de **ejecución** (producción, staging, desarrollo)
* **Mapeo** de software (bloques de construcción) a **hardware**

----

Contenido de la Sección
========================

Esta sección contiene:

**Tips de Vista de Despliegue (10 tips)**
   Consejos prácticos para documentar el **despliegue** del sistema

**Ejemplos de Aplicación (3 ejemplos)**
   Casos reales de **vistas de despliegue** en sistemas

----

Tips de Vista de Despliegue
============================

.. toctree::
   :maxdepth: 1
   :caption: Consejos para Deployment View
   
   deployment_tip_1
   deployment_tip_2
   deployment_tip_3
   deployment_tip_4
   deployment_tip_5
   deployment_tip_6
   deployment_tip_7
   deployment_tip_8
   deployment_tip_9
   deployment_tip_10

----

Ejemplos de Deployment View
============================

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos de Aplicación
   
   deployment_ejemplo_tpu_1
   deployment_ejemplo_htmlsc
   deployment_ejemplo_tpu_2

----

Motivación
==========

El software no se ejecuta sin **hardware**. Esta **infraestructura** subyacente puede y va a influenciar tu sistema y/o algunos conceptos transversales. Por lo tanto, necesitas conocer la **infraestructura**.

Debes documentar la **vista de despliegue** si:

* Los stakeholders necesitan entender la **infraestructura** técnica
* El **mapeo** de software a **hardware** no es obvio
* Existen múltiples **entornos** de **despliegue**
* Decisiones de **hardware** impactan la arquitectura
* Se requiere planificación de capacidad o escalabilidad

----

Forma y Notación
================

Quizás el **diagrama de despliegue** de más alto nivel ya está contenido en sección 3.2 como contexto técnico con tu propia **infraestructura** como UNA caja negra. En esta sección harás zoom dentro de esta caja negra usando **diagramas de despliegue** adicionales.

UML ofrece **diagramas de despliegue** para expresar esa vista. Úsalo, probablemente con diagramas anidados, cuando tu **infraestructura** sea más compleja.

Cuando tus stakeholders (de **hardware**) prefieran otros tipos de diagramas en lugar de **diagrama de despliegue** UML, déjalos usar cualquier tipo que sea capaz de mostrar **nodos** y canales de la **infraestructura**.

Existen varias notaciones para describir el **despliegue**:

**Diagramas UML:**
  * **Diagramas de despliegue** - Muestran **nodos** y **artefactos**
  * Diagramas de **componentes** con estereotipos de **despliegue**

**Otras notaciones:**
  * Tablas de **mapeo** software/**hardware**
  * Diagramas de **infraestructura** de red
  * Descripciones textuales de **nodos**
  * Diagramas de arquitectura en **nube**

----

Relación con Otras Secciones
=============================

**Sección 05 (Building Block View)**
   Los **bloques de construcción** se mapean a **nodos** de **hardware** en la **vista de despliegue**

**Sección 06 (Runtime View)**
   Los **escenarios de tiempo de ejecución** ocurren en el **entorno** de **despliegue**

**Sección 08 (Conceptos Transversales)**
   Conceptos como seguridad, logging, monitoreo se implementan en la **infraestructura**

----

7.1 Infraestructura Nivel 1
============================

Describe (usualmente en una combinación de diagramas, tablas y texto):

* La distribución de tu sistema a múltiples ubicaciones, **entornos**, computadoras, procesadores, ... así como las conexiones físicas entre ellos
* Justificación o motivación importante para esta estructura de **despliegue**
* Características de calidad y/o desempeño de la **infraestructura**
* El **mapeo** de **artefactos** de software (**bloques de construcción**) a elementos de la **infraestructura**

Para múltiples **entornos** o **despliegues** alternativos, por favor copia esta sección de arc42 para todos los **entornos** relevantes.

.. code-block:: text

   < insertar diagrama de vista general de infraestructura >

Motivación
----------

.. code-block:: text

   < insertar descripción de motivación o explicación en forma de texto >

Características de Calidad y/o Desempeño (opcional)
----------------------------------------------------

.. code-block:: text

   < opcionalmente insertar descripción de características de calidad o desempeño >

Mapeo
-----

.. code-block:: text

   < insertar descripción del mapeo de bloques de construcción >

----

7.2 Infraestructura Nivel 2
============================

Aquí puedes incluir la estructura interna de (algunos) elementos de **infraestructura** del **nivel de infraestructura** 1.

Por favor copia la estructura del nivel 1 para cada elemento seleccionado.

7.2.1 <Elemento de Infraestructura 1>
--------------------------------------

.. code-block:: text

   < insertar diagrama + explicación >

7.2.2 <Elemento de Infraestructura 2>
--------------------------------------

.. code-block:: text

   < insertar diagrama + explicación >

7.2.n <Elemento de Infraestructura n>
--------------------------------------

.. code-block:: text

   < insertar diagrama + explicación >

----

Información Adicional
=====================

Para más información sobre **vista de despliegue**, consulta:

**Preguntas Relacionadas**
   Ver `aquí <https://faq.arc42.org/category_c/>`_ para preguntas relacionadas con **infraestructura** técnica, **hardware**, **entornos** o **despliegue**.

**Tips de Deployment View**
   Consulta los 10 tips arriba para consejos prácticos sobre cómo documentar la **vista de despliegue**.

**Ejemplos de Aplicación**
   Revisa los 3 ejemplos arriba para ver casos reales de **vistas de despliegue**.

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_06` - Vista de Tiempo de Ejecución
   * :ref:`seccion_08` - Conceptos Transversales

----

:Sección: 07
:Título: Vista de Despliegue
:Nombre Original: Deployment View
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1
:Total archivos: 14 (1 principal + 10 tips + 3 ejemplos)