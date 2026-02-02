# Mejores Practicas de Sphinx

Guia de mejores practicas para desarrollo con Sphinx en el proyecto ADT.

## Estructura de Archivos

### Organizacion de Directorios

BIEN:
```
capitulo/
+-- index.rst (overview del capitulo)
+-- intro.rst (introduccion)
+-- seccion_1.rst
+-- seccion_2.rst
+-- _metadata/ (metadata, no en toctree)
```

MAL:
```
capitulo/
+-- todo_en_un_archivo.rst (demasiado grande)
+-- sin_index.rst (falta estructura)
```

### Tamaño de Archivos

RECOMENDADO:
- Index: 50-200 lineas
- Secciones: 100-500 lineas
- Capitulos completos: Dividir si > 1000 lineas

RAZON: Archivos pequeños son mas faciles de mantener y navegar.

## Markup RST

### Titulos y Secciones

JERARQUIA CONSISTENTE:
```rst
Titulo Documento (nivel 0)
==========================

Seccion Principal (nivel 1)
---------------------------

Subseccion (nivel 2)
~~~~~~~~~~~~~~~~~~~~

Subsubseccion (nivel 3)
^^^^^^^^^^^^^^^^^^^^^^^

Parrafo (nivel 4 - raro)
""""""""""""""""""""""""
```

REGLA: Usar mismos caracteres en todo el proyecto.

### Listas

BIEN:
```rst
- Item 1
- Item 2

 Parrafo adicional indentado.

- Item 3
```

MAL:
```rst
- Item 1
- Item 2
Parrafo sin indentar (rompe lista)
- Item 3
```

### Code Blocks

BIEN:
```rst
.. code-block:: python
 :caption: Ejemplo de codigo
 :linenos:

 def funcion():
 return "hola"
```

MAL:
```rst
```python
codigo
``` (esto es Markdown, no RST)
```

### Admoniciones

BIEN:
```rst
.. note::

 Texto de la nota con indentacion correcta.

.. warning::

 Advertencia importante.
```

MAL:
```rst
.. note:: Texto en misma linea

.. warning::
Texto sin indentar
```

## Toctree

### Profundidad

RECOMENDADO:
```rst
.. toctree::
 :maxdepth: 2
```

EVITAR:
```rst
.. toctree::
 :maxdepth: 5 # Demasiado profundo
```

RAZON: Profundidad > 3 dificulta navegacion.

### Glob Patterns

USAR CUANDO:
- Muchos archivos similares
- Archivos que se agregan frecuentemente

```rst
.. toctree::
 :glob:

 tutorials/*
 howto/*
```

NO USAR CUANDO:
- Orden especifico es importante
- Pocos archivos

### Opciones Utiles

```rst
.. toctree::
 :maxdepth: 2
 :caption: Titulo del TOC
 :numbered: # Numerar secciones
 :titlesonly: # Solo mostrar titulos
 :hidden: # Ocultar TOC del contenido
```

## Cross-References

### Referencias a Documentos

BIEN:
```rst
Ver :doc:`../fundamentos/intro` para mas detalles.
Ver :doc:`workflow general </02_procedimientos/workflow_general>`
```

EVITAR:
```rst
Ver `link <../fundamentos/intro.html>`__ (enlace directo)
```

RAZON: :doc: valida que documento existe.

### Labels y Referencias

DEFINIR LABEL:
```rst
.. _label-unico-descriptivo:

Seccion Objetivo
----------------
```

REFERENCIAR:
```rst
Ver :ref:`label-unico-descriptivo` para detalles.
```

CONVENCION DE NOMBRES:
- snake_case
- Descriptivo
- Prefijo por capitulo: `fundamentos-introduccion`

### Referencias a Glosario

DEFINIR:
```rst
.. glossary::

 ADT
 Arquitectura Documental de Traduccion

 RST
 reStructuredText
```

USAR:
```rst
Ver :term:`ADT` para definicion completa.
```

## Metadata

### Minima

```rst
.. meta::
 :description: Descripcion breve para SEO
 :keywords: palabra1, palabra2, palabra3
```

### Completa

```rst
.. meta::
 :description: Descripcion completa del documento
 :keywords: adt, traduccion, sphinx
 :author: Nombre Autor

:Fecha Creacion: YYYY-MM-DD
:Ultima Modificacion: YYYY-MM-DD
:Version: 1.0.0
:Estado: Draft | Published
:Autor: Nombre
```

## Performance

### Build Paralelo

```bash
# En Makefile
SPHINXOPTS ?= -j auto

# O manualmente
make html SPHINXOPTS="-j 4"
```

### Build Incremental

```bash
# Solo reconstruye cambios
make html

# Full rebuild
make clean html
```

### Cache

Sphinx cachea en `build/doctrees/`. No borrar a menos que problemas.

## Extensiones Utiles

### Estandar

```python
# conf.d.py
extensions = [
 'sphinx.ext.autodoc', # Documentar codigo Python
 'sphinx.ext.intersphinx', # Enlaces a otras docs Sphinx
 'sphinx.ext.todo', # TODOs
 'sphinx.ext.viewcode', # Enlaces a codigo fuente
]
```

### Terceros

```python
extensions = [
 'sphinx_rtd_theme', # Theme ReadTheDocs
 'sphinxcontrib.plantuml', # Diagramas PlantUML
]
```

## Configuracion conf.py

### Basica

```python
project = 'ADT Documentation'
copyright = '2026, ADT Team'
author = 'ADT Team'
version = '1.7'
release = '1.7.1'

language = 'es'
```

### HTML Theme

```python
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
```

### Exclusiones

```python
exclude_patterns = [
 '_build',
 'Thumbs.db',
 '.DS_Store',
 '_metadata', # No compilar metadata
 '**/README.md', # No compilar READMEs
]
```

## Troubleshooting

### Build Lento

SOLUCION:
1. Build paralelo: `-j auto`
2. Build incremental (no `make clean`)
3. Excluir directorios grandes

### Warnings Excesivos

SUPRIMIR SELECTIVAMENTE:
```python
# conf.d.py
suppress_warnings = [
 'image.nonlocal_uri', # URLs de imagenes externas
]
```

### Referencias Rotas

DIAGNOSTICO:
```bash
make linkcheck
```

FIX:
1. Verificar labels existen
2. Verificar paths correctos
3. Actualizar referencias obsoletas

## Antipatrones

### 1. Archivos Demasiado Grandes

EVITAR:
- Un archivo con 2000+ lineas
- Todo un capitulo en un archivo

HACER:
- Dividir en secciones logicas
- Un archivo por seccion principal

### 2. Toctree Desorganizado

EVITAR:
```rst
.. toctree::

 z_archivo
 a_archivo
 m_archivo # Orden aleatorio
```

HACER:
```rst
.. toctree::

 intro
 conceptos
 ejemplos
 conclusiones # Orden logico
```

### 3. Sin Labels

EVITAR:
- Secciones importantes sin labels
- Imposible referenciar desde otros documentos

HACER:
- Agregar labels a secciones principales
- Usar nomenclatura consistente

### 4. Hardcoded URLs

EVITAR:
```rst
Ver `documento <https://misite.com/docs/doc.html>`__
```

HACER:
```rst
Ver :doc:`documento </path/to/doc>`

# O si es externo, usar intersphinx
Ver :doc:`python:library/os`
```

## Checklist de Calidad

Antes de commit:

- [ ] Build exitoso sin errores
- [ ] Warnings revisados y justificados
- [ ] Toctree actualizado
- [ ] Labels agregados a secciones importantes
- [ ] Metadata completa
- [ ] Code blocks con lenguaje especificado
- [ ] Indentacion correcta en admoniciones
- [ ] Cross-references usan :doc: o :ref:
- [ ] Sin hardcoded URLs internas

## Recursos

Documentacion oficial:
- https://www.sphinx-doc.org/
- https://docutils.sourceforge.io/rst.html

Guias:
- source/05_herramientas_medios/sphinx/
- source/09_referencias/cheatsheets/cheatsheet_rst.rst

## Notas

- Estas son RECOMENDACIONES, no reglas absolutas
- Adaptar segun necesidades del proyecto
- Consistencia es mas importante que perfeccion
- Documentar decisiones que desvien de practicas estandar
