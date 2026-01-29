# Comando: sphinx-translate-section

Orquesta el proceso completo de traduccion de una seccion o documento siguiendo la metodologia ADT.

## Uso

```
sphinx-translate-section <url-o-archivo> <destino> [opciones]
```

## Parametros

### Requeridos

**url-o-archivo**
- URL web a traducir
- O path a archivo local (.md, .html, .txt)
- Ejemplo: https://arc42.org/section/02
- Ejemplo: docs/tutorial.md

**destino**
- Directorio destino en source/
- Path relativo desde raiz del proyecto
- Ejemplo: source/biblioteca/arc42/sections/02_constraints/traduccion/
- Ejemplo: source/diataxis/tutorials/

### Opcionales

**--mode <modo>**
- Modo de traduccion
- Valores: alta_fidelidad | marcado_visual | enriquecimiento
- Default: alta_fidelidad
- Ejemplo: --mode marcado_visual

**--framework <framework>**
- Framework de organizacion
- Valores: diataxis | arc42 | custom
- Default: custom
- Ejemplo: --framework arc42

**--category <categoria>**
- Categoria dentro del framework
- Para Diataxis: tutorials | how_to_guides | reference | explanation
- Para arc42: 01-12 (numero de seccion)
- Ejemplo: --category tutorials

**--validate**
- Ejecutar validacion completa despues de traduccion
- Flag boolean

**--dry-run**
- Mostrar lo que se haria sin ejecutar
- Flag boolean

## Proceso

### 1. Analisis de Fuente

DETERMINAR TIPO:
- Si es URL web -> usar translate_web_content.sh
- Si es archivo .md local -> usar adt_translator.py
- Si es arc42 -> usar arc42_scraper_python.py

VALIDACIONES:
- Fuente existe y es accesible
- Destino es directorio valido en source/
- Framework y categoria compatibles

### 2. Seleccion de Script

PARA CONTENIDO WEB:
```bash
bash scripts/traduccion/translate_web_content.sh <url> <destino>
```

PARA ARC42:
```bash
python scripts/traduccion/arc42_scraper_python.py \
 --section <numero> \
 --mode <modo> \
 --output <destino>
```

PARA ARCHIVO LOCAL:
```bash
python scripts/traduccion/adt_translator.py \
 --input <archivo> \
 --output <destino>/<nombre>.rst \
 --mode <modo> \
 --framework <framework>
```

### 3. Ejecucion de Traduccion

PASOS:
1. Ejecutar script seleccionado
2. Capturar output
3. Verificar archivos generados
4. Reportar resultado

### 4. Post-Procesamiento

GENERAR METADATA:
```rst
.. meta::
 :description: [Descripcion]
 :keywords: [palabras clave]
 :author: [Autor original]
 :source: <url-o-archivo>
 :translator: AI Assistant
 :date: YYYY-MM-DD

:Documento Original: <url-o-archivo>
:Modo de Traduccion: <modo>
:Framework: <framework>
:Categoria: <categoria>
:Fecha Traduccion: YYYY-MM-DD
```

CREAR README (si no existe):
```markdown
# Traduccion de [Nombre]

Fuente: <url-o-archivo>
Modo: <modo>
Framework: <framework>
Fecha: YYYY-MM-DD

## Archivos

- archivo1.rst - [Descripcion]
- archivo2.rst - [Descripcion]
```

### 5. Integracion

ACTUALIZAR TOCTREE:
- Detectar index.rst del capitulo padre
- Agregar referencia al nuevo contenido
- Validar sintaxis

EJEMPLO:
```rst
.. toctree::
 :maxdepth: 2

 existente1
 existente2
 nuevo_contenido # AGREGAR AQUI
```

### 6. Validacion (si --validate)

EJECUTAR:
```bash
# Build
make clean html

# Validar estructura
bash scripts/validar_estructura.sh

# Validar enlaces (opcional)
make linkcheck
```

VERIFICAR:
- Build exitoso (exit code 0)
- Sin errores
- Warnings aceptables
- Archivos en ubicacion correcta

### 7. Reporte

```
TRADUCCION COMPLETADA

Fuente: <url-o-archivo>
Destino: <destino>
Modo: <modo>
Framework: <framework>

ARCHIVOS GENERADOS:
- <destino>/archivo1.rst
- <destino>/archivo2.rst

METADATA: Generada
TOCTREE: Actualizado
BUILD: Exitoso

SIGUIENTE PASO:
1. Revisar archivos generados
2. Ajustar metadata si necesario
3. git add <archivos>
4. git commit -m "feat(traduccion): agregar [nombre]"
```

## Ejemplos

### Ejemplo 1: Traducir Seccion arc42

```bash
sphinx-translate-section \
 https://arc42.org/section/02 \
 source/biblioteca/arc42/sections/02_constraints/traduccion/ \
 --mode alta_fidelidad \
 --framework arc42 \
 --category 02 \
 --validate
```

Ejecuta:
1. Detecta que es arc42
2. Usa arc42_scraper_python.py --section 02
3. Genera archivos en destino
4. Crea metadata
5. Actualiza toctree
6. Valida build

### Ejemplo 2: Traducir Tutorial Web

```bash
sphinx-translate-section \
 https://example.com/tutorial.html \
 source/diataxis/tutorials/ \
 --mode marcado_visual \
 --framework diataxis \
 --category tutorials
```

Ejecuta:
1. Usa translate_web_content.sh
2. Aplica modo marcado_visual (admoniciones)
3. Genera en diataxis/tutorials/
4. Crea metadata
5. Actualiza toctree

### Ejemplo 3: Traducir Archivo Local

```bash
sphinx-translate-section \
 docs/howto.md \
 source/diataxis/how_to_guides/ \
 --mode alta_fidelidad \
 --framework diataxis \
 --category how_to_guides \
 --validate
```

Ejecuta:
1. Lee docs/howto.md
2. Usa adt_translator.py
3. Genera en how_to_guides/
4. Valida build completo

### Ejemplo 4: Dry Run

```bash
sphinx-translate-section \
 https://example.com/doc.html \
 source/biblioteca/ejemplo/ \
 --mode enriquecimiento \
 --dry-run
```

Output (no ejecuta):
```
DRY RUN - No se ejecutara traduccion

CONFIGURACION:
Fuente: https://example.com/doc.html
Destino: source/biblioteca/ejemplo/
Modo: enriquecimiento
Framework: custom

ACCIONES QUE SE EJECUTARIAN:
1. Descargar contenido de URL
2. Traducir con adt_translator.py
3. Generar metadata
4. Actualizar toctree en source/biblioteca/index.rst
5. Validar build (no especificado)

ARCHIVOS QUE SE CREARIAN:
- source/biblioteca/ejemplo/doc.rst
- source/biblioteca/ejemplo/README.md
```

## Integracion con Skills

### Con translation-workflow

Este comando ejecuta el workflow completo automáticamente:
- FASE 1: Analisis (automatico)
- FASE 2: Configuracion (parametros del comando)
- FASE 3: Ejecucion (script apropiado)
- FASE 4: Validacion (si --validate)
- FASE 5: Integracion (automatico)

### Con validation-suite

Si --validate especificado, usa validation-suite para:
- NIVEL 1: Build basico
- NIVEL 2: Validacion estructural
- NIVEL 3: Validacion de enlaces (opcional)

### Con work-logger

Sugerencia al finalizar:
```
SUGERENCIA: Documentar este trabajo

Usa work-logger skill para crear log:
.mywork/work-logs/YYYY-MM-DD-traducir-[nombre].md
```

## Casos Especiales

### Seccion arc42 con Multiples Archivos

arc42_scraper_python.py puede generar multiples archivos.

MANEJO:
- Dejar que script cree estructura
- Validar todos los archivos generados
- Actualizar toctree con glob si muchos archivos

```rst
.. toctree::
 :glob:

 02_constraints/*
```

### URL Requiere Autenticacion

ERROR: Si URL requiere autenticacion, el script fallara.

SOLUCION:
1. Descargar archivo manualmente
2. Usar como archivo local en vez de URL

### Contenido en Formato No Soportado

FORMATOS SOPORTADOS:
- HTML, Markdown, Plain Text

FORMATOS NO SOPORTADOS:
- PDF (requiere extraccion previa)
- DOCX (requiere conversion previa)

SOLUCION:
Convertir a formato soportado primero.

## Rollback

Si traduccion falla o resultado no es satisfactorio:

```bash
# Eliminar archivos generados
rm -rf <destino>/*

# Revertir cambios en toctree
git checkout source/*/index.rst

# O revertir commit completo
git revert <commit-hash>
```

## Validacion Post-Traduccion

```bash
# Verificar archivos generados
ls -la <destino>/

# Leer uno de los archivos
cat <destino>/archivo.rst

# Build completo
make clean html

# Ver HTML generado
open build/html/index.html
```

## Troubleshooting

**Error: "Script no encontrado"**
- Verificar que scripts existen en scripts/traduccion/
- Instalar dependencias: `pip install -r requirements.txt`

**Error: "Destino no existe"**
- Crear directorio: `mkdir -p <destino>`
- O verificar path correcto

**Error: "URL no accesible"**
- Verificar URL correcta
- Verificar conexion a internet
- Probar con curl: `curl -I <url>`

**Build falla despues de traduccion**
- Revisar sintaxis RST generada
- Verificar indentacion
- Consultar sphinx-expert skill

## Referencias

- scripts/traduccion/adt_translator.py
- scripts/traduccion/arc42_scraper_python.py
- scripts/traduccion/translate_web_content.sh
- translation-workflow skill
- validation-suite skill

## Notas

- Este comando automatiza translation-workflow completo
- Siempre revisar archivos generados manualmente
- Ajustar metadata segun necesidad
- Validar build antes de commit
- Documentar decisiones importantes en work-log
