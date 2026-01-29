---
name: commit-helper
description: "Ayuda a crear commits siguiendo Conventional Commits. Usar cuando el usuario necesite hacer un commit o escribir un mensaje de commit."
---

# Commit Helper - Conventional Commits

## Cuando usar

- Usuario pide hacer commit
- Se menciona "commit", "guardar cambios", "versionar"
- Despues de completar tarea
- Al finalizar traduccion o modificacion

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
