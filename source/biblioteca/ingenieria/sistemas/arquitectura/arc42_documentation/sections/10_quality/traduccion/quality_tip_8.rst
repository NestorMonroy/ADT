.. _quality_tip_8:

===============================================================
Tip 10-8: ¡Usa escenarios (de calidad) para análisis o evaluación de arquitectura!
===============================================================

:Tema: Evaluación de arquitectura con escenarios
:Palabras clave: quality, quality-scenario, scenario, atam

----

Usa **escenarios de calidad** para analizar o evaluar sistemáticamente tu arquitectura, similar al `método ATAM <https://www.sei.cmu.edu/architecture/tools/evaluate/atam.cfm>`_.

Una tabla como la siguiente (similar a la estructura propuesta en :ref:`tip 4-2 (enfoque de solución como tabla) <solution_tip_2>`) puede soportar evaluación cualitativa.

Tabla de Evaluación
===================

.. list-table:: Evaluación de Escenarios de Calidad
   :header-rows: 1
   :widths: 20 25 30 25
   
   * - **Objetivo de Calidad**
     - **Escenario**
     - **Enfoque de Solución**
     - **Riesgo**
   * - *<Q-goal 1>*
     - *<Texto>*
     - *<Texto>*
     - *<risk-1>*
   * - *<Q-goal 2>*
     - *<Texto>*
     - *<Texto>*
     - *<risk-2>*

----

**Método de Evaluación Paso a Paso:**

1. **Identificar escenarios críticos**
   
   * Selecciona los 5-10 **escenarios de calidad** más importantes
   * Prioriza por riesgo de negocio e impacto técnico

2. **Documentar enfoque de solución actual**
   
   * ¿Cómo la arquitectura actual aborda cada escenario?
   * ¿Qué patrones/tecnologías/decisiones se usan?

3. **Identificar riesgos**
   
   * ¿Qué podría fallar?
   * ¿Qué suposiciones son críticas?
   * ¿Qué no está probado/validado?

4. **Evaluar completitud**
   
   * ¿Todos los escenarios importantes tienen solución?
   * ¿Hay escenarios en conflicto?
   * ¿Hay gaps en la arquitectura?

Ejemplo Completo
================

.. list-table:: Ejemplo de Evaluación - Sistema de e-Commerce
   :header-rows: 1
   :widths: 20 25 30 25
   
   * - **Objetivo de Calidad**
     - **Escenario**
     - **Enfoque de Solución**
     - **Riesgo**
   * - **Performance**
     - Búsqueda de productos <200ms para 95% de requests
     - ElasticSearch con cache Redis, CDN para imágenes
     - Alta: Tamaño del índice crece 10x anualmente
   * - **Escalabilidad**
     - Soportar 10,000 usuarios concurrentes durante Black Friday
     - Kubernetes auto-scaling, load balancer, DB read replicas
     - Medio: Costos de cloud pueden ser muy altos
   * - **Seguridad**
     - Proteger datos de tarjetas de crédito (PCI DSS)
     - Tokenización con Stripe, sin almacenar datos de tarjeta
     - Bajo: Dependencia de proveedor externo
   * - **Disponibilidad**
     - 99.9% uptime (8h downtime/año)
     - Multi-region deployment, health checks, automated failover
     - Medio: Complejidad de sincronización entre regiones
   * - **Mantenibilidad**
     - Desplegar nuevo feature en <2h
     - CI/CD pipeline, feature flags, blue-green deployment
     - Bajo: Requiere disciplina de equipo

----

**Método ATAM (Architecture Tradeoff Analysis Method)**

El método ATAM del SEI usa **escenarios de calidad** como mecanismo central:

**Fases del ATAM:**

1. **Presentación** del negocio y arquitectura
2. **Investigación** de enfoques arquitectónicos
3. **Generación** de escenarios de calidad
4. **Análisis** de enfoques vs escenarios
5. **Brainstorming** y priorización de escenarios
6. **Análisis** de enfoques vs escenarios priorizados
7. **Presentación** de resultados

**Beneficios:**

* ✅ Identificación temprana de **riesgos** arquitectónicos
* ✅ Evaluación de **trade-offs** entre objetivos de calidad
* ✅ Validación de **decisiones arquitectónicas**
* ✅ Consenso entre **stakeholders**

----

**Template de Análisis Detallado:**

Para análisis más profundo, considera agregar estas columnas:

.. list-table:: Template Extendido
   :header-rows: 1
   :widths: 15 20 20 15 15 15
   
   * - **Q-Goal**
     - **Escenario**
     - **Solución**
     - **Riesgo**
     - **Trade-off**
     - **Sensibilidad**
   * - Performance
     - <200ms búsqueda
     - Cache + índice
     - Sincronización
     - Consistencia eventual
     - Alta: +10% carga = fallo

**Columnas adicionales explicadas:**

* **Trade-off**: ¿Qué se sacrifica para lograr este objetivo?
* **Sensibilidad**: ¿Qué tan sensible es a cambios en parámetros/carga?

----

**Resultado del Análisis:**

Al completar esta evaluación, deberías poder:

1. **Identificar riesgos** arquitectónicos claros
2. **Priorizar** esfuerzos de mitigación
3. **Comunicar** trade-offs a stakeholders
4. **Justificar** decisiones arquitectónicas
5. **Planificar** iteraciones futuras de arquitectura

----

.. seealso::
   * **Tip 4-2** - Enfoque de solución como tabla
   * **Tip 10-1** - Mantener objetivos de calidad cortos
   * **Sección 9** - Decisiones de Arquitectura
   * **Sección 11** - Riesgos y Deuda Técnica
   * **Método ATAM** - https://www.sei.cmu.edu/architecture/tools/evaluate/atam.cfm
