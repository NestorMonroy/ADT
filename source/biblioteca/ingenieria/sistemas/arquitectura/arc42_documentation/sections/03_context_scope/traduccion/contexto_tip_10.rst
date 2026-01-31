.. _contexto_tip_10:




Tip 3-10: ¡Diferencia el contexto de negocio y técnico!
=======================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Especialmente con sistemas de información, a menudo puedes ignorar detalles técnicos de la infraestructura dentro del contexto y enfocarte en aspectos relacionados con el dominio o negocio.
   
   Sin embargo, si el hardware o la tecnología juegan un rol importante para tu sistema, necesitas tanto un contexto de negocio (dominio) como un **contexto técnico**.




Ejemplo de Sistema Embebido (Automotriz)
========================================

En la figura siguiente puedes encontrar un ejemplo simplificado del mundo embebido: la parte izquierda muestra el **contexto de negocio** (dominio), la parte derecha representa el **contexto técnico**.

.. .. figure:: ../figuras/03-technical-context-automotive.png
..       :alt: Contexto automotriz - negocio y técnico
..       :align: center
..       :width: 90%
   
..       Diagrama de contexto para sistema automotriz (negocio y técnico)

Ejemplo de Sistema Basado en Web
================================

La figura siguiente muestra un pequeño ejemplo de un sistema de información (basado en web) con **contexto de negocio** y **contexto técnico**.

Reconoces protocolos como HTTPS o SSH dentro del contexto técnico, los cuales intencionalmente no se mencionan en el contexto de dominio.

Además, el componente "Reporting" (desde un punto de vista de dominio externo) se despliega en la misma infraestructura técnica que el sistema principal.

.. .. figure:: ../figuras/03-technical-context-info-sys.webp
..       :alt: Sistema de información - negocio y técnico
..       :align: center
..       :width: 90%
   
..       Ejemplo de sistema de información basado en web con contextos de negocio y técnico




.. seealso::
   * :ref:`seccion_3_1` - Contexto de Negocio
   * :ref:`seccion_3_2` - Contexto Técnico
   * :ref:`seccion_03` - Contexto y Alcance




:Tip: 3-10
:Tema: Diferenciación business vs technical context
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
