.. meta::
   :layout: post
   :title: Consejo 1-8: ¡Usa una lista numerada para describir requisitos funcionales!
   :tags: requirement functional-requirement
   :category: requirements
   :permalink: /tips/1-8/

.. _introduccion-tip-8:

===================================================================
Consejo 1-8: ¡Usa una lista numerada!
===================================================================

:Subtítulo: Para describir requisitos funcionales
:Tema: Listas numeradas como alternativa simple
:Categoría: Requisitos
:Audiencia: Arquitectos, Analistas

----

Recomendación
=============

En este contexto también podrías usar listas numeradas como una forma simple y 
pragmática de describir actividades, procedimientos o procesos.

El diagrama de actividad del :ref:`introduccion-tip-6` podría entonces documentarse 
de la siguiente manera:

1. Autenticación
2. Seleccionar un producto
3. Verificar tipo de cliente
   
   a. Cliente privado: agregar el IVA (impuesto al valor agregado)
   b. Cliente empresarial: solicitar el ID de IVA

4. Crear factura

----

Consideración
=============

En caso de que tengas que describir procesos concurrentes, los diagramas de 
actividad (ver :ref:`introduccion-tip-6`) son la mejor opción.

----

.. note::
   **Información de traducción:**
   
   - Archivo original: 2016-03-01-t-1-8.md
   - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
   - Fecha: 2026-01-27
