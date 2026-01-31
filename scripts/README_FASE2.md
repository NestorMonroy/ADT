# Scripts de Corrección Sphinx - FASE 2

**Ubicación**: `/tmp/ADT/scripts/`

Scripts creados durante la corrección incremental de WARNING de Sphinx (FASE 2) y auditoría de scripts.

---

## Scripts de Headers (FASE 2 - Commits 42-46)

### add_h1.py

**Propósito**: Añadir H1 a archivos Markdown que solo tienen frontmatter.

**Problema que resuelve**:
```
WARNING: Document headings start at H2, not H1
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/add_h1.py source/path/to/file.md

# Múltiples archivos
python3 scripts/add_h1.py source/**/*.md
```

**Qué hace**:
1. Lee el archivo Markdown
2. Extrae el `title` del frontmatter YAML
3. Añade un H1 (`#`) después del frontmatter con ese título
4. Guarda el archivo modificado

**Ejemplo**:
```markdown
# Antes
---
title: "Example Page"
---

## First Section

# Después
---
title: "Example Page"
---

# Example Page

## First Section
```

**Validado en**: 23 archivos, 0 errores (Commit 46)

---

### adjust_headers.py

**Propósito**: Ajustar headers para que sean consecutivos después de añadir H1.

**Problema que resuelve**:
```
WARNING: Non-consecutive header level increase; H1 to H3
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/adjust_headers.py source/path/to/file.md

# Múltiples archivos
python3 scripts/adjust_headers.py source/**/*.md
```

**Qué hace**:
1. Verifica que el archivo tenga H1
2. Reduce niveles de headers:
   - `####` (H4) → `###` (H3)
   - `###` (H3) → `##` (H2)
   - `##` (H2) se mantiene
   - `#` (H1) se mantiene

**Ejemplo**:
```markdown
# Antes (no consecutivo)
# H1 Título
### H3 Subsección  ← Salta de H1 a H3

# Después (consecutivo)
# H1 Título
## H2 Subsección  ← Ahora es consecutivo
```

**Validado en**: 13 archivos automáticos + 4 manuales, 0 errores (Commit 46)

---

## Scripts de Validación (Auditoría 2026-01-30)

### find_duplicate_labels.py

**Propósito**: Encontrar labels duplicados en archivos RST/MD.

**Problema que detecta**:
```
WARNING: duplicate label [label_name]
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/find_duplicate_labels.py $(rg -l "^\.\. _" source)
```

**Qué hace**:
- Busca labels RST (`.. _label:`)
- Busca labels MyST (`(label)=`)
- Reporta duplicados con ubicaciones

**Ejemplo de salida**:
```
⚠️  Encontrados 2 labels duplicados:

Label: 'intro' (2 ocurrencias)
  - source/section1.rst:10 (RST)
  - source/section2.md:5 (MyST)
```

---

### find_duplicate_toctree.py

**Propósito**: Encontrar entradas duplicadas en directivas toctree.

**Problema que detecta**:
```
WARNING: toctree contains reference to document 'X' more than once
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/find_duplicate_toctree.py $(rg -l "\.\. toctree::" source)
```

**Qué hace**:
- Analiza bloques toctree
- Detecta entradas duplicadas
- Reporta archivo y entrada duplicada

---

## Scripts de Corrección Automática (Auditoría 2026-01-30)

### fix_unknown_lexers.py

**Propósito**: Corregir lexers desconocidos en code-blocks.

**Problema que resuelve**:
```
WARNING: Pygments lexer name 'plantuml' is not known
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/fix_unknown_lexers.py source/**/*.rst source/**/*.md
```

**Lexers corregidos**:
- `plantuml` / `PlantUML` → `text`
- `atl` / `ATL` → `text`
- `ocl` / `OCL` → `text`

**Basado en**: Corrección manual Lexers (Commits 42-45)

---

### fix_list_spacing.py

**Propósito**: Añadir blank line antes de listas RST.

**Problema que resuelve**:
```
WARNING: Explicit markup ends without a blank line
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/fix_list_spacing.py source/**/*.rst
```

**Qué hace**:
- Detecta párrafos que terminan con `:`
- Añade blank line antes de listas
- Maneja listas con `-`, `*`, `+` y numeradas

---

### fix_list_table_spacing.py

**Propósito**: Añadir blank line entre opciones y contenido en list-table.

**Problema que resuelve**:
```
WARNING: Explicit markup ends without a blank line
```

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/fix_list_table_spacing.py source/**/*.rst
```

**Qué hace**:
- Detecta directivas `.. list-table::`
- Añade blank line después de opciones
- Antes del contenido (`* -`)

---

### fix_glossary_indentation.py

**Propósito**: Corregir indentación en directivas glossary.

**Regla**:
- Términos: 2 espacios
- Definiciones: 4 espacios

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/fix_glossary_indentation.py source/**/*.rst
```

**Qué hace**:
- Detecta directivas `.. glossary::`
- Ajusta indentación de términos (2 espacios)
- Ajusta indentación de definiciones (4 espacios)

---

## Scripts de Utilidades (Auditoría 2026-01-30)

### generar_glosario.py

**Propósito**: Generar glosario consolidado desde múltiples archivos.

**Uso**:
```bash
# Desde /tmp/ADT
python3 scripts/generar_glosario.py source/**/*.rst -o source/glosario.rst
```

**Qué hace**:
- Extrae términos de directivas glossary
- Consolida términos únicos
- Genera archivo glosario.rst

---

## Flujo de Trabajo Headers

Para corregir headers incorrectos, usa ambos scripts en secuencia:

```bash
cd /tmp/ADT

# FASE 1: Añadir H1 desde frontmatter
python3 scripts/add_h1.py source/**/*.md

# FASE 2: Ajustar headers consecutivos
python3 scripts/adjust_headers.py source/**/*.md

# Validar resultado
make html
```

**Resultado esperado**:
- WARNING "headings start at H2/H3" → 0
- WARNING "Non-consecutive header" → 0

---

## Flujo de Trabajo Completo

```bash
cd /tmp/ADT

# 1. Validar duplicados
python3 scripts/find_duplicate_labels.py $(rg -l "^\.\. _" source)
python3 scripts/find_duplicate_toctree.py $(rg -l "\.\. toctree::" source)

# 2. Corregir problemas automáticamente
python3 scripts/fix_unknown_lexers.py source/**/*.rst source/**/*.md
python3 scripts/fix_list_spacing.py source/**/*.rst
python3 scripts/fix_list_table_spacing.py source/**/*.rst
python3 scripts/fix_glossary_indentation.py source/**/*.rst

# 3. Generar glosario (opcional)
python3 scripts/generar_glosario.py source/**/*.rst -o source/glosario.rst

# 4. Validar build
make html
```

---

## Referencias

- **Commits Headers**: 42-46 (Corrección Headers, 47 WARNING)
- **Commit Scripts**: 50 (Ubicación correcta)
- **Commit Auditoría**: 51 (Creación de 7 scripts nuevos)
- **Documentación**: `.codex/skills/sphinx-expert/SKILL.md` v1.5.0
- **Metodología**: `.codex/skills/incremental-correction-methodology/SKILL.md`
- **Validación**: FASE 2 completa, 0 errores introducidos

---

## Notas

- Todos los scripts preservan encoding UTF-8
- Diseñados para uso desde `/tmp/ADT` (directorio raíz del proyecto)
- Aceptan rutas relativas y absolutas
- Incluyen manejo de errores y logging detallado
- Permisos ejecutables configurados
