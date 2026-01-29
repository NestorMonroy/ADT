# Scripts Disponibles en ADT

Ubicacion base: scripts/

## Scripts de Traduccion

### adt_translator.py

UBICACION: `scripts/traduccion/adt_translator.py`

PROPOSITO: Script principal de traduccion siguiendo metodologia ADT

USO:
```bash
python scripts/traduccion/adt_translator.py \
  --input <archivo_fuente> \
  --output <archivo_destino> \
  --mode <alta_fidelidad|marcado_visual|enriquecimiento> \
  --framework <diataxis|arc42|custom>
```

PARAMETROS:
- input: Archivo fuente (MD, HTML, TXT)
- output: Archivo RST destino
- mode: Modo de traduccion (defecto: alta_fidelidad)
- framework: Framework de organizacion (defecto: custom)

EJEMPLO:
```bash
python scripts/traduccion/adt_translator.py \
  --input docs/tutorial.md \
  --output source/diataxis/tutorials/mi_tutorial.rst \
  --mode marcado_visual \
  --framework diataxis
```

### arc42_scraper_python.py

UBICACION: `scripts/traduccion/arc42_scraper_python.py`

PROPOSITO: Extraccion y traduccion especializada de secciones arc42

USO:
```bash
python scripts/traduccion/arc42_scraper_python.py \
  --section <numero_seccion> \
  --mode <modo> \
  --output <directorio_destino>
```

PARAMETROS:
- section: Numero de seccion arc42 (01-12)
- mode: Modo de traduccion (recomendar alta_fidelidad)
- output: Directorio de salida

EJEMPLO:
```bash
python scripts/traduccion/arc42_scraper_python.py \
  --section 02 \
  --mode alta_fidelidad \
  --output source/biblioteca/arc42/sections/02_constraints/traduccion/
```

### translate_web_content.sh

UBICACION: `scripts/traduccion/translate_web_content.sh`

PROPOSITO: Traduccion de contenido desde URLs web

USO:
```bash
bash scripts/traduccion/translate_web_content.sh <url> <output_dir>
```

PARAMETROS:
- url: URL del contenido a traducir
- output_dir: Directorio de salida

EJEMPLO:
```bash
bash scripts/traduccion/translate_web_content.sh \
  https://example.com/doc.html \
  source/biblioteca/ejemplo/
```

## Scripts de Analisis

### analizar_seccion.py

UBICACION: `scripts/analizar_seccion.py`

PROPOSITO: Analisis automatico de estructura de seccion o directorio

USO:
```bash
python scripts/analizar_seccion.py <ruta_seccion>
```

PARAMETROS:
- ruta_seccion: Path a directorio a analizar

OUTPUT:
- analisis_seccion.json en el directorio analizado
- Reporte en terminal con estadisticas

EJEMPLO:
```bash
python scripts/analizar_seccion.py \
  source/biblioteca/arc42/sections/02_constraints/
```

OUTPUT GENERADO (analisis_seccion.json):
```json
{
  "seccion": "02_constraints",
  "ruta": "sections/02_constraints",
  "total_archivos": 7,
  "archivos_contenido": 6,
  "estadisticas": {
    "total_lineas": 128,
    "total_palabras": 419,
    "total_headings": 5
  },
  "archivos": [...]
}
```

### validar_estructura.sh

UBICACION: `scripts/validar_estructura.sh`

PROPOSITO: Validacion de conformidad con REGLAS_ESTRUCTURA_PROYECTO.rst

USO:
```bash
bash scripts/validar_estructura.sh [ruta_opcional]
```

PARAMETROS:
- ruta_opcional: Path especifico a validar (defecto: proyecto completo)

VALIDA:
- Nomenclatura de archivos (XX_nombre/)
- Estructura de directorios
- Archivos huerfanos (no en toctree)
- Directorios vacios
- Conformidad con convenciones

EJEMPLO:
```bash
# Validar proyecto completo
bash scripts/validar_estructura.sh

# Validar seccion especifica
bash scripts/validar_estructura.sh source/biblioteca/arc42/
```

OUTPUT:
```
VALIDACION ESTRUCTURAL

DIRECTORIOS: OK
NOMENCLATURA: OK
HUERFANOS: 2
VACIOS: 0

ARCHIVOS HUERFANOS:
- source/03_estandares/temporal.rst

ACCION: Agregar a toctree o eliminar
```

### progreso_libro.sh

UBICACION: `scripts/progreso_libro.sh`

PROPOSITO: Calcular progreso de traduccion de un libro

USO:
```bash
bash scripts/progreso_libro.sh <ruta_libro>
```

PARAMETROS:
- ruta_libro: Path al directorio del libro

ANALIZA:
- Archivos completados vs draft
- Porcentaje de avance
- Estimacion de trabajo restante

EJEMPLO:
```bash
bash scripts/progreso_libro.sh source/biblioteca/arc42/
```

OUTPUT:
```
PROGRESO: arc42

Total secciones: 12
Completadas: 2 (17%)
En progreso: 1 (8%)
Pendientes: 9 (75%)

Estimacion: 40 horas restantes
```

## Scripts de Inicializacion

### init_libro.sh

UBICACION: `scripts/init_libro.sh`

PROPOSITO: Inicializar estructura completa de nuevo libro en biblioteca/

USO:
```bash
bash scripts/init_libro.sh <nombre_libro>
```

PARAMETROS:
- nombre_libro: Nombre del libro (snake_case)

CREA:
- Directorio source/biblioteca/<dominio>/<tema>/<nombre_libro>/
- index.rst
- metadata_libro.rst
- glosario_acumulativo.rst
- Subdirectorios necesarios

EJEMPLO:
```bash
bash scripts/init_libro.sh documentacion_kubernetes
```

### init_capitulo.sh

UBICACION: `scripts/init_capitulo.sh`

PROPOSITO: Inicializar estructura de nuevo capitulo en source/

USO:
```bash
bash scripts/init_capitulo.sh <numero> <nombre>
```

PARAMETROS:
- numero: Numero del capitulo (01-99)
- nombre: Nombre del capitulo (snake_case)

CREA:
- Directorio source/<numero>_<nombre>/
- index.rst con toctree
- Subdirectorios estandar
- Actualiza source/index.rst

EJEMPLO:
```bash
bash scripts/init_capitulo.sh 11 nuevos_conceptos
```

### generate_section_metadata.py

UBICACION: `scripts/generate_section_metadata.py` (si existe)

PROPOSITO: Generar o validar metadata de secciones

USO:
```bash
# Generar metadata
python scripts/generate_section_metadata.py \
  --source <url_original> \
  --mode <modo> \
  <archivo_rst>

# Validar metadata
python scripts/generate_section_metadata.py \
  --validate <directorio>
```

## Makefile Targets

### Build y Limpieza

```bash
# Build HTML
make html

# Build HTML limpio (desde cero)
make clean html

# Limpiar solo build
make clean
```

### Validacion

```bash
# Validar enlaces externos e internos
make linkcheck

# Coverage de documentacion
make coverage
```

### Otros Targets

```bash
# Ver todos los targets disponibles
make help
```

## Workflow Tipico

### Traducir Nueva Seccion arc42

```bash
# 1. Analizar seccion
python scripts/analizar_seccion.py \
  source/biblioteca/arc42/sections/03_context_scope/

# 2. Traducir
python scripts/traduccion/arc42_scraper_python.py \
  --section 03 \
  --mode alta_fidelidad

# 3. Validar estructura
bash scripts/validar_estructura.sh

# 4. Build y verificar
make clean html
make linkcheck

# 5. Ver progreso
bash scripts/progreso_libro.sh source/biblioteca/arc42/
```

### Crear y Validar Nuevo Capitulo

```bash
# 1. Inicializar
bash scripts/init_capitulo.sh 11 nuevos_conceptos

# 2. Agregar contenido manualmente
# (editar archivos .rst)

# 3. Validar
bash scripts/validar_estructura.sh

# 4. Build
make html
```

### Traducir Documento Web

```bash
# 1. Descargar y traducir
bash scripts/traduccion/translate_web_content.sh \
  https://example.com/tutorial.html \
  source/diataxis/tutorials/

# 2. Ajustar metadata manualmente

# 3. Validar y build
make html
```

## Ubicacion de Outputs

### Scripts de Traduccion

OUTPUT: Archivos .rst en ubicacion especificada con parametro --output

### analizar_seccion.py

OUTPUT: analisis_seccion.json en directorio analizado

### validar_estructura.sh

OUTPUT: Reporte en terminal (stdout)

### progreso_libro.sh

OUTPUT: Reporte en terminal (stdout)

### Makefile

OUTPUT:
- HTML: build/html/
- Linkcheck: build/linkcheck/output.txt
- Coverage: build/coverage/

## Dependencias

Verificar que estan instaladas:

```bash
# Python packages
pip install -r requirements.txt

# Herramientas del sistema
# (usualmente ya instaladas en Linux/Mac)
bash --version
```

## Troubleshooting

### Script no ejecutable

```bash
# Dar permisos de ejecucion
chmod +x scripts/nombre_script.sh
```

### Error "module not found" en Python

```bash
# Instalar dependencias
pip install -r requirements.txt --break-system-packages
```

### Script no encuentra archivos

```bash
# Asegurar que estas en raiz del proyecto
cd ADT/
pwd  # Debe mostrar: .../ADT

# Ejecutar desde raiz
python scripts/script.py
```

## Notas Importantes

- SIEMPRE ejecutar scripts desde raiz del proyecto (ADT/)
- Scripts Python requieren dependencies de requirements.txt
- Scripts Bash son POSIX-compliant
- Ver README.md en scripts/ para detalles adicionales
- Consultar codigo fuente para parametros avanzados
