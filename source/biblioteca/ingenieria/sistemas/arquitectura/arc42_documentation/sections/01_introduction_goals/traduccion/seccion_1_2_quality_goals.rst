.. meta::
 :subseccion: 1.2
 :titulo: Atributos de Calidad Objetivo
 :tipo: Plantilla arc42
 :version: 1.0.0
 :fecha: 2026-01-27

.. _seccion-1-2-quality-goals:

===================================================================
1.2 Atributos de Calidad Objetivo
===================================================================

Contenido
=========

Los tres (máximo cinco) atributos de calidad objetivo principales para la arquitectura
cuyo cumplimiento es de mayor importancia para los stakeholders principales.

Realmente nos referimos a atributos de calidad objetivo **para la arquitectura**.
No los confundas con objetivos del proyecto. No son necesariamente idénticos.

----

Modelo de Calidad ISO 25010
----------------------------

El estándar ISO 25010 proporciona una buena visión general de temas potenciales
de interés:

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/01-ISO-25010-EN.webp
 :alt: Categorías de requisitos de calidad según ISO 25010
 :align: center
 :width: 80%

 Categorías de requisitos de calidad según ISO 25010

----

Motivación
==========

Debes conocer los atributos de calidad objetivo de tus stakeholders más importantes,
ya que influirán en decisiones arquitectónicas fundamentales.

Asegúrate de ser muy concreto sobre estas cualidades, **evita palabras de moda**.

Si como arquitecto no sabes cómo se juzgará la calidad de tu trabajo...

----

Forma
=====

Una tabla con los atributos de calidad objetivo más importantes y escenarios concretos,
ordenados por prioridades.

Ver :ref:`seccion-10-requisitos-calidad` para una visión completa de escenarios de calidad.

----

Ejemplos
========

- :ref:`requisitos-calidad-ejemplo-1` - HTML Sanity Checker
- :ref:`requisitos-calidad-ejemplo-3` - Traffic Pursuit Unit

----

Plantilla
=========

.. code-block:: rst

 1.2 Atributos de Calidad Objetivo
 ==================================

 .. list-table:: Top-3 Atributos de Calidad Objetivo
 :header-rows: 1
 :widths: 10 20 70

 * - Prioridad
   - Atributo de Calidad
 - Escenario / Descripción
 * - 1
   - [Ej: Performance]
 - [Escenario concreto: El sistema debe procesar 1000 transacciones
 por segundo con un tiempo de respuesta < 2 segundos]
 * - 2
   - [Ej: Disponibilidad]
 - [Escenario concreto: El sistema debe tener 99.9% uptime,
 permitiendo máximo 8.76 horas de inactividad al año]
 * - 3
   - [Ej: Mantenibilidad]
 - [Escenario concreto: Un desarrollador experimentado puede
 implementar cambios funcionales típicos en < 4 horas]

----

Atributos de Calidad Comunes
=============================

Algunos atributos de calidad típicos (según ISO 25010):

**Características del Producto:**

- **Adecuación funcional** (Functional suitability)

 - Completitud funcional
 - Corrección funcional
 - Pertinencia funcional

- **Eficiencia de desempeño** (Performance efficiency)

 - Comportamiento temporal (tiempo de respuesta)
 - Utilización de recursos
 - Capacidad

- **Compatibilidad** (Compatibility)

 - Coexistencia
 - Interoperabilidad

- **Usabilidad** (Usability)

 - Reconocibilidad de adecuación
 - Capacidad de aprendizaje
 - Operabilidad
 - Protección contra errores de usuario
 - Estética de interfaz de usuario
 - Accesibilidad

- **Confiabilidad** (Reliability)

 - Madurez
 - Disponibilidad
 - Tolerancia a fallos
 - Recuperabilidad

- **Seguridad** (Security)

 - Confidencialidad
 - Integridad
 - No repudio
 - Responsabilidad (accountability)
 - Autenticidad

- **Mantenibilidad** (Maintainability)

 - Modularidad
 - Reusabilidad
 - Analizabilidad
 - Modificabilidad
 - Testeabilidad

- **Portabilidad** (Portability)

 - Adaptabilidad
 - Instalabilidad
 - Reemplazabilidad

----

Tips Relacionados
=================

Ver:

- :ref:`introduccion-tip-11` - Requisitos de calidad explícitos
- :ref:`introduccion-tip-12` - Escenarios de calidad
- :ref:`introduccion-tip-13` - Suposiciones explícitas
- :ref:`introduccion-tip-14` - Checklists ISO 25010
- :ref:`introduccion-tip-15` - Ejemplos con stakeholders
- :ref:`introduccion-tip-16` - Top 3-5 atributos
- :ref:`introduccion-tip-17` - Combina con estrategia
- :ref:`introduccion-tip-18` - Difiere a sección 10
- :ref:`introduccion-tip-24` - Modelo de calidad arc42

----

.. important::
 **Reglas clave para Quality Goals:**

 1. **Máximo 3-5 atributos** (mantén el foco)
 2. **Especificidad** (evita "el sistema debe ser rápido")
 3. **Medibilidad** (incluye métricas concretas)
 4. **Escenarios** (describe situaciones específicas)
 5. **Priorización** (ordena por importancia)

----

.. note::
 **Información de traducción:**

 - Subsección arc42: 1.2 Quality Goals
 - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
 - Paso 3.4 aplicado: "quality goals" -> "atributos de calidad objetivo"
 (NO "objetivos de calidad")
 - Referencia: ISO/IEC 25010:2011 Software Quality Model
 - Fecha: 2026-01-27
