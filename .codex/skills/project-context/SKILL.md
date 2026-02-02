---
name: project-context
description: "Proporciona contexto metodologico completo del proyecto ADT. Usar cuando el usuario necesite entender metodologia ADT, frameworks (Diataxis, arc42), estructura del proyecto, o terminologia clave."
version: 1.2.0
created: 2026-01-29
updated: 2026-02-01
---

# Project Context - ADT Documentation

## Cuando usar

- Usuario necesita entender metodologia ADT
- Preguntas sobre estructura del proyecto
- Referencias a Diataxis, arc42, Sphinx
- Onboarding de colaboradores
- Decisiones sobre organizacion de contenido
- Explicacion de terminologia especializada

---

## Decision Framework: ¿Qué Sección Consultar?

**Usa este framework para navegar eficientemente el contexto**:

1. **¿Usuario pregunta "¿qué es ADT?"**
   → Ver "Metodologia ADT" (principios fundamentales)

2. **¿Usuario pregunta sobre Diataxis o arc42?**
   → Ver "Frameworks Aplicados"

3. **¿Usuario necesita entender estructura de directorios?**
   → Ver "Estructura del Proyecto"

4. **¿Usuario pregunta por términos específicos (signifiant, etc.)?**
   → Ver "Terminologia Clave"

5. **¿Usuario necesita saber DÓNDE ubicar contenido nuevo?**
   → Ver "Estructura del Proyecto" + "Frameworks Aplicados"

6. **¿Es nuevo colaborador necesitando onboarding?**
   → Leer skill completo (overview general)

7. **¿Usuario pregunta sobre herramientas (Sphinx, scripts)?**
   → Ver "Herramientas y Scripts"

8. **¿No sabes qué sección exactamente?**
   → Leer skill completo (es referencia, no muy largo)

**Regla de oro**: Este skill es **referencia**, no workflow operacional

---

## Trigger Patterns

### Señales Explícitas
- Usuario pregunta: "¿qué es ADT?"
- Usuario pregunta: "¿cómo funciona Diataxis?"
- Usuario pregunta: "¿dónde pongo este contenido?"
- Usuario dice: "explícame la metodología"
- Usuario nuevo pide orientación
- Usuario menciona: "según nuestra metodología"

### Señales Implícitas
- Usuario parece confundido sobre estructura
- Usuario menciona términos sin entenderlos
- Usuario toma decisiones sin conocer convenciones
- Usuario pregunta "¿por qué hacemos X así?"
- Contexto indica falta de conocimiento del proyecto

### Trigger Words
- "ADT", "metodología", "framework"
- "Diataxis", "arc42", "Sphinx"
- "estructura", "organización"
- "dónde", "cómo organizar", "convenciones"
- "signifiant", "signifié", "transformación"

**Anti-triggers** (NO es para esto):
- Este skill NO ejecuta código
- Este skill NO hace cambios en archivos
- Este skill NO crea contenido
- Solo proporciona **contexto y referencia**

---

## Self-Check Before Using Context

**Verificar necesidad real de consultar contexto**:

### Pre-Context Checks
- [ ] ¿Realmente necesito entender el contexto del proyecto?
- [ ] ¿O solo necesito ejecutar una tarea operacional?
- [ ] ¿Sé qué sección específica busco?
- [ ] ¿O necesito overview general?

**Si solo ejecutar tarea → Usar skill operacional directamente**

### During Context Use
- [ ] ¿Encontré la información que buscaba?
- [ ] ¿Entiendo los conceptos clave ahora?
- [ ] ¿Sé cómo aplicar esta información?
- [ ] ¿Necesito consultar otra sección?

**Si NO → Buscar en otra sección o preguntar al usuario**

### Post-Context Checks
- [ ] ¿Tengo suficiente información para proceder?
- [ ] ¿Entiendo las convenciones del proyecto?
- [ ] ¿Sé qué skill operacional usar ahora?
- [ ] ¿Puedo tomar decisiones informadas?

**Si NO → Profundizar o pedir aclaraciones al usuario**

---

## Metodologia ADT

ADT = Arquitectura Documental de Traduccion

### Principios Fundamentales

1. TRANSFORMACION NO TRADUCCION
 - La traduccion es una transformacion entre sistemas semioticos
 - Signifiant vs Signifie: forma vs contenido
 - Equivalencia funcional sobre equivalencia literal

2. FIDELIDAD ESTRUCTURAL
 - Preservar jerarquia y relaciones entre conceptos
 - Mantener coherencia terminologica
 - Respetar convenciones del medio destino

3. ENRIQUECIMIENTO CONTEXTUAL
 - Agregar metadata cuando mejore comprension
 - Explicitar relaciones implicitas en el original
 - Mantener trazabilidad al documento fuente

Ver detalles completos:
- references/metodologias/adt_fundamentals.md
- references/metodologias/transformation_theory.md

## Frameworks Aplicados

### Diataxis

Sistema de organizacion de documentacion en 4 cuadrantes:

TUTORIALS (learning-oriented)
- Guian paso a paso en aprendizaje
- Foco en el proceso de aprender
- Ubicacion: source/diataxis/tutorials/

HOW-TO GUIDES (task-oriented)
- Resuelven problemas especificos
- Foco en lograr un objetivo
- Ubicacion: source/diataxis/how_to_guides/

REFERENCE (information-oriented)
- Describen el sistema con precision
- Foco en informacion exacta
- Ubicacion: source/diataxis/reference/

EXPLANATION (understanding-oriented)
- Clarifican conceptos y decision
es
- Foco en comprension profunda
- Ubicacion: source/diataxis/explanation/

Ver: references/frameworks/diataxis_implementation.md

### arc42

Template de documentacion arquitectonica en 12 secciones estandar.

Ubicacion: source/biblioteca/arc42/sections/

Las 12 secciones:
01. Introduction and Goals - Proposito y objetivos
02. Constraints - Restricciones organizacionales y tecnicas
03. Context and Scope - Contexto de negocio y tecnico
04. Solution Strategy - Decisiones fundamentales
05. Building Blocks View - Estructura estatica
06. Runtime View - Comportamiento en ejecucion
07. Deployment View - Infraestructura
08. Crosscutting Concepts - Conceptos transversales
09. Architecture Decisions - ADRs importantes
10. Quality Requirements - Escenarios de calidad
11. Risks and Technical Debt - Riesgos identificados
12. Glossary - Terminologia del dominio

Ver: references/frameworks/arc42_structure.md

## Estructura del Proyecto

### Regla Fundamental

Segun REGLAS_ESTRUCTURA_PROYECTO.rst:

REGLA MAESTRA:
- source/ contiene SOLO contenido documental (se compila a HTML)
- Raiz contiene herramientas, scripts, configuraciones

### Directorios Principales

RAIZ (ADT/):
```
ADT/
+-- Makefile (herramienta compilacion)
+-- make.bat (batch Windows)
+-- build/ (salida HTML - no versionado)
+-- source/ (CONTENIDO DOCUMENTAL)
+-- scripts/ (automatizacion)
+-- config/ (configuraciones)
+-- tools/ (herramientas externas)
+-- .codex/ (configuracion Codex)
+-- .mywork/ (trabajo en progreso)
```

SOURCE (source/):
```
source/
+-- conf.py (config Sphinx)
+-- index.rst (indice principal)
+-- _static/ (recursos estaticos)
+-- _templates/ (templates Sphinx)
|
+-- 01_fundamentos/ (conceptos base, metodologia)
+-- 02_procedimientos/ (workflows, modos traduccion)
+-- 03_estandares/ (calidad, terminologia)
+-- 04_reglas_operativas/ (matrices decision)
+-- 05_herramientas_medios/ (Sphinx, LaTeX, MD)
+-- 06_casos_practicos/ (ejemplos, ejercicios)
+-- 07_guias_uso/ (tutoriales, FAQ)
+-- 08_prompts/ (plantillas)
+-- 09_referencias/ (cheatsheets)
+-- 10_apendices/ (glosarios, indices)
|
+-- biblioteca/ (traducciones)
| +-- arc42/
| +-- metadata_libro.rst
| +-- glosario_acumulativo.rst
| +-- sections/ (12 secciones)
|
+-- diataxis/ (framework organizacion)
| +-- tutorials/
| +-- how_to_guides/
| +-- reference/
| +-- explanation/
|
+-- docs_maestros/ (documentos fundamentales)
 +-- ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
 +-- METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
 +-- SINTESIS_METODOLOGICA_ADT.rst
 +-- REGLAS_ESTRUCTURA_PROYECTO.rst
```

Ver: references/estructura/reglas_proyecto.md
Ver: references/estructura/directory_layout.md

## Modos de Traduccion

### 1. Alta Fidelidad

CUANDO USAR:
- Especificaciones tecnicas sensibles
- Contratos y documentacion legal
- APIs y documentacion de referencia
- Documentacion que requiere precision maxima

CARACTERISTICAS:
- Preservacion maxima de estructura original
- Minimas transformaciones
- Terminologia tecnica sin traducir
- Formato conservado al maximo

### 2. Marcado Visual

CUANDO USAR:
- Tutoriales y guias educativas
- Guias de usuario
- Material que beneficia de aclaraciones
- Documentacion para principiantes

CARACTERISTICAS:
- Enriquecimiento con admoniciones (note, warning, tip)
- Mejora de navegabilidad
- Agregado de contexto visual
- Facilitar comprension

### 3. Enriquecimiento

CUANDO USAR:
- Material de referencia complejo
- Conceptos que requieren expansion
- Documentacion con contexto implicito
- Material educativo avanzado

CARACTERISTICAS:
- Expansion de conceptos
- Agregado de ejemplos practicos
- Enlaces a material relacionado
- Profundizacion en temas

Ver: references/metodologias/translation_modes.md

## Scripts Disponibles

### Scripts de Traduccion

adt_translator.py
- Ubicacion: scripts/traduccion/adt_translator.py
- Proposito: Traductor principal metodologia ADT
- Uso: python scripts/traduccion/adt_translator.py --input <fuente> --output <destino> --mode <modo>

arc42_scraper_python.py
- Ubicacion: scripts/traduccion/arc42_scraper_python.py
- Proposito: Extraccion y traduccion de secciones arc42
- Uso: python scripts/traduccion/arc42_scraper_python.py --section <num> --mode <modo>

translate_web_content.sh
- Ubicacion: scripts/traduccion/translate_web_content.sh
- Proposito: Traduccion de contenido web
- Uso: bash scripts/traduccion/translate_web_content.sh <url> <output>

### Scripts de Analisis

analizar_seccion.py
- Ubicacion: scripts/analizar_seccion.py
- Proposito: Analisis automatico de estructura de seccion
- Uso: python scripts/analizar_seccion.py <ruta_seccion>
- Output: analisis_seccion.json

validar_estructura.sh
- Ubicacion: scripts/validar_estructura.sh
- Proposito: Validacion de conformidad con reglas
- Uso: bash scripts/validar_estructura.sh [ruta]

progreso_libro.sh
- Ubicacion: scripts/progreso_libro.sh
- Proposito: Calcular progreso de traduccion
- Uso: bash scripts/progreso_libro.sh <ruta_libro>

### Scripts de Inicializacion

init_libro.sh
- Ubicacion: scripts/init_libro.sh
- Proposito: Inicializar estructura de nuevo libro
- Uso: bash scripts/init_libro.sh <nombre_libro>

init_capitulo.sh
- Ubicacion: scripts/init_capitulo.sh
- Proposito: Inicializar estructura de nuevo capitulo
- Uso: bash scripts/init_capitulo.sh <numero> <nombre>

### Makefile Targets

Build:
```bash
make html # Compilar a HTML
make clean # Limpiar build
make linkcheck # Validar enlaces
make coverage # Coverage de docs
```

Ver guia completa: references/scripts-guide/available_scripts.md

## Workflow General de Traduccion

Ver: source/02_procedimientos/workflow_general.rst

Fases del workflow:

1. ANALISIS DE DOCUMENTO FUENTE
 - Identificar tipo de documento
 - Analizar estructura
 - Determinar modo de traduccion
 - Validar coherencia con destino

2. CONFIGURACION DE TRANSFORMACION
 - Seleccionar script apropiado
 - Configurar parametros
 - Preparar glosario terminologico

3. EJECUCION DE TRANSFORMACION
 - Ejecutar script de traduccion
 - Aplicar transformaciones especificas
 - Generar metadata

4. VALIDACION DE SALIDA
 - Validar sintaxis RST
 - Verificar coherencia estructural
 - Validar calidad de traduccion
 - Revisar metadata

5. INTEGRACION EN PROYECTO
 - Actualizar toctree
 - Generar cross-references
 - Actualizar glosario
 - Documentar proceso
 - Commit

## Terminologia Clave

ADT: Arquitectura Documental de Traduccion

RST: reStructuredText (markup de Sphinx)

Signifiant: Significante, forma material del signo (palabras, estructura)

Signifie: Significado, contenido conceptual

Diataxis: Framework de organizacion documental en 4 cuadrantes

arc42: Template de documentacion arquitectonica en 12 secciones

Modo de Traduccion: Estrategia de transformacion (alta_fidelidad, marcado_visual, enriquecimiento)

Toctree: Tabla de contenidos de Sphinx (Table of Contents Tree)

Cross-reference: Referencia cruzada entre documentos

Admonition: Bloque especial de RST (note, warning, tip, etc)

Build: Proceso de compilacion de RST a HTML

Ver glosario completo: source/10_apendices/glosario_adt.rst

## Documentos Maestros

Ubicacion: source/docs_maestros/

ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
- Fundamentos de la metodologia ADT
- Principios semioticos
- Teoria de la transformacion

METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
- Metodologia especifica aplicada
- Casos de estudio
- Ejemplos practicos

SINTESIS_METODOLOGICA_ADT.rst
- Sintesis consolidada
- Integracion de conceptos
- Guia rapida

REGLAS_ESTRUCTURA_PROYECTO.rst
- Reglas OBLIGATORIAS del proyecto
- Estructura de directorios
- Validacion de conformidad

## Recursos Adicionales

### Cheatsheets
source/09_referencias/cheatsheets/cheatsheet_rst.rst
- Sintaxis RST rapida
- Directivas comunes
- Ejemplos practicos

### FAQ
source/07_guias_uso/faq.rst
- Preguntas frecuentes
- Respuestas rapidas
- Troubleshooting basico

### Troubleshooting
source/07_guias_uso/troubleshooting.rst
- Problemas comunes
- Soluciones paso a paso
- Diagnostico de errores

### Matrices de Decision
source/04_reglas_operativas/matrices_decision/
- MD_001: Seleccion de modo de traduccion
- MD_002: Cuando enriquecer contenido
- MD_003: Nivel de segmentacion
- MD_004: Traducir vs conservar

## Flujo de Trabajo Tipico

### Traducir Nueva Seccion arc42

1. Analizar seccion si necesario:
 ```bash
 python scripts/analizar_seccion.py source/biblioteca/arc42/sections/02_constraints/
 ```

2. Traducir contenido:
 ```bash
 python scripts/traduccion/arc42_scraper_python.py --section 02 --mode alta_fidelidad
 ```

3. Validar estructura:
 ```bash
 bash scripts/validar_estructura.sh
 ```

4. Build y verificar:
 ```bash
 make clean html
 make linkcheck
 ```

5. Commit:
 ```bash
 git add source/biblioteca/arc42/sections/02_constraints/
 git commit -m "feat(traduccion): agregar seccion arc42 Constraints"
 ```

### Crear Nuevo Capitulo

1. Inicializar estructura:
 ```bash
 bash scripts/init_capitulo.sh 11 nuevos_conceptos
 ```

2. Agregar contenido en source/11_nuevos_conceptos/

3. Actualizar toctree en source/index.rst

4. Validar y commit

## Convenciones del Proyecto

### Nomenclatura de Archivos

Capitulos: 01_nombre/, 02_nombre/ (numero con cero padding, underscore, snake_case)

Secciones: nombre_seccion.rst (snake_case, sin espacios)

Metadata: _metadata/ (prefijo underscore)

Templates: _templates/ (prefijo underscore)

### Estructura RST

```rst
Titulo Principal (nivel 0)
==========================

Seccion (nivel 1)
-----------------

Subseccion (nivel 2)
~~~~~~~~~~~~~~~~~~~~

Subsubseccion (nivel 3)
^^^^^^^^^^^^^^^^^^^^^^^
```

### Commits

Seguir Conventional Commits:
```
feat(traduccion): agregar nueva seccion arc42
fix(estructura): corregir enlaces rotos
docs(fundamentos): actualizar glosario
```

Ver skill commit-helper para detalles

## Notas Importantes

- SIEMPRE respetar REGLAS_ESTRUCTURA_PROYECTO.rst
- Validar build antes de cada commit: make html
- Mantener coherencia terminologica con glosario
- Documentar decisiones arquitectonicas importantes
- Usar scripts existentes antes de crear nuevos
- Consultar workflow_general.rst ante dudas de proceso
- Referencias en este skill apuntan a archivos reales del proyecto

---

## Optimización de Prompts y Contexto

Para mejorar cómo proporcionas contexto a Claude o cómo estructuras prompts relacionados con el proyecto ADT, consultar:

**`.codex/skills/anthropic-best-practices/prompting-tips.md`**

### Cuándo Consultar

**Situaciones donde prompting-tips.md es útil**:
- Necesitas explicar contexto complejo del proyecto a Claude
- Claude no entiende referencias a metodología ADT
- Trabajas en tareas multi-paso que requieren contexto del proyecto
- Quieres mejorar consistencia en cómo se usa terminología

### Técnicas Relevantes de prompting-tips.md

**Agregar Contexto Efectivamente**:
```
Contexto del proyecto ADT:
- Documentación técnica de arquitectura (arc42)
- Framework: Diataxis para organización de contenido
- Build system: Sphinx con Python 3.11+
- Idioma: Español (traducción de docs técnicos inglés→español)

[tu tarea específica]
```

**Trabajar con Terminología del Proyecto**:
```
Usar terminología consistente con glossary de ADT:
- "Modo Alta Fidelidad" (no "traducción literal")
- "arc42" (no "plantilla de arquitectura")
- "Diataxis" (no "framework de documentación")

[tu tarea]
```

**State Management para Proyectos Largos**:
- Usar JSON para trackear estado de trabajo en ADT
- Updates textuales de progreso
- Checkpoints después de secciones mayores

### Beneficio

Aplicar técnicas de prompting-tips.md cuando trabajas con ADT:
- Claude entiende mejor el contexto metodológico
- Terminología se usa consistentemente
- Tareas complejas se completan con mayor precisión
- Menos necesidad de re-explicar conceptos del proyecto

---

## Changelog

### v1.2.0 - 2026-02-01 - Integración con anthropic-best-practices

**Agregado**:
- Sección "Optimización de Prompts y Contexto"
- Referencia a anthropic-best-practices/prompting-tips.md
- Técnicas relevantes para trabajar con contexto ADT
- Ejemplos de cómo agregar contexto efectivamente

**Contenido de nueva sección**:
- Cuándo consultar prompting-tips.md
- Técnicas relevantes (agregar contexto, terminología, state management)
- Beneficios de aplicar técnicas a proyecto ADT

**Beneficio**:
- Usuarios saben cómo mejorar prompts relacionados con ADT
- Contexto del proyecto se comunica más efectivamente
- Terminología se usa consistentemente
- Mejor integración entre project-context y prompting best practices

### v1.1.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y navegación**:

✅ **Decision Framework** - ¿Qué Sección Consultar?
- 8 preguntas para navegar el contexto eficientemente
- Mapeo claro a secciones específicas
- Diferencia entre onboarding completo vs consulta específica

✅ **Trigger Patterns** - Cuándo consultar este skill
- Señales explícitas (usuario pregunta "¿qué es ADT?")
- Señales implícitas (confusión sobre estructura)
- Clarifica que es REFERENCIA, no ejecución

✅ **Self-Check Mechanisms** - Navegación efectiva
- Pre-Context (¿necesito contexto o ejecutar tarea?)
- During (¿encontré información?)
- Post-Context (¿puedo proceder informadamente?)

**Líneas agregadas**: ~85 líneas

**Beneficio principal**:
- Usuarios navegan contexto más eficientemente
- Claro que skill es referencia informativa, no operacional
- Mejor onboarding de nuevos colaboradores

### v1.0.0 - 2026-01-30
- Versión inicial
- Metodología ADT documentada
- Frameworks (Diataxis, arc42)
- Estructura del proyecto
- Terminología clave
