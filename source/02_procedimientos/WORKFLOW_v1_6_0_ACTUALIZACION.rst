.. meta::
 :artefacto: PROC_002_Workflow_General
 :tipo: Procedimiento
 :dominio: procedimientos
 :estado: Aprobado
 :version: 1.6.0
 :fecha_creacion: 2026-01-27
 :ultimo_cambio: 2026-01-27
 :autor: Equipo ADT
 :clasificacion: Interno

.. _proc-002-workflow-general-v1-6-0:




Workflow General de Traducción
==============================

:Versión: 1.6.0
:Categoría: Procedimientos
:Ubicación: 02_procedimientos/
:Tipo: Procedimiento Operativo Principal
:Base: Método Peshitta + ADT

**Registro de Cambios:**

- **v1.6.0 (2026-01-27):** MINOR - Agregada FASE 5.5: Documentación de Sección (OBLIGATORIA). Incluye creación de section-X.txt y section-X.json, verificación de completitud, y actualización de archivo principal. Agregadas lecciones aprendidas de Sección 01 (arc42). Checklist de verificación de contenido completo.
- **v1.5.0 (2026-01-27):** MINOR - Agregado Paso 3.4: Traducción Arquitectónica (OBLIGATORIO para arc42). Integración completa de Guía de Traducción Arquitectónica.
- **v1.4.0 (2026-01-27):** MINOR - Agregada FASE 3.5 CRÍTICA: Revisión de Literalidad (obligatoria)
- **v1.3.0 (2026-01-27):** MINOR - Correcciones críticas: estructura 1:1 explícita
- **v1.2.0 (2026-01-27):** MINOR - Agregadas herramientas Python, FASE 2 actualizada
- **v1.1.0 (2026-01-27):** MINOR - Corrección de estructura biblioteca/
- **v1.0.0 (2026-01-27):** MAJOR - Versión inicial

.. contents:: Contenido
 :depth: 3
 :local:




[TARGET] CAMBIOS IMPORTANTES EN v1.6.0
======================================

.. important::
 
 **FASE 5.5: Documentación de Sección (NUEVA - OBLIGATORIA)**

 Después de completar una sección/capítulo, SIEMPRE crear:

 
 1. **section-X.txt** - Documento de referencia completo
 2. **section-X.json** - Metadata estructurada
 3. **Verificar completitud** contra documento original
 4. **Actualizar archivo principal** con toctree

 **Propósito:** Mantener consistencia entre secciones, permitir consulta
 rápida sin compilar, y facilitar auditorías de completitud.

.. note::
 
 **Lecciones Aprendidas - Sección 01 (arc42):**

 - [OK] Verificar SIEMPRE contra documento original completo
 - [OK] No asumir que todo está traducido - comparar estructuras
 - [OK] Crear archivos de referencia (txt/json) AL FINAL
 - [OK] Subsecciones de plantilla son PARTE del contenido
 - [OK] Mantener consistencia con secciones previas




Resumen General del Workflow
============================

**Diagrama de Fases:**

.. code-block:: text

 FASE 0: VERIFICACIÓN INICIAL
 +-> Verificar estructura y requisitos

 FASE 1: PREPARACIÓN
 +-> Crear estructura de directorios

 FASE 2: ANÁLISIS ESTRUCTURAL
 +-> Identificar elementos del documento

 FASE 3: TRADUCCIÓN INICIAL
 +-> Paso 3.1: Estructura 1:1
 +-> Paso 3.2: Método Peshitta
 +-> Paso 3.3: Signifié
 +-> Paso 3.4: Traducción Arquitectónica (NUEVO en v1.5.0)

 FASE 3.5: REVISIÓN DE LITERALIDAD (CRÍTICO)
 +-> Detectar y corregir traducciones literales incorrectas

 FASE 4: APLICACIÓN DE TÁCTICAS
 +-> Ajustes contextuales

 FASE 5: VALIDACIÓN
 +-> 5.1: Compilación
 +-> 5.2: Preservación Semántica
 +-> 5.3: Calidad Visual

 FASE 5.5: DOCUMENTACIÓN DE SECCIÓN (NUEVO en v1.6.0 - OBLIGATORIO)
 +-> 5.5.1: Verificación de Completitud
 +-> 5.5.2: Creación de section-X.txt
 +-> 5.5.3: Creación de section-X.json
 +-> 5.5.4: Actualización de Archivo Principal

 FASE 6: REVISIÓN Y MEJORA
 +-> Refinamiento

 FASE 7: PUBLICACIÓN
 +-> Despliegue final

**Tiempo estimado total:** 3-6 horas por capítulo (depende de complejidad)




FASE 5.5: Documentación de Sección (NUEVA - OBLIGATORIA)
========================================================

.. important::
 
 **CUÁNDO EJECUTAR:**

 - Después de traducir TODA una sección/capítulo completo
 - Después de FASE 5 (Validación)
 - ANTES de considerar la sección "completa"
 - ANTES de pasar a la siguiente sección

.. warning::
 
 **NUNCA OMITIR ESTA FASE**

 Sin esta fase:
 
 - [ERROR] No hay forma de verificar completitud
 - [ERROR] Inconsistencia entre secciones
 - [ERROR] Pérdida de contenido (subsecciones, plantillas)
 - [ERROR] Metadata incompleta
 - [ERROR] Dificulta auditorías futuras

Paso 5.5.1: Verificación de Completitud
=======================================

.. important::
 
 **ESTE ES EL PASO MÁS CRÍTICO DE LA FASE 5.5**

 Verificar que TODO el contenido del documento original esté traducido.

**Proceso de Verificación:**

1. **Obtener documento original completo:**

 .. code-block:: bash

 # Para documentación arc42
 cd /ruta/a/seccion_original
 cat section-X.md # o equivalente

 # Para libros LaTeX
 cat capitulo_original.tex

2. **Comparar estructuras:**

 .. code-block:: text

 DOCUMENTO ORIGINAL TRADUCCIÓN
 +- Sección Principal +- [OK] seccion_X_principal.rst
 +- Subsección 1.1 +- [OK] seccion_1_1.rst
 +- Subsección 1.2 +- [OK] seccion_1_2.rst
 +- Subsección 1.3 +- [WARNING] FALTA? <- VERIFICAR
 +- Ejemplo 1 +- [OK] ejemplo_1.rst
 +- Ejemplo 2 +- [OK] ejemplo_2.rst
 +- Tips (1-24) +- [OK] tip_1.rst ... tip_24.rst
 +- Plantilla / Template +- [WARNING] FALTA? <- VERIFICAR

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
 echo "[ERROR] CONTENIDO INCOMPLETO - Faltan subsecciones"
 echo "Regresando a FASE 3 para traducir contenido faltante"

 # Traducir contenido faltante con Workflow v1.5.0
 # (aplicando Paso 3.4 si es contenido arquitectónico)

 # Luego regresar a FASE 5.5.1

**Ejemplo - Lección de Sección 01 (arc42):**

.. note::
 
 **CASO REAL - Lo que descubrimos:**

 Inicialmente tradujimos:
 
 - [OK] 4 ejemplos
 - [OK] 24 tips
 - [ERROR] FALTABAN las 3 subsecciones de plantilla (1.1, 1.2, 1.3)

 **Al revisar el documento original completo:**
 - Encontramos que había subsecciones 1.1, 1.2, 1.3 con plantillas
 - Estas subsecciones SON PARTE del contenido oficial arc42
 - No se deben omitir

 **Lección:** SIEMPRE verificar contra documento original completo,
 no asumir que todo está traducido.

Paso 5.5.2: Creación de section-X.txt
=====================================

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

   SECTION X: [TÍTULO EN INGLÉS]
   ==============================
   arc42 / [Nombre del Libro]

   Translated to Spanish | Método Peshitta + Workflow v1.X.X
   ==========================================================

   SOURCE DOCUMENT: section-X ([Título])
   TRANSLATION DATE: YYYY-MM-DD
   WORKFLOW VERSION: v1.X.X
   STATUS: [OK] 100% COMPLETE (X files)


   CONTENT OVERVIEW
   =================

   [Descripción general del contenido de la sección]


   STRUCTURE
   ==========

   SECTION X: [TÍTULO]
   |
   +- X.1 [SUBSECCIÓN 1]
   |  +- [Descripción]
   |
   +- X.2 [SUBSECCIÓN 2]
   |  +- [Descripción]
   |
   +- X.3 [SUBSECCIÓN 3]
      +- [Descripción]


   TRANSLATED FILES (X TOTAL)
   ===========================

   SUBSECTIONS (X files):
   =======================
   1. seccion_X_1.rst
      - X.1 [Título]
      - [Descripción]
      - Terminology: "term" -> "traducción"

   EXAMPLES (X files):


   TIPS (X files):







 ARCHITECTURAL TERMINOLOGY (Step 3.4 Applied)
=============================================

 CRITICAL TRANSLATIONS:
 +---------------------+----------------------------------------------+
 | English Term | Spanish Translation |
 +---------------------+----------------------------------------------+
 | [term 1] | [OK] [traducción correcta] |
 | | [ERROR] NOT "[traducción literal incorrecta]" |
 +---------------------+----------------------------------------------+




 SUBSECTION X.1: [TÍTULO]
=========================

 CONTENT:
 [Qué contiene]

 MOTIVATION:
 [Por qué es importante]

 FORM:
 [Cómo documentarlo]

 EXAMPLES:
 [Ejemplos disponibles]

 TEMPLATE:
==========

 [Plantilla lista para copiar]
==============================

 [Repetir para cada subsección]




 TRANSLATION STATISTICS
=======================

 [Métricas de traducción]




 REFERENCES
===========

 [Referencias oficiales]




 LICENSE
========

 Original content: [Licencia]
 Translation: [Licencia]




 TRANSLATION INFORMATION
========================

 Method: Peshitta Method + ADT Workflow v1.X.X
 Date: YYYY-MM-DD
 Status: [OK] 100% COMPLETE




 END OF SECTION X CONTENT
=========================

**Ubicación:**

.. code-block:: bash

 # Para arc42
 /sections/0X_section_name/section-X.txt

 # Para libros
 /biblioteca/.../Nombre_Libro/capitulo_XX/section-X.txt

**Ejemplo de Creación:**

.. code-block:: bash

 # Crear archivo section-1.txt para Sección 01 de arc42
 cd /sections/01_introduction_goals/

 # Crear con el contenido completo
 vim section-1.txt

 # Verificar
 wc -l section-1.txt
 # Debe tener ~500-1000 líneas dependiendo del contenido

Paso 5.5.3: Creación de section-X.json
======================================

.. important::
 
 **ARCHIVO OBLIGATORIO**

 Cada sección DEBE tener un archivo section-X.json con metadata
 estructurada en formato JSON.

**Propósito:**

- Metadata estructurada para procesamiento automatizado
- Fácil parsing con scripts
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

 "workflow_validation": {
 "hypothesis": "[Hipótesis si aplica]",
 "results": {
 "corrections_reduction": "X%",
 "time_reduction": "X%",
 "quality": "perfect/good/acceptable"
 },
 "conclusion": "[Conclusión]"
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
 python3 -m json.tool section-X.json > /dev/null && echo "[OK] JSON válido" || echo "[ERROR] JSON inválido"

Paso 5.5.4: Actualización de Archivo Principal
==============================================

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
===================

 .. toctree::
 :maxdepth: 1

 ejemplo_1
 ejemplo_2

 Tips y Consejos
================

 .. toctree::
 :maxdepth: 1

 tip_1

 tip_2
======
 tip_N

3. **Agregar nota de estado:**

 .. code-block:: rst

    .. note::
       **Estado de traducción:**

       - [OK] Subsecciones: X/X
       - [OK] Ejemplos: X/X
       - [OK] Tips: X/X

    ** SECCIÓN XX COMPLETADA: XX/XX archivos (100%) **

4. **Actualizar metadata del archivo:**

 .. code-block:: rst

    :Sección: XX - [Nombre]
    :Estado: [OK] 100% COMPLETADO (XX archivos)
    :Workflow: v1.X.X

Paso 5.5.5: Checklist Final de FASE 5.5
=======================================

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
 [ ] section-X.txt creado
 [ ] section-X.json creado
 [ ] Ambos archivos validados

 ARCHIVO PRINCIPAL:
 [ ] Toctree actualizado con TODO el contenido
 [ ] Metadata actualizada
 [ ] Nota de estado agregada

 CALIDAD:
 [ ] Terminología arquitectónica aplicada (si aplica)
 [ ] Coherencia con secciones previas
 [ ] Enlaces internos funcionan

 DOCUMENTACIÓN:
 [ ] Glosario actualizado
 [ ] Notas de traducción completas
 [ ] Reportes generados

**Si TODO está [OK] -> Sección COMPLETA, continuar a FASE 6**

**Si algo está [ERROR] -> Regresar al paso correspondiente**




Lecciones Aprendidas - Sección 01 (arc42)
=========================================

.. note::
 
 **PROCESO REAL - Qué funcionó y qué no:**

**[OK] Lo que FUNCIONÓ:**

1. **Workflow v1.5.0 con Paso 3.4 desde el inicio**

 - 70% más eficiente que v1.4.0
 - 0 correcciones necesarias en Lotes 2-4
 - Calidad perfecta desde FASE 3
 - Terminología arquitectónica correcta al 100%

2. **Enfoque por lotes**

 - 28 archivos divididos en 4 lotes manejables
 - Permite validación incremental
 - Facilita control de calidad
 - Reduce carga cognitiva

3. **Estructura 1:1 (original -> traducido)**

 - Trazabilidad clara
 - Fácil mantenimiento
 - Comparación directa posible

4. **Glosario incremental**

 - Términos agregados por lote
 - Previene inconsistencias
 - Referencia fácil

**[ERROR] Lo que NO FUNCIONÓ (y cómo se corrigió):**

1. **Asumir que todo estaba traducido**

 - [ERROR] Inicialmente solo tradujimos ejemplos y tips
 - [OK] Corregido: Revisar documento original COMPLETO
 - [OK] Encontramos 3 subsecciones faltantes (1.1, 1.2, 1.3)

 **Lección:** SIEMPRE verificar contra documento original completo

2. **No crear archivos de referencia al principio**

 - [ERROR] Solo teníamos archivos RST
 - [OK] Corregido: Crear section-X.txt y section-X.json

 **Lección:** Crear archivos de referencia AL FINAL, después de validar

3. **No documentar subsecciones de plantilla**

 - [ERROR] Asumimos que plantillas no eran contenido
 - [OK] Corregido: Las plantillas SON parte del contenido oficial

 **Lección:** Subsecciones de plantilla arc42 son OBLIGATORIAS

**[TARGET] Recomendaciones para Futuras Secciones:**

1. **Al iniciar una sección nueva:**

 - Leer documento original COMPLETO
 - Identificar TODA la estructura
 - Crear plan de lotes
 - No asumir nada

2. **Durante la traducción:**

 - Aplicar Paso 3.4 desde el inicio (si es contenido arquitectónico)
 - Mantener estructura 1:1
 - Actualizar glosario incrementalmente
 - Verificar calidad por lote

3. **Al finalizar la sección:**

 - FASE 5.5.1: Verificar completitud contra original
 - FASE 5.5.2: Crear section-X.txt
 - FASE 5.5.3: Crear section-X.json
 - FASE 5.5.4: Actualizar archivo principal
 - FASE 5.5.5: Checklist final

**Métricas de Éxito - Sección 01:**

.. code-block:: text

 EFICIENCIA:
 - Workflow v1.4.0: ~60 min/archivo
 - Workflow v1.5.0: ~18 min/archivo
 - Mejora: 70% más rápido

 CALIDAD:
 - Lote 1 (v1.4.0): 12 correcciones necesarias
 - Lotes 2-4 (v1.5.0): 0 correcciones
 - Mejora: 100% reducción de correcciones

 TERMINOLOGÍA:
 - Coherencia: 100% (31 archivos)
 - Paso 3.4 aplicado: Sí
 - Traducciones literales: 0




Checklist General Actualizado (v1.6.0)
======================================

.. code-block:: text

 ANTES DE EMPEZAR (FASE 0):
 [ ] Documento original completo disponible
 [ ] Estructura identificada
 [ ] Workflow v1.5.0 o superior

 PREPARACIÓN (FASE 1):
 [ ] Estructura de directorios creada
 [ ] Archivos originales en /original/

 ANÁLISIS (FASE 2):
 [ ] Elementos identificados
 [ ] Complejidad evaluada

 TRADUCCIÓN (FASE 3):
 [ ] Método Peshitta aplicado
 [ ] Paso 3.4 aplicado (si contenido arquitectónico)
 [ ] Estructura 1:1 mantenida

 REVISIÓN LITERALIDAD (FASE 3.5):
 [ ] Traducciones literales corregidas
 [ ] Terminología verificada

 VALIDACIÓN (FASE 5):
 [ ] Compila sin errores
 [ ] HTML correcto
 [ ] Enlaces funcionan

 DOCUMENTACIÓN SECCIÓN (FASE 5.5) NUEVO:
 [ ] Completitud verificada contra original
 [ ] section-X.txt creado
 [ ] section-X.json creado
 [ ] Archivo principal actualizado
 [ ] Toctree completo

 PUBLICACIÓN (FASE 7):
 [ ] Sección completa
 [ ] Calidad verificada
 [ ] Lista para despliegue

**Si TODO está [OK] -> Sección COMPLETA**




.. important::
 
 **RESUMEN DE CAMBIOS v1.6.0:**

 1. [OK] FASE 5.5 agregada (OBLIGATORIA)
 2. [OK] Verificación de completitud contra original
 3. [OK] Creación de section-X.txt (obligatorio)
 4. [OK] Creación de section-X.json (obligatorio)
 5. [OK] Actualización de archivo principal (obligatorio)
 6. [OK] Lecciones aprendidas de Sección 01
 7. [OK] Checklist general actualizado

 **Propósito:** Garantizar que NO se pierda contenido y mantener
 consistencia entre secciones.




.. note::
 
 **Para documentación completa del Workflow v1.5.0 (sin cambios):**

 Ver: :doc:`/02_procedimientos/workflow_general_v1_5_0_backup`

 **Diferencia principal v1.5.0 vs v1.6.0:**

 - v1.5.0: Hasta FASE 5 (Validación)
 - v1.6.0: Agrega FASE 5.5 (Documentación de Sección) - OBLIGATORIA




Historial de Versiones
======================

.. list-table::
 :header-rows: 1
 :widths: 10 15 15 60

 * - Versión
   - Fecha
   - Tipo
   - Cambios
 * - 1.6.0
   - 2026-01-27
   - MINOR
   - FASE 5.5 agregada, verificación completitud, archivos txt/json obligatorios
 * - 1.5.0
   - 2026-01-27
   - MINOR
   - Paso 3.4 Traducción Arquitectónica agregado
 * - 1.4.0
   - 2026-01-27
   - MINOR
   - FASE 3.5 Revisión Literalidad agregada
 * - 1.3.0
   - 2026-01-27
   - MINOR
   - Estructura 1:1 explícita
 * - 1.2.0
   - 2026-01-27
   - MINOR
   - Herramientas Python, FASE 2 mejorada
 * - 1.1.0
   - 2026-01-27
   - MINOR
   - Corrección biblioteca/
 * - 1.0.0
   - 2026-01-27
   - MAJOR
   - Versión inicial




.. note::
 
 **Información del documento:**

 :Versión: 1.6.0
 :Fecha: 2026-01-27
 :Autor: Equipo ADT
 :Estado: Aprobado
 :Próxima revisión: Después de completar Sección 02 (arc42)
