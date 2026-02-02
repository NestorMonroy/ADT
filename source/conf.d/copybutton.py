# -*- coding: utf-8 -*-
"""
conf.d/copybutton.py

Responsabilidad:
- Configurar sphinx-copybutton.
- Definir qué partes del bloque se excluyen del copiado.
- Declarar regex de prompts soportados (shell, Python, notebooks).
- Garantizar copiado limpio y reproducible en documentación técnica.

Este módulo NO debe:
- declarar extensiones
- depender del tema
- modificar comportamiento global de Sphinx
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Exclusiones de copiado
# ---------------------------------------------------------------------------

# Evita copiar:
# - números de línea
# - prompts de Graphviz / Pygments
# - salidas decorativas
copybutton_exclude = ".linenos, .gp, .go"


# ---------------------------------------------------------------------------
# Definición de prompts (regex)
# ---------------------------------------------------------------------------

# Prompts comunes soportados:
# - Python REPL (>>> / ...)
# - Shell ($)
# - Jupyter (In [n]:)
# - Continuaciones indentadas
copybutton_prompt_text = (
    r">>> "                # Python REPL
    r"|\.\.\. "             # Python continuation
    r"|\$ "                 # Shell
    r"|In \[\d*\]: "        # Jupyter
    r"| {2,5}\.\.\.: "      # Continuación indentada corta
    r"| {5,8}: "            # Continuación indentada larga
)

copybutton_prompt_is_regexp = True


# ---------------------------------------------------------------------------
# Política de copiado
# ---------------------------------------------------------------------------

# Copiar solo líneas con prompt (no copiar salidas)
copybutton_only_copy_prompt_lines = True