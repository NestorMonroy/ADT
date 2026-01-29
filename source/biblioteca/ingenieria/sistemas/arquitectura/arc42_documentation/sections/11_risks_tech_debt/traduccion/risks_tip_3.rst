.. _risks_tip_3:

===============================================================
Tip 11-3: ¡Identifica problemas o riesgos por evaluación cualitativa!
===============================================================

:Tema: Evaluación cualitativa de riesgos
:Palabras clave: risk, technical-debt, problem, atam

----

Algunos problemas y **riesgos** pueden ser identificados comparando sistemáticamente los **requisitos** (de calidad) con los enfoques de arquitectura e implementación.

Método de Evaluación
=====================

**Proceso de Comparación Sistemática:**

1. **Identificar requisitos de calidad**

 * Extraer de Sección 1.2 (Objetivos de Calidad)
 * Extraer de Sección 10 (Requisitos de Calidad detallados)

2. **Documentar enfoques arquitectónicos**

 * De Sección 4 (Vista de Solución)
 * De Sección 8 (Conceptos Transversales)
 * De Sección 9 (Decisiones de Arquitectura)

3. **Comparar sistemáticamente**

 * ¿El enfoque arquitectónico soporta el requisito?
 * ¿Hay gaps o contradicciones?
 * ¿Qué podría fallar?

4. **Identificar riesgos y problemas**

 * Requisitos no soportados -> RIESGO
 * Enfoques conflictivos -> PROBLEMA
 * Suposiciones no validadas -> RIESGO

----

**Ejemplo de Evaluación Cualitativa:**

.. list-table:: Evaluación Requisito vs Enfoque
 :header-rows: 1
 :widths: 20 25 25 30

 * - **Requisito**
 - **Enfoque Actual**
 - **Análisis**
 - **Riesgo Identificado**
 * - Performance: <100ms respuesta
 - Llamadas síncronas a DB
 - DB en región diferente = latencia 50-150ms
 - [WARNING] RIESGO: No cumplir SLA bajo carga
 * - Disponibilidad: 99.9%
 - Servidor único
 - Sin redundancia
 - PROBLEMA: Single point of failure
 * - Seguridad: Encriptación end-to-end
 - HTTPS en tránsito
 - Datos en reposo sin encriptar
 - [WARNING] GAP: Falta encriptación at-rest
 * - Escalabilidad: 10x usuarios
 - Arquitectura monolítica
 - Escalar = escalar todo
 - [WARNING] RIESGO: Costos altos de infraestructura

----

**Herramienta de Análisis: Matriz de Evaluación**

.. code-block:: text

 Requisito de Calidad: Performance (<200ms p95)
 +---------------------------------------------+
 | Enfoque Arquitectónico |
 +---------------------------------------------+
 | [OK] Cache en Redis (reduce DB queries) |
 | [OK] CDN para assets estáticos |
 | [WARNING] Base de datos sin índices optimizados |
 | [ERROR] Queries N+1 en múltiples endpoints |
 +---------------------------------------------+

 Análisis:
 +- Fortalezas: Cache + CDN dan buen baseline
 +- Debilidades: Queries ineficientes
 +- Riesgo: Bajo carga alta, cache misses = degradación

 Mitigación Propuesta:
 1. Agregar índices a queries frecuentes (2 días)
 2. Refactorizar queries N+1 (1 semana)
 3. Implementar query monitoring (3 días)

----

**Método ATAM Simplificado:**

El **Architecture Tradeoff Analysis Method (ATAM)** es un método formal para este tipo de evaluación:

**Pasos ATAM:**

1. **Presentar arquitectura** a stakeholders
2. **Identificar decisiones arquitectónicas** clave
3. **Generar escenarios de calidad** (ver Sección 10.2)
4. **Analizar cada decisión** contra escenarios
5. **Identificar trade-offs**, **sensibilidades** y **riesgos**
6. **Documentar hallazgos**

**Términos ATAM:**

* **Trade-off**: Decisión que beneficia un atributo pero perjudica otro

 *Ejemplo: Microservicios -> mejor escalabilidad, peor latencia*

* **Sensitivity**: Parámetro crítico que afecta significativamente un atributo

 *Ejemplo: Tamaño de pool de conexiones DB -> afecta throughput*

* **Risk**: Decisión que amenaza un requisito de calidad

 *Ejemplo: Sin replicación -> amenaza disponibilidad*

----

**Plantilla de Análisis Cualitativo:**

.. list-table::
 :header-rows: 1
 :widths: 15 20 20 15 15 15

 * - **Requisito**
 - **Enfoque**
 - **Trade-off**
 - **Sensitivity**
 - **Riesgo**
 - **Acción**
 * - *<Req>*
 - *<Enfoque arquitectónico>*
 - *<Qué se sacrifica>*
 - *<Parámetros críticos>*
 - *<Nivel de riesgo>*
 - *<Mitigación propuesta>*

----

**Beneficios de Evaluación Cualitativa:**

* [OK] **Detección temprana**: Riesgos identificados en diseño, no en producción
* [OK] **Objetividad**: Análisis sistemático vs intuición
* [OK] **Trazabilidad**: Requisito -> Enfoque -> Riesgo
* [OK] **Priorización**: Riesgos clasificados por impacto
* [OK] **Comunicación**: Evidencia clara para stakeholders

----

Ver También
===========

* **Tip 10-8** - `Usar escenarios de calidad para evaluación </tips/10-8>`_
* **Sección 10.2** - Escenarios de Calidad
* **Método ATAM** - https://www.sei.cmu.edu/architecture/tools/evaluate/atam.cfm

----

.. seealso::
 * **Tip 11-1** - Buscar riesgos con diferentes stakeholders
 * **Tip 11-2** - Analizar interfaces para riesgos
 * **Sección 4** - Vista de Solución
 * **Sección 9** - Decisiones de Arquitectura
