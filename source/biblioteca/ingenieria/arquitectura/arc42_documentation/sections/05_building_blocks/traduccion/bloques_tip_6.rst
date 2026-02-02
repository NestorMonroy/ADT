.. _bloques_tip_6:




Tip 5-6: ¡Oculta el funcionamiento interno de las cajas negras!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Las **cajas negras** respetan el principio de ocultamiento de información: Para usar una **caja negra**, solo necesitas conocer su **responsabilidad** y sus **interfaces** de entrada y salida.




Las **cajas negras** respetan el principio de ocultamiento de información: Para usar una **caja negra**, solo necesitas conocer su **responsabilidad** y sus **interfaces** de entrada y salida. Detalles adicionales de su funcionamiento interno (usualmente) no son requeridos.

Este ocultamiento proporciona una serie de ventajas:

* Puedes cambiar o modificar el funcionamiento interno, sin que los usuarios (clientes, consumidores) necesiten adaptarse a esos cambios.
* Podrías abstenerte de documentar la **caja blanca** de este **bloque de construcción**. Eso puede reducir el esfuerzo de mantenimiento de tu documentación.
* Eventualmente reduces el nivel de detalles que algunos stakeholders tienen que considerar o conocer.

En casos extremos, restringes la **vista de bloques de construcción** al nivel 1 (ver tip 5-3, 'el nivel 1 es tu amigo'), la **caja blanca** del sistema general - sin detallar ninguno de los **bloques de construcción** de nivel superior.

Información A Veces Requerida
=============================

Según la "teoría de cajas negras", conocer la **responsabilidad** e **interfaz** de tal **caja negra** es suficiente. Pero en realidad, a veces se requieren propiedades adicionales de tal **bloque de construcción** - por ejemplo, propiedades de tiempo de ejecución o **despliegue** u otros tipos de cualidades.

Ejemplo: Función Raíz Cuadrada
==============================

Consideremos una **caja negra** simple - la función raíz cuadrada (abreviado "sqrt") tiene una **interfaz** ("API") muy simple:

.. code-block:: text

   sqrt( número ) -> número

donde número > 0.

Para una **caja negra** sqrt, las siguientes propiedades adicionales podrían ser importantes:

* ¿Qué precisión proporciona nuestra **caja negra** sqrt, cuántos dígitos entregará? ("Corrección")
* ¿Todos los usuarios están permitidos para usar sqrt, o está nuestro sqrt restringido a usuarios específicos? ("Autorización")
* ¿Puede nuestra función sqrt ser llamada por muchos usuarios paralelos? ("Paralelismo, capacidad multi-usuario")
* ¿El uso de nuestra función sqrt costará dinero?
* ¿Qué tan rápido entregará nuestra función sus resultados? ("Eficiencia de rendimiento")

De los ejemplos ves que varias "Cualidades" podrían ser relevantes para tus **cajas negras**.




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_3` - Nivel 1 es tu amigo
   * :ref:`bloques_tip_5` - Responsabilidad de cajas negras




:Tip: 5-6
:Tema: Ocultamiento de información
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
