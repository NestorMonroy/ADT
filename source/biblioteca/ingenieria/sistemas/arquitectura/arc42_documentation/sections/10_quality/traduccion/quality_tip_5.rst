.. _quality_tip_5:

===============================================================
Tip 10-5: ¡Considera escenarios de uso o aplicación (calidad)!
===============================================================

:Tema: Escenarios de uso (usage scenarios)
:Palabras clave: quality, quality-scenario, scenario

----

Muchos **escenarios de calidad** estarán relacionados con el uso del sistema (**escenarios de aplicación**, **escenarios de caso de uso**).

Algunos autores llaman a esto *"calidad externamente visible"*.

Esto está relacionado con objetivos de alto nivel como:

* **Funcionalidad**
* **Velocidad de procesamiento**
* **Corrección** de cálculos o procesamiento
* **Robustez** concerniente a entrada de datos erróneos
* **Seguridad** de datos o confidencialidad

Los **escenarios de aplicación** describen cómo el sistema debe comportarse cuando es usado por humanos o vía interfaces arbitrarias.

Ejemplos
========

**Ejemplo 1: Rendimiento de UI**

 La ejecución de la función/caso de uso XYZ en la interfaz gráfica toma menos de un segundo.

**Ejemplo 2: Tiempo de respuesta post-login**

 Menos de 2 segundos después de un login exitoso, los usuarios ven desplegada una lista de todas las reservas de la última semana.

**Ejemplo 3: Usabilidad administrativa**

 Los administradores pueden modificar los derechos de acceso de usuarios vía GUI con un máximo de cinco clics.

----

**Características de Buenos Usage Scenarios:**

.. list-table::
 :header-rows: 1
 :widths: 30 70

 * - Característica
   - Descripción
 * - **Específico**
   - Identifica función/caso de uso exacto
 * - **Medible**
   - Incluye métrica clara (tiempo, clicks, etc.)
 * - **Realista**
   - Basado en uso real esperado
 * - **Relevante**
   - Importante para stakeholders
 * - **Verificable**
   - Puede ser probado/validado

**Categorías Comunes:**

* [TARGET] **Performance/Velocidad**: Tiempo de respuesta, throughput
* [OK] **Corrección**: Precisión de cálculos, validaciones
* **Seguridad**: Autenticación, autorización, encriptación
* **Robustez**: Manejo de datos inválidos/erróneos
* USER: **Usabilidad**: Facilidad de uso, número de clics
* [TABLE] **Funcionalidad**: Capacidades del sistema

----

.. seealso::
 * **Tip 10-6** - Escenarios de cambio
 * **Tip 10-7** - Escenarios de fallo/error
 * **Sección 10.2** - Escenarios de Calidad
