.. _estrategia_ejemplo_1:

===============================================================
Ejemplo de Estrategia de Solución: HTML Sanity Checker
===============================================================

.. note::
   **Ejemplo arc42**
   
   Necesitas un resumen breve y explicación de las ideas y estrategias de solución fundamentales. Estas ideas clave deben ser familiares para todos los involucrados en el desarrollo y la arquitectura.
   
   Explica brevemente cómo logras los requisitos de calidad más importantes.

----

4. Estrategia de Solución
==========================

1. Implementar HtmlSC principalmente en el lenguaje de programación Groovy y parcialmente en Java con dependencias externas mínimas.

2. Envolvemos esta implementación en un plugin de Gradle, para que pueda usarse dentro de builds automatizados. Los detalles se dan en la `Guía de usuario de Gradle <https://docs.gradle.org/current/userguide/userguide.html>`_.
   (El plugin de Maven aún está en desarrollo).

3. Aplicar el *patrón template-method* para habilitar:

   * Múltiples algoritmos de verificación
   * Salida tanto HTML (archivo) como texto (consola)

4. Confiar en las convenciones estándar de Gradle y Groovy para la configuración, teniendo un solo archivo de configuración.

   * Para el plugin de Maven, esto podría llevar a problemas.

----

Análisis
========

Este ejemplo muestra cómo una **estrategia de solución** simple y concisa puede:

* Describir decisiones tecnológicas clave (Groovy/Java)
* Explicar **patrones de diseño** fundamentales (template-method)
* Mencionar decisiones de integración (plugin de Gradle)
* Identificar **restricciones** potenciales (problemas con Maven)

La estrategia es breve pero suficientemente detallada para guiar decisiones de implementación posteriores.

----

.. seealso::
   * :ref:`seccion_04` - Estrategia de Solución
   * :ref:`estrategia_ejemplo_2` - Ejemplo MaMa

----

:Sistema: HTML Sanity Checker
:Tipo: Ejemplo de estrategia de solución
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
