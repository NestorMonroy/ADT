.. _seccion_05:



5. Vista de Bloques de Construcción




.. note::
 **Traducción con Paso 3.4 (Traducción Arquitectónica)**

 Esta sección aplica terminología arquitectónica coherente con arc42.

.. note::
 **Estado de traducción:**

 Sección 05 - Building Block View (Vista de Bloques de Construcción)

 Traducción: Método Peshitta + Paso 3.4
 Workflow: v1.6.0




Contenido
=========

La **vista de bloques de construcción** muestra la **descomposición** estática del sistema en **bloques de construcción** (módulos, **componentes**, **subsistemas**, clases, **interfaces**, paquetes, librerías, frameworks, capas, particiones, tiers, funciones, macros, operaciones, estructuras de datos, ...) así como sus **dependencias** (relaciones, asociaciones, ...)

Esta vista es obligatoria para toda documentación de arquitectura.
En analogía a una casa, este es el *plano*.

Motivación
==========

Mantén una visión general de tu código fuente haciendo su estructura comprensible a través de la abstracción.

Esto te permite comunicarte con tus stakeholders a un nivel abstracto sin revelar detalles de implementación.

Forma
=====

La **vista de bloques de construcción** es una colección jerárquica de **cajas blancas** y **cajas negras** (ver figura abajo) y sus descripciones.

.. .. figure:: ../figuras/05-building-block-hierarchy.png
..     :alt: Jerarquía de bloques de construcción
..     :align: center
..     :width: 80%

..     Alcance y Contexto, Diagrama de Nivel 1 y Nivel 2

* **Nivel 1** es la descripción de **caja blanca** del sistema general junto con descripciones de **caja negra** de todos los **bloques de construcción** contenidos.
* **Nivel 2** hace zoom en algunos **bloques de construcción** del nivel 1. Así contiene la descripción de **caja blanca** de **bloques de construcción** seleccionados del nivel 1, junto con descripciones de **caja negra** de sus **bloques de construcción** internos.
* **Nivel 3** (no mostrado en el diagrama arriba) hace zoom en detalles de **bloques de construcción** seleccionados del nivel 2, y así sucesivamente.




Subsecciones
============

.. toctree::
 :maxdepth: 2

 seccion_5_1_whitebox_sistema
 seccion_5_2_nivel_2
 seccion_5_3_nivel_3

Ejemplos Prácticos
==================

.. toctree::
 :maxdepth: 1

 bloques_ejemplo_hsc
 bloques_ejemplo_status
 bloques_ejemplo_tpu_nivel_1
 bloques_ejemplo_tpu_nivel_2

Tips y Consejos
===============

.. toctree::
 :maxdepth: 1

 bloques_tip_1
 bloques_tip_2
 bloques_tip_3
 bloques_tip_4
 bloques_tip_5
 bloques_tip_6
 bloques_tip_7
 bloques_tip_8
 bloques_tip_9
 bloques_tip_10
 bloques_tip_11
 bloques_tip_12
 bloques_tip_13
 bloques_tip_14
 bloques_tip_15
 bloques_tip_16
 bloques_tip_17
 bloques_tip_18
 bloques_tip_19
 bloques_tip_20
 bloques_tip_21
 bloques_tip_22
 bloques_tip_23
 bloques_tip_24
 bloques_tip_25
 bloques_tip_26
 bloques_tip_27
 bloques_tip_28




.. note::
 **Términos Arquitectónicos Clave (Paso 3.4):**

 * Building block -> Bloque de construcción
 * Building block view -> Vista de bloques de construcción
 * White box -> Caja blanca
 * Black box -> Caja negra
 * Decomposition -> Descomposición
 * Component -> Componente
 * Subsystem -> Subsistema
 * Module -> Módulo
 * Interface -> Interfaz
 * Dependency -> Dependencia
 * Level -> Nivel
 * Hierarchy -> Jerarquía
 * Responsibility -> Responsabilidad

:Sección: 05 - Vista de Bloques de Construcción
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
