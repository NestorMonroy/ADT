# 2026-01-30-00-35 - Lote 5: warnings de highlighting

Fecha: 2026-01-30 00:35
Autor: AI Assistant
Proyecto: ADT Documentation

## Resumen Ejecutivo

Se añadió un script para reemplazar lexers desconocidos (plantuml/atl/ocl)
en bloques `.. code-block::` por `text`, eliminando warnings de highlighting.
Se aplicó a los archivos listados en el Lote 5.

## Archivos Actualizados

- `scripts/fix_unknown_lexers.py`
- `tests/test_fix_unknown_lexers.py`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_5.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_6.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_7.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_8.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_9.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/traduccion/crosscutting_tip_7.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_3.rst`

## Cambios Relevantes

1. Helper y CLI `fix_unknown_lexers` con lista de lexers desconocidos.
2. Normalización de bloques `.. code-block:: plantuml` a `text`.
3. Test unitario para la transformación de lexers desconocidos.

## Validación

- `pytest -q tests/test_fix_unknown_lexers.py`

**Estado:** Completado
