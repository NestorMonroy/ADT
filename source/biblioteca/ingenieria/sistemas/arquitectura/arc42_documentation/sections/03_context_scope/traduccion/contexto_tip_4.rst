.. _contexto_tip_4:

===============================================================
Tip 3-4: ¡Indica explícitamente los riesgos en el contexto!
===============================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Algunos ejemplos de riesgos que debes señalar claramente en el contexto.

----

Tipos de Riesgos a Señalar
===========================

* **Riesgo de disponibilidad:** si sistemas externos influyen en la disponibilidad de tu sistema.
* **Riesgo de costo:** si usar un sistema externo es costoso, llamadas individuales u otros tipos de uso cuestan dinero. Ejemplos son verificaciones de tarjetas de crédito o servicios de pago/reserva.
* **Riesgos de seguridad:** si recibes/envías datos sensibles desde/hacia sistemas externos. Eso podría hacer estas **interfaces externas** particularmente interesantes para un atacante potencial.
* **Volatilidad (alta probabilidad de cambio) de sistemas externos:** si las interfaces de sistemas externos cambian a menudo (están "en progreso"). La sintaxis y semántica de los datos transmitidos podrían cambiarse con poco aviso, lo que significa que o tienes esfuerzo adaptándote a estos cambios o necesitas desarrollar un consumidor flexible para estas interfaces.
* **Riesgos de complejidad:** si usar esta interfaz es excepcionalmente complejo o difícil, porque podría tener estructuras de datos complejas, usar frameworks esotéricos, apretones de manos complicados o una mezcla arbitraria de esos.
* **Riesgos operacionales:** si operar/administrar la interfaz es especialmente difícil o requiere alto esfuerzo manual.

Ejemplo
=======

Ver el siguiente ejemplo, donde un riesgo se marca explícitamente con una etiqueta roja:

.. figure:: ../figuras/03-context-with-risk.png
   :alt: Contexto HTML Sanity Checker con riesgo marcado
   :align: center
   :width: 80%
   
   Contexto con riesgo marcado: "verifica sitios web y recursos externos"

Opciones para Documentar Riesgos
=================================

Puedes:

* Usar colores llamativos u otros medios visuales para indicar riesgo en el diagrama de contexto
* Usar color de texto en la tabla que explica el diagrama, o
* Crear una lista explícita de riesgos para riesgos en **interfaces externas** o **sistemas vecinos**

----

.. seealso::
   * :ref:`seccion_03` - Contexto y Alcance
   * :ref:`contexto_tip_1` - Demarcación del sistema

----

:Tip: 3-4
:Tema: Riesgos en el contexto
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
