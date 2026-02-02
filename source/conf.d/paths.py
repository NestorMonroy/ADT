# -*- coding: utf-8 -*-
"""
conf.d/paths.py

Responsabilidad:
- Definir rutas determinísticas (no depender del cwd).
- Exponer SOURCE_DIR, REPO_ROOT y helpers de path.
- Preparar sys.path para autodoc (si aplica).

Este módulo NO debe:
- declarar extensiones
- configurar tema
- tocar PlantUML / spelling / intersphinx
"""

from __future__ import annotations

import sys
from pathlib import Path


# source/conf.d/paths.py -> conf.d/
CONF_D_DIR = Path(__file__).resolve().parent

# source/
SOURCE_DIR = CONF_D_DIR.parent

# repo_root/
REPO_ROOT = SOURCE_DIR.parent


def q(p: Path) -> str:
    """
    Cita rutas con espacios (útil para Windows) y devuelve string.
    """
    return f'"{str(p)}"'


def ensure_sys_path(repo_root: Path = REPO_ROOT) -> None:
    """
    Inserta repo_root en sys.path para permitir imports del proyecto.
    Esto es requerido por sphinx.ext.autodoc cuando documentas código Python.

    Nota:
    - Se inserta en la posición 0 para priorizar el repo sobre site-packages.
    - Es idempotente: no duplica entradas.
    """
    root_str = str(repo_root)
    if sys.path and sys.path[0] == root_str:
        return
    if root_str in sys.path:
        sys.path.remove(root_str)
    sys.path.insert(0, root_str)


# Activa el path del repo por defecto (como en tu conf.py actual)
ensure_sys_path(REPO_ROOT)