.. _md_traducir_vs_conservar:

===============================================
MD-004: Traducir vs Conservar Término
===============================================

:Tipo: Matriz de Decisión
:Código: MD-004
:Prioridad: CRÍTICA
:Aplicabilidad: Toda traducción ADT
:Base: Decisiones terminológicas en 196 archivos arc42

.. contents:: Contenido
 :depth: 3
 :local:

----

Pregunta de Decisión
====================

**Pregunta:**
 ¿Debo traducir este término técnico al español o conservarlo en inglés?

**Importancia:**
 La decisión incorrecta puede:

 [ERROR] **Traducir término establecido** -> Confusión, búsquedas fallidas
 [ERROR] **Conservar término traducible** -> Texto híbrido innecesario

**Objetivo:**
 Proveer criterios objetivos basados en 196 archivos de arc42 donde se mantuvo 100% consistencia terminológica.

----

Árbol de Decisión
=================

**Proceso paso a paso:**

.. code-block:: text

 ¿Es término técnico establecido?
 |
 +- SÍ -> ¿Tiene traducción oficial en español?
 | |
 | +- SÍ -> ¿Es ampliamente usada la traducción?
 | | |
 | | +- SÍ -> TRADUCIR
 | | | Ejemplo: "Risk" -> "Riesgo"
 | | |
 | | +- NO -> CONSERVAR + opcional nota al pie
 | | Ejemplo: "Stakeholder" -> "Stakeholder"
 | |
 | +- NO -> CONSERVAR
 | Ejemplo: "ATAM" -> "ATAM"
 |
 +- NO -> TRADUCIR
 Ejemplo: "Quality" -> "Calidad"

----

Categorías de Términos
======================

Categoría 1: SIEMPRE CONSERVAR
-------------------------------

**1.1 Acrónimos Técnicos**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Decisión**
   - **Razón**
 * - API
   - API
   - Acrónimo universal
 * - REST
   - REST
   - Estilo arquitectónico estándar
 * - JSON
   - JSON
   - Formato de datos
 * - XML
   - XML
   - Formato de datos
 * - HTTP
   - HTTP
   - Protocolo
 * - SQL
   - SQL
   - Lenguaje de consulta
 * - UML
   - UML
   - Lenguaje de modelado
 * - URL
   - URL
   - Acrónimo técnico

**Justificación:**

.. code-block:: text

 - Búsqueda en Google: Se busca "API", no "Interfaz de Programación de Aplicaciones"
 - Documentación técnica: Siempre usa acrónimos
 - Comunicación profesional: "REST API" no "API REST de Transferencia de Estado Representacional"
 - Reconocimiento: Inmediato en acrónimo, confuso en traducción

**Uso en arc42:** 100% conservados (0 variaciones)

**1.2 Nombres de Patrones de Diseño**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Decisión**
   - **Razón**
 * - Singleton
   - Singleton
   - Patrón GoF establecido
 * - Factory
   - Factory
   - Patrón de creación
 * - Observer
   - Observer
   - Patrón de comportamiento
 * - Strategy
   - Strategy
   - Patrón de comportamiento
 * - Adapter
   - Adapter
   - Patrón estructural
 * - Facade
   - Facade
   - Patrón estructural
 * - Circuit Breaker
   - Circuit Breaker
   - Patrón resiliencia

**Justificación:**

.. code-block:: text

 - Libros de referencia: Gang of Four usa nombres en inglés
 - Código fuente: Clases se llaman "SingletonFactory", no "FábricaÚnica"
 - Discusión técnica: "Implementamos un Singleton" [OK] vs "Implementamos un Único" [ERROR]
 - Documentación: Toda literatura técnica usa inglés

**Uso en arc42:** 100% conservados

**1.3 Nombres de Metodologías**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Decisión**
   - **Razón**
 * - Scrum
   - Scrum
   - Metodología ágil
 * - Kanban
   - Kanban
   - Sistema de gestión
 * - ATAM
   - ATAM
   - Método de evaluación
 * - SAFe
   - SAFe
   - Framework escalado
 * - DevOps
   - DevOps
   - Cultura y práctica
 * - Agile
   - Agile (o Ágil)
   - Metodología (caso especial)

**Justificación:**

.. code-block:: text

 - Certificaciones: "Certified Scrum Master", no "Maestro Scrum Certificado"
 - Formación: Cursos se llaman "Scrum Training"
 - Comunidad: Eventos "Scrum Gathering", artículos "Scrum Guide"
 - Búsqueda: "Scrum" tiene 10x más resultados que "Melé" (traducción española)

**Uso en arc42:** 100% conservados

**Caso Especial - "Agile":**

.. code-block:: text

 Decisión en arc42: "Agile" (conservado)

 Alternativa válida: "Ágil" (traducción ampliamente usada)

 Criterio:
 - Si contexto es metodología formal -> "Agile"
 - Si contexto es adjetivo general -> "ágil"

 Ejemplos:
 [OK] "Metodología Agile" (nombre formal)
 [OK] "Desarrollo ágil" (adjetivo descriptivo)

**1.4 Roles Establecidos**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Decisión**
   - **Razón**
 * - Product Owner
   - Product Owner
   - Rol Scrum oficial
 * - Scrum Master
   - Scrum Master
   - Rol Scrum oficial
 * - Stakeholder
   - Stakeholder
   - Término universal PM
 * - DevOps Engineer
   - DevOps Engineer
   - Rol técnico moderno

**Justificación:**

.. code-block:: text

 - Títulos de trabajo: LinkedIn usa "Product Owner", no "Dueño de Producto"
 - Comunicación: En reuniones se dice "El Product Owner decide"
 - Guías oficiales: Scrum Guide define "Product Owner" en inglés
 - Búsqueda de empleo: Ofertas buscan "Product Owner"

**Uso en arc42:** 100% conservados

**1.5 Conceptos Arquitectónicos Específicos**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Decisión**
   - **Razón**
 * - Microservicio
   - Microservicio
   - Estilo arquitectónico
 * - Runtime
   - Runtime
   - Entorno de ejecución
 * - Deployment
   - Deployment
   - Proceso de despliegue
 * - Whitebox
   - Whitebox
   - Vista de caja blanca
 * - Blackbox
   - Blackbox
   - Vista de caja negra

**Nota sobre "Runtime":**

.. code-block:: text

 Decisión en arc42: "Runtime" (conservado)

 Razón:
 - "Runtime View" es nombre formal de sección arc42
 - "Tiempo de ejecución" es muy largo
 - "Runtime" es término establecido (.NET Runtime, Java Runtime)
 - Traducir sería inconsistente con industria

 Uso: "Vista de Runtime" [OK]

**Nota sobre "Deployment":**

.. code-block:: text

 Decisión en arc42: "Deployment" conservado en algunos contextos

 Contextos:
 - "Deployment View" -> "Vista de Despliegue" (título de sección)
 - "Deployment pipeline" -> "Pipeline de deployment"
 - "Deployment unit" -> "Unidad de deployment"

 Regla: Traducir en títulos formales, conservar en términos técnicos compuestos

----

Categoría 2: SIEMPRE TRADUCIR
------------------------------

**2.1 Conceptos Generales**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Traducción**
   - **Razón**
 * - Quality
   - Calidad
   - Concepto general
 * - Risk
   - Riesgo
   - Concepto general
 * - Goal
   - Objetivo
   - Concepto general
 * - Requirement
   - Requisito
   - Concepto general
 * - Decision
   - Decisión
   - Concepto general
 * - Constraint
   - Restricción
   - Concepto general

**Justificación:**

.. code-block:: text

 - No son términos técnicos específicos
 - Tienen traducción estándar en español
 - Usar inglés sería afectación innecesaria
 - Lectores hispanohablantes esperan español

**Uso en arc42:** 100% traducidos (0 variaciones)

**2.2 Verbos y Acciones**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Traducción**
   - **Razón**
 * - Implement
   - Implementar
   - Verbo común
 * - Design
   - Diseñar
   - Verbo común
 * - Test
   - Probar/Testear
   - Verbo común
 * - Deploy
   - Desplegar
   - Verbo común
 * - Document
   - Documentar
   - Verbo común
 * - Validate
   - Validar
   - Verbo común

**Justificación:**

.. code-block:: text

 - Son acciones, no términos técnicos
 - Traducción natural y clara
 - Conservar sería híbrido innecesario

**2.3 Adjetivos Descriptivos**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Traducción**
   - **Razón**
 * - Complex
   - Complejo
   - Adjetivo común
 * - Simple
   - Simple
   - Adjetivo común
 * - Critical
   - Crítico
   - Adjetivo común
 * - Optional
   - Opcional
   - Adjetivo común
 * - Required
   - Requerido
   - Adjetivo común
 * - Important
   - Importante
   - Adjetivo común

**2.4 Términos con Traducción Estándar ISO**

.. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - **Término**
   - **Traducción**
   - **Razón**
 * - Technical Debt
   - Deuda Técnica
   - Traducción ISO 25010
 * - Quality Attribute
   - Atributo de Calidad
   - Terminología ISO
 * - Building Block
   - Bloque de Construcción
   - Traducción establecida
 * - Glossary
   - Glosario
   - Traducción estándar

**Uso en arc42:** 100% traducidos consistentemente

----

Categoría 3: CASO POR CASO
---------------------------

**3.1 Términos Compuestos**

**Regla General:**

.. code-block:: text

 Si el término compuesto es nombre formal -> CONSERVAR
 Si es descripción técnica -> MEZCLAR apropiadamente

 Ejemplos:
 [OK] "Building Block View" -> "Vista de Bloques de Construcción" (título formal)
 [OK] "Runtime View" -> "Vista de Runtime" (término técnico + contexto)
 [OK] "Cross-cutting Concept" -> "Concepto Transversal" (traducible)

**Decisiones Reales de arc42:**

.. list-table::
 :header-rows: 1
 :widths: 40 35 25

 * - **Original**
   - **Decisión arc42**
   - **Razón**
 * - Building Block View
   - Vista de Bloques de Construcción
   - Título sección, traducible
 * - Runtime View
   - Vista de Runtime
   - "Runtime" técnico
 * - Deployment View
   - Vista de Despliegue
   - Título formal
 * - Context and Scope
   - Contexto y Alcance
   - Totalmente traducible
 * - Quality Requirements
   - Requisitos de Calidad
   - Totalmente traducible
 * - Crosscutting Concepts
   - Conceptos Transversales
   - Totalmente traducible
 * - Architecture Decisions
   - Decisiones Arquitectónicas
   - Totalmente traducible

**3.2 Neologismos Recientes**

**Criterio:**

.. code-block:: text

 ¿El término tiene < 5 años?
 ¿No hay consenso en traducción?

 -> CONSERVAR hasta que se establezca traducción

 Ejemplos actuales:
 - "Container" -> Container (no "Contenedor")
 - "Serverless" -> Serverless (no "Sin servidor")
 - "Edge Computing" -> Edge Computing

**Razón:**

.. code-block:: text

 - Traducción prematura puede quedar obsoleta
 - Comunidad puede adoptar término diferente
 - Búsqueda y comunicación más fácil en inglés
 - Esperar a que se establezca traducción estándar

**3.3 Términos con Múltiples Acepciones**

**Ejemplo: "View"**

.. code-block:: text

 Contexto 1: "Building Block View"
 -> "Vista" (perspectiva arquitectónica)

 Contexto 2: "Database view"
 -> "Vista" (objeto SQL)

 Contexto 3: "Point of view"
 -> "Punto de vista" (opinión)

 Decisión: TRADUCIR pero atender al contexto

**Ejemplo: "Model"**

.. code-block:: text

 Contexto 1: "Data model"
 -> "Modelo de datos"

 Contexto 2: "Business model"
 -> "Modelo de negocio"

 Contexto 3: "Model-View-Controller"
 -> "MVC" (acrónimo conservado)

 Decisión: DEPENDE del contexto

----

Verificación de Decisión
=========================

**Checklist antes de decidir:**

.. code-block:: text

 [ ] 1. ¿Es acrónimo técnico?
 SÍ -> CONSERVAR
 NO -> Continuar

 [ ] 2. ¿Es nombre de patrón/metodología?
 SÍ -> CONSERVAR
 NO -> Continuar

 [ ] 3. ¿Es rol establecido?
 SÍ -> CONSERVAR
 NO -> Continuar

 [ ] 4. ¿Tiene traducción ISO/estándar?
 SÍ -> TRADUCIR
 NO -> Continuar

 [ ] 5. ¿Es concepto general/verbo/adjetivo?
 SÍ -> TRADUCIR
 NO -> Continuar

 [ ] 6. ¿Es neologismo reciente sin consenso?
 SÍ -> CONSERVAR
 NO -> Evaluar caso por caso

**Prueba de Búsqueda Google:**

.. code-block:: text

 1. Buscar término en inglés: "TÉRMINO"
 2. Buscar posible traducción: "traducción"
 3. Comparar resultados técnicos

 Si inglés >> español (10x+ resultados) -> CONSERVAR
 Si español ≈ inglés -> TRADUCIR

 Ejemplo:
 "Stakeholder": 2,450,000,000 resultados
 "Interesado" (contexto PM): 45,000,000 resultados
 Ratio: 54x -> CONSERVAR "Stakeholder" [OK]

----

Tabla de Referencia Rápida
===========================

**Términos Comunes en Documentación Técnica:**

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Término**
   - **Categoría**
   - **Decisión**
   - **arc42**
 * - API
   - Acrónimo
   - API
   - [OK]
 * - Stakeholder
   - Rol
   - Stakeholder
   - [OK]
 * - Quality
   - Concepto
   - Calidad
   - [OK]
 * - Risk
   - Concepto
   - Riesgo
   - [OK]
 * - Building Block
   - Término arc42
   - Bloque de Construcción
   - [OK]
 * - Runtime
   - Técnico
   - Runtime
   - [OK]
 * - Deployment
   - Mixto
   - Despliegue/Deployment
   - [OK]
 * - Microservicio
   - Estilo arqui.
   - Microservicio
   - [OK]
 * - ATAM
   - Metodología
   - ATAM
   - [OK]
 * - Product Owner
   - Rol
   - Product Owner
   - [OK]
 * - Technical Debt
   - ISO
   - Deuda Técnica
   - [OK]
 * - Circuit Breaker
   - Patrón
   - Circuit Breaker
   - [OK]
 * - Glossary
   - Concepto
   - Glosario
   - [OK]

----

Casos de Uso de la Matriz
==========================

Caso 1: Traduciendo Título de Sección
--------------------------------------

**Escenario:**
 Estás traduciendo "5. Building Block View"

**Decisión:**

.. code-block:: text

 PASO 1: Analizar cada término

 "Building Block":
 [ ] ¿Acrónimo? NO
 [ ] ¿Patrón? NO
 [ ] ¿Rol? NO
 [ ] ¿ISO/estándar? SÍ (término arc42 establecido)

 -> TRADUCIR: "Bloque de Construcción"

 "View":
 [ ] Contexto: Vista arquitectónica
 [ ] Traducible: SÍ

 -> TRADUCIR: "Vista"

 RESULTADO: "5. Vista de Bloques de Construcción" [OK]

Caso 2: Párrafo con Términos Mixtos
------------------------------------

**Original:**

.. code-block:: text

 "The Product Owner defines quality requirements for the
 building blocks using ATAM methodology."

**Análisis término por término:**

.. code-block:: text

 "Product Owner": Rol -> CONSERVAR
 "quality": Concepto -> TRADUCIR ("calidad")
 "requirements": Concepto -> TRADUCIR ("requisitos")
 "building blocks": Término arc42 -> TRADUCIR ("bloques de construcción")
 "ATAM": Metodología -> CONSERVAR
 "methodology": Concepto -> TRADUCIR ("metodología")

**Traducción:**

.. code-block:: text

 "El Product Owner define los requisitos de calidad para los
 bloques de construcción usando la metodología ATAM." [OK]

Caso 3: Código con Comentarios
-------------------------------

**Original:**

.. code-block:: python

 # Singleton pattern implementation
 class ConfigurationManager:
 """Manages application configuration using Singleton pattern"""

**Decisión:**

.. code-block:: text

 En código:
 - Nombres de clases -> CONSERVAR inglés (convención)
 - Comentarios -> TRADUCIR
 - Términos técnicos en docstring -> CONSERVAR

 Traducción comentarios:
 # Implementación del patrón Singleton [OK]

 Docstring:
 """Gestiona la configuración de la aplicación usando el patrón Singleton""" [OK]

 Nota: "Singleton" conservado porque es nombre de patrón

----

Errores Comunes
===============

Error 1: Traducir Todo Literalmente
------------------------------------

**Incorrecto:**

.. code-block:: text

 [ERROR] "El Maestro Melé revisa el Backlog del Producto"

 Problemas:
 - "Scrum Master" -> "Maestro Melé" (ridículo)
 - "Product Backlog" -> "Backlog del Producto" (híbrido raro)

**Correcto:**

.. code-block:: text

 [OK] "El Scrum Master revisa el Product Backlog"

 Razón:
 - Términos establecidos conservados
 - Comunicación clara
 - Alineado con industria

Error 2: Conservar Todo en Inglés
----------------------------------

**Incorrecto:**

.. code-block:: text

 [ERROR] "The quality requirements define the constraints for the system"

 Problema:
 - Texto completamente en inglés
 - No es traducción

**Correcto:**

.. code-block:: text

 [OK] "Los requisitos de calidad definen las restricciones para el sistema"

 Razón:
 - Términos generales traducidos
 - Español natural

Error 3: Inconsistencia
-----------------------

**Incorrecto:**

.. code-block:: text

 Página 1: "El Stakeholder define..."
 Página 2: "El Interesado define..."
 Página 3: "La Parte Interesada define..."

 [ERROR] 3 traducciones diferentes del mismo término

**Correcto:**

.. code-block:: text

 SIEMPRE: "El Stakeholder define..."

 [OK] Consistencia 100%

----

Mantenimiento del Glosario
===========================

**Crear Glosario de Decisiones:**

.. code-block:: text

 Archivo: GLOSARIO_TERMINOLOGIA.md

 | Término Original | Decisión | Razón | Sección |
 |-----------------|----------|-------|---------|
 | Stakeholder | Conservar | Rol establecido | Todas |
 | Quality | Traducir -> Calidad | Concepto general | Todas |
 | Building Block | Traducir -> Bloque | Término arc42 | 5 |
 | ATAM | Conservar | Metodología | 10 |
 ...

**Actualizar con Cada Decisión:**

.. code-block:: text

 1. Nueva decisión tomada
 2. Agregar a glosario
 3. Verificar consistencia con decisiones previas
 4. Buscar y reemplazar si hay inconsistencia

----

Resumen Ejecutivo
=================

**Reglas Fundamentales:**

1. **SIEMPRE CONSERVAR:**
 - Acrónimos técnicos (API, REST, JSON)
 - Nombres de patrones (Singleton, Observer)
 - Metodologías (Scrum, ATAM, SAFe)
 - Roles establecidos (Product Owner, Stakeholder)

2. **SIEMPRE TRADUCIR:**
 - Conceptos generales (calidad, riesgo)
 - Verbos y acciones (implementar, diseñar)
 - Adjetivos (complejo, crítico)
 - Términos con traducción ISO

3. **CASO POR CASO:**
 - Términos compuestos (evaluar cada parte)
 - Neologismos recientes (esperar consenso)
 - Múltiples acepciones (según contexto)

**Verificación:**
 [OK] Consistencia 100% en 196 archivos de arc42
 [OK] 0 variaciones en términos clave
 [OK] Comunicación clara y profesional

----

.. seealso::
 * :doc:`MD_002_cuando_enriquecer` - Cuánto enriquecer
 * :doc:`../../03_estandares/calidad/criterios_calidad` - Criterio de precisión técnica
 * :doc:`../../01_fundamentos/glosario_traduccion` - Glosario fundamental

.. note::
 Estas decisiones están basadas en 196 archivos de arc42 donde se logró 100% consistencia terminológica. Actualizar glosario con cada proyecto.
