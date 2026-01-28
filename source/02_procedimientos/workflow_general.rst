.. meta::
   :artefacto: PROC_002_Workflow_General
   :tipo: Procedimiento
   :dominio: procedimientos
   :estado: Aprobado
   :version: 1.7.2
   :fecha_creacion: 2026-01-27
   :ultimo_cambio: 2026-01-27
   :autor: Equipo ADT
   :clasificacion: Interno

.. _proc-002-workflow-general:

=============================
Workflow General de Traducción
=============================

:Versión: 1.7.2
:Categoría: Procedimientos
:Ubicación: 02_procedimientos/
:Tipo: Procedimiento Operativo Principal
:Base: Método Peshitta + ADT

**Registro de Cambios:**

- **v1.7.2 (2026-01-27):** MAJOR - Agregados PASO 0 (CRÍTICO) y FASE 3.7 (BUCLE) con integración de script automático. PASO 0: Lectura de Fuente Completa ANTES de traducir - requiere leer plantilla arc42 completa, crear inventario con script (/tmp/ADT/scripts/analisis_profundo_funcional.py), verificar fuentes de verdad, y checklist pre-traducción. FASE 3.7: Verificación contra Original con BUCLE y script - comparar contra inventario, pregunta crítica "¿TODO traducido?", bucle de verificación (si NO → volver a FASE 3), documentación de iteraciones. Script automatiza creación de inventario (ahorra 20 min) y verificación de completitud (ahorra 25 min). Previene ERROR CRÍTICO: omitir contenido de plantillas (detectado en Sección 07). Principio: "Nunca empezar a traducir sin saber TODO lo que se va a traducir" + "Solo declarar completo después de verificar contra inventario".
- **v1.7.1 (2026-01-27):** MINOR - Agregado Paso 3.5: Enriquecimiento Opcional (nuevo). Define claramente cuándo SÍ/NO agregar contenido complementario, formato obligatorio para marcado (.. note::), ubicación correcta, y ejemplos. Renumerada antigua FASE 3.5 a FASE 3.6. Corrige error identificado: "no traducir completo el original PRIMERO". Principio: 1º Traducir TODO, 2º Terminología, 3º OPCIONAL Enriquecimiento marcado. Basado en análisis de Tips Sección 05 (arc42).
- **v1.7.0 (2026-01-27):** MINOR - Agregada FASE 5.6: Validación de Completitud y Fidelidad (OBLIGATORIA). Incluye verificación de longitud, secciones, ejemplos y contenido agregado. Actualizada Regla de Oro con definiciones precisas de "Traducción COMPLETA" y "Traducción FIEL". Agregados checklist pre-commit y señales de advertencia. Previene ERROR TIPO A (esqueletos) y ERROR TIPO B (contenido agregado). Basado en análisis de errores de Secciones 3 y 5.
- **v1.6.0 (2026-01-27):** MINOR - Agregada FASE 5.5: Documentación de Sección (OBLIGATORIA). Incluye creación de section-X.txt y section-X.json, verificación de completitud contra documento original, y actualización de archivo principal. Agregadas lecciones aprendidas de Sección 01 (arc42). Checklist de verificación de contenido completo.
- **v1.5.0 (2026-01-27):** MINOR - Agregado Paso 3.4: Traducción Arquitectónica (OBLIGATORIO para arc42). Integración completa de Guía de Traducción Arquitectónica con tabla de términos y ejemplos literal vs contextual.
- **v1.4.0 (2026-01-27):** MINOR - Agregada FASE 3.5 CRÍTICA: Revisión de Literalidad (obligatoria, no saltarse)
- **v1.3.0 (2026-01-27):** MINOR - Correcciones críticas: estructura 1:1 explícita en Paso 3.1, checklist de revisión Signifié en Paso 3.3
- **v1.2.0 (2026-01-27):** MINOR - Agregadas herramientas Python, FASE 2 actualizada con análisis automatizado, casos especiales y lecciones aprendidas de arc42
- **v1.1.0 (2026-01-27):** MINOR - Corrección de estructura biblioteca/, integración con Guía Metodológica Clasificación
- **v1.0.0 (2026-01-27):** MAJOR - Versión inicial

.. contents:: Contenido
   :depth: 3
   :local:

----

Introducción
============

Este documento describe el **workflow completo** para traducir documentación
técnica de LaTeX a RST/Sphinx usando la metodología ADT.

**Audiencia:**
   Cualquier persona que vaya a realizar traducciones en el proyecto ADT.

**Prerrequisitos:**
   - Haber leído :doc:`/01_fundamentos/principios_fundamentales`
   - Familiaridad con LaTeX y RST básico
   - Sphinx instalado y configurado

----

Integración con Biblioteca y Clasificación
===========================================

**IMPORTANTE:** Este workflow trabaja con la estructura de **biblioteca/** y utiliza
la **Guía Metodológica de Clasificación Documental**.

Estructura Base
---------------

.. code-block:: text

   /tmp/ADT/source/biblioteca/
   ├── _metadata_biblioteca/           # Guías de clasificación
   │   ├── META_BIB_001_Sistema_Clasificacion_1_0_0.rst
   │   ├── META_BIB_002_Guia_Organizacion_Jerarquica_1_0_0.rst
   │   └── META_BIB_003_Esquema_Codificacion_1_0_0.rst
   │
   ├── informatica/                    # Categoría
   │   └── programacion/               # Subcategoría
   │       └── full_stack/             # Especialidad
   │           └── Nombre_Libro/       # Libro completo
   │               ├── metadata_libro.rst
   │               ├── index.rst
   │               ├── glosario_acumulativo.rst
   │               └── nombre_capitulo/    # Sin números
   │                   ├── original/
   │                   ├── traduccion/
   │                   ├── glosario_capitulo.rst
   │                   ├── notas_traduccion.rst
   │                   └── figuras/

Sistema de Clasificación
-------------------------

**Código:** CATEGORÍA.SUBCATEGORÍA.ESPECIALIDAD.NÚMERO

**Ejemplos:**

- **INF.PRG.FST.001** = Informática > Programación > Full-Stack > Libro #1
- **ING.SIS.UML.002** = Ingeniería > Sistemas > UML > Libro #2
- **CIE.BIO.SYS.001** = Ciencias > Biología > Sistemas > Libro #1

**Documentos de Referencia:**

- :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT` (sección 10)
- :doc:`/docs_maestros/ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta`
- :doc:`/biblioteca/_metadata_biblioteca/META_BIB_001_Sistema_Clasificacion_1_0_0`

----

Visión General del Workflow
============================

Diagrama de Flujo
-----------------

.. code-block:: text

   WORKFLOW ADT - 7 FASES (+ PASO 0 y FASE 3.7 NUEVOS v1.7.2)
   ═══════════════════════════════════════════════════════════
   
   ★★★ PASO 0: LECTURA DE FUENTE COMPLETA (NUEVO v1.7.2)
   ├─ Obtener plantilla completa de la sección
   ├─ Crear inventario COMPLETO (⚡ con script)
   │  └─ python3 /tmp/ADT/scripts/analisis_profundo_funcional.py XX
   ├─ Verificar fuentes de verdad
   └─ Checklist pre-traducción
   
   FASE 1: PREPARACIÓN
   ├─ Análisis del documento fuente
   ├─ Configuración del entorno
   └─ Planificación de la traducción
   
   FASE 2: ANÁLISIS ESTRUCTURAL
   ├─ Identificar estructura jerárquica
   ├─ Mapear elementos especiales
   └─ Detectar inconsistencias
   
   FASE 3: TRADUCCIÓN INICIAL (Método por Defecto)
   ├─ 3.1: Traducción Literal
   ├─ 3.2: Mapeo 1:1
   ├─ 3.3: Preferencia Signifié
   ├─ 3.4: Traducción Arquitectónica (arc42)
   ├─ 3.5: Enriquecimiento Opcional
   ├─ 3.6: Revisión de Literalidad
   └─ 3.7: VERIFICACIÓN CONTRA ORIGINAL ★★★ (NUEVO v1.7.2)
       ├─ Comparar contra inventario (⚡ con script)
       │  └─ python3 /tmp/ADT/scripts/analisis_profundo_funcional.py XX
       ├─ ¿TODO traducido? → SI: continuar, NO: VOLVER a FASE 3
       └─ Documentar verificación
   
   FASE 4: APLICACIÓN DE TÁCTICAS
   ├─ Identificar objetivos (Domesticación, Claridad, etc.)
   ├─ Aplicar tácticas apropiadas
   └─ Documentar decisiones
   
   FASE 5: VALIDACIÓN
   ├─ Compilar Sphinx (make html)
   ├─ Verificar preservación semántica
   ├─ Revisar calidad visual
   ├─ 5.5: Documentación de Sección
   └─ 5.6: Validación de Completitud y Fidelidad
   
   FASE 6: REVISIÓN Y MEJORA
   ├─ Revisar enlaces y referencias
   ├─ Optimizar redacción
   └─ Aplicar feedback
   
   FASE 7: PUBLICACIÓN
   ├─ Compilación final
   ├─ Control de calidad
   └─ Despliegue
   
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   
   ⚡ AUTOMATIZACIÓN CON SCRIPT:
      Script: /tmp/ADT/scripts/analisis_profundo_funcional.py
      Ahorra: ~45 minutos por sección
      Genera: JSON + TXT en raíz de sección

Tiempo Estimado
---------------

**Por capítulo de libro** (en estructura biblioteca/):

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Fase
     - Tiempo
     - Observaciones
   * - Preparación
     - 15-30 min
     - Una vez por libro completo
   * - Análisis
     - 5-10 min
     - Por capítulo
   * - Traducción Inicial
     - 20-40 min
     - Depende de complejidad del capítulo
   * - Aplicación Tácticas
     - 10-20 min
     - Si es necesario
   * - Validación
     - 5-10 min
     - Por capítulo
   * - Revisión
     - 10-15 min
     - Por capítulo
   * - Publicación
     - 15-30 min
     - Al completar libro completo

**Total por capítulo:** ~70-130 min (1-2 horas)

**Total por libro típico (10-15 capítulos):** 15-30 horas

----

Herramientas y Scripts Disponibles
===================================

**NUEVA SECCIÓN v1.2.0:** Esta sección documenta las herramientas Python y scripts bash
disponibles para facilitar el proceso de traducción.

Scripts Python
--------------

analizar_seccion.py
~~~~~~~~~~~~~~~~~~~

**Propósito:**
   Análisis automático de archivos Markdown de una sección.

**Ubicación:**
   ``scripts/analizar_seccion.py``

**Uso:**

.. code-block:: bash

   # Analizar una sección
   python scripts/analizar_seccion.py sections/02_constraints
   
   # Genera:
   # - Reporte en consola (legible)
   # - analisis_seccion.json (datos estructurados)

**Información extraída:**

- Front matter YAML (metadatos)
- Estructura jerárquica (headings H1-H6)
- Elementos especiales:
  
  - Imágenes, tablas, bloques de código
  - Enlaces, DIVs HTML, listas

- Estadísticas de contenido

**Cuándo usar:**
   - Al inicio de FASE 2 (Análisis Estructural)
   - Después de redistribuir archivos de repositorio
   - Para verificar contenido de sección

Scripts Bash
------------

redistribuir_arc42_CORRECTO.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Propósito:**
   Redistribuir archivos del repositorio arc42 desde ``original/`` a secciones.

**Lección aprendida:**
   ⚠️ NO buscar archivos por palabras clave en nombres.
   ✅ Usar la estructura real del repositorio fuente.

validar_estructura.sh
~~~~~~~~~~~~~~~~~~~~~

**Propósito:**
   Validar que un libro cumple con NOM_001 y estructura de biblioteca.

**Uso:**

.. code-block:: bash

   ./scripts/validar_estructura.sh biblioteca/.../arc42_documentation

progreso_libro.sh
~~~~~~~~~~~~~~~~~

**Propósito:**
   Calcular progreso de traducción de un libro.

Ver más detalles en: :doc:`/scripts/README`

----

PASO 0: LECTURA DE FUENTE COMPLETA ★★★ (CRÍTICO)
==================================================

.. important::
   **OBLIGATORIO:** Este paso NO puede saltarse.
   
   Previene el error más común: **omitir contenido de plantillas**.

**Cuándo ejecutar:**

ANTES de cualquier otra fase.
ANTES de leer archivos en ``/original/``.
ANTES de crear estructura de carpetas.

**Tiempo estimado:** 15-30 minutos

----

Paso 0.1: Obtener Plantilla Completa de la Sección
---------------------------------------------------

**Para traducciones arc42:**

Cada sección arc42 tiene DOS tipos de contenido:

1. **Plantilla de sección** (documento principal)
2. **Archivos individuales** (tips, ejemplos)

**Ejemplo para Sección 07 (Deployment View):**

.. code-block:: text

   Contenido COMPLETO de Sección 07:
   
   A. PLANTILLA (documento que proporciona usuario):
      - Título: "7. Deployment view"
      - Content (descripción de qué contiene)
      - Motivation (por qué documentar)
      - Form (cómo documentar)
      - 7.1 Infrastructure Level 1 (plantilla con subsecciones)
      - 7.2 Infrastructure Level 2 (plantilla con subsecciones)
      - Further Info (enlaces y referencias)
   
   B. ARCHIVOS INDIVIDUALES (en /original/):
      - 10 tips: 2016-03-01-t-7-1.md a 2016-03-02-t-7-10.md
      - 3 ejemplos: 07-deployment-*.md

**⚠️ ERROR COMÚN:**

Solo leer archivos en ``/original/`` y asumir que eso es todo.

**✅ CORRECTO:**

1. Leer plantilla completa de la sección
2. Leer archivos individuales en ``/original/``
3. Crear inventario de TODO el contenido

**Dónde obtener plantilla:**

- Usuario proporciona documento con estructura completa
- O consultar: https://arc42.org/sections (para referencia)

----

Paso 0.2: Crear Inventario COMPLETO
------------------------------------

**Método 1: Automático con Script (RECOMENDADO)**

Usar script de análisis funcional:

.. code-block:: bash

   # Ejecutar análisis
   python3 /tmp/ADT/scripts/analisis_profundo_funcional.py 07
   
   # Salidas generadas en raíz de sección:
   # - ANALISIS_PROFUNDO_FUNCIONAL.json (datos completos)
   # - ANALISIS_PROFUNDO_FUNCIONAL.txt  (reporte legible)

**Ventajas del script:**

- ✅ Automatiza el conteo (ahorra 15-20 min)
- ✅ Detecta elementos especiales (imágenes, tablas)
- ✅ Genera estadísticas precisas
- ✅ Conteo 100% preciso

**Revisar archivo JSON generado:**

.. code-block:: json

   {
     "seccion": "07",
     "analisis_originales": {
       "total_archivos": 13,
       "agrupacion_por_tipo": {
         "tip": 10,
         "ejemplo": 3
       },
       "estadisticas_globales": {
         "total_palabras": 1693,
         "total_lineas": 383,
         "archivos_con_imagenes": 9,
         "total_imagenes": 12
       }
     }
   }

**Usar este JSON para crear inventario:**

.. code-block:: text

   INVENTARIO - SECCIÓN 07: DEPLOYMENT VIEW
   
   Generado con: analisis_profundo_funcional.py
   Fecha: 2026-01-27
   
   ═══════════════════════════════════════════════════════════
   
   RESUMEN (del JSON):
   • Total archivos: 13
   • Tips: 10
   • Ejemplos: 3
   • Total palabras: 1,693
   • Total líneas: 383
   • Archivos con imágenes: 9
   • Total imágenes: 12
   
   ───────────────────────────────────────────────────────────
   
   A. ARCHIVO PRINCIPAL:
      □ Título e introducción
      □ Content
      □ Motivation
      □ Form
      □ Plantilla 7.1 (con subsecciones)
      □ Plantilla 7.2 (con subsecciones)
      □ Further Info
      □ Toctree de tips
      □ Toctree de ejemplos
   
   B. TIPS (del JSON: archivos_individuales):
      □ Tip 7-1: 27 líneas, 136 palabras, tiene imágenes
      □ Tip 7-2: 22 líneas, 114 palabras, tiene tablas
      ...
   
   C. EJEMPLOS:
      □ Ejemplo 1: 63 líneas, tiene imágenes
      ...

**Guardar como:**

.. code-block:: bash

   /tmp/ADT/source/.../XX_seccion_nombre/INVENTARIO_SECCION_XX.txt

**Método 2: Manual**

Si el script no está disponible, crear inventario manualmente:

.. code-block:: text

   INVENTARIO - SECCIÓN XX
   
   A. ARCHIVO PRINCIPAL:
      □ Introducción/Content
      □ Motivation
      □ Form
      □ Plantilla X.1
      □ Plantilla X.2
      □ Further Info
   
   B. TIPS INDIVIDUALES:
      □ Tip X-1 (archivo: XXX.md)
      □ Tip X-2 (archivo: XXX.md)
      ...
   
   C. EJEMPLOS:
      □ Ejemplo 1 (archivo: XXX.md)
      ...

**Tiempo:**

- Con script: 5-10 min
- Manual: 20-30 min

.. important::
   **Recomendación:** Usar SIEMPRE el script si está disponible.
   
   El script está en: ``/tmp/ADT/scripts/analisis_profundo_funcional.py``
   
   Guardar JSON como referencia en raíz de sección.

----

Paso 0.3: Verificar Fuentes de Verdad
--------------------------------------

**Para cada tipo de documento, identificar la fuente correcta:**

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Tipo
     - Fuente de Verdad
     - Notas
   * - Archivo principal
     - Plantilla arc42 (usuario proporciona)
     - Contiene plantillas X.1, X.2, etc.
   * - Tips individuales
     - Archivos .md en ``/original/``
     - NO usar docs.arc42.org
   * - Ejemplos
     - Archivos .md en ``/original/``
     - NO usar docs.arc42.org

**Sobre docs.arc42.org:**

.. warning::
   **docs.arc42.org NO es una fuente diferente.**
   
   Es el renderizado Jekyll de los archivos .md:
   
   .. code-block:: text
   
      Archivos .md (fuente)
            ↓
      Jekyll procesa
            ↓
      docs.arc42.org (web renderizada)
   
   **Diferencias:**
   • Tags: YAML → Links clickeables
   • Imágenes: {{ site.imageurl }} → URLs completas
   • Formato: Markdown → HTML
   
   **PERO:** Contenido textual es idéntico ✓

**Verificación:**

.. code-block:: text

   □ Identifiqué fuente de verdad para archivo principal
   □ Identifiqué fuente de verdad para tips
   □ Identifiqué fuente de verdad para ejemplos
   □ NO hay confusión sobre qué archivo usar
   □ NO voy a usar docs.arc42.org como fuente

----

Paso 0.4: Checklist Pre-Traducción
-----------------------------------

**Antes de pasar a FASE 1, verificar:**

.. code-block:: text

   CHECKLIST PRE-TRADUCCIÓN:
   ═══════════════════════════════════════════════════════════
   
   LECTURA:
   □ Leí la plantilla arc42 COMPLETA de la sección
   □ Leí al menos 2-3 tips de ejemplo
   □ Leí al menos 1 ejemplo de aplicación
   
   IDENTIFICACIÓN:
   □ Identifiqué TODAS las partes del archivo principal
   □ Conté archivos .md en /original/ (tips + ejemplos)
   □ Verifiqué que número de archivos coincide
   
   DOCUMENTACIÓN:
   □ Creé inventario completo en INVENTARIO_SECCION_XX.txt
   □ O ejecuté script y guardé JSON
   □ Documenté total de archivos
   □ Documenté secciones del archivo principal
   
   CLARIDAD:
   □ Sé cuál es la fuente de verdad para archivo principal
   □ Sé cuál es la fuente de verdad para tips
   □ Sé cuál es la fuente de verdad para ejemplos
   □ NO tengo dudas sobre qué traducir
   
   PREPARACIÓN:
   □ Tengo todos los archivos fuente accesibles
   □ Tengo plantilla de sección a mano
   □ Creé estructura de carpetas (/original, /traduccion)
   
   ═══════════════════════════════════════════════════════════
   
   Solo SI TODOS están ✓ → Pasar a FASE 1
   
   Si alguno falta → DETENERSE y completar

**Tiempo invertido en PASO 0:**

- Lectura de plantilla: 5-10 min
- Creación de inventario (con script): 5-10 min
- Verificación de fuentes: 5 min
- **Total: 15-25 min**

**ROI (Retorno de Inversión):**

- Previene omisiones de contenido
- Evita tener que corregir después
- Ahorra horas de retrabajo
- Garantiza traducción completa desde el inicio

----

.. important::
   **Regla de Oro del PASO 0:**
   
   **"Nunca empieces a traducir sin saber TODO lo que vas a traducir."**
   
   25 minutos en PASO 0 ahorran horas de correcciones posteriores.

.. note::
   **Script de automatización:**
   
   Ubicación: ``/tmp/ADT/scripts/analisis_profundo_funcional.py``
   
   Documentación: ``/tmp/README_analisis_profundo.md``

----


FASE 1: Preparación
===================

Paso 1.1: Análisis del Documento Fuente y Clasificación
---------------------------------------------------------

**Objetivo:**
   Entender qué vamos a traducir y clasificarlo según la Guía Metodológica.

**Tareas:**

1. **Leer el documento fuente completo** (o capítulo)
   
   .. code-block:: bash
   
      # Abrir y leer el documento original
      less documento_original.pdf

2. **Clasificar el documento según Guía Metodológica:**
   
   Ver: :doc:`/biblioteca/_metadata_biblioteca/META_BIB_001_Sistema_Clasificacion`
   
   .. code-block:: text
   
      [ ] Categoría Principal (informatica/ingenieria/ciencias)
      [ ] Subcategoría (programacion/sistemas/biologia)
      [ ] Especialidad (full_stack/python/uml)
      [ ] Código de clasificación (ej: INF.PRG.FST.001)

3. **Identificar características del contenido:**
   
   .. code-block:: text
   
      [ ] Número de capítulos
      [ ] ¿Tiene figuras? ¿Cuántas?
      [ ] ¿Tiene tablas? ¿Cuántas?
      [ ] ¿Tiene ecuaciones matemáticas?
      [ ] ¿Tiene código fuente?
      [ ] ¿Tiene referencias bibliográficas?
      [ ] ¿Usa paquetes especiales LaTeX?
      [ ] ¿Tiene comandos custom (\newcommand)?

4. **Evaluar complejidad:**
   
   - **Baja:** Solo texto, secciones, énfasis básico
   - **Media:** + figuras, tablas, ecuaciones simples
   - **Alta:** + código, ecuaciones complejas, paquetes custom

**Ejemplo de Clasificación:**

.. code-block:: text

   Libro: "Modern Full-Stack Development" (Zammetti, 2024)
   
   Categoría: informatica/
   Subcategoría: programacion/
   Especialidad: full_stack/
   Código: INF.PRG.FST.001
   
   Ubicación final:
   biblioteca/informatica/programacion/full_stack/
   └── Modern_Full_Stack_Development_Zammetti_2ed/

Paso 1.2: Configuración de Estructura en Biblioteca
----------------------------------------------------

**Objetivo:**
   Crear estructura correcta en ``biblioteca/`` según clasificación.

**Tareas:**

1. **Crear estructura base del libro:**
   
   Ver: :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT` sección 10
   
   .. code-block:: bash
   
      # Ejemplo: Libro Full-Stack Development
      cd /tmp/ADT/source/biblioteca
      
      # Crear jerarquía según clasificación
      mkdir -p informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed
      
      cd informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed
      
      # Crear archivos base del libro
      touch metadata_libro.rst
      touch index.rst
      touch glosario_acumulativo.rst

2. **Crear estructura para el capítulo:**
   
   **Importante:** Sin números en nombres de carpeta (cumple NOM_001)
   
   .. code-block:: bash
   
      # Nombre descriptivo del capítulo (SIN número)
      mkdir -p server_side_action_node_npm/{original,traduccion,figuras}
      
      # Crear archivos del capítulo
      touch server_side_action_node_npm/glosario_capitulo.rst
      touch server_side_action_node_npm/notas_traduccion.rst

3. **Copiar/Convertir recursos originales:**
   
   .. code-block:: bash
   
      # Copiar PDF/LaTeX original
      cp ~/original/chapter_01.pdf server_side_action_node_npm/original/
      
      # Copiar figuras del capítulo
      cp ~/original/figures/*.{png,jpg} server_side_action_node_npm/figuras/
      
      # Si hay PDFs en figuras, convertir a PNG
      cd server_side_action_node_npm/figuras
      for f in *.pdf; do
          convert "$f" "${f%.pdf}.png"
      done

4. **Crear metadata del libro:**
   
   .. code-block:: bash
   
      # Editar metadata_libro.rst
      cat > metadata_libro.rst << 'EOF'
      .. meta::
         :libro_id: LIB_INF_FST_001
         :tipo: Libro_Tecnico
         :estado: En_Traduccion
         :progreso: 0%
         :clasificacion: INF.PRG.FST.001
      
      ========================================
      Modern Full-Stack Development (2nd Ed)
      ========================================
      
      Título Original
         Modern Full-Stack Development
      
      Autor
         Frank Zammetti
      
      Editorial
         Apress
      
      Año
         2024
      
      Clasificación
         INF.PRG.FST.001
         (Informática > Programación > Full-Stack)
      EOF

**Estructura Resultante:**

.. code-block:: text

   biblioteca/informatica/programacion/full_stack/
   └── Modern_Full_Stack_Development_Zammetti_2ed/
       ├── metadata_libro.rst
       ├── index.rst
       ├── glosario_acumulativo.rst
       │
       └── server_side_action_node_npm/      # Capítulo 1
           ├── original/
           │   └── chapter_01.pdf
           ├── traduccion/
           │   └── capitulo_01.rst          # A crear en FASE 3
           ├── glosario_capitulo.rst
           ├── notas_traduccion.rst
           └── figuras/
               ├── fig_01_01.png
               └── fig_01_02.png

5. **Verificar configuración Sphinx:**
   
   Asegurar que ``conf.py`` tiene extensiones necesarias:
   
   .. code-block:: python
   
      extensions = [
          'sphinx.ext.autodoc',
          'sphinx.ext.mathjax',        # Para ecuaciones
          'sphinx.ext.napoleon',
          'sphinx.ext.viewcode',
          'sphinxcontrib.bibtex',      # Para bibliografía
      ]

Paso 1.3: Planificación
------------------------

**Objetivo:**
   Decidir estrategia de traducción.

**Decisiones clave:**

1. **¿Modo 1 (Alta Fidelidad) o Modo 2 (Marcado Visual)?**
   
   .. list-table::
      :widths: 50 50
      :header-rows: 1
   
      * - Modo 1: Alta Fidelidad
        - Modo 2: Marcado Visual
      * - Preserva estructura original
        - Añade marcadores visuales
      * - Mínimas adaptaciones
        - Más adaptaciones para claridad
      * - Para: Libros formales, papers
        - Para: Tutoriales, material didáctico

2. **¿Qué objetivos son prioritarios?**
   
   .. code-block:: text
   
      Prioridad Alta:
      [ ] Domesticación (siempre)
      [ ] Claridad (si audiencia es amplia)
      [ ] Consistencia (si original es inconsistente)
      [ ] Simplificación (si original es verboso)

3. **¿Traducir todo o por secciones?**
   
   **Recomendación:** Sección por sección, compilando frecuentemente.

----

FASE 2: Análisis Estructural
=============================

**ACTUALIZADO v1.2.0:** Esta fase ahora incluye herramientas automatizadas.

Paso 2.1: Identificar Jerarquía y Ubicación en Biblioteca
-----------------------------------------------------------

**Objetivo:**
   Mapear estructura del documento y planificar ubicación en biblioteca.

**Para repositorios Markdown/GitHub:**

1. **Usar herramienta de análisis automático:**
   
   .. code-block:: bash
   
      # Analizar sección con Python
      python scripts/analizar_seccion.py sections/02_constraints
   
   Genera:
   
   - Reporte en consola con estructura completa
   - ``analisis_seccion.json`` con datos estructurados

2. **Revisar reporte generado:**
   
   El script identifica automáticamente:
   
   - Total de archivos y tipos
   - Front matter YAML (metadatos)
   - Estructura de headings (jerarquía)
   - Elementos especiales (ver Paso 2.2)

3. **Planificar estructura RST:**
   
   .. code-block:: text
   
      Sección: 02_constraints (6 archivos)
      
      Contenido identificado:
      ├─ 1 Ejemplo (HTML Sanity Checker)
      └─ 5 Tips (2-1 al 2-5)
      
      Propuesta RST:
      ===============
      restricciones.rst
      ├─ Introducción
      ├─ Ejemplo
      └─ Tips 2-1 al 2-5

**Para documentos LaTeX/PDF (método original):**

1. **Extraer estructura del documento:**
   
   .. code-block:: bash
   
      # Para LaTeX: ver estructura de capítulos
      grep -E '\\(chapter|section|subsection)' original.tex
      
      # Para PDF: revisar tabla de contenidos

2. **Crear mapa jerárquico del libro:**
   
   [Proceso existente]

3. **Planificar nombres de carpetas (sin números, descriptivos):**
   
   Ver: :doc:`/docs_maestros/ARQUITECTURA_TRADUCCION_IACT` sección 10.2

4. **Verificar clasificación y ubicación:**
   
   [Proceso existente]

Paso 2.2: Mapear Elementos Especiales
--------------------------------------

**Objetivo:**
   Identificar elementos que requieren atención especial.

**Método automatizado (Markdown/repositorios):**

El script ``analizar_seccion.py`` identifica automáticamente:

.. code-block:: text

   Elementos detectados:
   
   ✅ IMÁGENES:              0
   ✅ TABLAS:                0
   ✅ BLOQUES DE CÓDIGO:     2
   ✅ ENLACES:               3 (internos)
   ✅ DIVS HTML:             1
   ✅ LISTAS BULLET:         4 items

**Plan de conversión:**

1. **DIVs HTML → Directivas RST**
   
   .. code-block:: rst
   
      <!-- HTML -->
      <div class="arc42-example">
      Mensaje
      </div>
      
      <!-- RST -->
      .. note::
         **Ejemplo arc42:**
         
         Mensaje

2. **Enlaces internos → Referencias RST**
   
   .. code-block:: rst
   
      <!-- Markdown -->
      [tip 2-3](/tips/2-3)
      
      <!-- RST -->
      :ref:`tip-2-3`

**Método manual (LaTeX/otros formatos):**

.. code-block:: text

   FIGURAS:
   [ ] Listar todas las figuras
   [ ] Verificar que imágenes existen
   [ ] Planificar conversión si es necesario
   
   TABLAS:
   [ ] Identificar tipo (simple/compleja)
   [ ] Planificar formato RST apropiado
   
   ECUACIONES:
   [ ] Verificar compatibilidad con MathJax
   [ ] Identificar ecuaciones numeradas vs inline
   
   CÓDIGO:
   [ ] Identificar lenguaje
   [ ] Verificar si hay syntax highlighting
   
   REFERENCIAS:
   [ ] Listar \ref{} y planificar :ref:
   [ ] Listar \cite{} y verificar .bib
   
   COMANDOS CUSTOM:
   [ ] Identificar \newcommand
   [ ] Planificar equivalente RST/Sphinx

Paso 2.3: Detectar Inconsistencias
-----------------------------------

**Objetivo:**
   Identificar problemas del original que corregiremos.

**Para repositorios GitHub/Markdown:**

1. **Verificar clasificación de archivos:**
   
   Revisar que todos los archivos pertenecen a la sección:
   
   .. code-block:: text
   
      Archivo: 2021-12-12-t-1-24.md
      Front matter: category: requirements  ← ⚠️ PROBLEMA
      Ubicación: sections/02_constraints/   ← Incorrecto
      
      Acción: NO traducir, documentar problema

2. **Detectar typos en original:**
   
   .. code-block:: text
   
      Ejemplo: "contraints" → debería ser "constraints"
      
      Acción: Corregir silenciosamente en traducción

3. **Verificar enlaces internos:**
   
   .. code-block:: text
   
      Tip 2-3 → referencia a tip 2-4 ✅
      Tip 2-4 → referencia a tip 2-3 ✅
      
      Tipo: Referencias bidireccionales (intencional)

**Para documentos LaTeX:**

1. **Terminología inconsistente:**
   
   .. code-block:: bash
   
      # Buscar variaciones del mismo término
      grep -i "base de datos\|BD\|database" original.tex

2. **Estilos de énfasis variados:**
   
   .. code-block:: bash
   
      # ¿Usa \textbf y \emph para lo mismo?
      grep -E '\\(textbf|emph)' original.tex

3. **Referencias inconsistentes:**
   
   .. code-block:: bash
   
      # Buscar diferentes estilos de referencia
      grep -E '(ver|véase|como se mostró|antes)' original.tex

**Documentar:**

Crear ``FASE_2_ANALISIS_SECCION.txt`` con:

.. code-block:: text

   FASE 2: ANÁLISIS ESTRUCTURAL - Sección XX
   ==========================================
   
   ARCHIVOS ENCONTRADOS:
   [Lista completa]
   
   ELEMENTOS ESPECIALES:
   [Detalle de conversiones necesarias]
   
   PROBLEMAS DETECTADOS:
   [Lista de inconsistencias]
   
   DECISIONES TOMADAS:
   [Plan de traducción]

**Tiempo estimado FASE 2:**

- Con herramienta automatizada: 5-10 min
- Sin herramienta (manual): 10-15 min

----

FASE 3: Traducción Inicial (Método por Defecto)
================================================

Paso 3.1: Segmentación
-----------------------

**Nivel de trabajo:** CAPÍTULO/SECCIÓN (dentro de biblioteca/)

**Proceso:**

1. **Seleccionar un capítulo o sección completa:**
   
   .. code-block:: text
   
      # Estructura del capítulo en biblioteca/
      biblioteca/.../Nombre_Libro/
         └── server_side_action_node_npm/    # Capítulo completo
             ├── original/
             │   └── chapter_01.pdf
             ├── traduccion/
             │   └── capitulo_01.rst         # A crear aquí
             ├── glosario_capitulo.rst
             ├── notas_traduccion.rst
             └── figuras/

2. **IMPORTANTE: Estructura de archivos 1:1**
   
   **Principio fundamental:**
   
   .. important::
      **"Un archivo original → Un archivo traducido"**
      
      Mantener correspondencia 1:1 entre archivos originales y traducidos.
   
   **Para repositorios con múltiples archivos:**
   
   .. code-block:: text
   
      Si original/ tiene 6 archivos .md:
      
      traduccion/ debe tener:
      ├── index.rst (o nombre_seccion.rst)    # Índice con toctree
      ├── archivo_1.rst                       # 1:1 con original
      ├── archivo_2.rst                       # 1:1 con original
      ├── archivo_3.rst                       # 1:1 con original
      ├── archivo_4.rst                       # 1:1 con original
      ├── archivo_5.rst                       # 1:1 con original
      └── archivo_6.rst                       # 1:1 con original
      
      Total: 7 archivos (.rst) = 1 índice + 6 contenido
   
   **Ventajas de estructura 1:1:**
   
   ✅ Facilita mantenimiento
   ✅ Permite trabajar en archivos individuales
   ✅ Clara trazabilidad al original
   ✅ Mejor organización y navegación
   ✅ Compatible con toctree de Sphinx
   
   **NO crear:**
   
   ❌ Un solo archivo monolítico con todo el contenido
   ❌ Mezclar múltiples originales en un solo RST
   
   **Razón:** Dificulta mantenimiento y viola principio 1:1

3. **NO traducir:**
   - Todo el libro de una vez (demasiado)
   - Palabra por palabra (muy granular)
   - Solo títulos (muy superficial)

4. **SÍ traducir:**
   - Capítulo/sección completa con todas sus partes
   - Preservando estructura jerárquica
   - Creando archivos en ``traduccion/`` (ver punto 2)
   - Usando toctree en archivo índice para organizar

Paso 3.2: Rendición (Comando por Comando)
------------------------------------------

**Nivel de mapeo:** COMANDO LaTeX → ELEMENTO RST

**Tabla de rendición básica:**

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - LaTeX
     - RST
     - Notas
   * - ``\section{X}``
     - | ``X``
       | ``===``
     - Nivel 1
   * - ``\subsection{X}``
     - | ``X``
       | ``---``
     - Nivel 2
   * - ``\subsubsection{X}``
     - | ``X``
       | ``~~~``
     - Nivel 3
   * - ``\textbf{X}``
     - ``**X**``
     - Énfasis fuerte
   * - ``\emph{X}``
     - ``*X*``
     - Énfasis moderado
   * - ``\texttt{X}``
     - ````X````
     - Código inline
   * - ``\begin{itemize}``
     - ``-``
     - Lista no numerada
   * - ``\begin{enumerate}``
     - ``1. 2. 3.``
     - Lista numerada
   * - ``\ref{label}``
     - ``:ref:`label```
     - Referencia interna
   * - ``\cite{key}``
     - ``:cite:`key```
     - Citación
   * - ``\label{x}``
     - ``.. _x:``
     - Etiqueta
   * - ``\begin{figure}``
     - ``.. figure::``
     - Figura
   * - ``\begin{table}``
     - ``.. list-table::``
     - Tabla
   * - ``\begin{equation}``
     - ``.. math::``
     - Ecuación
   * - ``\begin{verbatim}``
     - ``.. code-block::``
     - Código

**Proceso:**

.. code-block:: text

   Para cada comando LaTeX:
   1. Buscar en tabla de rendición
   2. Si existe mapeo directo → aplicar
   3. Si NO existe → marcar para revisión

Paso 3.3: Preferencia (Signifié sobre Signifiant) + Revisión
-------------------------------------------------------------

**Principio:**
   Preservar CONTENIDO (función semántica), adaptar FORMA (sintaxis).

**Referencia teórica:**
   :doc:`/01_fundamentos/_fundamentos_conceptuales/signifiant_vs_signifie`

**Ejemplos de aplicación:**

1. **Listas:**
   
   .. code-block:: latex
   
      % LaTeX (Signifiant específico)
      \begin{enumerate}
      \item Primero
      \item Segundo
      \end{enumerate}
   
   .. code-block:: rst
   
      # RST (Signifiant adaptado, Signifié preservado)
      1. Primero
      2. Segundo

2. **Espaciado vertical:**
   
   .. code-block:: latex
   
      % LaTeX
      Párrafo 1
      \vspace{2cm}
      Párrafo 2
   
   .. code-block:: rst
   
      # RST (omitir \vspace - no semántico)
      Párrafo 1
      
      Párrafo 2

3. **Código fuente:**
   
   .. code-block:: latex
   
      % LaTeX
      \begin{verbatim}
      def foo():
          pass
      \end{verbatim}
   
   .. code-block:: rst
   
      # RST (preservar EXACTAMENTE - forma = contenido)
      .. code-block:: python
      
         def foo():
             pass

**Checklist de Revisión de Signifié:**

.. important::
   **DESPUÉS de traducir cada sección, revisar:**

.. code-block:: text

   PRESERVACIÓN DE CONTENIDO (Signifié):
   ─────────────────────────────────────
   [ ] ¿El lector obtiene la MISMA INFORMACIÓN?
   [ ] ¿Se preserva la FUNCIÓN de cada elemento?
   [ ] ¿Las relaciones semánticas están intactas?
   [ ] ¿El significado es equivalente al original?
   
   ADAPTACIÓN DE FORMA (Signifiant):
   ─────────────────────────────────────
   [ ] ¿Usamos sintaxis NATURAL de RST?
   [ ] ¿Evitamos ser demasiado literales?
   [ ] ¿Adaptamos comandos a idioma destino?
   [ ] ¿Omitimos elementos puramente estilísticos?
   
   EVITAR TRADUCCIÓN LITERAL:
   ─────────────────────────────────────
   [ ] ¿Hay traducciones palabra-por-palabra innecesarias?
   [ ] ¿Hay elementos que deberían omitirse?
   [ ] ¿La traducción suena "natural" en RST?
   
   SI CUALQUIER RESPUESTA ES "NO":
   → Revisar y ajustar la traducción

**Ejemplos de qué EVITAR:**

❌ **Traducción demasiado literal:**

.. code-block:: latex

   % LaTeX
   \textbf{importante}

.. code-block:: rst

   # ❌ INCORRECTO (demasiado literal)
   .. textbf::
      importante
   
   # ✅ CORRECTO (preserva función, adapta forma)
   **importante**

❌ **Preservar elementos no semánticos:**

.. code-block:: latex

   % LaTeX
   Párrafo 1
   \vspace{2cm}
   Párrafo 2

.. code-block:: rst

   # ❌ INCORRECTO (preserva espaciado literal)
   Párrafo 1
   
   .. raw:: latex
   
      \vspace{2cm}
   
   Párrafo 2
   
   # ✅ CORRECTO (omite elemento no semántico)
   Párrafo 1
   
   Párrafo 2

**Validación Final:**

.. code-block:: text

   Después de traducir y revisar, preguntar:
   
   ¿El lector obtiene la MISMA INFORMACIÓN que en el original?
   
   SI SÍ: ✅ Signifié preservado → Continuar
   SI NO: ⚠️ Revisar traducción → Ajustar
   
   ¿La traducción usa sintaxis NATURAL de RST?
   
   SI SÍ: ✅ Signifiant adaptado → Continuar
   SI NO: ⚠️ Demasiado literal → Simplificar

**Documentar decisiones:**

Si aplicaste adaptaciones significativas, documentar en ``notas_traduccion.rst``:

.. code-block:: rst

   Decisión: Omitir \vspace{2cm} (puramente estilístico)
   Razón: No aporta valor semántico en RST

**Tiempo estimado FASE 3:**

- Con segmentación clara: 30-45 min por sección/capítulo
- Incluye: traducción + aplicación de checklist + documentación inicial

----

Paso 3.4: Traducción Arquitectónica (CRÍTICO - arc42)
======================================================

.. danger::
   **ESTE PASO ES OBLIGATORIO PARA CONTENIDO TÉCNICO/ARQUITECTÓNICO**
   
   Para traducciones de arc42, documentación arquitectónica, o contenido 
   técnico especializado: **NO traducir literalmente**. Usar **contexto 
   arquitectónico**.

Principio Fundamental
---------------------

.. important::
   **Traducir el CONCEPTO, no las palabras individuales**
   
   En arquitectura de software, muchos términos tienen significados técnicos 
   específicos que NO coinciden con su traducción literal del inglés.

Problema de Traducción Literal
-------------------------------

**Ejemplo del problema:**

.. code-block:: rst

   Original (inglés):
   "Describes the relevant requirements and the driving forces that 
   software architects must consider."
   
   ❌ INCORRECTO (Literal):
   "Describe los requisitos relevantes y las fuerzas impulsoras que 
   los arquitectos de software deben considerar."
   
   ✅ CORRECTO (Contextual):
   "Describe los requisitos relevantes y los factores determinantes que 
   guían las decisiones de los arquitectos de software."

**Por qué es incorrecto:**

- "driving forces" en arquitectura NO son "fuerzas" físicas
- Son **factores** que determinan decisiones arquitectónicas
- "fuerzas impulsoras" suena extraño y no técnico en español

Tabla de Términos Arquitectónicos
----------------------------------

**Términos que SIEMPRE requieren traducción contextual:**

.. list-table:: Glosario de Traducción Arquitectónica arc42
   :header-rows: 1
   :widths: 25 30 45

   * - Inglés
     - ❌ Literal (INCORRECTO)
     - ✅ Contextual (CORRECTO)
   * - **driving forces**
     - fuerzas impulsoras
     - **factores determinantes**, impulsores
   * - **quality goals**
     - objetivos de calidad
     - **atributos de calidad objetivo**
   * - **stakeholder**
     - interesado, parte interesada
     - **stakeholder** (preservar en inglés)
   * - **building block**
     - bloque de construcción
     - **componente**, módulo arquitectónico
   * - **whitebox**
     - caja blanca
     - **vista interna**, descomposición
   * - **blackbox**
     - caja negra
     - **vista externa**, interfaz
   * - **crosscutting**
     - transversal
     - **aspectos transversales**, crosscutting
   * - **deployment view**
     - vista de despliegue
     - **vista de infraestructura**
   * - **runtime view**
     - vista de tiempo de ejecución
     - **vista de comportamiento**
   * - **constraints**
     - restricciones
     - **limitaciones**, restricciones
   * - **scope**
     - alcance
     - **ámbito**, alcance
   * - **motivation**
     - motivación
     - **justificación**, razón de ser

Ejemplos Completos: Literal vs Contextual
------------------------------------------

**Ejemplo 1: Driving Forces**

.. code-block:: rst

   ❌ INCORRECTO (Literal):
   Las fuerzas impulsoras incluyen requisitos funcionales y 
   objetivos de calidad.
   
   ✅ CORRECTO (Contextual):
   Los factores determinantes incluyen requisitos funcionales y 
   atributos de calidad objetivo.

**Contexto arquitectónico:**

   "Driving forces" = Requisitos funcionales clave + Atributos de calidad 
   críticos + Restricciones técnicas/negocio que IMPULSAN decisiones 
   arquitectónicas.

**Ejemplo 2: Quality Goals**

.. code-block:: rst

   ❌ INCORRECTO (Literal):
   Los tres objetivos de calidad principales son performance, 
   seguridad y usabilidad.
   
   ✅ CORRECTO (Contextual):
   Los tres atributos de calidad objetivo principales son performance 
   (< 2s response time), disponibilidad (99.9% uptime) y usabilidad.

**Contexto arquitectónico:**

   "Quality goals" NO son simplemente "objetivos" - son ATRIBUTOS 
   MEDIBLES Y ESPECÍFICOS de la ARQUITECTURA. Deben incluir métricas 
   concretas (ej: Performance < 2s, Availability 99.9%).

**Ejemplo 3: Building Blocks**

.. code-block:: rst

   ❌ INCORRECTO (Literal):
   El sistema está compuesto por cinco bloques de construcción principales.
   
   ✅ CORRECTO (Contextual):
   El sistema está compuesto por cinco componentes arquitectónicos principales.

**Contexto arquitectónico:**

   "Building blocks" = Elementos de la descomposición arquitectónica, 
   organizados jerárquicamente (nivel 1, nivel 2, nivel 3...).

Checklist de Traducción Arquitectónica
---------------------------------------

Antes de finalizar cualquier traducción de arc42, verificar:

.. code-block:: text

   □ "driving forces" → "factores determinantes" (NO "fuerzas impulsoras")
   □ "quality goals" → "atributos de calidad objetivo" (NO solo "objetivos")
   □ "stakeholder" → preservado sin traducir
   □ "building block" → "componente" o "módulo" (NO "bloque de construcción")
   □ "crosscutting" → "aspectos transversales" o preservar
   □ "whitebox/blackbox" → "vista interna/externa" o preservar con explicación
   □ Términos consistentes en TODA la traducción
   □ Glosario actualizado con definiciones arquitectónicas

Términos Técnicos Internacionales
----------------------------------

**Preservar SIN traducir** (términos técnicos estándar):

.. code-block:: rst

   ✅ stakeholder (NO "interesado")
   ✅ quality goals (puede preservarse o traducir contextualmente)
   ✅ runtime (puede preservarse)
   ✅ deployment (puede preservarse)
   ✅ middleware (NO traducir)
   ✅ framework (NO traducir)
   ✅ pattern (puede preservarse como "patrón")
   ✅ refactoring (puede preservarse)

**Razón:** Estos términos son estándares internacionales en gestión de 
proyectos, arquitectura de software e ingeniería de software (PMBoK, 
ISO/IEC 42010, SWEBOK).

Coherencia Terminológica
-------------------------

.. important::
   **Una vez elegida una traducción, mantenerla en TODO el documento**
   
   Si eliges "factores determinantes" para "driving forces":
   → Usar SIEMPRE "factores determinantes"
   → NO cambiar a "impulsores" en otro capítulo
   → Documentar en glosario

Documentación de Decisiones
----------------------------

**En el glosario, agregar:**

.. code-block:: rst

   .. glossary::
   
      Driving forces (Factores determinantes)
         En arquitectura de software, los factores que impulsan y moldean 
         las decisiones arquitectónicas. Incluyen requisitos funcionales 
         clave, atributos de calidad críticos, restricciones técnicas.
         
         **Nota de traducción:** NO traducir literalmente como "fuerzas 
         impulsoras". El término arquitectónico correcto es "factores 
         determinantes".

Referencias de Estándares
--------------------------

**Validar traducciones con:**

- ISO/IEC/IEEE 42010 (Architecture description)
- ISO/IEC 25010 (Systems and software Quality Models)
- IEEE 1471 (Architectural Description)
- SWEBOK v3.0 (Software Engineering Body of Knowledge)
- PMBoK (Project Management Body of Knowledge)

Tiempo Estimado Paso 3.4
-------------------------

- Primera revisión arquitectónica: +15 min por sección
- Consulta de glosario: +5 min
- Actualización de términos: +10 min

**Total adicional:** ~30 min (inversión que evita correcciones posteriores)

.. note::
   **Este paso PREVIENE correcciones masivas posteriores**
   
   Aplicar traducción arquitectónica desde el inicio es más eficiente que 
   corregir todos los archivos después (como sucedió en Lote 1 de sección 01).

----


Paso 3.5: Enriquecimiento Opcional ⚠️ (DECISIÓN CONSCIENTE)
------------------------------------------------------------

.. warning::
   **Este paso es OPCIONAL y debe aplicarse con criterio consciente.**
   
   Solo agregar contenido complementario cuando mejore REALMENTE la comprensión,
   y SIEMPRE debe estar marcado claramente.

**Objetivo:**
   Evaluar si agregar contenido complementario (ejemplos, diagramas, aclaraciones) 
   mejora la comprensión del documento traducido, sin modificar el mensaje original.

**Contexto Importante:**

El problema NO es "agregar contenido". El problema es:

❌ **ERROR:** No traducir COMPLETO el original PRIMERO, y en su lugar solo agregar contenido
✅ **CORRECTO:** Traducir TODO el original PRIMERO, luego opcionalmente agregar contenido MARCADO

Flujo Correcto
~~~~~~~~~~~~~~

.. code-block:: text

   1º → Traducir TODO el original (COMPLETO)
   2º → Aplicar terminología consistente (Paso 3.4)
   3º → OPCIONALMENTE agregar contenido MARCADO
   
   NO AL REVÉS.

Paso 3.5.1: Identificar Oportunidades de Enriquecimiento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preguntas a responder:**

1. ¿Hay un término técnico complejo que requiere aclaración?
2. ¿Un ejemplo visual (PlantUML, Mermaid) mejoraría la comprensión?
3. ¿Un concepto abstracto se beneficiaría de un caso concreto?
4. ¿Una tabla comparativa ayudaría a tomar decisiones?

**Si la respuesta es "SÍ" a alguna pregunta, proceder al siguiente paso.**

Paso 3.5.2: Evaluar Si Agregar Contenido
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Criterios de Decisión
^^^^^^^^^^^^^^^^^^^^^

**✅ SÍ AGREGAR cuando:**

1. **Aclaración de Términos Técnicos Complejos**
   
   - El término es complejo y no tiene explicación en el original
   - Ejemplo: Explicar "cohesión funcional" vs "cohesión secuencial"
   
   .. code-block:: rst
   
      .. note::
         **Contenido complementario en español**
         
         **Tipos de Cohesión:**
         
         - **Cohesión Funcional** (ideal): Elementos realizan única función
         - **Cohesión Secuencial**: Salida de A es entrada de B

2. **Ejemplos Visuales con PlantUML/Mermaid**
   
   - Un diagrama ilustra mejor que solo texto
   - Ejemplo: Diagrama de jerarquía de bloques de construcción
   
   .. code-block:: rst
   
      .. note::
         **Contenido complementario en español**
         
         **Ejemplo visual:**
         
         .. uml::
            
            package "Módulo A" {
              [Componente 1]
              [Componente 2]
            }

3. **Casos Concretos de Aplicación**
   
   - El original describe pero no muestra código
   - Ejemplo: Código Java mostrando estructura de paquetes
   
   .. code-block:: rst
   
      .. note::
         **Contenido complementario en español**
         
         **Ejemplo en Java:**
         
         .. code-block:: java
         
            package com.example.architecture;
            // código ejemplo

4. **Tablas Comparativas para Decisiones**
   
   - Ayuda a tomar decisiones arquitectónicas
   - Ejemplo: Cuándo usar nivel 2 vs nivel 3 de refinamiento
   
   .. code-block:: rst
   
      .. note::
         **Contenido complementario en español**
         
         .. list-table:: Cuándo refinar a nivel 2 vs 3
            :header-rows: 1
            
            * - Criterio
              - Nivel 2
              - Nivel 3
            * - Complejidad
              - Media
              - Alta

**❌ NO AGREGAR cuando:**

1. **Ya está claro en el original**
   
   - El original ya explica bien el concepto
   - No aporta valor adicional real
   - **Resultado:** Contenido redundante

2. **Agrega longitud sin valor**
   
   - Contenido "relleno" innecesario
   - Listas exhaustivas no útiles
   - Ejemplo incorrecto: Listar 10 lenguajes de programación cuando el original solo menciona uno
   - **Resultado:** Documentación inflada

3. **Es opinión personal**
   
   - Juicios de valor no en el original
   - Recomendaciones no respaldadas por el documento original
   - Preferencias personales del traductor
   - **Resultado:** Sesgo en la traducción

4. **Contradice o reemplaza el original**
   
   - Cambia el mensaje del original
   - Sugiere alternativas no mencionadas
   - Modifica la intención del autor
   - **Resultado:** Traducción incorrecta

Paso 3.5.3: Formato OBLIGATORIO para Contenido Agregado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   **TODO contenido agregado DEBE estar marcado con la directiva RST apropiada.**

Formato Estándar
^^^^^^^^^^^^^^^^

.. code-block:: rst

   [Traducción completa del original aquí]
   
   ----
   
   .. note::
      **Contenido complementario en español**
      
      Esta sección fue agregada en la traducción para mejorar 
      la comprensión del concepto original.
      
      [Contenido agregado aquí]
   
   ----
   
   [Continuar con resto de traducción o referencias]

Formatos Alternativos
^^^^^^^^^^^^^^^^^^^^^^

**Para ejemplos adicionales:**

.. code-block:: rst

   .. admonition:: Ejemplo adicional
      :class: note
      
      [Ejemplo agregado]

**Para tips adicionales:**

.. code-block:: rst

   .. tip::
      **Consejo adicional en español**
      
      [Tip agregado]

**Para aclaraciones importantes:**

.. code-block:: rst

   .. important::
      **Aclaración para lectores en español**
      
      [Aclaración agregada]

Paso 3.5.4: Ubicación Correcta del Contenido Agregado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Orden correcto dentro del documento:**

.. code-block:: text

   1. Título del documento
   2. Directivas RST (.. tip::, etc.) con resumen
   3. ---- (separador)
   4. [TRADUCCIÓN COMPLETA DEL ORIGINAL] ← Primero
   5. ---- (separador)
   6. [CONTENIDO COMPLEMENTARIO MARCADO] ← Después
   7. ---- (separador)
   8. Ver También / Referencias
   9. ---- (separador)
   10. .. seealso:: (referencias RST)
   11. ---- (separador)
   12. Metadata (:Tip:, :Tema:, etc.)

**Ejemplo completo de estructura:**

.. code-block:: rst

   .. _ejemplo_tip:
   
   =======================================
   Tip X: Título del Consejo
   =======================================
   
   .. tip::
      **Consejo Principal**
      
      Resumen del consejo en 1-2 líneas.
   
   ----
   
   [FASE 1: TRADUCCIÓN COMPLETA DEL ORIGINAL]
   
   Contenido traducido palabra por palabra del documento original.
   Todos los párrafos, listas, ejemplos del original están aquí.
   
   [FIN DE TRADUCCIÓN ORIGINAL]
   
   ----
   
   [FASE 3.5: ENRIQUECIMIENTO OPCIONAL - SI APLICA]
   
   .. note::
      **Contenido complementario en español**
      
      Esta sección fue agregada para mejorar la comprensión.
      
      [Contenido adicional aquí: diagrama, tabla, ejemplo]
   
   ----
   
   Ver También
   ===========
   
   * Referencia 1
   * Referencia 2
   
   ----
   
   .. seealso::
      * :ref:`seccion_relacionada`
   
   ----
   
   :Tip: X-Y
   :Tema: Descripción
   :Traducción: Método Peshitta + Paso 3.4 + Enriquecimiento
   :Workflow: v1.7.0

Checklist de Enriquecimiento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Antes de agregar contenido, verificar:**

.. code-block:: text

   TRADUCCIÓN BASE:
   [ ] Traduje TODO el contenido del original
   [ ] NO omití ninguna sección del original
   [ ] Preservé la estructura completa del original
   [ ] Apliqué Paso 3.4 (terminología consistente)
   
   EVALUACIÓN DE ENRIQUECIMIENTO:
   [ ] Identifiqué necesidad REAL de contenido adicional
   [ ] El contenido agrega valor REAL (no relleno)
   [ ] NO es opinión personal
   [ ] NO contradice el original
   
   FORMATO Y UBICACIÓN:
   [ ] Contenido marcado con .. note:: o similar
   [ ] Ubicado DESPUÉS de traducción completa
   [ ] Ubicado ANTES de referencias
   [ ] Mensaje claro: "Contenido complementario"
   
   METADATA:
   [ ] Actualizada metadata: "Enriquecimiento" en :Traducción:
   [ ] Workflow actualizado a v1.7.0

Ejemplos de Enriquecimiento Apropiado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Ejemplo 1: Aclaración de Concepto Técnico**

.. code-block:: rst

   [Traducción del original:]
   La cohesión es uno de los principios más fundamentales.
   
   ----
   
   .. note::
      **Contenido complementario en español**
      
      **Niveles de cohesión (de mayor a menor):**
      
      1. Cohesión Funcional - Elementos con una única función
      2. Cohesión Secuencial - Elementos en cadena de procesamiento
      3. Cohesión Comunicacional - Elementos sobre mismos datos

**Ejemplo 2: Diagrama Visual**

.. code-block:: rst

   [Traducción del original:]
   Los bloques de construcción forman una jerarquía.
   
   ----
   
   .. note::
      **Contenido complementario en español**
      
      **Ejemplo de jerarquía con PlantUML:**
      
      .. uml::
         
         package "Nivel 1" {
           [Sistema]
         }
         
         package "Nivel 2" {
           [Módulo A]
           [Módulo B]
         }

**Ejemplo 3: Tabla Comparativa**

.. code-block:: rst

   [Traducción del original:]
   Decide cuándo refinar a niveles más profundos.
   
   ----
   
   .. note::
      **Contenido complementario en español**
      
      .. list-table:: Guía de decisión para refinamiento
         :header-rows: 1
         
         * - Nivel
           - Cuándo usar
           - Cuándo evitar
         * - Nivel 2
           - Complejidad media
           - Sistema muy simple
         * - Nivel 3
           - Complejidad alta
           - Complejidad baja/media

Regla de Oro del Enriquecimiento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   **"Cuando tengas duda sobre agregar contenido, NO lo agregues."**
   
   La traducción completa y fiel del original es SIEMPRE suficiente.
   
   El enriquecimiento es un EXTRA opcional, no un requisito.

Tiempo Estimado Paso 3.5
~~~~~~~~~~~~~~~~~~~~~~~~~

**Si NO se agrega contenido:** 0 min (paso se omite)

**Si SÍ se agrega contenido:**

- Evaluación de oportunidades: 5-10 min
- Creación de contenido (por elemento):
  
  - Aclaración texto: 5-10 min
  - Diagrama PlantUML simple: 10-15 min
  - Tabla comparativa: 10-15 min
  - Ejemplo de código: 15-20 min

**Total estimado:** 15-60 min (dependiendo de cantidad de enriquecimiento)

.. note::
   **Este paso es completamente OPCIONAL**
   
   Si el documento original es claro y completo, puedes omitir este paso
   y proceder directamente a FASE 3.6: Revisión de Literalidad.

FASE 3.6: Revisión de Literalidad (CRÍTICO)
============================================

.. important::
   **Este paso es OBLIGATORIO y NO debe saltarse.**
   
   Después de completar la traducción inicial (FASE 3), SIEMPRE revisar 
   archivo por archivo para detectar y corregir traducciones demasiado literales.
   
   **Nota:** Si aplicaste correctamente el **Paso 3.4: Traducción Arquitectónica** 
   durante la traducción, esta fase será mucho más rápida, ya que los términos 
   técnicos ya estarán correctamente traducidos.

Paso 3.6.1: Revisión Sistemática
---------------------------------

**Objetivo:**
   Verificar que NO fuimos demasiado literales en las traducciones.

**Proceso:**

1. **Revisar CADA archivo traducido contra su original:**

   .. code-block:: text
   
      Para cada archivo RST traducido:
      
      1. Abrir archivo original (LaTeX/Markdown/etc.)
      2. Abrir archivo traducido (RST)
      3. Comparar línea por línea
      4. Aplicar checklist de revisión (ver abajo)
      5. Verificar términos arquitectónicos (Paso 3.4)
      6. Documentar problemas encontrados
      7. Ajustar si es necesario

2. **Aplicar checklist de revisión (del Paso 3.3 + Paso 3.4):**

   .. code-block:: text
   
      PARA CADA ARCHIVO:
      
      PRESERVACIÓN DE CONTENIDO (Signifié):
      [ ] ¿El lector obtiene la MISMA INFORMACIÓN?
      [ ] ¿Se preserva la FUNCIÓN de cada elemento?
      [ ] ¿Las relaciones semánticas están intactas?
      [ ] ¿El significado es equivalente?
      
      ADAPTACIÓN DE FORMA (Signifiant):
      [ ] ¿Usamos sintaxis NATURAL de RST?
      [ ] ¿Evitamos ser demasiado literales?
      [ ] ¿Adaptamos comandos a idioma destino?
      [ ] ¿Omitimos elementos puramente estilísticos?
      
      EVITAR TRADUCCIÓN LITERAL:
      [ ] ¿Hay traducciones palabra-por-palabra innecesarias?
      [ ] ¿Hay elementos que deberían omitirse?
      [ ] ¿La traducción suena "natural" en RST?
      [ ] ¿Hay metadatos innecesarios del formato original?
      
      VERIFICACIÓN ARQUITECTÓNICA (Paso 3.4 - CRÍTICO para arc42):
      [ ] "driving forces" → "factores determinantes" (NO "fuerzas impulsoras")
      [ ] "quality goals" → "atributos de calidad objetivo" (NO solo "objetivos")
      [ ] "stakeholder" → preservado sin traducir
      [ ] "building block" → "componente/módulo" (NO "bloque de construcción")
      [ ] Términos técnicos consistentes en TODO el documento
      [ ] Glosario actualizado con definiciones arquitectónicas

3. **Detectar patrones comunes de literalidad:**

   .. code-block:: text
   
      PATRONES TÍPICOS A REVISAR:
      
      ❌ "Debes hacer X" (literal de "You should do X")
         → ✅ "Haz X" o "Hacer X" (imperativo directo)
      
      ❌ "puede ser explicado" (literal de "can be explained")
         → ✅ "se explica" o "suele explicarse"
      
      ❌ Metadatos del formato original (:layout:, :permalink:)
         → ✅ Eliminar (no son semánticos)
      
      ❌ Construcciones muy cercanas al original
         → ✅ Naturalizar al español
      
      PATRONES ARQUITECTÓNICOS (arc42):
      
      ❌ "las fuerzas impulsoras del sistema"
         → ✅ "los factores determinantes del sistema"
      
      ❌ "los objetivos de calidad incluyen..."
         → ✅ "los atributos de calidad objetivo incluyen..."
      
      ❌ "los bloques de construcción principales"
         → ✅ "los componentes arquitectónicos principales"
      
      ❌ "las partes interesadas del proyecto"
         → ✅ "los stakeholders del proyecto"

Paso 3.6.2: Documentar Problemas Encontrados
---------------------------------------------

**Crear documento de revisión:**

.. code-block:: text

   Archivo: REVISION_LITERALIDAD_SECCION_XX.txt
   
   Contenido:
   
   ARCHIVO 1: nombre_archivo.rst
   ────────────────────────────────────────
   
   PROBLEMAS ENCONTRADOS:
   1. Línea 15: "Debes aclarar" → "Aclara"
   2. Línea 22: Metadatos innecesarios
   
   DECISIÓN: AJUSTAR
   
   ARCHIVO 2: otro_archivo.rst
   ────────────────────────────────────────
   
   PROBLEMAS ENCONTRADOS:
   Ninguno
   
   DECISIÓN: OK como está

Paso 3.6.3: Aplicar Ajustes
----------------------------

**Para cada problema identificado:**

1. **Priorizar ajustes:**

   .. code-block:: text
   
      PRIORIDAD ALTA (crítico):
      - Literalidad excesiva que afecta naturalidad
      - Metadatos innecesarios que ensucian el documento
      
      PRIORIDAD MEDIA:
      - Construcciones que podrían ser más naturales
      
      PRIORIDAD BAJA (opcional):
      - Mejoras menores de estilo

2. **Aplicar cambios:**

   Modificar archivos traducidos según prioridades.

3. **Documentar en notas_traduccion.rst:**

   .. code-block:: rst
   
      Ajustes Aplicados en Revisión de Literalidad
      =============================================
      
      Archivo: restricciones_tip-2.rst
      ────────────────────────────────
      
      Problema: "Debes aclarar" (literal de "You should clarify")
      Ajuste: "Aclara" (imperativo directo, más natural)
      Razón: En español técnico, imperativo es más idiomático

Paso 3.6.4: Validación Post-Ajustes
------------------------------------

**Verificar que ajustes no rompieron nada:**

.. code-block:: text

   DESPUÉS DE AJUSTAR:
   
   [ ] ¿Referencias cruzadas siguen funcionando?
   [ ] ¿Etiquetas de referencia intactas?
   [ ] ¿Contenido preservado? (Signifié)
   [ ] ¿Forma más natural? (Signifiant)
   [ ] ¿Archivos compilan? (verificar en FASE 5)

**Tiempo estimado FASE 3.6:**

- 15-30 min por sección (depende de cantidad de archivos)
- CRÍTICO: No saltarse este paso

**Regla de oro:**

.. important::
   **"Si no revisaste la literalidad, no terminaste FASE 3"**
   
   Este paso es TAN importante como la traducción misma.

----

FASE 3.7: VERIFICACIÓN CONTRA ORIGINAL ★★★ (CON BUCLE)
=======================================================

.. important::
   **OBLIGATORIO:** Verificación sistemática con bucle.
   
   Esta fase previene declarar "completo" prematuramente.

**Cuándo ejecutar:**

Inmediatamente DESPUÉS de completar FASE 3.6.
ANTES de pasar a FASE 4.
ANTES de declarar "traducción completa".

**Tiempo estimado:** 20-40 minutos (puede repetirse 2-3 veces)

----

Paso 3.7.1: Comparar Contra Inventario
---------------------------------------

**Método 1: Automático con Script (RECOMENDADO)**

Ejecutar script nuevamente DESPUÉS de traducir:

.. code-block:: bash

   # Ejecutar análisis (ahora con traducciones)
   python3 /tmp/ADT/scripts/analisis_profundo_funcional.py 07
   
   # Esto genera nuevo JSON con verificación de traducciones

**Revisar sección "verificacion_traducciones" del JSON:**

.. code-block:: json

   {
     "verificacion_traducciones": {
       "total_originales": 13,
       "total_traducciones": 13,
       "traducciones_faltantes": [],
       "comparaciones": [...],
       "estadisticas_completitud": {
         "completas": 0,
         "incompletas": 13,
         "similitud_promedio": "0.79%"
       }
     }
   }

**Análisis del reporte:**

1. **total_traducciones vs total_originales:**
   
   .. code-block:: text
   
      □ ¿Son iguales? → SI: ✓ todos los archivos existen
                        NO: ❌ faltan archivos

2. **traducciones_faltantes:**
   
   .. code-block:: text
   
      □ Lista vacía [] → ✓ No falta ningún archivo
      □ Lista con archivos → ❌ Traducir archivos faltantes

3. **similitud_promedio:**
   
   .. important::
      La similitud baja (< 5%) es NORMAL en .md → .rst
      
      Razón: Formato diferente (Markdown vs reStructuredText)
      NO indica traducciones incompletas.

**Ventajas del script:**

- ✅ Automatiza verificación (ahorra 20-25 min)
- ✅ Detecta archivos faltantes
- ✅ Genera reporte estructurado
- ✅ Conteo 100% preciso

**Complementar con verificación manual:**

Aunque el script automatiza mucho, también verificar manualmente:

.. code-block:: text

   VERIFICACIÓN MANUAL - ARCHIVO PRINCIPAL:
   
   □ Content (descripción) → ¿Completa?
   □ Motivation → ¿Completa?
   □ Form → ¿Completa?
   □ Plantilla X.1 → ¿Con todas subsecciones?
   □ Plantilla X.2 → ¿Con todas subsecciones?
   □ Further Info → ¿Completa?

**Método 2: Manual (si script no disponible)**

Usar inventario creado en PASO 0:

.. code-block:: text

   VERIFICACIÓN - ARCHIVO PRINCIPAL:
   
   seccion_XX_nombre.rst:
   
   □ Título e introducción → ¿Traducido?
   □ Content (descripción) → ¿Completa?
   □ Motivation → ¿Completa?
   □ Form → ¿Completa?
   □ Toctree tips → ¿Todos los archivos listados?
   □ Toctree ejemplos → ¿Todos los archivos listados?
   □ Plantilla X.1 → ¿Con todas subsecciones?
   □ Plantilla X.2 → ¿Con todas subsecciones?
   □ Further Info → ¿Traducido?
   
   VERIFICACIÓN - TIPS:
   
   □ Tip X-1 → ¿Completo? (comparar líneas)
   □ Tip X-2 → ¿Completo?
   ...
   
   VERIFICACIÓN - EJEMPLOS:
   
   □ Ejemplo 1 → ¿Completo?
   ...

**Criterios de completitud:**

1. **Longitud:**
   - Diferencia < 30%: Probablemente OK
   - Diferencia > 30%: REVISAR

2. **Secciones:**
   - Mismo número de headings: OK
   - Faltan headings: INCOMPLETO

3. **Elementos especiales:**
   - Tablas: Todas traducidas
   - Figuras: Todas referenciadas
   - Listas: Todas traducidas
   - Code blocks: Todos presentes

**Tiempo:**

- Con script: 10-15 min
- Manual: 30-40 min

----

Paso 3.7.2: Pregunta Crítica
-----------------------------

.. important::
   **¿Está TODO traducido?**
   
   Esta pregunta determina si continuar o regresar.

**Evaluación honesta:**

.. code-block:: text

   Responder SÍ solo si:
   
   ✓ Todos los archivos de inventario existen
   ✓ Todos los archivos están completos
   ✓ Archivo principal tiene todas las secciones
   ✓ Archivo principal tiene todas las plantillas
   ✓ No hay secciones omitidas
   ✓ Longitud apropiada vs original
   ✓ Todos los elementos especiales traducidos
   
   Si alguno falta → Responder NO

**Decisión:**

- **SÍ** → Pasar a Paso 3.7.4 (documentar) y luego a FASE 4
- **NO** → Ejecutar Paso 3.7.3 (bucle)

----

Paso 3.7.3: BUCLE DE VERIFICACIÓN
----------------------------------

**Si respuesta fue NO, ejecutar este bucle:**

.. code-block:: text

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │  PASO 3.7.2: ¿TODO traducido?                     │
   │                                                     │
   └──────────────────────┬──────────────────────────────┘
                          │
               ┌──────────┴──────────┐
               │                     │
              NO                    SÍ
               │                     │
               ↓                     ↓
   ┌───────────────────────┐  ┌──────────────────┐
   │                       │  │                  │
   │  PASO 3.7.3:         │  │  PASO 3.7.4      │
   │  VOLVER A FASE 3     │  │  DOCUMENTAR      │
   │                       │  │                  │
   │  1. Identificar lo   │  │  Luego:          │
   │     que falta        │  │  CONTINUAR A     │
   │                       │  │  FASE 4          │
   │  2. Traducir         │  │                  │
   │     faltante         │  │  (Validado)      │
   │                       │  │                  │
   │  3. Actualizar       │  └──────────────────┘
   │     archivo          │
   │                       │
   └───────┬───────────────┘
           │
           │ (Traducción de faltante completada)
           │
           ↓
   ┌───────────────────────┐
   │                       │
   │  PASO 3.7.2          │
   │  (OTRA VEZ)          │
   │                       │
   │  ¿Ahora sí está      │
   │   TODO traducido?    │
   │                       │
   └───────────────────────┘

**Acciones en el bucle:**

1. **Identificar faltantes:**
   
   .. code-block:: text
   
      Faltantes detectados:
      • Sección "Motivation" del archivo principal
      • Plantilla X.1 (solo tiene título, faltan subsecciones)
      • Tip X-5 (traducido solo 50%)

2. **Traducir faltantes:**
   
   - Volver a archivos originales
   - Traducir contenido faltante
   - Aplicar Pasos 3.4 (terminología) y 3.5 (enriquecimiento)
   - Actualizar archivo .rst

3. **Verificar nuevamente:**
   
   - Ejecutar Paso 3.7.1 otra vez
   - Responder Paso 3.7.2 otra vez
   - Si TODO → Paso 3.7.4
   - Si falta algo → Repetir bucle

**Límite de iteraciones:**

- Máximo recomendado: 3 iteraciones
- Si después de 3 iteraciones aún falta contenido:
  - Revisar inventario (¿está mal el inventario?)
  - Revisar fuentes (¿estás usando fuente correcta?)
  - Pedir ayuda / revisión externa

----

Paso 3.7.4: Documentar Verificación
------------------------------------

**Crear archivo de documentación:**

.. code-block:: bash

   /tmp/ADT/source/.../XX_seccion_nombre/
   VERIFICACION_COMPLETITUD_SECCION_XX.txt

**Formato del archivo:**

.. code-block:: text

   VERIFICACIÓN DE COMPLETITUD
   Sección: XX - Nombre de Sección
   
   ═══════════════════════════════════════════════════════════
   
   ITERACIÓN 1
   ───────────────────────────────────────────────────────────
   Fecha: YYYY-MM-DD HH:MM
   
   Pregunta: ¿Está TODO traducido?
   Respuesta: NO
   
   Faltantes identificados:
   • Archivo principal:
     - Sección "Motivation" (omitida)
     - Plantilla X.1 (incompleta, faltan subsecciones)
   • Tip X-5:
     - Traducido solo 60% (falta sección "Delegate")
   
   Acción tomada: VOLVER a FASE 3
   Tiempo invertido en traducir faltantes: 45 minutos
   
   ═══════════════════════════════════════════════════════════
   
   ITERACIÓN 2
   ───────────────────────────────────────────────────────────
   Fecha: YYYY-MM-DD HH:MM
   
   Pregunta: ¿Está TODO traducido?
   Respuesta: SÍ
   
   Verificación realizada:
   ✓ Archivo principal: 237 líneas (completo)
   ✓ Todos los tips: 10/10 completos
   ✓ Todos los ejemplos: 3/3 completos
   ✓ Longitud apropiada (diferencia < 20%)
   ✓ Todas las secciones presentes
   ✓ Todas las plantillas completas
   
   Acción tomada: CONTINUAR a FASE 4
   
   ═══════════════════════════════════════════════════════════
   
   RESULTADO FINAL: VERIFICACIÓN EXITOSA
   Total iteraciones: 2
   Tiempo total en verificación: 1.5 horas
   
   Estado: ✅ COMPLETO - Listo para FASE 4

**Beneficios de documentar:**

- Trazabilidad del proceso
- Evidencia de verificación
- Aprendizaje para futuras secciones
- Referencia para revisiones

**Guardar también:**

- JSONs del script (antes y después de traducir)
- Ubicación: Raíz de la sección

----

.. warning::
   **PROHIBIDO:**
   
   • NO pasar a FASE 4 sin ejecutar FASE 3.7
   • NO declarar "completo" sin verificar contra inventario
   • NO omitir documentación de verificación
   • NO crear checkpoints antes de completar FASE 3.7

.. important::
   **Regla de Oro de FASE 3.7:**
   
   **"Solo se declara 'completo' después de verificar contra inventario."**
   
   El bucle puede parecer tedioso, pero previene horas de retrabajo.

.. note::
   **Uso correcto del script:**
   
   1. Ejecutar ANTES de traducir (PASO 0) → Genera baseline
   2. Ejecutar DESPUÉS de traducir (FASE 3.7) → Verifica completitud
   3. Comparar ambos JSONs para detectar diferencias
   
   **Ubicación:** ``/tmp/ADT/scripts/analisis_profundo_funcional.py``

----

**Pasar a:** FASE 4 (solo si verificación exitosa)

----


----

FASE 4: Aplicación de Tácticas
===============================

Paso 4.1: Identificar Necesidad de Divergencia
-----------------------------------------------

**Pregunta:**
   ¿El método por defecto es suficiente o necesitamos desviarnos?

**Criterios para divergir:**

.. code-block:: text

   Divergir SI:
   [ ] Original usa construcción no idiomática para RST
   [ ] Contenido necesita aclaración
   [ ] Hay inconsistencias en el original
   [ ] Hay complejidad innecesaria
   
   NO divergir SI:
   [ ] Método por defecto funciona bien
   [ ] No hay objetivo claro para divergencia

Paso 4.2: Seleccionar Objetivo
-------------------------------

**Los 4 objetivos:**

1. **Domesticación** → ¿Necesita adaptarse a RST/Sphinx?
2. **Claridad** → ¿Necesita ser más comprensible?
3. **Consistencia** → ¿Hay inconsistencias que resolver?
4. **Simplificación** → ¿Hay complejidad innecesaria?

**Seleccionar UNO (máximo dos) más relevante.**

Paso 4.3: Aplicar Táctica Apropiada
------------------------------------

**Consultar:** :doc:`/01_fundamentos/objetivos_tacticas`

**Matriz resumida:**

.. code-block:: text

   DOMESTICACIÓN → Sustitución, Normalización, Modulación
   CLARIDAD → Adición, Especificación, Explicación
   CONSISTENCIA → Normalización, Generalización
   SIMPLIFICACIÓN → Omisión, Condensación

**Ejemplo práctico:**

.. code-block:: latex

   % Original (problema: referencia vaga)
   Como se mencionó anteriormente...

**Análisis:**

- Método por defecto: Traducir literal
- Problema: Vago (¿dónde exactamente?)
- Objetivo: Claridad
- Táctica: Especificación

**Traducción:**

.. code-block:: rst

   # RST (táctica aplicada)
   Como se mencionó en :ref:`seccion-introduccion`...

Paso 4.4: Documentar Decisión
------------------------------

**SIEMPRE documentar divergencias significativas:**

.. code-block:: rst

   .. note::
      **Decisión de traducción:**
      
      Original: "Como se mencionó anteriormente"
      Problema: Referencia vaga
      Objetivo: Claridad
      Táctica: Especificación
      Resultado: :ref:`seccion-introduccion` (explícito)

----

FASE 5: Validación
==================

Paso 5.1: Compilación
---------------------

**Después de traducir cada capítulo:**

.. code-block:: bash

   # Navegar a raíz del proyecto
   cd /tmp/ADT
   
   # Limpiar compilación anterior
   make clean
   
   # Compilar
   make html
   
   # Verificar resultado del capítulo específico
   firefox build/html/biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed/server_side_action_node_npm/capitulo_01.html

**Verificar:**

.. code-block:: text

   [ ] Compila sin errores
   [ ] Sin warnings críticos
   [ ] HTML generado existe en ruta correcta biblioteca/
   [ ] Glosario del capítulo se generó
   [ ] Figuras se muestran correctamente

Paso 5.2: Preservación Semántica
---------------------------------

**Checklist de completitud:**

.. code-block:: text

   CONTENIDO:
   [ ] Todas las secciones presentes
   [ ] Todos los párrafos traducidos
   [ ] Todas las figuras incluidas
   [ ] Todas las tablas presentes
   [ ] Todas las ecuaciones convertidas
   
   REFERENCIAS:
   [ ] Todos los \ref convertidos a :ref:
   [ ] Todos los \cite convertidos a :cite:
   [ ] Todas las etiquetas (\label) como .. _etiqueta:
   [ ] Referencias funcionan (clic va al destino)
   
   EXACTITUD:
   [ ] Código fuente sin cambios
   [ ] Ecuaciones matemáticas correctas
   [ ] Nombres propios preservados
   [ ] Números/datos exactos

Paso 5.3: Calidad Visual
-------------------------

**Revisar HTML generado:**

.. code-block:: text

   TIPOGRAFÍA:
   [ ] Títulos con jerarquía correcta
   [ ] Énfasis visible
   [ ] Código formateado correctamente
   
   LAYOUT:
   [ ] Figuras con buen tamaño
   [ ] Tablas legibles
   [ ] Ecuaciones bien renderizadas
   [ ] Espaciado apropiado
   
   NAVEGACIÓN:
   [ ] TOC (tabla de contenidos) completo
   [ ] Enlaces internos funcionan
   [ ] Enlaces externos (si hay) funcionan

----

FASE 5.5: Documentación de Sección ★ (NUEVA - OBLIGATORIA)
==========================================================

.. important::
   **CUÁNDO EJECUTAR:**
   
   - Después de traducir TODA una sección/capítulo completo
   - Después de FASE 5 (Validación)
   - ANTES de considerar la sección "completa"
   - ANTES de pasar a la siguiente sección

.. warning::
   **NUNCA OMITIR ESTA FASE**
   
   Sin esta fase:
   
   - ❌ No hay forma de verificar completitud
   - ❌ Inconsistencia entre secciones
   - ❌ Pérdida de contenido (subsecciones, plantillas)
   - ❌ Metadata incompleta
   - ❌ Dificulta auditorías futuras

Paso 5.5.1: Verificación de Completitud ★★★
--------------------------------------------

.. important::
   **ESTE ES EL PASO MÁS CRÍTICO DE LA FASE 5.5**
   
   Verificar que TODO el contenido del documento original esté traducido.

**Proceso de Verificación:**

1. **Obtener documento original completo:**

   .. code-block:: bash
   
      # Para documentación arc42
      cd /ruta/a/seccion_original
      cat section-X.md  # o equivalente
      
      # Para libros LaTeX
      cat capitulo_original.tex

2. **Comparar estructuras:**

   .. code-block:: text
   
      DOCUMENTO ORIGINAL                    TRADUCCIÓN
      ├─ Sección Principal                 ├─ ✅ seccion_X_principal.rst
      ├─ Subsección 1.1                    ├─ ✅ seccion_1_1.rst
      ├─ Subsección 1.2                    ├─ ✅ seccion_1_2.rst
      ├─ Subsección 1.3                    ├─ ⚠️  FALTA? ← VERIFICAR
      ├─ Ejemplo 1                         ├─ ✅ ejemplo_1.rst
      ├─ Ejemplo 2                         ├─ ✅ ejemplo_2.rst
      ├─ Tips (1-24)                       ├─ ✅ tip_1.rst ... tip_24.rst
      └─ Plantilla / Template              └─ ⚠️  FALTA? ← VERIFICAR

3. **Checklist de Completitud:**

   .. code-block:: text
   
      CONTENIDO PRINCIPAL:
      [ ] Todas las secciones numeradas traducidas
      [ ] Todas las subsecciones traducidas
      [ ] Todos los apéndices traducidos
      
      CONTENIDO SECUNDARIO (CRÍTICO - A MENUDO SE OLVIDA):
      [ ] Plantillas / Templates del documento original
      [ ] Subsecciones de plantilla (e.g., 1.1, 1.2, 1.3 en arc42)
      [ ] Ejemplos prácticos
      [ ] Tips / Consejos
      [ ] Anexos
      [ ] Índices
      
      ELEMENTOS:
      [ ] Todas las figuras
      [ ] Todas las tablas
      [ ] Todos los code-blocks
      [ ] Todas las ecuaciones (si aplica)
      
      REFERENCIAS:
      [ ] Glosario completo
      [ ] Notas de traducción
      [ ] Referencias bibliográficas

4. **Acción si falta contenido:**

   .. code-block:: bash
   
      # SI FALTA CONTENIDO - REGRESAR A FASE 3
      echo "❌ CONTENIDO INCOMPLETO - Faltan subsecciones"
      echo "Regresando a FASE 3 para traducir contenido faltante"
      
      # Traducir contenido faltante con Workflow v1.5.0+
      # (aplicando Paso 3.4 si es contenido arquitectónico)
      
      # Luego regresar a FASE 5.5.1

**Ejemplo - Lección de Sección 01 (arc42):**

.. note::
   **CASO REAL - Lo que descubrimos:**
   
   Inicialmente tradujimos:
   
   - ✅ 4 ejemplos
   - ✅ 24 tips
   - ❌ FALTABAN las 3 subsecciones de plantilla (1.1, 1.2, 1.3)
   
   **Al revisar el documento original completo:**
   
   - Encontramos que había subsecciones 1.1, 1.2, 1.3 con plantillas
   - Estas subsecciones SON PARTE del contenido oficial arc42
   - No se deben omitir
   
   **Lección:** SIEMPRE verificar contra documento original completo, 
   no asumir que todo está traducido.

Paso 5.5.2: Creación de section-X.txt ★★★
------------------------------------------

.. important::
   **ARCHIVO OBLIGATORIO**
   
   Cada sección DEBE tener un archivo section-X.txt con el contenido 
   completo en formato texto plano.

**Propósito:**

- Consulta rápida sin compilar Sphinx
- Plantillas copiables directamente
- Backup completo de información
- Referencia humano-legible
- Documentación independiente del sistema de build

**Contenido Mínimo Requerido:**

.. code-block:: text

   ================================================================================
   SECTION X: [TÍTULO EN INGLÉS]
   ================================================================================
   arc42 / [Nombre del Libro]
   Translated to Spanish | Método Peshitta + Workflow v1.X.X
   ================================================================================
   
   SOURCE DOCUMENT: section-X ([Título])
   TRANSLATION DATE: YYYY-MM-DD
   WORKFLOW VERSION: v1.X.X
   STATUS: ✅ 100% COMPLETE (X files)
   
   ================================================================================
   CONTENT OVERVIEW
   ================================================================================
   
   [Descripción general del contenido de la sección]
   
   ================================================================================
   STRUCTURE
   ================================================================================
   
   SECTION X: [TÍTULO]
   │
   ├─ X.1 [SUBSECCIÓN 1]
   │   └─ [Descripción]
   │
   ├─ X.2 [SUBSECCIÓN 2]
   │   └─ [Descripción]
   │
   └─ X.3 [SUBSECCIÓN 3]
       └─ [Descripción]
   
   ================================================================================
   TRANSLATED FILES (X TOTAL)
   ================================================================================
   
   SUBSECTIONS (X files):
   ────────────────────────────────────────────────────────────────────────
   1. seccion_X_1.rst
      - X.1 [Título]
      - [Descripción]
      - Terminology: "term" → "traducción"
   
   EXAMPLES (X files):
   ────────────────────────────────────────────────────────────────────────
   ...
   
   TIPS (X files):
   ────────────────────────────────────────────────────────────────────────
   ...
   
   ================================================================================
   ARCHITECTURAL TERMINOLOGY (Step 3.4 Applied - if applicable)
   ================================================================================
   
   CRITICAL TRANSLATIONS:
   ┌─────────────────────┬──────────────────────────────────────────────┐
   │ English Term        │ Spanish Translation                          │
   ├─────────────────────┼──────────────────────────────────────────────┤
   │ [term 1]            │ ✅ [traducción correcta]                     │
   │                     │ ❌ NOT "[traducción literal incorrecta]"     │
   └─────────────────────┴──────────────────────────────────────────────┘
   
   ================================================================================
   SUBSECTION X.1: [TÍTULO]
   ================================================================================
   
   CONTENT:
   [Qué contiene]
   
   MOTIVATION:
   [Por qué es importante]
   
   FORM:
   [Cómo documentarlo]
   
   EXAMPLES:
   [Ejemplos disponibles]
   
   TEMPLATE:
   ```
   [Plantilla lista para copiar]
   ```
   
   [Repetir para cada subsección]
   
   ================================================================================
   TRANSLATION STATISTICS
   ================================================================================
   
   [Métricas de traducción]
   
   ================================================================================
   REFERENCES
   ================================================================================
   
   [Referencias oficiales]
   
   ================================================================================
   LICENSE
   ================================================================================
   
   Original content: [Licencia]
   Translation: [Licencia]
   
   ================================================================================
   TRANSLATION INFORMATION
   ================================================================================
   
   Method: Peshitta Method + ADT Workflow v1.X.X
   Date: YYYY-MM-DD
   Status: ✅ 100% COMPLETE
   
   ================================================================================
   END OF SECTION X CONTENT
   ================================================================================

**Ubicación:**

.. code-block:: bash

   # Para arc42
   /sections/0X_section_name/section-X.txt
   
   # Para libros en biblioteca
   /biblioteca/.../Nombre_Libro/capitulo_XX/section-X.txt

**Ejemplo de Creación:**

.. code-block:: bash

   # Crear archivo section-1.txt para Sección 01 de arc42
   cd /sections/01_introduction_goals/
   
   # Crear con el contenido completo
   vim section-1.txt
   
   # Verificar tamaño (debe tener contenido sustancial)
   wc -l section-1.txt
   # Esperado: ~500-1000 líneas dependiendo del contenido

Paso 5.5.3: Creación de section-X.json ★★★
-------------------------------------------

.. important::
   **ARCHIVO OBLIGATORIO**
   
   Cada sección DEBE tener un archivo section-X.json con metadata 
   estructurada en formato JSON.

**Propósito:**

- Metadata estructurada para procesamiento automatizado
- Fácil parsing con scripts Python/JavaScript
- Integración con herramientas de análisis
- Validación de calidad automatizada
- Generación de reportes

**Estructura Mínima Requerida:**

.. code-block:: json

   {
     "section": {
       "number": "XX",
       "title_en": "[Título en inglés]",
       "title_es": "[Título en español]",
       "arc42_template": "section-X",
       "status": "complete",
       "completion_percentage": 100,
       "translation_date": "YYYY-MM-DD",
       "workflow_version": "v1.X.X"
     },
     
     "translation": {
       "method": "Peshitta + ADT Workflow v1.X.X",
       "source_language": "English",
       "target_language": "Spanish",
       "source_format": "Markdown",
       "target_format": "reStructuredText",
       "architectural_terminology_applied": true,
       "step_3_4_applied": true
     },
     
     "files": {
       "total": XX,
       "subsections": X,
       "examples": X,
       "tips": X,
       "breakdown": {
         "subsections": [
           {
             "number": "X.1",
             "title_en": "[Título]",
             "title_es": "[Título]",
             "filename": "seccion_X_1.rst",
             "workflow": "v1.X.X",
             "lines": XXX,
             "key_terminology": {
               "term_en": "traducción_es"
             }
           }
         ],
         "examples": [...],
         "tips": [...]
       }
     },
     
     "terminology": {
       "architectural_terms": {
         "term_1": {
           "translation": "traducción correcta",
           "incorrect_literal": "traducción literal incorrecta",
           "rationale": "Razón para la traducción",
           "occurrences": XX,
           "consistency": "100%"
         }
       },
       "overall_consistency": "100%"
     },
     
     "statistics": {
       "lines": {
         "original_approximate": XXX,
         "translated_approximate": XXX,
         "expansion_ratio": X.XX
       },
       "elements": {
         "figures": XX,
         "tables": XX,
         "code_blocks": XX,
         "external_links": XX
       }
     },
     
     "quality_assurance": {
       "architectural_terminology_verified": true,
       "step_3_4_applied_from_start": true,
       "consistency_check_passed": true,
       "all_links_functional": true,
       "all_figures_converted": true,
       "metadata_complete": true
     },
     
     "next_steps": {
       "immediate": [
         "Compile with Sphinx",
         "Verify HTML output"
       ],
       "medium_term": [
         "Apply to next section"
       ]
     },
     
     "references": {
       "original_docs": "https://...",
       "standards": ["ISO XXX", "IEEE XXX"]
     },
     
     "license": {
       "original": "CC BY-SA 4.0",
       "translation": "CC BY-SA 4.0"
     },
     
     "metadata": {
       "created": "YYYY-MM-DD",
       "last_updated": "YYYY-MM-DD",
       "version": "1.0.0",
       "status": "complete"
     }
   }

**Ubicación:**

.. code-block:: bash

   # Mismo directorio que section-X.txt
   /sections/0X_section_name/section-X.json

**Validación del JSON:**

.. code-block:: bash

   # Verificar que es JSON válido
   python3 -m json.tool section-X.json > /dev/null && echo "✅ JSON válido" || echo "❌ JSON inválido"
   
   # Ver estructura formateada
   python3 -m json.tool section-X.json | less

Paso 5.5.4: Actualización de Archivo Principal ★★
--------------------------------------------------

.. important::
   **ACTUALIZAR TOCTREE**
   
   El archivo principal de la sección debe tener el toctree completo 
   con TODOS los archivos traducidos.

**Proceso:**

1. **Abrir archivo principal:**

   .. code-block:: bash
   
      # Para arc42
      vim seccion_XX_nombre.rst
      
      # Para libros
      vim capitulo_XX.rst

2. **Actualizar toctree con TODO el contenido:**

   .. code-block:: rst
   
      Subsecciones de la Plantilla
      =============================
      
      .. toctree::
         :maxdepth: 2
         
         seccion_X_1
         seccion_X_2
         seccion_X_3
      
      Ejemplos Prácticos
      ==================
      
      .. toctree::
         :maxdepth: 1
         
         ejemplo_1
         ejemplo_2
      
      Tips y Consejos
      ===============
      
      .. toctree::
         :maxdepth: 1
         
         tip_1
         tip_2
         ...
         tip_N

3. **Agregar nota de estado:**

   .. code-block:: rst
   
      .. note::
         **Estado de traducción:**
         
         - ✅ Subsecciones: X/X
         - ✅ Ejemplos: X/X
         - ✅ Tips: X/X
         
         **🎉 SECCIÓN XX COMPLETADA: XX/XX archivos (100%) 🎉**

4. **Actualizar metadata del archivo:**

   .. code-block:: rst
   
      :Sección: XX - [Nombre]
      :Estado: ✅ 100% COMPLETADO (XX archivos)
      :Workflow: v1.X.X

Paso 5.5.5: Checklist Final de FASE 5.5 ★
------------------------------------------

.. code-block:: text

   VERIFICACIÓN DE COMPLETITUD:
   [ ] Documento original revisado completamente
   [ ] Estructura comparada (original vs traducción)
   [ ] TODO el contenido identificado está traducido
   [ ] Subsecciones de plantilla incluidas (si aplican)
   [ ] Ejemplos incluidos
   [ ] Tips/consejos incluidos
   [ ] Apéndices incluidos
   
   ARCHIVOS OBLIGATORIOS:
   [ ] section-X.txt creado y verificado
   [ ] section-X.json creado y validado
   [ ] Ambos archivos con contenido completo
   
   ARCHIVO PRINCIPAL:
   [ ] Toctree actualizado con TODO el contenido
   [ ] Metadata actualizada (versión, estado)
   [ ] Nota de estado agregada (100% completado)
   
   CALIDAD:
   [ ] Terminología arquitectónica aplicada (si aplica Paso 3.4)
   [ ] Coherencia con secciones previas
   [ ] Enlaces internos funcionan
   [ ] Figuras referenciadas correctamente
   
   DOCUMENTACIÓN:
   [ ] Glosario actualizado
   [ ] Notas de traducción completas
   [ ] Reportes generados (si aplican)

**Si TODO está ✅ → Sección COMPLETA, continuar a FASE 6**

**Si algo está ❌ → Regresar al paso correspondiente**

----

FASE 5.6: Validación de Completitud y Fidelidad ★ (NUEVA - OBLIGATORIA)
========================================================================

.. critical::
   **EJECUTAR DESPUÉS DE CADA ARCHIVO TRADUCIDO**
   
   Esta fase previene dos tipos de errores sistemáticos:
   
   - **ERROR TIPO A:** Esqueletos sin contenido completo
   - **ERROR TIPO B:** Contenido agregado no presente en el original
   
   Basado en análisis de errores en Secciones 3 y 5 (ver ``ANALISIS_ERRORES_TRADUCCIONES_SEC3_SEC5.md``)

.. important::
   **CUÁNDO EJECUTAR:**
   
   - ✅ Después de traducir CADA archivo individual
   - ✅ ANTES de considerar el archivo "completado"
   - ✅ ANTES de continuar con el siguiente archivo
   - ✅ OBLIGATORIO para todos los archivos (tips, subsecciones, ejemplos)

.. warning::
   **NUNCA OMITIR ESTA FASE**
   
   Sin esta validación:
   
   - ❌ Archivos con solo estructura/encabezados (ERROR TIPO A)
   - ❌ Contenido inventado mezclado con oficial (ERROR TIPO B)
   - ❌ Divergencia del documento original
   - ❌ Trabajo de corrección posterior (~3 horas en Secciones 3 y 5)

Paso 5.6.1: Verificación de Longitud ★★★
-----------------------------------------

.. important::
   **Indicador principal de calidad de traducción**
   
   La longitud del archivo traducido debe estar en un rango esperado
   respecto al original debido al formato RST.

**Proceso:**

1. **Obtener longitudes:**

   .. code-block:: bash
   
      # Líneas del archivo original
      wc -l original/tip-5-12.md
      # Ejemplo: 15 líneas
      
      # Líneas del archivo traducido
      wc -l traduccion/bloques_tip_12.rst
      # Ejemplo: 31 líneas

2. **Calcular ratio:**

   .. code-block:: text
   
      Ratio = líneas_traducido / líneas_original
      Ratio = 31 / 15 = 2.07x

3. **Verificar contra rangos esperados:**

   .. code-block:: text
   
      RANGO ESPERADO: 1.5x ≤ Ratio ≤ 3.5x
      
      ✅ CORRECTO (1.5-3.5x):
         Ratio = 2.07x → DENTRO DEL RANGO
      
      ⚠️ ERROR TIPO A - Contenido Faltante (<1.5x):
         Ratio = 0.8x → MUY CORTO
         Ratio = 1.2x → PROBABLEMENTE INCOMPLETO
         → ACCIÓN: Revisar y completar traducción
      
      ⚠️ ERROR TIPO B - Contenido Agregado (>3.5x):
         Ratio = 4.1x → MUY LARGO
         Ratio = 5.0x → PROBABLE CONTENIDO AGREGADO
         → ACCIÓN: Verificar contra original, eliminar agregados

**Excepciones al rango:**

- **Archivos muy cortos (<10 líneas original):**
  
  - Pueden tener ratio >3.5x naturalmente
  - Verificar contenido manualmente

- **Archivos con muchas listas:**
  
  - Formato RST agrega líneas (.. list-table::)
  - Verificar que las listas existan en el original

**Señales de advertencia:**

.. code-block:: text

   🚨 DETENER SI:
   
   1. Ratio < 1.5x
      → Probable ERROR TIPO A (esqueleto sin contenido)
      → REVISAR Y COMPLETAR
   
   2. Ratio > 3.5x
      → Probable ERROR TIPO B (contenido agregado)
      → VERIFICAR CONTRA ORIGINAL
   
   3. Archivo <30 líneas con original >40 líneas
      → Casi seguro ERROR TIPO A
      → COMPLETAR URGENTE

Paso 5.6.2: Verificación de Secciones ★★★
------------------------------------------

.. important::
   **Previene agregar contenido no oficial**
   
   SOLO deben existir secciones que estén en el documento original.

**Proceso:**

1. **Listar títulos del original:**

   .. code-block:: bash
   
      # Para Markdown
      grep "^##" original/tip-5-15.md
      
      # Ejemplo de salida:
      ## When to deviate from this rule

2. **Listar títulos de la traducción:**

   .. code-block:: bash
   
      # Para RST
      grep -E "^={3,}|^-{3,}" traduccion/bloques_tip_15.rst
      
      # O manualmente abrir el archivo y listar secciones

3. **Comparar secciones:**

   .. code-block:: text
   
      ORIGINAL:
      ├─ When to deviate from this rule
      
      TRADUCCIÓN:
      ├─ Cuándo Desviarse de Esta Regla  ✅
      └─ Ventajas del Mapeo Directo      ❌ ← NO EXISTE EN ORIGINAL

4. **Identificar agregados:**

   .. warning::
      **Secciones típicas que indican ERROR TIPO B:**
      
      - "Ventajas de..."
      - "Tipos de..."
      - "Ejemplos de..."
      - "Casos de uso..."
      - "Cuándo usar/no usar..."
      - "Mejores prácticas..."
      
      **Si estas secciones NO están en el original → ELIMINAR**

**Acción si hay secciones agregadas:**

.. code-block:: text

   SI encuentras secciones NO en el original:
   
   1. DETENER traducción
   2. COMPARAR con original línea por línea
   3. ELIMINAR todo contenido agregado
   4. REESCRIBIR con solo contenido original
   5. VOLVER a ejecutar FASE 5.6

Paso 5.6.3: Verificación de Ejemplos ★★
----------------------------------------

.. important::
   **Ejemplos inventados violan fidelidad**
   
   El número y tipo de ejemplos debe coincidir con el original.

**Proceso:**

1. **Contar code-blocks en original:**

   .. code-block:: bash
   
      # Markdown
      grep -c "^\`\`\`" original/tip-5-14.md
      # Ejemplo: 0 code-blocks

2. **Contar code-blocks en traducción:**

   .. code-block:: bash
   
      # RST
      grep -c ".. code-block::" traduccion/bloques_tip_14.rst
      # Ejemplo: 3 code-blocks  ← ERROR!

3. **Verificar discrepancias:**

   .. code-block:: text
   
      Original: 0 code-blocks
      Traducción: 3 code-blocks
      
      DIFERENCIA: +3 code-blocks agregados
      
      → ERROR TIPO B - Ejemplos inventados
      → ELIMINAR los 3 code-blocks

**Tipos de ejemplos a verificar:**

- Code-blocks (``.. code-block::``)
- Diagramas ASCII (pueden ser agregados)
- Listas con bullets extensas
- Tablas comparativas
- Figuras adicionales

**Tolerancia:**

- ±1 ejemplo por diferencias de formato: ACEPTABLE
- ≥2 ejemplos de diferencia: PROBABLE ERROR
- Ejemplos con contenido elaborado: VERIFICAR ORIGEN

Paso 5.6.4: Check Visual Rápido ★
----------------------------------

.. important::
   **Inspección visual en 30 segundos**
   
   Detecta patrones comunes de ERROR TIPO B.

**Lista de verificación visual:**

.. code-block:: text

   ABRIR archivo traducido y buscar visualmente:
   
   ❓ ¿Veo secciones con estos títulos?
      □ "Ventajas de..."
      □ "Tipos de..."
      □ "Ejemplos de..."
      □ "Casos de uso..."
      □ "Cuándo incluir/no incluir..."
      □ "Mejores prácticas..."
      
      SI → Probable ERROR TIPO B
   
   ❓ ¿Veo listas extensas con 4+ bullets?
      □ Listas de ventajas
      □ Listas de tipos/categorías
      □ Listas de recomendaciones
      
      SI → Verificar si existe en original
   
   ❓ ¿Veo diagramas ASCII elaborados?
      □ Diagramas de jerarquía
      □ Diagramas de flujo
      □ Ejemplos visuales
      
      SI → Verificar si existe en original
   
   ❓ ¿Veo tablas comparativas (✅/❌)?
      □ "Correcto vs Incorrecto"
      □ "Hacer vs No hacer"
      □ "Buenas vs Malas prácticas"
      
      SI → Verificar si existe en original

**Acción si respuesta es SÍ a cualquier pregunta:**

.. code-block:: text

   1. ABRIR archivo original
   2. BUSCAR la sección/elemento en cuestión
   3. SI NO existe en original → ELIMINAR de traducción
   4. SI existe en original → VERIFICAR que sea traducción fiel

Paso 5.6.5: Verificación de Fidelidad al Contenido ★★★
-------------------------------------------------------

.. important::
   **Regla de Oro de Traducción**
   
   Traducción = COMPLETA (100% contenido) + FIEL (0% agregados)

**Definiciones precisas:**

.. code-block:: text

   "Traducción COMPLETA" significa:
   ✅ TODO el texto original traducido palabra por palabra
   ✅ TODOS los ejemplos incluidos
   ✅ TODAS las explicaciones preservadas
   ✅ TODOS los detalles técnicos mantenidos
   ✅ Longitud esperada: 1.5-3.0x el original
   
   NO significa:
   ❌ Solo estructura y encabezados
   ❌ Resumen del contenido
   ❌ Parafraseo breve
   ❌ Versión abreviada

.. code-block:: text

   "Traducción FIEL" significa:
   ✅ SOLO el contenido que existe en el original
   ✅ Sin agregar secciones nuevas
   ✅ Sin agregar ejemplos propios
   ✅ Sin agregar listas de ventajas/tipos
   ✅ Sin expandir explicaciones
   
   NO significa:
   ❌ "Mejorar" el contenido original
   ❌ Agregar información "útil"
   ❌ Crear ejemplos "educativos"
   ❌ Completar información "faltante"

**Rol del traductor vs documentador:**

.. code-block:: text

   TU ROL COMO TRADUCTOR:
   ✅ Traducir fielmente el contenido existente
   ✅ Aplicar Paso 3.4 (terminología técnica)
   ✅ Mantener formato RST
   ✅ Preservar intención del autor
   
   NO ES TU ROL:
   ❌ "Mejorar" el contenido original
   ❌ Agregar valor educativo extra
   ❌ Expandir explicaciones incompletas
   ❌ Decidir qué debería incluir el documento

Paso 5.6.6: Checklist Pre-Commit ★★★
-------------------------------------

.. important::
   **COMPLETAR ANTES DE CONSIDERAR ARCHIVO "TERMINADO"**
   
   No continuar al siguiente archivo hasta que TODAS las casillas estén marcadas.

**Checklist obligatorio:**

.. code-block:: text

   COMPLETITUD (Evitar ERROR TIPO A):
   [ ] Leí el archivo original COMPLETO de inicio a fin
   [ ] Traduje TODO el texto (no hice resumen)
   [ ] Incluí TODOS los ejemplos mencionados en el original
   [ ] Incluí TODAS las explicaciones y detalles
   [ ] Longitud está en rango 1.5-3.5x del original
   [ ] Archivo >30 líneas si original >40 líneas
   
   FIDELIDAD (Evitar ERROR TIPO B):
   [ ] NO agregué secciones que no existen en el original
   [ ] NO agregué ejemplos propios o inventados
   [ ] NO agregué listas de ventajas/tipos no presentes
   [ ] NO expandí explicaciones del original
   [ ] Cada título de sección existe en el original
   [ ] Cada code-block tiene equivalente en original
   
   CALIDAD:
   [ ] Paso 3.4 aplicado (terminología coherente)
   [ ] Formato RST correcto
   [ ] Referencias cruzadas completas
   [ ] Metadata al final del archivo
   [ ] Figuras referenciadas correctamente
   
   VALIDACIÓN:
   [ ] Ejecuté Paso 5.6.1 (longitud) → PASÓ
   [ ] Ejecuté Paso 5.6.2 (secciones) → PASÓ
   [ ] Ejecuté Paso 5.6.3 (ejemplos) → PASÓ
   [ ] Ejecuté Paso 5.6.4 (check visual) → PASÓ
   [ ] Ejecuté Paso 5.6.5 (fidelidad) → PASÓ
   [ ] Sin señales de advertencia detectadas

**Si TODAS las casillas están ✅:**

.. code-block:: text

   ✅ Archivo COMPLETADO correctamente
   → Continuar con siguiente archivo
   → Aplicar FASE 5.6 al siguiente

**Si ALGUNA casilla está ❌:**

.. code-block:: text

   ❌ Archivo NO completado
   → NO continuar con siguiente
   → Corregir el problema identificado
   → VOLVER a ejecutar FASE 5.6 completa

Paso 5.6.7: Señales de Advertencia ★★
--------------------------------------

.. danger::
   **DETENER Y REVISAR INMEDIATAMENTE SI:**

**Señal 1: Longitud sospechosa**

.. code-block:: text

   🚨 Ratio < 1.5x
      INDICA: Probable contenido faltante (ERROR TIPO A)
      CAUSA COMÚN: Solo creé estructura, no traduje contenido
      EJEMPLO: Original 47 líneas → Traducido 15 líneas
      ACCIÓN: 
        1. Leer original completo
        2. Identificar qué falta
        3. Completar traducción
        4. Volver a validar

.. code-block:: text

   🚨 Ratio > 3.5x
      INDICA: Probable contenido agregado (ERROR TIPO B)
      CAUSA COMÚN: "Mejoré" el original con información extra
      EJEMPLO: Original 15 líneas → Traducido 62 líneas
      ACCIÓN:
        1. Comparar secciones con original
        2. Identificar qué agregué
        3. Eliminar contenido no original
        4. Volver a validar

**Señal 2: Archivo muy corto**

.. code-block:: text

   🚨 Archivo <30 líneas con original >40 líneas
      INDICA: Casi seguro ERROR TIPO A
      CAUSA COMÚN: Solo traduje encabezados
      ACCIÓN:
        1. STOP - No continuar
        2. Reescribir archivo completo
        3. Incluir TODO el contenido

**Señal 3: Escribiendo títulos nuevos**

.. code-block:: text

   🚨 Estoy escribiendo sección que no veo en original
      INDICA: Agregando contenido no autorizado
      CAUSA COMÚN: Pensé que sería "útil" agregarlo
      EJEMPLOS:
        - "Ventajas de..."
        - "Tipos de..."
        - "Mejores prácticas..."
      ACCIÓN:
        1. STOP inmediatamente
        2. NO escribir esa sección
        3. Continuar con contenido original únicamente

**Señal 4: Creando ejemplos elaborados**

.. code-block:: text

   🚨 Estoy creando code-block que no está en original
      INDICA: Inventando ejemplos
      CAUSA COMÚN: "El original necesita más ejemplos"
      ACCIÓN:
        1. STOP
        2. Verificar si ejemplo existe en original
        3. Si NO existe → NO agregarlo
        4. Si existe → Traducir el que está

**Señal 5: "Mejorando" explicaciones**

.. code-block:: text

   🚨 Estoy expandiendo una explicación que parece breve
      INDICA: Excediendo rol de traductor
      CAUSA COMÚN: "El original no explica suficiente"
      RECORDATORIO:
        - Tu rol es TRADUCIR, no MEJORAR
        - Si el original es breve, la traducción es breve
        - No decides qué debería incluir el documento
      ACCIÓN:
        1. STOP
        2. Traducir TAL CUAL está en original
        3. NO agregar explicaciones extra

Paso 5.6.8: Reporte de Validación (Opcional)
---------------------------------------------

Para auditoría y trazabilidad, opcionalmente documentar:

.. code-block:: text

   Archivo: bloques_tip_15.rst
   Original: tip-5-15.md
   
   VALIDACIÓN FASE 5.6:
   ✅ Longitud: 36 líneas / 20 líneas = 1.8x (RANGO OK)
   ✅ Secciones: Solo las del original
   ✅ Ejemplos: 1 figura (igual que original)
   ✅ Check visual: Sin secciones sospechosas
   ✅ Fidelidad: 100% contenido original, 0% agregados
   ✅ Checklist: Todas las casillas marcadas
   
   RESULTADO: ARCHIVO VÁLIDO ✅
   Fecha validación: 2026-01-27
   Validador: [nombre]

----

FASE 6: Revisión y Mejora
==========================

Paso 6.1: Revisión de Enlaces
------------------------------

**Verificar todos los enlaces:**

.. code-block:: bash

   # Buscar todos los :ref: en el documento
   grep -r ':ref:' source/capitulo_X/
   
   # Probar manualmente en HTML que funcionan

**Arreglar rotos:**

.. code-block:: rst

   # Si referencia no funciona:
   # 1. Verificar que etiqueta existe
   # 2. Verificar ortografía
   # 3. Verificar que está en un archivo incluido en toctree

Paso 6.2: Optimización de Redacción
------------------------------------

**Mejorar sin cambiar contenido:**

1. **Claridad:**
   - ¿Hay frases confusas que podemos aclarar?
   - ¿Conviene agregar ``.. note::`` en algún lugar?

2. **Concisión:**
   - ¿Hay redundancia que podemos condensar?
   - ¿Verbosidad que podemos simplificar?

3. **Consistencia:**
   - ¿Terminología consistente en todo el capítulo?
   - ¿Estilo consistente?

Paso 6.3: Aplicar Feedback
---------------------------

**Si hay revisión por pares:**

.. code-block:: text

   Para cada comentario de revisor:
   1. ¿Es válido? → Implementar cambio
   2. ¿Es debatible? → Discutir
   3. ¿Es erróneo? → Explicar por qué no se implementa

**Documentar cambios:**

.. code-block:: rst

   .. note::
      **Feedback implementado:**
      
      Revisor sugirió aclarar término "API"
      → Agregado: API (Application Programming Interface)

----

FASE 7: Publicación
===================

Paso 7.1: Compilación Final
----------------------------

**Compilación completa y limpia:**

.. code-block:: bash

   # Limpieza total
   make clean
   
   # Compilación final
   make html
   
   # Verificar warnings
   # Objetivo: 0 errors, mínimos warnings

Paso 7.2: Control de Calidad Final
-----------------------------------

**Checklist pre-publicación:**

.. code-block:: text

   COMPILACIÓN:
   [ ] 0 errores
   [ ] Warnings revisados y justificados
   [ ] HTML generado completo
   
   CONTENIDO:
   [ ] Todo el capítulo/documento traducido
   [ ] Sin secciones "TODO" pendientes
   [ ] Figuras/tablas completas
   
   CALIDAD:
   [ ] Enlaces funcionan
   [ ] Navegación correcta
   [ ] Formato visual apropiado
   [ ] Sin errores tipográficos obvios
   
   DOCUMENTACIÓN:
   [ ] Decisiones importantes documentadas
   [ ] Cambios significativos registrados

Paso 7.3: Despliegue
--------------------

**Publicar libro en biblioteca:**

.. code-block:: bash

   # Si es documentación web:
   rsync -avz build/html/biblioteca/ servidor:/docs/biblioteca/
   
   # O si es repositorio Git:
   cd /tmp/ADT
   git add source/biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed/
   git commit -m "Traducción completa: Modern Full-Stack Development - Capítulo 5"
   git push

**Actualizar catálogos:**

.. code-block:: bash

   # Actualizar índices de biblioteca
   # Ver: biblioteca/catalogo/
   
   # Actualizar metadata del libro
   vim biblioteca/.../Modern_Full_Stack_Development_Zammetti_2ed/metadata_libro.rst
   # Cambiar :progreso: y :estado:

**Notificar:**

- Actualizar changelog del proyecto
- Notificar a equipo de revisión
- Agregar a catálogo de libros completados

----

Lecciones Aprendidas
====================

Esta sección documenta experiencias y aprendizajes clave obtenidos durante 
la aplicación del workflow en proyectos reales.

Sección 01 - arc42 (Introducción y Objetivos)
----------------------------------------------

**Proyecto:** Traducción de arc42 Documentation - Section 1  
**Fecha:** 2026-01-27  
**Workflow aplicado:** v1.5.0 (Lotes 2-4), v1.4.0 + correcciones (Lote 1)  
**Resultado:** 31 archivos traducidos (100% completitud)

.. note::
   **CONTEXTO DEL PROYECTO:**
   
   Primera sección completa de arc42 traducida al español aplicando 
   el Workflow ADT con Paso 3.4 (Traducción Arquitectónica).

✅ **Lo que FUNCIONÓ:**
~~~~~~~~~~~~~~~~~~~~~~~

1. **Workflow v1.5.0 con Paso 3.4 desde el inicio**
   
   **Resultado:**
   
   - 70% más eficiente que v1.4.0
   - 0 correcciones necesarias en Lotes 2-4
   - Calidad perfecta desde FASE 3
   - Terminología arquitectónica correcta al 100%
   
   **Métrica:**
   
   - v1.4.0: ~60 min/archivo + 12 correcciones (2 horas extra)
   - v1.5.0: ~18 min/archivo + 0 correcciones
   - Ahorro: 70% de tiempo total

2. **Enfoque por lotes (4-9 archivos)**
   
   **Ventajas observadas:**
   
   - Control de calidad incremental
   - Validación manageable
   - Reduce carga cognitiva
   - Facilita detección temprana de problemas
   
   **Recomendación:** Usar lotes de 5-9 archivos para proyectos grandes

3. **Estructura 1:1 (original → traducido)**
   
   **Beneficios:**
   
   - Trazabilidad clara y directa
   - Fácil mantenimiento futuro
   - Comparación original vs traducción simple
   - Auditorías facilitadas

4. **Glosario incremental por lote**
   
   **Resultado:**
   
   - Previene inconsistencias terminológicas
   - Referencia fácil durante traducción
   - Construcción progresiva de vocabulario técnico

❌ **Lo que NO FUNCIONÓ (y cómo se corrigió):**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Asumir que todo estaba traducido sin verificar**
   
   **Problema:**
   
   - Inicialmente solo tradujimos 28 archivos (ejemplos y tips)
   - NO verificamos contra el documento original completo
   - FALTABAN 3 subsecciones de plantilla arc42 (1.1, 1.2, 1.3)
   
   **Impacto:**
   
   - Sección reportada como "completa" estaba incompleta (90%)
   - Falta de plantillas listas para usar
   - Inconsistencia con estructura oficial arc42
   
   **Corrección:**
   
   - Revisar documento original COMPLETO (no solo archivos visibles)
   - Comparar estructura: original vs traducción
   - Ejecutar checklist exhaustivo de completitud
   - Traducir contenido faltante (3 subsecciones)
   
   **Resultado:**
   
   - Sección completada al 100% (31 archivos)
   - Subsecciones 1.1, 1.2, 1.3 agregadas
   - Plantillas listas para copiar
   
   **LECCIÓN CRÍTICA:** NUNCA asumir completitud - SIEMPRE verificar 
   contra documento original completo (esto motivó la creación de FASE 5.5)

2. **No crear archivos de referencia al inicio**
   
   **Problema:**
   
   - Solo teníamos archivos RST individuales
   - No había forma fácil de consultar contenido completo sin Sphinx
   - Faltaba metadata estructurada para análisis
   
   **Corrección:**
   
   - Crear section-1.txt (referencia completa en texto plano)
   - Crear section-1.json (metadata estructurada)
   - Hacerlo AL FINAL, después de verificar completitud
   
   **Resultado:**
   
   - Consulta rápida sin compilar
   - Plantillas copiables directamente
   - Metadata para automatización
   
   **LECCIÓN:** Crear archivos de referencia AL FINAL del proceso, 
   no al principio (cuando aún no sabemos si está completo)

3. **No documentar subsecciones de plantilla**
   
   **Problema:**
   
   - Asumimos que "plantillas" no eran parte del contenido a traducir
   - Las consideramos "opcionales" o "de referencia"
   - No están en archivos MD separados (están en el spec oficial)
   
   **Corrección:**
   
   - Las plantillas/subsecciones SON parte del contenido oficial
   - arc42 sección 1 tiene 3 subsecciones: 1.1, 1.2, 1.3
   - Son obligatorias para completitud
   - Traducirlas como archivos RST independientes
   
   **Resultado:**
   
   - 3 archivos adicionales traducidos
   - Plantillas con formato RST correcto
   - Templates listos para proyectos reales
   
   **LECCIÓN:** Subsecciones de plantilla en especificaciones técnicas 
   (arc42, ISO, IEEE) son OBLIGATORIAS, no opcionales

🎯 **Recomendaciones para Futuras Secciones:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Al INICIAR una sección nueva:**

1. Leer documento original COMPLETO (no solo archivos repo)
2. Identificar TODA la estructura (subsecciones, plantillas, anexos)
3. Crear plan de lotes realista
4. No asumir nada sobre completitud

**Durante la TRADUCCIÓN:**

1. Aplicar Paso 3.4 desde el inicio si es contenido arquitectónico
2. Mantener estructura 1:1 estricta
3. Actualizar glosario incrementalmente por lote
4. Verificar calidad por lote antes de continuar

**Al FINALIZAR la sección:**

1. **FASE 5.5.1:** Verificar completitud contra original COMPLETO
2. **FASE 5.5.2:** Crear section-X.txt con contenido completo
3. **FASE 5.5.3:** Crear section-X.json con metadata
4. **FASE 5.5.4:** Actualizar archivo principal (toctree completo)
5. **FASE 5.5.5:** Ejecutar checklist final

📊 **Métricas de Éxito - Sección 01:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Eficiencia:**

.. code-block:: text

   Workflow v1.4.0: ~60 min/archivo + correcciones
   Workflow v1.5.0: ~18 min/archivo + 0 correcciones
   ───────────────────────────────────────────────
   Mejora:          70% más rápido

**Calidad:**

.. code-block:: text

   Lote 1 (v1.4.0):  12 correcciones necesarias
   Lotes 2-4 (v1.5.0): 0 correcciones
   ───────────────────────────────────────────────
   Mejora:          100% reducción de correcciones

**Terminología:**

.. code-block:: text

   Coherencia:      100% (31 archivos)
   Paso 3.4:        Aplicado desde inicio
   Traducciones literales incorrectas: 0

**Completitud:**

.. code-block:: text

   Inicial:         28/31 archivos (90%)
   Final:           31/31 archivos (100%)
   ───────────────────────────────────────────────
   Incremento:      +3 archivos (subsecciones plantilla)

🔄 **Cambios al Workflow Resultantes:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basado en estas lecciones, se creó:

**Workflow v1.6.0** con:

1. **FASE 5.5:** Documentación de Sección (OBLIGATORIA)
   
   - Verificación de completitud contra original
   - Creación de section-X.txt
   - Creación de section-X.json
   - Actualización de archivo principal
   - Checklist final

2. **Esta sección de Lecciones Aprendidas**
   
   - Documentar experiencias reales
   - Prevenir repetición de errores
   - Compartir mejores prácticas

----

Plantillas y Herramientas
=========================

Template de Sección
-------------------

.. code-block:: rst

   ================
   Título de Sección
   ================
   
   .. Metadata
   :Autor: [Nombre]
   :Fecha: [YYYY-MM-DD]
   :Original: [archivo.tex]
   :Estado: [Borrador/Revisión/Aprobado]
   
   .. Notas de traducción
   .. note::
      **Decisiones de traducción:**
      
      - [Decisión 1]
      - [Decisión 2]
   
   ----
   
   [Contenido aquí]
   
   ----
   
   Referencias
   ===========
   
   .. [#] Referencia 1
   .. [#] Referencia 2

Scripts Útiles
--------------

**Verificar compilación:**

.. code-block:: bash

   #!/bin/bash
   # check_build.sh
   
   make clean
   make html 2>&1 | tee build.log
   
   if grep -q "ERROR" build.log; then
       echo "❌ ERRORES en compilación"
       exit 1
   else
       echo "✅ Compilación exitosa"
   fi

**Contar progreso de libro:**

.. code-block:: bash

   #!/bin/bash
   # progreso_libro.sh
   
   # Ruta al libro
   LIBRO="biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed"
   
   # Contar capítulos totales (carpetas con traduccion/)
   total_capitulos=$(find "$LIBRO" -maxdepth 1 -type d -name "*" | grep -v "^$LIBRO$" | grep -v "front_matter" | grep -v "back_matter" | wc -l)
   
   # Contar capítulos con traducción
   traducidos=$(find "$LIBRO" -name "traduccion" -type d | wc -l)
   
   echo "Progreso del libro:"
   echo "  Traducidos: $traducidos / $total_capitulos capítulos"
   echo "  Porcentaje: $(($traducidos * 100 / $total_capitulos))%"
   
   # Actualizar metadata_libro.rst
   sed -i "s/:progreso:.*/:progreso: $(($traducidos * 100 / $total_capitulos))%/" "$LIBRO/metadata_libro.rst"

----

Troubleshooting Común
=====================

Problema 1: No Compila
-----------------------

**Síntoma:**
   ``make html`` falla con error.

**Diagnóstico:**

.. code-block:: bash

   # Ver error específico
   make html 2>&1 | grep -A 5 "ERROR"

**Soluciones comunes:**

- Error de sintaxis RST → Revisar indentación, directivas
- Referencia rota → Verificar etiquetas con ``.. _``
- Archivo faltante → Verificar paths en ``.. figure::``

Problema 2: Referencias No Funcionan
-------------------------------------

**Síntoma:**
   Clic en referencia no va a destino.

**Diagnóstico:**

.. code-block:: bash

   # Buscar etiqueta
   grep -r ".. _mi-etiqueta:" source/

**Soluciones:**

- Etiqueta no existe → Crear con ``.. _mi-etiqueta:``
- Etiqueta en archivo no incluido → Agregar a ``toctree``
- Ortografía → Verificar mayúsculas/guiones

Problema 3: Figuras No Aparecen
--------------------------------

**Síntoma:**
   Espacio en blanco donde debería estar figura.

**Diagnóstico:**

.. code-block:: bash

   # Verificar path
   ls -la source/capitulo_X/figuras/mi_figura.png

**Soluciones:**

- Archivo no existe → Copiar desde original
- Path incorrecto → Ajustar en ``.. figure::``
- Formato no soportado → Convertir a PNG/JPG

----

Métricas de Calidad
===================

**Objetivo:** Medir calidad de la traducción

Métrica 1: Tasa de Compilación
-------------------------------

.. code-block:: text

   Tasa de Compilación = Secciones que compilan sin errores / Total secciones
   
   Objetivo: 100%

Métrica 2: Preservación de Contenido
-------------------------------------

.. code-block:: text

   Completitud = Elementos traducidos / Total elementos
   
   Elementos: secciones, figuras, tablas, ecuaciones, referencias
   
   Objetivo: 100%

Métrica 3: Calidad Visual
--------------------------

.. code-block:: text

   Checklist de 20 ítems visuales
   
   Puntuación = Ítems OK / 20
   
   Objetivo: ≥ 95% (19/20)

Métrica 4: Tiempo por Sección
------------------------------

.. code-block:: text

   Tiempo Promedio = Σ(tiempo por sección) / N secciones
   
   Benchmark: 1-2 horas por sección estándar
   
   Objetivo: Mejorar eficiencia con experiencia

----

Casos Especiales y Lecciones Aprendidas
========================================

**NUEVA SECCIÓN v1.2.0:** Casos especiales encontrados y lecciones aprendidas.

Repositorios GitHub Pre-Organizados
------------------------------------

**Caso: arc42 documentation**

El repositorio arc42 (``docs.arc42.org-site``) está pre-organizado:

.. code-block:: text

   docs.arc42.org-site/
   ├── _posts/
   │   ├── 01-requirements/      ← 24 archivos
   │   ├── 02-constraints/       ← 5 archivos
   │   └── ... (12 secciones)
   └── _examples/
       ├── 01-*.md
       └── 02-*.md

**Lección aprendida:**

❌ **NO** buscar archivos por palabras clave en nombres
✅ **SÍ** usar la estructura de carpetas del repositorio

**Antes (incorrecto):**

.. code-block:: bash

   # Buscar: archivos con "constraint" en el nombre
   find . -name "*constraint*"
   # Resultado: Solo 1 archivo (faltan 5 tips)

**Ahora (correcto):**

.. code-block:: bash

   # Copiar desde carpetas organizadas
   cp _posts/02-constraints/* → sections/02_constraints/original/

Validación de Distribución de Archivos
---------------------------------------

**Proceso recomendado:**

1. Distribuir archivos (puede tener errores)
2. Analizar con herramienta:
   
   .. code-block:: bash
   
      python scripts/analizar_seccion.py sections/02_constraints

3. Comparar con fuente oficial
4. Si hay discrepancia, investigar y corregir
5. Re-analizar para confirmar

Archivos con Front Matter YAML
-------------------------------

**Uso del front matter:**

- **Validación:** Verificar ``category`` coincide con sección
- **Título:** Extraer título descriptivo
- **Tags:** Identificar términos para glosario

**Procesamiento:**

.. code-block:: rst

   <!-- NO incluir front matter en RST traducido -->
   <!-- Usar información así: -->
   
   .. _tip-2-1:
   
   Tip 2-1: [Título del front matter traducido]
   ---------------------------------------------
   
   [Contenido]

Numeración en Secciones
------------------------

**¿Violan NOM_001 las carpetas con números?**

✅ **NO, es correcto**

.. code-block:: text

   ❌ INCORRECTO:
   biblioteca/categoria/01_Mi_Libro/
   
   ✅ CORRECTO:
   biblioteca/categoria/Mi_Libro/
      sections/01_introduction/  ← Números OK aquí
      sections/02_constraints/   ← Números OK aquí

**Razón:** NOM_001 prohíbe números al inicio del **nombre del LIBRO**.
Los números en secciones son útiles para orden y navegación.

Referencias Cruzadas Bidireccionales
-------------------------------------

**Situación:**
   Tips que se referencian mutuamente

**Solución:**

.. code-block:: rst

   .. _tip-2-3:
   
   [Contenido]
   Ver también :ref:`tip-2-4`
   
   .. _tip-2-4:
   
   [Contenido]
   Ver también :ref:`tip-2-3`

Typos en Material Original
---------------------------

**Decisión:**

- **Error menor:** Corregir silenciosamente en traducción
- **Error significativo:** Documentar y considerar reportar

----

Conclusión
==========

**Este workflow de 7 fases proporciona:**

✅ Proceso sistemático y repetible  
✅ Checkpoints de calidad en cada fase  
✅ Documentación de decisiones  
✅ Métricas de progreso  
✅ Troubleshooting integrado

**Resultado esperado:**

   Traducciones de alta calidad, consistentes, y verificables.

**Próximo paso:**

   Aplicar este workflow en un libro real usando la estructura de biblioteca/.
   
   Ver ejemplos en:
   - :doc:`/biblioteca/arc42/index` (ejemplo en progreso)
   - :doc:`/docs_maestros/ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta`

----

Referencias
===========

- :doc:`/01_fundamentos/principios_fundamentales`
- :doc:`/01_fundamentos/objetivos_tacticas`
- :doc:`/01_fundamentos/_metodologias/metodo_por_defecto`
- :doc:`modo_alta_fidelidad/index`
- :doc:`modo_marcado_visual/index`

----

**Versión:** 1.4.0  
**Fecha:** 2026-01-27  
**Estado:** Aprobado - Procedimiento operativo principal  
**Actualizaciones v1.4.0:**
   - **FASE 3.5 agregada (CRÍTICA):** Revisión de Literalidad obligatoria
   - Checklist de revisión sistemática archivo por archivo
   - Patrones comunes de literalidad a detectar
   - Proceso de ajustes prioritizados y documentados
   - Regla: "Si no revisaste literalidad, no terminaste FASE 3"
**Actualizaciones v1.3.0:**
   - Estructura 1:1 explícita en Paso 3.1 (un archivo original → un archivo traducido)
   - Checklist de revisión Signifié en Paso 3.3 (evitar traducciones literales)
   - Ejemplos de qué evitar (traducciones demasiado literales)
**Actualizaciones v1.2.0:**
   - Herramientas Python de análisis automatizado
   - FASE 2 actualizada con método automatizado
   - Casos especiales y lecciones aprendidas (arc42)
