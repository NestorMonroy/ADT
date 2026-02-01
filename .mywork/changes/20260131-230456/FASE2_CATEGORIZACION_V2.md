# FASE 2: CATEGORIZACIÓN (Basada en Análisis Completo)

**Prerequisito**: ANALISIS_COMPLETO_BUILD.md ✅ COMPLETADO  
**Fecha**: 2026-01-31 23:06  
**Objetivo**: Agrupar issues similares para corrección eficiente basándose en datos reales

---

## FLUJO CORRECTO

```
FASE 0: Preparación ✅
    ↓
FASE 1: Análisis Inicial ✅
    ↓
GENERAR: ANALISIS_COMPLETO_BUILD.md ✅
    ↓
FASE 2: Categorización ← ESTAMOS AQUÍ
    ↓
FASE 3: Priorización
    ↓
FASE 4: Ejecución
```

**⚠️ REGLA CRÍTICA**: NO puedes hacer FASE 2 sin tener ANALISIS_COMPLETO_BUILD.md

**Por qué**: Categorizar sin datos reales = asumir números → estimaciones incorrectas → plan equivocado

---

## CATEGORÍA 1: Section Structure - CRITICAL

**Issues**: 31 CRITICAL (datos reales del análisis)
- Unexpected section title: 27
- Missing matching underline: 4

**Archivos afectados**: 5 archivos (datos reales)
```
source\02_procedimientos\WORKFLOW_v1_6_0_ACTUALIZACION.rst
source\02_procedimientos\workflow_general.rst
source\06_casos_practicos\errores_comunes\error_01_omisiones.rst
source\07_guias_uso\guia_rapida.rst
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
```

**Distribución por archivo** (del análisis):
```
19    source\02_procedimientos\workflow_general.rst
3     source\02_procedimientos\WORKFLOW_v1_6_0_ACTUALIZACION.rst
3     source\07_guias_uso\guia_rapida.rst
3     source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
3     source\06_casos_practicos\errores_comunes\error_01_omisiones.rst
```

**Concentración**: 61% (19/31) en `workflow_general.rst`

**Complejidad**: COMPLEJO
- Requiere entender estructura del documento
- Decisiones sobre jerarquía de secciones
- Afecta navegación y TOC
- Mayor concentración en 1 archivo (workflow_general.rst)

**Riesgo automatización**: ALTO
- Contexto crítico
- Puede romper estructura completa
- Requiere comprensión semántica

**Estrategia**: MANUAL PURO
**Procedimiento disponible**: NO (requiere análisis caso por caso)
**Prioridad**: URGENTE (bloquea build correcto)

---

## CATEGORÍA 2: List-Table Errors - ERROR

**Issues**: 8 ERROR (datos reales del análisis)
- Error parsing list-table directive: 5
- Empty list-table directive: 3

**Archivos afectados**: 5 archivos únicos (datos reales)
```
source\02_procedimientos\workflow_general.rst (3 issues)
source\04_reglas_operativas\matrices_decision\MD_002_cuando_enriquecer.rst (1)
source\07_guias_uso\guia_rapida.rst (1)
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst (2)
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\traduccion\quality_ejemplo_tpu_1.rst (1)
```

**Concentración**: 37.5% (3/8) en `workflow_general.rst`

**Complejidad**: COMPLEJO
- Requiere entender contenido de tabla
- Sintaxis de directiva específica
- Puede tener datos importantes

**Riesgo automatización**: ALTO
- Contenido varía por tabla
- Pérdida de datos si se hace mal
- Requiere revisión visual

**Estrategia**: MANUAL PURO
**Procedimiento disponible**: NO (análisis caso por caso)
**Prioridad**: ALTA (afecta renderizado)

---

## CATEGORÍA 3: Transitions - ERROR

**Issues**: 6 ERROR (datos reales)
- Document may not begin with a transition: 6

**Archivos afectados**: 3 archivos únicos (datos reales)
```
source\02_procedimientos\workflow_general.rst (3 issues)
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\12_glossary\traduccion\glossary_tip_4.rst (2)
source\docs_maestros\SINTESIS_METODOLOGICA_ADT.rst (1)
```

**Concentración**: 50% (3/6) en `workflow_general.rst`

**Complejidad**: TRIVIAL
- Solo eliminar línea de separación inicial (====)
- Patrón muy claro y documentado
- No afecta contenido

**Riesgo automatización**: BAJO
- Patrón predecible
- Fácil de validar
- Procedimiento claro en sphinx-expert

**Estrategia**: MANUAL RÁPIDO (o script simple con validación)
**Procedimiento disponible**: SÍ (sphinx-expert)
**Prioridad**: MEDIA (ERROR pero trivial de corregir)

---

## CATEGORÍA 4: Headers Incorrectos - WARNING

**Issues**: 309 WARNING (datos reales del análisis)
- Document headings start at H3, not H1: 139
- Document headings start at H2, not H1: 132
- Document headings start at H4, not H1: 23
- Non-consecutive header level increase: 13
- Title underline too short: 2

**Archivos afectados**: 294 archivos únicos (del headers_files.tmp - 21K)

**Top 10 archivos más afectados**:
```
(Ver ANALISIS_COMPLETO_BUILD.md sección 5.2)
```

**Distribución**: Muy dispersa (promedio ~1 issue/archivo)

**Complejidad**: MODERADO
- Requiere entender jerarquía del documento
- Decisión: ¿agregar H1 o cambiar niveles?
- Puede afectar TOC
- Muchos archivos afectados

**Riesgo automatización**: MEDIO-ALTO
- Contexto importante
- Diferentes estrategias según documento
- Procedimiento ayuda pero no automatizable

**Estrategia**: MANUAL SELECTIVO o DEFER
**Procedimiento disponible**: SÍ (sphinx-expert)
**Prioridad**: BAJA (no bloquea, pero son muchos)

---

## CATEGORÍA 5: Blank Lines - WARNING

**Issues**: 259 WARNING (datos reales del análisis)
- Block quote ends without blank line: 87
- Enumerated list ends without blank line: 84
- Explicit markup ends without blank line: 70
- Bullet list ends without blank line: 11
- Field list ends without blank line: 4
- Line block ends without blank line: 3

**Archivos afectados**: 179 archivos únicos (del blanklines_files.tmp - 3.1K)

**Distribución**: Dispersa (promedio ~1.4 issues/archivo)

**Complejidad**: MODERADO
- Patrón claro (agregar línea en blanco)
- Pero requiere identificar contexto correcto
- No debe romper otras estructuras
- Procedimiento documentado y probado

**Riesgo automatización**: BAJO
- Patrón repetitivo
- Procedimiento documentado en sphinx-expert
- Fácil de validar (build después)

**Estrategia**: SCRIPT SEGURO (con 7 protecciones)
**Procedimiento disponible**: SÍ (sphinx-expert)
**Prioridad**: MEDIA (numeroso pero automatizable)

---

## CATEGORÍA 6: Lexers Desconocidos - WARNING

**Issues**: 8 WARNING (datos reales)
- Pygments lexer name 'PlantUML' is not known: 6
- Pygments lexer name 'plantuml' is not known: 2

**Archivos afectados**: 9 archivos .md únicos (datos reales)
```
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\01-requirements\2016-03-01-t-1-9.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-5.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-6.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-7.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-8.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-9.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-02-t-6-11.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2016-03-01-t-8-7.md
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\2016-03-01-t-1-9.md
```

**Ubicación**: TODOS en `arc42_documentation/original/_posts` (archivos Markdown, no RST)

**Variantes**: 'PlantUML' (mayúscula) y 'plantuml' (minúscula)

**Complejidad**: TRIVIAL
- Cambiar 'PlantUML'/'plantuml' → 'text' en code-blocks
- O instalar lexer PlantUML
- O configurar en conf.py
- No afecta contenido

**Riesgo automatización**: BAJO
- Patrón único y localizado
- Fácil de reemplazar (búsqueda global)
- Validación simple

**Estrategia**: SCRIPT TRIVIAL o búsqueda/reemplazo manual
**Procedimiento disponible**: SÍ (sphinx-expert)
**Prioridad**: BAJA (quick win, 9 archivos concentrados)

---

## CATEGORÍA 7: Markup Incompleto - WARNING

**Issues**: 5 WARNING (datos reales)
- Inline strong start-string without end-string: 3
- Inline emphasis start-string without end-string: 2

**Archivos afectados**: ~3-5 archivos (del análisis)

**Complejidad**: MODERADO
- Requiere encontrar dónde cerrar markup
- Puede ser error tipográfico
- Requiere leer contexto

**Riesgo automatización**: MEDIO
- Contexto necesario
- No siempre claro dónde cerrar

**Estrategia**: MANUAL
**Procedimiento disponible**: NO
**Prioridad**: BAJA

---

## CATEGORÍA 8: Referencias - WARNING

**Issues**: 2 WARNING (datos reales)
- Footnote [#] is not referenced: 2

**Archivos afectados**: ~2 archivos

**Complejidad**: TRIVIAL
- Eliminar footnote o agregar referencia

**Riesgo automatización**: BAJO

**Estrategia**: MANUAL RÁPIDO
**Procedimiento disponible**: NO
**Prioridad**: BAJA

---

## CATEGORÍA 9: Glossary Terms - WARNING

**Issues**: 5 WARNING (datos reales)
- term not in glossary: 'Unreasonable'
- term not in glossary: 'Third Party Contracting'
- term not in glossary: 'Reference Architecture'
- term not in glossary: 'Programming Guidelines'
- (más términos)

**Archivos afectados**: ~3 archivos

**Complejidad**: MODERADO
- Agregar términos al glosario
- O cambiar referencias
- Requiere decisión: ¿agregar o eliminar referencia?

**Riesgo automatización**: MEDIO

**Estrategia**: MANUAL
**Procedimiento disponible**: NO
**Prioridad**: BAJA

---

## CATEGORÍA 10: Otros - ERROR + WARNING

**Issues**: ~15 restantes (datos reales del análisis)
- Unknown target name: 1 ERROR
- Unexpected indentation: 1 ERROR
- Content block expected for note: 1 ERROR
- Toctree glob pattern: 1 WARNING
- Otros: ~11 WARNING

**Complejidad**: VARIABLE

**Estrategia**: EVALUAR CASO POR CASO

**Prioridad**: BAJA

---

## RESUMEN DE CATEGORIZACIÓN (CON DATOS REALES)

| # | Categoría | Issues | Archivos | Concentración | Complejidad | Riesgo | Estrategia |
|---|-----------|--------|----------|---------------|-------------|--------|------------|
| 1 | Section Structure (CRITICAL) | 31 | 5 | 61% en 1 archivo | COMPLEJO | ALTO | Manual puro |
| 2 | List-Tables (ERROR) | 8 | 5 | 37% en 1 archivo | COMPLEJO | ALTO | Manual puro |
| 3 | Transitions (ERROR) | 6 | 3 | 50% en 1 archivo | TRIVIAL | BAJO | Manual rápido |
| 4 | Headers (WARNING) | 309 | 294 | Disperso | MODERADO | MEDIO-ALTO | Manual selectivo/Defer |
| 5 | Blank Lines (WARNING) | 259 | 179 | Disperso | MODERADO | BAJO | Script seguro |
| 6 | Lexers (WARNING) | 8 | 9 | 100% en .md | TRIVIAL | BAJO | Script trivial |
| 7 | Markup (WARNING) | 5 | ~5 | - | MODERADO | MEDIO | Manual |
| 8 | Referencias (WARNING) | 2 | ~2 | - | TRIVIAL | BAJO | Manual rápido |
| 9 | Glossary (WARNING) | 5 | ~3 | - | MODERADO | MEDIO | Manual |
| 10 | Otros | ~15 | Variable | - | VARIABLE | VARIABLE | Caso x caso |

**Total categorizado**: 648/661 (98%)

---

## HALLAZGOS CLAVE DEL ANÁLISIS

### 1. Archivo con Mayor Concentración: `workflow_general.rst`

**Issues en este archivo**:
- CRITICAL: 19/31 (61%)
- ERROR List-Tables: 3/8 (37%)
- ERROR Transitions: 3/6 (50%)
- **Total**: 25 issues en 1 archivo

**Implicación**: Corregir este archivo primero tiene máximo impacto.

### 2. Lexers Son Archivos Markdown

**Descubrimiento**: Los 8 WARNING de Lexers están en archivos .md (no .rst)
**Ubicación**: `arc42_documentation/original/_posts`
**Implicación**: Estrategia diferente (Markdown vs RST)

### 3. Dispersión de WARNING

**Headers**: 309 issues / 294 archivos = ~1 issue/archivo (muy disperso)
**Blank Lines**: 259 issues / 179 archivos = ~1.4 issues/archivo (disperso)

**Implicación**: Automatización viable para Blank Lines, evaluar Headers.

### 4. Archivos con CRITICAL + ERROR

**Intersección** (del análisis):
```
source\02_procedimientos\workflow_general.rst
source\07_guias_uso\guia_rapida.rst
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
```

**Implicación**: 3 archivos de máxima prioridad.

---

## VALIDACIÓN DE LA CATEGORIZACIÓN

✅ **Basada en datos reales**: Todos los números del ANALISIS_COMPLETO_BUILD.md
✅ **Archivos identificados**: Listados completos de archivos afectados
✅ **Distribución analizada**: Concentración vs dispersión medida
✅ **Hallazgos documentados**: Descubrimientos del análisis incorporados
✅ **Complejidad asignada**: Basada en procedimientos disponibles
✅ **Riesgo evaluado**: Considerando concentración y contexto
✅ **Estrategia definida**: Manual vs Script según riesgo

---

## OUTPUT FASE 2

✅ 10 categorías identificadas (con datos reales)
✅ Complejidad asignada (basada en análisis)
✅ Riesgo de automatización evaluado (basado en concentración)
✅ Estrategia recomendada (basada en procedimientos + riesgo)
✅ Procedimientos disponibles identificados
✅ Hallazgos clave documentados
✅ Archivo de mayor impacto identificado (workflow_general.rst)

**Prerequisito cumplido**: ANALISIS_COMPLETO_BUILD.md ✅
**Listo para**: FASE 3 - Priorización

---

## LECCIÓN APRENDIDA

**Anti-Patrón Evitado**: "Categorizar sin análisis completo"

**Antes** (FASE2_CATEGORIZACION.md original):
- Números estimados (~5-6 archivos con ERROR)
- "Muchos archivos" sin conteo real
- Sin identificar concentración

**Ahora** (FASE2_CATEGORIZACION_V2.md):
- Números exactos (5 archivos con List-Tables ERROR)
- Conteos reales (179 archivos con Blank Lines)
- Concentración medida (61% CRITICAL en 1 archivo)

**Impacto**: Plan más preciso, priorización correcta, estimaciones realistas.
