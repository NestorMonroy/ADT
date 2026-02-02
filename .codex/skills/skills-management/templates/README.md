# Templates de Skills Management

Directorio: `.codex/skills/skills-management/templates/`

---

## Propósito

Este directorio contiene templates para crear nuevos skills en el proyecto ADT siguiendo best practices oficiales de Anthropic.

---

## Templates Disponibles

### SKILL.md.template

**Archivo**: `SKILL.md.template`

**Propósito**: Template completo para crear archivos SKILL.md de nuevos skills

**Tamaño**: ~260 líneas con guías completas

**Contenido**:
- Frontmatter YAML (name, description, version, created, updated)
- Secciones estructuradas (Descripción, Cuándo Usar, Decision Framework, etc.)
- Placeholders descriptivos con [corchetes]
- Comentarios guía en cada sección
- Instrucciones finales de uso

**Basado en**:
- Anthropic skill authoring best practices
- Patrón de spec-driven-dev y work-logger
- Convenciones del proyecto ADT

---

## Guía de Uso

### Paso 1: Copiar Template

```bash
# Copiar template a nuevo skill
cp .codex/skills/skills-management/templates/SKILL.md.template \
   .codex/skills/[nombre-nuevo-skill]/SKILL.md
```

### Paso 2: Completar Frontmatter

Abrir `SKILL.md` y reemplazar:
- `[nombre-del-skill]`: Nombre en formato kebab-case (ej: `translation-workflow`)
- `[Descripción breve]`: Una oración que incluya QUÉ hace y CUÁNDO usarlo
- `[YYYY-MM-DD]`: Fecha actual en formato ISO

**Ejemplo de frontmatter completo**:
```yaml
---
name: commit-helper
description: "Ayuda a crear commits siguiendo Conventional Commits. Usar cuando el usuario necesite hacer un commit o escribir un mensaje de commit."
version: 1.0.0
created: 2026-02-01
updated: 2026-02-01
---
```

### Paso 3: Completar Secciones

Para cada sección, reemplazar placeholders:
- Eliminar comentarios entre `#`
- Reemplazar `[placeholders]` con contenido específico
- Eliminar secciones opcionales que no apliquen

**Secciones obligatorias**:
- Descripción
- Cuándo Usar
- Changelog (al menos v1.0.0)

**Secciones opcionales** (incluir solo si aportan valor):
- Decision Framework
- Trigger Patterns
- Self-Check
- Procedimiento
- Ejemplos
- Relaciones con Otros Skills
- Templates
- Notas
- Referencias

### Paso 4: Validar

Checklist antes de finalizar:
- [ ] Frontmatter YAML es válido (sin errores de sintaxis)
- [ ] Description incluye "Usar cuando..."
- [ ] Todos los placeholders [entre corchetes] fueron reemplazados
- [ ] Comentarios # fueron eliminados
- [ ] Secciones no aplicables fueron eliminadas
- [ ] Ejemplos son concretos y específicos (no genéricos)
- [ ] Trigger patterns están claros
- [ ] Changelog tiene al menos v1.0.0

### Paso 5: (Opcional) Consultar Best Practices

Para crear skills de alta calidad, consultar:
- `.codex/skills/anthropic-best-practices/skill-authoring.md`
- Principios de concisión, degrees of freedom, progressive disclosure
- Patrones de workflows y feedback loops

---

## Mejores Prácticas

### 1. Name (nombre del skill)

**Reglas**:
- Solo minúsculas, números y guiones (-)
- NO espacios, underscores o caracteres especiales
- Máximo 64 caracteres
- Descriptivo y único

**Bueno**: `commit-helper`, `translation-workflow`, `anthropic-best-practices`

**Malo**: `Commit_Helper`, `translation workflow`, `bp`

### 2. Description (descripción)

**Formato recomendado**: 
`"[Qué hace]. Usar cuando [trigger específico]."`

**Reglas**:
- Máximo 1024 caracteres
- Tercera persona (NO "Yo ayudo", SÍ "Ayuda a...")
- Incluir CUÁNDO usar (triggers/contextos)

**Bueno**: 
`"Ayuda a crear commits siguiendo Conventional Commits. Usar cuando el usuario necesite hacer un commit o escribir un mensaje de commit."`

**Malo**: 
`"Para commits"` (demasiado genérico, no incluye cuándo)

### 3. Concisión

**Principio**: Keep SKILL.md under 500 lines (Anthropic best practice)

Si el skill excede 500 líneas:
- Mover contenido detallado a archivos separados (ej: `reference.md`)
- Usar progressive disclosure pattern
- SKILL.md debe ser overview + decision framework + referencias

### 4. Ejemplos

**Bueno**: Ejemplos concretos con contexto del proyecto ADT
```markdown
### Ejemplo 1: Traducir sección arc42

**Contexto**: Traducción de Architecture Decisions (sección 9 de arc42)

**Input**: Documento original en inglés...
```

**Malo**: Ejemplos genéricos sin contexto
```markdown
### Ejemplo 1: Usar el skill

**Input**: Algún input...
```

### 5. Decision Frameworks

Incluir cuando el skill requiere tomar decisiones:
- Formato de preguntas: "¿[Condición]?" → [Resultado]
- Regla de oro al final
- Decisiones accionables (no ambiguas)

---

## Integración con anthropic-best-practices

Este template sigue best practices documentadas en:
`.codex/skills/anthropic-best-practices/skill-authoring.md`

**Principios aplicados**:
- **Concise is key**: Placeholders descriptivos, sin explicaciones innecesarias
- **Degrees of freedom**: Secciones opcionales permiten adaptar a necesidad
- **Progressive disclosure**: SKILL.md como overview, detalles en archivos separados
- **Testing**: Self-checks incluidos para validación

**Recomendación**: Leer `skill-authoring.md` antes de crear skill complejo

---

## Ejemplos de Skills Existentes

Para referencia, ver:
- `.codex/skills/commit-helper/SKILL.md` - Skill simple y completo
- `.codex/skills/spec-driven-dev/SKILL.md` - Skill con templates y fases
- `.codex/skills/work-logger/SKILL.md` - Skill con workflow específico
- `.codex/skills/anthropic-best-practices/SKILL.md` - Skill con progressive disclosure

---

## Workflow Completo

```
1. Decidir nombre del skill (kebab-case)
   ↓
2. Crear directorio: .codex/skills/[nombre-skill]/
   ↓
3. Copiar template: SKILL.md.template → SKILL.md
   ↓
4. Completar frontmatter (name, description, dates)
   ↓
5. Completar secciones obligatorias (Descripción, Cuándo Usar, Changelog)
   ↓
6. Completar secciones opcionales según necesidad
   ↓
7. Eliminar placeholders y comentarios
   ↓
8. Validar (frontmatter válido, ejemplos concretos, triggers claros)
   ↓
9. (Opcional) Consultar anthropic-best-practices para optimizar
   ↓
10. Skill listo para usar
```

---

## Preguntas Frecuentes

**Q: ¿Debo incluir todas las secciones del template?**

No. Incluir solo secciones que aporten valor. Obligatorias: Descripción, Cuándo Usar, Changelog. Resto son opcionales.

**Q: ¿Cómo sé si necesito Decision Framework?**

Si el skill requiere que el usuario tome decisiones (ej: elegir entre opciones, determinar tipo de acción), incluir Decision Framework.

**Q: ¿Cuándo usar Self-Check?**

Cuando hay validaciones importantes antes/durante/después de usar el skill (ej: build debe pasar, cambios deben ser atómicos).

**Q: ¿Qué hacer si el SKILL.md queda muy largo (>500 líneas)?**

Mover contenido detallado a archivos separados. SKILL.md debe tener overview + decision framework + referencias a archivos con detalles.

**Q: ¿Debo seguir anthropic-best-practices?**

Recomendado pero no obligatorio. Para skills simples, el template es suficiente. Para skills complejos o críticos, consultar best practices.

---

## Soporte

Si tienes dudas sobre cómo usar el template:
1. Ver ejemplos de skills existentes en `.codex/skills/`
2. Consultar `.codex/skills/anthropic-best-practices/skill-authoring.md`
3. Revisar este README

---

Última actualización: 2026-02-01
