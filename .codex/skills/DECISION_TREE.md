# Skills ADT - Decision Tree 🎯

**Guía rápida**: ¿Qué skill necesito para mi tarea?

**Última actualización**: 2026-02-01

---

## 🚨 PASO 0: SIEMPRE PRIMERO

**ANTES de cualquier trabajo**:

```bash
view /tmp/ADT/.codex/skills/project-discovery/SKILL.md
```

**project-discovery** es OBLIGATORIO al inicio de TODA conversación.

---

## 📋 Quick Start: ¿Qué Skill Para Qué Tarea?

### 🔴 Por Tipo de Tarea

#### Corrección de Errores/Warnings

**¿Cuántos issues tienes?**

```
100+ issues idénticos
│
├─→ ¿Son errores Sphinx/RST? → sphinx-expert (identificar tipo)
│   └─→ Luego: incremental-correction-methodology (estrategia)
│
├─→ ¿Son otros errores? → incremental-correction-methodology (directo)
│
└─→ Necesitas: validation-suite (validar progreso)
```

**<100 issues o variados**:
```
Pocos issues / errores variados
│
├─→ ¿Sphinx/RST? → sphinx-expert
├─→ ¿Build? → validation-suite
└─→ ¿Script? → bash-production-scripting
```

---

#### Documentación de Trabajo

**¿Qué necesitas documentar?**

```
Crear directorio trabajo
│
└─→ changes-directory-management
    → Crear .mywork/changes/YYYYMMDD-HHMMSS-nombre/

Documentar sesión completada
│
└─→ work-logger
    → Crear .mywork/work-logs/YYYY-MM-DD-HH-MM-titulo.md

Hacer commit
│
└─→ commit-helper
    → Formato: tipo(scope): descripción
```

---

#### Desarrollo/Features

**¿Qué tipo de desarrollo?**

```
Feature compleja (>2 horas)
│
└─→ spec-driven-dev
    → 4 fases: Requirements, Design, Tasks, Implementation

Traducción de contenido
│
└─→ translation-workflow
    → Modos: alta_fidelidad, marcado_visual, enriquecimiento

Contexto del proyecto
│
└─→ project-context
    → Metodología ADT, frameworks, terminología
```

---

#### Gestión

**¿Qué necesitas gestionar?**

```
Crear/actualizar skill
│
└─→ skills-management
    → Estructura, versionamiento, documentación

Scripts de producción
│
└─→ bash-production-scripting
    → Best practices cross-platform

Inicio de sesión
│
└─→ project-discovery ← SIEMPRE PRIMERO
    → Cargar skills del proyecto
```

---

## 🎯 Por Señales del Usuario

### Señales Textuales

| Usuario dice... | Skill a usar |
|----------------|--------------|
| "tengo muchos errores" | incremental-correction-methodology |
| "el build de Sphinx falla" | sphinx-expert |
| "traduce esto" / "convierte a RST" | translation-workflow |
| "vamos a implementar X" | spec-driven-dev |
| "documenta este trabajo" | work-logger |
| "haz commit" | commit-helper |
| "crea directorio" | changes-directory-management |
| "necesito script" | bash-production-scripting |
| "¿qué es ADT?" | project-context |
| "crea skill" | skills-management |
| "valida el build" | validation-suite |

### Señales Contextuales

| Contexto... | Skill a considerar |
|------------|-------------------|
| Nuevo en el proyecto | project-context + project-discovery |
| Trabajo complejo inicia | changes-directory-management → spec-driven-dev |
| Trabajo termina | work-logger → commit-helper |
| Build roto | sphinx-expert + validation-suite |
| Muchos issues repetitivos | incremental-correction-methodology |
| Transformación documental | translation-workflow |

---

## 🗺️ Mapa de Relaciones Entre Skills

### Flujo Típico de Trabajo

```
┌──────────────────────┐
│  project-discovery   │ ← INICIO (SIEMPRE)
│     (OBLIGATORIO)    │
└──────────┬───────────┘
           │
           ├─→ project-context ─────────────→ Entender metodología
           │
           ├─→ Trabajo simple (<30 min)
           │   └─→ Hacer directamente
           │       └─→ commit-helper (si commit)
           │
           └─→ Trabajo complejo (>30 min)
               └─→ changes-directory-management
                   └─→ Crear .mywork/changes/TIMESTAMP-nombre/
                       │
                       ├─→ spec-driven-dev (si >2h y estructurado)
                       │   └─→ Requirements → Design → Tasks → Implementation
                       │
                       ├─→ incremental-correction-methodology (si 100+ issues)
                       │   ├─→ sphinx-expert (si Sphinx/RST)
                       │   ├─→ validation-suite (validar)
                       │   └─→ bash-production-scripting (si scripts)
                       │
                       ├─→ translation-workflow (si traducción)
                       │   └─→ project-context (framework/terminología)
                       │
                       └─→ Al terminar:
                           ├─→ commit-helper (commits)
                           └─→ work-logger (documentar)
```

### Relaciones de Dependencia

```
project-discovery (base)
    ├─→ Todos los demás skills dependen de este
    └─→ EJECUTAR PRIMERO en TODA sesión

incremental-correction-methodology
    ├─→ Usa: validation-suite (validar progreso)
    ├─→ Usa: sphinx-expert (si errores Sphinx)
    ├─→ Usa: bash-production-scripting (si scripts)
    └─→ Usa: commit-helper (commits incrementales)

spec-driven-dev
    ├─→ Usa: changes-directory-management (crear directorio)
    ├─→ Usa: commit-helper (commits por fase)
    └─→ Usa: work-logger (documentar al final)

translation-workflow
    ├─→ Usa: project-context (entender frameworks)
    └─→ Usa: validation-suite (validar resultado)

changes-directory-management
    └─→ Usado por: spec-driven-dev, incremental-correction, etc.

work-logger
    └─→ Se usa al FINAL de cualquier trabajo significativo

commit-helper
    └─→ Se usa DURANTE y AL FINAL de cualquier trabajo

validation-suite
    └─→ Se usa para VALIDAR resultados de cualquier cambio
```

---

## 🔍 Casos de Uso Específicos

### Caso 1: "Corregir 230 WARNING de Sphinx"

**Workflow**:
1. ✅ `project-discovery` (obligatorio primero)
2. ✅ `changes-directory-management` (crear directorio trabajo)
3. ✅ `sphinx-expert` (entender tipos de WARNING)
4. ✅ `incremental-correction-methodology` (planificar corrección)
5. ✅ `validation-suite` (validar progreso)
6. ✅ `commit-helper` (commits incrementales)
7. ✅ `work-logger` (documentar al final)

### Caso 2: "Traducir sección 10 de arc42"

**Workflow**:
1. ✅ `project-discovery` (obligatorio primero)
2. ✅ `project-context` (entender arc42 y modos)
3. ✅ `translation-workflow` (ejecutar traducción)
4. ✅ `validation-suite` (validar build pasa)
5. ✅ `commit-helper` (commit con metadata)
6. ✅ `work-logger` (documentar decisiones)

### Caso 3: "Implementar feature nueva de validación"

**Workflow**:
1. ✅ `project-discovery` (obligatorio primero)
2. ✅ `changes-directory-management` (crear directorio)
3. ✅ `spec-driven-dev` (planificar en 4 fases)
   - Requirements
   - Design
   - Tasks
   - Implementation
4. ✅ `bash-production-scripting` (si scripts necesarios)
5. ✅ `validation-suite` (validar funciona)
6. ✅ `commit-helper` (commits por tarea)
7. ✅ `work-logger` (documentar al final)

### Caso 4: "Crear skill nuevo"

**Workflow**:
1. ✅ `project-discovery` (obligatorio primero)
2. ✅ `skills-management` (entender estructura)
3. ✅ `project-context` (opcional, para contexto)
4. ✅ Crear SKILL.md siguiendo template
5. ✅ `commit-helper` (commit del skill)
6. ✅ Actualizar README.md de skills

---

## 🎓 Reglas de Decisión Rápida

### ¿Cuándo Usar Qué?

**1. Siempre PRIMERO**:
```
project-discovery (OBLIGATORIO en toda nueva sesión)
```

**2. Si trabajo >30 minutos**:
```
changes-directory-management → Crear directorio
```

**3. Si >100 issues repetitivos**:
```
incremental-correction-methodology → Estrategia corrección
```

**4. Si errores Sphinx/RST**:
```
sphinx-expert → Identificar tipo de error
```

**5. Si feature >2 horas**:
```
spec-driven-dev → Planificación 4 fases
```

**6. Si traducción/transformación**:
```
translation-workflow → Modos y proceso
```

**7. Si scripts automáticos**:
```
bash-production-scripting → Best practices
```

**8. Siempre VALIDAR**:
```
validation-suite → Build pasa, issues disminuyen
```

**9. Siempre al TERMINAR**:
```
commit-helper → Commits
work-logger → Documentación
```

---

## ⚠️ Anti-Patrones

### NO Hacer

❌ **Empezar sin project-discovery**
- Consecuencia: Ignorar metodologías del proyecto

❌ **Crear archivos en `.mywork/` raíz**
- Correcto: Crear directorio en `.mywork/changes/`

❌ **Saltarse validation-suite**
- Consecuencia: Commits que rompen build

❌ **No documentar con work-logger**
- Consecuencia: Pérdida de conocimiento

❌ **Corregir 100+ issues sin incremental-correction**
- Consecuencia: Regresiones, pérdida de tiempo

❌ **Scripts sin bash-production-scripting**
- Consecuencia: Scripts frágiles, no portables

---

## 📊 Matriz de Decisión

| ¿Qué necesito? | Skill | Prioridad | Cuándo |
|----------------|-------|-----------|---------|
| Cargar proyecto | project-discovery | 🔴 CRÍTICA | Inicio sesión |
| Entender ADT | project-context | 🟡 Alta | Onboarding |
| Crear directorio | changes-directory-management | 🟡 Alta | Trabajo >30min |
| Planificar feature | spec-driven-dev | 🟡 Alta | Feature >2h |
| Corregir 100+ issues | incremental-correction | 🔴 CRÍTICA | Muchos issues |
| Fix Sphinx | sphinx-expert | 🟡 Alta | Errores Sphinx |
| Traducir | translation-workflow | 🟡 Alta | Transformación |
| Script robusto | bash-production-scripting | 🟢 Media | Scripts |
| Validar | validation-suite | 🔴 CRÍTICA | Siempre |
| Commit | commit-helper | 🟡 Alta | Siempre |
| Documentar | work-logger | 🟡 Alta | Al terminar |
| Crear skill | skills-management | 🟢 Media | Nuevo skill |

---

## 🔗 Links Rápidos

- [README principal](./README.md)
- [project-discovery](./project-discovery/SKILL.md) ← LEER PRIMERO
- [Todos los skills](./README.md#-skills-activas)
- [Critical Reminders](./README.md#-critical-reminders---leer-cada-sesión)

---

**Versión**: 1.0.0  
**Creado**: 2026-02-01  
**Mantenedor**: ADT Team  
**Ubicación del Proyecto**: `/tmp/ADT`
