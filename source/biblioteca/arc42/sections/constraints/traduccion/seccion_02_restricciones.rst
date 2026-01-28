.. meta::
   :descripcion: Sección 2 de arc42 - Restricciones Arquitectónicas
   :fuente: https://docs.arc42.org/section-2/
   :traducido: 2026-01-25
   :idioma: es-MX
   :modo: Traducción Arquitectónica Contextual (NO literal)
   :framework: ADT v1.0.0

===============================================
2 - Restricciones Arquitectónicas
===============================================

.. contents:: Contenido
   :depth: 3
   :local:

----

Propósito de esta Sección
==========================

Esta sección documenta cualquier :term:`restricción <restricción arquitectónica>` que 
limite la libertad de los arquitectos de software en sus decisiones de diseño, 
implementación o en los procesos de desarrollo.

.. important::
   **Alcance de las restricciones:** Estas restricciones frecuentemente trascienden 
   sistemas individuales y son válidas para organizaciones y empresas completas.

Ejemplos comunes de restricciones:

* Uso obligatorio de tecnologías específicas (lenguajes, frameworks, bases de datos)
* Limitaciones de infraestructura (data centers, clouds permitidos)
* Estándares organizacionales (procesos, metodologías)
* Regulaciones y normativas (GDPR, SOX, ISO)
* Restricciones presupuestarias y de tiempo

----

Contenido
=========

Una **restricción arquitectónica** es cualquier requisito que:

* **Limita** las opciones de diseño de los arquitectos
* **Restringe** las decisiones de implementación
* **Condiciona** el proceso de desarrollo

.. danger::
   **Confusión común:** NO confundir "constraint" (restricción) con "requirement" (requisito).
   
   * **Restricción (Constraint):** Algo que LIMITA tus opciones de diseño
   * **Requisito (Requirement):** Algo que el sistema DEBE cumplir
   
   **Ejemplos:**
   
   ❌ **Incorrecto:** "El sistema debe usar PostgreSQL" → Llamas a esto requisito
   ✅ **Correcto:** "El sistema debe usar PostgreSQL" → Esto es una RESTRICCIÓN técnica
   
   ❌ **Incorrecto:** "El sistema debe procesar 1000 transacciones/s" → Llamas a esto restricción
   ✅ **Correcto:** "El sistema debe procesar 1000 transacciones/s" → Esto es un REQUISITO funcional
   
   **Regla de oro:**
   
   * Si **limita tus opciones** → Restricción
   * Si **define lo que debe hacer** → Requisito

----

Motivación
==========

Los arquitectos deben saber **exactamente** dónde tienen libertad en sus decisiones 
de diseño y dónde deben cumplir con restricciones establecidas.

.. warning::
   Las restricciones **siempre** deben abordarse - aunque algunas sean negociables.

**¿Por qué documentar restricciones?**

1. **Transparencia:** El equipo conoce las limitaciones desde el inicio
2. **Evitar retrabajos:** No diseñar soluciones que violen restricciones
3. **Negociación:** Identificar restricciones negociables vs no negociables
4. **Trazabilidad:** Entender por qué se tomaron ciertas decisiones
5. **Onboarding:** Nuevos miembros entienden el contexto rápidamente

### Restricciones Negociables vs No Negociables

No todas las restricciones son absolutas:

.. list-table:: Tipos de Restricciones por Negociabilidad
   :widths: 30 35 35
   :header-rows: 1

   * - Tipo
     - Ejemplo
     - Negociabilidad
   * - **Técnicas Heredadas**
     - "Debe usar base de datos existente Oracle"
     - ⚠️ Difícil (migración costosa)
   * - **Regulatorias**
     - "Datos deben estar en EU (GDPR)"
     - ❌ No negociable
   * - **Organizacionales**
     - "Usar metodología Scrum"
     - ✅ Negociable con gerencia
   * - **Presupuestarias**
     - "Budget máximo $100K"
     - ⚠️ Posiblemente (con justificación)
   * - **Tecnológicas Políticas**
     - "Solo lenguajes aprobados: Java, Python"
     - ✅ Negociable (justificar nuevo lenguaje)

----

Forma
=====

Documentar restricciones en **tablas simples** con explicaciones claras.

Si es necesario, subdividir en categorías:

1. **Restricciones Técnicas** - Tecnologías, plataformas, herramientas
2. **Restricciones Organizacionales** - Estructura, procesos, recursos
3. **Restricciones Políticas** - Decisiones de management, estándares corporativos
4. **Convenciones** - Guías de programación, versionado, documentación

### Plantilla de Tabla de Restricciones

.. list-table:: Restricciones del Sistema
   :widths: 20 40 40
   :header-rows: 1

   * - Tipo
     - Restricción
     - Contexto / Justificación
   * - Técnica
     - *Ejemplo: PostgreSQL 15+ como BD*
     - *Contrato vigente con proveedor hasta 2027*
   * - Organizacional
     - *Ejemplo: Equipo máximo 8 personas*
     - *Política de equipos ágiles de la empresa*
   * - Política
     - *Ejemplo: Solo cloud AWS*
     - *Partnership estratégico corporativo*
   * - Convención
     - *Ejemplo: Code review obligatorio*
     - *Estándar de calidad del departamento*

----

Tipos de Restricciones
======================

2.1 Restricciones Técnicas
---------------------------

Limitaciones relacionadas con **tecnología, hardware, software**.

**Ejemplos comunes:**

.. admonition:: Restricciones Técnicas Típicas
   :class: note
   
   **Plataforma y OS:**
   
   * Sistema debe ejecutarse en Windows Server 2022
   * Aplicación móvil solo para iOS 16+
   * Debe ser compatible con navegadores Chrome, Firefox, Safari
   
   **Tecnologías Obligatorias:**
   
   * Lenguaje de programación: Java 17 LTS
   * Framework web: Spring Boot 3.x
   * Base de datos: PostgreSQL 15 o superior
   * Message broker: Apache Kafka
   
   **Infraestructura:**
   
   * Deployment solo en AWS (no Azure, no GCP)
   * Data center físico en Frankfurt
   * CDN: CloudFlare obligatorio
   
   **Herramientas de Desarrollo:**
   
   * IDE: IntelliJ IDEA (licencia corporativa)
   * Control de versiones: GitLab Enterprise
   * CI/CD: Jenkins (instalación on-premise)

### Ejemplo Real: Restricciones Técnicas

.. code-block:: rst

   **Sistema de Facturación Electrónica**
   
   +------------------+-------------------------------------+--------------------------------+
   | Categoría        | Restricción                         | Justificación                  |
   +==================+=====================================+================================+
   | Lenguaje         | Java 11 (mínimo)                    | Skills del equipo, ecosistema  |
   +------------------+-------------------------------------+--------------------------------+
   | Base de Datos    | PostgreSQL 13+                      | Contrato corporativo vigente   |
   +------------------+-------------------------------------+--------------------------------+
   | Servidor App     | WildFly 26                          | Estándar JEE del departamento  |
   +------------------+-------------------------------------+--------------------------------+
   | Cloud            | AWS (región us-east-1)              | Compliance: datos en USA       |
   +------------------+-------------------------------------+--------------------------------+
   | Autenticación    | LDAP corporativo (Active Directory) | Política de identidad única    |
   +------------------+-------------------------------------+--------------------------------+

2.2 Restricciones Organizacionales
-----------------------------------

Limitaciones relacionadas con **estructura, procesos, recursos humanos**.

**Ejemplos comunes:**

.. admonition:: Restricciones Organizacionales Típicas
   :class: note
   
   **Equipo y Recursos:**
   
   * Tamaño de equipo fijo: 6 personas (no se puede contratar más)
   * 40% del desarrollo debe ser offshore (India)
   * Solo 1 arquitecto disponible, tiempo compartido con otros proyectos
   
   **Procesos y Metodologías:**
   
   * Metodología obligatoria: Scrum con sprints de 2 semanas
   * Code reviews obligatorios (mínimo 2 aprobaciones)
   * Releases solo cada trimestre (ventanas de deployment)
   
   **Horarios y Disponibilidad:**
   
   * Equipo distribuido: 3 time zones (México, España, India)
   * Reuniones sincrónicas solo entre 13:00-15:00 UTC
   * Soporte 24/7 imposible (solo horario laboral)
   
   **Proveedores y Partners:**
   
   * Development offshore con partner certificado XYZ
   * QA por equipo externo (outsourcing)
   * Infraestructura gestionada por equipo DevOps corporativo

### Ejemplo Real: Restricciones Organizacionales

.. code-block:: rst

   **Proyecto Modernización CRM**
   
   +------------------+-------------------------------------+--------------------------------+
   | Categoría        | Restricción                         | Impacto en Arquitectura        |
   +------------------+-------------------------------------+--------------------------------+
   | Equipo           | 2 developers senior                 | Arquitectura debe ser simple   |
   |                  | 4 developers junior                 | Documentación exhaustiva       |
   +------------------+-------------------------------------+--------------------------------+
   | Outsourcing      | 50% desarrollo en Argentina         | APIs muy bien definidas        |
   |                  |                                     | Comunicación asíncrona         |
   +------------------+-------------------------------------+--------------------------------+
   | Proceso          | SAFE (Scaled Agile Framework)       | Sincronización con otros teams |
   |                  |                                     | PI Planning cada 10 semanas    |
   +------------------+-------------------------------------+--------------------------------+
   | Aprobaciones     | Architecture Review Board mensual   | Decisiones deben planificarse  |
   |                  |                                     | ADRs formales requeridos       |
   +------------------+-------------------------------------+--------------------------------+

2.3 Restricciones Políticas
----------------------------

Limitaciones relacionadas con **decisiones de management, estándares corporativos**.

**Ejemplos comunes:**

.. admonition:: Restricciones Políticas Típicas
   :class: note
   
   **Tecnológicas (decididas por management):**
   
   * "Solo tecnologías open-source" (decisión CEO)
   * "Migrar todo a microservicios" (mandato CTO)
   * "Cloud-first strategy" (política corporativa)
   
   **Comerciales:**
   
   * Partnership con Microsoft → Usar Azure, .NET
   * Contrato con Oracle → Usar Oracle DB obligatorio
   * Proveedor preferido IBM → Preferencia por soluciones IBM
   
   **Seguridad y Compliance:**
   
   * Certificación ISO 27001 obligatoria
   * SOC 2 Type II requerido
   * GDPR compliance (datos solo en EU)
   * HIPAA compliance (datos médicos en USA)
   
   **Marca y Legal:**
   
   * Usar solo productos con licencias aprobadas por Legal
   * No usar tecnologías de ciertos países (restricciones geopolíticas)
   * Branding guidelines estrictas (UI/UX predefinido)

2.4 Convenciones
----------------

**Guías, estándares y convenciones** que el equipo debe seguir.

**Tipos de convenciones:**

.. list-table:: Tipos de Convenciones Comunes
   :widths: 25 75
   :header-rows: 1

   * - Tipo
     - Ejemplos
   * - **Programación**
     - • Google Java Style Guide
       
       • PEP 8 para Python
       
       • ESLint rules para JavaScript
       
       • SonarQube quality gates
   * - **Versionado**
     - • Git Flow workflow
       
       • Semantic Versioning (semver)
       
       • Conventional Commits
       
       • Branch naming: feature/JIRA-123-description
   * - **Documentación**
     - • arc42 para arquitectura
       
       • OpenAPI 3.0 para APIs
       
       • Markdown para READMEs
       
       • Confluence para wiki técnico
   * - **Nomenclatura**
     - • CamelCase para clases Java
       
       • snake_case para funciones Python
       
       • kebab-case para URLs REST
       
       • SCREAMING_SNAKE_CASE para constantes
   * - **Testing**
     - • Code coverage mínimo 80%
       
       • Unit tests obligatorios (JUnit)
       
       • Integration tests para APIs
       
       • E2E tests para flujos críticos

### Ejemplo Real: Convenciones de Equipo

```rst
**Proyecto E-Commerce**

Convenciones de Código:
  • Lenguaje: Java 17
  • Style guide: Google Java Style
  • Linter: Checkstyle con reglas corporativas
  • Formatter: IntelliJ auto-format (compartido en repo)

Convenciones de Git:
  • Workflow: GitHub Flow (simplificado)
  • Commits: Conventional Commits
    * feat: nueva funcionalidad
    * fix: corrección de bug
    * docs: cambios en documentación
  • Branches: tipo/JIRA-id-descripcion
    * Ejemplo: feature/ECOM-456-payment-integration

Convenciones de Testing:
  • Framework: JUnit 5 + Mockito
  • Coverage mínimo: 75% (medido con JaCoCo)
  • Naming: testMetodoEnPrueba_Condicion_ResultadoEsperado()
  • Ejemplo: testCreateOrder_WithInvalidProduct_ThrowsException()

Convenciones de Documentación:
  • APIs: OpenAPI 3.0 (Swagger UI)
  • Arquitectura: arc42 (este documento)
  • ADRs: Markdown en docs/adr/
  • README: Template corporativo
```

----

Ejemplos
========

Ver ejemplos completos de restricciones en sistemas reales:

* `Example Constraints: HTML Sanity Checker <https://docs.arc42.org/examples/constraints-1/>`_

----

Recursos Adicionales
====================

Tips Relacionados (5 total)
----------------------------

.. admonition:: Tip 2-1
   :class: tip
   
   **¡Considera las restricciones de otros sistemas en la organización!**
   
   Tu sistema no vive aislado. Frecuentemente debe:
   
   * Integrarse con sistemas existentes
   * Compartir infraestructura común
   * Cumplir estándares corporativos
   * Usar servicios compartidos (autenticación, logging, etc.)
   
   **Ejemplo:**
   
   Si todos los sistemas de la empresa usan Active Directory para autenticación,
   tu sistema probablemente **debe** usarlo también (restricción organizacional).
   
   **Acción:** Investiga qué restricciones tienen otros sistemas y evalúa si 
   aplican también al tuyo.
   
   Tags: :badge:`constraint`

.. admonition:: Tip 2-2
   :class: tip
   
   **¡Clarifica las consecuencias de las restricciones!**
   
   No solo documentes "debemos usar tecnología X", explica:
   
   * ¿Por qué existe esta restricción?
   * ¿Qué impacto tiene en la arquitectura?
   * ¿Es negociable o absoluta?
   * ¿Qué alternativas se consideraron?
   
   **Ejemplo MALO:**
   
   ❌ "Debemos usar Oracle Database"
   
   **Ejemplo BUENO:**
   
   ✅ "Debemos usar Oracle Database porque:
   
   * Contrato corporativo vigente hasta 2027 (no negociable)
   * Equipo DBA solo tiene expertise en Oracle
   * Otros 15 sistemas de la empresa ya lo usan
   * Impacto: No podemos usar PostgreSQL aunque tenga mejor performance para nuestro caso"
   
   **Beneficio:** Los stakeholders entienden el **por qué** de decisiones que 
   parecen subóptimas.
   
   Tags: :badge:`constraint` :badge:`stakeholder`

.. admonition:: Tip 2-3
   :class: tip
   
   **¡Documenta restricciones organizacionales!**
   
   Las restricciones técnicas son obvias, pero las organizacionales son igual 
   de importantes:
   
   * Tamaño y composición del equipo
   * Disponibilidad de recursos (tiempo parcial, compartidos)
   * Procesos obligatorios (aprobaciones, revisiones)
   * Dependencias de otros equipos
   
   **Ejemplo:**
   
   ```rst
   Restricciones Organizacionales:
   
   1. Equipo de 5 personas (3 en México, 2 en España)
      → Comunicación asíncrona preferida
      → Reuniones sincrónicas máximo 1h/día
   
   2. Arquitecto disponible solo 50% del tiempo
      → Decisiones deben ser autónomas cuando sea posible
      → ADRs ligeros para documentar decisiones
   
   3. Deployment requiere aprobación Change Advisory Board
      → Ventanas de deployment solo viernes 10pm-2am
      → Rolling updates imposibles (downtime aceptable)
   ```
   
   **Impacto:** Estas restricciones afectan tanto la arquitectura como los procesos.
   
   Tags: :badge:`constraint`

.. admonition:: Tip 2-4
   :class: tip
   
   **¡Documenta restricciones de diseño y desarrollo!**
   
   Incluye restricciones que afectan **cómo** se diseña y desarrolla:
   
   * Guías de diseño (patrones obligatorios)
   * Frameworks y librerías aprobadas
   * Herramientas de desarrollo
   * Procesos de CI/CD
   
   **Ejemplo:**
   
   ```rst
   Restricciones de Diseño:
   
   • Patrón MVC obligatorio (estándar del equipo)
   • Dependency Injection con Spring Framework
   • Logging con SLF4J + Logback (no Log4j)
   • Exception handling centralizado
   
   Restricciones de Desarrollo:
   
   • IDE: IntelliJ IDEA (licencia corporativa)
   • Build tool: Maven 3.8+
   • Repository: GitLab Enterprise on-premise
   • CI/CD: Jenkins pipeline (Jenkinsfile en repo)
   • Artifacts: Nexus Repository Manager
   ```
   
   Tags: :badge:`constraint`

.. admonition:: Tip 2-5
   :class: tip
   
   **¡Diferencia diferentes categorías de restricciones!**
   
   Categorizar restricciones ayuda a:
   
   * Identificarlas sistemáticamente
   * Entender su origen y negociabilidad
   * Comunicarlas apropiadamente a stakeholders
   
   **Categorías recomendadas:**
   
   1. **Técnicas** - Tecnología, plataformas, herramientas
   2. **Organizacionales** - Equipo, procesos, recursos
   3. **Políticas** - Decisiones management, estándares corporativos
   4. **Convenciones** - Guías de código, documentación, nomenclatura
   5. **Regulatorias** - Leyes, certificaciones, compliance
   6. **Presupuestarias** - Costos, licencias, contratos
   
   **Plantilla:**
   
   ```rst
   2.1 Restricciones Técnicas
   --------------------------
   [Lista de restricciones técnicas]
   
   2.2 Restricciones Organizacionales
   -----------------------------------
   [Lista de restricciones organizacionales]
   
   2.3 Restricciones Políticas
   ---------------------------
   [Lista de restricciones políticas]
   
   ...
   ```
   
   **Beneficio:** Vista completa y estructurada de todas las limitaciones.
   
   Tags: :badge:`constraint` :badge:`essential`

----

Preguntas Frecuentes
--------------------

Ver `preguntas relacionadas con restricciones <https://faq.arc42.org/category_c/#c-sec-2>`_ 
en el FAQ oficial de arc42.

Preguntas clave:

* **C-2-1:** ¿Qué son las restricciones?
* **C-2-2:** ¿Cómo diferenciar restricciones de requisitos?
* **C-2-3:** ¿Qué hacer con restricciones heredadas?
* **C-2-4:** ¿Cómo negociar restricciones?

----

Glosario de Términos
====================

.. glossary::
   :sorted:

   restricción arquitectónica
   constraint
      Cualquier requisito, decisión o condición que **limita** la libertad de 
      los arquitectos en sus decisiones de diseño, implementación o proceso.
      
      Las restricciones pueden ser:
      
      * **Técnicas:** Tecnologías, plataformas, herramientas obligatorias
      * **Organizacionales:** Estructura de equipo, procesos, recursos
      * **Políticas:** Decisiones de management, estándares corporativos
      * **Regulatorias:** Leyes, certificaciones, compliance
      
      **Diferencia clave con "requisito":**
      
      * **Restricción:** LIMITA tus opciones ("Debes usar Java")
      * **Requisito:** DEFINE lo que debe hacer ("Sistema debe procesar pagos")
      
      **Ejemplos:**
      
      * "El sistema debe ejecutarse en AWS" → Restricción de infraestructura
      * "Solo se permite usar PostgreSQL" → Restricción técnica
      * "Equipo máximo de 6 personas" → Restricción organizacional
      * "Cumplimiento GDPR obligatorio" → Restricción regulatoria
      
      **Nota:** En arc42, las restricciones se documentan en la Sección 2.

   restricción técnica
   technical constraint
      Restricción relacionada con **tecnología, hardware o software**.
      
      Incluye decisiones sobre:
      
      * Lenguajes de programación permitidos
      * Frameworks y librerías aprobadas
      * Bases de datos autorizadas
      * Plataformas de ejecución (OS, cloud)
      * Herramientas de desarrollo obligatorias
      
      **Ejemplo:**
      
      "El sistema debe usar Java 17 porque es el único lenguaje con soporte 
      corporativo aprobado y el equipo tiene 5 años de experiencia en él."

   restricción organizacional
   organizational constraint
      Restricción relacionada con **estructura, procesos o recursos** de la organización.
      
      Incluye limitaciones sobre:
      
      * Tamaño y composición del equipo
      * Disponibilidad de recursos (tiempo parcial, compartidos)
      * Metodologías obligatorias (Scrum, SAFe)
      * Procesos de aprobación
      * Dependencias de otros equipos
      
      **Ejemplo:**
      
      "El equipo de desarrollo está distribuido en 3 continentes (México, España, India),
      lo que limita las reuniones sincrónicas a 1 hora al día y requiere comunicación
      asíncrona y documentación exhaustiva."

   restricción política
   political constraint
      Restricción resultante de **decisiones de management o políticas corporativas**.
      
      No necesariamente técnicamente justificadas, pero **obligatorias** por 
      decisión de negocio.
      
      **Ejemplos típicos:**
      
      * Partnership con Microsoft → Todo debe ser en Azure + .NET
      * Decisión CEO: "Migrar todo a microservicios"
      * Política corporativa: "Cloud-first strategy"
      * Mandato CTO: "Solo tecnologías open-source"
      
      **Característica:** Frecuentemente no negociables al nivel del proyecto.

   convención
   convention
      Guía, estándar o práctica establecida que el equipo **debe seguir**.
      
      Tipos comunes:
      
      * **Programación:** Style guides (Google Java Style, PEP 8)
      * **Versionado:** Git Flow, Semantic Versioning
      * **Documentación:** arc42, OpenAPI, Markdown
      * **Nomenclatura:** CamelCase, snake_case, kebab-case
      * **Testing:** Code coverage mínimo, frameworks obligatorios
      
      **Diferencia con restricción:**
      
      * Convenciones son más **específicas** y a nivel de código/proceso
      * Restricciones son más **generales** y a nivel de arquitectura
      
      **Ejemplo:**
      
      "Convención: Todos los commits deben seguir Conventional Commits 
      (feat:, fix:, docs:, etc.) para generar CHANGELOG automático."

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
   * - constraints
     - limitaciones
     - **restricciones arquitectónicas**
   * - freedom of design
     - libertad de diseño
     - **libertad en decisiones de diseño**
   * - technical constraints
     - limitaciones técnicas
     - **restricciones técnicas**
   * - organizational constraints
     - limitaciones organizacionales
     - **restricciones organizacionales**
   * - political constraints
     - limitaciones políticas
     - **restricciones políticas**
   * - conventions
     - convenios
     - **convenciones**
   * - negotiable
     - negociable
     - **negociable** (OK)

**Razón:** En arquitectura de software, "constraint" tiene un significado 
específico de RESTRICCIÓN que LIMITA opciones, no simplemente una "limitación" genérica.

Diferenciación Crítica
----------------------

**Constraint vs Requirement:**

Esta es la diferenciación **MÁS IMPORTANTE** en esta sección:

```
constraint (restricción):
  → LIMITA tus opciones de diseño
  → Ejemplo: "Debes usar PostgreSQL"

requirement (requisito):
  → DEFINE lo que el sistema debe hacer
  → Ejemplo: "Sistema debe almacenar datos de usuarios"
```

**En español, ambos podrían traducirse como "requisito" literalmente, pero en 
arquitectura son conceptos DIFERENTES.**

Principios Aplicados
--------------------

✅ **Contexto arquitectónico primero**
   - "Constraint" = restricción que limita opciones
   - No es simplemente una "limitación" genérica

✅ **Términos técnicos preservados cuando apropiado**
   - convention → convención (traducción directa OK)
   - negotiable → negociable (traducción directa OK)

✅ **Explicación de diferencias sutiles**
   - Constraint vs requirement explicado con ejemplos
   - Convención vs restricción diferenciados

✅ **Ejemplos abundantes**
   - Restricciones técnicas (5+ ejemplos)
   - Restricciones organizacionales (4+ ejemplos)
   - Restricciones políticas (4+ ejemplos)
   - Convenciones (5+ categorías con ejemplos)

✅ **Estilo consistente**
   - Español mexicano informal (tú)
   - Voz activa
   - Ejemplos MALO vs BUENO
   - Admonitions apropiadas

Referencias Utilizadas
----------------------

* arc42.org - Documentación oficial Sección 2
* arc42 FAQ - Preguntas sobre constraints
* Hofmeister et al. - Software Architecture, A Practical Guide
* ISO/IEC/IEEE 42010:2011 - Architecture description

----

**Fuente:** https://docs.arc42.org/section-2/  
**Traducido:** 2026-01-25  
**Modo:** Traducción Arquitectónica Contextual (NO literal)  
**Framework:** ADT (Arc42-Diátaxis-Traducción) v1.0.0  
**Guía aplicada:** ADT_GUIA_TRADUCCION_ARQUITECTONICA.md  
**Sección:** 2 de 12

.. important::
   **Diferencias clave con traducción literal:**
   
   * "constraints" → "restricciones arquitectónicas" (NO "limitaciones")
   * Diferenciación constraint vs requirement explicada claramente
   * Ejemplos abundantes de cada tipo de restricción
   * Tips expandidos con casos MALO vs BUENO
   * Glosario completo de 5 términos
