# -*- coding: utf-8 -*-
"""
conf.d/spelling.py

Responsabilidad:
- Configurar sphinxcontrib-spelling de forma enterprise.
- Mantener la configuración aislada para no afectar builds HTML normales.
- Asumir que el builder de spelling se ejecuta de manera explícita.

Este módulo NO debe:
- forzar la ejecución del builder spelling
- romper el build HTML si faltan dependencias externas
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Archivo base de palabras permitidas
# ---------------------------------------------------------------------------

# Lista blanca de términos técnicos, acrónimos, nombres propios, etc.
# Ruta relativa a source/
spelling_word_list_filename = "spelling_wordlist.txt"


# ---------------------------------------------------------------------------
# Patrones a excluir del corrector
# ---------------------------------------------------------------------------

# Se recomienda excluir:
# - archivos generados
# - bloques que no deben corregirse (ej. dumps, código)
spelling_exclude_patterns = [
    "_build/**",
    "_static/**",
    "_templates/**",
]


# ---------------------------------------------------------------------------
# Idioma del corrector
# ---------------------------------------------------------------------------

# El idioma real depende del diccionario instalado en el sistema (enchant/aspell).
# Sphinx no valida la existencia del diccionario en tiempo de import.
spelling_lang = "es"


# ---------------------------------------------------------------------------
# Comportamiento del builder spelling
# ---------------------------------------------------------------------------

# Mostrar sugerencias cuando haya errores
spelling_show_suggestions = True


# ---------------------------------------------------------------------------
# Nota operativa (documentada a propósito)
# ---------------------------------------------------------------------------

# Este módulo solo tiene efecto cuando:
# - la extensión 'sphinxcontrib.spelling' está habilitada
# - se ejecuta explícitamente el builder:
#
#   sphinx-build -b spelling source _build/spelling
#
# En builds HTML normales, esta configuración es inerte.