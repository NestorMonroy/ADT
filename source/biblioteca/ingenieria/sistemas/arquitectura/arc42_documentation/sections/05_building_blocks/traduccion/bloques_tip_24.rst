.. _bloques_tip_24:




Tip 5-24: ¡Usa el nivel 1 de bloques de construcción para información **adicional**!
====================================================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Puedes complementar el alto nivel de abstracción del nivel 1 de **bloques de construcción** con información adicional.




Puedes complementar el alto nivel de abstracción del nivel 1 de **bloques de construcción** con información adicional, como:

* Lenguajes de programación usados en el **bloque de construcción** específico
* Información de control de versiones (es decir, qué sistema vc se usa)
* Información organizacional (configuración del equipo, estado de completación o planificación)

Puedes usar color, sombreado, agrupamiento u otros medios gráficos, o denotar tales asuntos vía estereotipos.

En caso de que hagas eso, por favor explica estos tipos de información en una leyenda o explicación textual.

Ver el siguiente ejemplo:

.. .. figure:: ../figuras/05-whitebox-with-other-info.png
..       :alt: Caja blanca con leyenda
..       :align: center
..       :width: 65%
   
..       Caja blanca con información adicional explicada en leyenda

Piensa Dos Veces Antes de Agregar Información
=============================================

Puedes extender este tip a capas adicionales de la **vista de bloques de construcción**. Pero mantén en mente la regla fundamental de documentación económica: La información *adicional* podría ser relevante solo por un breve período de tiempo - así que mejor podrías abstenerte de incluirla en la documentación.

Eventualmente esta información "adicional" es interesante solo por corto tiempo - así que en la duda mejor déjala fuera.

Ejemplos de Información Adicional
=================================

**Útil incluir:**

* Tecnologías críticas o poco comunes
* Decisiones arquitectónicas importantes
* Restricciones permanentes

**Mejor evitar:**

* Nombres de desarrolladores individuales (cambian frecuentemente)
* Estado temporal de desarrollo
* Información que se vuelve obsoleta rápidamente




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Nivel 1




:Tip: 5-24
:Tema: Información adicional en nivel 1
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
