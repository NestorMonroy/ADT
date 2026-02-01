# Skills ADT - Decision Tree

**Última actualización**: 2026-02-01  
**Proyecto**: `/tmp/ADT`

---

## 🎯 Quick Start: ¿Qué Skill Necesito?

### Por Tipo de Tarea

#### 📝 Corrección de Errores/Warnings

```
¿100+ issues? → incremental-correction-methodology
¿Errores Sphinx/RST específicos? → sphinx-expert
¿Validar build antes de commit? → validation-suite
```

#### 📚 Documentación de Trabajo

```
¿Crear directorio de trabajo? → changes-directory-management
¿Documentar sesión completada? → work-logger
¿Hacer commit con mensaje? → commit-helper
```

#### 🔧 Desarrollo/Features

```
¿Feature compleja (>2h)? → spec-driven-dev
¿Traducir documento? → translation-workflow
¿Entender metodología ADT? → project-context
```

#### ⚙️ Gestión

```
¿Crear/actualizar skill? → skills-management
¿Scripts de producción? → bash-production-scripting
¿Inicio de sesión? → project-discovery (SIEMPRE PRIMERO)
```

---

## 🎤 Por Señales del Usuario

### Usuario dice...

| Frase del Usuario | Skill a Usar |
|-------------------|--------------|
| "tengo muchos errores/warnings" | `incremental-correction-methodology` |
| "traduce este documento" | `translation-workflow` |
| "documenta este trabajo" | `work-logger` |
| "vamos a implementar X" | `spec-driven-dev` |
| "haz commit" | `commit-helper` |
| "necesito script robusto" | `bash-production-scripting` |
| "error en Sphinx/RST" | `sphinx-expert` |
| "valida el build" | `validation-suite` |
| "¿qué es ADT?" | `project-context` |
| "crear nueva skill" | `skills-management` |
| "¿dónde documento mi trabajo?" | `changes-directory-management` |

### Contexto indica...

| Contexto | Skill a Usar |
|----------|--------------|
| Nueva sesión iniciada | `project-discovery` ⚠️ OBLIGATORIO |
| Trabajo >30 min empezando | `changes-directory-management` |
| Build tiene WARNING/ERROR | `sphinx-expert` + `validation-suite` |
| Múltiples archivos a corregir | `incremental-correction-methodology` |
| Trabajo multi-fase complejo | `spec-driven-dev` |
| Usuario confundido sobre estructura | `project-context` |

---

## 🗺️ Mapa de Relaciones entre Skills

### Flujo Estándar de Sesión

```
┌─────────────────────────────────────────────┐
│ 🚨 SESIÓN NUEVA                             │
│ → project-discovery (OBLIGATORIO PRIMERO)  │
└──────────────────┬──────────────────────────┘
                   │
                   ├─→ Lee README.md
                   ├─→ Identifica skills del proyecto
                   ├─→ Carga metodologías locales
                   │
                   ▼
┌────────────────────────────────────────────┐
│ TRABAJO SIMPLE (<30 min)                   │
└──────────────┬─────────────────────────────┘
               │
               ├─→ project-context (si necesita orientación)
               ├─→ sphinx-expert (si error técnico)
               ├─→ validation-suite (validar)
               ├─→ commit-helper (commit)
               │
               ▼
             [FIN]

┌────────────────────────────────────────────┐
│ TRABAJO COMPLEJO (>30 min)                 │
└──────────────┬─────────────────────────────┘
               │
               ▼
    changes-directory-management
               │
               ├─→ Crear directorio con timestamp
               ├─→ Trabajar DENTRO del directorio
               │
               ▼
         ┌────────────────┐
         │ ¿Muy complejo? │
         └───┬────────┬───┘
             │        │
            SÍ       NO
             │        │
             ▼        ▼
     spec-driven-dev  [Skills específicos]
     (4 fases)        │
             │        │
             ▼        ▼
        [Skills según fase]
             │
             ├─→ translation-workflow (si traducir)
             ├─→ sphinx-expert (si RST/Sphinx)
             ├─→ incremental-correction (si 100+ issues)
             ├─→ bash-production (si scripts)
             │
             ▼
       validation-suite
             │
             ▼
        work-logger
             │
             ▼
       commit-helper
             │
             ▼
           [FIN]
```

---

## 🔀 Relaciones y Dependencias

### Skills Base (Fundamentales)

```
project-discovery (Nivel 0 - CRÍTICO)
    │
    └─→ DEBE ejecutarse PRIMERO en TODA sesión
        Sin esto, Claude no conoce las metodologías

project-context (Nivel 1 - Referencia)
    │
    ├─→ Usado por: translation-workflow
    ├─→ Usado por: sphinx-expert
    └─→ Usado por: spec-driven-dev
```

### Skills Metodológicos (Procesos)

```
spec-driven-dev (Complejo)
    │
    ├─→ Usa: changes-directory-management
    ├─→ Usa: project-context
    └─→ Puede usar CUALQUIER skill según fase

incremental-correction-methodology (100+ issues)
    │
    ├─→ Usa: sphinx-expert (para issues técnicos)
    ├─→ Usa: validation-suite (validar progreso)
    ├─→ Usa: bash-production (si scripts automáticos)
    └─→ Usa: commit-helper (un archivo = un commit)
```

### Skills Operacionales (Ejecución)

```
translation-workflow
    │
    ├─→ Requiere: project-context (metodología ADT)
    ├─→ Usa: validation-suite (validar resultado)
    └─→ Termina con: work-logger + commit-helper

sphinx-expert
    │
    ├─→ Independiente (experto técnico)
    └─→ Termina con: validation-suite + commit-helper

bash-production-scripting
    │
    └─→ Independiente (best practices scripting)
```

### Skills de Soporte (Documentación/Gestión)

```
changes-directory-management
    │
    ├─→ Usado por: spec-driven-dev
    └─→ Diferencia con work-logger:
        - changes: trabajo EN PROGRESO
        - work-logger: trabajo COMPLETADO

work-logger
    │
    └─→ Se ejecuta DESPUÉS de completar trabajo
        Documenta QUÉ se hizo y POR QUÉ

commit-helper
    │
    └─→ Se ejecuta AL FINAL del workflow
        Genera mensaje conventional commit

validation-suite
    │
    └─→ Se ejecuta ANTES de commit
        Garantiza calidad del build

skills-management
    │
    └─→ Meta-skill (para gestionar otros skills)
        Usa: work-logger para documentar cambios
```

---

## 🎯 Workflows Típicos con Ejemplos

### Workflow 1: Traducir Documento arc42

```
Usuario: "Traduce la sección 10 de arc42 sobre Quality Requirements"

Claude ejecuta:
1. ✅ project-discovery (si nueva sesión)
2. ✅ project-context (entender metodología ADT)
3. ✅ translation-workflow
   - Modo: alta_fidelidad (documentación técnica)
   - Framework: arc42
   - Output: RST con metadata
4. ✅ validation-suite (build Sphinx)
5. ✅ work-logger (documentar traducción)
6. ✅ commit-helper
   - Mensaje: "feat(traduccion): add arc42 section 10 quality requirements"
```

**Tiempo**: 1-2 horas  
**Skills usados**: 5 (sin contar project-discovery)

---

### Workflow 2: Corregir 230 Warnings de Sphinx

```
Usuario: "Tengo 230 warnings en el build de Sphinx, ayúdame a corregirlos"

Claude ejecuta:
1. ✅ project-discovery (si nueva sesión)
2. ✅ changes-directory-management
   - Crear: .mywork/changes/20260201-143000-correccion-230-warnings/
3. ✅ incremental-correction-methodology
   - FASE 1: Análisis (30 min)
     - Categorizar 230 warnings
     - Priorizar por impacto
   - FASE 2: Estrategia
     - Decidir: manual vs script
     - Si script → aplicar 8 Protecciones
   - FASE 3: Ejecución
     - Usar sphinx-expert para issues técnicos
     - validation-suite después de cada categoría
   - FASE 4: Verificación
     - Confirmar 230 → 0 warnings
4. ✅ work-logger
   - Documentar: estrategia, progreso, decisiones
5. ✅ commit-helper (múltiples commits)
   - Un archivo = un commit

Después de CADA archivo:
  → sphinx-expert (analizar issue)
  → fix manual o script
  → validation-suite (confirmar disminución)
  → commit-helper (commit atómico)
```

**Tiempo**: 4-6 horas  
**Skills usados**: 6 (proceso incremental)

---

### Workflow 3: Implementar Feature Nueva Compleja

```
Usuario: "Vamos a implementar un sistema de versionamiento automático para documentos"

Claude ejecuta:
1. ✅ project-discovery (si nueva sesión)
2. ✅ changes-directory-management
   - Crear: .mywork/changes/20260201-150000-versionamiento-docs/
3. ✅ spec-driven-dev (feature >2 horas)
   
   FASE 1 - Requirements:
   - ✅ project-context (entender restricciones ADT)
   - Documento: YYYY-MM-DD-HH-MM-requirements-versionamiento.md
   
   FASE 2 - Design:
   - Documento: YYYY-MM-DD-HH-MM-design-versionamiento.md
   - Decisiones arquitectónicas
   
   FASE 3 - Tasks:
   - Documento: YYYY-MM-DD-HH-MM-tasks-versionamiento.md
   - Descomponer en tareas atómicas
   
   FASE 4 - Implementation:
   - ✅ bash-production-scripting (si scripts necesarios)
   - ✅ sphinx-expert (cambios en docs)
   - ✅ validation-suite (después de cada tarea)
   - ✅ commit-helper (por tarea completada)

4. ✅ work-logger (al finalizar proyecto)
5. ✅ Final validation-suite (build completo)
```

**Tiempo**: 1-2 días  
**Skills usados**: 7-8 (metodología completa)

---

### Workflow 4: Error Urgente en Build

```
Usuario: "ERROR: circular toctree reference, el build está roto"

Claude ejecuta:
1. ✅ project-discovery (si nueva sesión)
2. ✅ sphinx-expert (INMEDIATO - es experto)
   - Analizar error
   - Identificar archivos involucrados
   - Proponer solución
3. ✅ Implementar fix
4. ✅ validation-suite (confirmar build pasa)
5. ✅ commit-helper
   - Mensaje: "fix(sphinx): resolve circular toctree reference in X"

NO usar: spec-driven-dev (es urgente, no planificar)
NO usar: incremental-correction (es UN error específico)
SÍ usar: work-logger solo si fue complejo
```

**Tiempo**: 15-30 minutos  
**Skills usados**: 3-4 (hotfix rápido)

---

### Workflow 5: Documentar Sesión de Trabajo

```
Usuario: "Documenta todo lo que hicimos hoy"

Claude ejecuta:
1. ✅ work-logger
   - Crear: .mywork/work-logs/YYYY-MM-DD-HH-MM-titulo-trabajo.md
   - Secciones:
     - Resumen ejecutivo
     - Trabajo realizado (paso a paso)
     - Archivos afectados
     - Decisiones tomadas
     - Aprendizajes
   - Tags apropiados (#traduccion, #sphinx, etc.)
2. ✅ commit-helper
   - Mensaje: "docs(work-log): documentar [trabajo realizado]"
```

**Tiempo**: 10-15 minutos  
**Skills usados**: 2 (documentación simple)

---

### Workflow 6: Crear Nueva Skill

```
Usuario: "Necesito crear una skill para gestión de imágenes"

Claude ejecuta:
1. ✅ project-discovery (si nueva sesión)
2. ✅ changes-directory-management
   - Crear: .mywork/changes/20260201-160000-nueva-skill-imagenes/
3. ✅ skills-management
   - Seguir estructura estándar SKILL.md
   - Frontmatter YAML
   - Secciones obligatorias:
     - Cuando usar
     - Decision Framework
     - Trigger Patterns
     - Self-Checks
   - Versionamiento: v1.0.0
   - Changelog
4. ✅ Actualizar .codex/skills/README.md
   - Agregar skill a lista
   - Actualizar mapa de relaciones
5. ✅ work-logger
   - Documentar creación de skill
6. ✅ commit-helper
   - Mensaje: "feat(skills): add image-management skill v1.0.0"
```

**Tiempo**: 1-2 horas  
**Skills usados**: 4 (gestión de skills)

---

## ⚠️ Anti-Patrones Comunes

### ❌ Anti-Patrón 1: Saltar project-discovery

```
❌ INCORRECTO:
Usuario: "Traduce este documento"
Claude: [empieza a traducir directamente]

✅ CORRECTO:
Usuario: "Traduce este documento"
Claude:
1. view /tmp/ADT/.codex/skills/project-discovery/SKILL.md
2. Carga metodologías del proyecto
3. ENTONCES usa translation-workflow
```

**Por qué es malo**: Claude trabaja sin conocer las metodologías del proyecto

---

### ❌ Anti-Patrón 2: Archivos sueltos en `.mywork/`

```
❌ INCORRECTO:
.mywork/
├── PLAN.md
├── ANALISIS.md
└── ERROR.md

✅ CORRECTO:
.mywork/changes/20260201-143000-correccion-warnings/
├── PLAN_estrategia.md
├── ANALISIS_230_warnings.md
└── ERROR_toctree_circular.md
```

**Por qué es malo**: Sin contexto de directorio, archivos genéricos no descriptivos

---

### ❌ Anti-Patrón 3: Usar spec-driven-dev para Todo

```
❌ INCORRECTO:
Usuario: "Fix este typo"
Claude: [crea 4 documentos de spec-driven-dev]

✅ CORRECTO:
Usuario: "Fix este typo"
Claude:
1. Fix directo
2. validation-suite
3. commit-helper
```

**Por qué es malo**: Over-engineering para tarea simple

---

### ❌ Anti-Patrón 4: No Validar Antes de Commit

```
❌ INCORRECTO:
1. Hacer cambios
2. git commit (sin validar)
3. Build roto

✅ CORRECTO:
1. Hacer cambios
2. validation-suite (build DEBE pasar)
3. Solo si pasa → commit-helper
```

**Por qué es malo**: Commits que rompen build

---

### ❌ Anti-Patrón 5: Múltiples Cambios en Un Commit

```
❌ INCORRECTO:
git commit -m "fixed titles + added skill + updated README"

✅ CORRECTO:
git commit -m "fix(sphinx): title underline in workflow.rst"
git commit -m "feat(skills): add image-management v1.0.0"
git commit -m "docs(skills): update README with new skill"
```

**Por qué es malo**: Dificulta rollback y troubleshooting

---

## 🎓 Guía de Aprendizaje

### Nuevo Usuario → ¿Por Dónde Empiezo?

**Sesión 1 - Orientación (30 min)**:
1. `project-discovery` - Ejecutar y entender
2. `project-context` - Leer completo (metodología ADT)
3. Este archivo (README_DECISION_TREE.md) - Familiarizarse con workflows

**Sesión 2 - Primera Tarea Simple (1h)**:
1. Elegir tarea simple (ej: traducir 1 documento pequeño)
2. Seguir workflow correspondiente paso a paso
3. Crear `work-logger` al finalizar

**Sesión 3 - Tarea Compleja (2-3h)**:
1. Usar `spec-driven-dev` o `incremental-correction-methodology`
2. Seguir TODAS las fases
3. Documentar aprendizajes

**Regla de oro para aprender**: Seguir el proceso COMPLETO las primeras veces, aunque parezca lento. La velocidad viene después.

---

## 📊 Métricas de Decisión

### ¿Cuándo Usar Qué?

| Criterio | Skill Apropiado |
|----------|----------------|
| Tiempo < 30 min | Skills directos (sphinx-expert, commit-helper) |
| Tiempo > 30 min | changes-directory-management + skills |
| Tiempo > 2 horas | spec-driven-dev |
| 100+ issues | incremental-correction-methodology |
| Traducción | translation-workflow |
| Error técnico Sphinx | sphinx-expert |
| Scripts production | bash-production-scripting |
| Nueva sesión | project-discovery (SIEMPRE) |

---

## 🔗 Enlaces Útiles

- **README Principal**: [../README.md](./README.md)
- **Project Discovery**: [./project-discovery/SKILL.md](./project-discovery/SKILL.md)
- **Project Context**: [./project-context/SKILL.md](./project-context/SKILL.md)
- **Skills Management**: [./skills-management/SKILL.md](./skills-management/SKILL.md)

---

## 📝 Notas

- **Este documento es guía, no ley**: Usa tu juicio
- **Contexto importa**: Adapta workflows según necesidad
- **Calidad > Velocidad**: Seguir proceso ahorra tiempo
- **Documenta decisiones**: Si te desvías, documenta por qué

---

**Mantenedor**: ADT Team  
**Última actualización**: 2026-02-01  
**Ubicación**: `/tmp/ADT/.codex/skills/README_DECISION_TREE.md`

