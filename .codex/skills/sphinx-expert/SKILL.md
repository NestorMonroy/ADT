---
name: sphinx-expert
description: "Experto en Sphinx, RST y arquitectura documental. Usar para analisis de estructura, resolucion de problemas de build, optimizacion de markup RST, y decisiones sobre organizacion de contenido."
---

# Sphinx Expert

## Cuando usar

- Problemas de build
- Decisiones sobre estructura
- Optimizacion de markup RST
- Integracion de extensiones
- Troubleshooting enlaces rotos
- Performance de generacion

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
# conf.py
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
