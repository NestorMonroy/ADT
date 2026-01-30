# ADR-2026-01-30: Simplificación del toctree raíz

## Estado

Aceptado.

## Contexto

Sphinx reportaba warnings de documentos referenciados en múltiples toctrees.
El `source/index.rst` incluía entradas de subsecciones que también estaban
presentes en los índices de cada sección, generando duplicados y ruido
en los builds con `-W`.

## Decisión

Reducir el toctree raíz para listar únicamente los índices de cada sección
y delegar el detalle de subsecciones a los `index.rst` internos.

## Alternativas consideradas

1. Mantener el toctree raíz completo y ajustar manualmente cada toctree
   secundario para evitar duplicados.
2. Deshabilitar el warning de Sphinx para referencias múltiples.

## Consecuencias

- Se elimina la duplicación de referencias desde la raíz.
- La navegación se mantiene jerárquica: primero sección, luego detalle.
- El toctree principal queda más corto y fácil de mantener.
- Requiere que los `index.rst` de cada sección estén completos.

## Referencias

- Work-log Lote 6: `.mywork/work-logs/2026-01-30-01-15-lote-6-toctree.md`.
- Detector de duplicados: `scripts/find_duplicate_toctree.py`.
