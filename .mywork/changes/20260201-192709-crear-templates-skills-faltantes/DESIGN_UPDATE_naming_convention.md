# DESIGN ACTUALIZADO - Naming Convention Agregada

Fecha: 2026-02-01 20:05
Cambio: Agregada DA-009 sobre convención de nombres específicos

---

## CAMBIO APLICADO

### Nueva Decisión Arquitectónica: DA-009

**Título**: Naming Convention - Nombres Específicos Auto-documentados

**Regla de oro**: Nombre debe ser auto-documentado sin ver contenido

---

## CONVENCIÓN ESTABLECIDA

### Archivos en .mywork/changes/

**CORRECTO** (nombres específicos):
```
.mywork/changes/20260201-correccion-warnings/
├── PLAN_estrategia_correccion.md        ← Auto-documentado
├── ANALISIS_230_warnings_sphinx.md      ← Específico
├── DECISIONES_manual_vs_script.md       ← Claro
└── IMPLEMENTACION_lote_1_archivos.md    ← Descriptivo
```

**INCORRECTO** (nombres genéricos):
```
.mywork/changes/20260201-correccion-warnings/
├── PLAN.md              ← Muy genérico
├── ANALISIS.md          ← No se sabe qué analiza
├── DECISIONES.md        ← No se sabe sobre qué
└── IMPLEMENTACION.md    ← Poco específico
```

---

### EXCEPCIÓN: Templates en Skills

**Templates PUEDEN tener nombres genéricos** (contexto claro por ubicación):

```
.codex/skills/commit-helper/templates/
└── commit-message.template              ← OK (genérico pero ubicación da contexto)

.codex/skills/skills-management/templates/
├── SKILL.md.template                    ← OK (estándar)
└── README.md                            ← OK (estándar)

.codex/skills/incremental-correction-methodology/templates/
├── analysis-phase.md.template           ← OK (fase es específica)
├── categorization-plan.md.template      ← OK (plan es específico)
├── execution-log.md.template            ← OK (log es específico)
└── final-report.md.template             ← OK (report es específico)
```

**Razón de excepción**: 
- Path completo da contexto: `.codex/skills/commit-helper/templates/commit-message.template`
- No hay ambigüedad
- Templates son archivos de referencia, no documentos de trabajo

---

## ARCHIVOS DE ESTE PROYECTO

### Verificación de Cumplimiento

**Archivos actuales**:
- FASE-0-preparacion.md                                    CUMPLE (específico)
- 20260201-192709-requirements-crear-templates.md          CUMPLE (timestamp + específico)
- 20260201-200000-design-crear-templates.md                CUMPLE (timestamp + específico)
- REQUIREMENTS_v0.2_RESUMEN.md                            CUMPLE (versión + específico)
- COMPARACION_v0.1_vs_v0.2.md                             CUMPLE (específico)

**Archivo futuro**:
- 20260201-tasks-crear-templates.md                        CUMPLIRÁ (timestamp + específico)

**Templates a crear** (todos CUMPLEN - son excepción):
- commit-message.template
- SKILL.md.template
- analysis-phase.md.template
- categorization-plan.md.template
- execution-log.md.template
- final-report.md.template
- README.md (en templates/)

---

## BENEFICIOS DE ESTA CONVENCIÓN

### 1. Auto-documentación

**Sin abrir archivo**:
```bash
ls -la .mywork/changes/20260201-correccion-warnings/
# Output muestra nombres descriptivos
# Usuario sabe inmediatamente qué contiene cada archivo
```

### 2. Búsqueda Fácil

**Buscar por nombre**:
```bash
find . -name "*ANALISIS*warnings*"
# Encuentra análisis de warnings sin grep en contenido
```

### 3. Navegación Clara

**Múltiples documentos**:
```
.mywork/changes/proyecto-grande/
├── PLAN_fase_1_implementacion.md
├── PLAN_fase_2_testing.md
├── PLAN_fase_3_deployment.md
├── ANALISIS_rendimiento_inicial.md
├── ANALISIS_cobertura_tests.md
└── DECISIONES_tecnologias_elegidas.md
```

Sin convención, todos serían "PLAN.md" → confusión

---

## IMPACTO EN ESTE PROYECTO

### Cambios en Design v0.2

**Agregado**:
- DA-009: Naming Convention completa
- Ejemplos de nombres correctos/incorrectos
- Excepción documentada para templates
- Nota sobre archivo FASE 3

**Sin cambios**:
- Todos los archivos ya siguen convención
- Templates ya usan nombres apropiados
- Estructura de archivos sigue siendo correcta

---

## PRÓXIMOS PASOS

### FASE 3: Tasks

Archivo seguirá convención:
- Nombre: `20260201-tasks-crear-templates.md`
- NO: `tasks.md` (demasiado genérico)
- NO: `TASKS.md` (demasiado genérico)

---

## RESUMEN

**Convención establecida**: DA-009
**Regla de oro**: Nombres auto-documentados
**Excepción**: Templates en skills
**Cumplimiento actual**: 100%
**Acción requerida**: Ninguna (solo aplicar en archivos futuros)

---

Estado: APLICADO
Design actualizado: v0.2
Pendiente: Aprobación de Design completo para continuar FASE 3
