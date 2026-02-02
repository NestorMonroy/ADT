---
name: sphinx-expert
description: "Experto en Sphinx, RST y arquitectura documental. Usar para analisis de estructura, resolucion de problemas de build, optimizacion de markup RST, y decisiones sobre organizacion de contenido."
version: 1.1.0
created: 2026-01-29
updated: 2026-01-30
---

# Sphinx Expert

**Versión**: 1.1.0  
**Ubicación**: `/tmp/ADT/.codex/skills/sphinx-expert/`  
**Proyecto**: ADT Documentation (ubicado en `/tmp/ADT`)

## ⚠️ RECORDATORIO CRÍTICO

**Proyecto ubicado en**: `/tmp/ADT`

```bash
cd /tmp/ADT  # Siempre verificar
pwd          # Debe mostrar /tmp/ADT
```

## Cuando usar

- Problemas de build
- Decisiones sobre estructura
- Optimizacion de markup RST
- Integracion de extensiones
- Troubleshooting enlaces rotos
- Performance de generacion

---

## Procedimiento de Build Correcto

### ⚠️ REGLA CRÍTICA

**SIEMPRE ejecutar `make clean` ANTES de `make html`**

El build incremental puede ocultar errores. El build limpio garantiza resultados precisos.

### Comando Estándar

```bash
cd /tmp/ADT

# Paso 1: Limpiar (OBLIGATORIO)
make clean

# Paso 2: Build con timeout extendido
timeout 300 make html > .mywork/build-logs/build-TIMESTAMP.txt 2>&1

# Paso 3: Verificar resultado
echo "✅ Build completado" && tail -20 .mywork/build-logs/build-TIMESTAMP.txt
```

### Formato de Timestamp

**OBLIGATORIO**: Cada build debe tener timestamp único

Formato: `YYYY-MM-DD-HH-MM-SS`

Ejemplos:
```bash
build-2026-01-30-16-12-39.txt
build-fase1-2026-01-30.txt
build-final-2026-01-30-18-45-22.txt
```

### Ejemplo Completo

```bash
cd /tmp/ADT

# Generar timestamp
TIMESTAMP=$(date "+%Y-%m-%d-%H-%M-%S")
BUILD_LOG=".mywork/build-logs/build-${TIMESTAMP}.txt"

# Build limpio
make clean
timeout 300 make html > "$BUILD_LOG" 2>&1

# Verificar
echo "✅ Build guardado en: $BUILD_LOG"
tail -20 "$BUILD_LOG"
```

### Análisis de Resultados

```bash
# Contar issues
LOG=".mywork/build-logs/build-TIMESTAMP.txt"

echo "CRITICAL: $(grep "CRITICAL:" "$LOG" | wc -l)"
echo "ERROR:    $(grep "ERROR:" "$LOG" | wc -l)"
echo "WARNING:  $(grep "WARNING:" "$LOG" | wc -l)"

# Ver mensaje final
grep -E "build (succeeded|finished)" "$LOG" | tail -1
```

### Cuándo NO Hacer Build

- **Durante correcciones múltiples**: Esperar a completar TODAS las correcciones antes del build final
- **Sin make clean previo**: El cache puede ocultar problemas
- **Sin timestamp**: Imposible rastrear builds específicos

### Cuándo SÍ Hacer Build

- **Después de completar fase de correcciones**: Validar impacto
- **Antes de commits importantes**: Asegurar que no hay regresiones
- **Al finalizar trabajo**: Build final limpio para documentar

---

## Conocimientos RST Fundamentales

### ¿Qué es una Transition?

**Definición**: Una "transition" en RST es una línea de al menos 4 caracteres repetidos (como `====`, `----`, etc.) que **NO** es un underline de título.

**Problema común**: `ERROR: Document or section may not begin with a transition`

**Causa**: Línea de separación `====` al inicio del documento sin texto previo.

**Ejemplos**:

```rst
❌ MAL (transition al inicio):
====

Título del Documento
====================

✅ BIEN (sin transition inicial):
Título del Documento
====================
```

**Solución**: Eliminar la línea de separación inicial.

```bash
# Eliminar transition en línea 1
sed -i '1{/^====/d;}' archivo.rst
```

### Underlines de Títulos

**Regla**: El underline DEBE tener la misma longitud que el texto del título.

```rst
❌ MAL (underline corto):
Título Largo del Documento
========================     ← 24 caracteres, título tiene 27

✅ BIEN (underline correcto):
Título Largo del Documento
===========================  ← 27 caracteres, igual que título
```

**Solución**: Contar caracteres y ajustar underline.

```bash
# Contar caracteres de título
echo "Título Largo del Documento" | wc -c
# Resultado: 27

# Crear underline del mismo largo
echo "Título Largo del Documento" | sed 's/.=/g'
```

### Jerarquía de Headers

**Niveles en RST** (orden común):

```rst
H1 (Título Principal)
=====================

H2 (Sección)
------------

H3 (Subsección)
~~~~~~~~~~~~~~~

H4 (Sub-subsección)
^^^^^^^^^^^^^^^^^^^
```

**Regla**: Documentos deben empezar con H1, no con H2, H3 o H4.

**Problema común**: `WARNING: Document headings start at H3, not H1`

**Solución**: Añadir H1 al inicio o convertir primer header a H1.

### Indentación en Directivas

**Regla**: El contenido de directivas DEBE estar indentado (usualmente 3-4 espacios).

```rst
❌ MAL (sin indentar):
.. note::
Texto de la nota

✅ BIEN (indentado 3 espacios):
.. note::

   Texto de la nota
```

### Code Blocks

**Regla**: Contenido de code-blocks DEBE estar indentado (3 espacios típico).

```rst
❌ MAL (sin indentar):
.. code-block:: python

def funcion():
    return True

✅ BIEN (indentado 3 espacios):
.. code-block:: python

   def funcion():
       return True
```

### List-Tables

**Regla**: Options y contenido deben estar indentados correctamente.

```rst
❌ MAL (options sin indentar):
.. list-table::
:header-rows: 1

   * - Header 1
     - Header 2

✅ BIEN (options indentadas):
.. list-table::
   :header-rows: 1

   * - Header 1
     - Header 2
```

**Regla de celdas**: Cada celda necesita mismo número de items.

```rst
❌ MAL (row 1 tiene 3 celdas, row 2 tiene 2):
   * - Col1
     - Col2
     - Col3
   * - Data1
     - Data2

✅ BIEN (ambas rows tienen 3 celdas):
   * - Col1
     - Col2
     - Col3
   * - Data1
     - Data2
     - Data3
```

### Blank Lines (Líneas en Blanco)

**Regla**: Directivas, listas y block quotes requieren línea en blanco después.

```rst
❌ MAL (sin blank line):
.. note::
   Contenido de nota
Siguiente párrafo

✅ BIEN (con blank line):
.. note::
   Contenido de nota

Siguiente párrafo
```

**Warnings comunes**:
- `Block quote ends without a blank line`
- `Explicit markup ends without a blank line`
- `Enumerated list ends without a blank line`

**Solución**: Añadir línea vacía después de la directiva/lista.

---

## Capacidades

### 1. Analisis Estructural

Evalua:
- Jerarquia de toctree
- Nomenclatura de archivos
- Profundidad de anidamiento
- Referencias cruzadas
- Indices y glosarios

### 2. Resolucion de Build Issues

Errores comunes:
- WARNING: reference target not found
- ERROR: unknown directive type
- WARNING: toctree contains reference to nonexisting document
- ERROR: duplicate explicit target name

PROCESO:
1. Identificar error en output
2. Localizar archivo:linea
3. Diagnosticar causa raiz
4. Proponer fix minimo
5. Validar

### 3. Optimizacion RST

PATRONES RECOMENDADOS:

Enlaces:
```rst
BIEN:
:doc:`../fundamentos/index`
:ref:`label-unico`

MAL:
`link <../fundamentos/index.html>`__
```

Admoniciones:
```rst
BIEN:
.. note::

   Texto de la nota.

MAL:
.. note:: Texto en misma linea
```

Listas:
```rst
BIEN:
- Item 1
- Item 2

  Con parrafo adicional indentado.

MAL:
- Item 1
- Item 2
Parrafo sin indentar (rompe lista)
```

### 4. Toctree Management

PRINCIPIOS:
1. Un index.rst por directorio
2. Toctree en cada index.rst
3. Profundidad maxima: 3 niveles
4. Glob patterns para muchos archivos

EJEMPLO:
```rst
.. toctree::
   :maxdepth: 2
   :caption: Fundamentos
   :glob:

   fundamentos/index
   fundamentos/conceptos/*
```

### 5. Cross-References

TIPOS:
```rst
:doc:`path/to/document`      (documento)
:ref:`label-name`            (label)
:term:`termino`              (glosario)
:download:`archivo.pdf`      (descarga)
```

LABELS:
```rst
.. _label-unico:

Seccion Objetivo
----------------
```

REFERENCIAS:
```rst
Ver :ref:`label-unico` para mas detalles.
```

### 6. Metadata Management

```rst
.. meta::
   :description: Descripcion para SEO
   :keywords: palabra1, palabra2
   :author: Nombre Autor

:Fecha Creacion: YYYY-MM-DD
:Autor: Nombre
:Version: 1.0.0
:Estado: Draft | Published
```

## Troubleshooting Comun

### ERROR: Unknown directive type "note"

FIX:
```rst
MAL:
.. note:: Texto

BIEN:
.. note::

   Texto con indentacion.
```

### WARNING: reference target not found

FIX:
1. Buscar definicion del label
2. Verificar typos
3. Confirmar que esta en scope

```rst
# Definir
.. _label-correcto:

# Referenciar
:ref:`label-correcto`
```

### WARNING: toctree contains reference to nonexisting

FIX:
1. Verificar que archivo existe
2. Verificar path relativo correcto
3. Verificar que no esta en exclude_patterns

## Configuracion Sphinx

```python
# conf.d.py
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
```

## Performance Optimization

```bash
# Parallel build
make html SPHINXOPTS="-j 4"

# Incremental build
make html  # Solo reconstruye cambios

# Limpiar cache
make clean
```

## Reglas preventivas (evitar regresiones)

### Reglas de formato RST
- **Listas**: deja una línea en blanco antes de listas que siguen a un párrafo con `:`. Usa `scripts/fix_list_spacing.py`.
- **List-table**: siempre agrega una línea en blanco entre opciones y filas. Usa `scripts/fix_list_table_spacing.py`.
- **Glossary**: términos con 2 espacios y definiciones con 4 espacios de indentación. Usa `scripts/fix_glossary_indentation.py`.
- **Lexers desconocidos**: usar `.. code-block:: text` en lugar de `plantuml/atl/ocl` salvo que haya soporte instalado. Usa `scripts/fix_unknown_lexers.py`.

### Reglas de estructura
- **Toctree**: el índice raíz solo referencia `index.rst` por sección; el detalle vive en los índices internos.
- **Labels**: cada `.. _label:` debe ser único en el árbol `source/`.

### Checklist rápido
1. Ejecutar scripts de normalización en archivos tocados.
2. Validar duplicados de toctree y labels:
   - `python scripts/find_duplicate_toctree.py $(rg -l ".. toctree::" source)`
   - `python scripts/find_duplicate_labels.py $(rg -l "^.. _" source)`
3. Ejecutar tests de scripts relevantes con `pytest -q`.

## Scripts Usados

- scripts/validar_estructura.sh
- Makefile (html, clean, linkcheck)

## Referencias

- source/05_herramientas_medios/sphinx/
- source/07_guias_uso/troubleshooting.rst
- https://www.sphinx-doc.org/

## Notas

- Hacer backup antes de refactorings
- Validar build despues de cambios
- Documentar decisiones arquitectonicas
- Mantener coherencia con ADT

---

## Changelog

### v1.1.0 - 2026-01-30

**Nuevas Secciones**:
- ✅ "Procedimiento de Build Correcto"
  - Regla crítica: make clean ANTES de make html
  - Comando estándar con timeout 300
  - Timestamps OBLIGATORIOS en cada build
  - Cuándo hacer y NO hacer builds
  - Ejemplo completo de build con timestamp
  - Análisis de resultados

- ✅ "Conocimientos RST Fundamentales"
  - ¿Qué es una transition? (con ejemplos)
  - Underlines de títulos (longitud exacta)
  - Jerarquía de headers (H1, H2, H3, H4)
  - Indentación en directivas
  - Code blocks (3 espacios)
  - List-tables (indentación correcta)
  - Blank lines obligatorias

**Actualizaciones**:
- ✅ Añadido recordatorio crítico: proyecto en /tmp/ADT
- ✅ Versión 1.0.0 → 1.1.0
- ✅ Frontmatter con created/updated dates
- ✅ Backup creado: SKILL_backup_v1.0.0.md

**Razón de Actualización**:
- Necesidad identificada durante corrección manual de 1,123 issues Sphinx
- Documentar procedimiento correcto de build (evitar errores comunes)
- Consolidar conocimientos RST descubiertos durante correcciones
- Prevenir regresiones futuras

**Referencias**:
- Work session: corrección completa manual 2026-01-30
- Issues corregidos: 891 issues (79% del total)
- Aprendizajes documentados para futuras correcciones

### v1.0.0 - 2026-01-29

- Versión inicial
- Capacidades base de Sphinx expert
- Troubleshooting común
- Reglas preventivas
