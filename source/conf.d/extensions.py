# -*- coding: utf-8 -*-
"""
conf.d/extensions.py

Responsabilidad:
- Declarar y construir la lista de extensiones Sphinx.
- Aplicar políticas por perfil (SPHINX_PROFILE).
- Permitir overrides explícitos por flags (SPHINX_STRICT, SPHINX_ENABLE_*, etc.).
"""

from __future__ import annotations

import os


# ---------------------------------------------------------------------------
# Entrada de entorno
# ---------------------------------------------------------------------------

PROFILE = os.environ.get("SPHINX_PROFILE", "enterprise").lower()

# Overrides explícitos (tienen prioridad)
STRICT_OVERRIDE = os.environ.get("SPHINX_STRICT") == "1"

ENABLE_INTERSPHINX_OVERRIDE = os.environ.get("SPHINX_ENABLE_INTERSPHINX") == "1"
ENABLE_PLANTUML_OVERRIDE = os.environ.get("SPHINX_ENABLE_PLANTUML") == "1"
ENABLE_SPELLING_OVERRIDE = os.environ.get("SPHINX_ENABLE_SPELLING") == "1"

OFFLINE = os.environ.get("SPHINX_OFFLINE") == "1"


# ---------------------------------------------------------------------------
# Políticas por perfil (baseline)
# ---------------------------------------------------------------------------

PROFILE_POLICIES = {
    # Rápido, tolerante; sin tooling externo por defecto
    "dev": {
        "strict": False,
        "enable_intersphinx": False,
        "enable_plantuml": False,
        "enable_spelling": False,
    },
    # CI típico: reproducible; intersphinx solo si hay red
    "ci": {
        "strict": False,
        "enable_intersphinx": True,
        "enable_plantuml": False,
        "enable_spelling": False,
    },
    # QA: estricto; spelling activable; intersphinx si hay red
    "qa": {
        "strict": True,
        "enable_intersphinx": True,
        "enable_plantuml": False,
        "enable_spelling": True,
    },
    # Release: estricto; tooling habilitable (si el entorno lo soporta)
    "release": {
        "strict": True,
        "enable_intersphinx": True,
        "enable_plantuml": True,
        "enable_spelling": True,
    },
    # Enterprise por defecto: conservador y estable
    "enterprise": {
        "strict": False,
        "enable_intersphinx": False,
        "enable_plantuml": False,
        "enable_spelling": False,
    },
}

policy = PROFILE_POLICIES.get(PROFILE, PROFILE_POLICIES["enterprise"])


# ---------------------------------------------------------------------------
# Política efectiva (profile baseline + overrides)
# ---------------------------------------------------------------------------

STRICT = bool(STRICT_OVERRIDE or policy["strict"])

ENABLE_INTERSPHINX = bool(ENABLE_INTERSPHINX_OVERRIDE or policy["enable_intersphinx"])
ENABLE_PLANTUML = bool(ENABLE_PLANTUML_OVERRIDE or policy["enable_plantuml"])
ENABLE_SPELLING = bool(ENABLE_SPELLING_OVERRIDE or policy["enable_spelling"])

# OFFLINE gana: aunque profile quiera intersphinx, se apaga en offline
if OFFLINE:
    ENABLE_INTERSPHINX = False


# ---------------------------------------------------------------------------
# Extensiones por tier
# ---------------------------------------------------------------------------

CORE_EXTENSIONS = [
    "myst_parser",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

OPTIONAL_EXTENSIONS = [
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_toolbox.collapse",
    "sphinx_prompt",
    "notfound.extension",
]

EXTERNAL_TOOLING_EXTENSIONS = []

if ENABLE_INTERSPHINX:
    EXTERNAL_TOOLING_EXTENSIONS.append("sphinx.ext.intersphinx")

if ENABLE_PLANTUML:
    EXTERNAL_TOOLING_EXTENSIONS.append("sphinxcontrib.plantuml")

if ENABLE_SPELLING:
    EXTERNAL_TOOLING_EXTENSIONS.append("sphinxcontrib.spelling")


extensions = []
extensions.extend(CORE_EXTENSIONS)
extensions.extend(OPTIONAL_EXTENSIONS)
extensions.extend(EXTERNAL_TOOLING_EXTENSIONS)


# ---------------------------------------------------------------------------
# Strict mode
# ---------------------------------------------------------------------------

warningiserror = bool(STRICT)


# ---------------------------------------------------------------------------
# Exposición (auditoría)
# ---------------------------------------------------------------------------

EXTENSIONS_POLICY = {
    "profile": PROFILE,
    "strict": STRICT,
    "offline": OFFLINE,
    "effective": {
        "enable_intersphinx": ENABLE_INTERSPHINX,
        "enable_plantuml": ENABLE_PLANTUML,
        "enable_spelling": ENABLE_SPELLING,
    },
    "enabled": {
        "core": list(CORE_EXTENSIONS),
        "optional": list(OPTIONAL_EXTENSIONS),
        "external": list(EXTERNAL_TOOLING_EXTENSIONS),
    },
}