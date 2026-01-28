=============================
Fundamentos de Traducción ADT
=============================

.. note::
   Esta sección contiene los **fundamentos teóricos y conceptuales** del 
   proyecto ADT, basados en el Método Peshitta (Micheli, 2014) y estándares
   ISO 1087/704.

----

Introducción
============

Los fundamentos de ADT establecen la base metodológica para traducción técnica
de alta calidad, combinando:

- **Translation Studies** (50+ años de investigación)
- **MDA/MDE** (Model-Driven Architecture)
- **ISO 1087/704** (Terminología y metodologías)

----

Documentos Principales
======================

.. toctree::
   :maxdepth: 2
   :caption: Documentos Públicos

   glosario_traduccion
   principios_fundamentales
   objetivos_tacticas
   metodo_segmentacion

----

Base Teórica (Carpetas Privadas)
=================================

**Fundamentos Conceptuales** (_fundamentos_conceptuales/)
   Base teórica según ISO 1087
   
   - :doc:`_fundamentos_conceptuales/traduccion_como_transformacion`
   - :doc:`_fundamentos_conceptuales/signifiant_vs_signifie`

**Metodologías** (_metodologias/)
   Procedimientos según ISO 704
   
   - :doc:`_metodologias/metodo_por_defecto`

**Metadata** (_metadata/)
   Referencias bibliográficas
   
   - :doc:`_metadata/micheli_2014`

----

Modelos de Alto Nivel
======================

.. toctree::
   :maxdepth: 2
   :caption: Metamodelos

   metamodelos/framework_universal_transformacion

----

Conceptos Clave
===============

Isomorfismo Fundamental
-----------------------

**Traducción ≈ Transformación de Modelos**

.. code-block:: text

   Texto Fuente (LaTeX)  →  Texto Destino (RST/HTML)
         ≈                        ≈
   PIM (Platform-Ind.)   →  PSM (Platform-Spec.)

**Base:** 50+ años Translation Studies aplicados a ingeniería de software

Los Tres Pilares del Método
----------------------------

1. **Segmentación**
   
   Nivel al que trabajamos (sección, párrafo, frase, palabra)

2. **Rendición**
   
   Cómo mapeamos elementos básicos (comando por comando)

3. **Preferencia**
   
   Signifié (contenido) sobre Signifiant (forma)

Los Cuatro Objetivos
---------------------

Razones para desviarse del método por defecto:

1. **Domesticación** - Adaptar a plataforma destino
2. **Claridad** - Hacer comprensible
3. **Consistencia** - Resolver inconsistencias
4. **Simplificación** - Reducir complejidad

Las 14+ Tácticas
----------------

Operaciones concretas para lograr objetivos:

- Adición, Omisión, Sustitución
- Cambio de orden, Especificación, Generalización
- Explicación, Normalización, Transposición
- Modulación, Compensación, Amplificación
- Condensación, Literalización

----

Flujo de Aprendizaje
====================

**Para nuevos usuarios:**

1. **Leer:** :doc:`principios_fundamentales`
   
   Entender conceptos base (30 min)

2. **Consultar:** :doc:`glosario_traduccion`
   
   Familiarizarse con terminología (15 min)

3. **Estudiar:** :doc:`objetivos_tacticas`
   
   Aprender objetivos y tácticas (45 min)

4. **Profundizar:** :doc:`_fundamentos_conceptuales/traduccion_como_transformacion`
   
   Teoría completa (1-2 horas)

5. **Aplicar:** Ver :doc:`/02_procedimientos/workflow_general`
   
   Procedimiento paso a paso

----

Conexiones con Otros Documentos
================================

Documentos Maestros
-------------------

- :doc:`/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS`
- :doc:`/docs_maestros/SINTESIS_METODOLOGICA_ADT`
- :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT`

Procedimientos
--------------

- :doc:`/02_procedimientos/workflow_general`
- :doc:`/02_procedimientos/modo_alta_fidelidad/index`
- :doc:`/02_procedimientos/modo_marcado_visual/index`

Prompts
-------

- :doc:`/08_prompts/prompt_maestro_latex`
- :doc:`/08_prompts/prompt_maestro_sphinx`

----

Resumen Visual
==============

.. code-block:: text

   FUNDAMENTOS ADT
   ═══════════════════════════════════════════════════════════
   
   BASE TEÓRICA (Carpetas Privadas _)
   ├─ Fundamentos Conceptuales (ISO 1087)
   │  ├─ Traducción como Transformación
   │  └─ Signifiant vs Signifié
   ├─ Metodologías (ISO 704)
   │  └─ Método por Defecto (3 pilares)
   └─ Metadata
      └─ Micheli (2014)
   
   DOCUMENTOS PÚBLICOS
   ├─ Glosario de Traducción
   ├─ Principios Fundamentales
   ├─ Objetivos y Tácticas
   └─ Método de Segmentación
   
   METAMODELOS
   └─ Framework Universal de Transformación
   
   APLICACIÓN
   └─> Procedimientos (02_procedimientos/)
   └─> Prompts (08_prompts/)

----

Referencias
===========

**Estándares ISO:**

- ISO 1087:2019 - Terminology work and terminology science
- ISO 704:2022 - Terminology work — Principles and methods

**Literatura Académica:**

- Micheli, D. (2014). Translation Technique in Peshitta Zechariah
- Toury, G. (1995). Descriptive Translation Studies
- Nida, E. (1964). Toward a Science of Translating

**MDA/MDE:**

- OMG (2003). MDA Guide v1.0.1
- MOF (Meta Object Facility)

----

**Versión:** 1.0  
**Fecha:** 2026-01-27  
**Estado:** Aprobado
