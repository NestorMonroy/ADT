# FASE 2: CATEGORIZACIÓN

**Objetivo**: Agrupar issues similares para corrección eficiente

---

## CATEGORÍA 1: Section Structure - CRITICAL

**Issues**: 31 CRITICAL
- Unexpected section title: 27
- Missing matching underline: 4

**Archivos afectados**: 5
- workflow_general.rst
- WORKFLOW_v1_6_0_ACTUALIZACION.rst
- guia_rapida.rst
- error_01_omisiones.rst
- GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst

**Complejidad**: COMPLEJO
- Requiere entender estructura del documento
- Decisiones sobre jerarquía de secciones
- Afecta navegación y TOC

**Riesgo automatización**: ALTO
- Contexto crítico
- Puede romper estructura completa
- Requiere comprensión semántica

**Estrategia**: MANUAL PURO
**Procedimiento disponible**: NO (requiere análisis caso por caso)

---

## CATEGORÍA 2: List-Table Errors - ERROR

**Issues**: 8 ERROR
- Error parsing list-table directive: 5
- Empty list-table directive: 3

**Archivos afectados**: ~5-6

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

---

## CATEGORÍA 3: Transitions - ERROR

**Issues**: 6 ERROR
- Document may not begin with transition: 6

**Archivos afectados**: ~3

**Complejidad**: TRIVIAL
- Solo eliminar línea de separación inicial (====)
- Patrón muy claro
- No afecta contenido

**Riesgo automatización**: BAJO
- Patrón predecible
- Fácil de validar
- Procedimiento claro en sphinx-expert

**Estrategia**: MANUAL RÁPIDO (o script simple)
**Procedimiento disponible**: SÍ (sphinx-expert)

---

## CATEGORÍA 4: Headers Incorrectos - WARNING

**Issues**: 309 WARNING
- Document headings start at H3, not H1: 139
- Document headings start at H2, not H1: 132
- Document headings start at H4, not H1: 23
- Non-consecutive header level increase: 13
- Title underline too short: 2

**Archivos afectados**: Muchos

**Complejidad**: MODERADO
- Requiere entender jerarquía del documento
- Decisión: ¿agregar H1 o cambiar niveles?
- Puede afectar TOC

**Riesgo automatización**: MEDIO-ALTO
- Contexto importante
- Diferentes estrategias según documento
- Procedimiento ayuda pero no automatizable

**Estrategia**: MANUAL SELECTIVO
**Procedimiento disponible**: SÍ (sphinx-expert)

---

## CATEGORÍA 5: Blank Lines - WARNING

**Issues**: 259 WARNING
- Block quote ends without blank line: 87
- Enumerated list ends without blank line: 84
- Explicit markup ends without blank line: 70
- Bullet list ends without blank line: 11
- Field list ends without blank line: 4
- Line block ends without blank line: 3

**Archivos afectados**: Muchos

**Complejidad**: MODERADO
- Patrón claro (agregar línea en blanco)
- Pero requiere identificar contexto correcto
- No debe romper otras estructuras

**Riesgo automatización**: BAJO
- Patrón repetitivo
- Procedimiento documentado
- Fácil de validar (build después)

**Estrategia**: SCRIPT SEGURO (con 7 protecciones)
**Procedimiento disponible**: SÍ (sphinx-expert)

---

## CATEGORÍA 6: Lexers Desconocidos - WARNING

**Issues**: 8 WARNING
- Pygments lexer name 'PlantUML' is not known: 8

**Archivos afectados**: ~3

**Complejidad**: TRIVIAL
- Cambiar 'PlantUML' → 'text' o instalar lexer
- O configurar en conf.py
- No afecta contenido

**Riesgo automatización**: BAJO
- Patrón único
- Fácil de reemplazar
- Validación simple

**Estrategia**: SCRIPT TRIVIAL (o config)
**Procedimiento disponible**: SÍ (sphinx-expert)

---

## CATEGORÍA 7: Markup Incompleto - WARNING

**Issues**: 5 WARNING
- Inline strong start-string without end-string: 3
- Inline emphasis start-string without end-string: 2

**Archivos afectados**: ~3-5

**Complejidad**: MODERADO
- Requiere encontrar dónde cerrar markup
- Puede ser error tipográfico
- Requiere leer contexto

**Riesgo automatización**: MEDIO
- Contexto necesario
- No siempre claro dónde cerrar

**Estrategia**: MANUAL
**Procedimiento disponible**: NO

---

## CATEGORÍA 8: Referencias - WARNING

**Issues**: 2 WARNING
- Footnote not referenced: 2

**Archivos afectados**: ~2

**Complejidad**: TRIVIAL
- Eliminar footnote o agregar referencia

**Riesgo automatización**: BAJO

**Estrategia**: MANUAL RÁPIDO

---

## CATEGORÍA 9: Glossary Terms - WARNING

**Issues**: ~5 WARNING
- term not in glossary: varios términos

**Archivos afectados**: ~3

**Complejidad**: MODERADO
- Agregar términos al glosario
- O cambiar referencias

**Riesgo automatización**: MEDIO

**Estrategia**: MANUAL

---

## CATEGORÍA 10: Otros - ERROR + WARNING

**Issues**: ~23 restantes
- Unknown target name: 1
- Unexpected indentation: 1
- Content block expected for note: 1
- Toctree glob pattern: 1
- Otros: ~19

**Complejidad**: VARIABLE

**Estrategia**: EVALUAR CASO POR CASO

---

## RESUMEN DE CATEGORIZACIÓN

| Categoría | Issues | Complejidad | Riesgo Auto | Estrategia |
|-----------|--------|-------------|-------------|------------|
| 1. Section Structure (CRITICAL) | 31 | COMPLEJO | ALTO | Manual puro |
| 2. List-Tables (ERROR) | 8 | COMPLEJO | ALTO | Manual puro |
| 3. Transitions (ERROR) | 6 | TRIVIAL | BAJO | Manual rápido |
| 4. Headers (WARNING) | 309 | MODERADO | MEDIO-ALTO | Manual selectivo |
| 5. Blank Lines (WARNING) | 259 | MODERADO | BAJO | Script seguro |
| 6. Lexers (WARNING) | 8 | TRIVIAL | BAJO | Script trivial |
| 7. Markup (WARNING) | 5 | MODERADO | MEDIO | Manual |
| 8. Referencias (WARNING) | 2 | TRIVIAL | BAJO | Manual rápido |
| 9. Glossary (WARNING) | 5 | MODERADO | MEDIO | Manual |
| 10. Otros | 23 | VARIABLE | VARIABLE | Caso x caso |

**Total categorizado**: 656/661 (99%)

---

## OUTPUT FASE 2

✅ 10 categorías identificadas
✅ Complejidad asignada a cada una
✅ Riesgo de automatización evaluado
✅ Estrategia recomendada por categoría
✅ Procedimientos disponibles identificados

**Listo para FASE 3: Priorización**
