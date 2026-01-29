# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# ADT / ADT42 - Arc42-Diátaxis-Traducción
# Sistema de Traducción Técnica + Documentación estructurada
# Versión 1.0.0
#
# Layout del proyecto (decisión final):
#
#   repo_root/
#   ├─ source/
#   │  ├─ conf.py
#   │  ├─ _templates/
#   │  ├─ _static/
#   │  └─ index.rst / index.md
#   ├─ _build/            (se genera aquí)
#   ├─ Makefile
#   ├─ scripts/
#   └─ tools/
#
# Nota:
# - templates_path y html_static_path son relativos al SOURCEDIR (source/).
# - Este conf.py evita depender del "cwd" (directorio desde donde se ejecuta make).
# - Incluye extensiones opcionales instaladas por pip.
# - PlantUML se habilita, pero la configuración está blindada: si no existe el JAR,
#   no rompe el build (solo imprime WARNING).

# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path

# Ruta determinística (no depende del directorio desde donde se ejecute Sphinx)
# source/conf.py -> source/
SOURCE_DIR = Path(__file__).resolve().parent
# repo_root = parent de source/
REPO_ROOT = SOURCE_DIR.parent

# Path setup necesario para autodoc (documentar código Python)
# Permite importar módulos del proyecto para generar documentación automática
#
# Ejemplo (cuando exista código a documentar):
#   sys.path.insert(0, str(REPO_ROOT / "backend"))
#
# Por ahora, insertamos el root del repo como base razonable.
sys.path.insert(0, str(REPO_ROOT))

# -- Información General del Proyecto ----------------------------------------

project = "ADT - Procedimientos de Traducción Técnica"
copyright = "2026, Equipo ADT"
author = "Equipo ADT"

# Versión del Proyecto
version = "1.0"
release = "1.0.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension names here, as strings
extensions = [
    # Extensiones base (navegación, links, calidad de documentación)
    "sphinx.ext.intersphinx",       # Link to other projects' documentation
    "sphinx.ext.todo",              # Support for todo items
    "sphinx.ext.viewcode",          # Add links to highlighted source code
    "sphinx.ext.autosectionlabel",  # Auto-generate section labels

    # Extensiones para documentar código Python (listas para usarse cuando aplique)
    "sphinx.ext.autodoc",           # Auto-generate documentation from docstrings
    "sphinx.ext.napoleon",          # Support for NumPy and Google style docstrings

    # Extensiones de interactividad/diseño
    "sphinx_design",                # Design elements (cards, tabs, etc.)
    "sphinx_copybutton",            # Copy button for code blocks
    "sphinx_tabs.tabs",             # Tabs support
    "sphinx_toolbox.collapse",      # Secciones colapsables
    "notfound.extension",           # Página 404 personalizada
    "myst_parser",                  # Markdown support
    "sphinx_prompt",                # Prompts de consola (ojo: no 'sphinx-prompt')
    "sphinxcontrib.spelling",       # Corrector ortográfico (requiere tooling extra)
    "sphinxcontrib.plantuml",       # PlantUML (requiere jar + java)
]

# -- Configuración de Autodoc ------------------------------------------------
# Generar automáticamente documentación de miembros
autodoc_default_options = {
    "members": True,               # Documentar miembros
    "member-order": "bysource",    # Orden según aparecen en el código
    "special-members": "__init__", # Incluir __init__
    "undoc-members": False,        # Cambiar a True si quieres incluir sin docstring
    "exclude-members": "__weakref__",
}

# Configuración de Napoleon (docstrings estilo Google/NumPy)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Configuración de Archivos -----------------------------------------------

templates_path = ["_templates"]

# List of patterns to ignore
exclude_patterns = [
    "_build",      # por si alguien genera build dentro de source/
    "Thumbs.db",
    ".DS_Store",
    ".venv",
    "venv",
    ".git",
]

# Si usas .md y .rst mezclados (opcional):
# source_suffix = {
#     ".rst": "restructuredtext",
#     ".md": "markdown",
# }

# -- Configuración de Lenguaje -----------------------------------------------

language = "es"
html_search_language = "es"

# Dominio primario (útil para documentación de APIs / roles de Python)
primary_domain = "py"

# -- Estética y Resaltado ----------------------------------------------------

pygments_style = "sphinx"

# Comillas tipográficas inteligentes
smartquotes = True
smartquotes_action = "De"  # (D)ashes y (e)llipses

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

html_theme_options = {
    "light_css_variables": {
        "color-background-primary": "#F2F6F8",  # --adt-color-bg
        "color-foreground-primary": "#2A2F33",  # --adt-color-text

        "color-brand-primary": "#104E5E",       # --adt-color-primary-text (permitido para texto)
        "color-brand-content": "#104E5E",

        "color-background-border": "rgba(42, 47, 51, 0.15)",
        "color-background-secondary": "#E8EFF3",

        # IMPORTANTE: fuera el verde-lima
        "color-code-background": "rgba(11, 60, 73, 0.06)",
        "color-code-foreground": "#2A2F33",
    },
    "dark_css_variables": {
        "color-background-primary": "#0B3C49",  # --adt-color-petroleum-800
        "color-foreground-primary": "#F2F6F8",

        "color-brand-primary": "#6FAEC7",       # --adt-color-accent-500 (OK en oscuro)
        "color-brand-content": "#6FAEC7",

        "color-background-border": "rgba(111, 174, 199, 0.35)",
        "color-background-secondary": "rgba(255, 255, 255, 0.04)",

        "color-code-background": "rgba(242, 246, 248, 0.08)",
        "color-code-foreground": "#F2F6F8",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}



html_title = f"{project} v{version}"
html_short_title = "ADT Traducción"

html_static_path = ["_static"]

# Archivos CSS y JS personalizados (si existen)
html_css_files = [
    "css/custom.css",
]
html_js_files = [
    "js/custom.js",
]

# Custom sidebar templates
# IMPORTANTE:
#   Si se mantiene esta configuración, deben existir:
#     source/_templates/sidebar/brand.html
#     source/_templates/sidebar/search.html
#     source/_templates/sidebar/scroll-start.html
#     source/_templates/sidebar/navigation.html
#     source/_templates/sidebar/scroll-end.html
#
# Si aún no existen esos archivos, comenta html_sidebars para usar defaults del tema.
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}



notfound_urls_prefix = ""  # o el prefijo real si publicas en /repo/
notfound_template = "404.html"
notfound_no_urls_prefix = False
# Mostrar información de Sphinx
html_show_sphinx = True

# No copiar archivos fuente al build
html_copy_source = False

# Logo y Favicon (descomentar cuando existan archivos)
# html_favicon = "_static/img/favicon.ico"
# html_logo = "_static/img/logo.svg"

# -- Extension configuration -------------------------------------------------

# sphinx.ext.autosectionlabel
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# sphinx.ext.todo
todo_include_todos = True

# sphinx.ext.intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# sphinx-copybutton
# Excluir prompts y salidas de consola
copybutton_exclude = ".linenos, .gp, .go"

# Configuración de prompts (regex)
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = True

# myst_parser
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "tasklist",
]

# -- Configuración del Corrector Ortográfico ---------------------------------
# Nota:
#   sphinxcontrib-spelling puede requerir tooling extra (pyenchant/diccionarios).
#   Se deja configurado; si falla el builder de spelling, ajusta el entorno.
spelling_word_list_filename = "spelling_wordlist.txt"
spelling_exclude_patterns = []

# -- PlantUML configuration ---------------------------------------------------
# Contrato del proyecto:
#   - Java portable: tools/java/jdk-17/
#   - PlantUML jar : tools/plantuml.jar
#
# Objetivo:
#   No depender de JAVA_HOME/PATH global.
#
# Comportamiento:
#   - Si existe tools/plantuml.jar, se configura "plantuml".
#   - Si no existe, no se rompe el build (solo WARNING).

TOOLS_DIR = REPO_ROOT / "tools"
PLANTUML_JAR = TOOLS_DIR / "plantuml.jar"
JAVA_WIN = TOOLS_DIR / "java" / "jdk-17" / "bin" / "java.exe"
JAVA_NIX = TOOLS_DIR / "java" / "jdk-17" / "bin" / "java"

def _q(p: Path) -> str:
    # Cita paths con espacios (Windows)
    return f'"{str(p)}"'

if PLANTUML_JAR.exists():
    if JAVA_WIN.exists():
        java_bin = _q(JAVA_WIN)
    elif JAVA_NIX.exists():
        java_bin = _q(JAVA_NIX)
    else:
        # Fallback a java del sistema (si existe)
        java_bin = "java"

    plantuml = f"{java_bin} -jar {_q(PLANTUML_JAR)}"
else:
    print(f"[conf.py] WARNING: No existe {PLANTUML_JAR}. PlantUML deshabilitado.")

# -- Custom configuration ----------------------------------------------------

# Numeración de figuras y tablas
numfig = True
numfig_format = {
    "figure": "Figura %s",
    "table": "Tabla %s",
    "code-block": "Listado %s",
    "section": "Sección %s",
}

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": "",
    "figure_align": "htbp",
}

latex_engine = "pdflatex"
latex_use_xindy = False

latex_elements["preamble"] = r"""
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{lmodern}
"""

latex_documents = [
    (
        "index",
        "ADT-Traduccion.tex",
        "ADT - Procedimientos de Traducción Técnica",
        "Equipo ADT",
        "manual",
    ),
]

# -- Configuración de Salida Man Pages ---------------------------------------

man_pages = [
    (
        "index",
        "adt-traduccion",
        "ADT - Procedimientos de Traducción Técnica",
        ["Equipo ADT"],
        1,
    )
]

# -- Configuración de Salida Texinfo -----------------------------------------

texinfo_documents = [
    (
        "index",
        "ADT-Traduccion",
        "ADT - Procedimientos de Traducción Técnica",
        "Equipo ADT",
        "ADT-Traduccion",
        "Sistema de traducción técnica.",
        "Miscellaneous",
    ),
]

# -- Configuración de traducción / i18n --------------------------------------

locale_dirs = ["locale/"]
gettext_compact = False

# -- Configuración personalizada ADT -----------------------------------------

adt_project_info = {
    "name": "ADT",
    "full_name": "Arc42-Diátaxis-Traducción",
    "version": "1.0.0",
    "components": ["arc42", "diataxis", "traduccion", "biblioteca"],
    "frameworks": {
        "arc42": "12 secciones arquitectónicas",
        "diataxis": "4 tipos de documentación",
        "traduccion": "10 secciones metodológicas",
    },
}

# Configuración de glosarios
glossary_term_types = ["term", "technical-term", "acronym", "concept"]

# Configuración de referencias
ref_patterns = {
    "procedimiento": r"PROC_\d{3}",
    "estandar": r"STD_\d{3}",
    "regla": r"RT_\d{3}",
    "escenario": r"ESC_\d{3}",
}

# Configuración de traducción
translation_config = {
    "source_language": "en",
    "target_language": "es-MX",
    "preserve_technical_terms": True,
    "first_appearance_format": "español (:term:`inglés`)",
    "subsequent_format": "español",
}
