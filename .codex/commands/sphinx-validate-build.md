# Comando: sphinx-validate-build

Ejecuta suite completa de validacion del proyecto Sphinx, desde build basico hasta quality report.

## Uso

```
sphinx-validate-build [opciones]
```

## Opciones

**--level <nivel>**
- Nivel de validacion a ejecutar
- Valores: basic | full | release
- Default: full
- Ejemplo: --level basic

**--fix**
- Intentar auto-fix de problemas menores
- Flag boolean
- Solo funciona con algunos tipos de errores

**--report <archivo>**
- Generar reporte escrito en archivo
- Ejemplo: --report validation_report.md

**--no-clean**
- No ejecutar make clean antes de build
- Util para builds incrementales rapidos

## Niveles de Validacion

### LEVEL: basic

RAPIDO - Solo lo esencial para commit

EJECUTA:
```bash
make clean # (a menos que --no-clean)
make html
bash scripts/validar_estructura.sh
```

VERIFICA:
- Build exitoso (exit code 0)
- Sin errores de Sphinx
- Nomenclatura correcta
- Archivos huerfanos

TIEMPO: ~30 segundos

CUANDO USAR:
- Antes de cada commit
- Durante desarrollo activo
- Validacion rapida

### LEVEL: full

COMPLETO - Validacion exhaustiva

EJECUTA:
```bash
make clean
make html
bash scripts/validar_estructura.sh
make linkcheck
python scripts/generate_section_metadata.py --validate source/
make coverage
```

VERIFICA:
- Todo de 'basic'
- Enlaces internos y externos
- Metadata completa
- Coverage de documentacion

TIEMPO: ~2-3 minutos

CUANDO USAR:
- Antes de merge a main
- Despues de traducciones completas
- Validacion periodica

### LEVEL: release

EXHAUSTIVO - Quality assurance completo

EJECUTA:
```bash
# Todo de 'full' +
python scripts/quality_report.py --output quality_report.md
```

GENERA:
- Reporte de calidad completo
- Metricas de proyecto
- Analisis de cobertura
- Lista de TODOs

VERIFICA:
- Todo de 'full'
- Calidad general del proyecto
- Metricas vs thresholds
- Preparacion para release

TIEMPO: ~5-10 minutos

CUANDO USAR:
- Antes de release/tag
- Auditorias de calidad
- Evaluacion de estado del proyecto

## Proceso

### 1. Preparacion

LIMPIAR (si no --no-clean):
```bash
make clean
```

VERIFICAR PREREQUISITOS:
- Scripts existen
- Dependencias instaladas
- En raiz del proyecto

### 2. Ejecucion de Validaciones

POR CADA VALIDACION:
1. Anunciar inicio
2. Ejecutar comando
3. Capturar output
4. Verificar exit code
5. Parsear resultados
6. Reportar

EJEMPLO OUTPUT:
```
VALIDACION 1/6: Build HTML
Estado: EJECUTANDO...
Comando: make html
Resultado: [OK] EXITOSO (23.4s)

VALIDACION 2/6: Estructura
Estado: EJECUTANDO...
Comando: bash scripts/validar_estructura.sh
Resultado: [OK] EXITOSO (1.2s)
Advertencias: 2 archivos huerfanos encontrados

...
```

### 3. Auto-Fix (si --fix)

PROBLEMAS QUE SE AUTO-FIXEAN:
- Trailing whitespace en RST
- Missing blank lines
- Encoding issues (UTF-8)

PROCESO:
```bash
# Fix trailing whitespace
find source/ -name "*.rst" -exec sed -i 's/[[:space:]]*$//' {} \;

# Fix missing blank lines before sections
# (logica especifica)

# Re-ejecutar validacion
```

LIMITACIONES:
- NO fixea errores de sintaxis
- NO fixea referencias rotas
- NO fixea problemas estructurales

### 4. Generacion de Reporte (si --report)

FORMATO MARKDOWN:
```markdown
# Validation Report

Fecha: YYYY-MM-DD HH:MM
Nivel: <nivel>
Proyecto: ADT Documentation

## Resumen

- Build: [OK] EXITOSO
- Estructura: [OK] EXITOSO (2 warnings)
- Enlaces: [OK] EXITOSO
- Metadata: [OK] EXITOSO
- Coverage: [OK] EXITOSO (95.2%)

## Detalles

### Build HTML
Tiempo: 23.4s
Exit Code: 0
Warnings: 3

```
WARNING: toctree contains reference to nonexisting document
```

### Validacion de Enlaces
Total enlaces: 245
Rotos: 0
Redirects: 2

...

## Acciones Recomendadas

1. Revisar 2 archivos huerfanos
2. Actualizar metadata en 3 archivos
3. Resolver redirects en enlaces

## Metricas

Build time: 23.4s
Total archivos .rst: 157
Total palabras: 45,230
Coverage: 95.2%
```

### 5. Resultado Final

EXITOSO:
```
===========================================
VALIDACION COMPLETA: [OK] EXITOSO
===========================================

Nivel: <nivel>
Tiempo total: <tiempo>

RESULTADOS:
[OK] Build HTML: EXITOSO
[OK] Estructura: EXITOSO (2 warnings)
[OK] Enlaces: EXITOSO
[OK] Metadata: EXITOSO
[OK] Coverage: EXITOSO

WARNINGS:
- 2 archivos huerfanos encontrados
- 3 warnings de Sphinx (ver log)

SIGUIENTE PASO:
Revisar warnings si necesario, o proceder con commit.
```

FALLIDO:
```
===========================================
VALIDACION COMPLETA: [FAIL] FALLIDA
===========================================

Nivel: <nivel>
Tiempo total: <tiempo>

RESULTADOS:
[FAIL] Build HTML: FALLIDO
 Error: Unknown directive type "note" at workflow.rst:45

[OK] Estructura: EXITOSO

ABORTADO: Resto de validaciones no ejecutadas

SIGUIENTE PASO:
1. Revisar error en workflow.rst:45
2. Corregir problema
3. Re-ejecutar validacion
```

## Ejemplos

### Ejemplo 1: Validacion Basica Pre-Commit

```bash
sphinx-validate-build --level basic
```

Output:
```
VALIDACION BASICA

[1/2] Build HTML... [OK] (15.2s)
[2/2] Estructura... [OK] (0.8s)

EXITOSO - Listo para commit
```

### Ejemplo 2: Validacion Completa

```bash
sphinx-validate-build --level full
```

Output:
```
VALIDACION COMPLETA

[1/5] Build HTML... [OK] (23.4s)
[2/5] Estructura... [OK] (1.2s)
[3/5] Enlaces... [OK] (45.3s)
[4/5] Metadata... [OK] (2.1s)
[5/5] Coverage... [OK] (3.2s)

EXITOSO - Coverage: 95.2%
```

### Ejemplo 3: Con Auto-Fix

```bash
sphinx-validate-build --level basic --fix
```

Output:
```
VALIDACION BASICA CON AUTO-FIX

[1/2] Build HTML... [FAIL] FALLIDO
 3 archivos con trailing whitespace

AUTO-FIX: Ejecutando...
 Fijando trailing whitespace... [OK]
 Re-ejecutando build... [OK]

[1/2] Build HTML... [OK] (16.1s)
[2/2] Estructura... [OK] (0.9s)

EXITOSO - Problemas auto-fijados
```

### Ejemplo 4: Con Reporte

```bash
sphinx-validate-build --level release --report quality_report.md
```

Output:
```
VALIDACION RELEASE

[1/6] Build HTML... [OK]
[2/6] Estructura... [OK]
[3/6] Enlaces... [OK]
[4/6] Metadata... [OK]
[5/6] Coverage... [OK]
[6/6] Quality Report... [OK]

Reporte generado: quality_report.md

EXITOSO - Proyecto listo para release
```

### Ejemplo 5: Build Incremental Rapido

```bash
sphinx-validate-build --level basic --no-clean
```

Output:
```
VALIDACION BASICA (INCREMENTAL)

[1/2] Build HTML (incremental)... [OK] (3.2s)
[2/2] Estructura... [OK] (0.7s)

EXITOSO - Build incremental rapido
```

## Interpretacion de Resultados

### Exit Codes

- 0: Validacion exitosa
- 1: Validacion fallida
- 2: Error en ejecucion del comando

### Tipos de Problemas

**ERRORS** (bloquean):
- Build failures
- Syntax errors
- Broken internal references

**WARNINGS** (no bloquean):
- Archivos huerfanos
- Redirects en enlaces
- Metadata faltante
- Coverage < threshold

**INFO** (informativos):
- Build time
- Total archivos
- Estadisticas generales

## Integracion con CI/CD

```yaml
# .github/workflows/validation.yml
name: Validation

on: [push, pull_request]

jobs:
 validate:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v2
 - name: Setup Python
 uses: actions/setup-python@v2
 - name: Install dependencies
 run: pip install -r requirements.txt
 - name: Validate
 run: sphinx-validate-build --level full
```

## Troubleshooting

**Error: "make: command not found"**
- Instalar make
- O ejecutar manualmente: `sphinx-build -b html source/ build/html/`

**Error: "script not found"**
- Verificar estar en raiz del proyecto
- Verificar que scripts/ existe

**Validacion muy lenta**
- Usar --level basic para rapido
- Usar --no-clean para incremental
- Considerar parallel build en Makefile

**Auto-fix no funciona**
- Solo fixea problemas menores automatizables
- Errores complejos requieren intervencion manual

## Referencias

- validation-suite skill
- scripts/validar_estructura.sh
- Makefile (html, linkcheck, coverage, clean)

## Notas

- Ejecutar --level basic antes de cada commit
- Ejecutar --level full antes de merge
- Ejecutar --level release antes de tag/release
- Warnings no bloquean pero deben revisarse
- Auto-fix es conservador, solo fija problemas seguros
- Reporte de calidad util para tracking de metricas
