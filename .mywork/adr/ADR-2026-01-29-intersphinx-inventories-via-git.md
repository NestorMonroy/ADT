# ADR-2026-01-29: Inventarios intersphinx via git clone

Fecha: 2026-01-29
Estado: Propuesto

## Contexto

El entorno actual bloquea las descargas directas de `objects.inv` desde
`docs.python.org` y `sphinx-doc.org` (403). Para mantener builds de Sphinx
con `intersphinx` activo, necesitamos una fuente local de inventarios que
no dependa de `curl`/`urllib`.

## Decisión

Usar `git clone` con `--depth 1`, `--filter=blob:none` y `--sparse` para
descargar los repositorios de CPython y Sphinx y leer los inventarios
desde rutas locales conocidas.

Comandos de referencia:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/python/cpython.git tools/_downloads/cpython
git -C tools/_downloads/cpython sparse-checkout set Doc

git clone --depth 1 --filter=blob:none --sparse https://github.com/sphinx-doc/sphinx.git tools/_downloads/sphinx
git -C tools/_downloads/sphinx sparse-checkout set doc
```

Inventarios esperados:

- `tools/_downloads/cpython/Doc/objects.inv`
- `tools/_downloads/sphinx/doc/objects.inv`

## Alternativas consideradas

1. Descargar `objects.inv` vía `curl`.
   - Rechazada por bloqueos de proxy (403).
2. Descargar tarballs/zip.
   - Funciona para obtener código, pero no asegura inventarios generados.
3. Deshabilitar `intersphinx`.
   - Evita warnings pero elimina referencias externas útiles.

## Consecuencias

- Se requiere espacio adicional para los repositorios clonados.
- La estrategia permite trabajar offline una vez descargados los repos.
- La actualización de inventarios se puede realizar con `git pull`.
