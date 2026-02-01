# Listado Completo de WARNING - Build Log

**Fecha Build**: 2026-01-31 16:49:40  
**Build Log**: build-log-20260131-164940.log  
**Total WARNING**: 613

---

## 📊 RESUMEN POR TIPO

- **Document headings start at H3, not H1 [myst.header]**: 139 issues
- **Document headings start at H2, not H1 [myst.header]**: 132 issues
- **Block quote ends without a blank line; unexpected unindent. [docutils]**: 87 issues
- **Enumerated list ends without a blank line; unexpected unindent. [docutils]**: 84 issues
- **Explicit markup ends without a blank line; unexpected unindent. [docutils]**: 70 issues
- **Document headings start at H4, not H1 [myst.header]**: 23 issues
- **term not in glossary**: 17 issues
- **Non-consecutive header level increase; H2 to H4 [myst.header]**: 13 issues
- **Bullet list ends without a blank line; unexpected unindent. [docutils]**: 11 issues
- **Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]**: 8 issues
- **Field list ends without a blank line; unexpected unindent. [docutils]**: 4 issues
- **Line block ends without a blank line. [docutils]**: 3 issues
- **Inline strong start-string without end-string. [docutils]**: 3 issues
- **Title underline too short.**: 2 issues
- **Lexing literal_block '{\n"section"**: 2 issues
- **Inline emphasis start-string without end-string. [docutils]**: 2 issues
- **Footnote [#] is not referenced. [ref.footnote]**: 2 issues
- **toctree glob pattern 'traduccion/decision_ejemplo_*' didn't match any documents**: 1 issues
- **duplicate term description of Stakeholder, other instance in biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/glosario_seccion_01**: 1 issues
- **duplicate term description of Markdown, other instance in 01_fundamentos/glosario_traduccion**: 1 issues
- **duplicate label metadata-estado-traduccion, other instance in E**: 1 issues
- **Pygments lexer name 'plantuml' is not known [misc.highlighting_failure]**: 1 issues
- **Lexing literal_block '{\n"verificacion_traducciones"**: 1 issues
- **Lexing literal_block '.PHONY**: 1 issues
- **Lexing literal_block '# Analog�a en ATL\nrule DefaultVerbTranslation {\n    from\n        h **: 1 issues
- **Inline literal start-string without end-string. [docutils]**: 1 issues
- **Footnote [2] is not referenced. [ref.footnote]**: 1 issues
- **Footnote [1] is not referenced. [ref.footnote]**: 1 issues

---

## 📊 RESUMEN POR ARCHIVO (Top 30)

| Archivo | Issues |
|---------|--------|
| `source/02_procedimientos/workflow_general.rst` | 59 |
| `source/docs_maestros/GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst` | 29 |
| `source/02_procedimientos/WORKFLOW_v1_6_0_ACTUALIZACION.rst` | 17 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/metadata_libro.rst` | 16 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-1.md.rst` | 13 |
| `source/06_casos_practicos/errores_comunes/error_01_omisiones.rst` | 12 |
| `source/07_guias_uso/guia_rapida.rst` | 11 |
| `source/01_fundamentos/principios_fundamentales.rst` | 10 |
| `source/docs_maestros/SINTESIS_METODOLOGICA_ADT.rst` | 9 |
| `source/docs_maestros/PROMPT_MAESTRO_SPHINX_TRADUCCION.md.rst` | 9 |
| `source/docs_maestros/PLAN_CONTENIDO.rst` | 9 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/notas_traduccion_seccion_01.rst` | 9 |
| `source/07_guias_uso/troubleshooting.rst` | 9 |
| `source/07_guias_uso/tutorial_completo.rst` | 8 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-5.md.rst` | 7 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-3.md.rst` | 7 |
| `source/01_fundamentos/metamodelos/framework_universal_transformacion.rst` | 7 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/original/section-8.md.rst` | 6 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-8.md.rst` | 6 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/imprint-privacy.md.rst` | 6 |
| `source/09_referencias/cheatsheets/cheatsheet_rst.rst` | 6 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/11_risks_tech_debt/traduccion/risks_tip_1.rst` | 5 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/original/section-9.md.rst` | 5 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-3.rst` | 5 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-9.md.rst` | 5 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/traduccion/seccion_5_3_nivel_3.rst` | 4 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/traduccion/seccion_5_2_nivel_2.rst` | 4 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-5.rst` | 4 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-4.rst` | 4 |
| `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/traduccion/seccion_1_1_requisitos.rst` | 4 |

---

## 🟡 LISTADO COMPLETO DE LOS 613 WARNING

### 1. `source/01_fundamentos/_fundamentos_conceptuales/signifiant_vs_signifie.rst`

**WARNING #1** - Línea 308:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #2** - Línea 311:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 2. `source/01_fundamentos/_metodologias/metodo_por_defecto.rst`

**WARNING #3** - Línea 148:
- **Mensaje**: Inline literal start-string without end-string. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #4** - Línea 426:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #5** - Línea 461:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 3. `source/01_fundamentos/glosario_traduccion.rst`

**WARNING #6** - Línea 336:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #7** - Línea 349:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 4. `source/01_fundamentos/metamodelos/framework_universal_transformacion.rst`

**WARNING #8** - Línea 122:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #9** - Línea 125:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #10** - Línea 128:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #11** - Línea 168:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #12** - Línea 171:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #13** - Línea 174:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #14** - Línea 177:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 5. `source/01_fundamentos/principios_fundamentales.rst`

**WARNING #15** - Línea 379:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #16** - Línea 382:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #17** - Línea 385:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #18** - Línea 388:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #19** - Línea 391:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #20** - Línea 394:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #21** - Línea 397:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #22** - Línea 400:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #23** - Línea 403:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #24** - Línea 406:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 6. `source/02_procedimientos/WORKFLOW_ACTUALIZACION_v1_5_0.rst`

**WARNING #25** - Línea 53:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #26** - Línea 57:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #27** - Línea 61:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 7. `source/02_procedimientos/WORKFLOW_v1_6_0_ACTUALIZACION.rst`

**WARNING #28** - Línea 323:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #29** - Línea 337:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #30** - Línea 352:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #31** - Línea 355:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #32** - Línea 363:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #33** - Línea 371:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #34** - Línea 379:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #35** - Línea 388:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #36** - Línea 398:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #37** - Línea 444:
- **Mensaje**: Lexing literal_block '{/n"section": {/n"number": "XX",/n"title_en": "[T�tulo en ingl�s]",/n"title_es": "[T�tulo en espa�ol]",/n"arc42_template": "section-X",/n"status": "complete",/n"completion_percentage": 100,/n"translation_date": "YYYY-MM-DD",/n"workflow_version": "v1.X.X"/n},/n/n"translation": {/n"method": "Peshitta + ADT Workflow v1.X.X",/n"source_language": "English",/n"target_language": "Spanish",/n"source_format": "Markdown",/n"target_format": "reStructuredText",/n"architectural_terminology_applied": true,/n"step_3_4_applied": true/n},/n/n"files": {/n"total": XX,/n"subsections": X,/n"examples": X,/n"tips": X,/n"breakdown": {/n"subsections": [/n{/n"number": "X.1",/n"title_en": "[T�tulo]",/n"title_es": "[T�tulo]",/n"filename": "seccion_X_1.rst",/n"workflow": "v1.X.X",/n"lines": XXX,/n"key_terminology": {/n"term_en": "traducci�n_es"/n}/n}/n],/n"examples": [...],/n"tips": [...]/n}/n},/n/n"terminology": {/n"architectural_terms": {/n"term_1": {/n"translation": "traducci�n correcta",/n"incorrect_literal": "traducci�n literal incorrecta",/n"rationale": "Raz�n para la traducci�n",/n"occurrences": XX,/n"consistency": "100%"/n}/n},/n"overall_consistency": "100%"/n},/n/n"statistics": {/n"lines": {/n"original_approximate": XXX,/n"translated_approximate": XXX,/n"expansion_ratio": X.XX/n},/n"elements": {/n"figures": XX,/n"tables": XX,/n"code_blocks": XX,/n"external_links": XX/n}/n},/n/n"workflow_validation": {/n"hypothesis": "[Hip�tesis si aplica]",/n"results": {/n"corrections_reduction": "X%",/n"time_reduction": "X%",/n"quality": "perfect/good/acceptable"/n},/n"conclusion": "[Conclusi�n]"/n},/n/n"quality_assurance": {/n"architectural_terminology_verified": true,/n"step_3_4_applied_from_start": true,/n"consistency_check_passed": true,/n"all_links_functional": true,/n"all_figures_converted": true,/n"metadata_complete": true/n},/n/n"next_steps": {/n"immediate": [/n"Compile with Sphinx",/n"Verify HTML output"/n],/n"medium_term": [/n"Apply to next section"/n]/n},/n/n"references": {/n"original_docs": "https://...",/n"standards": ["ISO XXX", "IEEE XXX"]/n},/n/n"license": {/n"original": "CC BY-SA 4.0",/n"translation": "CC BY-SA 4.0"/n},/n/n"metadata": {/n"created": "YYYY-MM-DD",/n"last_updated": "YYYY-MM-DD",/n"version": "1.0.0",/n"status": "complete"/n}/n}' as "json" resulted in an error at token: 'X'. Retrying in relaxed mode. [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

**WARNING #38** - Línea 607:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #39** - Línea 610:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #40** - Línea 617:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #41** - Línea 620:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #42** - Línea 626:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #43** - Línea 629:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #44** - Línea 634:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 8. `source/02_procedimientos/workflow_general.rst`

**WARNING #45** - Línea 1104:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #46** - Línea 1194:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #47** - Línea 1199:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #48** - Línea 1222:
- **Mensaje**: Line block ends without a blank line. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #49** - Línea 1227:
- **Mensaje**: Line block ends without a blank line. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #50** - Línea 1232:
- **Mensaje**: Line block ends without a blank line. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #51** - Línea 123:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #52** - Línea 1363:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #53** - Línea 1937:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #54** - Línea 1972:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #55** - Línea 2243:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #56** - Línea 2253:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #57** - Línea 2288:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #58** - Línea 2291:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #59** - Línea 2364:
- **Mensaje**: Lexing literal_block '{/n"verificacion_traducciones": {/n"total_originales": 13,/n"total_traducciones": 13,/n"traducciones_faltantes": [],/n"comparaciones": [...],/n"estadisticas_completitud": {/n"completas": 0,/n"incompletas": 13,/n"similitud_promedio": "0.79%"/n}/n}/n}' as "json" resulted in an error at token: '.'. Retrying in relaxed mode. [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

**WARNING #60** - Línea 2452:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #61** - Línea 2457:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #62** - Línea 2462:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #63** - Línea 2466:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #64** - Línea 2470:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #65** - Línea 3045:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #66** - Línea 3056:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #67** - Línea 3064:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #68** - Línea 3086:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #69** - Línea 3103:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #70** - Línea 3117:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #71** - Línea 3132:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #72** - Línea 3135:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #73** - Línea 3143:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #74** - Línea 3151:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #75** - Línea 3159:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #76** - Línea 3168:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #77** - Línea 3178:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #78** - Línea 3224:
- **Mensaje**: Lexing literal_block '{/n"section": {/n"number": "XX",/n"title_en": "[T�tulo en ingl�s]",/n"title_es": "[T�tulo en espa�ol]",/n"arc42_template": "section-X",/n"status": "complete",/n"completion_percentage": 100,/n"translation_date": "YYYY-MM-DD",/n"workflow_version": "v1.X.X"/n},/n/n"translation": {/n"method": "Peshitta + ADT Workflow v1.X.X",/n"source_language": "English",/n"target_language": "Spanish",/n"source_format": "Markdown",/n"target_format": "reStructuredText",/n"architectural_terminology_applied": true,/n"step_3_4_applied": true/n},/n/n"files": {/n"total": XX,/n"subsections": X,/n"examples": X,/n"tips": X,/n"breakdown": {/n"subsections": [/n{/n"number": "X.1",/n"title_en": "[T�tulo]",/n"title_es": "[T�tulo]",/n"filename": "seccion_X_1.rst",/n"workflow": "v1.X.X",/n"lines": XXX,/n"key_terminology": {/n"term_en": "traducci�n_es"/n}/n}/n],/n"examples": [...],/n"tips": [...]/n}/n},/n/n"terminology": {/n"architectural_terms": {/n"term_1": {/n"translation": "traducci�n correcta",/n"incorrect_literal": "traducci�n literal incorrecta",/n"rationale": "Raz�n para la traducci�n",/n"occurrences": XX,/n"consistency": "100%"/n}/n},/n"overall_consistency": "100%"/n},/n/n"statistics": {/n"lines": {/n"original_approximate": XXX,/n"translated_approximate": XXX,/n"expansion_ratio": X.XX/n},/n"elements": {/n"figures": XX,/n"tables": XX,/n"code_blocks": XX,/n"external_links": XX/n}/n},/n/n"quality_assurance": {/n"architectural_terminology_verified": true,/n"step_3_4_applied_from_start": true,/n"consistency_check_passed": true,/n"all_links_functional": true,/n"all_figures_converted": true,/n"metadata_complete": true/n},/n/n"next_steps": {/n"immediate": [/n"Compile with Sphinx",/n"Verify HTML output"/n],/n"medium_term": [/n"Apply to next section"/n]/n},/n/n"references": {/n"original_docs": "https://...",/n"standards": ["ISO XXX", "IEEE XXX"]/n},/n/n"license": {/n"original": "CC BY-SA 4.0",/n"translation": "CC BY-SA 4.0"/n},/n/n"metadata": {/n"created": "YYYY-MM-DD",/n"last_updated": "YYYY-MM-DD",/n"version": "1.0.0",/n"status": "complete"/n}/n}' as "json" resulted in an error at token: 'X'. Retrying in relaxed mode. [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

**WARNING #79** - Línea 3380:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #80** - Línea 3383:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #81** - Línea 3390:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #82** - Línea 3393:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #83** - Línea 3399:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #84** - Línea 3402:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #85** - Línea 3641:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #86** - Línea 4029:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #87** - Línea 4033:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #88** - Línea 4037:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #89** - Línea 4398:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #90** - Línea 4401:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #91** - Línea 4423:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #92** - Línea 4425:
- **Mensaje**: Footnote [#] is not referenced. [ref.footnote]
- **Solución**: Ver mensaje específico

**WARNING #93** - Línea 4426:
- **Mensaje**: Footnote [#] is not referenced. [ref.footnote]
- **Solución**: Ver mensaje específico

**WARNING #94** - Línea 458:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #95** - Línea 463:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #96** - Línea 4665:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #97** - Línea 4773:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #98** - Línea 491:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #99** - Línea 496:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #100** - Línea 580:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #101** - Línea 763:
- **Mensaje**: Inline emphasis start-string without end-string. [docutils]
- **Solución**: Cerrar énfasis correctamente (*texto* o **texto**)

**WARNING #102** - Línea 766:
- **Mensaje**: Inline emphasis start-string without end-string. [docutils]
- **Solución**: Cerrar énfasis correctamente (*texto* o **texto**)

**WARNING #103** - Línea 789:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 9. `source/03_estandares/calidad/checklist_revision.rst`

**WARNING #104** - Línea 401:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #105** - Línea 445:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #106** - Línea 450:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #107** - Línea 80:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 10. `source/03_estandares/calidad/criterios_calidad.rst`

**WARNING #108** - Línea 145:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #109** - Línea 396:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #110** - Línea 404:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 11. `source/03_estandares/calidad/metricas_traduccion.rst`

**WARNING #111** - Línea 651:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 12. `source/04_reglas_operativas/matrices_decision/MD_001_modo_1_vs_modo_2.rst`

**WARNING #112** - Línea 123:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 13. `source/04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer.rst`

**WARNING #113** - Línea 286:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 14. `source/04_reglas_operativas/matrices_decision/MD_004_traducir_vs_conservar.rst`

**WARNING #114** - Línea 844:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #115** - Línea 864:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #116** - Línea 870:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #117** - Línea 876:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 15. `source/05_herramientas_medios/equivalencias/latex_rst_equivalencias.rst`

**WARNING #118** - Línea 426:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #119** - Línea 429:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #120** - Línea 432:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #121** - Línea 435:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 16. `source/05_herramientas_medios/sphinx/scripts_verificacion.rst`

**WARNING #122** - Línea 528:
- **Mensaje**: Lexing literal_block '.PHONY: verificar verificar-lote/n/nverificar:/n@echo "Verificando traducci�n..."/n@./scripts/verificar_traduccion.sh $(ORIG) $(TRAD)/n/nverificar-lote:/n@echo "Verificando lote completo..."/n@./scripts/verificar_lote.sh $(ORIG_DIR) $(TRAD_DIR)' as "makefile" resulted in an error at token: '@'. Retrying in relaxed mode. [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 17. `source/06_casos_practicos/antes_despues/caso_01_seccion_breve.rst`

**WARNING #123** - Línea 285:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 18. `source/06_casos_practicos/errores_comunes/error_01_omisiones.rst`

**WARNING #124** - Línea 152:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #125** - Línea 171:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #126** - Línea 172:
- **Mensaje**: Field list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #127** - Línea 175:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #128** - Línea 176:
- **Mensaje**: Field list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #129** - Línea 250:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #130** - Línea 253:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #131** - Línea 429:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #132** - Línea 496:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #133** - Línea 497:
- **Mensaje**: Field list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #134** - Línea 500:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #135** - Línea 501:
- **Mensaje**: Field list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 19. `source/07_guias_uso/faq.rst`

**WARNING #136** - Línea 411:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #137** - Línea 416:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #138** - Línea 420:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 20. `source/07_guias_uso/guia_rapida.rst`

**WARNING #139** - Línea 260:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #140** - Línea 292:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #141** - Línea 298:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #142** - Línea 316:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #143** - Línea 318:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #144** - Línea 329:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #145** - Línea 350:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #146** - Línea 360:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #147** - Línea 51:
- **Mensaje**: Inline strong start-string without end-string. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #148** - Línea 51:
- **Mensaje**: Inline strong start-string without end-string. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #149** - Línea 51:
- **Mensaje**: Inline strong start-string without end-string. [docutils]
- **Solución**: Ver mensaje específico

---

### 21. `source/07_guias_uso/troubleshooting.rst`

**WARNING #150** - Línea 178:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #151** - Línea 426:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #152** - Línea 429:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #153** - Línea 434:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #154** - Línea 439:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #155** - Línea 444:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #156** - Línea 454:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #157** - Línea 45:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #158** - Línea 55:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 22. `source/07_guias_uso/tutorial_completo.rst`

**WARNING #159** - Línea 1000:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #160** - Línea 1003:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #161** - Línea 1006:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #162** - Línea 1009:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #163** - Línea 1123:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #164** - Línea 125:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #165** - Línea 389:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #166** - Línea 526:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 23. `source/08_prompts/index.rst`

**WARNING #167** - Línea 328:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #168** - Línea 332:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #169** - Línea 336:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #170** - Línea 340:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 24. `source/09_referencias/cheatsheets/cheatsheet_rst.rst`

**WARNING #171** - Línea 154:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #172** - Línea 650:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #173** - Línea 655:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #174** - Línea 657:
- **Mensaje**: Footnote [1] is not referenced. [ref.footnote]
- **Solución**: Ver mensaje específico

**WARNING #175** - Línea 658:
- **Mensaje**: Footnote [2] is not referenced. [ref.footnote]
- **Solución**: Ver mensaje específico

**WARNING #176** - Línea 668:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 25. `source/biblioteca/_metadata_biblioteca/META_BIB_003_Esquema_Codificacion_1_0_0.rst`

**WARNING #177** - Línea 515:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 26. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/metadata_libro.rst`

**WARNING #178** - Línea 116:
- **Mensaje**: duplicate label metadata-estado-traduccion, other instance in E:/Proyectos/Translate/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/index.rst
- **Solución**: Usar etiquetas únicas o renombrar secciones

**WARNING #179** - Línea 192:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #180** - Línea 195:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #181** - Línea 198:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #182** - Línea 201:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #183** - Línea 204:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #184** - Línea 207:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #185** - Línea 210:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #186** - Línea 213:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #187** - Línea 217:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #188** - Línea 220:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #189** - Línea 223:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #190** - Línea 226:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #191** - Línea 235:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #192** - Línea 245:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #193** - Línea 268:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 27. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/01-overview-example-3.md.rst`

**WARNING #194** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #195** - Línea 29:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 28. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/01-overview-example-htmlsc-1.md.rst`

**WARNING #196** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 29. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/01-quality-reqs-example-1.md.rst`

**WARNING #197** - Línea 15:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 30. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/01-quality-reqs-example-3.md.rst`

**WARNING #198** - Línea 15:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 31. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/02-constraint-example-1.md.rst`

**WARNING #199** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 32. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/03-context-example-business-1.md.rst`

**WARNING #200** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 33. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/03-context-example-business-2.md.rst`

**WARNING #201** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 34. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/03-context-example-business-3.md.rst`

**WARNING #202** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 35. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/03-context-example-business-4.md.rst`

**WARNING #203** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 36. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/03-context-example-technical-1.md.rst`

**WARNING #204** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 37. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/03-context-example-technical-4.md.rst`

**WARNING #205** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 38. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/04-solutionStrategy-example-htmlsc-1.md.rst`

**WARNING #206** - Línea 20:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 39. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/04-solutionStrategy-example-mama-2.md.rst`

**WARNING #207** - Línea 17:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 40. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/05-buildingblock-example-hsc.md.rst`

**WARNING #208** - Línea 106:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #209** - Línea 16:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #210** - Línea 44:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 41. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/05-buildingblock-example-status.md.rst`

**WARNING #211** - Línea 16:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 42. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/05-buildingblock-example-tpu-lev-1.md.rst`

**WARNING #212** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 43. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/05-buildingblock-example-tpu-lev-2.md.rst`

**WARNING #213** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 44. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/06-runtime-example-htmlsc-1.md.rst`

**WARNING #214** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 45. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/06-runtime-example-mama-2.md.rst`

**WARNING #215** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 46. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/06-runtime-example-tpu-1.md.rst`

**WARNING #216** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #217** - Línea 17:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 47. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/07-deployment-example-tpu-1.md.rst`

**WARNING #218** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #219** - Línea 22:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 48. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/07-deployment-sample-htmlsc-1.md.rst`

**WARNING #220** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 49. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/07-deployment-sample-tpu-2.md.rst`

**WARNING #221** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 50. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/08-concept-example-htmlsc-1.md.rst`

**WARNING #222** - Línea 11:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 51. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/08-concept-example-htmlsc-2.md.rst`

**WARNING #223** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 52. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/08-concept-example-tpu-1.md.rst`

**WARNING #224** - Línea 11:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 53. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/08-concept-example-tpu-2.md.rst`

**WARNING #225** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 54. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/09-decision-example-htmlsc-1.md.rst`

**WARNING #226** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 55. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/09-decision-example-tpu-2.md.rst`

**WARNING #227** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 56. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/10-quality-scenario-example-htmlsc-2.md.rst`

**WARNING #228** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 57. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/10-quality-scenario-example-tpu-1.md.rst`

**WARNING #229** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 58. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/11-risk-example-htmlsc.md.rst`

**WARNING #230** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 59. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/11-risk-example-tpu.md.rst`

**WARNING #231** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 60. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_examples/12-glossary-example-htmlsc-1.md.rst`

**WARNING #232** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 61. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_includes/example.md.rst`

**WARNING #233** - Línea 2:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 62. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_includes/further-info.md.rst`

**WARNING #234** - Línea 19:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #235** - Línea 5:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 63. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/contact.md.rst`

**WARNING #236** - Línea 24:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #237** - Línea 8:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 64. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/examples.md.rst`

**WARNING #238** - Línea 8:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 65. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/imprint-privacy.md.rst`

**WARNING #239** - Línea 13:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #240** - Línea 15:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #241** - Línea 19:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #242** - Línea 25:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #243** - Línea 29:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #244** - Línea 32:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 66. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-1.md.rst`

**WARNING #245** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #246** - Línea 25:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #247** - Línea 28:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #248** - Línea 31:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #249** - Línea 47:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #250** - Línea 51:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #251** - Línea 58:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #252** - Línea 62:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #253** - Línea 75:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #254** - Línea 79:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #255** - Línea 88:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #256** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #257** - Línea 91:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 67. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-11.md.rst`

**WARNING #258** - Línea 11:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #259** - Línea 14:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #260** - Línea 20:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #261** - Línea 7:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 68. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-12.md.rst`

**WARNING #262** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #263** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #264** - Línea 23:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #265** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 69. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-2.md.rst`

**WARNING #266** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #267** - Línea 18:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #268** - Línea 22:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #269** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 70. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-3.md.rst`

**WARNING #270** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #271** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #272** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #273** - Línea 25:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #274** - Línea 31:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #275** - Línea 57:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #276** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 71. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-4.md.rst`

**WARNING #277** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #278** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #279** - Línea 24:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #280** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 72. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-5.md.rst`

**WARNING #281** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #282** - Línea 145:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #283** - Línea 171:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #284** - Línea 20:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #285** - Línea 25:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #286** - Línea 40:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #287** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 73. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-6.md.rst`

**WARNING #288** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #289** - Línea 23:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #290** - Línea 27:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #291** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 74. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-7.md.rst`

**WARNING #292** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #293** - Línea 32:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #294** - Línea 37:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #295** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 75. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-8.md.rst`

**WARNING #296** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #297** - Línea 20:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #298** - Línea 28:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #299** - Línea 36:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #300** - Línea 41:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #301** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 76. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_pages/section-9.md.rst`

**WARNING #302** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #303** - Línea 18:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #304** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #305** - Línea 27:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #306** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 77. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/01-requirements/2016-03-01-t-1-9.md`

**WARNING #307** - Línea 16:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 78. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/01-requirements/2016-03-02-t-1-12.md.rst`

**WARNING #308** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 79. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/01-requirements/2016-03-02-t-1-21.md.rst`

**WARNING #309** - Línea 13:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #310** - Línea 25:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 80. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/03-context/2016-03-01-t-3-9.md.rst`

**WARNING #311** - Línea 13:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #312** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #313** - Línea 9:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 81. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-01-t-5-1.md.rst`

**WARNING #314** - Línea 20:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #315** - Línea 27:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 82. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-01-t-5-3.md.rst`

**WARNING #316** - Línea 12:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 83. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-01-t-5-6.md.rst`

**WARNING #317** - Línea 26:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 84. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-01-t-5-7.md.rst`

**WARNING #318** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #319** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #320** - Línea 27:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 85. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-02-t-5-10.md.rst`

**WARNING #321** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #322** - Línea 22:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #323** - Línea 38:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 86. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-02-t-5-11.md.rst`

**WARNING #324** - Línea 23:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 87. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-02-t-5-13.md.rst`

**WARNING #325** - Línea 29:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #326** - Línea 45:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #327** - Línea 53:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 88. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-02-t-5-16.md.rst`

**WARNING #328** - Línea 16:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 89. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-02-t-5-17.md.rst`

**WARNING #329** - Línea 17:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #330** - Línea 25:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #331** - Línea 9:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 90. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-02-t-5-19.md.rst`

**WARNING #332** - Línea 28:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 91. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-03-t-5-20.md.rst`

**WARNING #333** - Línea 23:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 92. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-03-t-5-21.md.rst`

**WARNING #334** - Línea 37:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 93. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-03-t-5-22.md.rst`

**WARNING #335** - Línea 31:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #336** - Línea 52:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 94. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-03-t-5-24.md.rst`

**WARNING #337** - Línea 27:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 95. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-03-t-5-26.md.rst`

**WARNING #338** - Línea 19:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #339** - Línea 24:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 96. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/05-buildingblocks/2016-03-03-t-5-28.md.rst`

**WARNING #340** - Línea 20:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #341** - Línea 24:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 97. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-2.md.rst`

**WARNING #342** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #343** - Línea 38:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #344** - Línea 9:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 98. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-4.md.rst`

**WARNING #345** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 99. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-5.md`

**WARNING #346** - Línea 25:
- **Mensaje**: Pygments lexer name 'plantuml' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 100. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-5.md.rst`

**WARNING #347** - Línea 19:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 101. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-6.md`

**WARNING #348** - Línea 33:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 102. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-6.md.rst`

**WARNING #349** - Línea 16:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 103. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-7.md`

**WARNING #350** - Línea 24:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 104. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-7.md.rst`

**WARNING #351** - Línea 43:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 105. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-8.md`

**WARNING #352** - Línea 16:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 106. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-9.md`

**WARNING #353** - Línea 15:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 107. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-01-t-6-9.md.rst`

**WARNING #354** - Línea 53:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 108. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-02-t-6-10.md.rst`

**WARNING #355** - Línea 19:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 109. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-02-t-6-11.md`

**WARNING #356** - Línea 32:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 110. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/06-runtime/2016-03-02-t-6-11.md.rst`

**WARNING #357** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #358** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #359** - Línea 49:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 111. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/07-deployment/2016-03-01-t-7-1.md.rst`

**WARNING #360** - Línea 23:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 112. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/07-deployment/2016-03-01-t-7-2.md.rst`

**WARNING #361** - Línea 16:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 113. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/07-deployment/2016-03-01-t-7-9.md.rst`

**WARNING #362** - Línea 39:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #363** - Línea 9:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 114. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/08-concepts/2016-03-01-t-8-4.md.rst`

**WARNING #364** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 115. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/08-concepts/2016-03-01-t-8-5.md.rst`

**WARNING #365** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #366** - Línea 9:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 116. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/08-concepts/2016-03-01-t-8-7.md`

**WARNING #367** - Línea 29:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 117. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/08-concepts/2016-03-01-t-8-7.md.rst`

**WARNING #368** - Línea 25:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 118. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/08-concepts/2016-03-01-t-8-8.md.rst`

**WARNING #369** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #370** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #371** - Línea 30:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 119. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/08-concepts/2022-07-01-t-8-11.md.rst`

**WARNING #372** - Línea 13:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #373** - Línea 25:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #374** - Línea 35:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 120. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/09-decisions/2016-03-01-t-9-2.md.rst`

**WARNING #375** - Línea 20:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #376** - Línea 30:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #377** - Línea 40:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 121. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/09-decisions/2016-03-01-t-9-5.md.rst`

**WARNING #378** - Línea 24:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 122. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/10-quality/2016-03-01-t-10-2.md.rst`

**WARNING #379** - Línea 33:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 123. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/11-risks/2016-03-01-t-11-1.md.rst`

**WARNING #380** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 124. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/_posts/11-risks/2016-03-01-t-11-2.md.rst`

**WARNING #381** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 125. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/glosario_seccion_01.rst`

**WARNING #382** - Línea 66:
- **Mensaje**: duplicate term description of Markdown, other instance in 01_fundamentos/glosario_traduccion
- **Solución**: Ver mensaje específico

---

### 126. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/notas_traduccion_seccion_01.rst`

**WARNING #383** - Línea 106:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #384** - Línea 120:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #385** - Línea 299:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #386** - Línea 302:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #387** - Línea 305:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #388** - Línea 308:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #389** - Línea 69:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #390** - Línea 82:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #391** - Línea 94:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 127. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/01-overview-example-3.md.rst`

**WARNING #392** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #393** - Línea 29:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 128. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/01-overview-example-htmlsc-1.md.rst`

**WARNING #394** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 129. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/01-quality-reqs-example-1.md.rst`

**WARNING #395** - Línea 15:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 130. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/01-quality-reqs-example-3.md.rst`

**WARNING #396** - Línea 15:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 131. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/2016-03-01-t-1-9.md`

**WARNING #397** - Línea 16:
- **Mensaje**: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 132. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/2016-03-02-t-1-12.md.rst`

**WARNING #398** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 133. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/original/2016-03-02-t-1-21.md.rst`

**WARNING #399** - Línea 13:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #400** - Línea 25:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 134. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/traduccion/seccion_1_1_requisitos.rst`

**WARNING #401** - Línea 64:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #402** - Línea 69:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #403** - Línea 76:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #404** - Línea 82:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 135. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/glosario_seccion.rst`

**WARNING #405** - Línea 44:
- **Mensaje**: duplicate term description of Stakeholder, other instance in biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/glosario_seccion_01
- **Solución**: Ver mensaje específico

---

### 136. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/original/02-constraint-example-1.md.rst`

**WARNING #406** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 137. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_ejemplo-1.rst`

**WARNING #407** - Línea 36:
- **Mensaje**: term not in glossary: 'Platform-independent' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #408** - Línea 38:
- **Mensaje**: term not in glossary: 'Command Line' [ref.term]
- **Solución**: Ver mensaje específico

---

### 138. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-2.rst`

**WARNING #409** - Línea 23:
- **Mensaje**: term not in glossary: 'Consequences' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #410** - Línea 25:
- **Mensaje**: term not in glossary: 'Unreasonable' [ref.term]
- **Solución**: Ver mensaje específico

---

### 139. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-3.rst`

**WARNING #411** - Línea 27:
- **Mensaje**: term not in glossary: 'Freedom of Design' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #412** - Línea 28:
- **Mensaje**: term not in glossary: 'Development Process' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #413** - Línea 29:
- **Mensaje**: term not in glossary: 'Third Party Contracting' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #414** - Línea 30:
- **Mensaje**: term not in glossary: 'Legal Concerns' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #415** - Línea 31:
- **Mensaje**: term not in glossary: 'Management' [ref.term]
- **Solución**: Ver mensaje específico

---

### 140. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-4.rst`

**WARNING #416** - Línea 28:
- **Mensaje**: term not in glossary: 'Design Decision' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #417** - Línea 29:
- **Mensaje**: term not in glossary: 'Implementation Decision' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #418** - Línea 31:
- **Mensaje**: term not in glossary: 'Reference Architecture' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #419** - Línea 32:
- **Mensaje**: term not in glossary: 'Development Team' [ref.term]
- **Solución**: Ver mensaje específico

---

### 141. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/02_constraints/traduccion/restricciones_tip-5.rst`

**WARNING #420** - Línea 22:
- **Mensaje**: term not in glossary: 'Political Constraints' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #421** - Línea 23:
- **Mensaje**: term not in glossary: 'Programming Guidelines' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #422** - Línea 24:
- **Mensaje**: term not in glossary: 'Documentation Conventions' [ref.term]
- **Solución**: Ver mensaje específico

**WARNING #423** - Línea 25:
- **Mensaje**: term not in glossary: 'Naming Conventions' [ref.term]
- **Solución**: Ver mensaje específico

---

### 142. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/03-context-example-business-1.md.rst`

**WARNING #424** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 143. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/03-context-example-business-2.md.rst`

**WARNING #425** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 144. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/03-context-example-business-3.md.rst`

**WARNING #426** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 145. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/03-context-example-business-4.md.rst`

**WARNING #427** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 146. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/03-context-example-technical-1.md.rst`

**WARNING #428** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 147. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/03-context-example-technical-4.md.rst`

**WARNING #429** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 148. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/original/2016-03-01-t-3-9.md.rst`

**WARNING #430** - Línea 13:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #431** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #432** - Línea 9:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 149. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/traduccion/seccion_3_1_contexto_negocio.rst`

**WARNING #433** - Línea 51:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 150. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/03_context_scope/traduccion/seccion_3_2_contexto_tecnico.rst`

**WARNING #434** - Línea 50:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 151. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/04_solution_strategy/original/04-solutionStrategy-example-htmlsc-1.md.rst`

**WARNING #435** - Línea 20:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 152. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/04_solution_strategy/original/04-solutionStrategy-example-mama-2.md.rst`

**WARNING #436** - Línea 17:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 153. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/04_solution_strategy/traduccion/seccion_04_estrategia_solucion.rst`

**WARNING #437** - Línea 68:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 154. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/05-buildingblock-example-hsc.md.rst`

**WARNING #438** - Línea 106:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #439** - Línea 16:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #440** - Línea 44:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 155. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/05-buildingblock-example-status.md.rst`

**WARNING #441** - Línea 16:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 156. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/05-buildingblock-example-tpu-lev-1.md.rst`

**WARNING #442** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 157. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/05-buildingblock-example-tpu-lev-2.md.rst`

**WARNING #443** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 158. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-01-t-5-1.md.rst`

**WARNING #444** - Línea 20:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #445** - Línea 27:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 159. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-01-t-5-3.md.rst`

**WARNING #446** - Línea 12:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 160. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-01-t-5-6.md.rst`

**WARNING #447** - Línea 26:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 161. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-01-t-5-7.md.rst`

**WARNING #448** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #449** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #450** - Línea 27:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 162. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-02-t-5-10.md.rst`

**WARNING #451** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #452** - Línea 22:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #453** - Línea 38:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 163. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-02-t-5-11.md.rst`

**WARNING #454** - Línea 23:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 164. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-02-t-5-13.md.rst`

**WARNING #455** - Línea 29:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #456** - Línea 45:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #457** - Línea 53:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 165. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-02-t-5-16.md.rst`

**WARNING #458** - Línea 16:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 166. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-02-t-5-17.md.rst`

**WARNING #459** - Línea 17:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #460** - Línea 25:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #461** - Línea 9:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 167. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-02-t-5-19.md.rst`

**WARNING #462** - Línea 28:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 168. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-03-t-5-20.md.rst`

**WARNING #463** - Línea 23:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 169. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-03-t-5-21.md.rst`

**WARNING #464** - Línea 37:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 170. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-03-t-5-22.md.rst`

**WARNING #465** - Línea 31:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #466** - Línea 52:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 171. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-03-t-5-24.md.rst`

**WARNING #467** - Línea 27:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 172. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-03-t-5-26.md.rst`

**WARNING #468** - Línea 19:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #469** - Línea 24:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 173. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/original/2016-03-03-t-5-28.md.rst`

**WARNING #470** - Línea 20:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #471** - Línea 24:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 174. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/traduccion/seccion_5_1_whitebox_sistema.rst`

**WARNING #472** - Línea 46:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #473** - Línea 51:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #474** - Línea 56:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 175. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/traduccion/seccion_5_2_nivel_2.rst`

**WARNING #475** - Línea 34:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #476** - Línea 37:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #477** - Línea 47:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #478** - Línea 55:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 176. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/05_building_blocks/traduccion/seccion_5_3_nivel_3.rst`

**WARNING #479** - Línea 34:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #480** - Línea 37:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #481** - Línea 45:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #482** - Línea 51:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 177. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/original/06-runtime-example-htmlsc-1.md.rst`

**WARNING #483** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 178. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/original/06-runtime-example-mama-2.md.rst`

**WARNING #484** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 179. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/original/06-runtime-example-tpu-1.md.rst`

**WARNING #485** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #486** - Línea 17:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 180. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/original/2016-03-01-t-6-2.md.rst`

**WARNING #487** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #488** - Línea 38:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #489** - Línea 9:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 181. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/original/2016-03-01-t-6-4.md.rst`

**WARNING #490** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 182. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/original/2016-03-02-t-6-10.md.rst`

**WARNING #491** - Línea 19:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 183. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/07_deployment_view/original/07-deployment-example-tpu-1.md.rst`

**WARNING #492** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #493** - Línea 22:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 184. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/07_deployment_view/original/07-deployment-sample-htmlsc-1.md.rst`

**WARNING #494** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 185. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/07_deployment_view/original/07-deployment-sample-tpu-2.md.rst`

**WARNING #495** - Línea 15:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 186. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/07_deployment_view/original/2016-03-01-t-7-1.md.rst`

**WARNING #496** - Línea 23:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 187. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/07_deployment_view/original/2016-03-01-t-7-2.md.rst`

**WARNING #497** - Línea 16:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 188. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/07_deployment_view/original/2016-03-01-t-7-9.md.rst`

**WARNING #498** - Línea 39:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #499** - Línea 9:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 189. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/08-concept-example-htmlsc-1.md.rst`

**WARNING #500** - Línea 11:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 190. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/08-concept-example-htmlsc-2.md.rst`

**WARNING #501** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 191. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/08-concept-example-tpu-1.md.rst`

**WARNING #502** - Línea 11:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 192. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/08-concept-example-tpu-2.md.rst`

**WARNING #503** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 193. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/2016-03-01-t-8-4.md.rst`

**WARNING #504** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 194. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/2016-03-01-t-8-5.md.rst`

**WARNING #505** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #506** - Línea 9:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 195. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/2016-03-01-t-8-8.md.rst`

**WARNING #507** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #508** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #509** - Línea 30:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 196. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_concepts/original/2022-07-01-t-8-11.md.rst`

**WARNING #510** - Línea 13:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #511** - Línea 25:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #512** - Línea 35:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 197. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/original/2016-03-01-t-8-4.md.rst`

**WARNING #513** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 198. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/original/2016-03-01-t-8-5.md.rst`

**WARNING #514** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #515** - Línea 9:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 199. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/original/2016-03-01-t-8-8.md.rst`

**WARNING #516** - Línea 17:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #517** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #518** - Línea 30:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 200. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/original/2022-07-01-t-8-11.md.rst`

**WARNING #519** - Línea 13:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #520** - Línea 25:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #521** - Línea 35:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 201. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/original/section-8.md.rst`

**WARNING #522** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #523** - Línea 20:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #524** - Línea 28:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #525** - Línea 36:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #526** - Línea 41:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #527** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 202. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/original/09-decision-example-htmlsc-1.md.rst`

**WARNING #528** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 203. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/original/09-decision-example-tpu-2.md.rst`

**WARNING #529** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 204. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/original/2016-03-01-t-9-2.md.rst`

**WARNING #530** - Línea 20:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #531** - Línea 30:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #532** - Línea 40:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 205. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/original/2016-03-01-t-9-5.md.rst`

**WARNING #533** - Línea 24:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 206. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/original/section-9.md.rst`

**WARNING #534** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #535** - Línea 18:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #536** - Línea 21:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #537** - Línea 27:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #538** - Línea 8:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 207. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/09_architecture_decisions/traduccion/seccion_09_decisiones_arquitectonicas.rst`

**WARNING #539** - Línea 76:
- **Mensaje**: toctree glob pattern 'traduccion/decision_ejemplo_*' didn't match any documents
- **Solución**: Ver mensaje específico

---

### 208. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/original/10-quality-scenario-example-htmlsc-2.md.rst`

**WARNING #540** - Línea 12:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 209. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/original/10-quality-scenario-example-tpu-1.md.rst`

**WARNING #541** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 210. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/original/2016-03-01-t-10-2.md.rst`

**WARNING #542** - Línea 33:
- **Mensaje**: Document headings start at H4, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 211. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/traduccion/quality_ejemplo_tpu_1.rst`

**WARNING #543** - Línea 59:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 212. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/11_risks_tech_debt/original/11-risk-example-htmlsc.md.rst`

**WARNING #544** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 213. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/11_risks_tech_debt/original/11-risk-example-tpu.md.rst`

**WARNING #545** - Línea 12:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 214. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/11_risks_tech_debt/original/2016-03-01-t-11-1.md.rst`

**WARNING #546** - Línea 18:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 215. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/11_risks_tech_debt/original/2016-03-01-t-11-2.md.rst`

**WARNING #547** - Línea 14:
- **Mensaje**: Document headings start at H2, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 216. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/11_risks_tech_debt/traduccion/risks_tip_1.rst`

**WARNING #548** - Línea 74:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #549** - Línea 78:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #550** - Línea 83:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #551** - Línea 87:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #552** - Línea 91:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 217. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/original/12-glossary-example-htmlsc-1.md.rst`

**WARNING #553** - Línea 13:
- **Mensaje**: Document headings start at H3, not H1 [myst.header]
- **Solución**: Ver mensaje específico

---

### 218. `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_4.rst`

**WARNING #554** - Línea 164:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

---

### 219. `source/docs_maestros/ARQUITECTURA_TRADUCCION_IACT.rst`

**WARNING #555** - Línea 290:
- **Mensaje**: Title underline too short.
- **Solución**: Extender underline para igualar longitud del título

**WARNING #556** - Línea 290:
- **Mensaje**: Title underline too short.
- **Solución**: Extender underline para igualar longitud del título

---

### 220. `source/docs_maestros/GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst`

**WARNING #557** - Línea 1087:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #558** - Línea 1090:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #559** - Línea 1118:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #560** - Línea 1147:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #561** - Línea 1168:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #562** - Línea 1182:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #563** - Línea 1211:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #564** - Línea 1226:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #565** - Línea 1243:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #566** - Línea 1258:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #567** - Línea 126:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #568** - Línea 1270:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #569** - Línea 1279:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #570** - Línea 1282:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #571** - Línea 1287:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #572** - Línea 1289:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #573** - Línea 1291:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #574** - Línea 129:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #575** - Línea 132:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #576** - Línea 135:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #577** - Línea 2308:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #578** - Línea 2314:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #579** - Línea 2318:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #580** - Línea 321:
- **Mensaje**: Bullet list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #581** - Línea 53:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #582** - Línea 56:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #583** - Línea 59:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #584** - Línea 62:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #585** - Línea 65:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 221. `source/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS.md`

**WARNING #586** - Línea 1172:
- **Mensaje**: Lexing literal_block '# Analog�a en ATL/nrule DefaultVerbTranslation {/n    from/n        h : Hebrew!Verb/n    to/n        s : Syriac!Verb (/n            tense <- h.getTemporalSituation(),  # Signifi�/n            # NO: form <- h.form  # Signifiant/n        )/n}/n' as "python" resulted in an error at token: '!'. Retrying in relaxed mode. [misc.highlighting_failure]
- **Solución**: Ver mensaje específico

---

### 222. `source/docs_maestros/PLAN_CONTENIDO.rst`

**WARNING #587** - Línea 416:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #588** - Línea 421:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #589** - Línea 424:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #590** - Línea 432:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #591** - Línea 449:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #592** - Línea 456:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #593** - Línea 461:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #594** - Línea 466:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #595** - Línea 474:
- **Mensaje**: Block quote ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

### 223. `source/docs_maestros/PROMPT_MAESTRO_SPHINX_TRADUCCION.md.rst`

**WARNING #596** - Línea 332:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #597** - Línea 353:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #598** - Línea 360:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #599** - Línea 367:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #600** - Línea 385:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #601** - Línea 394:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #602** - Línea 413:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #603** - Línea 431:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

**WARNING #604** - Línea 441:
- **Mensaje**: Non-consecutive header level increase; H2 to H4 [myst.header]
- **Solución**: Ver mensaje específico

---

### 224. `source/docs_maestros/SINTESIS_METODOLOGICA_ADT.rst`

**WARNING #605** - Línea 394:
- **Mensaje**: Explicit markup ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Agregar línea en blanco después de directiva

**WARNING #606** - Línea 496:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #607** - Línea 499:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #608** - Línea 502:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #609** - Línea 508:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #610** - Línea 624:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #611** - Línea 629:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #612** - Línea 634:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

**WARNING #613** - Línea 640:
- **Mensaje**: Enumerated list ends without a blank line; unexpected unindent. [docutils]
- **Solución**: Ver mensaje específico

---

**Total WARNING**: 613
