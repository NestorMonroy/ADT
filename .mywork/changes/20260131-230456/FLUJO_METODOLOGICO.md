# Flujo Metodológico Correcto - Corrección Incremental

**Basado en**: incremental-correction-methodology v1.3.0  
**Actualizado**: 2026-02-01 con convención de nombres integrada  
**Versión anterior**: 2026-01-31 con lección aprendida

---

## 📝 CONVENCIÓN DE NOMBRES

**NUEVO (2026-02-01)**: Todos los archivos creados deben seguir convención específica.

**Ver documentación completa**: `CONVENCION_NOMBRES.md` y `.mywork/changes/README.md`

**Regla de Oro**:
> El nombre del archivo debe responder: "¿QUÉ es esto y de QUÉ trata?"

**Formato general**:
```
<TIPO>_<CONTEXTO_ESPECIFICO>_<VERSION>.<ext>
```

**Patrones principales**:
- **Fases**: `FASE<N>_<NOMBRE>.md`
- **Análisis**: `ANALISIS_<TIPO>_<contexto>.md`
- **Scripts**: `SCRIPT_<ACCION>_<nombre_script>.md`
- **Errores**: `ERROR_<descripcion_especifica>.md`
- **Decisiones**: `DECISIONES.md` o `DECISIONES_<contexto>.md`

---

## FLUJO COMPLETO CON ARCHIVOS

```
FASE 0: PREPARACIÓN (15-20 min)
├── Crear: PLAN.md (obligatorio)
├── Crear: DECISIONES.md (obligatorio, se actualiza en toda la sesión)
├── Crear: TRACKING.md (obligatorio)
├── Opcional: FASE0_PREPARACION.md
├── Leer: incremental-correction-methodology COMPLETO
├── Leer: skill(s) específico(s) del dominio
├── Verificar git status limpio
└── Checklist 8/8 ✅
    ↓
FASE 1: ANÁLISIS INICIAL (30-45 min)
├── Crear: FASE1_ANALISIS_INICIAL.md (opcional)
├── Generar: critical.txt, errors.txt, warnings.txt
├── Generar: *.tmp (archivos temporales)
├── Build: make clean && make html
├── Extracción de issues
└── Análisis de distribución
    ↓
FASE 1.5: ANÁLISIS COMPLETO ⚠️ OBLIGATORIO (15-20 min)
├── Crear: ANALISIS_COMPLETO_BUILD.md (OBLIGATORIO)
├── Incluir: Conteo total, archivos, distribución, concentración
├── Incluir: Detalles completos de cada categoría
└── Validar: >500 líneas, 6+ secciones
    ↓
FASE 2: CATEGORIZACIÓN (15-20 min)
├── Crear: FASE2_CATEGORIZACION.md
├── Si hay correcciones: FASE2_CATEGORIZACION_V2.md
├── Usar: Datos del ANALISIS_COMPLETO_BUILD.md (NO estimaciones)
├── Asignar: Complejidad, riesgo, estrategia
└── Documentar: Procedimientos disponibles
    ↓
FASE 3: PRIORIZACIÓN (5-10 min)
├── Crear: FASE3_PRIORIZACION.md
├── Opcional: FASE3_REVISION_ANTIPATRONES.md
├── Actualizar: DECISIONES.md con decisiones de priorización
├── Aplicar criterios: Gravedad, Concentración, Facilidad
└── Definir orden de ejecución (sesiones)
    ↓
FASE 4: EJECUCIÓN INCREMENTAL (Variable)
├── Si creas script: SCRIPT_DESARROLLO_<nombre>.md
├── Si usas script: SCRIPT_RESUMEN_<nombre>.md
├── Si dry-run: SCRIPT_DRY_RUN_<nombre>.txt
├── Si error: ERROR_<descripcion>.md
├── Si análisis: ANALISIS_<tipo>_<contexto>.md
├── Actualizar: TRACKING.md con progreso
├── Actualizar: DECISIONES.md con decisiones emergentes
└── Commits incrementales después de cada corrección
    ↓
FINALIZACIÓN:
└── Crear: RESUMEN_SESION.md (OBLIGATORIO)
```

---

## 📂 ARCHIVOS POR FASE (Detalle)

### FASE 0: PREPARACIÓN

**Archivos OBLIGATORIOS**:

1. **`PLAN.md`**
```markdown
# Plan - Sesión <session-id>

**Fecha**: 2026-MM-DD  
**Objetivo**: [Objetivo principal]

## Contexto
[Por qué se hace esta sesión]

## Fases Planificadas
- [ ] FASE 0: Preparación
- [ ] FASE 1: Análisis
- [ ] FASE 2: Categorización
- [ ] FASE 3: Priorización
- [ ] FASE 4: Ejecución

## Tiempo Estimado
Total: X horas

## Checklist 8/8
□ Skill leído: incremental-correction-methodology
□ Skill leído: [otros skills]
□ Directorio: .mywork/changes/<session-id>/
□ Git: limpio
□ 8 Protecciones: entendidas
□ Anti-patrones: revisados
□ PLAN.md: creado
□ Convención nombres: revisada
```

2. **`DECISIONES.md`**
```markdown
# Decisiones - Sesión <session-id>

## DECISIÓN 1: [Título]
**QUÉ**: [Qué se decidió]
**POR QUÉ**: [Razones]
**ALTERNATIVAS**: [Qué más se consideró]
**TRADE-OFFS**: [Pros/contras]
**DECISIÓN FINAL**: [Decisión]

---
```

3. **`TRACKING.md`**
```markdown
# Tracking - Sesión <session-id>

## Issues Iniciales
- CRITICAL: X
- ERROR: Y
- WARNING: Z
- **Total**: N

## Progreso
### [Fecha/Hora]
- Archivo: [nombre]
- Issues resueltos: N
- Método: [manual/script]
- Commit: [hash]

## Issues Actuales
- CRITICAL: X (-N)
- ERROR: Y (-N)
- WARNING: Z (-N)
- **Total**: M (-N)
```

**Archivo OPCIONAL**:
- `FASE0_PREPARACION.md` - Documentación detallada de preparación

---

### FASE 1: ANÁLISIS INICIAL

**Archivos generados**:

1. **Datos del build** (automático):
```
critical.txt         ← Todos los CRITICAL
errors.txt           ← Todos los ERROR
warnings.txt         ← Todos los WARNING
```

2. **Temporales** (opcional):
```
critical_files.tmp   ← Lista de archivos con CRITICAL
error_files.tmp      ← Lista de archivos con ERROR
*.tmp                ← Otros temporales
```

3. **Documentación** (opcional):
```
FASE1_ANALISIS_INICIAL.md    ← Documentar proceso de análisis
```

**Comandos típicos**:
```bash
cd /tmp/ADT
make clean && make html 2>&1 | tee build-log-$(date +%Y%m%d-%H%M%S).log

# Extraer issues
grep "CRITICAL:" build-log.txt > critical.txt
grep "ERROR:" build-log.txt > errors.txt
grep "WARNING:" build-log.txt > warnings.txt
```

---

### FASE 1.5: ANÁLISIS COMPLETO ⚠️ OBLIGATORIO

**Archivo OBLIGATORIO**:

**`ANALISIS_COMPLETO_BUILD.md`**

**Tamaño esperado**: >500 líneas

**Estructura mínima**:
```markdown
# Análisis Completo del Build

**Fecha**: 2026-MM-DD  
**Build log**: build-log-<timestamp>.log

## 1. CONTEO TOTAL
- CRITICAL: X issues
- ERROR: Y issues
- WARNING: Z issues
- **Total**: N issues

## 2. ANÁLISIS CRITICAL
### Archivos Afectados (X archivos)
1. archivo1.rst: N issues
2. archivo2.rst: M issues
...

### Distribución
- Concentración alta: [archivos con >50%]
- Detalles completos de cada issue

## 3. ANÁLISIS ERROR
[Similar a CRITICAL]

## 4. ANÁLISIS WARNING
### Por Categoría
1. Categoría 1: N issues
   - Archivos: [lista]
...

## 5. RESUMEN CONSOLIDADO
[Tabla comparativa]

## 6. CONCLUSIONES Y RECOMENDACIONES

## 7. ARCHIVOS DE REFERENCIA
- critical.txt
- errors.txt
- warnings.txt

## 8. COMANDOS ÚTILES
```

**Validación**:
```bash
# Verificar que existe y tiene contenido suficiente
wc -l ANALISIS_COMPLETO_BUILD.md  # Debe ser >500
grep "^## " ANALISIS_COMPLETO_BUILD.md | wc -l  # Debe ser >=6
```

---

### FASE 2: CATEGORIZACIÓN

**Archivos generados**:

1. **`FASE2_CATEGORIZACION.md`** (primera versión)

**Estructura**:
```markdown
# FASE 2: Categorización

**Basado en**: ANALISIS_COMPLETO_BUILD.md  
**Fecha**: 2026-MM-DD

## Categoría 1: [Nombre]

**Issues**: X (basado en ANALISIS)  
**Archivos afectados**: [lista exacta del ANALISIS]  
**Distribución**: 
- archivo1.rst: N issues (X%)
- archivo2.rst: M issues (Y%)

**Complejidad**: TRIVIAL | MODERADO | COMPLEJO  
**Riesgo automatización**: BAJO | MEDIO | ALTO  
**Estrategia**: Manual | Script | Híbrido  
**Procedimiento disponible**: [Si/No - referencia al skill]

## Categoría 2: ...
```

2. **Si hay correcciones**: `FASE2_CATEGORIZACION_V2.md`, `V3.md`, etc.

**CRÍTICO**: 
- ❌ NO usar estimaciones ("~5 archivos")
- ✅ Usar datos exactos del ANALISIS_COMPLETO_BUILD.md

---

### FASE 3: PRIORIZACIÓN

**Archivos generados**:

1. **`FASE3_PRIORIZACION.md`**

```markdown
# FASE 3: Priorización

**Basado en**: FASE2_CATEGORIZACION.md  
**Fecha**: 2026-MM-DD

## Criterios Aplicados

1. **Gravedad** (40%): CRITICAL > ERROR > WARNING
2. **Concentración** (25%): Alta (>50%) > Media > Baja
3. **Facilidad** (15%): TRIVIAL > MODERADO > COMPLEJO
4. **Riesgo** (10%): BAJO > MEDIO > ALTO
5. **Procedimientos** (5%): Con procedimiento > Sin
6. **Dependencias** (5%): Causa otros > Independiente

## Scoring por Categoría

| Categoría | Score | Prioridad |
|-----------|-------|-----------|
| Cat1      | 12/15 | #1        |
| Cat2      | 10/15 | #2        |
...

## Plan de Ejecución

### Sesión 1: [Categoría] - PRIORITY #1
- **Archivos**: [lista]
- **Issues**: N
- **Tiempo estimado**: X horas
- **Estrategia**: [manual/script]
- **Justificación**: [por qué primero]

### Sesión 2: ...

## Decisiones Críticas
[Referencia a DECISIONES.md]
```

2. **Opcional**: `FASE3_REVISION_ANTIPATRONES.md`

```markdown
# Revisión de Anti-Patrones - FASE 3

## Anti-Patrón #1: [Nombre]
**Aplicable**: SI | NO  
**Cómo se previene**: [explicación]

## Anti-Patrón #2: ...
```

3. **Actualizar**: `DECISIONES.md` con decisiones de priorización

---

### FASE 4: EJECUCIÓN

**Archivos según actividad**:

#### Si Desarrollas un Script:

1. **`SCRIPT_DESARROLLO_<nombre_script>.md`**
```markdown
# Desarrollo Script: <nombre_script>

## Objetivo
[Qué debe hacer]

## Análisis del Problema
[Patrón detectado]

## Diseño
[Cómo lo resolverá]

## Implementación
[Ubicación del script]
```

2. **`SCRIPT_RESUMEN_<nombre_script>.md`**
```markdown
# Script: <nombre_script>

## Características
- Versión: X.Y.Z
- Ubicación: scripts/<nombre_script>.sh
- Archivos procesados: N
- Issues corregidos: M

## Uso
[Ejemplos de comandos]

## Resultados
[Qué encontró, qué corrigió]
```

3. **`SCRIPT_DRY_RUN_<nombre_script>.txt`**
```
[Output completo del dry-run]
```

#### Si Encuentras Errores:

**`ERROR_<descripcion_especifica>.md`**

Ejemplos:
- `ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md`
- `ERROR_BUILD_nuevos_warnings.md`
- `ERROR_SCRIPT_sed_pattern_mismatch.md`

```markdown
# Error: <Descripción>

## Contexto
[Dónde/cuándo ocurrió]

## Problema
[Qué salió mal]

## Causa Raíz
[Por qué ocurrió]

## Impacto
[Qué afectó]

## Solución
[Cómo se corrigió]

## Lección
[Qué aprendimos]
```

#### Si Haces Análisis Específicos:

**`ANALISIS_<tipo>_<contexto>.md`**

Ejemplos:
- `ANALISIS_CRITICAL_error_01_omisiones.md`
- `ANALISIS_WARNING_headers_detallado.md`
- `ANALISIS_DISTRIBUCION_issues.md`

```markdown
# Análisis: <Tipo> - <Contexto>

## Objetivo
[Qué se está analizando]

## Datos
[Fuente de datos]

## Análisis
[Hallazgos detallados]

## Conclusiones
[Qué se descubrió]

## Recomendaciones
[Qué hacer con esto]
```

#### Actualizar Continuamente:

1. **`TRACKING.md`** - Después de cada corrección
2. **`DECISIONES.md`** - Cuando tomas decisiones emergentes

---

### FINALIZACIÓN DE SESIÓN

**Archivo OBLIGATORIO**:

**`RESUMEN_SESION.md`**

```markdown
# Resumen - Sesión <session-id>

**Fecha**: 2026-MM-DD  
**Duración**: X horas  
**Fases completadas**: 0, 1, 2, 3, 4

## Objetivo Original
[Del PLAN.md]

## Qué se Hizo

### FASE 0: Preparación
[Resumen]

### FASE 1-1.5: Análisis
[Resumen]

### FASE 2: Categorización
[Resumen]

### FASE 3: Priorización
[Resumen]

### FASE 4: Ejecución
[Resumen]

## Qué se Logró

**Issues Resueltos**:
- CRITICAL: X → Y (-Z)
- ERROR: A → B (-C)
- WARNING: D → E (-F)
- **Total**: M → N (-O)

**Archivos Modificados**: P  
**Scripts Creados**: Q  
**Commits**: R

## Decisiones Importantes
1. [Referencia a DECISIONES.md #1]
2. [Referencia a DECISIONES.md #2]
...

## Errores y Aprendizajes
1. [Error detectado + lección]
2. ...

## Archivos Generados
- PLAN.md
- DECISIONES.md
- ANALISIS_COMPLETO_BUILD.md
- FASE2_CATEGORIZACION_V2.md
- FASE3_PRIORIZACION.md
- SCRIPT_RESUMEN_<nombre>.md
- [otros]

## Próximos Pasos
1. [Qué queda pendiente]
2. [Próxima sesión]
...

## Referencias
- Build log: [ubicación]
- Backups: [ubicación]
- Commits: [rango de hashes]
```

---

## ✅ CHECKLIST DE NOMBRES

Antes de crear un archivo, verificar:

```
□ ¿Incluye TIPO al inicio? (FASE, ANALISIS, SCRIPT, ERROR)
□ ¿Incluye CONTEXTO específico?
□ ¿Si hay versiones, está marcada? (_V2, _V3)
□ ¿Es claro qué contiene sin abrirlo?
□ ¿Sigue formato <TIPO>_<CONTEXTO>_<VERSION>?
□ ¿Evita nombres genéricos? (NO: output.txt, temp.md)
□ ¿Usa extensión correcta? (.md documentos, .txt datos, .tmp temporales)
```

**Si todos ✅** → Nombre correcto

---

## 📋 EJEMPLOS COMPLETOS

### Sesión Típica - Archivos Creados:

```
.mywork/changes/20260131-230456/
├── PLAN.md                                    ← FASE 0
├── DECISIONES.md                              ← FASE 0 (actualizado en toda sesión)
├── TRACKING.md                                ← FASE 0 (actualizado en toda sesión)
│
├── critical.txt                               ← FASE 1
├── errors.txt
├── warnings.txt
├── ANALISIS_COMPLETO_BUILD.md                 ← FASE 1.5 (OBLIGATORIO)
│
├── FASE2_CATEGORIZACION.md                    ← FASE 2 V1
├── FASE2_CATEGORIZACION_V2.md                 ← FASE 2 V2 (corregida)
│
├── FASE3_PRIORIZACION.md                      ← FASE 3
├── FASE3_REVISION_ANTIPATRONES.md             ← FASE 3 (opcional)
│
├── SCRIPT_RESUMEN_fix_critical_titles.md      ← FASE 4
├── SCRIPT_DRY_RUN_fix_critical_titles.txt
├── ANALISIS_CRITICAL_error_01_omisiones.md
├── ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md
│
└── RESUMEN_SESION.md                          ← Finalización
```

---

## ⚠️ REGLA CRÍTICA: ANALISIS_COMPLETO_BUILD.md

**FASE 2 NO PUEDE EJECUTARSE SIN ANALISIS_COMPLETO_BUILD.md**

### Por Qué Es Crítico

**Problema observado** (sesión 2026-01-31):
- FASE 2 original usó estimaciones: "~5-6 archivos"
- Resultado: Números incorrectos, priorización subóptima
- Causa raíz: Categorizar sin datos reales

**Solución implementada**:
- FASE 1 → Genera ANALISIS_COMPLETO_BUILD.md PRIMERO
- ANALISIS contiene TODOS los datos
- FASE 2 usa datos del ANALISIS (no estimaciones)

### Validación Pre-FASE 2

```bash
# Verificar ANALISIS existe y está completo
[ -f "ANALISIS_COMPLETO_BUILD.md" ] || echo "❌ BLOQUEADOR"
[ $(wc -l < ANALISIS_COMPLETO_BUILD.md) -gt 500 ] || echo "❌ Muy corto"
[ $(grep -c "^## " ANALISIS_COMPLETO_BUILD.md) -ge 6 ] || echo "❌ Faltan secciones"
```

---

## 🎯 TIEMPO ESTIMADO POR FASE

| Fase | Actividad | Tiempo | Archivos Clave |
|------|-----------|--------|----------------|
| 0 | Preparación | 15-20 min | PLAN.md, DECISIONES.md, TRACKING.md |
| 1 | Análisis Inicial | 30-45 min | critical.txt, errors.txt, warnings.txt |
| 1.5 | Generar ANALISIS | 15-20 min | **ANALISIS_COMPLETO_BUILD.md** |
| 2 | Categorización | 15-20 min | FASE2_CATEGORIZACION.md |
| 3 | Priorización | 5-10 min | FASE3_PRIORIZACION.md |
| 4 | Ejecución | Variable | SCRIPT_*, ANALISIS_*, ERROR_* |
| Fin | Resumen | 10-15 min | RESUMEN_SESION.md |

**Total preparación**: 80-115 min (antes de correcciones)  
**ROI**: Validado - ahorra horas de trabajo ineficiente

---

## 📖 REFERENCIAS

**Documentación del Sistema**:
- `.mywork/changes/README.md` - Sistema completo de organización
- `CONVENCION_NOMBRES.md` - Convención detallada con ejemplos
- Este documento - Flujo con archivos integrados

**Skills**:
- `incremental-correction-methodology` v1.3.0
- `sphinx-expert` (si aplica)

**Templates**:
- Ver README.md para templates de PLAN, DECISIONES, RESUMEN

---

## 🔄 FLUJO VISUAL CON ARCHIVOS

```
┌─────────────────────────────────────────────────────┐
│ FASE 0: PREPARACIÓN                                 │
│ Crear: PLAN.md, DECISIONES.md, TRACKING.md         │
│ Opcional: FASE0_PREPARACION.md                      │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│ FASE 1: ANÁLISIS INICIAL                            │
│ Generar: critical.txt, errors.txt, warnings.txt     │
│ Opcional: FASE1_ANALISIS_INICIAL.md                 │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│ FASE 1.5: ANÁLISIS COMPLETO ⚠️ OBLIGATORIO          │
│ Crear: ANALISIS_COMPLETO_BUILD.md                   │
│ Validar: >500 líneas, 6+ secciones                  │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│ FASE 2: CATEGORIZACIÓN                              │
│ Crear: FASE2_CATEGORIZACION.md                      │
│ Si correcciones: _V2.md, _V3.md                     │
│ Usar: Datos del ANALISIS (NO estimaciones)          │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│ FASE 3: PRIORIZACIÓN                                │
│ Crear: FASE3_PRIORIZACION.md                        │
│ Opcional: FASE3_REVISION_ANTIPATRONES.md            │
│ Actualizar: DECISIONES.md                           │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│ FASE 4: EJECUCIÓN                                   │
│ Scripts: SCRIPT_RESUMEN_*.md, SCRIPT_DRY_RUN_*.txt  │
│ Análisis: ANALISIS_<tipo>_<contexto>.md             │
│ Errores: ERROR_<descripcion>.md                     │
│ Actualizar: TRACKING.md, DECISIONES.md              │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│ FINALIZACIÓN                                        │
│ Crear: RESUMEN_SESION.md (OBLIGATORIO)              │
└─────────────────────────────────────────────────────┘
```

---

**Versión**: 2.0 (con convención de nombres integrada)  
**Fecha**: 2026-02-01  
**Validado en**: Sesión 20260131-230456  
**Metodología base**: incremental-correction-methodology v1.3.0  
**Próxima actualización**: Cuando se identifique mejora del flujo
