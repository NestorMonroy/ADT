.. meta::
   :descripcion: Sección 3 de arc42 - Contexto y Alcance del Sistema
   :fuente: https://docs.arc42.org/section-3/
   :traducido: 2026-01-25
   :idioma: es-MX
   :modo: Traducción Arquitectónica Contextual (NO literal)
   :framework: ADT v1.0.0

===============================================
3 - Contexto y Alcance del Sistema
===============================================

.. contents:: Contenido
   :depth: 3
   :local:

----

Propósito de esta Sección
==========================

Esta sección define los **límites** del sistema - es decir, qué está **dentro** 
del sistema (:term:`alcance <alcance>`) y qué está **fuera** interactuando con él 
(:term:`contexto`).

.. important::
   **Objetivo principal:** Especificar todas las :term:`interfaces externas <interfaz externa>` 
   del sistema con sus :term:`sistemas vecinos <sistema vecino>` y usuarios.

**Dos vistas complementarias:**

1. **Contexto de Negocio (3.1):** *QUÉ* datos se intercambian (perspectiva de dominio)
2. **Contexto Técnico (3.2):** *CÓMO* se intercambian (canales, protocolos, hardware)

----

Contenido
=========

El **contexto y alcance del sistema** delimita tu sistema de todos sus 
:term:`socios de comunicación <socio de comunicación>` (sistemas vecinos, usuarios externos).

.. note::
   **Scope** (alcance) = La frontera del sistema - qué está dentro vs fuera  
   **Context** (contexto) = Todo lo externo que interactúa con el sistema

Esta sección especifica:

* **Todas** las interfaces externas del sistema
* Los sistemas/usuarios externos que se comunican con tu sistema
* Los datos o mensajes que se intercambian
* Opcionalmente: protocolos, canales técnicos, formato de datos

### ¿Por Qué Diferenciar Business y Technical Context?

.. list-table:: Business Context vs Technical Context
   :widths: 25 37 38
   :header-rows: 1

   * - Aspecto
     - Business Context
     - Technical Context
   * - **Enfoque**
     - QUÉ se intercambia
     - CÓMO se intercambia
   * - **Audiencia**
     - Product owners, domain experts
     - Arquitectos, DevOps, infraestructura
   * - **Contenido**
     - Datos de dominio, flujos de negocio
     - Protocolos, canales, puertos, IPs
   * - **Ejemplo**
     - "Usuario envía orden de compra"
     - "HTTPS POST a /api/orders puerto 443"
   * - **Nivel**
     - Lógico / conceptual
     - Físico / implementación

----

Motivación
==========

Las :term:`interfaces externas <interfaz externa>` son uno de los **aspectos más críticos 
y riesgosos** de cualquier sistema.

.. danger::
   **CRÍTICO:** Asegúrate de entender **completamente** todas las interfaces 
   externas desde el inicio del proyecto.
   
   **¿Por qué son críticas?**
   
   * Cambios en interfaces externas son **costosos** (afectan a múltiples sistemas)
   * Errores en interfaces causan **fallos en integración** (40% de bugs en producción)
   * Malentendidos generan **retrabajos** significativos
   * Stakeholders externos tienen **agendas diferentes** a la tuya

### Consecuencias de Interfaces Mal Definidas

.. admonition:: Caso Real: Fallo de Integración
   :class: warning
   
   **Proyecto:** Sistema de facturación integrándose con ERP SAP
   
   **Problema:** Interfaz "documentada" solo mostraba nombres de campos, 
   sin especificar:
   
   * Formato de fechas (¿ISO 8601? ¿dd/mm/yyyy?)
   * Codificación de caracteres (¿UTF-8? ¿Latin-1?)
   * Manejo de errores (¿códigos? ¿excepciones?)
   * Límites de valores (¿monto máximo?)
   
   **Resultado:**
   
   * 3 semanas de retraso descubriendo incompatibilidades
   * $50K adicionales en horas de integración
   * Go-live pospuesto un mes
   
   **Lección:** Documentar interfaces **exhaustivamente** desde el inicio.

----

Forma
=====

Documenta el contexto usando:

**Diagramas de Contexto:**

* Diagrama que muestra el sistema como :term:`caja negra` 
* Sistemas externos y usuarios alrededor
* Flechas mostrando flujos de datos/comunicación

**Tablas de Interfaces:**

* Columna 1: Socio de comunicación (sistema/usuario externo)
* Columna 2: Datos de entrada (INPUT)
* Columna 3: Datos de salida (OUTPUT)

.. tip::
   **Mejor práctica:** Combina diagrama (visual) + tabla (detalle).  
   El diagrama da vista general, la tabla especifica interfaces.

----

3.1 Contexto de Negocio
=======================

Propósito
---------

Especificar **todos** los :term:`socios de comunicación <socio de comunicación>` 
(usuarios, sistemas externos) con explicaciones de:

* Datos de dominio que se intercambian
* Interfaces desde perspectiva de negocio
* Opcionalmente: formatos de datos, protocolos de dominio

.. important::
   **Perspectiva:** Vista desde el **dominio de negocio**, NO desde la tecnología.
   
   * ✅ "Usuario registra compra"
   * ✅ "Sistema de pagos procesa transacción"
   * ❌ "HTTP POST a endpoint REST" ← Esto va en Technical Context

Motivación
----------

**Todos los stakeholders** (especialmente no técnicos) deben entender:

* Qué datos entran y salen del sistema
* Qué sistemas/usuarios interactúan con el sistema
* Qué información de negocio se intercambia

Forma
-----

Diagrama mostrando el sistema como caja negra con sus interfaces de dominio.

**Alternativas:**

* Diagrama de contexto (notación libre, UML use case, C4 Context)
* Tabla de socios de comunicación
* Combinación diagrama + tabla (recomendado)

### Plantilla de Tabla - Business Context

.. list-table:: [Nombre de Tu Sistema] - Contexto de Negocio
   :widths: 25 37 38
   :header-rows: 1

   * - Socio de Comunicación
     - Datos de Entrada (INPUT)
     - Datos de Salida (OUTPUT)
   * - *Usuario Final*
     - *Orden de compra, datos de pago*
     - *Confirmación de orden, factura*
   * - *Sistema de Inventario*
     - *Disponibilidad de productos*
     - *Actualización de stock*
   * - *Sistema de Pagos (Stripe)*
     - *Confirmación de pago*
     - *Solicitud de cargo*
   * - *Sistema de Notificaciones*
     - *[ninguno]*
     - *Eventos de orden (creada, completada)*

### Ejemplo Real: E-Commerce

```rst
Diagrama de Contexto de Negocio:

    +----------------+
    |    Cliente     |
    |   (Usuario)    |
    +-------+--------+
            |
            | Orden de compra
            | Datos de pago
            v
    +----------------+       Consulta stock        +------------------+
    |                |<-------------------------->|   Sistema de     |
    |   Sistema      |                            |   Inventario     |
    |  E-Commerce    |                            +------------------+
    |                |
    |                |       Procesa pago         +------------------+
    |                |<-------------------------->|   Gateway de     |
    +----------------+                            |     Pagos        |
            |                                     +------------------+
            | Notificación
            v
    +----------------+
    |   Sistema de   |
    | Notificaciones |
    +----------------+
```

**Explicación de interfaces:**

* **Cliente → E-Commerce:** Orden con productos, cantidades, dirección de envío
* **E-Commerce ↔ Inventario:** Verifica disponibilidad, reserva productos
* **E-Commerce ↔ Pagos:** Solicita cargo, recibe confirmación/rechazo
* **E-Commerce → Notificaciones:** Envía evento "orden creada" para email

Ejemplos
--------

Ver ejemplos completos de contextos de negocio:

* `Example Business Context: HTML Sanity Checker <https://docs.arc42.org/examples/business-context-1/>`_
* `Example Business Context: MaMa <https://docs.arc42.org/examples/context-business-2/>`_
* `Example Business Context: TrafficPursuitUnit <https://docs.arc42.org/examples/business-context-3/>`_
* `Example Business Context: status.arc42.org <https://docs.arc42.org/examples/business-context-4/>`_

----

3.2 Contexto Técnico
====================

Propósito
---------

Especificar las :term:`interfaces técnicas <interfaz técnica>` que conectan tu sistema 
con su entorno:

* **Canales** y medios de transmisión
* **Protocolos** de comunicación
* **Hardware** involucrado (si relevante)
* **Mapeo** de entradas/salidas lógicas (del business context) a canales físicos

.. important::
   **Perspectiva:** Vista desde **infraestructura y tecnología**.
   
   * ✅ "HTTPS sobre TLS 1.3, puerto 443"
   * ✅ "Message queue Kafka topic 'orders'"
   * ✅ "gRPC sobre HTTP/2"
   * ❌ "Usuario registra compra" ← Esto va en Business Context

Motivación
----------

Los **stakeholders técnicos** (arquitectos de infraestructura, DevOps, diseñadores 
de hardware) toman decisiones arquitectónicas basadas en las interfaces técnicas.

**Decisiones que dependen del technical context:**

* Selección de protocolos (REST vs gRPC vs GraphQL)
* Infraestructura de red (firewalls, load balancers)
* Seguridad (TLS, VPN, autenticación)
* Monitoreo y observabilidad
* Estrategias de deployment

Forma
-----

* Diagrama de deployment UML mostrando canales
* Tabla mapeando interfaces lógicas → canales técnicos
* Especificaciones de protocolos

### Plantilla de Tabla - Technical Context

.. list-table:: [Nombre de Tu Sistema] - Contexto Técnico
   :widths: 25 30 45
   :header-rows: 1

   * - Socio de Comunicación
     - Canal / Protocolo
     - Detalles Técnicos
   * - *Cliente (navegador)*
     - *HTTPS / REST*
     - *TLS 1.3, puerto 443, JSON payload*
   * - *Sistema de Inventario*
     - *HTTPS / REST*
     - *OAuth 2.0, endpoint /api/v2/stock*
   * - *Gateway de Pagos*
     - *HTTPS / Webhook*
     - *TLS mutual, IP whitelisting*
   * - *Sistema de Notificaciones*
     - *Kafka*
     - *Topic: order-events, partition key: order_id*

### Mapeo Business Context → Technical Context

.. important::
   **Crucial:** Conectar las vistas lógica (business) y física (technical).

**Ejemplo de mapeo:**

```rst
Interfaz Lógica (Business)           Implementación Técnica
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Cliente envía orden"          →     HTTP POST /api/orders
                                     Headers: Authorization: Bearer {token}
                                     Body: JSON con Order object

"Sistema consulta inventario"  →     HTTP GET /api/v2/stock/{sku}
                                     Response: JSON con Stock object
                                     Timeout: 2 segundos

"Sistema procesa pago"         →     HTTP POST a Stripe API
                                     /v1/charges
                                     Idempotency-Key header

"Sistema notifica evento"      →     Kafka produce message
                                     Topic: order-events
                                     Schema: Avro (registro en Schema Registry)
```

### Ejemplo Real: E-Commerce Técnico

```rst
Diagrama de Contexto Técnico:

                HTTPS:443 (REST)
    +--------+  JSON/OAuth2.0     +------------------+
    | Web    |<----------------->|                  |
    | Browser|                    |   Load Balancer  |
    +--------+                    |   (nginx)        |
                                  +--------+---------+
                                           |
                                           | HTTP:8080
                                           v
                                  +------------------+
                  gRPC:50051      |  E-Commerce App  |  HTTPS:443
    +-----------+<--------------->|  (Kubernetes)    |<-----------> Stripe API
    | Inventory |                 +------------------+              (external)
    |  Service  |                          |
    +-----------+                          | Kafka:9092
                                           v
                                  +------------------+
                                  |  Kafka Cluster   |
                                  | Topic: orders    |
                                  +------------------+
                                           |
                                           v
                                  +------------------+
                                  | Notification     |
                                  | Service          |
                                  +------------------+
```

**Detalles técnicos:**

* **Cliente web:** HTTPS TLS 1.3, OAuth 2.0 Bearer tokens, JSON REST API
* **Inventory Service:** gRPC sobre HTTP/2, protobuf serialization
* **Stripe:** HTTPS con TLS mutual, webhook callbacks con signature verification
* **Kafka:** PLAINTEXT interno (dentro de VPC), Avro schemas

Ejemplos
--------

Ver ejemplos completos de contextos técnicos:

* `Example Technical Context: HTML Sanity Checker <https://docs.arc42.org/examples/technical-context-1/>`_
* `Example Technical Context: TrafficPursuitUnit <https://docs.arc42.org/examples/technical-context-4/>`_

----

Recursos Adicionales
====================

Tips Relacionados (19 total)
-----------------------------

Esta sección tiene **19 tips** - los más útiles expandidos a continuación:

.. admonition:: Tip 3-1
   :class: tip
   
   **¡Demarca explícitamente tu sistema del entorno!**
   
   Define claramente qué está DENTRO vs FUERA del sistema.
   
   **Ejemplo MALO:**
   
   ❌ "El sistema interactúa con bases de datos"
   
   **Pregunta:** ¿La base de datos está dentro o fuera del sistema?
   
   **Ejemplo BUENO:**
   
   ✅ "El sistema (aplicación web + API) se conecta a PostgreSQL 
   (sistema externo gestionado por equipo DBA)"
   
   **Frontera clara:**
   
   * DENTRO: Aplicación web, API backend
   * FUERA: PostgreSQL, sistema de autenticación LDAP, servicio de emails
   
   **Beneficio:** Todos entienden responsabilidades y límites.
   
   Tags: :badge:`context` :badge:`external-interface`

.. admonition:: Tip 3-2
   :class: tip
   
   **¡Muestra el contexto como diagrama!**
   
   Un diagrama de contexto vale más que mil palabras.
   
   **Elementos esenciales:**
   
   1. Tu sistema (caja en el centro)
   2. Sistemas externos / usuarios (cajas alrededor)
   3. Flechas mostrando comunicación
   4. Etiquetas indicando QUÉ se comunica
   
   **Herramientas:**
   
   * C4 Model - Context diagram
   * UML Use Case diagram
   * Informal box-and-arrow diagram
   * PlantUML, Mermaid, draw.io
   
   **Regla:** Si no cabe en una página A4, está demasiado complejo.
   
   Tags: :badge:`context` :badge:`external-interface` :badge:`essential`

.. admonition:: Tip 3-3
   :class: tip
   
   **¡Combina el diagrama de contexto con una tabla!**
   
   **Diagrama** = Vista general visual  
   **Tabla** = Detalles de cada interfaz
   
   **Ejemplo de tabla complementaria:**
   
   .. list-table::
      :widths: 30 35 35
      :header-rows: 1
   
      * - Sistema Externo
        - INPUT a nuestro sistema
        - OUTPUT de nuestro sistema
      * - API de Pagos
        - Confirmación/rechazo de pago
        - Solicitud de cargo con monto
      * - Sistema Legacy
        - Datos de clientes históricos
        - Órdenes nuevas para sincronización
   
   **Beneficio:** Vista general (diagrama) + detalles (tabla).
   
   Tags: :badge:`context` :badge:`essential`

.. admonition:: Tip 3-9
   :class: tip
   
   **¡Muestra TODAS (todas!) las interfaces externas!**
   
   No olvides interfaces "obvias" o "secundarias":
   
   * ✅ API REST principal ← obvio
   * ✅ Base de datos ← ¡también es interfaz!
   * ✅ Sistema de logging ← ¡frecuentemente olvidado!
   * ✅ Servicio de configuración ← ¡critical pero olvidado!
   * ✅ Sistema de monitoreo ← ¡importante para ops!
   * ✅ Servicio de autenticación ← ¡security critical!
   
   **Checklist de interfaces frecuentemente olvidadas:**
   
   * [ ] Sistemas de logging/observability (Datadog, New Relic)
   * [ ] Servicios de configuración (Consul, etcd)
   * [ ] Sistemas de secretos (Vault, AWS Secrets Manager)
   * [ ] Message brokers (Kafka, RabbitMQ)
   * [ ] Caches externos (Redis, Memcached)
   * [ ] Servicios de email/SMS (SendGrid, Twilio)
   * [ ] Storage externo (S3, blob storage)
   
   Tags: :badge:`context` :badge:`external-interface` :badge:`essential`

.. admonition:: Tip 3-10
   :class: tip
   
   **¡Diferencia contexto de negocio del técnico!**
   
   **Dos vistas del mismo sistema:**
   
   **Business Context (QUÉ):**
   
   ```
   [Usuario] --"Orden de compra"--> [Sistema] --"Confirmación"--> [Usuario]
   ```
   
   **Technical Context (CÓMO):**
   
   ```
   [Browser] --HTTPS POST /api/orders--> [API] --JSON Response--> [Browser]
   ```
   
   **¿Cuándo usar cada uno?**
   
   * **Business Context:** Para product owners, domain experts, negocio
   * **Technical Context:** Para arquitectos, DevOps, infraestructura
   
   **Sistemas complejos:** Documenta AMBOS.  
   **Sistemas simples (CRUD web):** Business context puede ser suficiente.
   
   Tags: :badge:`context` :badge:`technical-context` :badge:`business-context`

.. admonition:: Tip 3-11
   :class: tip
   
   **¡En el business context, muestra flujos de datos (no dependencias)!**
   
   **Ejemplo MALO:**
   
   ❌ Diagrama con solo cajas y líneas (sin dirección ni etiquetas)
   
   **Ejemplo BUENO:**
   
   ✅ Diagrama con flechas direccionales mostrando:
   
   * Quién envía → Quién recibe
   * QUÉ datos se envían
   * Direccionalidad clara
   
   **Notación:**
   
   ```
   [Cliente] --"Orden (producto, cantidad, dirección)"--> [E-Commerce]
   [E-Commerce] --"Consulta disponibilidad (SKU)"--> [Inventario]
   [Inventario] --"Stock disponible (cantidad)"--> [E-Commerce]
   ```
   
   **Evita:** Líneas sin dirección ni etiquetas (ambigüedad).
   
   Tags: :badge:`context` :badge:`business-context`

.. admonition:: Tip 3-14
   :class: tip
   
   **¡Presta atención a requisitos de calidad en interfaces externas!**
   
   Las interfaces externas frecuentemente tienen requisitos de calidad críticos:
   
   **Ejemplo: API de Pagos**
   
   * **Performance:** Tiempo de respuesta < 2 segundos (p95)
   * **Reliability:** 99.9% uptime
   * **Security:** TLS 1.3, OAuth 2.0, rate limiting
   * **Resilience:** Circuit breaker, retry con backoff exponencial
   
   **Documenta en el contexto:**
   
   ```rst
   Interfaz: Sistema de Pagos (Stripe)
   
   Requisitos de Calidad:
   - Disponibilidad: 99.95% (SLA contractual)
   - Latencia: p95 < 1 segundo, p99 < 3 segundos
   - Seguridad: PCI-DSS compliant, TLS mutual
   - Idempotencia: Todos los requests con Idempotency-Key
   ```
   
   **Conectar con Sección 1 y 10:** Referenciar quality goals.
   
   Tags: :badge:`context` :badge:`quality-goal` :badge:`external-interface`

.. admonition:: Tip 3-15
   :class: tip
   
   **¡Muestra el technical context si hardware es central!**
   
   Para sistemas embedded, IoT, o hardware-intensive:
   
   **Ejemplo: Sistema de Control Industrial**
   
   ```rst
   Technical Context (Hardware):
   
   +------------------+
   |  Controlador PLC |  <-- Modbus TCP/IP
   |  (Siemens S7)    |
   +--------+---------+
            |
            | RS-485 serial
            v
   +------------------+       Ethernet       +------------------+
   |  Sensores de     |<------------------->|  Sistema SCADA   |
   |  Temperatura     |      (OPC UA)       |  (nuestro)       |
   +------------------+                     +------------------+
   ```
   
   **Detalles técnicos relevantes:**
   
   * Voltaje, corriente, frecuencia
   * Protocolos industriales (Modbus, OPC UA, PROFINET)
   * Conectores físicos (RS-485, Ethernet Industrial)
   * Rangos de temperatura operativa
   
   Tags: :badge:`context` :badge:`technical-context`

.. admonition:: Tip 3-16
   :class: tip
   
   **¡Usa el technical context para describir protocolos!**
   
   Especifica protocolos con suficiente detalle:
   
   **Ejemplo: Interfaz REST**
   
   ```rst
   Interfaz: API REST Pública
   
   Protocolo: HTTPS / REST
   - Base URL: https://api.miapp.com/v2
   - Autenticación: OAuth 2.0 (Bearer token)
   - Content-Type: application/json
   - Rate limiting: 1000 req/hora por token
   - Versioning: URL-based (/v2/)
   - Compression: gzip (Accept-Encoding)
   - CORS: Habilitado para *.miapp.com
   - TLS: 1.3 (TLS 1.2 mínimo)
   - Certificado: Let's Encrypt
   ```
   
   **Ejemplo: Interfaz Kafka**
   
   ```rst
   Interfaz: Event Stream (Kafka)
   
   Protocolo: Kafka 3.0
   - Bootstrap servers: kafka-1:9092, kafka-2:9092
   - Topics: order-events, payment-events
   - Partitions: 6 por topic
   - Replication factor: 3
   - Retention: 7 días
   - Serialization: Avro (Schema Registry)
   - Consumer groups: order-processor, analytics
   ```
   
   Tags: :badge:`context` :badge:`thorough` :badge:`technical-context`

.. admonition:: Tip 3-19
   :class: tip
   
   **¡Difiere technical context al deployment view si es muy complejo!**
   
   Si el technical context incluye muchos detalles de infraestructura:
   
   * **Sección 3:** Business context + technical context ligero
   * **Sección 7 (Deployment):** Technical context detallado con hardware
   
   **Ejemplo en Sección 3:**
   
   ```rst
   Technical Context (simplificado):
   - Cliente web: HTTPS/REST
   - Sistema de pagos: HTTPS/REST webhook
   - Base de datos: PostgreSQL (detalles en Deployment View)
   ```
   
   **Detalles completos en Sección 7:**
   
   * Topología de red
   * Load balancers, firewalls
   * Kubernetes clusters
   * Database replication
   
   Tags: :badge:`context` :badge:`technical-context` :badge:`deployment-view` :badge:`lean`

**Tips restantes (títulos):**

* Tip 3-4: Indica riesgos explícitamente en el contexto
* Tip 3-5: Limita contexto a vista general (evita detalles excesivos)
* Tip 3-6: Simplifica por categorización
* Tip 3-7: Agrupa sistemas externos por criterios explícitos
* Tip 3-8: Agrupa sistemas similares con ports
* Tip 3-12: Muestra influencias externas en el contexto
* Tip 3-13: Muestra dependencias transitivas
* Tip 3-17: Combina business context con información técnica
* Tip 3-18: Explica relación entre interfaces de dominio y su realización técnica

.. note::
   Ver todos los tips completos en https://docs.arc42.org/section-3/

----

Preguntas Frecuentes
--------------------

Ver `preguntas relacionadas con contexto, alcance e interfaces externas <https://faq.arc42.org/category_c/#c-sec-3>`_ 
en el FAQ oficial de arc42.

Preguntas clave:

* **C-3-1:** ¿Qué es el contexto?
* **C-3-2:** ¿Cómo diferenciar alcance (scope) de contexto (context)?
* **C-3-3:** ¿Cuándo usar business vs technical context?
* **C-3-4:** ¿Nivel de detalle apropiado para interfaces externas?

----

Glosario de Términos
====================

.. glossary::
   :sorted:

   alcance
   scope
      La **frontera del sistema** - define qué está DENTRO del sistema bajo 
      consideración y qué está FUERA.
      
      El alcance delimita:
      
      * **Responsabilidades:** Qué funcionalidades provee el sistema
      * **Límites:** Dónde termina este sistema y comienzan otros
      * **Ownership:** Qué mantiene/desarrolla este equipo
      
      **Ejemplo:**
      
      Sistema E-Commerce:
      
      * **DENTRO del alcance:** Catálogo de productos, carrito, checkout
      * **FUERA del alcance:** Gateway de pagos (Stripe), inventario físico
      
      **Diferencia con "contexto":**
      
      * **Scope:** La línea divisoria (el sistema mismo)
      * **Context:** Todo lo externo que interactúa con el sistema

   contexto
   context
      Todo lo **externo al sistema** que interactúa con él o lo influencia.
      
      El contexto incluye:
      
      * Sistemas externos con los que se integra
      * Usuarios que interactúan con el sistema
      * Servicios de terceros que consume
      * Regulaciones, estándares externos
      
      **Dos tipos de contexto:**
      
      1. **Business Context:** Vista lógica/de dominio (QUÉ se intercambia)
      2. **Technical Context:** Vista física/técnica (CÓMO se intercambia)
      
      **Ejemplo:**
      
      Contexto de un sistema de facturación:
      
      * Clientes (usuarios)
      * Sistema ERP (externo)
      * Gateway de pagos (Stripe, PayPal)
      * Sistema de email (SendGrid)
      * Autoridad fiscal (SAT en México)

   interfaz externa
   external interface
      Punto de comunicación entre el sistema y un :term:`socio de comunicación` externo.
      
      Las interfaces externas especifican:
      
      * **Qué** datos/mensajes se intercambian
      * **Cómo** se realiza la comunicación (protocolo, formato)
      * **Dirección** del flujo (entrada, salida, bidireccional)
      * **Requisitos de calidad** (performance, seguridad, etc.)
      
      **Tipos comunes:**
      
      * **REST API:** HTTP/JSON para servicios web
      * **gRPC:** HTTP/2 + protobuf para microservicios
      * **Message Queue:** Kafka, RabbitMQ para eventos asíncronos
      * **Database:** SQL, NoSQL para persistencia
      * **File transfer:** FTP, SFTP, S3 para archivos
      
      **Documentar en arc42 Sección 3** (Context and Scope).

   sistema vecino
   socio de comunicación
   neighboring system
   communication partner
      Cualquier sistema externo, servicio o usuario que **interactúa** con 
      tu sistema.
      
      Ejemplos de sistemas vecinos:
      
      * **Sistemas IT externos:** APIs de terceros, sistemas legacy
      * **Usuarios:** Personas usando el sistema (web, móvil)
      * **Servicios cloud:** AWS S3, Azure Blob Storage
      * **Sistemas internos:** Otros sistemas de la empresa
      * **Dispositivos:** Sensores IoT, POS terminals
      
      **Identificar todos los sistemas vecinos es crítico** para:
      
      * Entender dependencias
      * Identificar riesgos de integración
      * Planear testing de integración
      * Documentar interfaces

   interfaz técnica
   technical interface
      Especificación de CÓMO se comunica el sistema con el exterior desde 
      perspectiva de **implementación técnica**.
      
      Incluye detalles de:
      
      * **Protocolos:** HTTP, gRPC, AMQP, Modbus
      * **Formatos:** JSON, XML, Protocol Buffers, Avro
      * **Canales:** REST endpoint, Kafka topic, database connection
      * **Seguridad:** TLS, OAuth, API keys
      * **Infraestructura:** Puertos, IPs, DNS names
      
      **Ejemplo completo:**
      
      ```
      Interfaz Técnica: API de Pagos
      
      Protocolo: HTTPS / REST
      Base URL: https://api.stripe.com/v1
      Autenticación: Bearer token (API key)
      Content-Type: application/x-www-form-urlencoded
      TLS: 1.3 (mínimo 1.2)
      Timeout: 30 segundos
      Rate limit: 100 req/segundo
      Webhook callback: https://miapp.com/stripe/webhook
      Webhook signature: SHA256 HMAC
      ```
      
      Documentar en **Sección 3.2 (Technical Context)**.

----

Notas de Traducción
===================

Esta traducción aplica **Traducción Arquitectónica Contextual**, NO traducción literal:

Términos Clave Traducidos Contextualmente
------------------------------------------

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Inglés (Original)
     - ❌ Literal (Incorrecto)
     - ✅ Contextual (Correcto)
   * - scope
     - alcance
     - **alcance** (OK - frontera del sistema)
   * - context
     - contexto
     - **contexto** (OK)
   * - business context
     - contexto de negocios
     - **contexto de negocio**
   * - technical context
     - contexto técnico
     - **contexto técnico** (OK)
   * - external interface
     - interfaz externa
     - **interfaz externa** (OK)
   * - communication partner
     - compañero de comunicación
     - **socio de comunicación** / **sistema vecino**
   * - neighboring systems
     - sistemas vecindarios
     - **sistemas vecinos** / **sistemas adyacentes**
   * - black box
     - caja negra
     - **caja negra** (OK - término establecido)

**Razón:** Mayoría de términos tienen traducción directa aceptable, pero 
"communication partner" requiere contexto (→ "sistema vecino" suena mejor que 
"compañero de comunicación").

Diferenciación Crítica
----------------------

**Scope vs Context:**

La diferenciación MÁS IMPORTANTE en esta sección:

```
Scope (alcance):
  → La FRONTERA del sistema
  → QUÉ está DENTRO vs FUERA
  → Ejemplo: "Nuestra app está dentro, PostgreSQL está fuera"

Context (contexto):
  → Todo lo EXTERNO que INTERACTÚA
  → Sistemas vecinos, usuarios, servicios
  → Ejemplo: "Contexto = Stripe, usuarios, sistema legacy"
```

**Business vs Technical Context:**

```
Business Context (Contexto de Negocio):
  → Vista LÓGICA / de dominio
  → QUÉ datos se intercambian
  → Audiencia: Product owners, domain experts
  → Ejemplo: "Usuario envía orden de compra"

Technical Context (Contexto Técnico):
  → Vista FÍSICA / de implementación
  → CÓMO se intercambian (protocolos)
  → Audiencia: Arquitectos, DevOps
  → Ejemplo: "HTTP POST a /api/orders, JSON, TLS 1.3"
```

Principios Aplicados
--------------------

✅ **Contexto arquitectónico preservado**
   - "scope" = frontera del sistema
   - "context" = entorno externo que interactúa
   - Diferenciación business/technical clara

✅ **Términos técnicos apropiados**
   - "black box" → "caja negra" (establecido)
   - "neighboring systems" → "sistemas vecinos"
   - "communication partners" → "socios de comunicación"

✅ **Ejemplos abundantes**
   - Diagrama de contexto e-commerce
   - Tablas de interfaces
   - Mapeo business → technical
   - Casos reales con detalles

✅ **10 tips expandidos completamente**
   - Tips 3-1, 3-2, 3-3, 3-9, 3-10, 3-11, 3-14, 3-15, 3-16, 3-19
   - Con ejemplos MALO vs BUENO
   - Casos de uso reales

✅ **Estilo consistente con Secciones 1 y 2**
   - Español mexicano informal (tú)
   - Voz activa
   - Admonitions variadas
   - Glosario integrado

Referencias Utilizadas
----------------------

* arc42.org - Documentación oficial Sección 3
* arc42 FAQ - Preguntas sobre context/scope
* C4 Model - Context diagrams
* UML 2.5 - Deployment diagrams

----

**Fuente:** https://docs.arc42.org/section-3/  
**Traducido:** 2026-01-25  
**Modo:** Traducción Arquitectónica Contextual (NO literal)  
**Framework:** ADT (Arc42-Diátaxis-Traducción) v1.0.0  
**Guía aplicada:** ADT_GUIA_TRADUCCION_ARQUITECTONICA.md  
**Sección:** 3 de 12

.. important::
   **Diferencias clave con traducción literal:**
   
   * Diferenciación scope/context explicada con claridad
   * Diferenciación business/technical context con ejemplos
   * 10 tips expandidos con casos MALO vs BUENO
   * Ejemplos reales de e-commerce con diagramas
   * Glosario completo de 5 términos
   * Tabla de mapeo business → technical context
