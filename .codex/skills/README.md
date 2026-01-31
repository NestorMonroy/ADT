# Skills del Proyecto ADT

**Proyecto ubicado en**: `/tmp/ADT`  
**Última actualización**: 2026-01-30

---

## ⚠️ RECORDATORIO CRÍTICO

**El proyecto SIEMPRE está en**: `/tmp/ADT`

```bash
cd /tmp/ADT  # Siempre verificar ubicación
```

---

## 📋 Skills Activas

| Skill | Versión | Descripción | Cuándo Usar |
|-------|---------|-------------|-------------|
| [skills-management](./skills-management/) | 1.0.0 | Gestión y versionamiento de skills | Crear/actualizar skills |
| [incremental-correction-methodology](./incremental-correction-methodology/) | 1.0.0 | Metodología de corrección incremental | Corregir 100+ issues, balancear velocidad vs calidad |
| [changes-directory-management](./changes-directory-management/) | 1.0.0 | Gestión de directorios en .mywork/changes/ | Crear/renombrar directorios de trabajo |
| [project-context](./project-context/) | 1.0.0 | Contexto metodológico ADT | Entender ADT, frameworks, terminología |
| [translation-workflow](./translation-workflow/) | 1.0.0 | Workflow de traducción | Traducir contenido con metodología ADT |
| [sphinx-expert](./sphinx-expert/) | 1.2.0 | Experto Sphinx/RST | Resolver problemas de build, optimizar RST, corregir WARNING |
| [validation-suite](./validation-suite/) | 1.0.0 | Suite de validación | Verificar builds, calidad antes de commits |
| [work-logger](./work-logger/) | 1.0.0 | Sistema de logging | Documentar trabajo completado |
| [commit-helper](./commit-helper/) | 1.0.0 | Conventional Commits | Escribir mensajes de commit estándar |
| [spec-driven-dev](./spec-driven-dev/) | 1.1.0 | Desarrollo en 4 fases | Features complejas, cambios arquitectónicos |

---

## 🗺️ Mapa de Relaciones

### Flujo Típico de Trabajo

```
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

**Última actualización**: 2026-01-30  
**Mantenedor**: ADT Team  
**Ubicación del Proyecto**: `/tmp/ADT`
