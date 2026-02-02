# -*- coding: utf-8 -*-
"""
conf.d/theme_furo.py

Responsabilidad:
- Configurar el tema HTML (Furo).
- Definir tokens de color (light / dark) alineados a identidad ADT.
- Declarar títulos, assets estáticos y archivos CSS/JS.
- No declarar extensiones.
- No tocar sidebars (eso va en un módulo separado si se decide).

Principios:
- Contraste adecuado (WCAG) en light y dark.
- Tokens coherentes y reutilizables.
- HTML debe funcionar aunque falten assets custom.
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Tema base
# ---------------------------------------------------------------------------

html_theme = "furo"


# ---------------------------------------------------------------------------
# Opciones del tema (design tokens)
# ---------------------------------------------------------------------------

html_theme_options = {
    "light_css_variables": {
        "color-background-primary": "#F2F6F8",
        "color-foreground-primary": "#2A2F33",

        "color-brand-primary": "#104E5E",
        "color-brand-content": "#104E5E",

        "color-background-border": "rgba(42, 47, 51, 0.15)",
        "color-background-secondary": "#E8EFF3",

        "color-code-background": "rgba(11, 60, 73, 0.06)",
        "color-code-foreground": "#2A2F33",
    },
    "dark_css_variables": {
        "color-background-primary": "#0B3C49",
        "color-foreground-primary": "#F2F6F8",

        "color-brand-primary": "#6FAEC7",
        "color-brand-content": "#6FAEC7",

        "color-background-border": "rgba(111, 174, 199, 0.35)",
        "color-background-secondary": "rgba(255, 255, 255, 0.04)",

        "color-code-background": "rgba(242, 246, 248, 0.08)",
        "color-code-foreground": "#F2F6F8",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}


# ---------------------------------------------------------------------------
# Títulos del sitio
# ---------------------------------------------------------------------------

# Estas variables deben existir en conf.py principal:
# - project
# - version
#
# Se asumen ya definidas antes de importar este módulo.

html_title = f"{project} v{version}"
html_short_title = "ADT Traducción"


# ---------------------------------------------------------------------------
# Assets estáticos
# ---------------------------------------------------------------------------

html_static_path = ["_static"]

# Archivos custom (si no existen, Sphinx no falla)
html_css_files = [
    "css/custom.css",
]

html_js_files = [
    "js/custom.js",
]


# ---------------------------------------------------------------------------
# Branding opcional (activar solo cuando existan los archivos)
# ---------------------------------------------------------------------------

# html_logo = "_static/img/logo.svg"
# html_favicon = "_static/img/favicon.ico"