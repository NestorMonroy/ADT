# Work log: P-001 estrategia git clone para inventarios intersphinx

Fecha: 2026-01-29

## Objetivo

Reducir el bloqueo por proxy usando `git clone` con sparse checkout para
obtener inventarios `objects.inv` desde repos oficiales.

## Acciones realizadas

1. Cree el script `scripts/setup_intersphinx_via_git.sh` con:
   - `git clone --depth 1 --filter=blob:none --sparse`
   - `sparse-checkout` a `Doc` (cpython) y `doc` (sphinx).
2. Actualice la resolucion de `intersphinx_mapping` para detectar:
   - `tools/_downloads/cpython/Doc/objects.inv`
   - `tools/_downloads/sphinx/doc/objects.inv`
3. Agregue pruebas unitarias para validar la deteccion de esos paths.

## Resultado

- Script listo para ejecutarse en entornos donde `curl` es bloqueado por
  proxy.
- El mapping acepta inventarios locales provenientes de git clone.

## Evidencia

- Script: `scripts/setup_intersphinx_via_git.sh`.
- Cambios en `source/conf.py` y pruebas en `tests/test_intersphinx_utils.py`.

## Proximos pasos

- Ejecutar el script en el entorno objetivo y validar que existan los
  `objects.inv`.
- Reintentar `make html` y verificar ausencia de warnings de intersphinx.
