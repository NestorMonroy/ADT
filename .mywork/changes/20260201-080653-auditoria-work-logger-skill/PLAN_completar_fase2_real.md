# Plan: Completar Fase 2 - Los 8 Skills Faltantes

**Fecha**: 2026-02-01  
**Tiempo estimado**: 3 horas  
**Objetivo**: Actualizar REALMENTE los 8 skills pendientes

---

## 🎯 Skills a Actualizar (8)

### Prioridad CRÍTICA (4)
1. **work-logger** v1.0.0 → v1.1.0 (usuario pidió auditar este)
2. **commit-helper** v1.0.0 → v1.1.0 (uso frecuente)
3. **project-discovery** v1.0.0 → v1.1.0 (falta solo Decision Framework)
4. **project-context** v1.0.0 → v1.1.0 (referencia constante)

### Prioridad ALTA (4)
5. **spec-driven-dev** v1.1.0 → v1.2.0 (ya tiene v1.1.0)
6. **translation-workflow** v1.0.0 → v1.1.0
7. **skills-management** v1.0.0 → v1.1.0
8. **bash-production-scripting** sin YAML → v1.1.0

---

## 📋 Proceso por Skill (ESTRICTO)

### Paso 1: Backup
```bash
cp SKILL.md SKILL_backup_v[VERSION_ACTUAL].md
```

### Paso 2: Actualizar
- Agregar/actualizar Decision Framework
- Agregar/actualizar Trigger Patterns
- Agregar/actualizar Self-Checks
- Actualizar version: X.Y.Z
- Actualizar updated: 2026-02-01
- Agregar entrada en Changelog

### Paso 3: Verificación OBLIGATORIA
```bash
# Verificar versión
grep "version:" SKILL.md

# Verificar Fase 2
grep "## Decision Framework" SKILL.md
grep "## Trigger Patterns" SKILL.md
grep "## Self-Check" SKILL.md

# ✅ TODOS deben dar resultado
```

### Paso 4: Marcar Completado
- [ ] Solo si verificación pasa

---

## ⏱️ Estimación Tiempo

| Skill | Complejidad | Tiempo | Estado |
|-------|-------------|--------|--------|
| work-logger | Media | 25 min | ⏳ Pendiente |
| commit-helper | Baja | 15 min | ⏳ Pendiente |
| project-discovery | Muy Baja | 10 min | ⏳ Pendiente |
| project-context | Media | 20 min | ⏳ Pendiente |
| spec-driven-dev | Media | 25 min | ⏳ Pendiente |
| translation-workflow | Media | 20 min | ⏳ Pendiente |
| skills-management | Media | 20 min | ⏳ Pendiente |
| bash-production-scripting | Alta | 30 min | ⏳ Pendiente |
| **TOTAL** | | **~3 horas** | |

---

## 🚨 REGLAS ABSOLUTAS

### ✅ HACER
1. Crear backup ANTES de modificar
2. Verificar con grep DESPUÉS de modificar
3. Actualizar version y updated
4. Agregar changelog
5. NO marcar completado sin verificar

### ❌ NO HACER
1. Asumir que está hecho
2. Copiar/pegar lista sin verificar
3. Reportar sin grep
4. Saltar pasos de verificación
5. Confiar en memoria

---

## 📝 Checklist Final (ANTES de reportar)

- [ ] 8 backups creados (verificar con ls)
- [ ] 8 skills con Decision Framework (grep confirma)
- [ ] 8 skills con Trigger Patterns (grep confirma)
- [ ] 8 skills con Self-Checks (grep confirma)
- [ ] 8 versiones actualizadas (grep version:)
- [ ] 8 updated: 2026-02-01 (grep updated:)
- [ ] Auditoría final con script automático

---

**Inicio**: Por definir  
**Fin esperado**: +3 horas  
**Verificación**: OBLIGATORIA antes de reportar
