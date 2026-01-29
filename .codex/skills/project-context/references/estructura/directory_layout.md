# Layout de Directorios del Proyecto ADT

## Vista Completa

```
ADT/ (raiz proyecto)
|
+-- Makefile (build commands)
+-- make.bat (Windows batch)
+-- README.md (proyecto overview)
+-- .gitignore (git exclusions)
|
+-- build/ (OUTPUT - no versionado)
| +-- html/ (documentacion generada)
|
+-- source/ (CONTENIDO DOCUMENTAL)
| +-- conf.py (config Sphinx)
| +-- index.rst (indice principal)
| +-- _static/ (CSS, JS, imagenes)
| +-- _templates/ (templates Sphinx)
| |
| +-- 01_fundamentos/ (metodologia ADT)
| +-- 02_procedimientos/ (workflows)
| +-- 03_estandares/ (calidad, terminologia)
| +-- 04_reglas_operativas/ (matrices decision)
| +-- 05_herramientas_medios/ (Sphinx, LaTeX, MD)
| +-- 06_casos_practicos/ (ejemplos)
| +-- 07_guias_uso/ (tutoriales, FAQ)
| +-- 08_prompts/ (plantillas)
| +-- 09_referencias/ (cheatsheets)
| +-- 10_apendices/ (glosarios)
| |
| +-- biblioteca/ (traducciones)
| +-- diataxis/ (framework organizacion)
| +-- docs/ (docs tecnicas)
| +-- docs_maestros/ (docs fundamentales)
|
+-- scripts/ (AUTOMATIZACION)
| +-- traduccion/ (scripts traduccion)
| +-- analizar_seccion.py
| +-- validar_estructura.sh
| +-- progreso_libro.sh
| +-- init_libro.sh
| +-- init_capitulo.sh
|
+-- config/ (CONFIGURACIONES)
| +-- sphinx/
| +-- templates/
|
+-- tools/ (HERRAMIENTAS EXTERNAS)
| +-- plantuml.jar
|
+-- .codex/ (CONFIGURACION CODEX)
| +-- config.json
| +-- skills/
| +-- commands/
|
+-- .mywork/ (TRABAJO EN PROGRESO)
 +-- changes/ (specs en desarrollo)
 +-- specs/ (specs completadas)
 +-- work-logs/ (logs de trabajo)
```

## Capitulos Principales (source/)

### 01. Fundamentos

```
01_fundamentos/
+-- index.rst
+-- _fundamentos_conceptuales/
+-- _metodologias/
+-- _ontologia_terminologia/
+-- glosario_traduccion.rst
+-- principios_fundamentales.rst
```

CONTENIDO:
- Conceptos base de ADT
- Metodologia de traduccion
- Ontologia y taxonomias
- Principios semioticos

### 02. Procedimientos

```
02_procedimientos/
+-- index.rst
+-- workflow_general.rst
+-- modo_alta_fidelidad/
+-- modo_marcado_visual/
+-- modo_enriquecimiento/
```

CONTENIDO:
- Workflow general de traduccion
- Modos de traduccion detallados
- Procesos paso a paso

### 03. Estandares

```
03_estandares/
+-- index.rst
+-- calidad/
| +-- criterios_calidad.rst
| +-- metricas_traduccion.rst
+-- terminologia/
+-- restricciones/
```

CONTENIDO:
- Criterios de calidad
- Estandares terminologicos
- Restricciones y limitaciones

### 04. Reglas Operativas

```
04_reglas_operativas/
+-- index.rst
+-- matrices_decision/
| +-- MD_001_modo_1_vs_modo_2.rst
| +-- MD_002_cuando_enriquecer.rst
| +-- MD_003_nivel_segmentacion.rst
| +-- MD_004_traducir_vs_conservar.rst
+-- escenarios/
```

CONTENIDO:
- Matrices de decision
- Escenarios de aplicacion
- Reglas operacionales

### 05. Herramientas y Medios

```
05_herramientas_medios/
+-- index.rst
+-- sphinx/
| +-- configuracion.rst
| +-- scripts_verificacion.rst
+-- latex/
+-- markdown/
```

CONTENIDO:
- Documentacion de Sphinx
- Herramientas de generacion
- Configuraciones tecnicas

### 06. Casos Practicos

```
06_casos_practicos/
+-- index.rst
+-- ejemplos/
+-- ejercicios/
+-- errores_comunes/
```

CONTENIDO:
- Ejemplos completos de traduccion
- Ejercicios practicos
- Errores comunes y soluciones

### 07. Guias de Uso

```
07_guias_uso/
+-- index.rst
+-- tutoriales/
+-- faq.rst
+-- troubleshooting.rst
```

CONTENIDO:
- Tutoriales paso a paso
- Preguntas frecuentes
- Resolucion de problemas

### 08. Prompts

```
08_prompts/
+-- index.rst
+-- plantillas/
+-- ejemplos/
```

CONTENIDO:
- Plantillas reutilizables
- Prompts para LLMs
- Ejemplos de uso

### 09. Referencias

```
09_referencias/
+-- index.rst
+-- cheatsheets/
| +-- cheatsheet_rst.rst
+-- recursos_externos/
```

CONTENIDO:
- Cheatsheets rapidos
- Referencias tecnicas
- Enlaces a recursos

### 10. Apendices

```
10_apendices/
+-- index.rst
+-- glosario_adt.rst
+-- indices/
+-- recursos/
```

CONTENIDO:
- Glosario consolidado
- Indices varios
- Material suplementario

## Biblioteca de Traducciones

```
biblioteca/
+-- arc42/
 +-- index.rst
 +-- metadata_libro.rst
 +-- glosario_acumulativo.rst
 +-- sections/
 +-- 01_introduction_goals/
 | +-- original/
 | +-- traduccion/
 | +-- glosario_seccion.rst
 | +-- notas_traduccion.rst
 | +-- analisis_seccion.json
 +-- 02_constraints/
 | +-- [similar]
 +-- [01-12 secciones]
```

CONTENIDO:
- Traducciones de templates arquitectonicos
- Organizadas por dominio y framework
- Metadata completa por libro/seccion

## Framework Diataxis

```
diataxis/
+-- index.rst
+-- tutorials/
| +-- index.rst
| +-- [tutoriales]
+-- how_to_guides/
| +-- index.rst
| +-- [guias]
+-- reference/
| +-- index.rst
| +-- [referencias]
+-- explanation/
 +-- index.rst
 +-- [explicaciones]
```

CONTENIDO:
- Documentacion organizada segun Diataxis
- 4 tipos de contenido claramente separados

## Documentos Maestros

```
docs_maestros/
+-- ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
+-- METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
+-- SINTESIS_METODOLOGICA_ADT.rst
+-- REGLAS_ESTRUCTURA_PROYECTO.rst
```

CONTENIDO:
- Documentos fundamentales del proyecto
- Metodologia completa
- Reglas obligatorias

## Scripts de Automatizacion

```
scripts/
+-- traduccion/
| +-- adt_translator.py
| +-- arc42_scraper_python.py
| +-- translate_web_content.sh
+-- analizar_seccion.py
+-- validar_estructura.sh
+-- progreso_libro.sh
+-- init_libro.sh
+-- init_capitulo.sh
+-- generate_section_metadata.py
+-- README.md
```

CONTENIDO:
- Scripts de traduccion automatizada
- Herramientas de analisis
- Utilidades de inicializacion
- Scripts de validacion

## Configuracion Codex

```
.codex/
+-- config.json
+-- README.md
+-- skills/
| +-- project-context/
| | +-- SKILL.md
| | +-- references/
| +-- commit-helper/
| +-- work-logger/
| +-- translation-workflow/
| +-- validation-suite/
| +-- sphinx-expert/
| +-- spec-driven-dev/
+-- commands/
 +-- sphinx-init-chapter.md
 +-- sphinx-translate-section.md
 +-- sphinx-validate-build.md
 +-- sphinx-analyze-progress.md
```

CONTENIDO:
- Skills de Codex para asistencia
- Comandos complejos
- Referencias metodologicas

## Directorio de Trabajo

```
.mywork/
+-- changes/ (NO versionado)
| +-- YYYY-MM-DD-brief-desc/
| +-- requirements.md
| +-- design.md
| +-- tasks.md
| +-- implementation/
+-- specs/ (SI versionado)
| +-- YYYY-MM-DD-brief-desc/
| +-- requirements.md
| +-- design.md
| +-- tasks.md
+-- work-logs/ (SI versionado)
 +-- YYYY-MM-DD-titulo.md
 +-- archive/
 +-- YYYY/
```

CONTENIDO:
- Trabajo en progreso (changes/)
- Especificaciones completadas (specs/)
- Logs de trabajo documentados (work-logs/)

## Convenciones de Nomenclatura

### Capitulos
FORMATO: `XX_nombre/`
- XX = 01-10 (con cero padding)
- nombre = snake_case

### Archivos RST
FORMATO: `nombre_archivo.rst`
- snake_case
- extension .rst (minuscula)

### Directorios Especiales
FORMATO: `_nombre/`
- Prefijo underscore para metadata, templates, etc
- No se incluyen directamente en toctree

### Archivos de Script
FORMATO: `nombre_script.py` o `nombre_script.sh`
- snake_case
- extension apropiada (.py, .sh, etc)

## Paths Importantes

### Documentacion Principal
- Indice: `source/index.rst`
- Config Sphinx: `source/conf.py`

### Metodologia
- Fundamentos: `source/docs_maestros/`
- Procedimientos: `source/02_procedimientos/`

### Traducciones
- arc42: `source/biblioteca/arc42/`
- Otros: `source/biblioteca/<dominio>/<tema>/`

### Scripts
- Traduccion: `scripts/traduccion/`
- Validacion: `scripts/validar_estructura.sh`
- Analisis: `scripts/analizar_seccion.py`

### Build
- HTML: `build/html/`
- Doctrees: `build/doctrees/`

## Referencias

Documento completo:
- source/docs_maestros/REGLAS_ESTRUCTURA_PROYECTO.rst

Scripts de validacion:
- scripts/validar_estructura.sh

Documentacion Sphinx:
- source/conf.py
- source/05_herramientas_medios/sphinx/
