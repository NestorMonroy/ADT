# -*- coding: utf-8 -*-
"""
Sphinx configuration file (Enterprise Orchestrator)

Importante:
- La carpeta se llama literalmente: source/conf.d/
- Python NO puede importarla con "from conf.d import ..." porque interpreta
  "conf" como paquete y "d" como subpaquete.
- Por eso este conf.py carga módulos por RUTA usando importlib.

Contrato:
- scripts se ejecutan desde /ADT (repo root)
- Sphinx invoca este conf.py desde source/
"""

from __future__ import annotations

import os
import sys
import warnings
import importlib.util
from pathlib import Path

from pygments.lexers.special import TextLexer


# =============================================================================
# 0) Rutas base (sin depender de imports)
# =============================================================================

SOURCE_DIR = Path(__file__).resolve().parent          # .../ADT/source
REPO_ROOT = SOURCE_DIR.parent                         # .../ADT
CONF_D_DIR = SOURCE_DIR / "conf.d"                    # .../ADT/source/conf.d


def _load_conf_module(module_name: str, file_path: Path):
    """
    Carga un módulo Python desde ruta absoluta y lo retorna.
    No requiere que el directorio sea un paquete importable.
    """
    if not file_path.exists():
        raise RuntimeError(f"Missing conf.d module file: {file_path}")

    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not create import spec for: {file_path}")

    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


# =============================================================================
# 1) sys.path (autodoc) y path determinístico
# =============================================================================

# Para autodoc: el repo root en sys.path permite importar módulos del proyecto.
repo_root_str = str(REPO_ROOT)
if sys.path and sys.path[0] != repo_root_str:
    if repo_root_str in sys.path:
        sys.path.remove(repo_root_str)
    sys.path.insert(0, repo_root_str)


# =============================================================================
# 2) Cargar módulos conf.d por ruta
# =============================================================================

ext_cfg = _load_conf_module("conf_d_extensions", CONF_D_DIR / "extensions.py")
theme_cfg = _load_conf_module("conf_d_theme_furo", CONF_D_DIR / "theme_furo.py")
myst_cfg = _load_conf_module("conf_d_myst", CONF_D_DIR / "myst.py")
copy_cfg = _load_conf_module("conf_d_copybutton", CONF_D_DIR / "copybutton.py")
out_cfg = _load_conf_module("conf_d_outputs", CONF_D_DIR / "outputs.py")

# Opcionales (solo si se habilitan por flags y se usan)
# Se cargan más adelante bajo condición.


# =============================================================================
# 3) Políticas enterprise (extensions + warningiserror)
# =============================================================================

extensions = ext_cfg.extensions
warningiserror = ext_cfg.warningiserror

warnings.filterwarnings(
    "ignore",
    message="The str interface for _JavaScript objects is deprecated.",
    category=DeprecationWarning,
)


# =============================================================================
# 4) Metadatos del proyecto
# =============================================================================

project = "ADT - Procedimientos de Traducción Técnica"
copyright = "2026, Equipo ADT"
author = "Equipo ADT"

version = "1.0"
release = "1.0.0"

html_title = f"{project} v{version}"
html_short_title = "ADT Traducción"


# =============================================================================
# 5) Configuración general
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
# 6) Resaltado (Pygments) y lexers de blindaje
# =============================================================================

pygments_style = "sphinx"
pygments_lexers = {
    "plantuml": TextLexer,
    "atl": TextLexer,
    "ocl": TextLexer,
}


# =============================================================================
# 7) Tema (Furo) + assets estáticos
# =============================================================================

html_theme = theme_cfg.html_theme
html_theme_options = theme_cfg.html_theme_options
html_static_path = theme_cfg.html_static_path
html_css_files = theme_cfg.html_css_files
html_js_files = theme_cfg.html_js_files


# =============================================================================
# 8) MyST + smartquotes + suppress_warnings
# =============================================================================

myst_enable_extensions = myst_cfg.myst_enable_extensions
myst_heading_anchors = myst_cfg.myst_heading_anchors
myst_ref_domains = getattr(myst_cfg, "myst_ref_domains", ["std", "py"])

smartquotes = myst_cfg.smartquotes
smartquotes_action = myst_cfg.smartquotes_action

suppress_warnings = list(getattr(myst_cfg, "suppress_warnings", []))

# Supresión adicional solo fuera de strict
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
# 9) Copybutton
# =============================================================================

copybutton_exclude = copy_cfg.copybutton_exclude
copybutton_prompt_text = copy_cfg.copybutton_prompt_text
copybutton_prompt_is_regexp = copy_cfg.copybutton_prompt_is_regexp
copybutton_only_copy_prompt_lines = copy_cfg.copybutton_only_copy_prompt_lines


# =============================================================================
# 10) Autodoc / Napoleon / Todo
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
# 11) Sidebar custom (opcional, seguro)
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
# 12) notfound.extension
# =============================================================================

notfound_urls_prefix = ""
notfound_template = "404.html"
notfound_no_urls_prefix = False


# =============================================================================
# 13) HTML general
# =============================================================================

html_show_sphinx = True
html_copy_source = False


# =============================================================================
# 14) Intersphinx (solo si la extensión está activa)
# =============================================================================

if "sphinx.ext.intersphinx" in extensions:
    intersphinx_cfg = _load_conf_module("conf_d_intersphinx", CONF_D_DIR / "intersphinx.py")
    intersphinx_mapping = intersphinx_cfg.resolve_intersphinx_mapping(
        os.environ,
        REPO_ROOT / "tools" / "_downloads",
    )


# =============================================================================
# 15) PlantUML (solo si la extensión está activa)
# =============================================================================

if "sphinxcontrib.plantuml" in extensions:
    plantuml_cfg = _load_conf_module("conf_d_plantuml", CONF_D_DIR / "plantuml.py")
    plantuml_cmd = plantuml_cfg.resolve_plantuml_command(REPO_ROOT)
    if plantuml_cmd:
        plantuml = plantuml_cmd
    else:
        print("[conf.py] WARNING: PlantUML deshabilitado; falta tools/plantuml.jar")


# =============================================================================
# 16) Spelling (solo si la extensión está activa)
# =============================================================================

if "sphinxcontrib.spelling" in extensions:
    spelling_cfg = _load_conf_module("conf_d_spelling", CONF_D_DIR / "spelling.py")
    spelling_word_list_filename = spelling_cfg.spelling_word_list_filename
    spelling_exclude_patterns = spelling_cfg.spelling_exclude_patterns
    spelling_lang = spelling_cfg.spelling_lang
    spelling_show_suggestions = spelling_cfg.spelling_show_suggestions


# =============================================================================
# 17) Outputs (numfig, LaTeX, man, texinfo)
# =============================================================================

numfig = out_cfg.numfig
numfig_format = out_cfg.numfig_format

latex_engine = out_cfg.latex_engine
latex_use_xindy = out_cfg.latex_use_xindy
latex_elements = out_cfg.latex_elements
latex_documents = out_cfg.latex_documents

man_pages = out_cfg.man_pages
texinfo_documents = out_cfg.texinfo_documents


# =============================================================================
# 18) i18n
# =============================================================================

locale_dirs = ["locale/"]
gettext_compact = False


# =============================================================================
# 19) Metadatos ADT (inertes salvo consumo explícito)
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