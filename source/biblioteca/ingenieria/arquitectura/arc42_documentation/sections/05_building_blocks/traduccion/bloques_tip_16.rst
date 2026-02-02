.. _bloques_tip_16:




Tip 5-16: ¡Mapea bloques de construcción según los constructos de modularización de tu lenguaje de programación!
================================================================================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   En caso de que apliques los constructos de modularización de tu lenguaje de programación al diseñar **bloques de construcción**, obtendrás el mapeo óptimo de código fuente a la arquitectura.




En caso de que apliques los constructos de modularización de tu lenguaje de programación al diseñar o especificar **bloques de construcción** de arquitectura, obtendrás el mapeo óptimo de código fuente a la arquitectura.

Para desarrollo de sistemas Java, por ejemplo, los **bloques de construcción** de arquitectura (es decir, **cajas negras** del nivel 1) deben corresponder a paquetes Java.

Cuándo Desviarse de Esta Regla
==============================

* En sistemas crecidos *históricamente* puede ser útil desviarse de esta regla si el código está (aparentemente) desorganizado...
* Si usas varios lenguajes de programación para implementar **bloques de construcción** de otra manera cohesivos (es decir, implementas partes del **bloque de construcción** en Java, otras partes en JavaScript, incluso otras partes en Python)
* Si algunos de tus frameworks/librerías o incluso productos usados imponen *otra* estructuración de código... entonces debes cumplir con las sugerencias de tus herramientas ("no pelees con la plataforma"), pero sin embargo crea **bloques de construcción** arquitectónicos significativos.
* Si lo ubicado en el paquete/namespace/**módulo** no es cohesivo (ver tip 5-17, cohesión es rey)




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_17` - Cohesión




:Tip: 5-16
:Tema: Mapeo según constructos de lenguaje
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
