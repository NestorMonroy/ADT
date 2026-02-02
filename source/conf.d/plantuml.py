# -*- coding: utf-8 -*-
"""
conf.d/plantuml.py

Responsabilidad:
- Configurar PlantUML de forma portable y enterprise.
- No depender de JAVA_HOME ni del PATH global.
- Detectar Java portable del proyecto o usar fallback al sistema.
- No romper el build si PlantUML no está disponible.

Este módulo asume:
- La extensión 'sphinxcontrib.plantuml' se habilita condicionalmente
  en extensions.py mediante flags de entorno.
"""

from __future__ import annotations

from pathlib import Path


# ---------------------------------------------------------------------------
# Resolución de rutas base
# ---------------------------------------------------------------------------

def _q(p: Path) -> str:
    """
    Cita rutas con espacios (principalmente para Windows).
    """
    return f'"{str(p)}"'


def resolve_plantuml_command(repo_root: Path) -> str | None:
    """
    Resuelve el comando PlantUML a utilizar.

    Estrategia:
    1) Buscar PlantUML jar dentro del repositorio.
    2) Buscar Java portable dentro del repositorio.
    3) Fallback a 'java' del sistema si existe el jar.
    4) Si no hay jar, deshabilitar PlantUML limpiamente.

    Retorna:
    - string con el comando PlantUML
    - None si no se puede habilitar
    """
    tools_dir = repo_root / "tools"

    plantuml_jar = tools_dir / "plantuml.jar"
    java_win = tools_dir / "java" / "jdk-17" / "bin" / "java.exe"
    java_nix = tools_dir / "java" / "jdk-17" / "bin" / "java"

    if not plantuml_jar.exists():
        return None

    if java_win.exists():
        java_bin = _q(java_win)
    elif java_nix.exists():
        java_bin = _q(java_nix)
    else:
        java_bin = "java"

    return f"{java_bin} -jar {_q(plantuml_jar)}"


# ---------------------------------------------------------------------------
# Activación (solo si conf.py decide usarlo)
# ---------------------------------------------------------------------------

# Este módulo NO asigna la variable 'plantuml' automáticamente.
# conf.py debe hacer explícitamente:
#
# from conf.d.plantuml import resolve_plantuml_command
# plantuml_cmd = resolve_plantuml_command(REPO_ROOT)
# if plantuml_cmd:
#     plantuml = plantuml_cmd
#
# Si resolve_plantuml_command retorna None:
# - PlantUML queda deshabilitado
# - El build HTML no se rompe