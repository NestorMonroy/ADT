---
name: project-discovery
description: "Metodología OBLIGATORIA para descubrir y cargar skills del proyecto ANTES de cualquier trabajo. Garantiza que Claude siempre lea las metodologías locales primero, independientemente de su system prompt de Anthropic."
version: 1.1.0
created: 2026-02-01
updated: 2026-02-01
priority: CRITICAL
order: 0
---

# Project Discovery

**Versión**: 1.0.0  
**Ubicación**: `/tmp/ADT/.codex/skills/project-discovery/`  
**Aplicable a**: TODA conversación nueva con el proyecto ADT

---

## ⚠️ REGLA ABSOLUTA

**Este skill se ejecuta PRIMERO, antes que cualquier otro skill.**

**Contexto crítico**: El system prompt de Claude de Anthropic **NO** instruye buscar skills en el proyecto del usuario. Solo conoce skills en `/mnt/skills/`. Por lo tanto, Claude debe ser **explícitamente instruido** a buscar y cargar `.codex/skills/` al inicio de CADA sesión.

---

## Decision Framework: ¿Debo Ejecutar Project-Discovery?

**La respuesta es casi siempre SÍ. Usa este framework para confirmarlo**:

1. **¿Es el inicio de una conversación nueva?**
   → SÍ, ejecutar INMEDIATAMENTE

2. **¿Ya ejecuté project-discovery en esta sesión?**
   → No necesitas repetir (a menos que cambios en skills)

3. **¿El usuario mencionó el proyecto ADT?**
   → SÍ, ejecutar AHORA

4. **¿Estoy trabajando en `/tmp/ADT/`?**
   → SÍ, ejecutar PRIMERO

5. **¿El usuario asume que conozco metodologías del proyecto?**
   → SÍ, ejecutar URGENTE

6. **¿Voy a crear/modificar archivos del proyecto?**
   → SÍ, ejecutar ANTES de empezar

7. **¿Solo respondo preguntas generales sin trabajo en archivos?**
   → QUIZÁS no necesario

8. **¿No estoy seguro?**
   → SÍ, ejecutar (más seguro)

**Regla de oro**: **Cuando dudes → EJECUTA**

**Regla CRÍTICA**: **PRIMERA acción en CADA sesión nueva → project-discovery**

---

## Cuándo Usar Esta Skill

### ✅ SIEMPRE usar cuando:
- Inicia una conversación nueva
- El usuario menciona el proyecto ADT
- El usuario dice "nuestro proyecto"
- El usuario referencia metodologías o convenciones
- Trabajas en `/tmp/ADT/`
- **DEFAULT**: Si dudas, ejecuta project-discovery

### ❌ NO necesitas usar cuando:
- Ya ejecutaste project-discovery en esta sesión
- Ya cargaste los skills del proyecto
- Solo respondes preguntas generales (sin trabajo en archivos)

---

## Filosofía Fundamental

> **Principio central**: Skills del Proyecto > Skills del Sistema
> 
> Las metodologías locales en `.codex/skills/` tienen prioridad sobre cualquier skill genérico de `/mnt/skills/`.

**Por qué es crítico**:
- System prompt de Anthropic puede cambiar sin aviso
- Solo lista skills en `/mnt/skills/` (genéricos)
- NO instruye buscar skills del proyecto
- Claude puede ignorar metodologías locales sin este skill

**Validado en producción**:
- Sesión: 2026-02-01
- Problema: Claude ignoró 11 skills en `.codex/skills/`
- Causa: System prompt no instruye buscar skills locales
- Solución: Este skill garantiza detección automática

---

## Workflow Obligatorio

### PASO 0: Verificar Ubicación (5 segundos)

```bash
cd /tmp/ADT
pwd
```

**Resultado esperado**: `/tmp/ADT`

**Si falla**: Preguntar al usuario dónde está el proyecto

---

### PASO 1: Buscar Skills del Proyecto (10 segundos)

```bash
# Verificar si existe .codex/skills
if [ -d .codex/skills ]; then
    echo "✅ Skills del proyecto encontrados"
    ls -la .codex/skills/
else
    echo "⚠️ No hay .codex/skills/ - usando solo skills del sistema"
fi
```

**Resultado esperado**: Directorio existe con múltiples subdirectorios

**Si NO existe**:
- Informar al usuario
- Preguntar si hay metodologías en otra ubicación
- Continuar con skills del sistema

---

### PASO 2: Leer README Obligatorio (30 segundos)

```bash
view .codex/skills/README.md
```

**Contenido clave a extraer**:
- ✅ Lista de skills activos (con versiones)
- ✅ Mapa de relaciones entre skills
- ✅ Guía de uso por tarea
- ✅ Ubicación del proyecto (`/tmp/ADT`)

**Información crítica**:
- Total de skills disponibles
- Cuáles son skills base (project-context)
- Cuáles son skills metodológicos (incremental-correction, spec-driven-dev)
- Cuáles son skills técnicos (sphinx-expert, validation-suite)

---

### PASO 3: Identificar Skills Relevantes (10 segundos)

**Decision Framework**:

1. **¿La tarea involucra corrección de 100+ issues?**
   → `incremental-correction-methodology`

2. **¿La tarea involucra Sphinx/RST/build errors?**
   → `sphinx-expert`

3. **¿La tarea requiere crear directorios en `.mywork/changes/`?**
   → `changes-directory-management`

4. **¿La tarea requiere commits?**
   → `commit-helper`

5. **¿La tarea requiere documentar trabajo completado?**
   → `work-logger`

6. **¿La tarea requiere validación antes de commit?**
   → `validation-suite`

7. **¿La tarea involucra traducción?**
   → `translation-workflow`

8. **¿La tarea es un cambio complejo (>2 horas)?**
   → `spec-driven-dev`

9. **¿Siempre?**
   → `project-context` (base para entender ADT)

**Regla de oro**: Si dudas, carga `project-context` + el skill que parezca más relevante.

---

### PASO 4: Cargar Skills Relevantes (variable)

```bash
# Ejemplo para tarea de corrección de errores de Sphinx
view .codex/skills/incremental-correction-methodology/SKILL.md
view .codex/skills/sphinx-expert/SKILL.md
view .codex/skills/validation-suite/SKILL.md
view .codex/skills/project-context/SKILL.md
```

**Cuántos skills cargar**:
- **Mínimo**: 1 (project-context)
- **Típico**: 2-3 skills
- **Máximo**: 5 skills (no sobrecargues)

**Orden de lectura**:
1. `project-context` PRIMERO (siempre)
2. Skills metodológicos (incremental, spec-driven)
3. Skills técnicos (sphinx, validation)
4. Skills de soporte (commit-helper, work-logger)

---

### PASO 5: Confirmar al Usuario (5 segundos)

**Template de confirmación**:

```
✅ He cargado los siguientes skills del proyecto ADT:
- project-context (v1.0.0)
- incremental-correction-methodology (v1.3.0)
- sphinx-expert (v1.6.0)

Estoy listo para trabajar siguiendo nuestra metodología.
```

**Beneficios de confirmar**:
- Usuario sabe qué metodologías se están usando
- Usuario puede corregir si falta algún skill
- Transparencia en el proceso
- Confianza en que se seguirán las reglas del proyecto

---

## Trigger Patterns

### Señales Explícitas (100% seguro)

- Usuario dice: "Lee primero los skills del proyecto"
- Usuario dice: "Sigue nuestra metodología"
- Usuario dice: "Estamos en `/tmp/ADT/`"
- Usuario dice: "Usa las convenciones de ADT"
- Usuario dice: "Revisa `.codex/skills/`"

### Señales Implícitas (muy probable)

- Usuario menciona "nuestro proyecto"
- Usuario menciona "nuestra metodología"
- Usuario menciona "según nuestras reglas"
- Usuario menciona "ADT" sin contexto
- Usuario sube archivo de `/tmp/ADT/`
- Usuario menciona arc42, Sphinx, reStructuredText

### Trigger Words Clave

**Palabras que indican proyecto local**:
- "nuestro", "nuestra", "nuestros"
- "proyecto", "metodología", "convención"
- "ADT", "arc42", "transformación"
- ".codex", "skills", "README"

**Acciones que requieren contexto**:
- "corrige errores de Sphinx"
- "traduce esta sección"
- "crea un plan para..."
- "valida el build"
- "haz commit de..."

---

## Self-Check Before Starting ANY Work

Antes de hacer **CUALQUIER** trabajo en el proyecto, verifica:

**Checklist Obligatoria**:
- [ ] ¿Estoy en `/tmp/ADT/`?
- [ ] ¿Leí `.codex/skills/README.md`?
- [ ] ¿Identifiqué los skills relevantes para esta tarea?
- [ ] ¿Cargué al menos 1 skill del proyecto?
- [ ] ¿Entiendo el contexto metodológico de ADT?
- [ ] ¿Confirmé al usuario qué skills cargué?

**Si alguna respuesta es NO → STOP y ejecuta project-discovery COMPLETO**

---

## Antipatrones - Qué NO Hacer

### ❌ ANTIPATRÓN 1: Asumir que no hay skills locales
**Problema**: Ignorar `.codex/skills/` sin verificar

**Ejemplo real (2026-02-01)**:
- Claude trabajó durante horas en el proyecto
- Nunca buscó `.codex/skills/`
- Ignoró 11 skills documentados
- Violó metodologías establecidas

**Solución**: SIEMPRE ejecutar PASO 1 (buscar skills)

### ❌ ANTIPATRÓN 2: Ir directo a /mnt/skills
**Problema**: Usar skills genéricos sin buscar específicos

**Por qué es malo**:
- Skills de `/mnt/skills/` son genéricos
- No conocen las reglas del proyecto ADT
- Pueden contradecir metodologías locales

**Solución**: Buscar `.codex/skills/` PRIMERO

### ❌ ANTIPATRÓN 3: Empezar a trabajar sin leer README
**Problema**: No saber qué skills existen

**Consecuencia**:
- No sabes qué metodologías hay
- No sabes qué versiones usar
- No sabes cómo relacionan los skills

**Solución**: PASO 2 (leer README) es OBLIGATORIO

### ❌ ANTIPATRÓN 4: Seguir convenciones genéricas
**Problema**: Usar "best practices" genéricas cuando hay específicas

**Ejemplo**:
- Convención genérica: "usa CamelCase para directorios"
- Convención de ADT: "usa timestamp: YYYYMMDD-HHMMSS"

**Solución**: Skills del proyecto > Convenciones genéricas

### ❌ ANTIPATRÓN 5: No confirmar qué skills cargaste
**Problema**: Usuario no sabe qué metodología estás siguiendo

**Consecuencia**:
- Falta de transparencia
- Usuario no puede corregir
- Confusión sobre proceso

**Solución**: PASO 5 (confirmar) es OBLIGATORIO

---

## Beneficios

### ✅ Garantiza Consistencia
- Misma metodología en cada sesión
- Independiente del system prompt de Anthropic
- Independiente de la versión de Claude

### ✅ Reduce Errores
- No más "olvidar" buscar skills locales
- No más usar convenciones incorrectas
- No más ignorar metodologías documentadas

### ✅ Mejora Transparencia
- Usuario sabe qué skills se están usando
- Usuario puede verificar el proceso
- Usuario puede corregir si es necesario

### ✅ Independencia del Proveedor
- No depende de que Anthropic mantenga su system prompt
- Funciona aunque Anthropic cambie instrucciones
- Portátil a otros LLMs que puedan leer archivos

### ✅ Reproducibilidad
- Mismo flujo de discovery en cada sesión
- Documentado y versionado
- Auditable y mejorable

---

## Integración con README.md

Al crear este skill, también se debe actualizar `.codex/skills/README.md`:

```markdown
## ⚠️ SKILL CRÍTICO - EJECUTAR PRIMERO

**project-discovery** (v1.0.0) es el skill #0
- **Order**: 0 (primero, antes que todo)
- **Priority**: CRITICAL
- **Cuándo**: TODA conversación nueva

DEBE ejecutarse ANTES que cualquier otro skill.

Sin este skill, Claude puede:
- ❌ Ignorar metodologías del proyecto
- ❌ Usar convenciones genéricas incorrectas
- ❌ No cargar skills relevantes
```

---

## Ejemplos de Uso

### Example 1: Conversación Nueva - Corrección de Errores

**Usuario**: "Ayúdame a corregir los errores de build de Sphinx"

**Claude (internamente - ejecuta project-discovery)**:

```
PASO 0: ✅ Verifico ubicación → /tmp/ADT
PASO 1: ✅ Busco .codex/skills → Existe, 11 subdirectorios
PASO 2: ✅ Leo README.md
        - 11 skills activos
        - project-context es base
        - incremental-correction para 100+ issues
        - sphinx-expert para errores de Sphinx
PASO 3: ✅ Identifico skills relevantes:
        - project-context (siempre)
        - sphinx-expert (errores de Sphinx)
        - incremental-correction (probablemente hay 100+ errores)
        - validation-suite (validar fixes)
PASO 4: ✅ Cargo 4 skills
PASO 5: ✅ Confirmo al usuario
```

**Claude (respuesta al usuario)**:

```
✅ He cargado los siguientes skills del proyecto ADT:
- project-context (v1.0.0)
- sphinx-expert (v1.6.0)  
- incremental-correction-methodology (v1.3.0)
- validation-suite (v1.0.0)

Primero, vamos a analizar los errores de build siguiendo nuestra 
metodología incremental. ¿Ya tienes el output del build?
```

---

### Example 2: Usuario Menciona Implícitamente el Proyecto

**Usuario**: "Según nuestra metodología, ¿cómo debo organizar este trabajo?"

**Claude (internamente)**:

```
Trigger detectado: "nuestra metodología"
→ Ejecutar project-discovery

PASO 0-5: [ejecuta workflow completo]
```

**Claude (respuesta)**:

```
✅ He cargado los skills del proyecto ADT:
- project-context (v1.0.0)
- changes-directory-management (v1.0.0)
- spec-driven-dev (v1.1.0)

Según nuestra metodología, para organizar el trabajo debes:
1. Crear un directorio en .mywork/changes/ con timestamp
2. Si es un cambio complejo (>2h), usar spec-driven-dev
3. Documentar en PLAN.md dentro del directorio

¿El cambio que planeas es complejo (>2 horas)?
```

---

### Example 3: Fallo - Claude No Ejecutó Project Discovery

**Usuario**: "Corrige estos 100 WARNING de Sphinx"

**Claude (SIN project-discovery - INCORRECTO)**:

```
Claro, voy a crear un script para corregir automáticamente...
[Usa convenciones genéricas]
[No sigue metodología incremental]
[Viola las 7 Protecciones]
```

**Resultado**: 5 archivos dañados, 2 horas de rollback

---

**Claude (CON project-discovery - CORRECTO)**:

```
✅ He cargado: incremental-correction-methodology (v1.3.0)

Según nuestra metodología para 100+ issues:

FASE 0: Preparación (15-20 min) - OBLIGATORIA
- Leer methodology skill
- Leer sphinx-expert skill
- Entender el contexto

FASE 1: Análisis inicial (30 min) - OBLIGATORIO
- Build completo
- Categorización
- Priorización

¿Ya hiciste el análisis inicial o empezamos con eso?
```

**Resultado**: Proceso controlado, 0 errores introducidos

---

## When NOT to Use This Skill

### ❌ NO usar project-discovery cuando:

1. **Ya lo ejecutaste en esta conversación**
   - No es necesario repetirlo
   - Los skills ya están cargados en contexto

2. **Solo respondes preguntas generales**
   - "¿Qué es Sphinx?"
   - "¿Cómo funciona RST?"
   - No se requiere trabajar en archivos

3. **El usuario explícitamente NO quiere usar metodologías**
   - Usuario dice "ignora las reglas del proyecto"
   - Usuario dice "usa tu propio criterio"
   - (Raro, pero respetar si ocurre)

### ✅ SÍ usar cuando haya duda

**Regla de oro**: Si no estás 100% seguro si ejecutar project-discovery → **Ejecutarlo**

Es mejor "descubrir" dos veces que no descubrir ninguna.

---

## Versionamiento

### v1.0.0 (2026-02-01)
- ✅ Versión inicial
- ✅ Workflow de 5 pasos (0-5)
- ✅ Decision framework para identificar skills
- ✅ Trigger patterns documentados
- ✅ Antipatrones documentados
- ✅ Self-check checklist
- ✅ Examples de uso

### Futuras Versiones

**v1.1.0** (planeada):
- Auto-detección de ubicación del proyecto
- Caché de skills cargados en sesión
- Sugerencias de skills basadas en contexto

**v1.2.0** (planeada):
- Validación de versiones de skills
- Warning si skills están desactualizados
- Integración con work-logger

---

## Critical Reminders

### 🚨 REMINDER 1: SIEMPRE Primero
**project-discovery NO es opcional en conversaciones nuevas**

Incluso si el usuario no lo menciona explícitamente, Claude debe:
1. Detectar que está en un proyecto (ADT)
2. Ejecutar project-discovery automáticamente
3. Cargar skills relevantes

### 🚨 REMINDER 2: System Prompt NO es Suficiente
El system prompt de Claude de Anthropic:
- ❌ NO menciona buscar skills de proyecto
- ❌ Solo lista skills en `/mnt/skills/`
- ❌ Puede cambiar sin aviso

**Por lo tanto**: Este skill es la ÚNICA garantía de que las metodologías del proyecto se cargarán.

### 🚨 REMINDER 3: Transparencia SIEMPRE
SIEMPRE confirma al usuario (PASO 5):
- Qué skills cargaste
- Qué versiones
- Que estás listo para trabajar

Sin confirmación, el usuario no sabe si seguiste el proceso.

---

## Métricas de Éxito

### ¿Cómo saber si project-discovery funciona?

**Indicadores positivos**:
- ✅ Claude carga skills del proyecto en cada sesión
- ✅ Claude sigue metodologías documentadas
- ✅ Claude usa convenciones correctas del proyecto
- ✅ 0 violaciones de antipatrones (como ignorar `.codex/skills/`)

**Indicadores de problema**:
- ❌ Claude usa convenciones genéricas
- ❌ Claude no menciona skills cargados
- ❌ Claude no sigue metodología incremental
- ❌ Claude crea archivos con nombres incorrectos

**Métrica clave**:
> **Tasa de discovery**: % de sesiones donde Claude ejecuta project-discovery automáticamente
> 
> **Objetivo**: 100% en sesiones que involucran trabajo en el proyecto

---

## Conclusión

**project-discovery** es el skill más crítico del proyecto ADT porque:

1. **Resuelve un problema real**: Claude ignoró `.codex/skills/` en sesión 2026-02-01
2. **Independiente de Anthropic**: No depende del system prompt
3. **Garantiza consistencia**: Mismo proceso en cada sesión
4. **Transparente**: Usuario sabe qué se está usando
5. **Reproducible**: Documentado y versionado

**Sin este skill**: Claude puede trabajar sin conocer las metodologías del proyecto.

**Con este skill**: Claude SIEMPRE carga las metodologías primero.

---

**Última actualización**: 2026-02-01  
**Mantenedor**: ADT Team  
**Ubicación del Proyecto**: `/tmp/ADT`

---

## Changelog

### v1.1.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y decision-making**:

✅ **Decision Framework** - ¿Debo Ejecutar Project-Discovery?
- 8 preguntas para decidir si ejecutar
- Regla de oro: "Cuando dudes → EJECUTA"
- Regla CRÍTICA: "PRIMERA acción en CADA sesión nueva"
- Clarifica que casi siempre la respuesta es SÍ

**Líneas agregadas**: ~35 líneas

**Beneficio principal**:
- Claude entiende que debe ejecutar automáticamente
- NO espera señal del usuario
- Primera acción en toda sesión nueva

**Nota**: Trigger Patterns y Self-Checks ya existían en v1.0.0

### v1.0.0 - 2026-02-01
- Versión inicial
- Metodología OBLIGATORIA de inicio de sesión
- Workflow de discovery completo
- Trigger Patterns documentados
- Self-Checks implementados
