.. _contexto_tip_18:

===============================================================
Tip 3-18: ¡Explica la relación entre las interfaces de dominio y su realización técnica!
===============================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Mapea **interfaces de dominio** (del **contexto de negocio**) a **interfaces técnicas** (del **contexto técnico**).

----

En caso de que tus **interfaces de dominio** se realicen en la infraestructura técnica a través de diferentes **canales** técnicos, **protocolos** o **interfaces**, debes describir explícitamente el mapeo entre esas dos *áreas*.

Un ejemplo simple de tal situación se puede encontrar en el diagrama siguiente. Las relaciones (mapeo) pueden describirse fácilmente con una tabla:

.. list-table:: Mapeo de interfaces de dominio a realización técnica
   :header-rows: 1
   :widths: 50 50
   
   * - Interfaz de dominio
     - Implementación técnica
   * - Interrupción de freno, anulación del conductor, revoluciones por minuto, válvula de aceleración, posiciones
     - Bus CAN
   * - Comandos del usuario
     - Interruptores, teclas, palancas en cabina
   * - Información de estado
     - Salida de audio, pantalla en cabina

.. figure:: ../figuras/03-context-for-mapping.webp
   :alt: Diagrama de contexto para mapeo
   :align: center
   :width: 80%
   
   Mapeo entre interfaces de dominio y su realización técnica

----

.. seealso::
   * :ref:`seccion_3_1` - Contexto de Negocio
   * :ref:`seccion_3_2` - Contexto Técnico
   * :ref:`contexto_tip_10` - Diferenciación business/technical

----

:Tip: 3-18
:Tema: Mapeo de interfaces dominio-técnicas
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
