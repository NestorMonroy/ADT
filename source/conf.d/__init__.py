# -*- coding: utf-8 -*-
"""
conf.d

Paquete de configuración modular de Sphinx (enterprise).

Este paquete contiene módulos con responsabilidades aisladas:
- paths: resolución de rutas y sys.path
- extensions: extensiones y políticas por perfil
- theme_furo: tema y tokens de diseño
- myst: configuración Markdown (MyST)
- copybutton: reglas de copiado de bloques
- intersphinx: enlaces cruzados (offline/proxy-safe)
- plantuml: integración PlantUML portable
- spelling: corrector ortográfico
- outputs: salidas adicionales (LaTeX, man, texinfo)

Reglas:
- NO ejecutar lógica en import.
- NO definir efectos secundarios.
- NO modificar variables globales de Sphinx aquí.
- Este archivo existe para declarar el paquete y documentar su propósito.
"""
