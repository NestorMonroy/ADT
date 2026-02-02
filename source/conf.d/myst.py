# -*- coding: utf-8 -*-
"""
conf.d/myst.py

Responsabilidad:
- Configurar MyST-Parser como estándar de Markdown técnico.
- Declarar extensiones MyST permitidas.
- Controlar anclajes de encabezados y compatibilidad con RST.

Este módulo NO debe:
- declarar extensiones Sphinx (eso va en extensions.py)
- tocar tema, paths o tooling externo
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Extensiones MyST habilitadas
# ---------------------------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",       # ::: fences (admonitions, tabs, etc.)
    "deflist",           # listas de definición
    "dollarmath",        # matemáticas LaTeX ($$)
    "html_admonition",   # admonitions en HTML
    "html_image",        # imágenes con atributos HTML
    "replacements",      # (c) (r) -> símbolos tipográficos
    "smartquotes",       # comillas tipográficas
    "tasklist",          # listas de tareas
]


# ---------------------------------------------------------------------------
# Encabezados y anclajes
# ---------------------------------------------------------------------------

# Genera IDs automáticos para encabezados hasta nivel h3
# Útil para enlaces internos estables
myst_heading_anchors = 3


# ---------------------------------------------------------------------------
# Compatibilidad RST / MyST
# ---------------------------------------------------------------------------

# Permite usar referencias RST (:ref:, :term:, etc.) desde Markdown
myst_ref_domains = ["std", "py"]


# ---------------------------------------------------------------------------
# Configuración de comillas inteligentes
# ---------------------------------------------------------------------------

# Estas opciones afectan tanto a MyST como a RST
smartquotes = True
smartquotes_action = "De"  # Dash y ellipsis


# ---------------------------------------------------------------------------
# Supresión de warnings específicos de MyST
# ---------------------------------------------------------------------------

# Útil mientras se normaliza el corpus documental
suppress_warnings = [
    "myst.xref_missing",
]