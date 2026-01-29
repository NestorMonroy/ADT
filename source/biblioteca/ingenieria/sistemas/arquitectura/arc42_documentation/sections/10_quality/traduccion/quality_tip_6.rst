.. _quality_tip_6:

===============================================================
Tip 10-6: ¡¡Considera escenarios de cambio (calidad)!!
===============================================================

:Tema: Escenarios de cambio (change scenarios)
:Palabras clave: quality, quality-scenario, scenario

----

Aparte de los **escenarios de uso o aplicación** (ver :ref:`tip 10-5 <quality_tip_5>`), deberías considerar cambios o modificaciones para **requisitos de calidad**.

Esto cubre solicitudes de cambio arbitrarias, como:

* Adiciones o modificaciones de **requisitos funcionales** (es decir, reglas de cálculo o validación modificadas)
* Adaptación a **requisitos de calidad** modificados (es decir, requisitos de **rendimiento** o **throughput** mejorados)
* Reacción a cambios en **acuerdos de nivel de servicio** (service-level agreements)

Tales **escenarios de cambio** cubren los importantes **objetivos de calidad** de:

* **Mantenibilidad** (maintainability)
* **Modificabilidad** (modifiability)
* **Cambiabilidad** (changeability)
* **Flexibilidad** (flexibility)

Ejemplos
========

**Ejemplo 1: Integración de proveedor externo**

 La integración de un nuevo proveedor de pagos (externo) es posible dentro de un máximo de dos persona-semanas.

**Ejemplo 2: Adaptación a requisitos legales**

 El formato de datos del reporte de reservas anual puede adaptarse a los requisitos estatutarios (legales) dentro de 80 persona-horas.

**Ejemplo 3: Flexibilidad de base de datos**

 El sistema debe ser usable con los sistemas de base de datos DB2, Oracle y MySQL sin modificaciones al código fuente.

----

**Tipos de Change Scenarios:**

.. list-table::
 :header-rows: 1
 :widths: 30 40 30

 * - Tipo de Cambio
   - Descripción
 - Métrica Típica
 * - **Funcional**
   - Nuevas features, reglas modificadas
 - Persona-horas/días
 * - **Calidad**
   - Performance mejorado, disponibilidad
 - Esfuerzo de adaptación
 * - **Tecnológico**
   - Nueva DB, framework, librería
 - Tiempo sin downtime
 * - **Regulatorio**
   - Cumplimiento legal, GDPR, etc.
 - Deadline compliance
 * - **Integración**
   - Nuevos servicios externos
 - Tiempo de integración

**Estructura Recomendada para Change Scenarios:**

1. **Tipo de cambio**: ¿Qué categoría? (funcional, tecnológico, etc.)
2. **Descripción del cambio**: ¿Qué debe cambiar exactamente?
3. **Esfuerzo máximo**: Persona-horas/días/semanas
4. **Restricciones**: Sin downtime, sin cambios de código, etc.
5. **Criterio de éxito**: ¿Cómo se valida?

----

**Beneficios de Documentar Change Scenarios:**

* [OK] **Diseño anticipado** para cambios futuros predecibles
* [OK] **Estimación** de costos de mantenimiento
* [OK] **Identificación** de áreas rígidas vs flexibles
* [OK] **Justificación** de decisiones arquitectónicas
* [OK] **Comunicación** clara con stakeholders de negocio

----

.. seealso::
 * **Tip 10-5** - Escenarios de uso/aplicación
 * **Tip 10-7** - Escenarios de fallo/error
 * **Sección 9** - Decisiones de Arquitectura (justificación de flexibilidad)
 * **Sección 11** - Riesgos y Deuda Técnica (cambios costosos)
