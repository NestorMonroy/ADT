# -*- coding: utf-8 -*-
"""
conf.d/outputs.py

Responsabilidad:
- Configurar salidas adicionales de Sphinx:
  - numeración de figuras/tablas
  - LaTeX / PDF
  - man pages
  - Texinfo
- Mantener estas configuraciones aisladas del build HTML básico.

Este módulo NO debe:
- habilitar builders automáticamente
- depender de extensiones externas
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Numeración de figuras, tablas y bloques
# ---------------------------------------------------------------------------

numfig = True

numfig_format = {
    "figure": "Figura %s",
    "table": "Tabla %s",
    "code-block": "Listado %s",
    "section": "Sección %s",
}


# ---------------------------------------------------------------------------
# Salida LaTeX / PDF
# ---------------------------------------------------------------------------

latex_engine = "pdflatex"
latex_use_xindy = False

latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": "",
    "figure_align": "htbp",
}

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


# ---------------------------------------------------------------------------
# Salida Man Pages
# ---------------------------------------------------------------------------

man_pages = [
    (
        "index",
        "adt-traduccion",
        "ADT - Procedimientos de Traducción Técnica",
        ["Equipo ADT"],
        1,
    )
]


# ---------------------------------------------------------------------------
# Salida Texinfo
# ---------------------------------------------------------------------------

texinfo_documents = [
    (
        "index",
        "ADT-Traduccion",
        "ADT - Procedimientos de Traducción Técnica",
        "Equipo ADT",
        "ADT-Traduccion",
        "Sistema de traducción técnica.",
        "Miscellaneous",
    )
]