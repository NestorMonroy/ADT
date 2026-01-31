.. _bloques_tip_8:




Tip 5-8: ¡Justifica cada estructura de caja blanca!
===================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Cada estructura de **caja blanca** es la **descomposición** de una **caja negra** en partes más pequeñas (llamamos a esas *cajas negras contenidas*) más sus **dependencias** o relaciones mutuas.




Cada estructura de **caja blanca** es la **descomposición** de una **caja negra** en partes más pequeñas (llamamos a esas *cajas negras contenidas*) más sus **dependencias** o relaciones mutuas.

En **cada** **caja blanca** debes explicar brevemente las razones para la **descomposición** o estructura específica:

* ¿Por qué esta **caja blanca** consiste de cinco **cajas negras**?
* ¿Por qué la **caja negra** contenida A habla con B?

Esta información a veces se llama *razonamiento de diseño* para esta **caja blanca** específica.

Ejemplos de Razonamiento
========================

**Buenas justificaciones:**

* "Separamos la lógica de negocio de la presentación para facilitar pruebas independientes"
* "Usamos este patrón de arquitectura en capas para aislar cambios en la base de datos"
* "El componente A se comunica con B para sincronizar datos de usuario en tiempo real"

**Justificaciones insuficientes:**

* "Porque sí"
* "Es obvio"
* (Sin justificación)




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Plantilla de caja blanca




:Tip: 5-8
:Tema: Razonamiento de diseño
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
