.. _estrategia_ejemplo_2:

===============================================================
Ejemplo de Estrategia de Solución: MaMa
===============================================================

.. note::
   **Ejemplo arc42**
   
   Necesitas un resumen breve y explicación de las ideas y estrategias de solución fundamentales. Estas ideas clave deben ser familiares para todos los involucrados en el desarrollo y la arquitectura.
   
   Explica brevemente cómo logras los requisitos de calidad más importantes.

----

4. Estrategia de Solución

==========================

Por favor nota:

* En la *vida real* incluirías enlaces a descripciones detalladas - eso se omite en este ejemplo.
* En este ejemplo, los enfoques están centrados alrededor de requisitos específicos. Eso no es necesario - ciertos **enfoques estratégicos** en tu sistema podrían ser bastante generales y no relacionados a requisitos específicos.

.. list-table:: Estrategia de Solución MaMa
   :header-rows: 1
   :widths: 30 40 30
   
   * - **Meta/Requisito**
     - **Enfoque Arquitectónico**
     - **Detalles**
   * - Estructura de Datos Flexible
     - Estructura de base de datos + código de persistencia se genera completamente (100%) desde modelo UML
     - 
   * - Flexibilidad en Formatos de Transmisión (CSV y formatos de registro fijo)
     - Crear lenguajes específicos de dominio para configuraciones de importación/exportación CSV y formato fijo. Construir un parser basado en ANTLR para estos lenguajes más los intérpretes correspondientes.
     - Sección 8.2
   * - Flexibilidad (Formatos CSV/fijo configurables)
     - Implementar editor personalizado para DSL CSV/fijo como plugin de Eclipse
     - Sección 8.2
   * - Performance (importar/procesar 250k imágenes/24hrs)
     - Tratar imágenes como caso especial, almacenar imágenes en filesystem en lugar de base de datos, crear ruta/nombre de archivo único basado en ID de cliente, incluir pruebas de carga en build automático, crear generador de datos de prueba
     - Incluir caso especial para persistencia de imágenes en generador de código, Sección 8.1

----

Análisis
========

Este ejemplo muestra una **estrategia de solución** más compleja que:

* Relaciona cada **enfoque de solución** con **metas de calidad** específicas
* Proporciona detalles técnicos concretos de implementación
* Referencia secciones detalladas del documento (Sección 8)
* Aborda requisitos no funcionales (performance, flexibilidad)

La tabla facilita la trazabilidad entre requisitos y **decisiones arquitectónicas**.

Puntos Clave
============

**Generación de Código:** El 100% del código de persistencia se genera desde el modelo UML, una decisión fundamental que impacta todo el desarrollo.

**DSL Específicos de Dominio:** Uso de lenguajes específicos de dominio (DSL) con ANTLR para configuración, mostrando un enfoque sofisticado para flexibilidad.

**Optimización de Performance:** Decisiones específicas para lograr throughput requerido (250k imágenes/24hrs), como almacenamiento en filesystem.

----

.. seealso::
   * :ref:`seccion_04` - Estrategia de Solución
   * :ref:`estrategia_ejemplo_1` - Ejemplo HTML Sanity Checker

----

:Sistema: MaMa
:Tipo: Ejemplo de estrategia de solución (tabla)
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
