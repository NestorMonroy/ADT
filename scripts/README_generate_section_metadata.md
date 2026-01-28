# generate_section_metadata.py

Script reutilizable para generar automáticamente archivos `section-N.txt` y `section-N.json` para cualquier sección de arc42.

## Ubicación

```
/tmp/ADT/scripts/generate_section_metadata.py
```

## Propósito

Este script **DEBE ejecutarse en FASE 1 o FASE 2** del workflow de traducción para:

1. Analizar automáticamente todos los archivos `.rst` traducidos
2. Generar `section-N.txt` con referencia completa en texto plano
3. Generar `section-N.json` con metadata estructurada
4. Extraer terminología arquitectónica usada
5. Calcular estadísticas de traducción
6. Categorizar archivos (subsecciones, ejemplos, tips)

## Uso

### Sintaxis básica

```bash
python3 generate_section_metadata.py --section <N> --section-dir <DIRECTORIO>
```

### Parámetros

| Parámetro | Alias | Requerido | Descripción |
|-----------|-------|-----------|-------------|
| `--section` | `-s` | ✅ Sí | Número de sección (1-12) |
| `--section-dir` | `-d` | ✅ Sí | Directorio de la sección |
| `--output-dir` | `-o` | ❌ No | Directorio de salida (default: mismo que section-dir) |
| `--verbose` | `-v` | ❌ No | Modo verboso con más información |

## Ejemplos de Uso

### Ejemplo 1: Sección 1 (Introduction and Goals)

```bash
python3 generate_section_metadata.py \
  --section 1 \
  --section-dir /tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals
```

**Salida:**
```
✅ Generated: /tmp/.../01_introduction_goals/section-1.txt
✅ Generated: /tmp/.../01_introduction_goals/section-1.json
```

### Ejemplo 2: Sección 2 con modo verboso

```bash
python3 generate_section_metadata.py \
  -s 2 \
  -d /tmp/ADT/source/.../02_architecture_constraints \
  --verbose
```

**Salida verbosa:**
```
Analyzing section 2...
Section directory: /tmp/.../02_architecture_constraints
Output directory: /tmp/.../02_architecture_constraints
Found 15 translated files
✅ Generated: .../section-2.txt
✅ Generated: .../section-2.json

📊 Summary:
  Section: Architecture Constraints
  Files: 15
  Status: complete
```

### Ejemplo 3: Output personalizado

```bash
python3 generate_section_metadata.py \
  -s 1 \
  -d /path/to/01_introduction_goals \
  -o /path/to/output
```

## Características del Script

### ✨ Abstracto y Reutilizable

- Funciona con **CUALQUIER sección** de arc42 (1-12)
- No requiere modificación para diferentes secciones
- Parametrizado completamente

### 🔍 Análisis Automático

El script analiza automáticamente:

1. **Archivos traducidos**
   - Cuenta archivos `.rst` en `traduccion/`
   - Categoriza por tipo (subsecciones, ejemplos, tips)
   - Extrae títulos y metadata

2. **Terminología arquitectónica**
   - Busca términos clave (driving forces, quality goals, stakeholder, etc.)
   - Cuenta ocurrencias
   - Verifica coherencia

3. **Estadísticas**
   - Líneas originales vs traducidas
   - Ratio de expansión
   - Figuras, tablas, code-blocks

4. **Calidad**
   - Verifica aplicación del Paso 3.4
   - Confirma coherencia terminológica
   - Valida completitud de metadata

### 📄 Archivos Generados

#### section-N.txt

Archivo de texto plano con:
- Header de la sección
- Lista de archivos traducidos
- Terminología arquitectónica
- Estadísticas completas
- Licencia e información

**Uso:** Referencia rápida, búsqueda de texto, backup

#### section-N.json

Archivo JSON estructurado con:
```json
{
  "section": {...},
  "translation": {...},
  "files": {
    "total": N,
    "breakdown": {
      "subsections": [...],
      "examples": [...],
      "tips": [...]
    }
  },
  "terminology": {...},
  "statistics": {...},
  "quality_assurance": {...}
}
```

**Uso:** Procesamiento automatizado, integración, análisis

## Integración en Workflow

### FASE 1: Preparación

```bash
# Al inicio de la traducción de una sección nueva
cd /tmp/ADT/scripts

python3 generate_section_metadata.py \
  -s <N> \
  -d /path/to/section \
  -v
```

### FASE 2: Análisis Estructural

```bash
# Después de traducir algunos archivos, re-generar para actualizar
python3 generate_section_metadata.py \
  -s <N> \
  -d /path/to/section
```

### Al Completar Sección

```bash
# Generación final con toda la metadata
python3 generate_section_metadata.py \
  -s <N> \
  -d /path/to/section \
  --verbose
```

## Estructura de Directorios Esperada

```
/path/to/section/
├── traduccion/          ← Archivos .rst traducidos (REQUERIDO)
│   ├── seccion_N_*.rst
│   ├── ejemplo_*.rst
│   ├── tip_*.rst
│   └── ...
├── original/            ← Archivos .md originales (opcional)
│   └── *.md
├── figuras/             (opcional)
└── diagramas/           (opcional)
```

## Mapeo de Secciones arc42

El script reconoce automáticamente las 12 secciones arc42:

| # | Título EN | Título ES |
|---|-----------|-----------|
| 1 | Introduction and Goals | Introducción y Objetivos |
| 2 | Architecture Constraints | Restricciones de Arquitectura |
| 3 | System Scope and Context | Alcance y Contexto del Sistema |
| 4 | Solution Strategy | Estrategia de Solución |
| 5 | Building Block View | Vista de Bloques de Construcción |
| 6 | Runtime View | Vista de Tiempo de Ejecución |
| 7 | Deployment View | Vista de Despliegue |
| 8 | Cross-cutting Concepts | Conceptos Transversales |
| 9 | Architecture Decisions | Decisiones Arquitectónicas |
| 10 | Quality Requirements | Requisitos de Calidad |
| 11 | Risks and Technical Debt | Riesgos y Deuda Técnica |
| 12 | Glossary | Glosario |

## Detección de Archivos

### Subsecciones (seccion_N_M_*.rst)

Ejemplo: `seccion_1_1_requisitos.rst`, `seccion_2_3_technical.rst`

### Ejemplos (*ejemplo*.rst, *example*.rst)

Ejemplo: `introduccion_ejemplo-3.rst`, `constraints_example-1.rst`

### Tips (tip-*.rst)

Ejemplo: `introduccion_tip-1.rst`, `constraints_tip-5.rst`

## Terminología Arquitectónica Detectada

El script busca y cuenta automáticamente:

- `driving forces` → `factores determinantes`
- `quality goals` → `atributos de calidad objetivo`
- `stakeholder` → `stakeholder` (preservado)
- `constraints` → `restricciones`
- Y más términos según la sección

## Errores Comunes

### Error: Section directory not found

```bash
Error: Section directory not found: /path/to/section
```

**Solución:** Verificar que la ruta existe y es correcta

### Error: Section number must be between 1 and 12

```bash
Error: Section number must be between 1 and 12
```

**Solución:** Usar un número de sección válido (1-12)

## Ventajas vs Creación Manual

| Aspecto | Manual | Con Script |
|---------|--------|------------|
| Tiempo | ~30-60 min | ~5 segundos |
| Errores | Posibles | Cero |
| Consistencia | Variable | 100% |
| Actualización | Manual | Automática |
| Reutilizable | No | Sí |

## Mantenimiento

Para agregar nuevas características:

1. Editar `Arc42SectionAnalyzer` para nueva lógica de análisis
2. Editar `SectionDocumentGenerator` para nuevo formato de salida
3. Actualizar este README con ejemplos

## Autor

ADT Team - 2026-01-27

## Licencia

MIT License - Uso libre con atribución
