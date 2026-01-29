# 2026-01-29-17-31 - Auditoria de paquetes y rutas

Fecha: 2026-01-29 17:31
Timestamp: 2026-01-29 17:31
Autor: AI Assistant
Proyecto: ADT Documentation
Version: 1.7.1

## Resumen Ejecutivo

Se amplio la auditoria con inventario de paquetes instalados (APT y pip),
variables de PATH y rutas relevantes del proyecto. El entorno cuenta con
Python 3.12.12 en pyenv y un conjunto amplio de paquetes Python para
Sphinx/QA. APT muestra utilidades base, compiladores y herramientas de
build. Se listaron rutas clave (`/workspace/ADT`, `.mywork`, `_build`,
`source`) con permisos. Se registro el PATH completo para ubicar
herramientas disponibles.

## Contexto

### Situacion Inicial
Faltaba documentar paquetes instalados y rutas del entorno.

### Objetivo
Registrar inventario basico de paquetes y rutas relevantes.

## Trabajo Realizado

### Paso 1: PATH del sistema

```bash
echo "$PATH"
```

Resultado: PATH incluye pyenv, mise, toolchains y utilidades del sistema.

### Paso 2: Paquetes APT (muestra)

```bash
dpkg -l | head -n 50
```

Resultado: se listaron paquetes base (apt, bash, build-essential, clang,
cmake, curl, etc.) y diccionarios aspell.

### Paso 3: Paquetes Python (pip, muestra)

```bash
python3 -m pip list --format=columns | head -n 40
```

Resultado: paquetes de Sphinx/QA/formatting (alabaster, furo, flake8,
black, docutils, etc.).

### Paso 4: Version de Python y site-packages

```bash
python3 - <<'PY'
import sys, site
print('python:', sys.version)
print('executable:', sys.executable)
print('site-packages:', site.getsitepackages())
PY
```

Resultado: Python 3.12.12 en `/root/.pyenv/versions/3.12.12`.

### Paso 5: Rutas del proyecto

```bash
ls -ld /workspace /workspace/ADT /workspace/ADT/.mywork /workspace/ADT/_build /workspace/ADT/source
```

Resultado: rutas accesibles con permisos `drwxr-xr-x`.

## Paquetes Instalados (resumen)

### APT (extracto)
- Herramientas base: `apt`, `bash`, `coreutils`, `curl`.
- Build: `build-essential`, `cmake`, `clang-20`, `clang-tools-20`.
- Diccionarios: `aspell`, `aspell-en`, `dictionaries-common`.

### Pip (extracto)
- Sphinx/Docs: `alabaster`, `docutils`, `furo`, `sphinx` (presente en entorno).
- QA/formatting: `black`, `flake8`, `isort`, `coverage`.

## Rutas y PATH

### PATH (resumen)
Incluye:
- `/root/.pyenv/shims` y `/root/.pyenv/bin`
- `/root/.local/share/mise/installs/*`
- `/usr/local/bin`, `/usr/bin`, `/bin`

### Rutas del proyecto
- `/workspace/ADT` (repo)
- `/workspace/ADT/.mywork` (work-logs)
- `/workspace/ADT/_build` (salidas Sphinx)
- `/workspace/ADT/source` (fuentes)

## Evidencia

```
python: 3.12.12 (main, Jan 12 2026, 17:43:59) [GCC 13.3.0]
executable: /root/.pyenv/versions/3.12.12/bin/python3
site-packages: ['/root/.pyenv/versions/3.12.12/lib/python3.12/site-packages']
```

## Resultados

### Validacion
- [x] Inventario basico de APT registrado.
- [x] Inventario basico de pip registrado.
- [x] PATH y rutas del proyecto documentadas.

## Proximos Pasos

1. Exportar inventarios completos si se requiere auditoria exhaustiva.
2. Revisar compatibilidad de toolchains si se agregan nuevas dependencias.

---

**Tags:** #auditoria #paquetes #rutas #entorno
**Estado:** Completado
