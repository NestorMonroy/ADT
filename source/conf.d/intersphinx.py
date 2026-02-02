# -*- coding: utf-8 -*-
"""
conf.d/intersphinx.py

Responsabilidad:
- Configurar intersphinx de forma enterprise.
- Soportar modo offline y entornos con proxy.
- Resolver inventarios locales si existen.
- No romper el build si intersphinx no está disponible.

Este módulo asume:
- La extensión 'sphinx.ext.intersphinx' se habilita en extensions.py
  solo cuando el entorno lo permite.
"""

from __future__ import annotations

import os
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers internos
# ---------------------------------------------------------------------------

def _normalize_inventory_path(value: str | None) -> str | None:
    """
    Normaliza valores de paths provenientes de variables de entorno.
    Acepta None, strings vacíos, 'none', 'null'.
    """
    if value is None:
        return None
    normalized = value.strip()
    if not normalized:
        return None
    if normalized.lower() in {"none", "null"}:
        return None
    return str(Path(normalized).expanduser())


def _resolve_inventory_path(
    env: dict[str, str],
    downloads_dir: Path | None,
    filenames: tuple[str, ...],
    env_key: str,
) -> str | None:
    """
    Resuelve la ruta del inventory en el siguiente orden:
    1) Variable de entorno explícita.
    2) Archivo existente en el directorio de descargas.
    3) None (Sphinx intentará descarga remota).
    """
    env_value = _normalize_inventory_path(env.get(env_key))
    if env_value:
        return env_value

    if downloads_dir is None:
        return None

    for filename in filenames:
        candidate = downloads_dir / filename
        if candidate.exists():
            return str(candidate)

    return None


# ---------------------------------------------------------------------------
# Configuración principal
# ---------------------------------------------------------------------------

def resolve_intersphinx_mapping(
    env: dict[str, str] | None = None,
    downloads_dir: Path | None = None,
) -> dict:
    """
    Construye el mapping de intersphinx considerando:
    - flags de entorno
    - modo offline
    - inventarios locales

    Variables de entorno soportadas:
    - SPHINX_SKIP_INTERSPHINX=1
    - SPHINX_OFFLINE=1
    - SPHINX_INTERSPHINX_PYTHON
    - SPHINX_INTERSPHINX_SPHINX
    - SPHINX_INTERSPHINX_PYTHON_INV
    - SPHINX_INTERSPHINX_SPHINX_INV
    """
    if env is None:
        env = os.environ

    if env.get("SPHINX_SKIP_INTERSPHINX") == "1":
        return {}

    if env.get("SPHINX_OFFLINE") == "1":
        return {}

    python_base = env.get(
        "SPHINX_INTERSPHINX_PYTHON",
        "https://docs.python.org/3/",
    )
    sphinx_base = env.get(
        "SPHINX_INTERSPHINX_SPHINX",
        "https://www.sphinx-doc.org/en/master/",
    )

    python_inv = _resolve_inventory_path(
        env,
        downloads_dir,
        ("python-objects.inv", "cpython/Doc/objects.inv"),
        "SPHINX_INTERSPHINX_PYTHON_INV",
    )

    sphinx_inv = _resolve_inventory_path(
        env,
        downloads_dir,
        ("sphinx-objects.inv", "sphinx/doc/objects.inv"),
        "SPHINX_INTERSPHINX_SPHINX_INV",
    )

    return {
        "python": (python_base, python_inv),
        "sphinx": (sphinx_base, sphinx_inv),
    }


# ---------------------------------------------------------------------------
# Activación (solo si conf.py decide usarlo)
# ---------------------------------------------------------------------------

# Este módulo NO asigna intersphinx_mapping automáticamente.
# conf.py debe hacer explícitamente:
#
# from conf.d.intersphinx import resolve_intersphinx_mapping
# intersphinx_mapping = resolve_intersphinx_mapping(
#     os.environ,
#     REPO_ROOT / "tools" / "_downloads",
# )