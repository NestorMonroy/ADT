.. _quality_ejemplo_tpu_1:

===============================================================
Ejemplo de Escenarios de Calidad: TrafficPursuitUnit
===============================================================

:Sistema: TrafficPursuitUnit (TPU)
:Categoría: Sistema de persecución de tráfico policial
:Palabras clave: quality, example

----

Este ejemplo muestra **requisitos de calidad** completos para TrafficPursuitUnit (TPU), incluyendo un **quality tree** detallado y **escenarios de calidad** específicos.

----

10. Requisitos de Calidad
==========================

10.1 Quality Tree
=================

.. note::
 Los números (1), (2), (3) en la siguiente tabla repiten los **requisitos de calidad** de nivel superior del capítulo 1.2.

Quality Tree Completo
---------------------

.. list-table:: Quality Tree - TrafficPursuitUnit
 :header-rows: 1
 :widths: 20 20 35 10

 * - **Categoría de Calidad**
   - **Calidad**
   - **Descripción**
   - **Escenario**
 * - **Usability (Usabilidad)**
   - Ease of Use (3)
   - Facilidad de uso por el policía, especialmente en el caso de uso de perseguir otro coche
 -
 * -
   - Ease of Learning
   - Las funciones estándar deben ser tan fáciles e intuitivas de usar como sea posible sin necesidad de instrucción previa prolongada
   - SC1
 * - **Performance (Rendimiento)**
   - Accuracy (1)
   - Las mediciones y cálculos deben ser correctos y precisos dentro del rango de desviación especificado
 -
 * -
   - Comprehensiveness
   - Los algoritmos usados deben ser tan legalmente herméticos como sea posible y comprensibles
 -
 * -
   - Precision & Accuracy
   - Si es posible, las inserciones de video deben hacerse con la granularidad de un frame de video
 -
 * -
   - Robustness (2)
   - El sistema debe trabajar de manera confiable bajo todas las condiciones de entorno y operación especificadas
 -
 * - **Operational & Environmental**
   - Temperature Range
   - El rango de temperatura en el cual se asegura el funcionamiento correcto del dispositivo debe estar entre -25 grados y +85 grados
   - SC3
 * - **Maintainability & Support**
   - Maintenance & Repair
   - Debe ser posible reemplazar componentes fuera de la caja de medición sin afectar la medición correcta dentro de la caja de medición
 -
 * - **Security (Seguridad)**
   - Integrity
   - La verificabilidad de la autenticidad de los archivos de video debe estar asegurada con un código de verificación
 -
 * - **Cultural and Regional**
   - Multilanguage
   - Los textos de la interfaz de usuario deben poder convertirse mediante un archivo de traducción a diferentes idiomas con conjunto de caracteres ASCII
   - SC4
 * -
   - Local Time Adaptability
   - La diferencia de tiempo con Greenwich debe ser ajustable con una granularidad de 1 minuto
 -
 * -
   - Local Legal Rules Adaptability
   - El procedimiento de medición debe ser adaptable a la legislación regional
 -
 * - **Legal (Legal)**
   - Legal Compliance
   - Implementación y aplicación correcta de todos los requisitos legales en la evaluación para los diferentes tipos de persecuciones
   - SC2

----

10.2 Escenarios de Calidad
===========================

.. list-table:: Escenarios de Calidad Detallados
 :header-rows: 1
 :widths: 10 90

 * - **ID**
   - **Escenario**
 * - **SC1**
   - Un usuario que no conoce el sistema puede operarlo después de 10 minutos de instrucción.
 * - **SC2**
   - Al reproducir un video frame por frame posteriormente, cada frame contiene exactamente la información esperada.
 * - **SC3**
   - Incluso bajo temperatura máxima y mínima (por ejemplo, en una cámara climática), el dispositivo siempre produce la misma velocidad a frecuencia de pulso constante.
 * - **SC4**
   - Con archivos de traducción apropiados reemplazando el idioma predeterminado (inglés), todos los textos mostrados e impresos ahora aparecen en este idioma.

----

Análisis del Quality Tree
==========================

**Distribución de Requisitos por Categoría:**

.. list-table::
 :header-rows: 1
 :widths: 35 20 20 25

 * - **Categoría ISO 25010**
   - **# Requisitos**
   - **# Escenarios**
   - **Prioridad**
 * - Usability
   - 2
   - 1 (SC1)
   - Alta (3)
 * - Performance
   - 4
   - 1 (SC2, SC3)
   - Crítica (1, 2)
 * - Operational
   - 1
   - 1 (SC3)
   - Alta
 * - Maintainability
   - 1
   - 0
   - Media
 * - Security
   - 1
   - 0
   - Alta
 * - Cultural/Regional
   - 3
   - 1 (SC4)
   - Media
 * - Legal
   - 1
   - 1 (SC2)
   - Crítica

**Observaciones:**

1. **Énfasis en Performance**

 * 4 requisitos relacionados con **precisión** y **robustez**
 * Crítico para un sistema de medición legal

2. **Adaptabilidad Regional**

 * 3 requisitos sobre multi-idioma y legislación local
 * Importante para producto internacional

3. **Gaps Identificados**

 * Maintainability: Sin escenarios específicos
 * Security: Sin escenarios de verificación de integridad

----

**Lecciones Aprendidas:**

[OK] **Buenas Prácticas:**

* Vinculación clara entre objetivos (1.2) y quality tree (10.1)
* Escenarios medibles y específicos
* Cobertura de aspectos legales y regionales

[WARNING] **Áreas de Mejora:**

* Algunos requisitos de calidad sin escenarios asociados
* Podría beneficiarse de más escenarios de **mantenibilidad**
* Falta métrica de tiempo para SC2 (frame-by-frame)

**Aplicabilidad:**

Este ejemplo es particularmente útil para:

* Sistemas **embebidos** con restricciones ambientales
* Sistemas con requisitos **legales** estrictos
* Productos **internacionales** multi-idioma
* Sistemas de **medición** de alta precisión

----

.. seealso::
 * **Ejemplo HTMLSC-2** - Escenarios más simples y directos
 * **Tip 10-4** - Usar quality tree como checklist
 * **Tip 10-8** - Evaluación de arquitectura con escenarios
 * **ISO 25010:2023** - Estándar de calidad de software
