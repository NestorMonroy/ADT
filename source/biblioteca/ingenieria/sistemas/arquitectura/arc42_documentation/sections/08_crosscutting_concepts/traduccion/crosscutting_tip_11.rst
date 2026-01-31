====================================================================

Tip 8-11: ¡(Hiper)Enlace entre Bloques de Construcción y Conceptos!
===================================================================

.. meta::
   :layout: post
   :title: Tip 8-11: ¡(Hiper)Enlace entre Bloques de Construcción y Conceptos!
   :tags: concepto
   :category: conceptos
   :permalink: /tips/8-11/

Los conceptos transversales y los bloques de construcción están íntimamente relacionados.

Establezca enlaces bidireccionales entre ellos:

De Bloques de Construcción a Conceptos
======================================

En la descripción de un bloque de construcción (Sección 5), mencione qué conceptos
transversales son relevantes:

   *"Este servicio implementa el* **concepto de autenticación** *descrito en la Sección 8.3"*

De Conceptos a Bloques de Construcción
======================================

En la documentación de un concepto (Sección 8), liste qué bloques de construcción
lo implementan o se ven afectados por él:

.. note::
   **Concepto de Logging (Sección 8.2)**
   
   Implementado por:
   
   * Logger Service (Sección 5.1.3)
   * Todos los servicios backend (usan Logger Service)
   * Frontend Application (log client-side)

Beneficios
==========

* **Navegación más fácil** en la documentación
* **Comprensión más rápida** de dependencias
* **Mejor trazabilidad** de decisiones arquitectónicas
* **Mantenimiento más simple** de la documentación

.. tip::
   Use referencias cruzadas de Sphinx para crear hipervínculos automáticos:
   
   ``ver :ref:`concepto-autenticacion```
