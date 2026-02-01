# CORRECCIÓN: Error en Diagnóstico - Nombres Específicos

**Fecha**: 2026-02-01  
**Problema**: Error en DIAGNOSTICO_violacion_metodologia_changes_directory.md  
**Error detectado por**: Usuario

---

## ❌ LO QUE PUSE MAL EN EL DIAGNÓSTICO

En el diagnóstico escribí:

```markdown
### Paso 2: Crear Archivos DENTRO del Directorio

```bash
cd .mywork/changes/20260201-073000-mejoras-skills-fase2/

# Ahora SÍ puedo usar nombres "genéricos" porque el directorio da contexto
touch PLAN_trabajo.md                          ❌ INCORRECTO
touch PROPUESTA_v2.md                          ❌ INCORRECTO
touch COMPARACION_propuesta_vs_completado.md   ❌ INCORRECTO
touch ANALISIS_anthropic_best_practices.md     ❌ INCORRECTO
```
```

**Por qué está MAL**: 
- La convención establecida (Opción B) es **SIEMPRE nombres específicos**
- No importa si están en directorio con contexto
- No hay excepciones por "contexto de directorio"

---

## ✅ LO CORRECTO

**Convención**: `TIPO_contexto_especifico_descriptivo.md` **SIEMPRE**

```bash
cd .mywork/changes/20260201-073000-mejoras-skills-fase2/

# Nombres específicos INCLUSO dentro de directorio
touch PLAN_mejoras_skills_fase2.md                             ✅ CORRECTO
touch PROPUESTA_mejoras_skills_v2_basada_anthropic.md         ✅ CORRECTO
touch COMPARACION_propuesta_original_vs_completado_fase2.md   ✅ CORRECTO
touch ANALISIS_anthropic_best_practices_llms_full.md          ✅ CORRECTO
touch ESTADO_progreso_fase2_7_de_12_skills.md                 ✅ CORRECTO
touch RESUMEN_aplicacion_convencion_nombres_especificos.md    ✅ CORRECTO
```

**Por qué CORRECTO**:
- Auto-documentados (no dependen de contexto)
- Funcionan si se mueven a otro directorio
- Buscables por nombre
- Consistencia total

---

## 📋 REGLA FINAL (Sin Ambigüedad)

**Formato obligatorio SIEMPRE**:
```
TIPO_contexto_especifico_descriptivo.md
```

**NO hay excepciones**:
- ❌ NO por estar en directorio con contexto
- ❌ NO por ser archivo temporal
- ❌ NO por "es obvio qué es"

**Ejemplos correctos en CUALQUIER ubicación**:

```bash
# En .mywork/ raíz
PLAN_mejoras_skills_fase2.md

# En .mywork/changes/20260201-073000-mejoras-skills-fase2/
PLAN_mejoras_skills_fase2.md  # MISMO nombre (específico)

# En cualquier otro lado
PLAN_mejoras_skills_fase2.md  # SIEMPRE específico
```

---

## 🔍 POR QUÉ COMETÍ EL ERROR

1. **Pensé que contexto de directorio era suficiente**
   - Directorio: `20260201-073000-mejoras-skills-fase2/`
   - "Ya da contexto, puedo usar `PLAN.md`"
   - ❌ INCORRECTO

2. **Confundí con otros sistemas de nombrado**
   - En algunos proyectos, archivos en directorios contextuales usan nombres genéricos
   - Pero ADT estableció: SIEMPRE específicos (Opción B)

3. **No refresqué la convención en memoria**
   - Usuario estableció convención claramente
   - No la interioricé completamente
   - Necesito skill para refrescar (por eso creamos refresh-skills-context)

---

## ✅ CORRECCIÓN APLICADA

**Actualizado**: DIAGNOSTICO_violacion_metodologia_changes_directory.md

**Sección corregida**: "LO QUE DEBÍ HACER - Paso 2"

**Nueva versión**:
```markdown
### Paso 2: Crear Archivos DENTRO del Directorio

```bash
cd .mywork/changes/20260201-073000-mejoras-skills-fase2/

# Nombres ESPECÍFICOS (convención SIEMPRE aplica)
touch PLAN_mejoras_skills_fase2.md
touch PROPUESTA_mejoras_skills_v2_basada_anthropic.md
touch COMPARACION_propuesta_original_vs_completado.md
touch ANALISIS_anthropic_best_practices_llms_full.md
```

**Por qué correcto**:
- Específicos (no dependen de directorio)
- Auto-documentados
- Portables
- Consistentes con convención establecida
```
```

---

## 💡 LECCIÓN

**"SIEMPRE" significa SIEMPRE**:
- No hay "excepto si..."
- No hay "pero cuando..."
- No hay contexto que justifique excepción

**Convención establecida (Opción B)**:
```
Formato: TIPO_contexto_especifico_descriptivo.md
Aplica: SIEMPRE (100% de los casos)
Excepciones: NINGUNA
```

---

**Creado**: 2026-02-01  
**Propósito**: Corregir error en diagnóstico previo  
**Lección**: "SIEMPRE" no tiene excepciones

