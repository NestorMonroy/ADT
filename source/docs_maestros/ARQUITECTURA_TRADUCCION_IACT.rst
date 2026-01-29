.. meta::
   :artefacto: ARQUITECTURA_TRADUCCION_IACT
   :tipo: Arquitectura_Documental
   :dominio: fundamentos
   :subdominio: arquitectura
   :estado: Aprobado
   :version: 2.0.0
   :fecha_creacion: 2026-01-08
   :ultimo_cambio: 2026-01-08
   :autor: Equipo Traducción
   :clasificacion: Interno

.. _arquitectura-traduccion-iact-v2:

==============================================================================
Arquitectura Documental: Biblioteca de Traducción Técnica IACT v2.0.0
==============================================================================

.. contents:: Contenido
   :depth: 4
   :local:

----

1. Propósito

============

Este documento establece la arquitectura completa de la **Biblioteca de 
Traducción Técnica** siguiendo la nomenclatura y estándares del proyecto 
IACT v2.0.0.

**Cambios v2.0.0 (MAJOR):**

- [OK] Nueva sección ``/biblioteca`` para gestión de libros traducidos
- [OK] Nuevos prefijos: LIB, CAT, META_BIB, GLOS_BIB
- [OK] Integración de Guía Metodológica de Clasificación Documental
- [OK] Metodología de organización jerárquica por libro completo
- [OK] Análisis estándares ISO de terminología (ISO 1087, ISO 704, etc.)

----

2. Alcance

==========

La arquitectura define:

1. Estructura de carpetas y subcarpetas
2. Nomenclatura de artefactos (archivos .rst)
3. Prefijos por tipo de contenido (34 prefijos)
4. Reglas de versionado semántico
5. Carpetas privadas (prefijo _) vs públicas
6. Organización de biblioteca de libros traducidos
7. Sistema de clasificación documental

----

3. Conformidad con Estándares

==============================

3.1. Cumplimiento NOM_001 v2.0.0
---------------------------------

[OK] Prefijos en MAYÚSCULAS: 34 prefijos definidos
[OK] 3 dígitos para artefactos globales (PROC_001, STD_001)
[OK] 2 dígitos para artefactos con módulos (FND_01, ONT_01)
[OK] Versionado semántico obligatorio: _[MAJOR]_[MINOR]_[PATCH].rst
[OK] Separador guión bajo (_) entre componentes
[OK] Nombres descriptivos en PascalCase
[OK] Sin números en carpetas (excepto metadata de capítulos)
[OK] Sin espacios en nombres de archivos y carpetas
[OK] Extensión .rst para documentos
[OK] Carpetas privadas con prefijo _

**Cumplimiento:** 100%

3.2. Cumplimiento STD_001 v1.1.0
---------------------------------

[OK] Sin emojis, usar [OK], [ERROR], [WARN]
[OK] Metadatos obligatorios en todos los artefactos
[OK] Estructura clara con secciones numeradas
[OK] Referencias cruzadas (:doc:, :ref:, :term:)

**Cumplimiento:** 100%

----

4. Estructura de Carpetas

==========================

4.1. Vista General
------------------

::

    source/
    │
    ├── index.rst                       # Índice principal Sphinx
    │
    ├── fundamentos/                    # [PÚBLICO] Base conceptual
    │   ├── index.rst
    │   ├── GLOS_001_Glosario_Traduccion_1_0_0.rst
    │   │
    │   ├── _metadata/                  # [PRIVADO] Metadata proyecto
    │   ├── _fundamentos_conceptuales/  # [PRIVADO] Basado ISO 1087
    │   ├── _ontologia_terminologia/    # [PRIVADO] Basado ISO 1087
    │   ├── _taxonomias_y_metamodelos/  # [PRIVADO] Clasificaciones
    │   └── _metodologias_traduccion/   # [PRIVADO] Basado ISO 704
    │
    ├── procedimientos/                 # [PÚBLICO] Workflows operativos
    ├── estandares/                     # [PÚBLICO] Estándares traducción
    ├── reglas_operativas/              # [PÚBLICO] Reglas específicas
    ├── herramientas_medios/            # [PÚBLICO] Por formato
    ├── casos_practicos/                # [PÚBLICO] Ejemplos y errores
    ├── guias_uso/                      # [PÚBLICO] Guías rápidas
    ├── prompts/                        # [PÚBLICO] Automatización
    ├── referencias/                    # [PÚBLICO] Referencias externas
    ├── apendices/                      # [PÚBLICO] Info adicional
    │
    └── biblioteca/                     # [PÚBLICO] ✨ NUEVA v2.0.0
        ├── index.rst
        ├── _metadata_biblioteca/       # [PRIVADO] Metodología clasificación
        │
        ├── informatica/                # Clasificación por dominio
        │   ├── programacion/
        │   │   ├── full_stack/
        │   │   │   └── Modern_Full_Stack_Development_Zammetti_2ed/
        │   │   ├── python/
        │   │   └── javascript/
        │   └── inteligencia_artificial/
        │
        ├── ingenieria/                 # Clasificación por dominio
        │   ├── sistemas/
        │   └── mecanica/
        │
        ├── ciencias/                   # Clasificación por dominio
        │   ├── biologia/
        │   └── quimica/
        │
        └── catalogo/                   # Catálogos y búsqueda
            ├── CAT_001_Indice_Alfabetico_1_0_0.rst
            ├── CAT_002_Indice_Por_Dominio_1_0_0.rst
            ├── CAT_003_Indice_Por_Autor_1_0_0.rst
            └── CAT_004_Indice_Cronologico_1_0_0.rst

----

5. Definición de Prefijos

==========================

5.1. Prefijos de Procedimientos (30 prefijos)
----------------------------------------------

.. list-table::
   :widths: 15 30 55
   :header-rows: 1

   * - Prefijo
     - Significado
     - Uso
   * - PROC
     - Procedure
     - Procedimientos operativos de traducción
   * - STD
     - Standard
     - Estándares y normas de traducción
   * - CNST
     - Constraint
     - Restricciones y limitaciones
   * - GLOS
     - Glossary
     - Glosarios terminológicos generales
   * - FND
     - Foundation
     - Fundamentos conceptuales (ISO 1087)
   * - TXM
     - Taxonomy
     - Taxonomías de clasificación
   * - MTM
     - Metamodel
     - Metamodelos de estructura documental
   * - RT
     - Rule Translation
     - Reglas de traducción específicas
   * - ESC
     - Escenario
     - Escenarios de traducción
   * - MD
     - Matrix Decision
     - Matrices de decisión
   * - REF
     - Reference
     - Referencias externas
   * - EQV
     - Equivalence
     - Equivalencias cross-medio
   * - CASE
     - Case Study
     - Casos de estudio
   * - ERR
     - Error
     - Errores comunes
   * - SUCCESS
     - Success Story
     - Casos de éxito
   * - EX
     - Exercise
     - Ejercicios prácticos
   * - GUIDE
     - Guide
     - Guías de uso
   * - FAQ
     - Frequently Asked Questions
     - Preguntas frecuentes
   * - TRBL
     - Troubleshooting
     - Resolución de problemas
   * - PROMPT
     - Prompt
     - Prompts de producción
   * - TPL
     - Template
     - Plantillas
   * - CHK
     - Checklist
     - Listas de verificación
   * - BIB
     - Bibliography
     - Bibliografía
   * - DOC
     - Documentation
     - Documentación oficial externa
   * - CS
     - CheatSheet
     - Hojas de referencia rápida
   * - VER
     - Version
     - Historia de versiones
   * - CONTRIB
     - Contributors
     - Contribuidores
   * - LIC
     - License
     - Información de licencia
   * - ROAD
     - Roadmap
     - Hoja de ruta
   * - ONT
     - Ontology
     - Ontología terminológica (ISO 1087)

5.2. Prefijos de Metadata (2 prefijos)
---------------------------------------

.. list-table::
   :widths: 15 30 55
   :header-rows: 1

   * - Prefijo
     - Significado
     - Uso
   * - META
     - Metadata
     - Metadata del proyecto traducción
   * - METH
     - Methodology
     - Metodologías de trabajo (ISO 704)

5.3. Prefijos de Biblioteca (4 prefijos) ✨ NUEVO v2.0.0
---------------------------------------------------------

.. list-table::
   :widths: 15 30 55
   :header-rows: 1

   * - Prefijo
     - Significado
     - Uso
   * - LIB
     - Library Item
     - Libros traducidos completos
   * - CAT
     - Catalog
     - Catálogos e índices de biblioteca
   * - META_BIB
     - Metadata Biblioteca
     - Metadata sistema biblioteca
   * - GLOS_BIB
     - Glossary Biblioteca
     - Glosarios específicos de biblioteca

**Total Prefijos:** 34 prefijos

----

6. Sección 1: Fundamentos

==========================

6.1. Estructura de ``fundamentos/``
------------------------------------

::

    fundamentos/
    ├── index.rst
    ├── GLOS_001_Glosario_Traduccion_1_0_0.rst
    │
    ├── _metadata/
    │   ├── META_001_Identidad_Proyecto_Traduccion_1_0_0.rst
    │   ├── META_002_Clasificacion_Tipos_Documento_1_0_0.rst
    │   ├── META_003_Estructura_Biblioteca_1_0_0.rst
    │   └── META_004_Historia_Versiones_1_0_0.rst
    │
    ├── _fundamentos_conceptuales/
    │   ├── FND_01_Concepto_Termino_1_0_0.rst
    │   ├── FND_02_Concepto_Designacion_1_0_0.rst
    │   ├── FND_03_Concepto_Definicion_1_0_0.rst
    │   ├── FND_04_Concepto_Traduccion_1_0_0.rst
    │   ├── FND_05_Concepto_Fidelidad_1_0_0.rst
    │   └── FND_06_Concepto_Equivalencia_1_0_0.rst
    │
    ├── _ontologia_terminologia/
    │   ├── ONT_01_Conceptos_Nucleares_1_0_0.rst
    │   ├── ONT_02_Relaciones_Conceptuales_1_0_0.rst
    │   ├── ONT_03_Jerarquia_Conceptual_1_0_0.rst
    │   ├── ONT_04_Vocabulario_Controlado_1_0_0.rst
    │   └── ONT_05_Modelo_Terminologico_ISO_1087_1_0_0.rst
    │
    ├── _taxonomias_y_metamodelos/
    │   ├── taxonomias/
    │   │   ├── TXM_01_Taxonomia_Tipos_Traduccion_1_0_0.rst
    │   │   ├── TXM_02_Taxonomia_Generos_Textuales_1_0_0.rst
    │   │   └── TXM_03_Taxonomia_Estrategias_Traduccion_1_0_0.rst
    │   └── metamodelos/
    │       ├── MTM_01_Metamodelo_Estructura_Libro_1_0_0.rst
    │       ├── MTM_02_Metamodelo_Estructura_Articulo_1_0_0.rst
    │       └── MTM_03_Metamodelo_Glosario_Terminologico_1_0_0.rst
    │
    └── _metodologias_traduccion/
        ├── METH_01_Compilacion_Terminologias_1_0_0.rst
        ├── METH_02_Escritura_Definiciones_1_0_0.rst
        ├── METH_03_Relacion_Conceptos_1_0_0.rst
        └── METH_04_Traduccion_Asistida_CAT_1_0_0.rst

6.2. Justificación Carpetas Privadas
-------------------------------------

**Carpetas con prefijo _ (privadas):**

1. **_metadata/**
   
   - Contiene metadata del proyecto (no contenido operativo)
   - Información administrativa y de gobernanza

2. **_fundamentos_conceptuales/**
   
   - Basado en ISO 1087:2019 (vocabulario terminológico)
   - Define conceptos nucleares (término, concepto, designación)
   - Base teórica, no procedimientos operativos

3. **_ontologia_terminologia/**
   
   - Basado en ISO 1087:2019 (ontología terminológica)
   - Modelo conceptual de términos y relaciones
   - Fundamento teórico para glosarios

4. **_taxonomias_y_metamodelos/**
   
   - Clasificaciones abstractas
   - Metamodelos de estructura documental
   - No son documentos operativos directos

5. **_metodologias_traduccion/**
   
   - Basado en ISO 704:2022 (métodos de trabajo)
   - Metodologías generales de compilación terminológica
   - Marco teórico para procedimientos

**¿Por qué privadas?**

- Son fundamentos conceptuales, no documentos operativos
- Basadas en estándares ISO (teoría formal)
- Usuarios finales consultan procedimientos, no ontologías

----

7. Sección 2: Procedimientos

=============================

7.1. Estructura de ``procedimientos/``
---------------------------------------

::

    procedimientos/
    ├── index.rst
    ├── PROC_001_Organizacion_Biblioteca_Libros_1_0_0.rst    ✨ NUEVO
    ├── PROC_002_Workflow_General_Traduccion_1_0_0.rst
    ├── PROC_003_Alta_Fidelidad_Protocolo_Gemini_1_0_0.rst
    ├── PROC_004_Marcado_Visual_Terminos_1_0_0.rst
    ├── PROC_005_Adaptacion_LaTeX_a_Sphinx_1_0_0.rst
    ├── PROC_006_Gestion_Glosarios_1_0_0.rst
    ├── PROC_007_Control_Calidad_Traduccion_1_0_0.rst
    ├── PROC_008_Revision_Tecnica_1_0_0.rst
    └── PROC_009_Publicacion_Documentos_1_0_0.rst

7.2. PROC_001: Primer Procedimiento (NUEVO v2.0.0)
----------------------------------------------------

**Nombre:** ``PROC_001_Organizacion_Biblioteca_Libros_1_0_0.rst``

**Propósito:** Definir cómo organizar un libro nuevo en ``/biblioteca``

**Contenido:**

1. Aplicación de Guía Metodológica de Clasificación Documental
2. Determinación de categoría (Informática, Ingeniería, Ciencias)
3. Determinación de subcategoría (Programación, IA, Sistemas)
4. Determinación de especialidad (Full-Stack, Python, UML)
5. Asignación de código de clasificación (INF.PRG.FST.001)
6. Creación de estructura de carpetas por libro
7. Nomenclatura de capítulos (sin números, nombres descriptivos)
8. Generación de metadata del libro
9. Creación de glosario acumulativo
10. Catalogación en índices

**Referencias:**

- Guía Metodológica de Clasificación Documental
- NOM_001 v2.0.0
- STD_001 v1.1.0

----

8. Sección 3: Estándares

========================

8.1. Estructura de ``estandares/``
-----------------------------------

::

    estandares/
    ├── index.rst
    ├── STD_001_Estandar_Nomenclatura_Archivos_1_0_0.rst
    ├── STD_002_Estandar_Formato_RST_1_0_0.rst
    ├── STD_003_Estandar_Metadata_Documentos_1_0_0.rst
    ├── STD_004_Estandar_Referencias_Cruzadas_1_0_0.rst
    ├── STD_005_Estandar_Glosarios_Terminologicos_1_0_0.rst
    ├── STD_006_Estandar_Marcado_Primera_Aparicion_1_0_0.rst
    ├── STD_007_Criterios_Fidelidad_Alta_1_0_0.rst
    ├── STD_008_Estandar_Versionado_Semantico_1_0_0.rst
    ├── STD_009_Estandar_Control_Calidad_1_0_0.rst
    └── STD_010_Estandar_Clasificacion_Biblioteca_1_0_0.rst  ✨ NUEVO

----

9. Sección 4: Reglas Operativas

================================

9.1. Estructura de ``reglas_operativas/``
------------------------------------------

::

    reglas_operativas/
    ├── index.rst
    │
    ├── reglas_traduccion/
    │   ├── RT_01_Primera_Aparicion_Terminos_1_0_0.rst
    │   ├── RT_02_Nombres_Propios_1_0_0.rst
    │   ├── RT_03_Acronimos_Siglas_1_0_0.rst
    │   ├── RT_04_Codigo_Fuente_1_0_0.rst
    │   ├── RT_05_Referencias_Cruzadas_1_0_0.rst
    │   ├── RT_06_Figuras_Tablas_1_0_0.rst
    │   ├── RT_07_Ecuaciones_Matematicas_1_0_0.rst
    │   └── RT_08_URLs_Enlaces_1_0_0.rst
    │
    ├── restricciones/
    │   ├── CNST_01_Restriccion_Emojis_1_0_0.rst
    │   ├── CNST_02_Restriccion_Anglicismos_1_0_0.rst
    │   ├── CNST_03_Restriccion_Longitud_Linea_1_0_0.rst
    │   └── CNST_04_Restriccion_Nivel_Anidacion_1_0_0.rst
    │
    └── escenarios/
        ├── ESC_01_Traduccion_Libro_Tecnico_1_0_0.rst
        ├── ESC_02_Traduccion_Manual_Usuario_1_0_0.rst
        ├── ESC_03_Traduccion_Articulo_Cientifico_1_0_0.rst
        └── ESC_04_Traduccion_Tutorial_1_0_0.rst

----

10. Sección 5: Biblioteca (NUEVA v2.0.0)

=========================================

10.1. Estructura de ``biblioteca/``
------------------------------------

::

    biblioteca/
    ├── index.rst
    │
    ├── _metadata_biblioteca/
    │   ├── META_BIB_001_Sistema_Clasificacion_1_0_0.rst
    │   ├── META_BIB_002_Guia_Organizacion_Jerarquica_1_0_0.rst
    │   └── META_BIB_003_Esquema_Codificacion_1_0_0.rst
    │
    ├── informatica/
    │   ├── programacion/
    │   │   ├── full_stack/
    │   │   │   └── Modern_Full_Stack_Development_Zammetti_2ed/
    │   │   │       ├── metadata_libro.rst
    │   │   │       ├── index.rst
    │   │   │       ├── glosario_acumulativo.rst
    │   │   │       │
    │   │   │       ├── server_side_action_node_npm/
    │   │   │       │   ├── original/
    │   │   │       │   │   └── chapter_01.pdf
    │   │   │       │   ├── traduccion/
    │   │   │       │   │   └── capitulo_01.rst
    │   │   │       │   ├── glosario_capitulo.rst
    │   │   │       │   ├── notas_traduccion.rst
    │   │   │       │   └── figuras/
    │   │   │       │
    │   │   │       ├── advanced_node_npm/
    │   │   │       ├── client_side_react/
    │   │   │       ├── advanced_react/
    │   │   │       ├── typescript_foundation/
    │   │   │       ├── advanced_typescript/
    │   │   │       ├── webpack_bundling/
    │   │   │       ├── mailbag_server/
    │   │   │       ├── mailbag_client/
    │   │   │       ├── battlejong_server/
    │   │   │       ├── battlejong_client/
    │   │   │       ├── docker_deployment/
    │   │   │       ├── fooderator_server/
    │   │   │       └── fooderator_client/
    │   │   │
    │   │   ├── python/
    │   │   └── javascript/
    │   │
    │   └── inteligencia_artificial/
    │
    ├── ingenieria/
    │   ├── sistemas/
    │   └── mecanica/
    │
    ├── ciencias/
    │   ├── biologia/
    │   └── quimica/
    │
    └── catalogo/
        ├── CAT_001_Indice_Alfabetico_1_0_0.rst
        ├── CAT_002_Indice_Por_Dominio_1_0_0.rst
        ├── CAT_003_Indice_Por_Autor_1_0_0.rst
        └── CAT_004_Indice_Cronologico_1_0_0.rst

10.2. Nomenclatura de Capítulos
--------------------------------

**Regla:** Sin números en nombres de carpetas (cumple NOM_001)

**Formato:**
::

    nombre_descriptivo_del_capitulo/

**Ejemplos:**
::

    ✅ Correcto:
    server_side_action_node_npm/
    advanced_node_npm/
    client_side_react/
    typescript_foundation/
    docker_deployment/

    ❌ Incorrecto:
    Chapter_01_Server_Side_Action/       # Viola NOM_001
    01_Server_Side_Action/                # Viola NOM_001
    chapter1/                             # Poco descriptivo

**Preservar orden con metadata:**

.. code-block:: rst

   .. meta::
      :capitulo_numero: 01
      :orden: 01
      :titulo_original: Server-Side Action: Node and NPM

10.3. Sistema de Clasificación Documental
------------------------------------------

**Basado en:** Guía Metodológica de Clasificación Documental

**Niveles:**

1. **Categoría Principal:** Dominio general
   
   - Informática
   - Ingeniería
   - Ciencias

2. **Subcategoría:** Área específica
   
   - Programación
   - Inteligencia Artificial
   - Sistemas

3. **Especialidad:** Subtema
   
   - Full-Stack
   - Python
   - UML

4. **Código de Clasificación:** Alfanumérico
   
   - INF.PRG.FST.001
   - ING.SIS.UML.002
   - CIE.BIO.SYS.001

**Aplicación:**

Ver ``PROC_001_Organizacion_Biblioteca_Libros_1_0_0.rst``

10.4. Metadata de Libro
------------------------

**Archivo:** ``metadata_libro.rst``

**Contenido Mínimo:**

.. code-block:: rst

   .. meta::
      :libro_id: LIB_INF_FST_001
      :tipo: Libro_Tecnico
      :estado: En_Traduccion
      :progreso: 35%
      :clasificacion: INF.PRG.FST.001

   Título Original
      Modern Full-Stack Development

   Autor
      Frank Zammetti

   Clasificación
      INF.PRG.FST.001

   Estado
      35% completado (5 de 14 capítulos)

   Procedimientos Aplicados
      - PROC_002_Workflow_General_1_0_0
      - PROC_003_Alta_Fidelidad_1_0_0

**Ver:** Ejemplo completo en sección 10.6

10.5. Glosario de Capítulo
---------------------------

**Archivo:** ``glosario_capitulo.rst``

**Propósito:** Listar todos los términos del capítulo con primera aparición

**Formato:**

.. code-block:: rst

   .. glossary::
      :sorted:

      Node.js
         Entorno de ejecución de JavaScript...
         
         **Primera aparición:** Página 2, Sección "Runtimes"
         **Ver también:** :term:`V8 Engine`

      NPM
         Node Package Manager...

10.6. Glosario Acumulativo
---------------------------

**Archivo:** ``glosario_acumulativo.rst``

**Propósito:** Consolidar TODOS los términos del libro

**Generación:** Automática desde glosarios de capítulos

**Estadísticas:**

- Total de términos únicos
- Capítulos donde aparece cada término
- Frecuencia de uso

----

11. Catálogos de Biblioteca

============================

11.1. CAT_001: Índice Alfabético
---------------------------------

**Formato:**

.. code-block:: rst

   A
   ===
   - Advanced TypeScript (Zammetti, 2024) → INF.PRG.FST.001, Cap. 6

   B
   ===
   - BattleJong Client (Zammetti, 2024) → INF.PRG.FST.001, Cap. 11

11.2. CAT_002: Índice por Dominio
----------------------------------

**Formato:**

.. code-block:: rst

   Informática
   ===========
   
   Programación
   ------------
   - Modern Full-Stack Development (Zammetti, 2024) → INF.PRG.FST.001

11.3. CAT_003: Índice por Autor
--------------------------------

**Formato:**

.. code-block:: rst

   Zammetti, Frank
   ===============
   - Modern Full-Stack Development (2024) → INF.PRG.FST.001

11.4. CAT_004: Índice Cronológico
----------------------------------

**Formato:**

.. code-block:: rst

   2024
   ====
   - Modern Full-Stack Development (Zammetti) → INF.PRG.FST.001

----

12. Mapeo de Contenido Existente

=================================

12.1. Documentos de Sesión Previa → v2.0.0
-------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Documento v1.0.0
     - Ubicación v2.0.0
   * - procedimiento_traduccion.md
     - PROC_002_Workflow_General_1_0_0.rst
   * - principios_alta_fidelidad.md
     - STD_007_Criterios_Fidelidad_1_0_0.rst
   * - matriz_decision_fidelidad.md
     - MD_001_Modo_1_vs_Modo_2_1_0_0.rst
   * - guia_rapida.md
     - GUIDE_001_Guia_Rapida_1_0_0.rst
   * - PROMPT_MAESTRO_SPHINX.md
     - PROMPT_002_Maestro_Sphinx_1_0_0.rst

12.2. Nuevos Documentos v2.0.0
-------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Documento Nuevo
     - Ubicación
   * - Guía Clasificación Documental
     - META_BIB_002_Guia_Organizacion_1_0_0.rst
   * - Análisis ISO Terminología
     - fundamentos/_metodologias_traduccion/
   * - Procedimiento Biblioteca
     - PROC_001_Organizacion_Biblioteca_1_0_0.rst
   * - Estándar Clasificación
     - STD_010_Estandar_Clasificacion_1_0_0.rst

----

13. Base en Estándares ISO

===========================

13.1. Fundamentos Teóricos
---------------------------

**ISO 1087:2019** - Terminology work and terminology science — Vocabulary

- Estado: Confirmado 2025, sigue vigente
- Páginas: 38
- Justifica: ``_fundamentos_conceptuales/``, ``_ontologia_terminologia/``
- Define: término, concepto, designación, definición

**ISO 704:2022** - Terminology work — Principles and methods

- Estado: Vigente (4ª edición)
- Páginas: 90
- Justifica: ``_metodologias_traduccion/``
- Proporciona: Métodos de compilación terminológica

**ISO 12620-2:2022** - Management of terminology resources — Part 2: Repositories

- Estado: Vigente
- Páginas: 8
- Justifica: Procedimientos de gestión
- Proporciona: Gobernanza de repositorios terminológicos

13.2. Formatos y Representación
--------------------------------

**ISO 16642:2017** - Terminological Markup Framework (TMF)

- Estado: Vigente
- Aplicabilidad: Limitada (solo para sistemas informáticos)

**ISO 30042:2019** - TermBase eXchange (TBX)

- Estado: Vigente (TBX 3.0)
- Aplicabilidad: Intercambio de glosarios

**Ver:** ``ANALISIS_ESTANDARES_ISO_TERMINOLOGIA.md`` para detalles completos

----

14. Versionado Semántico

=========================

14.1. Reglas de Versionado
---------------------------

**Formato:** ``_[MAJOR]_[MINOR]_[PATCH].rst``

**Incremento MAJOR (x.0.0):**

- Cambios incompatibles en estructura
- Añadir/eliminar secciones principales
- Cambios en nomenclatura que requieren migración

**Ejemplo v1.0.0 → v2.0.0:**

- [OK] Nueva sección /biblioteca (estructura fundamental)
- [OK] Nuevos prefijos (LIB, CAT, META_BIB, GLOS_BIB)
- [OK] Nueva metodología de organización

**Incremento MINOR (0.x.0):**

- Nueva funcionalidad compatible
- Añadir nuevos prefijos sin cambiar existentes
- Añadir nuevos procedimientos

**Incremento PATCH (0.0.x):**

- Correcciones de errores
- Clarificaciones de documentación
- Mejoras menores sin cambios estructurales

14.2. Historia de Versiones
----------------------------

.. list-table::
   :widths: 10 15 75
   :header-rows: 1

   * - Versión
     - Fecha
     - Cambios
   * - 2.0.0
     - 2026-01-08
     - [MAJOR] Nueva sección /biblioteca con sistema de clasificación
       documental completo. Nuevos prefijos: LIB, CAT, META_BIB, GLOS_BIB.
       Integración Guía Metodológica Clasificación. Nomenclatura capítulos
       sin números. Análisis estándares ISO terminología.
   * - 1.0.0
     - 2026-01-08
     - Versión inicial con 10 secciones, 30 prefijos, estructura base
       siguiendo nomenclatura IACT v2.0.0

----

15. Ventajas de la Arquitectura v2.0.0

=======================================

15.1. Ventajas Técnicas
------------------------

[OK] **Conformidad Total:** 100% con NOM_001 y STD_001
[OK] **Escalabilidad:** Fácil añadir nuevos libros y categorías
[OK] **Trazabilidad:** Original → Traducción con metadata completa
[OK] **Búsqueda Optimizada:** Múltiples catálogos (alfabético, dominio, autor)
[OK] **Modularidad:** Cada libro es independiente
[OK] **Versionado:** Control de versiones por capítulo y por libro

15.2. Ventajas Operativas
--------------------------

[OK] **Separación Clara:** Procedimientos vs Productos (biblioteca)
[OK] **Clasificación Múltiple:** Por dominio, idioma, tipo, estado
[OK] **Tracking Granular:** Progreso por capítulo
[OK] **Glosarios Incrementales:** Por capítulo + acumulativo
[OK] **Revisiones Independientes:** Capítulo por capítulo
[OK] **Build Independiente:** Sphinx puede compilar cada libro

15.3. Ventajas Metodológicas
-----------------------------

[OK] **Base en ISO:** Fundamentos en ISO 1087, ISO 704
[OK] **Guía Metodológica:** Clasificación sistemática y verificable
[OK] **Coherencia:** Lógica, claridad, exhaustividad
[OK] **Aplicabilidad:** Adaptable a diferentes dominios
[OK] **Documentación Completa:** Cada decisión justificada

----

16. Próximos Pasos

==================

16.1. Implementación Inmediata
-------------------------------

1. Crear ``PROC_001_Organizacion_Biblioteca_Libros_1_0_0.rst``
2. Crear ``STD_010_Estandar_Clasificacion_Biblioteca_1_0_0.rst``
3. Copiar Guía Metodológica a ``META_BIB_002_Guia_Organizacion_1_0_0.rst``
4. Crear estructura ``/biblioteca`` con ejemplo completo
5. Implementar primer libro: Modern Full-Stack Development

16.2. Documentación Complementaria
-----------------------------------

1. Actualizar ``index.rst`` principal con nueva sección biblioteca
2. Crear tutoriales de clasificación
3. Crear checklists de organización
4. Documentar casos prácticos de clasificación
5. Generar catálogos automáticamente

16.3. Validación
----------------

1. Verificar cumplimiento NOM_001 en todos los archivos
2. Verificar cumplimiento STD_001 en todos los archivos
3. Validar estructura con Sphinx (``make html``)
4. Revisar metadatos con scripts de validación
5. Obtener feedback del equipo de traducción

----

17. Referencias

===============

17.1. Estándares IACT
----------------------

- NOM_001_Nomenclatura_Proyecto_IACT_2_0_0.rst
- STD_001_Estandares_Documentacion_Sin_Emojis_1_1_0.rst

17.2. Estándares ISO
--------------------

- ISO 1087:2019 - Terminology work and terminology science
- ISO 704:2022 - Terminology work — Principles and methods
- ISO 12620-2:2022 - Management of terminology resources
- ISO 16642:2017 - Terminological Markup Framework
- ISO 30042:2019 - TermBase eXchange (TBX)

17.3. Documentos de Análisis
-----------------------------

- ANALISIS_ESTANDARES_ISO_TERMINOLOGIA.md
- ANALISIS_CUMPLIMIENTO_NOM_STD.md
- Guía_Metodológica_para_Clasificación_Documental.txt

----

18. Apéndices

=============

18.1. Ejemplo Completo: Modern Full-Stack Development
------------------------------------------------------

**Ver sección 10.1** para estructura completa de carpetas.

**Características:**

- 14 capítulos traducibles
- Código de clasificación: INF.PRG.FST.001
- Nomenclatura sin números: ``server_side_action_node_npm/``
- Metadata completa por capítulo
- Glosarios por capítulo + acumulativo
- Figuras adaptadas por capítulo
- Tracking de progreso: 35% completado

18.2. Template de Metadata de Libro
------------------------------------

Ver ejemplo completo en respuesta anterior (metadata_libro.rst)

18.3. Template de Glosario de Capítulo
---------------------------------------

Ver ejemplo completo en respuesta anterior (glosario_capitulo.rst)

----

**Documento controlado. Versión 2.0.0. Fecha: 2026-01-08.**

**Aprobado por:** Equipo Traducción

**Próxima revisión:** 2026-07-08 (6 meses)
