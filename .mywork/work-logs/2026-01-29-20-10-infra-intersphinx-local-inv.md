# Work log: P-001 soporte para inventarios intersphinx locales

Fecha: 2026-01-29

## Objetivo

Mitigar el bloqueo por proxy de los inventarios intersphinx habilitando
el uso de inventarios locales (objects.inv) y registrando el intento de
descarga directa.

## Acciones realizadas

1. Cree `tools/_downloads` para almacenar artefactos locales.
2. Intente descargar los inventarios oficiales:
   - `curl -L -o tools/_downloads/python-objects.inv https://docs.python.org/3/objects.inv`
   - `curl -L -o tools/_downloads/sphinx-objects.inv https://www.sphinx-doc.org/en/master/objects.inv`
3. Actualice `source/conf.py` para resolver el mapping de intersphinx
   con soporte de inventarios locales por variables de entorno y por
   deteccion automatica en `tools/_downloads`.
4. Agregue pruebas unitarias para validar la resolucion del mapping.

## Resultado

- Ambos `curl` fallaron con `CONNECT tunnel failed, response 403`.
- El config ahora admite inventarios locales con:
  - `SPHINX_INTERSPHINX_PYTHON_INV`
  - `SPHINX_INTERSPHINX_SPHINX_INV`
  - Deteccion automatica de `tools/_downloads/python-objects.inv` y
    `tools/_downloads/sphinx-objects.inv` si existen.

## Evidencia

- Logs de error 403 en los comandos `curl`.
- Cambios en `source/conf.py` y pruebas en `tests/test_intersphinx_utils.py`.

## Proximos pasos

- Solicitar mirror/proxy con acceso permitido para descargar los
  inventarios oficiales.
- Una vez disponible, colocar los `.inv` en `tools/_downloads` y
  verificar el build de Sphinx sin warnings de intersphinx.
