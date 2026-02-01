---
name: validation-suite
description: "Suite completa de validacion para Sphinx y contenido RST. Usar para verificar builds, validar estructura, detectar errores, y asegurar calidad antes de commits."
version: 1.0.0
created: 2026-01-29
updated: 2026-01-30
---

# Validation Suite - Quality Assurance

## Cuando usar

- Antes de hacer commit
- Despues de traducir contenido
- Al modificar estructura
- Cuando build falla
- Antes de merge a main
- Auditorias periodicas

## Niveles de Validacion

### NIVEL 1: Build Basico (OBLIGATORIO)

```bash
make clean
make html

# Resultado esperado:
# build succeeded.
# Exit code 0
# Sin lineas "ERROR"
```

Si falla: Consultar sphinx-expert skill

### NIVEL 2: Validacion Estructural

```bash
bash scripts/validar_estructura.sh
```

Verifica:
- Nomenclatura archivos (XX_nombre/)
- Existencia index.rst
- Archivos huerfanos
- Directorios vacios

### NIVEL 3: Validacion de Enlaces

```bash
make linkcheck
```

Verifica:
- Cross-references internos (:doc:, :ref:)
- Enlaces externos
- Downloads
- Imagenes

Ver: `build/linkcheck/output.txt`

### NIVEL 4: Calidad de Traduccion

Checklist manual:

Coherencia terminologica:
- [ ] Terminos consistentes
- [ ] Nombres propios conservados
- [ ] Codigo sin traducir

Completitud:
- [ ] Todas secciones presentes
- [ ] Metadata completa
- [ ] Referencias actualizadas

Modo aplicado:
- [ ] Admoniciones apropiadas
- [ ] Nivel de detalle correcto

### NIVEL 5: Validacion de Metadata

```bash
python scripts/generate_section_metadata.py --validate source/
```

Campos requeridos:
- description, keywords, author, date
- Documento Original (si traduccion)
- Modo de Traduccion (si traduccion)

### NIVEL 6: Coverage

```bash
make coverage
```

Verifica:
- Secciones sin contenido
- TODOs pendientes

## Proceso Pre-Commit

```bash
# 1. Build
make clean html

# 2. Estructura
bash scripts/validar_estructura.sh

# 3. Si TODO OK:
git add <archivos>
git commit -m "..."
```

## Metricas de Calidad

Thresholds:
- Build success: 100%
- Broken links: 0
- Metadata coverage: > 95%
- Orphan files: 0

## Troubleshooting

Build falla con "Unknown directive":
- Verificar sintaxis
- Verificar indentacion

Enlaces rotos:
- Buscar definicion del label
- Verificar typos

## Referencias

- scripts/validar_estructura.sh
- Makefile (html, linkcheck, coverage)
- source/07_guias_uso/troubleshooting.rst

## Notas

- Validacion no sustituye revision manual
- Warnings pueden indicar problemas reales
- Linkcheck puede tener falsos positivos
