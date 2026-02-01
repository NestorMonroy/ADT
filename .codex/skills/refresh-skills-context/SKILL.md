---
name: refresh-skills-context
description: "Refresca skills en memoria durante sesión activa. Usar cuando: actualizaste skills y necesitas recargarlos, trabajas >2h y metodología puede haber cambiado, o detectas que usas conocimiento antiguo de skills."
version: 1.0.0
created: 2026-02-01
updated: 2026-02-01
related_skills:
  - project-discovery: "Ejecutar al INICIO de sesión (este es para DURANTE)"
  - skills-management: "Para actualizar skills"
---

# Refresh Skills Context - Recarga de Skills en Memoria

**Versión**: 1.0.0  
**Ubicación**: `/tmp/ADT/.codex/skills/refresh-skills-context/`  
**Proyecto**: ADT Documentation

---

## ⚠️ DIFERENCIA CRÍTICA

**project-discovery**: Ejecutar al **INICIO** de cada sesión nueva
**refresh-skills-context**: Ejecutar **DURANTE** sesión activa cuando:
- Actualizaste skills
- Trabajas >2 horas
- Detectas conocimiento antiguo

---

## Cuándo Usar

### ✅ SIEMPRE usar cuando:

1. **Actualizaste skills DURANTE la sesión**
   - Agregaste Decision Framework a skill
   - Modificaste SKILL.md
   - Creaste nuevo skill
   - Moviste/renombraste skills

2. **Sesión larga (>2 horas)**
   - Context window puede haber "olvidado" skills
   - Metodología puede haber cambiado
   - Necesitas refrescar conocimiento

3. **Detectas que usas conocimiento antiguo**
   - No sigues metodología actual
   - Mencionas versiones viejas de skills
   - Contradices lo documentado en skills

### ❌ NO usar cuando:

- Es inicio de sesión nueva → usar `project-discovery`
- No has actualizado skills
- Sesión corta (<1 hora) sin cambios

---

## Decision Framework: ¿Necesito Refrescar?

**Pregúntate en este orden**:

1. **¿Acabo de actualizar algún skill?**
   → SÍ → **REFRESH INMEDIATO**

2. **¿Trabajo >2 horas en esta sesión?**
   → SÍ → **REFRESH PREVENTIVO**

3. **¿Estoy siguiendo metodología correcta?**
   → NO → **REFRESH CORRECTIVO**

4. **¿Mencioné versión de skill que no coincide con actual?**
   → SÍ → **REFRESH OBLIGATORIO**

5. **¿Usuario señala que no sigo metodología?**
   → SÍ → **REFRESH CRÍTICO**

6. **¿Recuerdo claramente contenido de todos los skills relevantes?**
   → NO → **REFRESH RECOMENDADO**

**Regla de oro**: Si dudas → **REFRESH** (no cuesta mucho, evita errores)

---

## Trigger Patterns

### Señales Explícitas (100% ejecutar)

- Usuario dice: "refresca las skills"
- Usuario dice: "acabamos de actualizar [skill]"
- Usuario dice: "no estás siguiendo la metodología"
- Usuario dice: "revisa el skill actualizado"

### Señales Implícitas (muy probable)

- Usuario corrige tu comportamiento
- Usuario señala contradicción con skill
- Usuario pregunta: "¿leíste el skill X?"
- Trabajas >2 horas sin refrescar

### Señales Automáticas (self-trigger)

**Claude debe auto-detectar**:
- Mencioné versión antigua de skill
- No seguí Decision Framework documentado
- Violé Self-Checks que acabo de implementar
- Contradije metodología que documenté

### Trigger Words

- "refresca", "recarga", "actualiza contexto"
- "skill actualizado", "nueva versión"
- "no sigues", "contradices", "violaste"
- "versión antigua", "conocimiento obsoleto"

---

## Self-Check Before Refresh

### Pre-Refresh Checks
- [ ] ¿Estoy en /tmp/ADT?
- [ ] ¿Identifiqué QUÉ skills necesito refrescar?
- [ ] ¿O necesito refrescar TODOS?

### During Refresh Checks
- [ ] ¿Estoy leyendo versión ACTUAL del skill?
- [ ] ¿Entiendo los cambios vs versión que tenía?
- [ ] ¿Veo Decision Frameworks, Trigger Patterns, Self-Checks?

### Post-Refresh Checks
- [ ] ¿Ahora recuerdo metodología actualizada?
- [ ] ¿Puedo aplicar Decision Framework correctamente?
- [ ] ¿Entiendo qué cambió?

---

## Workflow de Refresh

### PASO 1: Identificar Skills a Refrescar (30 seg)

**Opción A: Refresh Específico**
```bash
# Solo skills que cambiaron
cd /tmp/ADT/.codex/skills

# Ver qué skills tienen version reciente
grep -r "updated: 2026-02-01" */SKILL.md
```

**Opción B: Refresh Completo**
```bash
# Todos los skills (si sesión muy larga o muchos cambios)
cd /tmp/ADT/.codex/skills
ls -d */
```

### PASO 2: Leer README Actualizado (1 min)

```bash
view .codex/skills/README.md
```

**Verificar**:
- ¿Hay nuevos skills?
- ¿Hay skills deprecados?
- ¿Cambió mapa de relaciones?

### PASO 3: Refrescar Skills Críticos (2-5 min)

**Prioridad de lectura**:

1. **CRÍTICOS** (siempre refrescar):
   - project-discovery
   - changes-directory-management
   - incremental-correction-methodology

2. **ALTA** (si relevantes para tarea actual):
   - sphinx-expert (si trabajas con Sphinx)
   - validation-suite (si validas builds)
   - commit-helper (si vas a hacer commits)
   - work-logger (si vas a documentar)

3. **MEDIA** (si los mencionaste recientemente):
   - spec-driven-dev
   - translation-workflow
   - project-context

4. **BAJA** (solo si necesario):
   - bash-production-scripting
   - skills-management

**Comando**:
```bash
# Leer skill actualizado
view .codex/skills/[skill-name]/SKILL.md
```

**Enfocarse en**:
- Frontmatter (versión actualizada)
- Decision Framework (si agregado)
- Trigger Patterns (si agregado)
- Self-Checks (si agregado)
- Secciones modificadas

### PASO 4: Confirmar al Usuario (10 seg)

Ejemplo:
"He refrescado los siguientes skills (versiones actualizadas):
- changes-directory-management v1.1.0
- refresh-skills-context v1.0.0

Ahora aplicaré la metodología correcta."

---

## Casos de Uso Comunes

### Caso 1: Acabamos de Actualizar Skills (Fase 2)

**Situación**: Completamos Fase 2 - agregamos Decision Frameworks a 12 skills

**Acción**:
```bash
cd /tmp/ADT/.codex/skills

# Refrescar los 12 skills actualizados
view validation-suite/SKILL.md
view incremental-correction-methodology/SKILL.md
view sphinx-expert/SKILL.md
# ... etc para todos los actualizados
```

**Resultado**: Ahora conoces Decision Frameworks, Trigger Patterns, Self-Checks

---

### Caso 2: Sesión Larga (>2h) sin Refresh

**Situación**: Llevas 4 horas trabajando, no has refrescado skills

**Acción**:
```bash
cd /tmp/ADT/.codex/skills

# Refresh preventivo de skills críticos
view changes-directory-management/SKILL.md
view work-logger/SKILL.md
view commit-helper/SKILL.md
```

**Resultado**: Metodología refrescada, evitas usar conocimiento antiguo

---

### Caso 3: Usuario Señala Violación de Metodología

**Situación**: Usuario dice "no estás siguiendo changes-directory-management"

**Acción**:
```bash
# Refresh INMEDIATO del skill señalado
view .codex/skills/changes-directory-management/SKILL.md

# Leer secciones críticas:
# - Decision Framework
# - Trigger Patterns
# - Self-Checks
```

**Resultado**: Corriges comportamiento según metodología actual

---

### Caso 4: Acabas de Crear Nuevo Skill

**Situación**: Usuario y Claude crearon `refresh-skills-context` skill

**Acción**:
```bash
# Leer el skill que acabas de crear
view .codex/skills/refresh-skills-context/SKILL.md

# Actualizar README si existe
view .codex/skills/README.md
```

**Resultado**: Conoces el nuevo skill, puedes usarlo

---

## Diferencia con project-discovery

| Aspecto | project-discovery | refresh-skills-context |
|---------|-------------------|------------------------|
| **Cuándo** | INICIO de sesión | DURANTE sesión |
| **Frecuencia** | 1 vez por sesión | N veces según necesidad |
| **Trigger** | Automático (nueva sesión) | Manual (skill actualizado) |
| **Alcance** | Todos los skills | Skills específicos |
| **Propósito** | Cargar contexto inicial | Actualizar contexto |
| **Obligatorio** | SÍ (siempre) | CONDICIONAL (si cambios) |

---

## Antipatrones

### ❌ ANTIPATRÓN 1: No Refrescar Después de Actualizar

**Problema**:
- Actualizas skill con Decision Framework
- NO refrescas el skill
- Sigues usando conocimiento antiguo (sin Decision Framework)

**Consecuencia**: Contradices lo que acabas de documentar

**Solución**: SIEMPRE refrescar después de actualizar skill

---

### ❌ ANTIPATRÓN 2: Asumir que "Ya Lo Sé"

**Problema**:
- Sesión >2 horas
- "No necesito refrescar, recuerdo todo"
- Context window ha "olvidado" detalles

**Consecuencia**: Violaciones sutiles de metodología

**Solución**: Refresh preventivo cada 2 horas

---

### ❌ ANTIPATRÓN 3: Refrescar Todo Innecesariamente

**Problema**:
- Lees TODOS los skills cada vez
- Pierdes tiempo en skills irrelevantes
- Sobrecarga context window

**Consecuencia**: Ineficiencia, lentitud

**Solución**: Refrescar solo skills relevantes/actualizados

---

### ❌ ANTIPATRÓN 4: No Confirmar al Usuario

**Problema**:
- Refrescas skills en silencio
- Usuario no sabe que refrescaste
- Usuario repite la corrección

**Consecuencia**: Frustración del usuario

**Solución**: SIEMPRE confirmar "He refrescado [skills]"

---

## Integración con Workflow

### Workflow Completo con Refresh

```
INICIO DE SESIÓN
├─→ project-discovery (cargar skills inicialmente)
│
DURANTE SESIÓN (2+ horas)
├─→ [trabajo normal]
├─→ [actualizar skill]
├─→ refresh-skills-context (recargar skill actualizado) ← NUEVO
├─→ [más trabajo]
│
FIN DE SESIÓN
└─→ work-logger (documentar)
```

### Integración con skills-management

**Cuando usas skills-management para actualizar skill**:

```bash
# 1. Actualizar skill (usando skills-management)
# Modificas .codex/skills/[nombre]/SKILL.md

# 2. INMEDIATAMENTE después
# Ejecutar refresh-skills-context
view .codex/skills/[nombre]/SKILL.md

# 3. Confirmar
"He refrescado [nombre] v[nueva-version]"
```

---

## Métricas de Éxito

### Indicadores de que Refresh Funciona

✅ **No contradices skills que acabas de actualizar**
✅ **Sigues Decision Frameworks recién agregados**
✅ **Aplicas Self-Checks implementados recientemente**
✅ **Mencionas versiones correctas de skills**
✅ **Usuario no necesita recordarte metodología**

### Indicadores de que Necesitas Refresh

❌ **Usuario señala violación de metodología**
❌ **Mencionas versión antigua de skill**
❌ **No aplicas Decision Framework que existe**
❌ **Contradices lo que documentaste**
❌ **Sesión >2h sin refrescar**

---

## Ejemplo Real: Este Mismo Caso

### Lo Que Pasó

1. ✅ Completamos Fase 2 (actualizamos 12 skills)
2. ❌ NO refresqué los skills actualizados
3. ❌ Violé changes-directory-management
4. ✅ Usuario señaló el error
5. ✅ Estamos creando refresh-skills-context

### Lo Que Debí Hacer

```bash
# Después de completar Fase 2
cd /tmp/ADT/.codex/skills

# Refrescar skills críticos actualizados
view changes-directory-management/SKILL.md  # v1.1.0
view work-logger/SKILL.md                   # v1.1.0
view commit-helper/SKILL.md                 # v1.1.0

# Confirmar
"He refrescado skills actualizados (v1.1.0).
Ahora aplicaré Decision Frameworks implementados."
```

**Resultado esperado**: NO hubiera violado metodología

---

## Versionamiento

### v1.0.0 (2026-02-01)

**Skill inicial - Refresh de Skills en Memoria**

**Propósito**:
- Resolver problema de "conocimiento antiguo"
- Permitir refresh durante sesión larga
- Complementar project-discovery

**Funcionalidad**:
- Decision Framework para decidir cuándo refrescar
- Trigger Patterns (explícitos, implícitos, automáticos)
- Self-Checks (pre/during/post refresh)
- Workflow de refresh por prioridad
- Casos de uso documentados
- Diferenciación clara con project-discovery

**Motivación**:
- Detectado en producción: Claude violó changes-directory-management
- Causa raíz: No refrescó skill después de actualizarlo en Fase 2
- Solución: Nuevo skill para refrescar contexto durante sesión

**Líneas**: 600+  
**Dependencias**: project-discovery, skills-management

---

**Última actualización**: 2026-02-01  
**Mantenedor**: ADT Team  
**Ubicación del Proyecto**: `/tmp/ADT`
