.. _contexto_tip_12:




Tip 3-12: ¡Muestra influencias externas en el contexto!
=======================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Tu sistema podría necesitar manejar diferentes tipos de dependencias con sistemas externos.




Tipos de Dependencias
=====================

Tu sistema podría necesitar manejar diferentes tipos de dependencias con sistemas externos, por ejemplo:

* Dependencias de datos o información
* Dependencias temporales
* Dependencias locales o espaciales
* Dependencias de hardware
* Dependencias de personas, organizaciones o roles
* Dependencias transitivas (indirectas)

A menudo solo mostrarás roles de usuario y dependencias de datos/información en el **contexto de dominio**. Sin embargo, a veces otros tipos de dependencias también pueden ser importantes para tu sistema. Tales dependencias pueden describirse en el diagrama mismo o en una explicación adicional.

Ejemplo
=======

Se muestra un ejemplo en la siguiente figura: los usuarios deben registrarse antes de usar el sistema (paso 1), el sistema ordena la mensajería de texto (paso 2), que un proveedor externo de mensajes de texto envía a través de la red móvil (paso 3). El usuario ingresa el código (paso 4), y en el paso 5, el sistema verifica la identidad de una persona contra un servidor externo de identidad de sucursal, que, a su vez, activa una verificación en una oficina de registro (paso 6).

Los pasos 3 y 6 son dependencias transitivas (también llamadas indirectas). El sistema depende de la oficina de registro, aunque no usa su interfaz directamente. El sistema es mantenido por administradores, quienes solo tienen acceso a través de un dispositivo de hardware (Control de Acceso por Hardware, HAC). El sistema y el HAC deben estar físicamente en la misma habitación - una dependencia espacial.

Algunas de estas dependencias tienen impacto en el logro de los requisitos de calidad para tu sistema - y por lo tanto podrían ser riesgos (ver tip 3-4, Mostrar riesgos en el contexto).

.. .. figure:: ../figuras/03-context-different-dependencies.webp
..       :alt: Ejemplo de diagrama de dependencias
..       :align: center
..       :width: 90%
   
..       Ejemplo: diferentes tipos de dependencias en el contexto




.. seealso::
   * :ref:`seccion_03` - Contexto y Alcance
   * :ref:`contexto_tip_4` - Riesgos en el contexto
   * :ref:`contexto_tip_13` - Dependencias transitivas




:Tip: 3-12
:Tema: Influencias externas
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
