---
name: commit-helper
description: "Ayuda a crear commits siguiendo Conventional Commits. Usar cuando el usuario necesite hacer un commit o escribir un mensaje de commit."
version: 1.2.0
created: 2026-01-29
updated: 2026-02-01
---

# Commit Helper - Conventional Commits

## Cuando usar

- Usuario pide hacer commit
- Se menciona "commit", "guardar cambios", "versionar"
- Despues de completar tarea
- Al finalizar traduccion o modificacion

---

## Decision Framework: ¿Qué Tipo de Commit?

**Usa este framework para elegir el tipo correcto**:

1. **¿Es nueva funcionalidad o contenido?**
   → `feat` (nueva traducción, nuevo capítulo, nueva feature)

2. **¿Corrige un error o bug?**
   → `fix` (error de traducción, fix build, corrección)

3. **¿Solo cambia documentación del proyecto?**
   → `docs` (README, CONTRIBUTING, doc files)

4. **¿Solo cambia formato/estilo sin lógica?**
   → `style` (indentación, espacios, formato)

5. **¿Reorganiza código sin cambiar comportamiento?**
   → `refactor` (reestructurar sin cambiar función)

6. **¿Actualiza herramientas o build?**
   → `chore` (dependencias, scripts, config)

7. **¿No estás seguro entre dos tipos?**
   → Usar el más específico (feat > fix > docs > chore)

**Regla de oro**: Si añade valor → `feat`, si corrige → `fix`

---

## Trigger Patterns

### Señales Explícitas
- Usuario dice: "haz commit"
- Usuario dice: "guarda los cambios"
- Usuario dice: "commitea esto"
- Usuario pregunta: "¿cómo hago commit?"
- Usuario menciona: "mensaje de commit"

### Señales Implícitas
- Trabajo completado exitosamente
- Build pasa después de cambios
- Usuario dice "listo" o "terminado"
- Contexto indica fin de tarea
- Usuario pregunta "¿qué sigue?"

### Trigger Words
- "commit", "guardar", "versionar"
- "git add", "git commit"
- "mensaje", "commit message"
- "conventional commits"

**Anti-triggers** (NO hacer commit todavía):
- Build falla
- Usuario dice "aún no"
- Trabajo incompleto
- Usuario dice "falta X"
- Cambios experimentales

---

## Self-Check Before Commit

**OBLIGATORIO antes de hacer commit**:

### Pre-Commit Checks
- [ ] ¿El build pasa? (sphinx-build sin errores críticos)
- [ ] ¿Los cambios están relacionados? (un cambio lógico)
- [ ] ¿Revisé los archivos con `git status`?
- [ ] ¿El tipo de commit es correcto?
- [ ] ¿El scope es apropiado?

**Si NO → NO hacer commit todavía**

### During-Commit Checks
- [ ] ¿Mensaje sigue formato conventional commits?
- [ ] ¿Description <72 caracteres?
- [ ] ¿Imperativo presente? (add, fix, update NO added, fixed, updated)
- [ ] ¿Sin punto final en description?
- [ ] ¿Body explica el "por qué" si necesario?

**Si NO → Corregir mensaje**

### Post-Commit Checks
- [ ] ¿Commit aparece en `git log`?
- [ ] ¿Mensaje legible y claro?
- [ ] ¿Un solo commit por cambio lógico?
- [ ] ¿Listos para push o más trabajo?

**Si NO → Considerar `git commit --amend`**

---

## Formato de Commit

```
<type>(<scope>): <description>

[body opcional]

[footer opcional]
```

## Tipos Validos

- **feat** - Nueva funcionalidad (nueva traduccion, nuevo capitulo)
- **fix** - Correccion de bug (error traduccion, fix build)
- **docs** - Solo documentacion (actualizar README)
- **style** - Formato sin cambios funcionales (indentacion)
- **refactor** - Refactorizacion (reorganizar estructura)
- **test** - Tests (nuevos test cases)
- **chore** - Build, tools (actualizar dependencias, scripts)
- **perf** - Performance (optimizar build)

## Scopes Comunes

- **traduccion** - Traduccion de contenido
- **estructura** - Cambios estructurales
- **sphinx** - Configuracion Sphinx
- **scripts** - Scripts de automatizacion
- **metadata** - Gestion de metadata
- **validacion** - Validacion y QA
- **codex** - Configuracion Codex
- **docs** - Documentacion del proyecto

## Reglas

1. Description: max 72 caracteres, imperativo presente, sin punto final
2. NO usar emojis
3. NO agregar co-authored-by sin colaboracion real
4. Tipo y scope en minusculas
5. Body opcional pero recomendado para cambios no triviales

## Ejemplos

### Traduccion Nueva

```
feat(traduccion): agregar seccion arc42 Introduction and Goals

Traduccion completa de seccion 1 de arc42 aplicando modo
de alta fidelidad para preservar estructura tecnica.

Incluye metadata completa y validacion de build.
```

### Fix de Build

```
fix(sphinx): corregir referencia rota en workflow_general.rst

El label procedimientos-validacion no existia, causando
warning en build. Agregado label faltante.
```

### Refactor Estructural

```
refactor(estructura): reorganizar subdirectorios de fundamentos

Movidos archivos de ontologia a _ontologia_terminologia/
para mejor organizacion segun convenciones.

Actualizado index.rst con nueva estructura de toctree.
```

### Actualizacion de Script

```
chore(scripts): actualizar adt_translator con soporte para arc42

Agregado parametro --arc42-section para manejar secciones
especificas del template arc42.
```

### Breaking Change

```
feat(sphinx)!: migrar a Sphinx 7.0

BREAKING CHANGE: Requiere Python 3.11+. Actualizar con
pip install -r requirements.txt.

Beneficios: mejor performance, nuevas directivas.
```

## Convenciones del Proyecto

### Archivos de Traduccion

```
feat(traduccion): agregar [nombre documento] en [categoria]

Documento: [nombre original]
Fuente: [URL o referencia]
Modo: [Alta Fidelidad | Marcado Visual | Enriquecimiento]
Framework: [Diataxis | arc42]
```

### Cambios en Scripts

```
chore(scripts): [descripcion breve]

Script: scripts/[ruta]
Cambios:
- [cambio 1]
- [cambio 2]
```

### Actualizacion de Metadata

```
docs(metadata): actualizar metadata de [seccion]

Archivos afectados: [numero]
Campos actualizados: [lista]
```

## Proceso de Commit

1. Revisar cambios: `git status` y `git diff`
2. Stagear archivos: `git add <archivos>`
3. Commit: `git commit -m "type(scope): description"`
4. O con editor para body: `git commit`
5. Verificar: `git log -1`

## Validacion Pre-Commit

Antes de commit:
- Revisar diff completo
- Verificar cambios atomicos (un cambio logico)
- Confirmar description describe el cambio
- Build exitoso si aplica

Despues de commit:
- Verificar con: `git log -1`
- Si error y no pusheado: `git commit --amend`

## Referencias

Conventional Commits: https://www.conventionalcommits.org/

## Notas

- Commits atomicos: un cambio logico por commit
- Stagear solo archivos relacionados
- Nunca usar `git add .` sin revisar
- Preferir commits frecuentes pequeños sobre grandes

---

## Templates

### commit-message.template

**Ubicación**: `templates/commit-message.template`

**Propósito**: Plantilla completa para crear mensajes de commit siguiendo Conventional Commits

**Contenido**:
- Formato estructurado: type(scope): subject + body + footer
- Guía completa de types (feat, fix, docs, style, refactor, test, chore, perf)
- Scopes comunes del proyecto ADT
- Reglas de formato (imperativo, max 50 chars, sin punto final)
- Ejemplos completos (simples, con body, con breaking changes)
- Instrucciones paso a paso

**Cuándo usar**:
- Primera vez escribiendo commits en el proyecto
- Necesitas recordar formato Conventional Commits
- Quieres asegurar calidad del mensaje
- Trabajas con scopes poco familiares

**Workflow de uso**:
1. Abrir `templates/commit-message.template`
2. Copiar contenido a editor
3. Reemplazar placeholders [type], [scope], [subject], etc.
4. Eliminar líneas de comentarios (#)
5. Copiar mensaje final
6. Usar en `git commit -m "mensaje"` o en editor git

**Ejemplo de uso**:
```bash
# Ver template
cat .codex/skills/commit-helper/templates/commit-message.template

# Usar contenido para crear commit
git commit -m "feat(skills): add commit-message template"
```

**Beneficios**:
- Reduce tiempo recordando formato
- Asegura consistencia en mensajes
- Previene errores comunes (punto final, tiempo verbal incorrecto)
- Incluye scopes específicos del proyecto

---

## Changelog

### v1.2.0 - 2026-02-01 - Templates

**Agregado**:
- Template commit-message.template en templates/
- Sección "Templates" en SKILL.md documentando uso del template

**Contenido del template**:
- Formato completo Conventional Commits
- Guía de types (feat, fix, docs, style, refactor, test, chore, perf)
- Scopes comunes de ADT
- Reglas de formato (imperativo, max 50 chars)
- 3 ejemplos completos (simple, con body, con breaking change)
- Instrucciones paso a paso

**Beneficio**:
- Usuarios tienen referencia rápida para formato correcto
- Reduce tiempo creando mensajes de commit
- Asegura consistencia en todo el proyecto

### v1.1.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y decision-making**:

✅ **Decision Framework** - ¿Qué Tipo de Commit?
- 7 preguntas para elegir tipo correcto
- Regla de oro: "Si añade valor → feat, si corrige → fix"
- Clarifica diferencias entre tipos similares

✅ **Trigger Patterns** - Cuándo hacer commit
- Señales explícitas (usuario dice "haz commit")
- Señales implícitas (trabajo completado, build pasa)
- Trigger words específicos
- Anti-triggers (build falla, trabajo incompleto)

✅ **Self-Check Mechanisms** - 3 niveles de checks
- Pre-Commit (build pasa, cambios relacionados, tipo correcto)
- During-Commit (formato, <72 chars, imperativo)
- Post-Commit (commit en log, legible, listo para push)

**Líneas agregadas**: ~95 líneas

**Beneficio principal**:
- Usuarios eligen tipo de commit correcto
- Previene commits con build roto
- Mensaje sigue conventional commits automáticamente

### v1.0.0 - 2026-01-30
- Versión inicial
- Soporte Conventional Commits
- Ejemplos y convenciones del proyecto
