.. _risks_tip_4:

===============================================================
Tip 11-4: ¡Analiza los _procesos_ para problemas y riesgos!
===============================================================

:Tema: Riesgos en procesos
:Palabras clave: risk, problem

----

Algunos problemas y **riesgos** se originan de *procesos* dentro y alrededor del sistema, es decir:

Procesos de Requisitos
======================

**Riesgo:** Si no hay un proceso de requisitos acordado y claro, esto puede llevar a problemas a largo plazo.

**Problemas Comunes:**

* [ERROR] **Requisitos ambiguos o contradictorios**

 Ejemplo: "El sistema debe ser rápido y seguro" sin métricas

* [ERROR] **Cambios de requisitos sin control**

 Ejemplo: Scope creep sin evaluación de impacto

* [ERROR] **Falta de priorización**

 Ejemplo: Todo es "urgente y crítico"

* [ERROR] **Stakeholders no identificados**

 Ejemplo: Descubrir usuario clave en fase de testing

**Mitigaciones:**

* [OK] Proceso formal de gestión de requisitos
* [OK] Template estándar para requisitos
* [OK] Revisión y aprobación de cambios
* [OK] Análisis de stakeholders temprano

----

Procesos de Desarrollo
=======================

Incluyen **implementación**, **pruebas**, **versionado**, **configuración**.

**Riesgos Típicos:**

.. list-table::
 :header-rows: 1
 :widths: 30 35 35

 * - **Proceso**
   - **Riesgo**
   - **Mitigación**
 * - **Implementación**
   - Sin estándares de código
   - Code reviews + linters
 * - **Versionado**
   - Git flow no definido
   - Adoptar Git flow o trunk-based
 * - **Testing**
   - Tests solo manuales
   - Automatización de tests
 * - **Configuración**
   - Config hardcodeada
   - Externalize configuration

----

Procesos de Build, Release y Deployment
========================================

**Pueden causar problemas serios para los sistemas.**

**Problemas Comunes:**

* **Builds no reproducibles**

 *Riesgo: "Funciona en mi máquina" -> falla en producción*

 **Solución:** Docker containers + lock files

* **Deployment manual propenso a errores**

 *Riesgo: Pasos olvidados, configuración incorrecta*

 **Solución:** CI/CD automatizado

* **Sin rollback plan**

 *Riesgo: Deploy roto -> downtime prolongado*

 **Solución:** Blue-green deployment + feature flags

* **Releases poco frecuentes**

 *Riesgo: Cambios grandes = mayor riesgo*

 **Solución:** Continuous deployment + small batches

**Pipeline de CI/CD Robusto:**

.. code-block:: text

 Commit -> Build -> Unit Tests -> Integration Tests ->
 Security Scan -> Deploy Staging -> E2E Tests ->
 Manual Approval -> Deploy Production -> Health Check ->
 Rollback if needed

----

Procesos de Test y Quality Assurance
=====================================

**Riesgos:**

* [WARNING] **Cobertura de tests baja**

 *Consecuencia: Bugs no detectados llegan a producción*

* [WARNING] **Tests lentos**

 *Consecuencia: Desarrolladores los saltan -> cobertura baja*

* [WARNING] **Sin tests de regresión**

 *Consecuencia: Fixes rompen funcionalidad existente*

* [WARNING] **QA solo al final**

 *Consecuencia: Bugs costosos de arreglar*

**Mejores Prácticas:**

* [OK] **Test Pyramid**: Muchos unit, algunos integration, pocos E2E
* [OK] **Tests automatizados en CI**: Ejecutar en cada commit
* [OK] **Shift-left testing**: Testing temprano en el ciclo
* [OK] **Test coverage mínimo**: Por ejemplo, 80%

----

Procesos de Gestión
====================

Los procesos de **gestión** y decisiones relacionadas pueden no estar alineados con los requisitos del sistema y/o **objetivos de calidad**.

**Desalineaciones Comunes:**

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - **Desalineación**
   - **Impacto**
   - **Mitigación**
 * - Management prioriza features sobre calidad
   - Deuda técnica creciente
   - Comunicar costo de deuda
 * - Decisiones sin input técnico
   - Compromisos irrealistas
   - Incluir arquitecto en planning
 * - Presión por deadlines
   - Shortcuts -> bugs
   - Timeboxing + MVP approach
 * - Sin tiempo para refactoring
   - Código se degrada
   - Reservar 20% para tech debt

----

**Checklist de Análisis de Procesos:**

Para cada proceso crítico, pregunta:

1. [ ] **¿Está documentado?**

 Si no -> ¿Cómo se capacita a nuevos miembros?

2. [ ] **¿Es seguido consistentemente?**

 Si no -> ¿Por qué? ¿Es demasiado complejo?

3. [ ] **¿Tiene métricas de calidad?**

 Si no -> ¿Cómo sabes si funciona?

4. [ ] **¿Es automatizado donde sea posible?**

 Si no -> ¿Cuál es el riesgo de error humano?

5. [ ] **¿Hay feedback loops?**

 Si no -> ¿Cómo mejora el proceso?

6. [ ] **¿Está alineado con objetivos de calidad?**

 Si no -> ¿Qué compromiso está haciendo?

----

**Ejemplo de Riesgo de Proceso:**

.. code-block:: text

 ID: PROC-001
 Tipo: Proceso de Deployment

 Problema:
 Deployments a producción se hacen manualmente los viernes tarde.
 Requiere 3 horas, múltiples pasos manuales, sin rollback plan.

 Riesgos:
 - Error humano -> downtime
 - Viernes tarde -> soporte limitado fin de semana
 - Sin rollback -> recovery lento

 Impacto: Alto (downtime = pérdida de ingresos)
 Probabilidad: Media (1 de cada 4 deploys tiene problema)

 Mitigación Propuesta:
 1. Automatizar deployment con CI/CD (2 semanas)
 2. Cambiar ventana a martes-jueves (inmediato)
 3. Implementar blue-green deployment (3 semanas)
 4. Practicar rollback en staging (1 semana)

----

.. seealso::
 * **Tip 11-1** - Buscar riesgos con stakeholders
 * **Tip 11-5** - Analizar datos para riesgos
 * **Tip 11-6** - Analizar código fuente para riesgos
 * **Sección 9** - Decisiones de Arquitectura
