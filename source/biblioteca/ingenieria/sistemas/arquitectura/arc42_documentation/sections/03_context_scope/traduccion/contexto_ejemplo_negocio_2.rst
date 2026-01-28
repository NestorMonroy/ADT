.. _contexto_ejemplo_negocio_2:

============================================================
Ejemplo de Contexto de Negocio: MaMa
============================================================

.. note::
   **Ejemplo arc42**
   
   Un diagrama simple con una breve explicación en una tabla.

----

3. Vista de Contexto
====================

3.1 Contexto de Negocio
-----------------------

.. figure:: ../figuras/3-Mama-Business-Context.png
   :alt: Contexto de negocio
   :align: center
   :width: 80%
   
   Diagrama de contexto de negocio de MaMa

Elementos del Contexto
=======================

.. list-table:: 
   :header-rows: 1
   :widths: 30 70
   
   * - Elemento
     - Descripción
   * - **MaMa**
     - Nuestro sistema (sistema bajo diseño)
   * - **Mandator**
     - La organización que proporciona a MaMa datos de clientes y direcciones, y paga por su servicio
   * - **PrintService**
     - Compañía que imprime cartas en nombre de MaMa. Acepta PDF, PostScript o AFP como formato de entrada
   * - **...**
     - ...

----

Observaciones
=============

Este ejemplo muestra un **contexto de negocio** donde:

* El sistema (MaMa) se representa como **caja negra**
* Se identifican los **socios de comunicación** principales
* Se especifican las **interfaces de dominio** con descripción clara
* Se documentan los formatos de intercambio de datos

.. seealso::
   * :ref:`seccion_3_1` - Plantilla de Contexto de Negocio
   * :ref:`seccion_03` - Contexto y Alcance completo

----

:Ejemplo: Contexto de Negocio
:Sistema: MaMa
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
