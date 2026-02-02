---
name: sphinx-expert
description: "Experto en Sphinx, RST y arquitectura documental. Usar para analisis de estructura, resolucion de problemas de build, optimizacion de markup RST, y decisiones sobre organizacion de contenido."
version: 1.3.0
created: 2026-01-29
updated: 2026-01-30
---

# Sphinx Expert

**Versión**: 1.3.0  
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

## WARNING Management

### Filosofía de Corrección

**Principio fundamental**: Calidad > Velocidad

Durante FASE 2 de corrección (2026-01-30), se validó que:
- Manual puro con commits frecuentes > Scripts sin validación rigurosa
- 0 errores introducidos > velocidad de corrección
- Análisis inicial (30 min) ahorra 3+ horas de trabajo mal enfocado

### Catálogo de WARNING Comunes

#### 1. Labels Duplicados (`duplicate label`)

**Causa**: `autosectionlabel` genera labels automáticos de títulos. Si dos secciones tienen el mismo título, genera duplicados.

**Ejemplo**:
```rst
Contenido          # autosectionlabel → "contenido"
=========

# Más adelante:

Contenido          # autosectionlabel → "contenido" ⚠️ DUPLICADO
=========
```

**Solución**: Labels explícitos únicos

**RST**:
```rst
.. _seccion10-contenido:

Contenido
=========
```

**MyST Markdown**:
```markdown
(section10-content)=
### Content
```

**Estrategia de prefijos**: Use formato `archivo-seccion-nombre` o `componente-seccion-nombre`

**Ejemplos validados**:
- `metadata-estado-traduccion:`
- `arc42-estado-traduccion:`
- `section10-1-content:`
- `hsc-core-razonamiento:`
- `resultscollector-cajas-negras:`

**Referencias**: Ver commits 35-38 (4 archivos, 15 WARNING corregidos)

#### 2. Blank Lines Faltantes

**Causa**: RST requiere blank line después de directivas, listas, code-blocks.

**Patrones comunes**:
```rst
# ❌ MAL
.. note::
   Contenido
Siguiente párrafo

# ✅ BIEN  
.. note::
   Contenido

Siguiente párrafo

# ❌ MAL (enumerated list)
2. **Item**:
 - Subitems
3. **Siguiente**

# ✅ BIEN
2. **Item**:
 - Subitems

3. **Siguiente**

# ❌ MAL (code-block indentation)
.. code-block:: rst

 Título
======

# ✅ BIEN
.. code-block:: rst

 Título
 ======
```

**Reglas**:
1. Blank line DESPUÉS de: `.. note::`, `.. warning::`, `.. code-block::`
2. Blank line ANTES de item siguiente en enumerated list
3. Contenido de code-block COMPLETAMENTE indentado

**Referencias**: Ver commit 34 (7 WARNING corregidos)

#### 3. Headers Incorrectos (`headings start at H3, not H1`)

**Causa**: Documento empieza con H3 (o H2, H4) sin H1 previo.

**Ejemplo**:
```rst
# ❌ MAL - Empieza con H3
Subsección
~~~~~~~~~~

# ✅ BIEN - Añadir H1
Título Principal
================

Subsección
~~~~~~~~~~
```

**Solución**: Añadir H1 descriptivo al inicio del documento.

**Pendiente**: 36 WARNING (commit futuro)

#### 4. Lexers Desconocidos (`is not known`)

**Causa**: `.. code-block:: PlantUML` usa lexer no instalado.

**Solución**: Cambiar a `text` si no hay soporte:
```rst
# ❌ MAL
.. code-block:: PlantUML

# ✅ BIEN
.. code-block:: text
```

**Lexers problemáticos**:
- `PlantUML` (7)
- `plantuml` (3)
- `atl` (2)
- `ocl` (1)

**Pendiente**: 14 WARNING (script seguro recomendado)

#### 5. Imágenes Faltantes (`image file not readable`)

**Causa**: Path con variables Jekyll (`{{site.imageurl}}`) o archivos no existen.

**Ejemplo**:
```rst
# ❌ MAL
.. image:: {{site.imageurl}}/ruta/imagen.png

# ✅ BIEN - Comentar temporalmente
.. # image:: {{site.imageurl}}/ruta/imagen.png
   (Imagen pendiente de conversión)
```

**Pendiente**: 143 WARNING (script simple de comentado)

#### 6. Toctree Glob Pattern

**Causa**: Patrón glob no encuentra archivos.

**Ejemplo**:
```rst
# ❌ MAL
.. toctree::
   :glob:
   
   traduccion/crosscutting_*ejemplo*

# ✅ BIEN - Comentar si no hay archivos
.. .. toctree::
..    :glob:
..
..    traduccion/crosscutting_*ejemplo*

.. note::
   Archivos pendientes de traducción.
```

**Referencias**: Ver commit 33 (1 WARNING corregido)

### Procedimientos de Corrección

#### Procedimiento: Corregir Labels Duplicados

**Input**: Build log con `WARNING: duplicate label`

**Pasos**:

1. **Extraer labels duplicados**
   ```bash
   grep "duplicate label" build.log
   ```

2. **Identificar archivos y líneas**
   ```
   archivo.rst:72: WARNING: duplicate label ...razonamiento
   archivo.rst:144: WARNING: duplicate label ...razonamiento
   ```

3. **Ver contexto de cada ocurrencia**
   ```bash
   # Ver líneas 65-80 y 138-155
   ```

4. **Diseñar prefijos únicos**
   - Primera ocurrencia: `componente-a-razonamiento`
   - Segunda ocurrencia: `componente-b-razonamiento`

5. **Añadir labels explícitos**
   
   **RST**:
   ```rst
   .. _hsc-core-razonamiento:
   
   Razonamiento
   ============
   ```
   
   **MyST**:
   ```markdown
   (section10-content)=
   ### Content
   ```

6. **Commit inmediato**
   ```bash
   git add archivo.rst
   git commit -m "fix: resolver labels duplicados - N WARNING"
   ```

7. **Validar** (opcional: build parcial)

**Tiempo estimado**: 5-10 min por archivo

**Resultado validado**: 15/15 labels corregidos, 0 errores introducidos

#### Procedimiento: Corregir Blank Lines

**Input**: Build log con `ends without a blank line`

**Pasos**:

1. **Extraer archivos afectados**
   ```bash
   grep "ends without" build.log | cut -d: -f1-2
   ```

2. **Ver contexto de línea problemática**

3. **Identificar tipo**:
   - Explicit markup (directiva)
   - Enumerated list
   - Block quote
   - Code-block

4. **Añadir blank line apropiada**
   - Después de directiva
   - Antes de siguiente item en lista
   - Verificar indentación en code-block

5. **Commit por archivo**

**Advertencia**: Archivos UTF-8 pueden complicar edición con `str_replace`. Considerar edición manual directa.

**Resultado parcial**: 7/14 corregidos (commit 34)

#### Procedimiento: Corregir Lexers Desconocidos

**Input**: Build log con `Pygments lexer name '...' is not known`

**Pasos**:

1. **Extraer archivos afectados**
   ```bash
   grep "is not known" build.log | cut -d: -f1 | sort -u
   ```

2. **Identificar lexers problemáticos**
   ```bash
   grep "is not known" build.log | grep -o "lexer name '.*'" | sort -u
   ```
   
   Comunes: `plantuml`, `PlantUML`, `atl`, `ocl`

3. **Cambiar a lexer genérico**
   
   **RST**:
   ```rst
   # Antes
   .. code-block:: plantuml
   
   # Después
   .. code-block:: text
   ```
   
   **Markdown**:
   ```markdown
   # Antes
   ```plantuml
   
   # Después
   ```text
   ```

4. **Aplicar cambio**:
   - Manual para 1-2 archivos (validar patrón)
   - Script para resto si patrón es claro
   - Build final para validar todos

5. **Commit en lotes lógicos** (por carpeta/tipo)

**Tiempo estimado**: 10-15 min para 14 archivos

**Variantes observadas**:
- `plantuml` (minúscula)
- `PlantUML` (capitalizada)
- `atl`, `ocl` (lenguajes de transformación)

**Resultado validado**: 14/14 lexers corregidos (commits 42-45), 0 errores introducidos

**Lección**: Verificar capitalización del lexer en archivos originales.

#### Procedimiento: Corregir Headers Incorrectos

**Input**: Build log con `Document headings start at HX, not H1`

**IMPORTANTE**: Este procedimiento puede introducir WARNING secundarios (`Non-consecutive header`). Planificar en 2 fases.

**FASE 1: Añadir H1**

1. **Extraer archivos afectados**
   ```bash
   grep "headings start at" build.log | cut -d: -f1 | sed 's/\.rst$//' | sort -u
   ```

2. **Identificar frontmatter y title**
   - Archivos MD suelen tener frontmatter YAML con `title`
   - Usar ese title como H1

3. **Añadir H1 después del frontmatter**
   
   **Patrón**:
   ```markdown
   ---
   title: "Example Title"
   ---
   
   # Example Title  ← AÑADIR
   
   ### Existing H3
   ```

4. **Script recomendado** (Python):
   ```python
   # Ver: /tmp/add_h1.py
   # Extrae title de frontmatter
   # Añade H1 después de ---
   ```

5. **Validar con build**
   - Esperado: WARNING "headings start at" corregidos
   - Posible: WARNING "Non-consecutive" nuevos

**FASE 2: Ajustar Headers Consecutivos** (si aparecen WARNING nuevos)

1. **Identificar saltos no consecutivos**
   ```bash
   grep "Non-consecutive" build.log | cut -d: -f1 | sort -u
   ```

2. **Ajustar niveles**:
   - H1 → H3 se convierte en H1 → H2
   - H1 → H4 se convierte en H1 → H2 (bajando todo un nivel)
   
   ```markdown
   # H1 Título
   ### H3  → ## H2  ← CAMBIAR
   #### H4 → ### H3 ← CAMBIAR
   ```

3. **Script recomendado** (Python):
   ```python
   # Ver: /tmp/adjust_headers.py
   # Reduce un nivel: H3→H2, H4→H3
   # Mantiene H1 y H2
   ```

4. **Casos edge manuales**:
   - Algunos archivos pueden no ser capturados
   - Revisar build log final
   - Corregir manualmente (rápido: 1-2 min por archivo)

5. **Build final para validar**

**Tiempo estimado**: 
- Fase 1: 10 min (23 archivos)
- Fase 2: 15 min (13 archivos script + 4 manuales)
- Total: 25 min

**Resultado validado**: 47/47 headers corregidos (commit 46), 0 errores finales

**Efectos secundarios documentados**:
- Fase 1 puede introducir 31 WARNING "Non-consecutive"
- Fase 2 los corrige completamente
- Planificación en 2 fases es correcta

**Scripts creados**:
- `/tmp/add_h1.py`: Añadir H1 desde frontmatter
- `/tmp/adjust_headers.py`: Ajustar niveles consecutivos

**Lección crítica**: Efectos secundarios son esperables. Documentar y planificar corrección.

### Herramientas de Análisis

#### Análisis de Build Log

**Categorizar WARNING**:
```bash
grep "WARNING:" build.log | \
  cut -d: -f4- | \
  sort | uniq -c | \
  sort -rn
```

**Extraer archivos por tipo**:
```bash
# Labels duplicados
grep "duplicate label" build.log | cut -d: -f1 | sort -u

# Blank lines
grep "ends without" build.log | cut -d: -f1 | sort -u

# Headers
grep "headings start at" build.log | cut -d: -f1 | sort -u

# Lexers
grep "is not known" build.log | cut -d: -f1 | sort -u

# Imágenes
grep "image file not readable" build.log | cut -d: -f1 | sort -u
```

### Métricas de Progreso

**Template de seguimiento**:
```
CATEGORÍA X: Nombre (N WARNING)
  Corregidos: M/N (P%)
  Tiempo usado: T minutos
  Commits: C1, C2, ...
  Estado: COMPLETADO/EN PROGRESO/PENDIENTE
```

**Validación**: Verificar que WARNING disminuye después de cada corrección.

### Referencias Cruzadas

- **incremental-correction-methodology**: Para metodología general (7 Protecciones, Trade-offs, Anti-Patrones)
- **commit-helper**: Para formato de commits detallados
- **Lecciones aprendidas**: `.mywork/changes/[timestamp]/LECCIONES-APRENDIDAS.md`

---

## Changelog

### v1.3.0 - 2026-01-30

**Procedimientos Nuevos Añadidos**:
- ✅ "Procedimiento: Corregir Lexers Desconocidos"
  - Patrón simple: plantuml/PlantUML/atl/ocl → text
  - Manual + script para aplicación masiva
  - Variantes de capitalización documentadas
  - Tiempo: 10-15 min para 14 archivos
  - Validado: 14/14 corregidos (commits 42-45)

- ✅ "Procedimiento: Corregir Headers Incorrectos"
  - Proceso en 2 fases (CRÍTICO)
  - Fase 1: Añadir H1 desde frontmatter
  - Fase 2: Ajustar headers consecutivos
  - Scripts Python: add_h1.py, adjust_headers.py
  - Efectos secundarios documentados (31 WARNING temporales)
  - Tiempo: 25 min para 23 archivos
  - Validado: 47/47 corregidos (commit 46)

**Conocimiento Validado (continuación FASE 2)**:
- Lexers: Cambio trivial pero necesita atención a capitalización
- Headers: Efectos secundarios esperables, planificación en 2 fases
- Scripts Python > bash para casos con frontmatter/regex complejo
- Casos edge siempre existen (4 archivos corregidos manualmente)

**Resultados FASE 2 Actualizado**:
- 84/230 WARNING corregidos (36.5%)
- Categorías completadas: 4/7 (Toctree, Labels, Lexers, Headers)
- Commits 42-46: 5 commits adicionales
- 0 errores finales introducidos

**Métricas de Velocidad**:
- Lexers: 10 min (14 WARNING)
- Headers: 25 min (47 WARNING)
- Total sesión: 62 WARNING en 35 min efectivos

**Lecciones Nuevas**:
1. Build al final > builds intermedios (ahorra tiempo)
2. Scripts Python ideales para frontmatter YAML
3. Efectos secundarios se documentan y corrigen en fase 2
4. Validar patrón con 2-3 archivos antes de script masivo

**Scripts Creados**:
- `/tmp/add_h1.py`: Extraer title de frontmatter → H1
- `/tmp/adjust_headers.py`: Bajar niveles (H3→H2, H4→H3)

**Referencias**:
- Commits: 42-45 (Lexers), 46 (Headers)
- Backup: SKILL_backup_v1.2.0.md

### v1.2.0 - 2026-01-30

**Nueva Sección Mayor**:
- ✅ "WARNING Management"
  - Filosofía de corrección: Calidad > Velocidad
  - Catálogo de 6 WARNING comunes con soluciones
  - Procedimientos validados: Labels duplicados, Blank lines
  - Herramientas de análisis (grep, categorización)
  - Métricas de progreso
  - Referencias cruzadas a incremental-correction-methodology

**Conocimiento Validado**:
- Labels duplicados: RST vs MyST, prefijos jerárquicos
- Blank lines: Patrones comunes y soluciones
- Headers, Lexers, Imágenes, Toctree: Catálogo documentado

**Resultados FASE 2**:
- 23/230 WARNING corregidos (10%)
- 0 errores introducidos
- Commits 33-38: 6 commits detallados
- Trade-off validado: Calidad > Velocidad (6x más lento, 0 regresiones)

**Procedimientos Transferibles**:
- Análisis inicial ahorra 3+ horas
- Manual puro con commits frecuentes > Scripts sin validación
- Un archivo = Un commit = Seguridad total

**Referencias**:
- Lecciones aprendidas: LECCIONES-APRENDIDAS.md (743 líneas)
- Metodología general: incremental-correction-methodology v1.0.0
- Work session: FASE 2 corrección WARNING 2026-01-30

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
