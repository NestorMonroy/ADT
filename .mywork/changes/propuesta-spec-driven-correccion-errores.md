# Propuesta: Aplicar Spec-Driven Development para Corrección de Errores de Build

Fecha: 2026-01-30 03:31
Proyecto: ADT Documentation

## Contexto

Acabamos de completar un análisis exhaustivo del build de Sphinx que reveló:
- **949 issues totales**
- **72 ERRORS**
- **33 CRITICAL**
- **844 WARNINGS**

Documentado en: `.mywork/work-logs/2026-01-30-03-27-analisis-completo-build-sphinx-errores-warnings.md`

## Metodología Propuesta: Spec-Driven Development

Según `.codex/skills/spec-driven-dev/SKILL.md`, esta metodología es apropiada para:
- ✅ Cambios arquitectónicos
- ✅ Refactorings importantes
- ✅ Trabajo que requiere planificación estructurada

**Nuestra situación califica** porque:
1. Son 949 issues que requieren priorización sistemática
2. Involucra múltiples archivos (730 archivos fuente)
3. Necesita coordinación de correcciones
4. Requiere validación incremental
5. Debe documentar decisiones técnicas

## Metodología en 4 Fases

### FASE 1: Requirements (Requerimientos) 📋

**Objetivo**: Definir QUÉ necesitamos corregir

**Directorio**: `.mywork/changes/2026-01-30-corregir-errores-build-sphinx/`

**Archivo**: `2026-01-30-03-31-requirements-corregir-errores-build.md`

**Contenido propuesto**:
- Contexto: Estado actual del build (949 issues)
- Problema: Errores bloquean calidad de documentación
- Objetivos: 
  - Eliminar 72 ERRORS
  - Eliminar 33 CRITICAL
  - Reducir WARNINGS críticos
- Requisitos funcionales priorizados por categoría
- Restricciones: No romper contenido existente
- Criterios de aceptación: Build exitoso con 0 ERRORS/CRITICAL

### FASE 2: Design (Diseño) 🎨

**Objetivo**: Definir CÓMO corregiremos los issues

**Archivo**: `2026-01-30-XX-XX-design-corregir-errores-build.md`

**Contenido propuesto**:
- Decisiones arquitectónicas:
  - DA-001: Estrategia de corrección por lotes (por categoría)
  - DA-002: Uso de scripts de fix existentes vs. manual
  - DA-003: Orden de corrección (CRITICAL → ERROR → WARNING)
- Componentes afectados (archivos RST)
- Plan de validación incremental
- Plan de rollback

### FASE 3: Tasks (Tareas) ✅

**Objetivo**: Definir pasos EXACTOS de implementación

**Archivo**: `2026-01-30-XX-XX-tasks-corregir-errores-build.md`

**Contenido propuesto**:
- TASK-001 a TASK-NNN con:
  - Descripción detallada
  - Archivos afectados
  - Comandos exactos
  - Criterios de éxito
  - Dependencias
  - Checkpoints de validación

### FASE 4: Implementation (Implementación) 🚀

**Objetivo**: EJECUTAR las tareas definidas

**Proceso**:
- Ejecutar cada TASK en orden
- Validar criterios de éxito
- Commits frecuentes
- Documentar problemas en QUESTIONS.md si aparecen

## Ventajas de Este Enfoque

1. **Estructurado**: Cada fase construye sobre la anterior
2. **Aprobación explícita**: Usuario aprueba cada fase antes de continuar
3. **Documentado**: Decisiones registradas para futuro
4. **Reversible**: Plan de rollback en cada fase
5. **Validable**: Criterios claros de éxito
6. **Reproducible**: Proceso bien definido

## Alternativa Rápida (No Recomendada)

Podríamos empezar a corregir errores directamente sin spec:
- ❌ Sin priorización clara
- ❌ Sin coordinación entre correcciones
- ❌ Riesgo de romper algo
- ❌ Decisiones no documentadas
- ❌ Difícil de pausar/reanudar

## Propuesta de Acción

### Opción A: Spec-Driven Completo (RECOMENDADO)

```
1. Crear FASE 1: Requirements
   └─> SOLICITAR APROBACIÓN del usuario
2. Crear FASE 2: Design
   └─> SOLICITAR APROBACIÓN del usuario
3. Crear FASE 3: Tasks
   └─> SOLICITAR APROBACIÓN del usuario
4. Ejecutar FASE 4: Implementation
   └─> Con validación continua
```

**Tiempo estimado**: 
- Fases 1-3: 1-2 horas de planificación
- Fase 4: 8-15 horas de implementación

**Ventaja**: Proceso estructurado, decisiones documentadas, bajo riesgo

### Opción B: Spec-Driven Simplificado

```
1. Crear Requirements + Design combinados
   └─> SOLICITAR APROBACIÓN del usuario
2. Crear Tasks detalladas
   └─> SOLICITAR APROBACIÓN del usuario
3. Ejecutar Implementation
```

**Tiempo estimado**:
- Fases 1-2: 30-60 min de planificación
- Fase 3: 8-15 horas de implementación

**Ventaja**: Más rápido, aún estructurado

### Opción C: Corrección Directa por Prioridad

```
1. Empezar con CRITICAL (33)
2. Continuar con ERRORS (72)
3. Abordar WARNINGS críticos
```

**Tiempo estimado**: 8-15 horas

**Desventaja**: Sin estructura formal, decisiones ad-hoc

## Recomendación Final

**Opción A: Spec-Driven Completo**

Razones:
1. Tenemos 949 issues - necesitamos estructura
2. El proyecto ya tiene metodología establecida en `.codex/`
3. La inversión en planificación ahorra tiempo en implementación
4. Documenta decisiones para mantenimiento futuro
5. Permite pausar/reanudar de manera ordenada

## Siguiente Paso Inmediato

**Si usuario aprueba Opción A**:
```
Crear: .mywork/changes/2026-01-30-corregir-errores-build-sphinx/
       └── 2026-01-30-03-31-requirements-corregir-errores-build.md
       
Contenido: Requirements completos basados en análisis de 949 issues

SOLICITAR APROBACIÓN antes de continuar con FASE 2
```

**Si usuario aprueba Opción B**:
```
Crear: .mywork/changes/2026-01-30-corregir-errores-build-sphinx/
       └── 2026-01-30-03-31-requirements-design-corregir-errores.md
       
Contenido: Requirements + Design combinados

SOLICITAR APROBACIÓN antes de Tasks
```

**Si usuario prefiere Opción C**:
```
Empezar corrección directa de CRITICAL issues (25 Section Title Issues)
```

## Pregunta al Usuario

**¿Qué opción prefiere para abordar la corrección de los 949 issues del build?**

A. Spec-Driven Completo (4 fases, aprobación por fase)
B. Spec-Driven Simplificado (2 fases combinadas)
C. Corrección directa por prioridad

---

**Archivo**: `.mywork/changes/propuesta-spec-driven-correccion-errores.md`
**Estado**: Esperando decisión del usuario
