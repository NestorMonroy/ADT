# FASE 0: Preparación - Crear Templates para Skills Faltantes

Fecha: 2026-02-01 19:27
Proyecto: ADT Documentation
Directorio: `.mywork/changes/20260201-192709-crear-templates-skills-faltantes/`

---

## Contexto del Proyecto

### Situación Actual

- **Problema identificado**: Solo 2 de 15 skills (13%) tienen templates
- **Skills con templates**: spec-driven-dev (3), work-logger (1)
- **Skills sin templates que necesitan**: 7 skills identificados
- **Deuda técnica**: 8-11 horas estimadas

### Análisis Completado

- ✅ Análisis exhaustivo de 15 skills
- ✅ Evaluación de calidad de templates existentes (9/10)
- ✅ Identificación de skills que necesitan templates
- ✅ Priorización en alta/media/baja
- ✅ Estimación de esfuerzo
- ✅ Work-log creado: `2026-02-01-19-25-analisis-templates-skills.md`

### Documentación de Referencia

**Skills cargados**:
- project-context v1.1.0
- project-discovery v1.1.0
- spec-driven-dev v1.2.0
- work-logger v1.1.0
- skills-management v1.1.0
- changes-directory-management v1.1.0

**Documentos creados**:
- ANALISIS_TEMPLATES_SKILLS.md (completo, 400+ líneas)
- TEMPLATES_RESUMEN.md (ejecutivo)
- TABLA_ESTADO_TEMPLATES.md (visual)
- Work-log: 2026-02-01-19-25-analisis-templates-skills.md

---

## Alcance de Este Proyecto

### Objetivo Principal

Crear templates faltantes para skills de **ALTA PRIORIDAD** (3 skills):
1. commit-helper
2. skills-management
3. incremental-correction-methodology

### Criterios de Éxito

- [x] FASE 0: Preparación completada
- [ ] FASE 1: Requirements documentados y aprobados
- [ ] FASE 2: Design técnico completado y aprobado
- [ ] FASE 3: Tasks descompuestas con estimaciones
- [ ] FASE 4: Templates creados y validados
- [ ] Templates funcionan como se espera
- [ ] Documentación actualizada en cada skill
- [ ] Work-log final creado

### Fuera de Alcance

- Templates de media prioridad (translation-workflow, bash-production-scripting)
- Templates de baja prioridad (sphinx-expert, validation-suite)
- Estos se abordarán en proyectos futuros

---

## Skills a Modificar

### 1. commit-helper

**Ubicación**: `.codex/skills/commit-helper/`
**Estado actual**: Sin directorio templates/
**Template a crear**: `commit-message.template`
**Esfuerzo estimado**: 30 minutos

**Razón**: Skill específico para crear commits, template asegura formato Conventional Commits consistente

### 2. skills-management

**Ubicación**: `.codex/skills/skills-management/`
**Estado actual**: Sin directorio templates/
**Templates a crear**: 
- `SKILL.md.template`
- (opcional) `SKILL-with-templates.md.template`

**Esfuerzo estimado**: 1-2 horas

**Razón**: Skill para CREAR skills, template asegura consistencia en TODOS los skills futuros

### 3. incremental-correction-methodology

**Ubicación**: `.codex/skills/incremental-correction-methodology/`
**Estado actual**: Sin directorio templates/
**Templates a crear**:
- `analysis-phase.md.template`
- `categorization-plan.md.template`
- `execution-log.md.template`
- `final-report.md.template`

**Esfuerzo estimado**: 2-3 horas

**Razón**: Metodología compleja similar a spec-driven-dev, templates facilitan adopción

---

## Modelo de Referencia: spec-driven-dev

### Templates Existentes

**spec-driven-dev/templates/**:
1. `requirements.md.template` (111 líneas)
   - 13 secciones numeradas
   - Contexto, Problema, Objetivos
   - Requisitos Funcionales/No Funcionales
   - Restricciones, Stakeholders, Riesgos
   - Historial de cambios

2. `design.md.template`
   - Decisiones Arquitectónicas
   - Componentes Afectados
   - Plan de Testing

3. `tasks.md.template`
   - Tareas descompuestas
   - Criterios de éxito por tarea
   - Orden de ejecución
   - Checkpoints

**Calidad**: 9/10 - Excelente estructura

### Características a Replicar

- ✅ Secciones numeradas claras
- ✅ Placeholders descriptivos con [corchetes]
- ✅ Tablas para datos estructurados
- ✅ Checkboxes para validación
- ✅ Ejemplos cuando relevante
- ✅ Historial de cambios
- ✅ Comentarios guía en formato MD

---

## Decisiones de Preparación

### Decisión 1: Usar spec-driven-dev para Este Proyecto

**Contexto**: Proyecto de crear templates es complejo (4-6 horas)

**Opciones**:
- A: Usar spec-driven-dev (4 fases)
- B: Hacerlo directamente sin planificación

**Elegida**: A

**Razón**: 
- Proyecto >2 horas cumple criterio para spec-driven
- Afecta 3 skills críticos del proyecto
- Requiere diseño cuidadoso de templates
- Beneficio de documentación para futuro

### Decisión 2: Priorizar Solo Alta Prioridad

**Contexto**: 7 skills podrían tener templates (8-11h total)

**Opciones**:
- A: Crear todos (8-11h)
- B: Solo alta prioridad (4-6h)
- C: Solo quick win (30min)

**Elegida**: B

**Razón**:
- Alta prioridad cubre skills más usados
- Resuelve 80% del problema con 50% del esfuerzo
- Media/baja pueden esperar

### Decisión 3: Nivel de Detalle en Templates

**Contexto**: Templates pueden ser exhaustivos o minimalistas

**Opciones**:
- A: Templates completos como spec-driven-dev (100+ líneas)
- B: Templates minimalistas (20-30 líneas)

**Elegida**: A para skills-management, A moderado para commit-helper e incremental

**Razón**:
- skills-management merece template completo (asegura consistencia futura)
- commit-helper puede ser más corto (solo formato de mensaje)
- incremental necesita templates estructurados pero no exhaustivos

---

## Verificación de Preparación

### Pre-Requirements Checks

- [x] ¿Entiendo el problema completamente?
- [x] ¿Tengo análisis previo documentado?
- [x] ¿Identifiqué todos los skills afectados?
- [x] ¿Tengo modelo de referencia (spec-driven-dev)?
- [x] ¿Sé qué características replicar?
- [x] ¿Decisiones de alcance tomadas?
- [x] ¿Directorio de trabajo creado?
- [x] ¿Work-log del análisis creado?

**Resultado**: ✅ PREPARACIÓN COMPLETADA

### Ready for FASE 1 (Requirements)

- [x] Contexto claro
- [x] Alcance definido
- [x] Skills identificados
- [x] Modelo de referencia disponible
- [x] Decisiones iniciales tomadas

**Conclusión**: ✅ LISTO PARA FASE 1

---

## Próximo Paso

**FASE 1: Requirements**

Crear documento de requirements que defina:
- Contexto del problema
- Objetivos específicos
- Requisitos funcionales para cada template
- Criterios de aceptación
- Restricciones y dependencias

**Archivo a crear**: `20260201-192709-requirements-crear-templates.md`

---

**Estado**: ✅ COMPLETADA
**Tiempo invertido**: 15 minutos
**Próxima fase**: FASE 1 - Requirements
