.. _risks_tip_2:

===============================================================
Tip 11-2: ¡Analiza las interfaces (externas) para problemas y riesgos!
===============================================================

:Tema: Riesgos en interfaces externas
:Palabras clave: risk, problem, external-interface, interface

----

Las **interfaces** (a menudo **interfaces externas**) son fuentes de problemas, o al menos conllevan **riesgos** significativos, con respecto a algunos **requisitos de calidad** del sistema, es decir:

* **Disponibilidad** (Availability)
* **Robustez** (Robustness)
* **Seguridad** (Security)

Tipos de Riesgos en Interfaces
===============================

**1. Riesgos de Disponibilidad**

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Riesgo**
 - **Ejemplo**
 * - Servicio externo no disponible
 - API de pago cae -> sistema no puede procesar transacciones
 * - Latencia alta
 - Servicio de terceros lento -> timeouts en nuestro sistema
 * - Rate limiting
 - API externa limita requests -> funcionalidad degradada

**2. Riesgos de Robustez**

* **Cambios inesperados en formato de datos**

 Ejemplo: API externa cambia estructura JSON sin previo aviso

* **Datos inválidos o inconsistentes**

 Ejemplo: Servicio externo retorna valores fuera de rango esperado

* **Versioning y compatibilidad**

 Ejemplo: Actualización de API rompe integración existente

**3. Riesgos de Seguridad**

* **Autenticación débil**

 Ejemplo: API externa usa tokens no expirados

* **Datos sensibles en tránsito**

 Ejemplo: Interfaz transmite datos sin encriptación

* **Injection attacks**

 Ejemplo: Interfaz vulnerable a SQL injection o XSS

----

**Análisis Sistemático de Interfaces:**

**Paso 1: Inventario de Interfaces**

Identifica TODAS las interfaces externas:

.. code-block:: text

 Interface ID: EXT-001
 Nombre: Servicio de Pagos Stripe
 Tipo: REST API
 Dirección: Bidireccional (llamamos nosotros)
 Criticidad: Alta

 Interface ID: EXT-002
 Nombre: Webhook de notificaciones
 Tipo: HTTP POST callback
 Dirección: Inbound (ellos nos llaman)
 Criticidad: Media

**Paso 2: Evaluar Riesgos por Interface**

Para cada interfaz, pregunta:

1. ¿Qué pasa si esta interfaz no está disponible?
2. ¿Qué pasa si esta interfaz retorna datos incorrectos?
3. ¿Qué pasa si esta interfaz es lenta?
4. ¿Qué pasa si esta interfaz cambia sin aviso?
5. ¿Qué pasa si esta interfaz es comprometida?

**Paso 3: Documentar Mitigaciones**

.. list-table:: Ejemplo de Análisis de Interfaz
 :header-rows: 1
 :widths: 20 30 25 25

 * - **Interface**
 - **Riesgo**
 - **Impacto**
 - **Mitigación**
 * - API Pagos
 - Servicio no disponible
 - Alto: no se procesan pagos
 - Circuit breaker + cola de reintentos
 * - API Pagos
 - Cambio de formato
 - Alto: integración rota
 - Tests de contrato + versionado
 * - Webhook
 - Datos maliciosos
 - Medio: posible XSS
 - Validación estricta + sanitización

----

**Estrategias de Mitigación Comunes:**

* **Circuit Breaker Pattern**: Prevenir cascada de fallos
* [PROCESSING] **Retry with Exponential Backoff**: Manejar fallos transitorios
* [LIST] **Contract Testing**: Detectar cambios incompatibles temprano
* [OK] **Input Validation**: Rechazar datos inesperados
* **Mutual TLS**: Autenticación bidireccional
* [TABLE] **Monitoring & Alerting**: Detectar problemas rápido
* [MASK] **Fallback & Degradación**: Funcionalidad reducida vs fallo total

----

Ver También
===========

* **Sección 3** - `Contexto y Alcance del Sistema </section-3/>`_
* **Tip 3-14** - Requisitos de calidad en interfaces externas
* **Tip 11-3** - Identificar riesgos por evaluación cualitativa

----

.. seealso::
 * **Sección 3.1** - Contexto de Negocio (interfaces de negocio)
 * **Sección 3.2** - Contexto Técnico (interfaces técnicas)
 * **Sección 10** - Requisitos de Calidad (disponibilidad, seguridad)
