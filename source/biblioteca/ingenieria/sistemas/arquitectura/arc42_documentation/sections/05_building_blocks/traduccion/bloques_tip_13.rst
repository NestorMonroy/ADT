.. _bloques_tip_13:

===============================================================
Tip 5-13: ¡Explica el mapeo de código fuente a bloques de construcción!
===============================================================

.. tip::
   **Consejo de Bloques de Construcción arc42**
   
   El mapeo entre código fuente y **bloques de construcción** debe ser explícito y bien razonado.

----

En algunos casos (ideales), la estructura de **bloques de construcción** mapea exactamente a la estructura de archivos, paquetes o módulos del código fuente. Pero tristemente eso no siempre es cierto.

Considera el siguiente diagrama: En el centro encuentras un extracto de un sistema de archivos, conteniendo varios archivos ``.java`` y ``.php``. A la izquierda y derecha de este listado de directorio hipotético encuentras dos alternativas de cómo mapear estas fuentes a **bloques de construcción** arquitectónicos:

* ``A_1`` consiste de x.java y y.java, ``A_2`` de z.java y algunos archivos php, ``A_3`` de g.java y h.java.
* ``B_1`` de x.java, y.java y z.java, ``B_2`` de todo el resto

.. figure:: ../figuras/05-mapping-code-to-blocks.png
   :alt: Diagrama de mapeo de código a bloques
   :align: center
   :width: 85%
   
   Alternativas de mapeo de código fuente a bloques de construcción

Puede haber buenas razones para ambas versiones. Para tu sistema, debes tener razones específicas de por qué ciertos **bloques de construcción** contienen qué código fuente.

El Mapeo de Bloques de Construcción a Código es una Decisión Específica
========================================================================

Aunque el mapeo de código a **bloques de construcción** *debería* estar alineado con estructuras del sistema de archivos, puede haber casos donde es completamente diferente - algunos ejemplos:

* Alguien ha puesto accidentalmente demasiados archivos en el mismo directorio
* Varios lenguajes de programación están mezclados en el mismo árbol de fuentes
* La **responsabilidad** de **bloques de construcción** ha cambiado con el tiempo, pero los archivos de código fuente correspondientes no se han movido apropiadamente
* Otras restricciones imponen una estructura de directorio específica, por ejemplo, algunos frameworks oscuros requieren ciertos archivos fuente en ubicaciones específicas, o el proceso de construcción/despliegue espera ciertas estructuras de directorio, que no mapean a **bloques de construcción** arquitectónicos.

Mantén el Mapeo de Código y Bloques de Construcción Directo
============================================================

Intenta mantener ese mapeo simple y directo. Mapeos complejos, como la versión izquierda en el diagrama arriba, deben evitarse.

En casos ideales, los directorios en el sistema de archivos son idénticos a **bloques de construcción**. Las **cajas negras** contenidas son entonces archivos contenidos en subdirectorios...

Ver También
===========

* Tip 5-14 (dónde está el código fuente)
* Tip 5-15 (mapear bloques a directorios)
* Tip 5-16 (usar constructos de modularización de lenguajes de programación)

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_14` - Ubicación del código
   * :ref:`bloques_tip_15` - Mapeo a directorios

----

:Tip: 5-13
:Tema: Mapeo código-bloques
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
