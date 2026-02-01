# ANÁLISIS: Inconsistencia en changes-directory-management

**Fecha**: 2026-02-01  
**Skill**: changes-directory-management v1.1.0  
**Problema**: Menciona "PLAN.md" (nombre genérico) vs convención nombres específicos

---

## 🔍 INCONSISTENCIA DETECTADA

### En changes-directory-management SKILL.md

**Línea 60**:
```markdown
3. **¿El trabajo está en progreso activo?**
   → Usar timestamp actual
   → Crear PLAN.md dentro  ← ❌ NOMBRE GENÉRICO
```

**Línea 141**:
```markdown
### Post-Creación
- [ ] ¿Creé PLAN.md dentro del directorio?  ← ❌ NOMBRE GENÉRICO
```

**Problema**: 
- Skill sugiere crear `PLAN.md` (genérico)
- Convención establecida: `TIPO_contexto_especifico.md` SIEMPRE
- No hay excepciones, incluso dentro de directorios

---

## ✅ CORRECCIÓN NECESARIA

### Debe decir (consistente con convención):

**Línea 60**:
```markdown
3. **¿El trabajo está en progreso activo?**
   → Usar timestamp actual
   → Crear PLAN_trabajo_directorio.md dentro
```

**Línea 141**:
```markdown
### Post-Creación
- [ ] ¿Creé PLAN_trabajo_directorio.md dentro del directorio?
```

**Alternativas válidas**:
```
PLAN_trabajo_mejoras_skills.md
PLAN_implementacion_feature_x.md
PLAN_correccion_warnings_sphinx.md
```

**NUNCA**:
```
PLAN.md  ← ❌ Genérico
```

---

## 📋 OTROS SKILLS A REVISAR

Buscar menciones de nombres genéricos en skills:

```bash
cd /tmp/ADT/.codex/skills
grep -r "PLAN\.md" */SKILL.md
grep -r "ANALISIS\.md" */SKILL.md
grep -r "RESUMEN\.md" */SKILL.md
grep -r "TRACKING\.md" */SKILL.md
```

**Resultado esperado**: Encontrar y corregir todas las menciones

---

## ✅ ACCIÓN REQUERIDA

1. Actualizar changes-directory-management:
   - Cambiar "PLAN.md" → "PLAN_trabajo_directorio.md"
   - O usar placeholder: "PLAN_[contexto_especifico].md"
   - Actualizar version a v1.2.0

2. Revisar otros skills:
   - incremental-correction-methodology
   - spec-driven-dev
   - Cualquier otro que mencione nombres genéricos

3. Agregar a Critical Reminders:
   - "Nombres específicos SIEMPRE - sin excepciones"

---

**Creado**: 2026-02-01  
**Estado**: Análisis completado  
**Próxima acción**: Actualizar changes-directory-management

