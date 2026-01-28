.. meta::
   :descripcion: Sección 1 de arc42 - Introducción y Objetivos
   :fuente: https://docs.arc42.org/section-1/
   :traducido: 2026-01-25
   :idioma: es-MX
   :modo: Traducción Arquitectónica Contextual (NO literal)
   :framework: ADT v1.0.0

===============================================
1 - Introducción y Objetivos
===============================================

.. contents:: Contenido
   :depth: 3
   :local:

----

Propósito de esta Sección
==========================

Esta sección describe los requisitos relevantes y los **factores determinantes** 
que deben considerar los :term:`arquitectos de software <arquitecto de software>` 
y el equipo de desarrollo.

.. note::
   **Traducción contextual:** "driving forces" en arquitectura se traduce como 
   "factores determinantes" - son los factores que impulsan y moldean las 
   decisiones arquitectónicas, NO simplemente "fuerzas impulsoras".

Estos factores incluyen:

* **Objetivos de negocio subyacentes:** Las metas del negocio que el sistema debe soportar
* **Características esenciales:** Funcionalidades clave y requisitos funcionales del sistema
* **Atributos de calidad objetivo:** Los :term:`quality goals <quality goal>` que la arquitectura debe satisfacer
* **Stakeholders relevantes:** Las personas, roles y organizaciones interesadas, junto con sus expectativas

----

1.1 Vista General de Requisitos
================================

Contenido
---------

Descripción breve de los requisitos funcionales, los factores determinantes, 
y un extracto (o resumen) de los requisitos del sistema.

Esta sección debe incluir enlaces a los documentos de requisitos existentes, 
con información clara sobre dónde encontrarlos.

Motivación
----------

Desde la perspectiva de los usuarios finales, un sistema se crea o modifica para:

* Mejorar el soporte de una actividad de negocio
* Mejorar la calidad del servicio o producto

El sistema existe para resolver problemas reales del negocio.

Forma
-----

Descripción textual breve, preferiblemente en formato tabular de :term:`casos de uso <caso de uso>`.

.. important::
   Si existen documentos de requisitos formales, esta vista general debe 
   referenciarlos claramente.

**Principios para esta sección:**

* Mantén los extractos lo más breves posible
* Balancea la legibilidad con la potencial redundancia respecto a los documentos formales de requisitos
* No dupliques contenido innecesariamente

Ejemplos
--------

Ver ejemplos completos en:

* `Overview Example: Traffic Pursuit Unit <https://docs.arc42.org/examples/overview-example-3/>`_
* `Overview Example: HTML Sanity Checker <https://docs.arc42.org/examples/overview-example-htmlsc-1/>`_

.. admonition:: Plantilla
   :class: note
   
   *<insertar vista general de requisitos aquí>*

----

1.2 Atributos de Calidad Objetivo (Quality Goals)
==================================================

Contenido
---------

Los **tres a cinco atributos de calidad principales** que la arquitectura debe 
satisfacer, según las prioridades de los :term:`stakeholders <stakeholder>` más importantes.

.. warning::
   **Importante:** Estos son atributos de calidad de la **ARQUITECTURA**, 
   no del proyecto. No confundas quality goals arquitectónicos con objetivos 
   del proyecto - no son necesariamente idénticos.

El estándar ISO 25010 proporciona una taxonomía completa de atributos de calidad:

Categorías de Calidad según ISO 25010
--------------------------------------

.. figure:: https://docs.arc42.org/images/1-2-iso-25010-topics-en.png
   :alt: Categorías ISO 25010 de atributos de calidad
   :align: center
   :width: 85%
   
   Taxonomía de atributos de calidad según ISO/IEC 25010

**Categorías principales de ISO 25010:**

1. **Functional Suitability** (Idoneidad Funcional)
   - Completitud funcional
   - Corrección funcional
   - Pertinencia funcional

2. **Performance Efficiency** (Eficiencia de Desempeño)
   - Comportamiento temporal
   - Utilización de recursos
   - Capacidad

3. **Compatibility** (Compatibilidad)
   - Coexistencia
   - Interoperabilidad

4. **Usability** (Usabilidad)
   - Reconocibilidad
   - Aprendizaje
   - Operabilidad
   - Protección contra errores de usuario
   - Estética de interfaz
   - Accesibilidad

5. **Reliability** (Confiabilidad)
   - Madurez
   - Disponibilidad
   - Tolerancia a fallos
   - Recuperabilidad

6. **Security** (Seguridad)
   - Confidencialidad
   - Integridad
   - No repudio
   - Responsabilidad
   - Autenticidad

7. **Maintainability** (Mantenibilidad)
   - Modularidad
   - Reusabilidad
   - Analizabilidad
   - Modificabilidad
   - Facilidad de pruebas

8. **Portability** (Portabilidad)
   - Adaptabilidad
   - Instalabilidad
   - Reemplazabilidad

Motivación
----------

Debes conocer los atributos de calidad objetivo de tus stakeholders más importantes, 
ya que estos **influenciarán directamente las decisiones arquitectónicas fundamentales**.

.. danger::
   **Crítico:** Asegúrate de ser muy **concreto y específico** sobre estos 
   atributos de calidad.
   
   * ❌ **Evita buzzwords** vagos como "el sistema debe ser rápido"
   * ✅ **Sé específico:** "Tiempo de respuesta < 2 segundos para el 95% de las transacciones"

Si como arquitecto no sabes cómo se juzgará la calidad de tu trabajo, 
¿cómo puedes tomar decisiones informadas?

Forma
-----

Una tabla con los atributos de calidad más importantes y :term:`escenarios concretos <escenario de calidad>`, 
ordenados por prioridad.

.. tip::
   Ver :doc:`/section-10/index` (Requisitos de Calidad) para una vista 
   completa de escenarios de calidad y cómo documentarlos.

Ejemplos
--------

Ver ejemplos completos de escenarios de calidad:

* `Example Quality Scenarios: HTML Sanity Checker <https://docs.arc42.org/examples/quality-htmlsc-2/>`_
* `Example Quality Scenarios: TrafficPursuitUnit <https://docs.arc42.org/examples/quality-tpu-1/>`_

.. admonition:: Plantilla
   :class: note
   
   .. list-table:: Atributos de Calidad Objetivo
      :widths: 20 40 40
      :header-rows: 1
   
      * - Prioridad
        - Atributo de Calidad
        - Escenario Concreto
      * - 1
        - *<atributo>*
        - *<escenario medible>*
      * - 2
        - *<atributo>*
        - *<escenario medible>*
      * - 3
        - *<atributo>*
        - *<escenario medible>*

----

1.3 Stakeholders
================

Contenido
---------

Vista general explícita de los :term:`stakeholders <stakeholder>` del sistema, 
es decir, todas las personas, roles u organizaciones que:

* **Deben conocer** la arquitectura
* **Tienen que estar convencidos** de que la arquitectura es adecuada
* **Tienen que trabajar** con la arquitectura o con el código
* **Necesitan la documentación** de la arquitectura para realizar su trabajo
* **Tienen que tomar decisiones** sobre el sistema o su desarrollo

Motivación
----------

Debes conocer a **todas las partes involucradas** en el desarrollo del sistema 
o **afectadas por el sistema**.

.. warning::
   **Si no identificas correctamente a tus stakeholders, podrías encontrarte 
   con sorpresas desagradables más adelante en el proceso de desarrollo.**

Estos stakeholders determinan:

* El **alcance** (scope) de tu trabajo
* El **nivel de detalle** requerido en la documentación
* Las **prioridades** y decisiones arquitectónicas

Forma
-----

Tabla con nombres de roles, nombres de personas (cuando sean conocidos), 
y sus expectativas respecto a la arquitectura y su documentación.

Plantilla de Tabla de Stakeholders
-----------------------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Rol / Nombre
     - Contacto
     - Expectativas
   * - *Ejemplo: Product Owner*
     - *nombre@empresa.com*
     - *Arquitectura que permita entregas incrementales cada 2 semanas*
   * - *Ejemplo: Equipo de Desarrollo*
     - *equipo-dev@empresa.com*
     - *Documentación clara de componentes y sus interfaces*
   * - *Ejemplo: Equipo de Operaciones*
     - *ops@empresa.com*
     - *Sistema desplegable con Docker, métricas observables*
   * - *<rol>*
     - *<contacto>*
     - *<expectativas>*

.. tip::
   **Consejo práctico:** No todos los stakeholders tienen la misma importancia 
   o influencia. Considera clasificarlos usando una matriz de poder/interés.

----

Recursos Adicionales
====================

Tips Relacionados (24 total)
-----------------------------

arc42 proporciona 24 tips específicos para esta sección. A continuación, 
los más relevantes organizados por tema:

**Requisitos Funcionales (Tips 1-1 a 1-10)**

.. admonition:: Tip 1-1
   :class: tip
   
   **¡Da un resumen compacto de requisitos y factores determinantes!**
   
   No abrumes con detalles - enfócate en lo esencial que guía la arquitectura.
   
   Tags: :badge:`requirement`

.. admonition:: Tip 1-2
   :class: tip
   
   **¡Limítate a las tareas y casos de uso esenciales!**
   
   Documenta solo lo que realmente importa para decisiones arquitectónicas.
   
   Tags: :badge:`requirement`

.. admonition:: Tip 1-3
   :class: tip
   
   **¡Resalta los objetivos de negocio del sistema!**
   
   La arquitectura existe para servir al negocio - hazlo explícito.
   
   Tags: :badge:`requirement` :badge:`goal`

.. admonition:: Tip 1-6
   :class: tip
   
   **¡Usa diagramas de actividad para describir requisitos funcionales!**
   
   Los flujos visuales comunican mejor que texto largo.
   
   Tags: :badge:`requirement` :badge:`activity-diagram`

.. admonition:: Tip 1-7
   :class: tip
   
   **¡Usa diagramas BPMN para describir requisitos funcionales!**
   
   Especialmente útil cuando hay procesos de negocio complejos.
   
   Tags: :badge:`requirement` :badge:`bpmn`

**Atributos de Calidad (Tips 1-11 a 1-18)**

.. admonition:: Tip 1-11
   :class: tip
   
   **¡Trabaja siempre con requisitos de calidad explícitos!**
   
   Los atributos de calidad vagos conducen a arquitecturas vagas.
   
   Tags: :badge:`requirement` :badge:`quality` :badge:`essential`

.. admonition:: Tip 1-12
   :class: tip
   
   **¡Explica requisitos de calidad mediante escenarios!**
   
   Un escenario vale más que mil adjetivos vagos.
   
   **Ejemplo:** En lugar de "el sistema debe ser rápido", especifica:
   "El sistema debe procesar 1000 transacciones/segundo con latencia < 100ms (p95)."
   
   Tags: :badge:`requirement` :badge:`quality` :badge:`scenario` :badge:`essential`

.. admonition:: Tip 1-13
   :class: tip
   
   **¡Si no obtienes requisitos de calidad, haz tus supuestos *explícitos*!**
   
   Es mejor documentar supuestos que trabajar con ambigüedad.
   
   Tags: :badge:`requirement` :badge:`quality` :badge:`assumption`

.. admonition:: Tip 1-16
   :class: tip
   
   **¡Describe solo los 3-5 atributos de calidad principales en la introducción!**
   
   Guarda los detalles completos para la Sección 10.
   
   Tags: :badge:`requirement` :badge:`quality` :badge:`lean` :badge:`quality-goal`

.. admonition:: Tip 1-18
   :class: tip
   
   **¡Difiere requisitos de calidad detallados y completos a la sección 10 de arc42!**
   
   La Sección 1 es para los atributos principales. La Sección 10 para el análisis completo.
   
   Tags: :badge:`requirement` :badge:`quality-goal` :badge:`thorough`

**Stakeholders (Tips 1-19 a 1-24)**

.. admonition:: Tip 1-19
   :class: tip
   
   **¡Busca stakeholders ampliamente!**
   
   Los stakeholders ocultos causan problemas tarde en el proyecto.
   
   Tags: :badge:`requirement` :badge:`stakeholder` :badge:`essential`

.. admonition:: Tip 1-20
   :class: tip
   
   **¡Describe las expectativas de los stakeholders!**
   
   No solo nombres - documenta qué esperan de la arquitectura.
   
   Tags: :badge:`requirement` :badge:`stakeholder` :badge:`essential`

.. admonition:: Tip 1-21
   :class: tip
   
   **¡Mantén una tabla de stakeholders!**
   
   Una tabla simple y clara es mejor que documentación narrativa confusa.
   
   Tags: :badge:`stakeholder` :badge:`essential` :badge:`thorough`

.. admonition:: Tip 1-24
   :class: tip
   
   **¡Aprovecha el arc42 Quality Model (open-source) y sus ejemplos!**
   
   No reinventes la rueda - usa recursos probados.
   
   Tags: :badge:`requirement` :badge:`quality` :badge:`scenario`

.. note::
   **Tips completos:** Hay 24 tips en total para esta sección. 
   Consulta https://docs.arc42.org/section-1/ para ver todos los tips con 
   explicaciones detalladas.

Preguntas Frecuentes
--------------------

Ver `preguntas relacionadas con introducción, objetivos y requisitos <https://faq.arc42.org/category_c/#c-sec-1>`_ 
en el FAQ oficial de arc42.

----

Glosario de Términos
====================

.. glossary::
   :sorted:

   arquitecto de software
      Persona responsable de diseñar, documentar y comunicar la arquitectura 
      de un sistema de software. Define decisiones técnicas clave que afectan 
      a múltiples componentes del sistema.
      
      **Responsabilidades típicas:**
      - Decisiones arquitectónicas fundamentales
      - Documentación arquitectónica
      - Comunicación con stakeholders
      - Evaluación de trade-offs técnicos

   stakeholder
      Persona, rol u organización que tiene interés, influencia o es afectada 
      por el sistema y su arquitectura.
      
      **Tipos comunes:**
      - Product Owners y gerentes de producto
      - Equipos de desarrollo
      - Equipos de operaciones (DevOps)
      - Usuarios finales
      - Clientes y sponsors del proyecto
      - Auditores y compliance
      - Equipos de seguridad
      
      **Nota:** Este término se preserva en inglés por ser estándar internacional 
      en gestión de proyectos y arquitectura de software.

   quality goal
   atributo de calidad objetivo
      Atributo de calidad que la arquitectura debe exhibir y que es de alta 
      prioridad para los stakeholders principales.
      
      Los quality goals deben ser:
      
      * **Específicos:** No vagos o ambiguos
      * **Medibles:** Con métricas claras
      * **Priorizados:** Ordenados por importancia
      * **Concretos:** Expresados como escenarios
      
      **Ejemplo MALO:** "El sistema debe ser rápido"  
      **Ejemplo BUENO:** "El sistema debe responder en < 2 segundos para el 95% de las consultas de usuario"
      
      Ver ISO 25010 para taxonomía completa.

   caso de uso
   use case
      Descripción de cómo un actor (usuario o sistema externo) interactúa con 
      el sistema para lograr un objetivo específico.
      
      **Formato típico:**
      
      * **Actor:** Quién interactúa
      * **Objetivo:** Qué quiere lograr
      * **Flujo principal:** Pasos para lograrlo
      * **Flujos alternativos:** Variaciones y errores
      
      **Ejemplo:** "Como usuario registrado, quiero buscar productos por categoría 
      para encontrar artículos de mi interés"

   escenario de calidad
   quality scenario
      Descripción concreta y medible de cómo el sistema debe comportarse respecto 
      a un atributo de calidad específico.
      
      **Estructura de un escenario:**
      
      1. **Fuente del estímulo:** Quién/qué origina el evento
      2. **Estímulo:** Qué sucede
      3. **Entorno:** Bajo qué condiciones
      4. **Artefacto:** Qué parte del sistema se ve afectada
      5. **Respuesta:** Cómo debe reaccionar el sistema
      6. **Medida de respuesta:** Cómo se mide
      
      **Ejemplo completo:**
      
      "Cuando 1000 usuarios concurrentes (fuente) realizan búsquedas (estímulo) 
      durante horas pico (entorno), el motor de búsqueda (artefacto) debe procesar 
      cada consulta (respuesta) en menos de 500ms percentil 95 (medida)."
      
      Ver plantilla completa en Sección 10: Quality Requirements.

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
   * - driving forces
     - fuerzas impulsoras
     - **factores determinantes**
   * - quality goals
     - objetivos de calidad
     - **atributos de calidad objetivo**
   * - stakeholder
     - interesado / parte interesada
     - **stakeholder** (preservado)
   * - building block
     - bloque de construcción
     - **componente arquitectónico**
   * - crosscutting
     - transversal
     - **crosscutting / aspectos transversales**

**Razón:** En arquitectura de software, estos términos tienen significados 
técnicos específicos que se pierden en traducción literal.

Principios Aplicados
--------------------

✅ **Contexto arquitectónico primero**
   - Entender el concepto en arquitectura de software
   - Usar terminología establecida en la comunidad hispana de arquitectos

✅ **Términos técnicos internacionales preservados**
   - stakeholder, quality goals, use case
   - Son estándar en ISO/IEEE y se usan así en español

✅ **Explicación en primera aparición**
   - Término marcado con ``:term:``
   - Definición completa en glosario

✅ **Coherencia terminológica**
   - "factores determinantes" usado consistentemente
   - No cambios arbitrarios entre secciones

✅ **Estilo**
   - Español mexicano informal (tú)
   - Voz activa preferida
   - Lenguaje claro y directo

Referencias Utilizadas
----------------------

* ISO/IEC 25010:2011 - Systems and software Quality Requirements and Evaluation
* ISO/IEC/IEEE 42010:2011 - Systems and software engineering — Architecture description
* SWEBOK v3 - Software Engineering Body of Knowledge
* arc42.org - Documentación oficial
* Guía de Traducción Arquitectónica ADT v1.0.0

----

**Fuente:** https://docs.arc42.org/section-1/  
**Traducido:** 2026-01-25  
**Modo:** Traducción Arquitectónica Contextual (NO literal)  
**Framework:** ADT (Arc42-Diátaxis-Traducción) v1.0.0  
**Guía aplicada:** ADT_GUIA_TRADUCCION_ARQUITECTONICA.md  
**Sección:** 1 de 12

.. important::
   **Diferencia con traducción anterior:**
   
   Esta versión aplica traducción CONTEXTUAL basada en terminología arquitectónica,
   NO traducción literal palabra por palabra. Ver sección "Notas de Traducción" 
   para detalles de los cambios aplicados.
