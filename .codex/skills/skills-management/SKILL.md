---
name: skills-management
description: "Gestión, versionamiento y actualización de skills en .codex/skills/. Usar cuando se necesite crear, actualizar o documentar skills del proyecto."
version: 1.2.0
created: 2026-01-30
author: ADT Team
---

# Skills Management - Gestión de Skills del Proyecto

**Versión**: 1.0.0  
**Ubicación**: `/tmp/ADT/.codex/skills/skills-management/`  
**Proyecto**: ADT Documentation (ubicado en `/tmp/ADT`)

## ⚠️ RECORDATORIO CRÍTICO

**El proyecto SIEMPRE está en**: `/tmp/ADT`

Antes de cualquier operación, verificar:
```bash
pwd  # Debe ser /tmp/ADT
cd /tmp/ADT  # Si no estás ahí
```

---

## Cuando Usar

Usar esta skill cuando:
- Necesites crear una nueva skill
- Vayas a actualizar una skill existente
- Necesites documentar procedimientos del proyecto
- Quieras establecer relaciones entre skills
- Necesites versionar cambios en skills

**NO usar para**:
- Work logs de trabajo diario (usar `work-logger`)
- Commits (usar `commit-helper`)
- Validación de builds (usar `validation-suite`)

---

## Decision Framework: ¿Qué Operación de Skill Necesito?

**Usa este framework para identificar la operación correcta**:

1. **¿Necesito crear skill NUEVA?**
   → Ver sección "Crear Nueva Skill"

2. **¿Necesito ACTUALIZAR skill existente?**
   → Ver sección "Actualizar Skill"

3. **¿Necesito DEPRECAR skill obsoleto?**
   → Ver sección "Deprecar Skills"

4. **¿Solo necesito BUSCAR información en skills?**
   → Ver sección "Comandos Útiles"

5. **¿Necesito DOCUMENTAR relaciones entre skills?**
   → Actualizar README.md en `.codex/skills/`

6. **¿No estoy seguro qué operación?**
   → Leer skill completo primero

**Regla de oro**: **Operación determinada → ir directamente a sección**

---

## Trigger Patterns

### Señales Explícitas
- Usuario dice: "crear nueva skill"
- Usuario dice: "actualizar skill X"
- Usuario pregunta: "¿cómo gestiono skills?"
- Usuario dice: "necesito documentar metodología nueva"

### Señales Implícitas
- Usuario menciona metodología nueva no documentada
- Usuario detecta skill obsoleto o incompleto
- Necesidad de documentar proceso importante
- Usuario pregunta dónde documentar algo

### Trigger Words
- "skill", "metodología", "proceso", "documentar"
- "crear", "actualizar", "versionar"
- "gestión", "management"
- ".codex/skills/"

**Anti-triggers** (NO este skill):
- Trabajo operacional normal (no gestión de skills)
- Work logs (usar work-logger)
- Commits normales (usar commit-helper)

---

## Self-Check Before Skill Operation

**OBLIGATORIO antes de operación en skills**:

### Pre-Operation Checks
- [ ] ¿Sé qué operación necesito? (crear/actualizar/deprecar)
- [ ] ¿Estoy en `/tmp/ADT/`?
- [ ] ¿Tengo backup si voy a actualizar?
- [ ] ¿Leí documentación relevante?

**Si NO → Preparar antes de operar**

### During Operation Checks

**Si CREAR**:
- [ ] ¿Sigo estructura SKILL.md estándar?
- [ ] ¿Tengo frontmatter YAML?
- [ ] ¿Incluí todas las secciones obligatorias?
- [ ] ¿Actualicé README.md?

**Si ACTUALIZAR**:
- [ ] ¿Creé backup primero?
- [ ] ¿Actualicé version (semver)?
- [ ] ¿Actualicé campo updated?
- [ ] ¿Documenté cambios en Changelog?

**Si NO en alguno → PAUSE - Corregir**

### Post-Operation Checks
- [ ] ¿El skill funciona correctamente?
- [ ] ¿README.md actualizado?
- [ ] ¿Versionamiento correcto?
- [ ] ¿Hice commit de cambios?

**Si NO → COMPLETAR antes de cerrar**

---

## Versionamiento Semántico

### Formato: x.y.z

**x (MAJOR)**: Cambios incompatibles, restructuración completa
- Ejemplo: 1.0.0 → 2.0.0

**y (MINOR)**: Nueva funcionalidad compatible, secciones nuevas
- Ejemplo: 1.0.0 → 1.1.0

**z (PATCH)**: Correcciones, clarificaciones, typos
- Ejemplo: 1.0.0 → 1.0.1

### Ejemplos

```
1.0.0 → 1.0.1  # Corregir typo en documentación
1.0.1 → 1.1.0  # Añadir nueva sección "Ejemplos Avanzados"
1.1.0 → 2.0.0  # Cambiar estructura completa del workflow
```

---

## Proceso de Actualización de Skills

### REGLA DE ORO: NUNCA ELIMINAR INFORMACIÓN

**Siempre hacer backup antes de actualizar**

### Paso 1: Backup de Versión Anterior

```bash
cd /tmp/ADT/.codex/skills/[nombre-skill]/

# Obtener versión actual
CURRENT_VERSION=$(grep "^version:" SKILL.md | cut -d' ' -f2)

# Crear backup con versión
cp SKILL.md SKILL_backup_v${CURRENT_VERSION}.md

# Verificar
ls -la SKILL*.md
```

**Ejemplo**:
```bash
cd /tmp/ADT/.codex/skills/work-logger/
CURRENT_VERSION="1.0.0"
cp SKILL.md SKILL_backup_v1.0.0.md
```

### Paso 2: Actualizar Versión

Editar `SKILL.md`:

```markdown
---
name: skill-name
version: 1.1.0  # ← Actualizar aquí
updated: 2026-02-01  # ← Añadir fecha
---
```

### Paso 3: Documentar Cambios

Añadir al final de `SKILL.md`:

```markdown
---

## Changelog

### v1.1.0 - 2026-01-30
- Añadida sección "Ejemplos Avanzados"
- Actualizado proceso de validación
- Mejorada documentación de comandos

### v1.0.0 - 2026-01-28
- Versión inicial
```

### Paso 4: Commit

```bash
git add .codex/skills/[nombre-skill]/
git commit -m "docs(skills): actualizar [nombre-skill] v1.0.0 → v1.1.0

- Cambio 1
- Cambio 2
- Backup creado: SKILL_backup_v1.0.0.md"
```

---

## Estructura de Directorio de Skills

```
/tmp/ADT/.codex/skills/
├── skills-management/           # Esta skill
│   ├── SKILL.md                 # Versión actual
│   └── SKILL_backup_vX.X.X.md   # Backups versionados
│
├── [nombre-skill]/
│   ├── SKILL.md                 # Versión actual
│   ├── SKILL_backup_v1.0.0.md   # Backup versión anterior
│   ├── templates/               # (opcional) Templates
│   └── examples/                # (opcional) Ejemplos
│
└── README.md                    # Índice de todas las skills
```

---

## Crear Nueva Skill

### Paso 1: Decidir si Merece Nueva Skill

**Crear nueva skill si**:
- Funcionalidad completamente nueva
- Workflow independiente
- Puede ser reutilizado en múltiples contextos
- No encaja en ninguna skill existente

**Actualizar skill existente si**:
- Es extensión de funcionalidad existente
- Mejora proceso ya documentado
- Añade ejemplos/casos de uso a skill actual

### Paso 2: Crear Estructura

```bash
cd /tmp/ADT/.codex/skills/
mkdir -p nueva-skill/templates
cd nueva-skill/
```

### Paso 3: Usar Template

```bash
cat > SKILL.md <<'EOF'
---
name: nueva-skill
description: "Descripción breve de qué hace y cuándo usar"
version: 1.1.0
created: 2026-01-30
author: ADT Team
related_skills:
  - skill-relacionada-1
  - skill-relacionada-2
---

# Nueva Skill - Título Descriptivo

**Versión**: 1.0.0
**Ubicación**: `/tmp/ADT/.codex/skills/nueva-skill/`
**Proyecto**: ADT Documentation (ubicado en `/tmp/ADT`)

## Cuando Usar

[Describir casos de uso]

**NO usar para**:
[Describir qué NO hacer con esta skill]

## [Sección Principal]

[Contenido]

## Relaciones con Otras Skills

- **[skill-1]**: [Cómo se relaciona]
- **[skill-2]**: [Cómo se relaciona]

---

## Changelog

### v1.0.0 - 2026-01-30
- Versión inicial
EOF
```

### Paso 4: Commit

```bash
git add .codex/skills/nueva-skill/
git commit -m "docs(skills): añadir skill nueva-skill v1.0.0

- Funcionalidad X
- Workflow Y
- Integración con skill-relacionada"
```

---

## Relaciones entre Skills

### Mapa de Dependencias Actual

```
project-context          # Base: contexto del proyecto
    ↓
├── translation-workflow # Usa contexto ADT
├── sphinx-expert        # Usa estructura de proyecto
├── validation-suite     # Valida estructura de proyecto
│
commit-helper            # Independiente: estándar de commits
│
work-logger              # Independiente: documentación de trabajo
    ↓
└── skills-management    # Meta: gestiona skills (usa work-logger)
│
spec-driven-dev          # Metodología: desarrollo en 4 fases
    ↓
└── [Puede usar cualquier otra skill]
```

### Cómo Documentar Relaciones

En el frontmatter de cada `SKILL.md`:

```yaml
---
related_skills:
  - project-context: "Proporciona contexto metodológico base"
  - validation-suite: "Valida resultados del workflow"
---
```

O en sección dedicada:

```markdown
## Relaciones con Otras Skills

### Dependencias
- **project-context**: Requiere entender metodología ADT
- **sphinx-expert**: Usa conocimiento de estructura RST

### Complementarias
- **validation-suite**: Validar después de usar esta skill
- **commit-helper**: Commitear cambios con mensajes estándar

### Flujo Sugerido
1. Usar **project-context** para entender contexto
2. Aplicar esta skill
3. Validar con **validation-suite**
4. Documentar con **work-logger**
5. Commit con **commit-helper**
```

---

## Template Completo de Skill

```markdown
---
name: nombre-skill
description: "Descripción concisa (1-2 líneas)"
version: 1.1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD  # Solo si hay actualizaciones
author: ADT Team
related_skills:
  - skill-1
  - skill-2
tags:
  - tag1
  - tag2
---

# Nombre Skill - Título Largo Descriptivo

**Versión**: 1.0.0
**Ubicación**: `/tmp/ADT/.codex/skills/nombre-skill/`
**Proyecto**: ADT Documentation (ubicado en `/tmp/ADT`)

## ⚠️ RECORDATORIO

**Proyecto ubicado en**: `/tmp/ADT`

## Cuando Usar

Usar esta skill cuando:
- [Caso de uso 1]
- [Caso de uso 2]

**NO usar para**:
- [Anti-patrón 1]
- [Anti-patrón 2]

## [Sección Principal 1]

### Subsección

[Contenido con ejemplos]

```bash
# Comandos siempre desde /tmp/ADT
cd /tmp/ADT
comando
```

## [Sección Principal 2]

[Más contenido]

## Relaciones con Otras Skills

### Dependencias
- **skill-base**: [Por qué la necesita]

### Complementarias
- **skill-complementaria**: [Cómo se usa en conjunto]

### Flujo Sugerido
1. [Paso 1 con skill X]
2. [Paso 2 con esta skill]
3. [Paso 3 con skill Y]

## Ejemplos

### Ejemplo 1: [Nombre]

[Descripción]

```bash
cd /tmp/ADT
[comandos]
```

[Resultado esperado]

## Troubleshooting

### Problema: [Descripción]

**Síntoma**: [Qué se ve]

**Causa**: [Por qué pasa]

**Solución**:
```bash
cd /tmp/ADT
[solución]
```

## Referencias

- [Documento interno relacionado]
- [Documentación externa]

---

## Changelog

### v1.0.0 - YYYY-MM-DD
- Versión inicial
- [Características principales]
```

---

## Mantenimiento de Skills

### Auditoría Periódica

**Cada 3-6 meses**, revisar:

```bash
cd /tmp/ADT/.codex/skills/

# Listar skills sin versión
for skill in */SKILL.md; do
  if ! grep -q "^version:" "$skill"; then
    echo "⚠️  Sin versión: $skill"
  fi
done

# Listar skills desactualizadas (sin updated en 6+ meses)
# [Script personalizado según necesidad]
```

### Deprecar Skills

Si una skill ya no es útil:

**NO ELIMINAR**. En su lugar:

1. Marcar como deprecada en frontmatter:

```yaml
---
name: skill-deprecada
status: DEPRECATED
deprecated_since: 2026-01-30
replaced_by: nueva-skill
---
```

2. Añadir aviso al inicio:

```markdown
# ⚠️ SKILL DEPRECADA

**Esta skill ha sido deprecada desde**: 2026-01-30  
**Usar en su lugar**: `nueva-skill`  
**Razón**: [Explicación]

---

# [Contenido original conservado]
```

3. Mover a directorio `deprecated/`:

```bash
cd /tmp/ADT/.codex/skills/
mkdir -p deprecated/
mv skill-deprecada/ deprecated/
```

### Archivar Backups Antiguos

Después de 3+ versiones:

```bash
cd /tmp/ADT/.codex/skills/nombre-skill/

mkdir -p archive/
mv SKILL_backup_v1.0.0.md archive/
mv SKILL_backup_v1.1.0.md archive/

# Mantener solo últimas 2-3 versiones en raíz
```

---

## Índice de Skills (README.md)

Mantener actualizado `/tmp/ADT/.codex/skills/README.md`:

```markdown
# Skills del Proyecto ADT

**Proyecto ubicado en**: `/tmp/ADT`

## Skills Activas

| Skill | Versión | Descripción | Cuándo Usar |
|-------|---------|-------------|-------------|
| [project-context](./project-context/) | 1.0.0 | Contexto metodológico | Entender ADT, frameworks |
| [translation-workflow](./translation-workflow/) | 1.0.0 | Workflow traducción | Traducir contenido |
| ... | ... | ... | ... |

## Skills Deprecadas

| Skill | Deprecada | Reemplazada Por | Razón |
|-------|-----------|-----------------|-------|
| [skill-vieja](./deprecated/skill-vieja/) | 2026-01-15 | nueva-skill | [Razón] |

## Mapa de Relaciones

[Diagrama o lista de dependencias]

## Cómo Usar

Ver [skills-management](./skills-management/) para:
- Crear nuevas skills
- Actualizar skills existentes  
- Versionar cambios
```

---

## Comandos Útiles

### Buscar en Skills

```bash
cd /tmp/ADT

# Buscar por palabra clave
grep -r "keyword" .codex/skills/*/SKILL.md

# Listar todas las versiones
grep -h "^version:" .codex/skills/*/SKILL.md | sort

# Ver skills relacionadas con X
grep -A2 "related_skills:" .codex/skills/*/SKILL.md | grep -i "skill-x"
```

### Validar Estructura

```bash
cd /tmp/ADT/.codex/skills/

# Verificar que todas tienen versión
for skill in */SKILL.md; do
  if grep -q "^version:" "$skill"; then
    version=$(grep "^version:" "$skill" | cut -d' ' -f2)
    echo "✓ $(dirname $skill): v$version"
  else
    echo "✗ $(dirname $skill): SIN VERSIÓN"
  fi
done
```

---

## Changelog

### v1.0.0 - 2026-01-30

**Versión inicial**

- Definido versionamiento semántico (x.y.z)
- Proceso de backup antes de actualizar
- Regla de oro: NUNCA ELIMINAR INFORMACIÓN
- Template completo de skill
- Gestión de relaciones entre skills
- Procedimiento de deprecación
- Comandos útiles de gestión
- Recordatorio crítico: proyecto en /tmp/ADT

**Razón de Creación**:
- Necesidad de estandarizar gestión de skills
- Prevenir pérdida de información
- Facilitar evolución de documentación del proyecto

**Referencias**:
- Observación de estructura existente en `.mywork/changes/`
- Convenciones de `work-logger`
- Necesidad identificada por usuario

---

**Notas**:
- Esta skill es "meta" - documenta cómo gestionar skills
- Aplicar este mismo proceso a esta skill si necesita actualización
- Mantener sincronizado con prácticas reales del proyecto

---

## Templates Disponibles

Este skill incluye templates para crear nuevos skills siguiendo best practices.

### Directorio templates/

**Ubicación**: `.codex/skills/skills-management/templates/`

**Contenido**:
- `SKILL.md.template` - Template completo para crear SKILL.md
- `README.md` - Guía completa de uso de templates

---

### SKILL.md.template

**Propósito**: Plantilla completa para crear archivos SKILL.md de nuevos skills

**Características**:
- Frontmatter YAML completo (name, description, version, created, updated)
- Todas las secciones estándar con placeholders descriptivos
- Comentarios guía en cada sección
- Basado en best practices de Anthropic
- ~260 líneas con instrucciones completas

**Secciones incluidas**:
- Obligatorias: Descripción, Cuándo Usar, Changelog
- Opcionales: Decision Framework, Trigger Patterns, Self-Check, Procedimiento, Ejemplos, Relaciones con Otros Skills, Templates, Notas, Referencias

**Workflow de uso**:
1. Copiar template a nuevo directorio de skill:
   ```bash
   cp .codex/skills/skills-management/templates/SKILL.md.template \
      .codex/skills/[nombre-nuevo-skill]/SKILL.md
   ```

2. Completar frontmatter (name, description, dates)

3. Reemplazar todos los placeholders [entre corchetes]

4. Completar secciones obligatorias (Descripción, Cuándo Usar, Changelog)

5. Completar secciones opcionales según necesidad

6. Eliminar comentarios y placeholders no usados

7. Validar:
   - Frontmatter YAML válido
   - Description incluye "Usar cuando..."
   - Ejemplos son concretos y específicos
   - Triggers están claros

**Ejemplo rápido**:
```bash
# Crear directorio para nuevo skill
mkdir -p .codex/skills/mi-nuevo-skill

# Copiar template
cp .codex/skills/skills-management/templates/SKILL.md.template \
   .codex/skills/mi-nuevo-skill/SKILL.md

# Editar y completar placeholders
# ... edición manual del archivo ...
```

---

### README.md del directorio templates/

**Propósito**: Guía completa de uso de templates con mejores prácticas

**Contenido**:
- Propósito de cada template
- Guía paso a paso de uso
- Mejores prácticas (naming, description, concisión, ejemplos)
- Integración con anthropic-best-practices
- Workflow completo
- FAQ

**Cuándo consultar**:
- Primera vez creando un skill
- Dudas sobre cómo completar secciones
- Necesitas verificar mejores prácticas
- Quieres optimizar la calidad del skill

---

## Integración con anthropic-best-practices

Para crear skills de alta calidad, este skill se integra con:

**`.codex/skills/anthropic-best-practices/skill-authoring.md`**

Consultar este archivo para:
- **Principios de skill authoring**: Concisión, degrees of freedom, testing
- **Skill structure**: Naming conventions, descriptions efectivas
- **Progressive disclosure**: Cuándo split contenido en archivos separados
- **Workflows y feedback loops**: Patrones de ejecución paso a paso
- **Common patterns**: Templates, examples, conditional workflows
- **Evaluation and iteration**: Cómo mejorar skills iterativamente

**Workflow recomendado**:
1. Usar `SKILL.md.template` para estructura básica
2. Consultar `anthropic-best-practices/skill-authoring.md` para optimización
3. Aplicar principios de concisión y progressive disclosure
4. Validar con self-checks

**Beneficio**: Skills creados siguen best practices oficiales de Anthropic desde el inicio

---

## Changelog

### v1.2.0 - 2026-02-01 - Templates

**Agregado**:
- Template SKILL.md.template en templates/
- README.md en templates/ con guía completa de uso
- Sección "Templates Disponibles" en SKILL.md
- Sección "Integración con anthropic-best-practices"

**Contenido de templates**:
- SKILL.md.template (~260 líneas con guías completas)
- Frontmatter YAML, placeholders descriptivos, comentarios guía
- Secciones obligatorias y opcionales
- Basado en best practices de Anthropic

**README.md incluye**:
- Workflow paso a paso
- Mejores prácticas (naming, description, concisión)
- Integración con anthropic-best-practices
- FAQ

**Beneficio**:
- Crear nuevos skills es más fácil y consistente
- Skills siguen best practices desde el inicio
- Reduce tiempo de creación de skill nuevo
- Asegura calidad y completitud

### v1.1.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y decision-making**:

✅ **Decision Framework** - ¿Qué Operación de Skill Necesito?
- 6 preguntas para identificar operación correcta
- Mapeo directo a secciones del skill
- Regla de oro para navegación eficiente

✅ **Trigger Patterns** - Cuándo usar este skill
- Señales explícitas (usuario dice "crear skill")
- Señales implícitas (metodología nueva no documentada)
- Clarifica que NO es para trabajo operacional

✅ **Self-Check Mechanisms** - Checks por tipo de operación
- Pre-Operation (preparación, ubicación, backup)
- During Operation (diferentes para crear/actualizar/deprecar)
- Post-Operation (funcionalidad, README, commit)

**Líneas agregadas**: ~85 líneas

**Beneficio principal**:
- Usuarios identifican operación necesaria rápidamente
- Checklist específico por tipo de operación
- Previene olvidos en actualización de skills

### v1.0.0 - 2026-01-30
- Versión inicial
- Gestión completa de skills
- Versionamiento semántico
- Plantillas y ejemplos
