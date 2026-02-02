# Mejoras para el Proyecto ADT - Basadas en System Prompt de Claude

**Fecha**: 2026-02-01  
**Fuente**: Análisis de CLAUDE_SYSTEM_PROMPT_COMPLETE.txt  
**Objetivo**: Identificar patrones útiles para agregar a `.codex/skills/`

---

## 🎯 PATRÓN 1: Skill de "Project Discovery" (CRÍTICO)

### Problema Actual
- Claude NO busca automáticamente `.codex/skills/`
- System prompt de Anthropic NO instruye búsqueda de skills locales
- Depende del criterio de Claude

### Solución: Crear nuevo skill

**Ubicación propuesta**: `.codex/skills/project-discovery/SKILL.md`

**Contenido sugerido**:

```markdown
---
name: project-discovery
description: "Metodología OBLIGATORIA para descubrir y cargar skills del proyecto ANTES de cualquier trabajo. Garantiza que Claude siempre lea las metodologías locales primero."
version: 1.0.0
priority: CRITICAL
order: 0
---

# Project Discovery

**REGLA ABSOLUTA**: Este skill se ejecuta PRIMERO, antes que cualquier otro.

## Cuándo Usar

✅ SIEMPRE al inicio de CADA conversación nueva
✅ SIEMPRE que el usuario mencione el proyecto ADT
✅ SIEMPRE antes de leer cualquier skill de /mnt/skills

## Workflow Obligatorio

### PASO 0: Verificar Ubicación (5 segundos)
```bash
cd /tmp/ADT  # Siempre verificar
pwd          # Confirmar ubicación
```

### PASO 1: Buscar Skills del Proyecto (10 segundos)
```bash
# Verificar si existe .codex/skills
if [ -d .codex/skills ]; then
    echo "✅ Skills del proyecto encontrados"
    ls -la .codex/skills/
else
    echo "❌ No hay skills del proyecto"
fi
```

### PASO 2: Leer README Obligatorio (30 segundos)
```bash
view .codex/skills/README.md
```

**Contenido clave del README**:
- Lista de skills activos
- Versiones actuales
- Mapa de relaciones
- Guía de uso por tarea

### PASO 3: Identificar Skills Relevantes (10 segundos)

**Decision Framework**:
1. ¿La tarea involucra corrección de 100+ issues? → `incremental-correction-methodology`
2. ¿La tarea involucra Sphinx/RST? → `sphinx-expert`
3. ¿La tarea requiere crear directorios en .mywork/changes/? → `changes-directory-management`
4. ¿La tarea requiere commits? → `commit-helper`
5. ¿La tarea requiere logging? → `work-logger`
6. ¿Siempre? → `project-context` (base para todo)

### PASO 4: Cargar Skills Relevantes (variable)
```bash
# Ejemplo para tarea de corrección de errores
view .codex/skills/incremental-correction-methodology/SKILL.md
view .codex/skills/sphinx-expert/SKILL.md
view .codex/skills/validation-suite/SKILL.md
```

### PASO 5: Confirmar al Usuario (5 segundos)
"He cargado los siguientes skills del proyecto: X, Y, Z"

---

## Trigger Patterns

**Detectar automáticamente cuando aplicar**:

### Señales Explícitas
- Usuario menciona "/tmp/ADT"
- Usuario dice "nuestro proyecto"
- Usuario dice "según nuestra metodología"
- Usuario pregunta por convenciones del proyecto

### Señales Implícitas
- Archivo subido con path que contiene "ADT"
- Usuario usa terminología específica de ADT (transformación, traducción, etc.)
- Usuario menciona arc42, Sphinx, reStructuredText
- Contexto de trabajo en documentación

---

## Self-Check Before Starting

Antes de hacer CUALQUIER trabajo, verificar:

- [ ] ¿Estoy en /tmp/ADT?
- [ ] ¿Leí .codex/skills/README.md?
- [ ] ¿Identifiqué los skills relevantes?
- [ ] ¿Cargué al menos 1 skill del proyecto?
- [ ] ¿Entiendo el contexto metodológico de ADT?

**Si alguna respuesta es NO → STOP y ejecutar project-discovery primero**

---

## Antipatrones

❌ **NO hacer**:
1. Asumir que no hay skills del proyecto
2. Ir directamente a /mnt/skills sin buscar locales
3. Empezar a trabajar sin leer README.md
4. Seguir convenciones genéricas si existen específicas del proyecto

---

## Beneficios

✅ **Garantiza** que Claude siempre use metodologías del proyecto
✅ **Independiente** del system prompt de Anthropic
✅ **Explícito** - no depende de criterio de Claude
✅ **Reproducible** - mismo flujo en cada sesión
✅ **Documentado** - usuario sabe qué esperar

---

## Integración con README.md

Actualizar `.codex/skills/README.md` para incluir:

```markdown
## ⚠️ SKILL CRÍTICO - LEER PRIMERO

**project-discovery** es el skill #0 (orden: 0, priority: CRITICAL)

DEBE ejecutarse ANTES que cualquier otro skill en TODA conversación nueva.

Sin este skill, Claude puede no cargar las metodologías del proyecto.
```

---

## Ejemplo de Uso

```
[Nueva conversación inicia]

Usuario: "Ayúdame a corregir los errores de build de Sphinx"

Claude [internamente]:
1. ✅ Verifico ubicación: /tmp/ADT
2. ✅ Busco skills: .codex/skills existe
3. ✅ Leo README.md
4. ✅ Identifico skills relevantes: sphinx-expert, validation-suite
5. ✅ Cargo ambos skills
6. ✅ Confirmo al usuario

Claude [respuesta]:
"He cargado los skills del proyecto: sphinx-expert (v1.6.0) y validation-suite (v1.0.0). 
Vamos a analizar los errores de Sphinx siguiendo nuestra metodología..."
```

---

## Versionamiento

- **v1.0.0**: Versión inicial - workflow básico de discovery
- Futuras versiones pueden agregar:
  - Auto-detección de ubicación del proyecto
  - Caché de skills cargados
  - Validación de versiones de skills

---

**Este skill resuelve el problema identificado**: Claude ignoró `.codex/skills/` porque su system prompt no instruye buscarlos. Con este skill como #0, el problema se elimina.
```

---

## 🎯 PATRÓN 2: Decision Frameworks Numerados

### En Mi System Prompt
```xml
<decision_framework>
1. Time reference mentioned? → recent_chats
2. Specific topic/content mentioned? → conversation_search  
3. Both time AND topic? → If you have a specific time frame, use recent_chats...
4. Vague reference? → Ask for clarification
5. No past reference? → Don't use tools
</decision_framework>
```

### Aplicación a TU Proyecto

**Agregar a cada skill existente**:

#### Ejemplo 1: incremental-correction-methodology
```markdown
## Decision Framework: ¿Usar Manual vs Script?

1. ¿Los issues son idénticos (mismo patrón)? → Considerar script
2. ¿Puedes cumplir las 7 Protecciones? → Script SEGURO posible
3. ¿Los issues varían en contexto? → Manual OBLIGATORIO
4. ¿No estás 100% seguro? → Manual por defecto
5. ¿Ya tuviste problemas con scripts antes? → Manual SIEMPRE

**Regla**: Si dudas entre manual y script → MANUAL
```

#### Ejemplo 2: sphinx-expert
```markdown
## Decision Framework: ¿Qué Tipo de Error?

1. ¿Es WARNING de "document isn't included in toctree"? → Agregar a toctree
2. ¿Es ERROR de "Unknown directive"? → Verificar extensión Sphinx
3. ¿Es WARNING de "Explicit markup ends without blank line"? → Agregar línea en blanco
4. ¿Es CRITICAL de "Title underline too short"? → Ajustar underline
5. ¿Es ERROR de "malformed table"? → Revisar formato de tabla

**Regla**: Si el error no está en la lista → Consultar SKILL.md completo
```

---

## 🎯 PATRÓN 3: Trigger Patterns Explícitos

### En Mi System Prompt
```xml
<trigger_patterns>
**Always use past chats tools when you see:** 
- Explicit references: "continue our conversation about..."
- Temporal references: "what did we talk about yesterday"
- Implicit signals: 
  - Past tense verbs: "you suggested", "we decided"
  - Possessives without context: "my project", "our approach"
</trigger_patterns>
```

### Aplicación a TU Proyecto

**Agregar a cada skill**:

#### Ejemplo: changes-directory-management
```markdown
## Trigger Patterns

### Cuándo usar este skill:

**Señales Explícitas**:
- Usuario dice "crea un directorio en changes/"
- Usuario dice "necesito documentar este cambio"
- Usuario dice "vamos a trabajar en X"

**Señales Implícitas**:
- Usuario pide hacer cambios complejos (>30 min)
- Usuario menciona "plan" o "diseño"
- Usuario dice "vamos a..."
- Usuario pregunta "dónde pongo esto?"

**Trigger words**:
- "cambio", "change", "modificación"
- "plan", "diseño", "spec"
- "documentar", "registrar"
- "directorio", "carpeta", "folder"

### Cuándo NO usar:

❌ Cambios triviales (1-2 líneas)
❌ Fixes rápidos sin planificación
❌ Solo consultas (sin implementación)
```

---

## 🎯 PATRÓN 4: Self-Check Mechanisms

### En Mi System Prompt
```xml
<self_check_before_responding>
Before including ANY text from search results, ask yourself:
- Is this quote 15+ words? (If yes -> SEVERE VIOLATION)
- Have I already quoted this source? (If yes -> source is CLOSED)
- Is this a song lyric, poem, or haiku? (If yes -> do not reproduce)
</self_check_before_responding>
```

### Aplicación a TU Proyecto

**Agregar a skills críticos**:

#### Ejemplo 1: incremental-correction-methodology
```markdown
## Self-Check Before Using Script

Antes de ejecutar CUALQUIER script automático, verificar:

- [ ] ¿Cumple las 7 Protecciones TODAS?
- [ ] ¿Hice dry-run y revisé output?
- [ ] ¿Tengo git status limpio?
- [ ] ¿Probé en UN archivo primero?
- [ ] ¿Entiendo qué hace CADA línea del script?
- [ ] ¿Tengo plan de rollback listo?
- [ ] ¿Documenté la decisión de usar script?

**Si alguna respuesta es NO → NO ejecutar script, hacer manual**
```

#### Ejemplo 2: commit-helper
```markdown
## Self-Check Before Commit

Antes de hacer commit:

- [ ] ¿El mensaje sigue formato conventional commits?
- [ ] ¿El scope es correcto?
- [ ] ¿La descripción es clara?
- [ ] ¿Validé que el build pasa?
- [ ] ¿Un solo cambio lógico por commit?
- [ ] ¿Los archivos relacionados están juntos?

**Si alguna respuesta es NO → Revisar antes de commit**
```

---

## 🎯 PATRÓN 5: "When NOT to Use" Sections

### En Mi System Prompt
```xml
<when_not_to_use_past_chats_tools>
**Don't use past chats tools for:**
- Questions that require followup...
- General knowledge questions...
- Current events or news queries...
</when_not_to_use_past_chats_tools>
```

### Aplicación a TU Proyecto

**Agregar a CADA skill**:

#### Ejemplo: spec-driven-dev
```markdown
## When NOT to Use This Skill

❌ **NO usar spec-driven-dev para**:
- Cambios triviales (<30 min de trabajo)
- Fixes urgentes de producción
- Corrección de typos
- Actualizaciones de dependencias
- Cambios cosméticos de formato
- Experimentación rápida (usar branches temporales)

✅ **SÍ usar para**:
- Features nuevas (>2 horas)
- Cambios arquitectónicos
- Refactorings grandes
- Migraciones
- Cualquier cambio que afecte >10 archivos
```

---

## 🎯 PATRÓN 6: Examples Section Abundante

### En Mi System Prompt
```xml
<examples>
**Example 1**: ...
**Example 2**: ...
**Example 3**: ...
[15+ examples provided]
</examples>
```

### Aplicación a TU Proyecto

**Agregar sección de ejemplos a cada skill**:

#### Ejemplo: incremental-correction-methodology
```markdown
## Examples

### Example 1: Decisión Manual vs Script
**Situación**: 50 WARNING de "document isn't included in toctree"
**Análisis**:
- ✅ Patrón idéntico en todos
- ✅ Fix simple (agregar a toctree)
- ⚠️ Pero archivos en diferentes ubicaciones
- ⚠️ Algunos pueden estar deprecated

**Decisión**: Manual para primeros 5, luego evaluar si script es seguro
**Resultado**: Descubrimos que 3/5 estaban deprecated → Manual fue correcto

### Example 2: 7 Protecciones Violadas
**Situación**: Script que corrige 100 errores en batch
**Problemas**:
- ❌ NO dry-run
- ❌ NO un archivo a la vez
- ❌ NO git commit por archivo
- ❌ NO validación de issues disminuyen

**Resultado**: 5 archivos dañados, 2 horas de rollback
**Lección**: Las 7 Protecciones son OBLIGATORIAS, no opcionales

[10+ ejemplos más...]
```

---

## 🎯 PATRÓN 7: Good/Bad Examples

### En Mi System Prompt
```xml
<good_file_sharing_examples>
[Claude finishes running code]
Claude calls present_files tool
[end of output]

These examples are good because:
1. Are succinct
2. Use the present_files tool
</good_file_sharing_examples>
```

### Aplicación a TU Proyecto

#### Ejemplo: work-logger
```markdown
## Good vs Bad Examples

### ✅ GOOD - Work Log Entry
```markdown
# Work Log: 2026-01-31

## Task: Fix Sphinx WARNING in workflow_general.rst

**Changes**:
- Fixed 3 explicit markup warnings (lines 145, 287, 423)
- Added blank lines after directives

**Validation**:
- Before: 230 WARNING
- After: 227 WARNING
- ✅ Confirmed reduction

**Commit**: abc123f
**Duration**: 25 min
```

### ❌ BAD - Work Log Entry
```markdown
Fixed some stuff in workflow file. Took a while.
```

**Why BAD**:
- No specific files mentioned
- No validation metrics
- No commit reference
- No reproducibility
```

---

## 🎯 PATRÓN 8: Critical Reminders Section

### En Mi System Prompt
```xml
<critical_reminders>
- CRITICAL COPYRIGHT RULE - HARD LIMITS: ...
- Claude is not a lawyer...
- Refuse or redirect harmful requests...
</critical_reminders>
```

### Aplicación a TU Proyecto

**Crear en README.md**:

```markdown
## 🚨 Critical Reminders - LEER CADA SESIÓN

### REMINDER 1: Project Discovery PRIMERO
**SIEMPRE** ejecutar project-discovery skill antes de cualquier trabajo.
Claude NO busca `.codex/skills/` automáticamente - es tu responsabilidad.

### REMINDER 2: Las 7 Protecciones NO son Opcionales
Si vas a usar scripts automáticos, las 7 Protecciones son OBLIGATORIAS.
NO hay "bueno, esta vez vamos rápido" - siempre terminan en desastre.

### REMINDER 3: Calidad > Velocidad
La metodología incremental privilegia calidad sobre velocidad.
Si tienes prisa, aún así sigue el proceso - te ahorra tiempo a largo plazo.

### REMINDER 4: Un Commit = Un Cambio Lógico
NO agrupar cambios no relacionados en un commit.
Facilita rollback, code review, y troubleshooting.

### REMINDER 5: Validar ANTES de Commit
Sphinx build DEBE pasar antes de commit.
NO crear commits que rompan el build.
```

---

## 📊 RESUMEN DE MEJORAS PROPUESTAS

| # | Patrón | Prioridad | Impacto | Esfuerzo |
|---|--------|-----------|---------|----------|
| 1 | **Project Discovery Skill** | 🔴 CRÍTICA | ⭐⭐⭐ Alto | 2-3 horas |
| 2 | Decision Frameworks | 🟡 Alta | ⭐⭐ Medio | 1 hora |
| 3 | Trigger Patterns | 🟡 Alta | ⭐⭐ Medio | 1-2 horas |
| 4 | Self-Check Mechanisms | 🟢 Media | ⭐⭐ Medio | 30 min |
| 5 | "When NOT to Use" | 🟢 Media | ⭐ Bajo | 30 min |
| 6 | Examples Section | 🟢 Media | ⭐⭐ Medio | 2-3 horas |
| 7 | Good/Bad Examples | 🟢 Baja | ⭐ Bajo | 1 hora |
| 8 | Critical Reminders | 🟡 Alta | ⭐⭐ Medio | 30 min |

---

## 🎯 Plan de Implementación Sugerido

### Fase 1: Crítico (Hacer AHORA)
1. ✅ Crear `project-discovery` skill
2. ✅ Actualizar README.md con reminders
3. ✅ Agregar decision frameworks a skills existentes

### Fase 2: Alta Prioridad (Esta semana)
4. Agregar trigger patterns a todos los skills
5. Agregar self-checks a skills críticos
6. Documentar "when NOT to use" en cada skill

### Fase 3: Completar (Próximas 2 semanas)
7. Agregar examples sections (10+ por skill)
8. Agregar good/bad examples
9. Validar con uso real

---

## 🔄 Mantenimiento Continuo

**Cada vez que encuentres un problema**:
1. ¿Había un trigger pattern que lo previniera? → Agregar
2. ¿Un decision framework lo hubiera evitado? → Agregar
3. ¿Un self-check lo hubiera detectado? → Agregar
4. ¿Un ejemplo ayudaría a otros? → Agregar

**Los skills son documentación VIVA** - mejoran con experiencia real.

---

**Conclusión**: Tu proyecto YA es robusto. Estos patrones lo harían **excepcional**.
