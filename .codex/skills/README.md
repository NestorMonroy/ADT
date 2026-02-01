# Skills del Proyecto ADT

**Proyecto ubicado en**: `/tmp/ADT`  
**Última actualización**: 2026-02-01

---

## 🚨 SKILL CRÍTICO - EJECUTAR PRIMERO

**ATENCIÓN CLAUDE**: Antes de hacer CUALQUIER trabajo en este proyecto, DEBES ejecutar:

```bash
view /tmp/ADT/.codex/skills/project-discovery/SKILL.md
```

**project-discovery** (v1.0.0) es el skill #0 (CRITICAL, order: 0)

- **DEBE ejecutarse PRIMERO** en TODA conversación nueva
- **Garantiza** que Claude cargue las metodologías del proyecto
- **Independiente** del system prompt de Anthropic

**Por qué es crítico**:
El system prompt de Claude de Anthropic NO instruye buscar skills en proyectos de usuarios. Solo conoce `/mnt/skills/`. Sin project-discovery, Claude puede:
- ❌ Ignorar todas las metodologías de este proyecto
- ❌ Usar convenciones genéricas incorrectas
- ❌ No seguir nuestras reglas establecidas

**Ver**: [project-discovery/SKILL.md](./project-discovery/SKILL.md) para workflow completo

---

## ⚠️ RECORDATORIO CRÍTICO

**El proyecto SIEMPRE está en**: `/tmp/ADT`

```bash
cd /tmp/ADT  # Siempre verificar ubicación
```

---

## 🎯 Guía Rápida de Navegación

**¿No sabes qué skill usar?** Ver: [README_DECISION_TREE.md](./README_DECISION_TREE.md)

El Decision Tree te ayuda a:
- ✅ Encontrar el skill correcto para tu tarea
- ✅ Entender relaciones entre skills
- ✅ Ver workflows típicos con ejemplos
- ✅ Evitar anti-patrones comunes

---

## 🚨 Critical Reminders - LEER CADA SESIÓN

### REMINDER 1: Project Discovery PRIMERO ⚠️

**SIEMPRE** ejecutar `project-discovery` skill antes de cualquier trabajo.

Claude NO busca `.codex/skills/` automáticamente - el system prompt de Anthropic solo conoce `/mnt/skills/`.

**Trigger automático**: Inicio de CADA nueva sesión

**Validación**:
- [ ] ¿Ejecuté `view /tmp/ADT/.codex/skills/project-discovery/SKILL.md`?
- [ ] ¿Leí README.md de skills?
- [ ] ¿Identifiqué skills relevantes para la tarea?

**Si NO → STOP - Ejecutar project-discovery primero**

---

### REMINDER 2: Las 8 Protecciones NO son Opcionales

Si usas scripts automáticos en `incremental-correction-methodology`:

✅ **Las 8 Protecciones son OBLIGATORIAS**:
1. Dry-run siempre
2. Un archivo a la vez
3. Git status limpio
4. Commit por archivo
5. Validar issues disminuyen
6. Backup antes de empezar
7. Rollback plan listo
8. Documentar decisión

❌ **NO hay**: "esta vez voy rápido", "solo son unos archivos"

**Validado en producción**: 0 regresiones siguiendo las 8, múltiples errores violándolas

---

### REMINDER 3: NUNCA Archivos Sueltos en `.mywork/` Raíz

**Regla absoluta**: NO crear archivos .md directamente en `.mywork/` raíz

**Metodología correcta** (`changes-directory-management`):

```bash
# Trabajo >30 minutos → Crear directorio
cd /tmp/ADT
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
mkdir -p .mywork/changes/${TIMESTAMP}-descripcion-trabajo

# Trabajar DENTRO del directorio
cd .mywork/changes/${TIMESTAMP}-descripcion-trabajo
touch PLAN.md ANALISIS.md DECISIONES.md
```

**Formato directorios**:
- Trabajo >2h: `YYYYMMDD-HHMMSS-descripcion/` (timestamp OBLIGATORIO)
- Trabajo <2h: `descripcion-corta/` (sin timestamp)

**Validación**:
- [ ] ¿El trabajo tomará >30 min?
- [ ] ¿Creé directorio en `.mywork/changes/`?
- [ ] ¿Estoy trabajando DENTRO del directorio?

**Si NO → Crear directorio primero**

---

### REMINDER 4: Convención de Nombres - SIEMPRE Específicos 📋

**Formato obligatorio para archivos**:
```
TIPO_contexto_especifico_descriptivo.md
```

**Contexto determina especificidad**:

**Archivos EN RAÍZ** (sin directorio padre) → Nombres MUY específicos:
✅ `PLAN_correccion_incremental_230_warnings_sphinx.md`
✅ `ANALISIS_COMPLETO_build_sphinx_errores_criticos.md`
✅ `ERROR_script_fix_critical_titles_underlines_longitud.md`
✅ `DECISIONES_estrategia_traduccion_arc42_seccion_10.md`

❌ `PLAN.md` (sin contexto - prohibido en raíz)
❌ `ANALISIS.md` (genérico - prohibido en raíz)

**Archivos DENTRO de directorio** → Pueden ser más cortos (directorio da contexto):
```
.mywork/changes/20260201-correccion-warnings/
├── PLAN.md                    ← OK (directorio da contexto)
├── ANALISIS.md                ← OK (sabemos que es de warnings)
├── DECISIONES.md              ← OK (contexto claro)
```

**Pero preferible nombres específicos también dentro**:
```
.mywork/changes/20260201-correccion-warnings/
├── PLAN_estrategia_correccion.md        ← Mejor
├── ANALISIS_230_warnings_sphinx.md      ← Mejor
├── DECISIONES_manual_vs_script.md       ← Mejor
```

**Regla de oro**: Nombre debe ser auto-documentado sin ver contenido

**Excepción**: Templates dentro de skills
```
.codex/skills/<skill-name>/templates/<nombre>.template
```

---

### REMINDER 5: Calidad > Velocidad

Metodología incremental privilegia calidad sobre velocidad.

**Filosofía**:
- Seguir el proceso ahorra tiempo a largo plazo
- Atajos → más tiempo en rollback y fixes
- "Rápido y mal" es más lento que "despacio y bien"

**Cuando tengas prisa**:
1. Respira profundo
2. Sigue el proceso completo
3. Agradécete después (evitaste desastre)

---

### REMINDER 6: Un Commit = Un Cambio Lógico

NO agrupar cambios no relacionados en un commit.

**Formato**: `tipo(scope): descripción` (Conventional Commits)

**Ejemplos correctos**:
✅ `fix(sphinx): title underline too short in workflow_general.rst`
✅ `docs(skills): add decision frameworks to all skills`
✅ `refactor(scripts): extract validation logic to separate function`

**Ejemplos incorrectos**:
❌ `fixed stuff` (vago, sin tipo/scope)
❌ `fix(sphinx): titles + added new skill + updated README` (múltiples cambios)

**Beneficios**:
- Facilita rollback
- Mejora code review
- Simplifica troubleshooting

---

### REMINDER 7: Validar ANTES de Commit

Build DEBE pasar antes de commit.

**Workflow obligatorio**:
```bash
# 1. Hacer cambios
vim source/file.rst

# 2. Validar (OBLIGATORIO)
./scripts/build.sh  # o el comando de build apropiado

# 3. Solo si build pasa → Commit
git add source/file.rst
git commit -m "fix(docs): descripción del cambio"
```

**NO crear commits que rompan el build**

**Usar**: `validation-suite` skill para validaciones

---

### REMINDER 8: Templates Dentro de Skills

Templates en raíz del proyecto → **ANTI-PATRÓN**

**Ubicación correcta**:
```
.codex/skills/<skill-name>/templates/<template-name>.template
```

**Ejemplo correcto**:
```
.codex/skills/work-logger/
├── SKILL.md
└── templates/
    └── work-log.md.template
```

**Razón**:
- Versionamiento conjunto con skill
- Portabilidad
- Organización clara
- Fuente de creación es el skill

---

## 📋 Skills Activas

| Skill | Versión | Descripción | Cuándo Usar |
|-------|---------|-------------|-------------|
| [**project-discovery** 🚨](./project-discovery/) | **1.1.0** | **EJECUTAR PRIMERO - Descubrimiento y carga de skills del proyecto** | **TODA conversación nueva, ANTES de cualquier trabajo** |
| [skills-management](./skills-management/) | 1.1.0 | Gestión y versionamiento de skills | Crear/actualizar skills |
| [incremental-correction-methodology](./incremental-correction-methodology/) | 1.4.0 | Metodología de corrección incremental | Corregir 100+ issues, balancear velocidad vs calidad |
| [changes-directory-management](./changes-directory-management/) | 1.1.0 | Gestión de directorios en .mywork/changes/ | Crear/renombrar directorios de trabajo |
| [project-context](./project-context/) | 1.1.0 | Contexto metodológico ADT | Entender ADT, frameworks, terminología |
| [translation-workflow](./translation-workflow/) | 1.1.0 | Workflow de traducción | Traducir contenido con metodología ADT |
| [sphinx-expert](./sphinx-expert/) | 1.7.0 | Experto Sphinx/RST | Resolver problemas de build, optimizar RST, corregir WARNING |
| [validation-suite](./validation-suite/) | 1.1.0 | Suite de validación | Verificar builds, calidad antes de commits |
| [work-logger](./work-logger/) | 1.1.0 | Sistema de logging | Documentar trabajo completado |
| [commit-helper](./commit-helper/) | 1.1.0 | Conventional Commits | Escribir mensajes de commit estándar |
| [spec-driven-dev](./spec-driven-dev/) | 1.2.0 | Desarrollo en 4 fases | Features complejas, cambios arquitectónicos |
| [bash-production-scripting](./bash-production-scripting/) | 1.1.0 | Best practices bash | Scripts robustos, cross-platform, producción |

**Total**: 12 skills (1 CRÍTICO, 11 activas)

---

## 🗺️ Mapa de Relaciones

### Flujo Típico de Trabajo

```
0. project-discovery 🚨 (OBLIGATORIO - PRIMERO)
   ↓
   Descubre y carga skills del proyecto
   Lee README.md, identifica skills relevantes
   ↓
1. project-context
   ↓
   Entender metodología y estructura del proyecto
   ↓
2. spec-driven-dev (opcional para cambios grandes)
   ↓
   Planificar en 4 fases
   ↓
3. translation-workflow / sphinx-expert
   ↓
   Realizar trabajo (traducir, documentar, etc.)
   ↓
4. validation-suite
   ↓
   Validar cambios
   ↓
5. work-logger
   ↓
   Documentar trabajo completado
   ↓
6. commit-helper
   ↓
   Commit con mensaje estándar
```

### Dependencias entre Skills

```
project-context (Base)
    ├── translation-workflow (requiere contexto ADT)
    ├── sphinx-expert (requiere estructura proyecto)
    └── validation-suite (valida estructura proyecto)

spec-driven-dev (Metodología)
    └── Puede usar cualquier skill según fase
    └── Usa changes-directory-management para organizar trabajo

skills-management (Meta)
    └── work-logger (para documentar cambios en skills)

changes-directory-management (Gestión)
    ├── work-logger (diferencia: completado vs en progreso)
    └── spec-driven-dev (estructura de directorios)

commit-helper (Independiente)
work-logger (Independiente)
```

---

## 📚 Guía de Uso por Tarea

### Tarea: Traducir Sección de arc42

1. `project-context` - Entender metodología ADT
2. `translation-workflow` - Ejecutar workflow de traducción
3. `validation-suite` - Validar resultado
4. `work-logger` - Documentar traducción completada
5. `commit-helper` - Commit con mensaje estándar

### Tarea: Resolver Errores de Build Sphinx

1. `sphinx-expert` - Analizar y resolver errores
2. `validation-suite` - Validar fix
3. `work-logger` - Documentar solución
4. `commit-helper` - Commit con mensaje estándar

### Tarea: Implementar Feature Nueva

1. `spec-driven-dev` - Planificar en 4 fases
2. `project-context` - Asegurar alineación con ADT
3. `sphinx-expert` - Implementar cambios en docs
4. `validation-suite` - Validar todo
5. `work-logger` - Documentar implementación
6. `commit-helper` - Commit con mensaje estándar

### Tarea: Crear/Actualizar Skill

1. `skills-management` - Seguir proceso de versionamiento
2. `work-logger` - Documentar cambio en skill
3. `commit-helper` - Commit con mensaje estándar

### Tarea: Corregir 100+ Issues (Linter, WARNING, etc.)

1. `incremental-correction-methodology` - Seguir metodología 4 fases
2. `sphinx-expert` - Para issues técnicos de Sphinx (si aplica)
3. `validation-suite` - Validar que issues disminuyen
4. `work-logger` - Documentar progreso por categoría
5. `commit-helper` - Commits detallados (un archivo = un commit)

**Puntos clave**:
- Análisis inicial obligatorio (30 min)
- Categorización y priorización
- 7 Protecciones si usa scripts
- Trade-off: Calidad > Velocidad
- Documentar decisiones en tiempo real

---

## 🔧 Gestión de Skills

### Crear Nueva Skill

Ver proceso completo en [skills-management](./skills-management/)

```bash
cd /tmp/ADT/.codex/skills/
mkdir nueva-skill
# ... seguir template
```

### Actualizar Skill Existente

**REGLA DE ORO**: Siempre hacer backup antes

```bash
cd /tmp/ADT/.codex/skills/nombre-skill/
cp SKILL.md SKILL_backup_v1.0.0.md
# ... actualizar SKILL.md
# ... incrementar versión
```

Ver [skills-management](./skills-management/) para proceso completo.

### Versionamiento

Formato: **x.y.z** (semántico)

- **x (MAJOR)**: Cambios incompatibles, reestructuración
- **y (MINOR)**: Nueva funcionalidad compatible
- **z (PATCH)**: Correcciones, clarificaciones

---

## 📂 Estructura de Directorio

```
/tmp/ADT/.codex/skills/
├── README.md                    # Este archivo
│
├── skills-management/           # ★ Meta-skill (gestión de skills)
│   └── SKILL.md
│
├── project-context/             # Base: contexto metodológico
│   ├── SKILL.md
│   └── references/
│       ├── estructura/
│       └── frameworks/
│
├── translation-workflow/        # Workflow de traducción
│   └── SKILL.md
│
├── sphinx-expert/               # Experto Sphinx/RST
│   └── SKILL.md
│
├── validation-suite/            # Suite de validación
│   └── SKILL.md
│
├── work-logger/                 # Sistema de logging
│   ├── SKILL.md
│   └── templates/
│       └── work-log.md.template
│
├── commit-helper/               # Conventional Commits
│   └── SKILL.md
│
└── spec-driven-dev/             # Desarrollo en 4 fases
    ├── SKILL.md
    └── templates/
```

---

## 🔍 Comandos Útiles

### Buscar en Skills

```bash
cd /tmp/ADT

# Buscar por palabra clave
grep -r "traducción" .codex/skills/*/SKILL.md

# Listar todas las versiones
grep -h "^version:" .codex/skills/*/SKILL.md | sort -u

# Ver skills sin versión
for skill in .codex/skills/*/SKILL.md; do
  if ! grep -q "^version:" "$skill"; then
    echo "⚠️  $skill"
  fi
done
```

### Verificar Integridad

```bash
cd /tmp/ADT/.codex/skills/

# Verificar que todas tienen SKILL.md
for dir in */; do
  if [ ! -f "${dir}SKILL.md" ]; then
    echo "❌ ${dir} sin SKILL.md"
  else
    echo "✓ ${dir}"
  fi
done
```

---

## 📖 Referencias

### Documentación Interna

- [.mywork/work-logs/](../../.mywork/work-logs/) - Logs de trabajo completado
- [.mywork/changes/](../../.mywork/changes/) - Planes y documentación de cambios
- [.mywork/adr/](../../.mywork/adr/) - Architectural Decision Records

### Skills Relacionadas

Cada skill tiene su propia documentación detallada. Ver directorio individual.

---

## 📝 Notas

- **Nunca eliminar información** de skills - hacer backups versionados
- Skills son **documentación viva** - actualizar con experiencia
- Mantener **este README sincronizado** al añadir/actualizar skills
- Proyecto **siempre en /tmp/ADT** - verificar antes de cada operación

---

## Changelog del README

### 2026-02-01 (v7) - Propuesta v2 Implementada

- ✅ **README_DECISION_TREE.md creado**: Guía completa de navegación
  - Decision tree por tipo de tarea
  - Decision tree por señales del usuario
  - Mapa visual de relaciones entre skills
  - 6 workflows típicos con ejemplos completos
  - Anti-patrones comunes documentados
  - Guía de aprendizaje para nuevos usuarios
- ✅ Link actualizado en README.md principal
- ✅ 573 líneas de navegación y ejemplos

### 2026-02-01 (v6) - Fase 2 Completada

- ✅ **Critical Reminders expandidos**: 8 reminders completos
  - REMINDER 1: Project Discovery PRIMERO (con validación checklist)
  - REMINDER 2: Las 8 Protecciones NO opcionales (actualizado de 7 a 8)
  - REMINDER 3: NUNCA archivos sueltos en `.mywork/` raíz (NUEVO)
  - REMINDER 4: Convención nombres SIEMPRE específicos (NUEVO, con ejemplos detallados)
  - REMINDER 5: Calidad > Velocidad
  - REMINDER 6: Un Commit = Un Cambio Lógico
  - REMINDER 7: Validar ANTES de Commit
  - REMINDER 8: Templates dentro de skills (NUEVO)
- ✅ Documentada convención de nombres con contexto
- ✅ Actualizado incremental-correction a 8 Protecciones
- ✅ Skills actualizados con Decision Frameworks, Trigger Patterns, Self-Checks

### 2026-02-01 (v5)

- ✅ Añadida skill CRÍTICA: **project-discovery** v1.0.0
- ✅ Agregada sección "SKILL CRÍTICO - EJECUTAR PRIMERO"
- ✅ Agregada sección "Critical Reminders"
- ✅ Actualizado flujo típico con paso 0 (project-discovery)
- ✅ Total: 12 skills (1 CRÍTICA + 11 activas)
- ✅ Enfatizado independencia del system prompt de Anthropic

### 2026-01-30 (v4)

- ✅ Añadida skill: incremental-correction-methodology v1.0.0
- ✅ Actualizada skill: sphinx-expert v1.1.0 → v1.2.0
- ✅ Nueva tarea: "Corregir 100+ Issues"
- ✅ Total: 10 skills activas
- ✅ Estructuración: Técnico (sphinx) vs Metodológico (incremental)

### 2026-01-30 (v3)

- ✅ Actualizada skill: spec-driven-dev v1.0.0 → v1.1.0
- ✅ Formato de directorios estandarizado con timestamp

### 2026-01-30 (v2)

- ✅ Añadida skill: changes-directory-management v1.0.0
- ✅ Actualizado mapa de relaciones
- ✅ Total: 9 skills activas
- ✅ sphinx-expert actualizado a v1.1.0

### 2026-01-30 (v1)

- ✅ Versión inicial
- ✅ Listado de 8 skills activas
- ✅ Mapa de relaciones entre skills
- ✅ Guías de uso por tarea
- ✅ Comandos útiles de gestión
- ✅ Recordatorio crítico: /tmp/ADT

---

**Última actualización**: 2026-02-01  
**Mantenedor**: ADT Team  
**Ubicación del Proyecto**: `/tmp/ADT`
