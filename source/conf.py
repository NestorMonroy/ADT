# -*- coding: utf-8 -*-
"""
Sphinx configuration file (Enterprise Orchestrator)

Este archivo:
- Orquesta la configuración modular ubicada en source/conf.d/
- Aplica políticas enterprise vía variables de entorno
- No contiene lógica de negocio compleja
- Mantiene separación estricta de responsabilidades

Contrato:
- Se ejecuta siempre desde el repo root (/ADT)
- conf.d es un paquete explícito (tiene __init__.py)
"""

from __future__ import annotations

import os
import warnings
from pathlib import Path

from pygments.lexers.special import TextLexer


# =============================================================================
# 1) Paths determinísticos + sys.path
# =============================================================================

from conf.d import paths as paths_cfg

SOURCE_DIR: Path = paths_cfg.SOURCE_DIR
REPO_ROOT: Path = paths_cfg.REPO_ROOT


# =============================================================================
# 2) Extensiones + políticas enterprise (profile/strict/offline)
# =============================================================================

from conf.d import extensions as ext_cfg

extensions = ext_cfg.extensions
warningiserror = ext_cfg.warningiserror


# Silenciar warnings conocidos de terceros (ruido no accionable)
warnings.filterwarnings(
    "ignore",
    message="The str interface for _JavaScript objects is deprecated.",
    category=DeprecationWarning,
)


# =============================================================================
# 3) Información general del proyecto
# =============================================================================

project = "ADT - Procedimientos de Traducción Técnica"
copyright = "2026, Equipo ADT"
author = "Equipo ADT"

version = "1.0"
release = "1.0.0"


# =============================================================================
# 4) Configuración general
# =============================================================================

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".venv",
    "venv",
    ".git",
    "_archivados/**",
    "**/*BACKUP*",
    "**/*backup*",
    "**/*.bak",
    "**/*~",
]

language = "es"
html_search_language = "es"
primary_domain = "py"


# =============================================================================
# 5) Resaltado y lexers (blindaje DSLs)
# =============================================================================

pygments_style = "sphinx"

pygments_lexers = {
    "plantuml": TextLexer,
    "atl": TextLexer,
    "ocl": TextLexer,
}


# =============================================================================
# 6) Tema (Furo) + assets estáticos
# =============================================================================

from conf.d import theme_furo as theme_cfg

html_theme = theme_cfg.html_theme
html_theme_options = theme_cfg.html_theme_options
html_title = theme_cfg.html_title
html_short_title = theme_cfg.html_short_title
html_static_path = theme_cfg.html_static_path
html_css_files = theme_cfg.html_css_files
html_js_files = theme_cfg.html_js_files


# =============================================================================
# 7) MyST (Markdown) + smartquotes + suppress_warnings
# =============================================================================

from conf.d import myst as myst_cfg

myst_enable_extensions = myst_cfg.myst_enable_extensions
myst_heading_anchors = myst_cfg.myst_heading_anchors
myst_ref_domains = getattr(myst_cfg, "myst_ref_domains", ["std", "py"])

smartquotes = myst_cfg.smartquotes
smartquotes_action = myst_cfg.smartquotes_action

suppress_warnings = list(getattr(myst_cfg, "suppress_warnings", []))

# Supresión adicional solo si NO estamos en strict
if not ext_cfg.STRICT:
    suppress_warnings.extend(
        [
            "ref.doc",
            "ref.ref",
            "toc.not_included",
            "toc.secnum",
            "toc",
        ]
    )


# =============================================================================
# 8) Copybutton
# =============================================================================

from conf.d import copybutton as copy_cfg

copybutton_exclude = copy_cfg.copybutton_exclude
copybutton_prompt_text = copy_cfg.copybutton_prompt_text
copybutton_prompt_is_regexp = copy_cfg.copybutton_prompt_is_regexp
copybutton_only_copy_prompt_lines = copy_cfg.copybutton_only_copy_prompt_lines


# =============================================================================
# 9) Autodoc / Napoleon / Todo
# =============================================================================

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": False,
    "exclude-members": "__weakref__",
}

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

todo_include_todos = True


# =============================================================================
# 10) Sidebar custom (opcional, seguro)
# =============================================================================

def _has_template(rel_path: str) -> bool:
    candidate = SOURCE_DIR / "_templates" / rel_path
    return candidate.exists() and candidate.is_file()


if os.environ.get("SPHINX_SIDEBAR_CUSTOM") == "1":
    required = [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
    if all(_has_template(p) for p in required):
        html_sidebars = {"**": required}
    else:
        missing = [p for p in required if not _has_template(p)]
        print(
            "[conf.py] WARNING: Sidebars custom deshabilitados; faltan templates:",
            ", ".join(missing),
        )


# =============================================================================
# 11) notfound.extension
# =============================================================================

notfound_urls_prefix = ""
notfound_template = "404.html"
notfound_no_urls_prefix = False


# =============================================================================
# 12) HTML general
# =============================================================================

html_show_sphinx = True
html_copy_source = False

# html_favicon = "_static/img/favicon.ico"
# html_logo = "_static/img/logo.svg"


# =============================================================================
# 13) Intersphinx (proxy/offline-safe)
# =============================================================================

if "sphinx.ext.intersphinx" in extensions:
    from conf.d.intersphinx import resolve_intersphinx_mapping

    intersphinx_mapping = resolve_intersphinx_mapping(
        os.environ,
        REPO_ROOT / "tools" / "_downloads",
    )


# =============================================================================
# 14) PlantUML (java portable, no rompe build)
# =============================================================================

if "sphinxcontrib.plantuml" in extensions:
    from conf.d.plantuml import resolve_plantuml_command

    plantuml_cmd = resolve_plantuml_command(REPO_ROOT)
    if plantuml_cmd:
        plantuml = plantuml_cmd
    else:
        print("[conf.py] WARNING: PlantUML deshabilitado; falta tools/plantuml.jar")


# =============================================================================
# 15) Spelling (solo builder spelling)
# =============================================================================

if "sphinxcontrib.spelling" in extensions:
    from conf.d import spelling as spelling_cfg

    spelling_word_list_filename = spelling_cfg.spelling_word_list_filename
    spelling_exclude_patterns = spelling_cfg.spelling_exclude_patterns
    spelling_lang = spelling_cfg.spelling_lang
    spelling_show_suggestions = spelling_cfg.spelling_show_suggestions


# =============================================================================
# 16) Outputs (numfig, LaTeX, man, texinfo)
# =============================================================================

from conf.d import outputs as out_cfg

numfig = out_cfg.numfig
numfig_format = out_cfg.numfig_format

latex_engine = out_cfg.latex_engine
latex_use_xindy = out_cfg.latex_use_xindy
latex_elements = out_cfg.latex_elements
latex_documents = out_cfg.latex_documents

man_pages = out_cfg.man_pages
texinfo_documents = out_cfg.texinfo_documents


# =============================================================================
# 17) i18n
# =============================================================================

locale_dirs = ["locale/"]
gettext_compact = False


# =============================================================================
# 18) Metadatos ADT (inertes salvo consumo explícito)
# =============================================================================

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

glossary_term_types = ["term", "technical-term", "acronym", "concept"]

ref_patterns = {
    "procedimiento": r"PROC_\d{3}",
    "estandar": r"STD_\d{3}",
    "regla": r"RT_\d{3}",
    "escenario": r"ESC_\d{3}",
}

translation_config = {
    "source_language": "en",
    "target_language": "es-MX",
    "preserve_technical_terms": True,
    "first_appearance_format": "español (:term:`inglés`)",
    "subsequent_format": "español",
}
