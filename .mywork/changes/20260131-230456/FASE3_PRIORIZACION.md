# FASE 3: PRIORIZACIÓN

**Fecha**: 2026-01-31 23:50  
**Basado en**: ANALISIS_COMPLETO_BUILD.md + FASE2_CATEGORIZACION_V2.md  
**Objetivo**: Determinar orden óptimo de ejecución basado en 6 criterios

---

## CRITERIOS DE PRIORIZACIÓN APLICADOS

### Criterio 1: Gravedad (Peso: 40%)
```
CRITICAL > ERROR > WARNING
```
**Razón**: CRITICAL bloquea build correcto, debe resolverse primero

### Criterio 2: Concentración (Peso: 25%) 🆕 v1.3.0
```
Alta concentración (>50% en 1 archivo) > Baja concentración
```
**Razón**: workflow_general.rst tiene 61% CRITICAL → máximo impacto por archivo

### Criterio 3: Facilidad (Peso: 15%)
```
TRIVIAL > MODERADO > COMPLEJO
```
**Razón**: Quick wins generan momentum psicológico

### Criterio 4: Riesgo (Peso: 10%)
```
BAJO riesgo automatización > MEDIO > ALTO
```
**Razón**: Evitar introducir regresiones

### Criterio 5: Procedimientos (Peso: 5%)
```
Con procedimiento documentado > Sin procedimiento
```
**Razón**: Menos riesgo, guía clara en sphinx-expert

### Criterio 6: Dependencias (Peso: 5%)
```
Errores que causan otros > Errores independientes
```
**Razón**: Resolver causa puede resolver efectos

---

## APLICACIÓN DE CRITERIOS POR CATEGORÍA

### CATEGORÍA 1: Section Structure (CRITICAL)

**Datos del análisis**:
- Issues: 31 CRITICAL
- Archivos: 5 (workflow_general.rst: 19, otros: 3 cada uno)
- Concentración: **61% en 1 archivo** ⭐
- Complejidad: COMPLEJO
- Riesgo: ALTO
- Procedimiento: NO

**Evaluación por criterios**:
1. Gravedad: ✅✅✅✅ (CRITICAL = máximo)
2. Concentración: ✅✅✅ (61% = altísimo)
3. Facilidad: ❌ (COMPLEJO)
4. Riesgo: ❌ (ALTO)
5. Procedimientos: ❌ (NO disponible)
6. Dependencias: ✅ (CRITICAL puede causar ERROR/WARNING)

**Puntuación**: 10/15 = 67%

**Decisión**: PRIORIDAD #1
**Razón**: Gravedad CRITICAL + Concentración 61% >> Complejidad

---

### CATEGORÍA 2: Transitions (ERROR)

**Datos del análisis**:
- Issues: 6 ERROR
- Archivos: 3 (workflow_general.rst: 3, otros: 2 + 1)
- Concentración: 50% en 1 archivo
- Complejidad: TRIVIAL
- Riesgo: BAJO
- Procedimiento: SÍ (sphinx-expert)

**Evaluación por criterios**:
1. Gravedad: ✅✅✅ (ERROR)
2. Concentración: ✅✅ (50%)
3. Facilidad: ✅✅✅ (TRIVIAL = máximo)
4. Riesgo: ✅✅ (BAJO)
5. Procedimientos: ✅ (Disponible)
6. Dependencias: ✅ (ERROR puede causar WARNING)

**Puntuación**: 13/15 = 87%

**Decisión**: PRIORIDAD #2 (Quick Win después de CRITICAL)
**Razón**: ERROR + TRIVIAL + Procedimiento = ejecución rápida y segura

---

### CATEGORÍA 3: List-Tables (ERROR)

**Datos del análisis**:
- Issues: 8 ERROR
- Archivos: 5 (workflow_general.rst: 3, otros: 2+1+1+1)
- Concentración: 37% en 1 archivo
- Complejidad: COMPLEJO
- Riesgo: ALTO
- Procedimiento: NO

**Evaluación por criterios**:
1. Gravedad: ✅✅✅ (ERROR)
2. Concentración: ✅ (37%)
3. Facilidad: ❌ (COMPLEJO)
4. Riesgo: ❌ (ALTO)
5. Procedimientos: ❌ (NO disponible)
6. Dependencias: ✅ (ERROR puede causar WARNING)

**Puntuación**: 8/15 = 53%

**Decisión**: PRIORIDAD #3
**Razón**: ERROR debe resolverse, pero DESPUÉS de quick win (Transitions)

---

### CATEGORÍA 4: Lexers (WARNING)

**Datos del análisis**:
- Issues: 8 WARNING
- Archivos: 9 archivos .md (TODOS en arc42_documentation)
- Concentración: 100% en directorio específico
- Complejidad: TRIVIAL
- Riesgo: BAJO
- Procedimiento: SÍ (sphinx-expert)

**Evaluación por criterios**:
1. Gravedad: ✅ (WARNING)
2. Concentración: ✅✅ (100% en directorio)
3. Facilidad: ✅✅✅ (TRIVIAL = máximo)
4. Riesgo: ✅✅ (BAJO)
5. Procedimientos: ✅ (Disponible)
6. Dependencias: ❌ (Independiente)

**Puntuación**: 11/15 = 73%

**Decisión**: PRIORIDAD #4 (Quick Win #2)
**Razón**: TRIVIAL + Procedimiento + Concentrado en 1 directorio = rápido

---

### CATEGORÍA 5: Blank Lines (WARNING)

**Datos del análisis**:
- Issues: 259 WARNING
- Archivos: 179 archivos
- Concentración: Disperso (~1.4 issues/archivo)
- Complejidad: MODERADO
- Riesgo: BAJO
- Procedimiento: SÍ (sphinx-expert)

**Evaluación por criterios**:
1. Gravedad: ✅ (WARNING)
2. Concentración: ❌ (Disperso)
3. Facilidad: ✅✅ (MODERADO)
4. Riesgo: ✅✅ (BAJO)
5. Procedimientos: ✅ (Disponible + Validado)
6. Dependencias: ❌ (Independiente)

**Puntuación**: 8/15 = 53%

**Decisión**: PRIORIDAD #5 (Script seguro viable)
**Razón**: Numeroso pero procedimiento documentado + riesgo bajo

---

### CATEGORÍA 6: Headers (WARNING)

**Datos del análisis**:
- Issues: 309 WARNING
- Archivos: 294 archivos
- Concentración: Muy disperso (~1 issue/archivo)
- Complejidad: MODERADO
- Riesgo: MEDIO-ALTO
- Procedimiento: SÍ (sphinx-expert, pero no automatizable)

**Evaluación por criterios**:
1. Gravedad: ✅ (WARNING)
2. Concentración: ❌ (Muy disperso)
3. Facilidad: ✅ (MODERADO)
4. Riesgo: ❌ (MEDIO-ALTO)
5. Procedimientos: ⚠️ (Disponible pero manual selectivo)
6. Dependencias: ❌ (Independiente)

**Puntuación**: 5/15 = 33%

**Decisión**: PRIORIDAD #6 (DEFER o Manual Selectivo)
**Razón**: Numeroso + Disperso + Riesgo medio → evaluar después

---

### CATEGORÍA 7-10: Otros (Markup, Referencias, Glossary, Otros)

**Datos del análisis**:
- Issues totales: ~27 WARNING + ERROR
- Complejidad: Variable
- Riesgo: Variable

**Evaluación**:
- Bajo impacto (pocos issues)
- Sin procedimientos específicos
- Complejidad variable

**Decisión**: PRIORIDAD #7 (Evaluar caso por caso DESPUÉS)
**Razón**: Bajo volumen, resolver después de categorías principales

---

## ORDEN DE EJECUCIÓN FINAL

Basado en puntuaciones y criterios:

### FASE 4A: SESIÓN 1 - CRITICAL (Prioridad máxima)

**Objetivo**: Resolver CRITICAL para desbloquear build

**Categoría**: Section Structure (31 CRITICAL, 5 archivos)

**Orden de archivos** (por concentración):
1. **workflow_general.rst** (19 CRITICAL) ← 61% del problema
2. WORKFLOW_v1_6_0_ACTUALIZACION.rst (3 CRITICAL)
3. guia_rapida.rst (3 CRITICAL)
4. GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst (3 CRITICAL)
5. error_01_omisiones.rst (3 CRITICAL)

**Estrategia**: Manual puro, un archivo a la vez
**Tiempo estimado**: 2-3 horas (30-40 min/archivo)
**Commits**: 5 commits (1 por archivo)
**Validación**: Build después de cada archivo

**POR QUÉ PRIMERO**:
- ✅ CRITICAL bloquea build correcto
- ✅ 61% concentrado en 1 archivo (máximo impacto)
- ✅ Resolver causa potencialmente resuelve efectos downstream

---

### FASE 4B: SESIÓN 2 - ERROR Quick Win (Momentum)

**Objetivo**: Quick win para generar momentum

**Categoría**: Transitions (6 ERROR, 3 archivos)

**Orden de archivos**:
1. workflow_general.rst (3 ERROR)
2. glossary_tip_4.rst (2 ERROR)
3. SINTESIS_METODOLOGICA_ADT.rst (1 ERROR)

**Estrategia**: Manual rápido (patrón simple: eliminar línea inicial)
**Tiempo estimado**: 30 minutos (10 min/archivo)
**Commits**: 3 commits (1 por archivo) O 1 commit agrupado
**Validación**: Build después de completar

**POR QUÉ SEGUNDO**:
- ✅ TRIVIAL = ejecución rápida
- ✅ Procedimiento documentado en sphinx-expert
- ✅ Quick win genera momentum psicológico
- ✅ ERROR debe resolverse antes que WARNING

---

### FASE 4C: SESIÓN 3 - ERROR Complejo

**Objetivo**: Resolver ERROR restantes

**Categoría**: List-Tables (8 ERROR, 5 archivos)

**Orden de archivos** (por concentración):
1. workflow_general.rst (3 ERROR)
2. GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst (2 ERROR)
3. MD_002_cuando_enriquecer.rst (1 ERROR)
4. guia_rapida.rst (1 ERROR)
5. quality_ejemplo_tpu_1.rst (1 ERROR)

**Estrategia**: Manual puro (requiere entender contenido tabla)
**Tiempo estimado**: 1-1.5 horas (10-15 min/tabla)
**Commits**: 5 commits (1 por archivo)
**Validación**: Build después de cada archivo

**POR QUÉ TERCERO**:
- ✅ ERROR debe resolverse
- ✅ COMPLEJO requiere atención (DESPUÉS de quick win)
- ✅ Concentración moderada (37% en workflow_general.rst)

---

### FASE 4D: SESIÓN 4 - WARNING Quick Win (Lexers)

**Objetivo**: Quick win adicional

**Categoría**: Lexers (8 WARNING, 9 archivos .md)

**Ubicación**: TODOS en `arc42_documentation/original/_posts`

**Estrategia**: Script trivial O búsqueda/reemplazo manual
- Cambiar 'PlantUML' → 'text'
- Cambiar 'plantuml' → 'text'

**Tiempo estimado**: 15-20 minutos
**Commits**: 1 commit con todos los cambios (archivos .md, bajo riesgo)
**Validación**: Build después

**POR QUÉ CUARTO**:
- ✅ TRIVIAL = muy rápido
- ✅ Procedimiento documentado
- ✅ Concentrado en 1 directorio
- ✅ Quick win mantiene momentum

---

### FASE 4E: SESIÓN 5 - WARNING Numeroso (Blank Lines)

**Objetivo**: Resolver WARNING numeroso con script seguro

**Categoría**: Blank Lines (259 WARNING, 179 archivos)

**Estrategia**: Script con 7 Protecciones Obligatorias
- Dry-run obligatorio
- Un archivo a la vez (lotes de 10-20 para eficiencia)
- Git commit por lote
- Validar que issues disminuyen
- Rollback si falla

**Tiempo estimado**: 2-3 horas (incluye desarrollo script)
**Commits**: ~10-20 commits (lotes pequeños)
**Validación**: Build después de cada lote

**POR QUÉ QUINTO**:
- ✅ Procedimiento documentado y validado
- ✅ Riesgo BAJO (patrón simple)
- ✅ Script seguro viable
- ⚠️ Numeroso (requiere tiempo)

---

### FASE 4F: SESIÓN 6 - WARNING Disperso (Headers)

**Objetivo**: EVALUAR si proceder o DEFER

**Categoría**: Headers (309 WARNING, 294 archivos)

**Opciones**:
- **A) DEFER**: Skip para sesión futura
- **B) Manual Selectivo**: Solo archivos críticos o con múltiples issues
- **C) Abordar casos específicos**: Solo H3→H1 (más comunes)

**Decisión**: EVALUAR después de completar FASE 4A-4E

**POR QUÉ EVALUAR DESPUÉS**:
- ⚠️ Muy disperso (~1 issue/archivo)
- ⚠️ Riesgo medio-alto
- ⚠️ 294 archivos = 4-6 horas manual
- ✅ Procedimiento disponible pero manual selectivo

**Criterio de decisión**:
- Si tiempo disponible >10 horas: Abordar selectivo
- Si tiempo <10 horas: DEFER

---

### FASE 4G: SESIÓN 7 - Otros (Opcional)

**Categorías restantes**:
- Markup (5 WARNING) - Manual
- Referencias (2 WARNING) - Manual rápido
- Glossary (5 WARNING) - Manual
- Otros (~15) - Caso por caso

**Estrategia**: Evaluar caso por caso DESPUÉS
**Tiempo estimado**: Variable
**Prioridad**: BAJA (pocos issues)

---

## ESTIMACIONES DE TIEMPO

| Sesión | Categoría | Issues | Archivos | Tiempo | Acumulado |
|--------|-----------|--------|----------|--------|-----------|
| 1 | CRITICAL (Section) | 31 | 5 | 2-3h | 2-3h |
| 2 | ERROR (Transitions) | 6 | 3 | 30min | 2.5-3.5h |
| 3 | ERROR (List-Tables) | 8 | 5 | 1-1.5h | 3.5-5h |
| 4 | WARNING (Lexers) | 8 | 9 | 20min | 3.8-5.3h |
| 5 | WARNING (Blank Lines) | 259 | 179 | 2-3h | 5.8-8.3h |
| 6 | WARNING (Headers) | 309 | 294 | DEFER/4-6h | 9.8-14.3h |
| 7 | Otros | ~27 | Variable | Variable | - |

**Escenarios**:

**Mínimo viable** (Solo CRITICAL):
- Sesión 1 solamente
- 31 issues resueltos
- 2-3 horas
- Build sin CRITICAL ✅

**Realista** (CRITICAL + ERROR):
- Sesiones 1-3
- 45 issues resueltos (31 CRITICAL + 14 ERROR)
- 3.5-5 horas
- Build sin errores graves ✅

**Óptimo** (+ Quick Wins):
- Sesiones 1-4
- 53 issues resueltos
- 3.8-5.3 horas
- Build sin CRITICAL/ERROR + quick wins ✅

**Comprehensive** (+ Blank Lines):
- Sesiones 1-5
- 312 issues resueltos (47% del total)
- 5.8-8.3 horas
- Mayoría de issues resueltos ✅

**Completo** (TODO menos Headers):
- Sesiones 1-5 + 7
- ~340 issues resueltos (51% del total)
- 6-9 horas
- Solo Headers y casos edge pendientes

**Exhaustivo** (TODO):
- Sesiones 1-7 completas
- ~661 issues resueltos (100%)
- 12-16 horas
- Build perfecto ✅

---

## RECOMENDACIÓN BASADA EN TIEMPO DISPONIBLE

### Si tienes <3 horas:
**Ejecutar**: Sesión 1 (CRITICAL)  
**Resultado**: Build sin CRITICAL  
**Issues resueltos**: 31 (5% del total)

### Si tienes 4-5 horas:
**Ejecutar**: Sesiones 1-3 (CRITICAL + ERROR)  
**Resultado**: Build sin errores graves  
**Issues resueltos**: 45 (7% del total)

### Si tienes 6-8 horas:
**Ejecutar**: Sesiones 1-5 (hasta Blank Lines)  
**Resultado**: 47% de issues resueltos  
**Issues resueltos**: 312 (47% del total)  
**Recomendado** ✅

### Si tienes >10 horas:
**Ejecutar**: Sesiones 1-6 (incluye Headers selectivo)  
**Resultado**: 70-80% de issues resueltos  
**Issues resueltos**: ~450-500 (70-80% del total)

---

## DECISIONES DOCUMENTADAS

### Decisión 1: Priorizar workflow_general.rst

**QUÉ**: Corregir workflow_general.rst PRIMERO en cada categoría

**POR QUÉ**:
- Concentración: 61% CRITICAL (19/31)
- Concentración: 37% List-Tables (3/8)
- Concentración: 50% Transitions (3/6)
- **Total en este archivo**: 25 issues

**TRADE-OFF**:
- ✅ Máximo impacto por archivo (25 issues en 1)
- ❌ Archivo complejo (múltiples issues)
- **Decisión**: Beneficio >> Complejidad

### Decisión 2: Transitions ANTES que List-Tables

**QUÉ**: ERROR Transitions (Sesión 2) antes que ERROR List-Tables (Sesión 3)

**POR QUÉ**:
- Transitions: TRIVIAL, 30 min
- List-Tables: COMPLEJO, 1-1.5 horas
- Quick win genera momentum psicológico

**TRADE-OFF**:
- ✅ Momentum (resolver rápido primero)
- ✅ Procedimiento documentado (menor riesgo)
- ❌ List-Tables tiene más issues (8 vs 6)
- **Decisión**: Momentum > Cantidad

### Decisión 3: Lexers ANTES que Blank Lines

**QUÉ**: WARNING Lexers (Sesión 4) antes que WARNING Blank Lines (Sesión 5)

**POR QUÉ**:
- Lexers: 8 issues, 20 min, TRIVIAL
- Blank Lines: 259 issues, 2-3 horas, MODERADO
- Quick win adicional mantiene momentum

**TRADE-OFF**:
- ✅ Quick win mantiene motivación
- ✅ Concentrado (1 directorio)
- ❌ Blank Lines más impactante (259 vs 8)
- **Decisión**: Mantener momentum > Impacto inmediato

### Decisión 4: Headers → DEFER/Evaluar

**QUÉ**: Evaluar Headers DESPUÉS de completar Sesiones 1-5

**POR QUÉ**:
- 309 issues en 294 archivos (muy disperso)
- Riesgo medio-alto
- 4-6 horas estimadas
- Solo WARNING (no bloqueante)

**TRADE-OFF**:
- ✅ Evita gastar tiempo en disperso de bajo impacto
- ✅ Prioriza issues graves primero
- ❌ Deja 309 issues pendientes
- **Decisión**: Priorizar impacto > Completitud

### Decisión 5: Script para Blank Lines (CONDICIONAL)

**QUÉ**: Usar script con 7 Protecciones para Blank Lines

**CONDICIONAL**: Solo SI usuario aprueba script

**POR QUÉ**:
- Procedimiento documentado y validado
- Riesgo BAJO
- 179 archivos = inviable manual (5-6 horas)
- Script ahorra 2-3 horas

**TRADE-OFF**:
- ✅ Eficiencia (2h vs 5h)
- ✅ Procedimiento probado
- ⚠️ Requiere desarrollo script (30-45 min)
- ❌ Usuario prefiere manual (experiencia previa negativa)
- **Decisión**: Preguntar al usuario

**Alternativa**: Si usuario prefiere manual → DEFER Blank Lines

---

## PLAN DE VALIDACIÓN

**Después de cada corrección**:
1. Build limpio: `make clean && make html`
2. Capturar log: `make clean && make html 2>&1 | tee build-TIMESTAMP.log`
3. Contar issues: `grep -c "WARNING:" build.log` (y ERROR, CRITICAL)
4. Verificar NO introducimos nuevos issues
5. Commit si validación pasa
6. Rollback si validación falla

**Frecuencia**:
- CRITICAL: Build después de CADA archivo
- ERROR: Build después de CADA archivo
- WARNING Lexers: Build después de completar
- WARNING Blank Lines: Build después de cada LOTE (10-20 archivos)

---

## CRITERIO DE "DONE"

**Mínimo aceptable**:
- ✅ 0 CRITICAL
- ✅ 0 ERROR

**Óptimo**:
- ✅ 0 CRITICAL
- ✅ 0 ERROR
- ✅ <100 WARNING (reducción 80%+)

**Perfecto**:
- ✅ 0 CRITICAL
- ✅ 0 ERROR
- ✅ 0 WARNING

---

## SIGUIENTE PASO

**FASE 3 COMPLETADA** ✅

**Output**:
- Plan de priorización con 7 sesiones definidas
- 5 decisiones documentadas con trade-offs
- Estimaciones por escenario
- Recomendación basada en tiempo

**Próximo paso**: Presentar plan al usuario para validación

**Pregunta para el usuario**:
1. ¿Cuánto tiempo tienes disponible?
2. ¿Qué escenario prefieres? (Mínimo/Realista/Óptimo/Comprehensive)
3. ¿Script para Blank Lines O manual/defer?

Una vez decidas, procederemos a **FASE 4: EJECUCIÓN**.
