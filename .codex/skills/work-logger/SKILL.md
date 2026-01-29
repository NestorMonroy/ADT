---
name: work-logger
description: "Sistema de logging estructurado de trabajo. Usar cuando se complete tarea importante, traduccion, o implementacion que deba quedar documentada."
---

# Work Logger - Documentacion de Trabajo

## Cuando usar

- Usuario pide "documentar esto"
- Al completar traduccion significativa
- Despues de resolver problema complejo
- Al finalizar feature importante
- Para registrar decisiones tecnicas
- Cuando algo debe quedar para referencia futura

## Ubicacion

`.mywork/work-logs/YYYY-MM-DD-titulo.md`

## Proceso

### 1. Determinar si Merece Log

SI documentar:
- Traducciones completas
- Scripts nuevos o modificados
- Resolucion de problemas complejos
- Cambios arquitectonicos
- Decisiones importantes
- Workflows nuevos

NO documentar:
- Typos corregidos
- Cambios triviales de formato
- Updates menores

### 2. Generar Nombre

```bash
DATE=$(date "+%F") # YYYY-MM-DD
TITULO="breve-descripcion-kebab-case" # max 50 chars
ARCHIVO=".mywork/work-logs/${DATE}-${TITULO}.md"
```

Ejemplos:
- 2026-01-28-traducir-arc42-quality-requirements.md
- 2026-01-28-resolver-problema-build-sphinx.md

### 3. Usar Template

Ver: `templates/work-log.md.template`

Secciones principales:
- Resumen ejecutivo (OBLIGATORIO)
- Trabajo realizado (OBLIGATORIO)
- Archivos afectados (OBLIGATORIO)
- Decisiones tomadas (opcional)
- Problemas encontrados (opcional)
- Aprendizajes (opcional)

### 4. Reglas de Contenido

SEGURIDAD:
- NUNCA passwords, API keys, tokens
- Usar placeholders: `<valor de API_KEY>`

FORMATO:
- Markdown con sintaxis correcta
- Bloques de codigo con lenguaje especificado
- Titulos jerarquicos

LENGUAJE:
- Idioma principal: Español
- Terminos tecnicos: Sin traducir
- Comandos y rutas: Literales

### 5. Escribir Archivo

```bash
mkdir -p .mywork/work-logs

cat > .mywork/work-logs/YYYY-MM-DD-titulo.md <<'EOF'
[contenido del log]
EOF
```

### 6. Commit

```bash
git add .mywork/work-logs/YYYY-MM-DD-titulo.md
git commit -m "docs(work-log): documentar [trabajo realizado]"
```

## Template Basico

```markdown
# YYYY-MM-DD - Titulo del Trabajo

Fecha: YYYY-MM-DD HH:MM
Autor: [Nombre]
Proyecto: ADT Documentation

## Resumen Ejecutivo

[1-2 parrafos describiendo que se hizo y por que]

## Trabajo Realizado

### Paso 1: [Nombre]
[Descripcion]

```bash
comandos
```

[Resultado]

## Archivos Afectados

Creados:
- path/file.rst - [Descripcion]

Modificados:
- path/existing.rst - [Cambio]

## Aprendizajes

1. [Leccion 1]
2. [Leccion 2]

---

Tags: #tag1 #tag2
Estado: Completado
```

## Ejemplos

### Ejemplo: Traduccion

```markdown
# 2026-01-28 - Traduccion de arc42 Quality Requirements

Fecha: 2026-01-28 14:30
Autor: AI Assistant
Proyecto: ADT Documentation

## Resumen Ejecutivo

Traduccion completa de la seccion 10 del template arc42 (Quality
Requirements) del ingles al español, aplicando modo de Alta Fidelidad.

## Trabajo Realizado

### Paso 1: Analisis
Analice estructura del documento original.

```bash
python scripts/analizar_seccion.py \
 source/biblioteca/arc42/sections/10_quality_requirements/
```

### Paso 2: Traduccion
```bash
python scripts/traduccion/arc42_scraper_python.py \
 --section 10 \
 --mode alta_fidelidad
```

## Archivos Afectados

Creados:
- source/biblioteca/arc42/sections/10_quality_requirements/index.rst

Modificados:
- source/biblioteca/arc42/index.rst

## Resultados

- [x] Build exitoso
- [x] Linkcheck OK
- [x] Metadata completa

---

Tags: #traduccion #arc42
Estado: Completado
```

### Ejemplo: Resolucion de Problema

```markdown
# 2026-01-28 - Resolver ERROR Referencia Circular

## Resumen Ejecutivo

Resolucion de error critico en build causado por referencia
circular entre fundamentos/index.rst y metodologias/index.rst.

## Problemas Encontrados

### Problema: Referencia Circular
Sintomas: ERROR: circular toctree references

Causa: fundamentos/index.rst -> _metodologias/index.rst ->
fundamentos/index.rst

Solucion: Elimine toctree de _metodologias/index.rst

Prevencion: No usar toctree hacia arriba en jerarquia

## Archivos Afectados

Modificados:
- source/01_fundamentos/_metodologias/index.rst

## Aprendizajes

1. toctree debe formar DAG
2. Usar :doc: para refs hacia arriba

---

Tags: #bugfix #sphinx
Estado: Completado
```

## Busqueda en Logs

```bash
# Por tag
grep -r "#traduccion" .mywork/work-logs/

# Por termino
grep -r "arc42" .mywork/work-logs/

# Listar recientes
ls -lt .mywork/work-logs/ | head -10
```

## Mantenimiento

Archivar logs antiguos:

```bash
# Crear directorio archivo
mkdir -p .mywork/work-logs/archive/2025/

# Mover logs viejos (> 6 meses)
mv .mywork/work-logs/2025-*.md .mywork/work-logs/archive/2025/
```

## Notas

- Work logs son para HUMANOS, no parseo
- Priorizar claridad sobre brevedad
- Incluir suficiente contexto
- Documentar decisiones NO obvias
- Escribir pensando en "yo del futuro"
