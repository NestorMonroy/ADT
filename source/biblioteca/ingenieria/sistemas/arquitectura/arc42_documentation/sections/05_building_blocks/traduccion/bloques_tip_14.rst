.. _bloques_tip_14:

===============================================================
Tip 5-14: ¡Explica dónde encontrar el código fuente de tus bloques de construcción!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   En caso de que tu mapeo de código fuente a **bloques de construcción** no sea trivial, tu documentación arc42 debe declarar explícitamente dónde encontrar las fuentes.

----

En caso de que tu mapeo de código fuente a **bloques de construcción** no sea trivial, tu documentación arc42 debe declarar explícitamente dónde encontrar las fuentes.

* En caso de que te ciñas al Tip 5-15 (**bloques de construcción** alineados con estructura de directorio), solo necesitas documentar o especificar el directorio raíz de tu repositorio de código fuente. Detalles adicionales resultarán de este directorio raíz.
* En caso de que tu código fuente sea administrado en diferentes repositorios (por ejemplo, diferentes repositorios git o subversion), debes agregar un enlace a estos repositorios en los **bloques de construcción** del nivel 1.
* En caso de que tu código fuente esté distribuido sobre varios directorios, podrías documentar la ubicación de tus 2-3 artefactos de fuente más importantes por **bloque de construcción**.

.. important::
   NUNCA caigas en la trampa de listar **todos** los artefactos de código para cualquier **caja blanca**, ya que esa información es tan volátil...

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_15` - Alineación con directorios

----

:Tip: 5-14
:Tema: Ubicación del código fuente
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
