# Design: Corrección de Errores de Build Sphinx

**Versión**: 1.1.0
**Basado en**: Requirements v1.0.0 (`2026-01-30-03-31-requirements-corregir-errores-build.md`)
**Fecha**: 2026-01-30
**Estado**: Draft
**Tipo**: Refactoring / Quality Assurance

## Control de Versiones

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0.0 | 2026-01-30 03:43 | Claude | Versión inicial del diseño técnico |
| 1.1.0 | 2026-01-30 03:50 | Claude | Tests movidos a /tests/ (hermana de scripts/). Scripts organizados en subcarpetas. Agregado uso de regex/NLP para casos complejos |

## 1. Visión General

### 1.1 Estrategia de Alto Nivel

**Enfoque**: Corrección incremental por lotes categorizados con validación continua

**Fases de corrección**:
1. **CRÍTICO** (33 issues) → Estabilizar estructura
2. **ERROR** (72 issues) → Eliminar errores de parseo
3. **WARNING-Alta** (467 issues) → Corregir problemas de alto impacto
4. **WARNING-Media** (377 issues) → Normalización general

**Principios guía**:
- Correcciones atómicas por categoría
- Validación después de cada lote
- Commits frecuentes (rollback granular)
- Scripts funcionales reutilizables
- Tests automatizados antes de aplicar

### 1.2 Arquitectura de Solución

```
┌─────────────────────────────────────────────────────────────┐
│                    PIPELINE DE CORRECCIÓN                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  FASE 1: ANÁLISIS                                           │
│  - Categorizar issues por tipo                              │
│  - Priorizar por impacto                                    │
│  - Identificar archivos afectados                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  FASE 2: SELECCIÓN DE HERRAMIENTAS                          │
│  - Evaluar scripts existentes                               │
│  - Identificar gaps (scripts faltantes)                     │
│  - Diseñar nuevos scripts funcionales                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  FASE 3: DESARROLLO/ACTUALIZACIÓN                           │
│  - Desarrollar scripts faltantes                            │
│  - Actualizar scripts deficientes                           │
│  - Crear tests unitarios (pytest)                           │
│  - Validar en dry-run mode                                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  FASE 4: APLICACIÓN INCREMENTAL                             │
│  - Ejecutar scripts por lote                                │
│  - Validar con make html                                    │
│  - Review manual de cambios críticos                        │
│  - Commit por lote                                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  FASE 5: VALIDACIÓN FINAL                                   │
│  - Build completo limpio                                    │
│  - Comparación baseline vs final                            │
│  - Generación de reporte                                    │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 Orden de Corrección (Priorizado)

| Lote | Categoría | Issues | Estrategia | Script |
|------|-----------|--------|------------|--------|
| L1 | Section Title Issues (CRITICAL) | 25 | Script nuevo | `fix_section_structure.py` |
| L2 | Title Underline (CRITICAL) | 8 | Script nuevo | `fix_title_underlines.py` |
| L3 | Indentation (ERROR) | 28 | Script nuevo | `fix_indentation_errors.py` |
| L4 | Content Block Parsing (ERROR) | 18 | Manual + documentar | - |
| L5 | Missing Content (ERROR) | 11 | Manual + documentar | - |
| L6 | Document Heading Levels (WARNING) | 339 | Script nuevo | `fix_heading_levels.py` |
| L7 | Missing Images (WARNING) | 142 | Script nuevo | `resolve_image_references.py` |
| L8 | List Formatting (WARNING) | 100 | Script existente actualizado | `fix_list_spacing.py` |
| L9 | Title Formatting (WARNING) | 88 | Cubierto por L2 | - |
| L10 | Duplicate Labels (WARNING) | 43 | Script existente + manual | `find_duplicate_labels.py` |
| L11 | List Tables (WARNING) | ~30 | Scripts existentes | `fix_list_table_*.py` |
| L12 | Glossary Terms (WARNING) | 17 | Manual (fuera alcance) | - |
| L13 | Otros (WARNING) | ~100 | Caso por caso | Varios |

**Total issues cubiertos con scripts**: ~802 (84.5%)
**Total issues manuales/fuera alcance**: ~147 (15.5%)

## 2. Decisiones Arquitectónicas

### DA-001: Estrategia de Corrección Incremental por Lotes

**Contexto**: 
- Tenemos 949 issues distribuidos en 730 archivos
- Corrección masiva simultánea es riesgosa
- Necesitamos capacidad de rollback granular

**Decisión**: 
Corregir incrementalmente en 13 lotes categorizados, validando después de cada lote.

**Alternativas consideradas**:
1. ❌ Corrección masiva en un solo commit
   - Riesgo: Difícil identificar qué corrección rompe
   - Rollback: Todo o nada
2. ❌ Corrección archivo por archivo
   - Tiempo: Extremadamente lento (730 archivos)
   - Overhead: Commits excesivos
3. ✅ Corrección por lotes categorizados
   - Balance entre granularidad y eficiencia
   - Commits significativos y rollbackeables

**Consecuencias**:
- ✅ Rollback granular si algo falla
- ✅ Validación incremental detecta problemas temprano
- ✅ Progreso visible y medible
- ⚠️ Requiere disciplina en orden de ejecución
- ⚠️ Más commits en historial (pero informativos)

### DA-002: Programación Funcional en Scripts Python

**Contexto**:
- Scripts existentes usan estilo imperativo con side-effects
- Necesitamos scripts confiables, testables y mantenibles
- Proyecto adopta estándares de calidad altos

**Decisión**:
Todos los scripts (nuevos y actualizados) usarán programación funcional pura.

**Principios arquitectónicos**:
```python
# BIEN: Función pura
def fix_title_underline(line: str, title: str) -> str:
    """Retorna nueva línea con underline correcto."""
    return '=' * len(title)

# MAL: Función con side-effect
def fix_title_underline(file_path: str) -> None:
    """Modifica archivo in-place."""
    with open(file_path, 'w') as f:  # Side-effect!
        f.write(new_content)
```

**Arquitectura de script tipo**:
```python
from typing import List, Tuple
from pathlib import Path
from functools import reduce

# 1. PARSERS (str → estructura)
def parse_rst_file(content: str) -> List[Block]:
    """Parsea RST a bloques estructurados."""
    ...

# 2. TRANSFORMERS (estructura → estructura)
def fix_blocks(blocks: List[Block]) -> List[Block]:
    """Aplica correcciones a bloques."""
    return [fix_block(b) for b in blocks]

# 3. RENDERERS (estructura → str)
def render_blocks(blocks: List[Block]) -> str:
    """Renderiza bloques a RST."""
    ...

# 4. IO (side-effects aislados)
def process_file(path: Path, dry_run: bool = True) -> Tuple[bool, str]:
    """Procesa archivo, retorna (success, diff)."""
    content = path.read_text()  # Input
    blocks = parse_rst_file(content)
    fixed = fix_blocks(blocks)
    new_content = render_blocks(fixed)
    
    if not dry_run:
        path.write_text(new_content)  # Output
    
    return (True, compute_diff(content, new_content))
```

**Alternativas consideradas**:
1. ❌ Mantener estilo imperativo
   - Difícil de testear
   - Propenso a bugs
2. ❌ POO con clases
   - Overkill para transformaciones simples
   - Más boilerplate
3. ✅ Programación funcional
   - Testeable (funciones puras)
   - Composable (pipe transformaciones)
   - Declarativo (fácil de entender)

**Consecuencias**:
- ✅ Scripts testables con pytest fácilmente
- ✅ Menos bugs por ausencia de side-effects
- ✅ Composición para casos complejos
- ✅ Dry-run mode trivial de implementar
- ⚠️ Curva de aprendizaje para colaboradores imperativos
- ⚠️ Más memoria (inmutabilidad)

### DA-003: Dry-Run Mode Obligatorio en Scripts

**Contexto**:
- Scripts modificarán cientos de archivos
- Errores en scripts pueden dañar contenido
- Necesitamos validar cambios antes de aplicar

**Decisión**:
Todos los scripts tendrán modo `--dry-run` que solo reporta cambios sin aplicarlos.

**Interfaz estándar**:
```bash
# Dry-run (default)
python scripts/fix_heading_levels.py source/ --dry-run

# Output:
# [DRY-RUN] Would fix: source/01_fundamentos/index.rst
#   - Line 5: H2 → H1
#   - Line 12: H3 → H2
# [DRY-RUN] Would fix: source/02_procedimientos/workflow.rst
#   - Line 8: H3 → H2
# Total files affected: 45
# Total changes: 127

# Aplicar cambios reales
python scripts/fix_heading_levels.py source/ --apply

# Output:
# [APPLIED] Fixed: source/01_fundamentos/index.rst (2 changes)
# [APPLIED] Fixed: source/02_procedimientos/workflow.rst (1 change)
# Total files modified: 45
# Total changes applied: 127
```

**Consecuencias**:
- ✅ Validación sin riesgo
- ✅ Preview de cambios antes de commit
- ✅ Debugging de lógica de script
- ⚠️ Requiere implementar diff output
- ⚠️ Dos modos de ejecución a testear

### DA-004: Tests Unitarios con Pytest (Coverage > 80%)

**Contexto**:
- Scripts críticos que modifican archivos del proyecto
- Necesitamos confianza en correcciones
- Programación funcional facilita testing

**Decisión**:
Cada script tendrá suite de tests con pytest, cobertura mínima 80%.

**Estructura de tests**:
```
scripts/
├── fix_heading_levels.py
└── tests/
    ├── test_fix_heading_levels.py
    └── fixtures/
        ├── sample_incorrect.rst
        └── sample_expected.rst
```

**Ejemplo de test**:
```python
# tests/test_fix_heading_levels.py
import pytest
from fix_heading_levels import fix_heading_level, parse_rst_file

def test_fix_heading_level_h2_to_h1():
    input_line = "Título\n------"
    expected = "Título\n======"
    assert fix_heading_level(input_line, current=2, target=1) == expected

def test_parse_rst_file_with_fixture():
    content = Path('fixtures/sample_incorrect.rst').read_text()
    blocks = parse_rst_file(content)
    assert len(blocks) == 5
    assert blocks[0].level == 2  # Incorrecto

def test_full_pipeline():
    input_rst = Path('fixtures/sample_incorrect.rst').read_text()
    expected = Path('fixtures/sample_expected.rst').read_text()
    
    blocks = parse_rst_file(input_rst)
    fixed = fix_blocks(blocks)
    output = render_blocks(fixed)
    
    assert output == expected
```

**Alternativas consideradas**:
1. ❌ Sin tests
   - Riesgo alto de bugs
   - No confiable
2. ❌ Tests manuales
   - No escalable
   - No reproducible
3. ✅ Tests automatizados pytest
   - Rápido feedback
   - Reproducible
   - Integrable en CI/CD

**Consecuencias**:
- ✅ Confianza en scripts
- ✅ Detecta regresiones
- ✅ Documentación ejecutable
- ⚠️ Tiempo de desarrollo mayor
- ⚠️ Requiere fixtures representativas

### DA-005: Validación Continua con Make HTML

**Contexto**:
- Correcciones pueden introducir nuevos errores
- Build completo tarda ~25 segundos
- Necesitamos feedback rápido

**Decisión**:
Validar con `make clean html` después de cada lote de correcciones.

**Pipeline de validación**:
```bash
# 1. Aplicar lote
python scripts/fix_section_structure.py source/ --apply

# 2. Validar build
make clean html > build_lote_L1.log 2>&1

# 3. Analizar resultado
python scripts/analyze_build_log.py build_lote_L1.log

# 4. Si OK → commit, si FAIL → rollback
if [ $? -eq 0 ]; then
    git add source/
    git commit -m "fix(critical): correct section structure (L1)"
else
    git checkout -- source/
    echo "ROLLBACK: Script introdujo errores"
fi
```

**Métricas de validación**:
- Exit code de make
- Reducción neta de issues (no debe aumentar)
- No nuevos CRITICAL o ERROR
- Warnings pueden fluctuar (categorías diferentes)

**Consecuencias**:
- ✅ Detecta problemas inmediatamente
- ✅ Previene acumulación de errores
- ✅ Rollback automático si falla
- ⚠️ Tiempo de validación (25s por lote × 13 lotes = ~5 min)

### DA-006: Scripts Reutilizables como Biblioteca

**Contexto**:
- Múltiples scripts compartirán funcionalidad (parseo RST)
- Evitar duplicación de código
- Facilitar mantenimiento

**Decisión**:
Crear módulo `rst_utils` con funciones compartidas.

**Estructura**:
```
scripts/
├── rst_utils/
│   ├── __init__.py
│   ├── parser.py      # parse_rst_file, parse_block
│   ├── renderer.py    # render_blocks, render_block
│   ├── analyzer.py    # detect_heading_level, find_issues
│   └── types.py       # Block, Heading, List, etc.
├── fix_heading_levels.py  # Usa rst_utils
├── fix_section_structure.py  # Usa rst_utils
└── fix_title_underlines.py   # Usa rst_utils
```

**Ejemplo de uso**:
```python
# fix_heading_levels.py
from rst_utils import parse_rst_file, render_blocks
from rst_utils.analyzer import detect_heading_levels

def fix_heading_levels(content: str) -> str:
    blocks = parse_rst_file(content)
    issues = detect_heading_levels(blocks)
    fixed = apply_fixes(blocks, issues)
    return render_blocks(fixed)
```

**Consecuencias**:
- ✅ DRY (Don't Repeat Yourself)
- ✅ Mantenimiento centralizado
- ✅ Tests compartidos
- ⚠️ Dependencia entre scripts
- ⚠️ Requiere diseño cuidadoso de API

### DA-007: Estrategia Híbrida: Scripts + Manual

**Contexto**:
- Algunos issues son demasiado complejos para automatizar
- Content Block Parsing (18) requiere análisis contextual
- Missing Content (11) requiere decisión de qué agregar

**Decisión**:
Combinar corrección automatizada (scripts) con manual (revisión humana).

**Categorías por estrategia**:

**AUTOMATIZABLE (85%)** - Scripts:
- Section Title Issues
- Title Underline
- Indentation
- Heading Levels
- List Formatting
- Duplicate Labels

**SEMI-AUTOMATIZABLE (10%)** - Script + Manual:
- Missing Images (script identifica, humano decide)
- Content Block Parsing (script reporta, humano corrige)

**MANUAL (5%)** - Revisión humana:
- Missing Content (requiere contenido nuevo)
- Casos edge complejos

**Consecuencias**:
- ✅ Eficiencia en casos simples
- ✅ Calidad en casos complejos
- ⚠️ Requiere documentar casos manuales
- ⚠️ Dos workflows diferentes

### DA-008: Uso de Regex y Herramientas Avanzadas para Casos Complejos

**Contexto**:
- Algunos patrones RST son complejos de detectar con parsing simple
- Issues específicos pueden requerir análisis sofisticado
- Necesitamos flexibilidad para casos difíciles

**Decisión**:
Utilizar regex, NLP y otras herramientas de IA cuando sea apropiado para casos complejos.

**Herramientas disponibles**:

**1. Expresiones Regulares (regex)**:
```python
import re

# Detectar títulos con underline incorrecto
TITLE_PATTERN = re.compile(
    r'^(.+)\n([=\-~^"+\'`:])\2+$',  # Título + underline
    re.MULTILINE
)

# Detectar variables sin expandir
IMAGE_VAR_PATTERN = re.compile(
    r'\{\{site\.(imageurl|baseurl|url)\}\}'
)

# Detectar indentación inconsistente
INDENT_PATTERN = re.compile(
    r'^( {2,})(?! )',  # Múltiples espacios no uniformes
    re.MULTILINE
)
```

**2. Análisis de Tokens (tokenización)**:
```python
from typing import List, Tuple

def tokenize_rst_block(text: str) -> List[Tuple[str, str]]:
    """Tokeniza RST en (tipo, contenido)."""
    # Usar regex combinado con lógica contextual
    tokens = []
    for line in text.split('\n'):
        if re.match(r'^\.\.', line):
            tokens.append(('directive', line))
        elif re.match(r'^[=\-~^]+$', line):
            tokens.append(('underline', line))
        else:
            tokens.append(('text', line))
    return tokens
```

**3. Análisis de Contexto (state machine)**:
```python
from enum import Enum
from typing import Optional

class ParserState(Enum):
    NORMAL = 1
    IN_DIRECTIVE = 2
    IN_CODE_BLOCK = 3
    IN_LIST = 4

def analyze_with_context(lines: List[str]) -> List[Issue]:
    """Analiza RST considerando contexto."""
    state = ParserState.NORMAL
    issues = []
    
    for i, line in enumerate(lines):
        if state == ParserState.NORMAL:
            if re.match(r'^\.\. \w+::', line):
                state = ParserState.IN_DIRECTIVE
        # ... lógica de state machine
    
    return issues
```

**4. Fuzzy Matching para Detección de Errores**:
```python
from difflib import SequenceMatcher

def detect_title_mismatch(title: str, underline: str) -> bool:
    """Detecta si underline no coincide con título."""
    expected_length = len(title)
    actual_length = len(underline)
    
    # Tolerancia de ±2 caracteres
    return abs(expected_length - actual_length) > 2
```

**5. Pattern Recognition con Heurísticas**:
```python
def detect_section_structure_issue(blocks: List[Block]) -> Optional[Issue]:
    """Detecta problemas de estructura con heurísticas."""
    headings = [b for b in blocks if isinstance(b, Heading)]
    
    # Heurística: primer heading debe ser H1
    if headings and headings[0].level != 1:
        return Issue(
            severity='critical',
            category='section_structure',
            message=f'Document starts at H{headings[0].level}, should be H1'
        )
    
    # Heurística: no saltar niveles
    for i in range(1, len(headings)):
        level_jump = headings[i].level - headings[i-1].level
        if level_jump > 1:
            return Issue(
                severity='warning',
                category='heading_levels',
                message=f'Heading level jumps from {headings[i-1].level} to {headings[i].level}'
            )
    
    return None
```

**6. NLP/ML para Casos Avanzados (opcional)**:
```python
# Para casos muy complejos (si se necesita)
from typing import List

def classify_content_type(text: str) -> str:
    """
    Clasifica tipo de contenido usando heurísticas.
    En casos muy complejos, podría usar un modelo ML.
    """
    # Heurísticas simples primero
    if re.match(r'^\.\. (code-block|literalinclude)::', text):
        return 'code'
    elif re.match(r'^\.\. (note|warning|tip|important)::', text):
        return 'admonition'
    elif re.match(r'^-|\*|\d+\.', text.strip()):
        return 'list'
    
    # Si ninguna heurística funciona, análisis más profundo
    # (podría usar spaCy, transformers, etc. si se justifica)
    return 'paragraph'
```

**Casos de uso específicos**:

| Problema | Herramienta | Ejemplo |
|----------|-------------|---------|
| Títulos mal formados | Regex | `r'^(.+)\n([=\-]+)$'` |
| Variables sin expandir | Regex | `r'\{\{.*?\}\}'` |
| Indentación inconsistente | Regex + análisis | Detectar múltiples niveles |
| Estructura de secciones | State machine | Tracking de niveles |
| Content block parsing | Tokenización + contexto | Identificar bloques válidos |
| Detección de errores sutiles | Fuzzy matching | Comparar patrones esperados |

**Alternativas consideradas**:
1. ❌ Solo parsing estructural simple
   - No maneja casos edge
   - Falsos positivos/negativos
2. ❌ Solo regex complejos
   - Difícil de mantener
   - Frágil ante variaciones
3. ✅ Combinación de técnicas
   - Regex para patrones simples
   - State machines para contexto
   - Heurísticas para casos complejos
   - ML solo si es absolutamente necesario

**Consecuencias**:
- ✅ Mayor cobertura de casos
- ✅ Menos falsos positivos
- ✅ Manejo robusto de variaciones
- ⚠️ Mayor complejidad de código
- ⚠️ Requiere tests exhaustivos
- ⚠️ Posible over-engineering (evitar ML innecesario)

## 3. Componentes Afectados

### 3.1 Nuevos Componentes

**Scripts de corrección organizados** (a crear):
```
scripts/
├── correction/                        # NUEVA: Scripts de corrección
│   ├── __init__.py
│   ├── fix_section_structure.py      # L1: CRITICAL section titles
│   ├── fix_title_underlines.py       # L2: CRITICAL underlines
│   ├── fix_indentation_errors.py     # L3: ERROR indentation
│   ├── fix_heading_levels.py         # L6: WARNING heading levels
│   └── resolve_image_references.py   # L7: WARNING missing images
├── analysis/                          # NUEVA: Scripts de análisis
│   ├── __init__.py
│   ├── analyze_build_log.py          # Ya existe (mover aquí)
│   ├── find_duplicate_labels.py      # Ya existe (mover aquí)
│   └── find_duplicate_toctree.py     # Ya existe (mover aquí)
└── lib/                               # NUEVA: Biblioteca compartida
    ├── __init__.py
    ├── rst_utils/                     # Utilidades RST
    │   ├── __init__.py
    │   ├── parser.py                  # parse_rst_file, parse_block
    │   ├── renderer.py                # render_blocks, render_block
    │   ├── analyzer.py                # detect_issues
    │   └── types.py                   # Block, Heading, Issue (dataclasses)
    └── regex_patterns.py              # Regex patterns compartidos
```

**Tests** (en /tests/ como hermana de scripts/):
```
tests/
├── test_correction/                   # Tests para scripts/correction/
│   ├── __init__.py
│   ├── test_fix_section_structure.py
│   ├── test_fix_title_underlines.py
│   ├── test_fix_indentation_errors.py
│   ├── test_fix_heading_levels.py
│   └── test_resolve_image_references.py
├── test_analysis/                     # Tests para scripts/analysis/
│   ├── __init__.py
│   ├── test_analyze_build_log.py
│   ├── test_find_duplicate_labels.py
│   └── test_find_duplicate_toctree.py
├── test_lib/                          # Tests para scripts/lib/
│   ├── __init__.py
│   ├── test_rst_utils/
│   │   ├── test_parser.py
│   │   ├── test_renderer.py
│   │   └── test_analyzer.py
│   └── test_regex_patterns.py
└── fixtures/                          # Fixtures compartidas
    ├── section_structure/
    │   ├── input_incorrect.rst
    │   └── output_expected.rst
    ├── title_underlines/
    │   ├── input_incorrect.rst
    │   └── output_expected.rst
    ├── indentation/
    │   ├── input_incorrect.rst
    │   └── output_expected.rst
    └── heading_levels/
        ├── input_incorrect.rst
        └── output_expected.rst
```

**Biblioteca de patrones regex** (a crear):
```python
# scripts/lib/regex_patterns.py
"""Patrones regex compartidos para análisis RST."""

import re
from typing import Pattern

# Títulos con underline
TITLE_WITH_UNDERLINE: Pattern = re.compile(
    r'^(.+)\n([=\-~^"+\'`:])\2+$',
    re.MULTILINE
)

# Variables de template sin expandir
TEMPLATE_VARIABLE: Pattern = re.compile(
    r'\{\{site\.(imageurl|baseurl|url)\}\}'
)

# Directivas RST
DIRECTIVE: Pattern = re.compile(
    r'^\.\. (\w+)::',
    re.MULTILINE
)

# Listas (bullet/enumerated)
LIST_ITEM: Pattern = re.compile(
    r'^(\s*)([*\-+]|\d+\.|\#\.)\s+',
    re.MULTILINE
)

# Indentación
INDENTATION: Pattern = re.compile(
    r'^( +)',
    re.MULTILINE
)

# Bloques de código
CODE_BLOCK: Pattern = re.compile(
    r'^\.\. (code-block|literalinclude)::.*?$',
    re.MULTILINE
)

# Referencias internas
INTERNAL_REF: Pattern = re.compile(
    r':(?:doc|ref):`([^`]+)`'
)

# Labels
LABEL: Pattern = re.compile(
    r'^\.\. _([a-zA-Z0-9_\-]+):',
    re.MULTILINE
)
```

### 3.2 Componentes Modificados

**Scripts existentes** (a actualizar y reorganizar):

```
scripts/
├── correction/                        # Reorganizar aquí
│   ├── fix_list_spacing.py           # MOVER + refactorizar a funcional
│   ├── fix_list_table_spacing.py     # MOVER + refactorizar a funcional
│   ├── fix_glossary_indentation.py   # MOVER + refactorizar a funcional
│   ├── fix_unknown_lexers.py         # MOVER + refactorizar a funcional
│   ├── fix_blanklines_and_listtable_fp.py  # YA es funcional, MOVER
│   ├── fix_list_table_blocks_fp.py   # YA es funcional, MOVER
│   ├── fix_list_table_indent_fp.py   # YA es funcional, MOVER
│   └── fix_meta_transition.py        # MOVER + revisar
└── analysis/                          # Reorganizar aquí
    ├── find_duplicate_labels.py      # MOVER + agregar auto-fix mode
    └── find_duplicate_toctree.py     # MOVER + mantener

# Scripts existentes que permanecen en raíz (no son de corrección)
scripts/
├── actualizar_metadata_arc42.sh      # Metadata (categoría diferente)
├── analisis_profundo_funcional.py    # Análisis (categoría diferente)
├── analizar_seccion.py                # Análisis (categoría diferente)
├── clasificador_biblioteca.py         # Clasificación (categoría diferente)
├── clonar_repo_arc42.sh               # Setup (categoría diferente)
├── convert_to_lf.py                   # Utilidad (categoría diferente)
├── corregir_nombres_arc42.sh          # Utilidad (categoría diferente)
├── distribuir_archivos_arc42.sh       # Utilidad (categoría diferente)
└── validar_estructura.sh              # Validación (sin cambios)
```

**Cambios por script**:

**fix_list_spacing.py** → **scripts/correction/fix_list_spacing.py**:
- Refactorizar de imperativo a funcional
- Agregar type hints completos
- Agregar tests en /tests/test_correction/
- Mantener funcionalidad actual

**fix_list_table_spacing.py** → **scripts/correction/fix_list_table_spacing.py**:
- Refactorizar a funcional
- Agregar dry-run mode si no existe
- Tests exhaustivos

**fix_glossary_indentation.py** → **scripts/correction/fix_glossary_indentation.py**:
- Refactorizar a funcional
- Validar contra casos reales del proyecto
- Actualizar si hay gaps

**find_duplicate_labels.py** → **scripts/analysis/find_duplicate_labels.py**:
- NUEVO: Agregar modo auto-fix (opcional)
- Mantener modo detect-only (default)
- Sugerir nombres alternativos para labels duplicados

**Scripts *_fp.py** (ya funcionales):
- Solo mover a subcarpeta correcta
- Agregar tests si no existen
- Verificar que sigan estándares

**Archivos RST** (~730 archivos en `source/`):
- Modificados incrementalmente por lotes
- Sin cambios en estructura de directorios
- Metadata preservada

### 3.3 Componentes Deprecados

**Ninguno**. Scripts existentes se reorganizan y actualizan, no se eliminan.

## 4. Estructura de Archivos

### 4.1 Estructura de Scripts (Post-Implementación)

```
ADT/
├── scripts/
│   ├── correction/                    # NUEVA: Scripts de corrección
│   │   ├── __init__.py
│   │   ├── fix_section_structure.py   # NUEVO: L1
│   │   ├── fix_title_underlines.py    # NUEVO: L2
│   │   ├── fix_indentation_errors.py  # NUEVO: L3
│   │   ├── fix_heading_levels.py      # NUEVO: L6
│   │   ├── resolve_image_references.py # NUEVO: L7
│   │   ├── fix_list_spacing.py        # MOVIDO + refactorizado
│   │   ├── fix_list_table_spacing.py  # MOVIDO + refactorizado
│   │   ├── fix_glossary_indentation.py # MOVIDO + refactorizado
│   │   ├── fix_unknown_lexers.py      # MOVIDO + refactorizado
│   │   ├── fix_blanklines_and_listtable_fp.py  # MOVIDO
│   │   ├── fix_list_table_blocks_fp.py # MOVIDO
│   │   ├── fix_list_table_indent_fp.py # MOVIDO
│   │   └── fix_meta_transition.py     # MOVIDO
│   ├── analysis/                      # NUEVA: Scripts de análisis
│   │   ├── __init__.py
│   │   ├── analyze_build_log.py       # MOVIDO (de /tmp/)
│   │   ├── find_duplicate_labels.py   # MOVIDO + auto-fix
│   │   └── find_duplicate_toctree.py  # MOVIDO
│   ├── lib/                           # NUEVA: Bibliotecas compartidas
│   │   ├── __init__.py
│   │   ├── rst_utils/
│   │   │   ├── __init__.py
│   │   │   ├── parser.py              # NUEVO
│   │   │   ├── renderer.py            # NUEVO
│   │   │   ├── analyzer.py            # NUEVO
│   │   │   └── types.py               # NUEVO
│   │   └── regex_patterns.py          # NUEVO
│   ├── actualizar_metadata_arc42.sh   # SIN CAMBIOS
│   ├── analisis_profundo_funcional.py # SIN CAMBIOS
│   ├── analizar_seccion.py            # SIN CAMBIOS
│   ├── clasificador_biblioteca.py     # SIN CAMBIOS
│   ├── clonar_repo_arc42.sh           # SIN CAMBIOS
│   ├── convert_to_lf.py               # SIN CAMBIOS
│   ├── corregir_nombres_arc42.sh      # SIN CAMBIOS
│   ├── distribuir_archivos_arc42.sh   # SIN CAMBIOS
│   ├── validar_estructura.sh          # SIN CAMBIOS
│   ├── README.md                      # ACTUALIZAR
│   └── __init__.py                    # SIN CAMBIOS
├── tests/                             # HERMANA de scripts/
│   ├── test_correction/               # NUEVO: Tests de corrección
│   │   ├── __init__.py
│   │   ├── test_fix_section_structure.py
│   │   ├── test_fix_title_underlines.py
│   │   ├── test_fix_indentation_errors.py
│   │   ├── test_fix_heading_levels.py
│   │   ├── test_resolve_image_references.py
│   │   ├── test_fix_list_spacing.py
│   │   ├── test_fix_list_table_spacing.py
│   │   └── test_fix_glossary_indentation.py
│   ├── test_analysis/                 # NUEVO: Tests de análisis
│   │   ├── __init__.py
│   │   ├── test_analyze_build_log.py
│   │   ├── test_find_duplicate_labels.py
│   │   └── test_find_duplicate_toctree.py
│   ├── test_lib/                      # NUEVO: Tests de bibliotecas
│   │   ├── __init__.py
│   │   ├── test_rst_utils/
│   │   │   ├── __init__.py
│   │   │   ├── test_parser.py
│   │   │   ├── test_renderer.py
│   │   │   └── test_analyzer.py
│   │   └── test_regex_patterns.py
│   ├── fixtures/                      # NUEVO: Fixtures compartidas
│   │   ├── section_structure/
│   │   │   ├── input_incorrect.rst
│   │   │   └── output_expected.rst
│   │   ├── title_underlines/
│   │   │   ├── input_incorrect.rst
│   │   │   └── output_expected.rst
│   │   ├── indentation/
│   │   │   ├── input_incorrect.rst
│   │   │   └── output_expected.rst
│   │   └── heading_levels/
│   │       ├── input_incorrect.rst
│   │       └── output_expected.rst
│   └── conftest.py                    # NUEVO: Configuración pytest
├── source/                            # MODIFICADO: 730 archivos RST
│   └── ... (sin cambios estructurales)
└── .mywork/
    └── changes/2026-01-30-corregir-errores-build-sphinx/
        ├── 2026-01-30-03-31-requirements-v1.0.0.md
        ├── 2026-01-30-03-43-design-v1.1.0.md  # ESTE ARCHIVO
        └── logs/                      # NUEVO: Logs de validación
            ├── build_lote_L1.log
            ├── build_lote_L2.log
            └── ...
```

**Justificación de la estructura**:

**scripts/correction/**:
- Agrupa todos los scripts que CORRIGEN archivos
- Facilita encontrar herramientas de corrección
- Clara separación de responsabilidades

**scripts/analysis/**:
- Scripts que solo ANALIZAN (no modifican)
- find_duplicate_* son análisis
- analyze_build_log.py es análisis

**scripts/lib/**:
- Código reutilizable
- rst_utils: lógica común de RST
- regex_patterns: patrones compartidos

**tests/** (hermana, no hija):
- Estructura paralela a scripts/
- Más fácil de configurar pytest
- Convención estándar de Python
- Evita importación circular

**Scripts en raíz de scripts/**:
- Scripts específicos de proyecto (arc42, metadata)
- No son de corrección general
- Mantenidos separados por claridad

### 4.2 Archivos de Configuración

**pytest.ini** (en raíz del proyecto):
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
pythonpath = . scripts
addopts = 
    --verbose
    --cov=scripts
    --cov-report=html
    --cov-report=term
    --cov-fail-under=80
```

**mypy.ini** (en raíz del proyecto):
```ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
files = scripts/**/*.py
exclude = scripts/(actualizar_metadata|clonar_repo|corregir_nombres|distribuir_archivos).*
```

**pyproject.toml** (actualizar si existe, o crear):
```toml
[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'
extend-exclude = '''
/(
  | _build
  | build
  | dist
  | source
)/
'''

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

[tool.coverage.run]
source = ["scripts"]
omit = [
    "*/tests/*",
    "*/__init__.py",
    "scripts/actualizar_metadata*",
    "scripts/clonar_repo*"
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
]
```

**tests/conftest.py** (crear):
```python
"""Configuración compartida para pytest."""

import pytest
from pathlib import Path

@pytest.fixture
def fixtures_dir():
    """Retorna directorio de fixtures."""
    return Path(__file__).parent / 'fixtures'

@pytest.fixture
def sample_rst_file(fixtures_dir, tmp_path):
    """Crea archivo RST temporal para testing."""
    content = (fixtures_dir / 'section_structure' / 'input_incorrect.rst').read_text()
    test_file = tmp_path / 'test.rst'
    test_file.write_text(content)
    return test_file

@pytest.fixture
def expected_output(fixtures_dir):
    """Lee output esperado."""
    return (fixtures_dir / 'section_structure' / 'output_expected.rst').read_text()
```

**scripts/README.md** (actualizar sección de organización):
```markdown
# Scripts ADT

## Organización

### correction/
Scripts que MODIFICAN archivos RST para corregir errores:
- `fix_section_structure.py` - Corrige estructura de secciones
- `fix_title_underlines.py` - Corrige underlines de títulos
- `fix_heading_levels.py` - Normaliza niveles de encabezados
- `fix_indentation_errors.py` - Corrige indentación
- `resolve_image_references.py` - Resuelve referencias de imágenes
- `fix_list_spacing.py` - Corrige espaciado de listas
- etc.

### analysis/
Scripts que ANALIZAN sin modificar:
- `analyze_build_log.py` - Analiza logs de build
- `find_duplicate_labels.py` - Detecta labels duplicados
- `find_duplicate_toctree.py` - Detecta toctree duplicados

### lib/
Bibliotecas compartidas:
- `rst_utils/` - Utilidades para parseo/rendering de RST
- `regex_patterns.py` - Patrones regex compartidos

### Tests
Los tests están en `/tests/` (hermana de `/scripts/`)
- `tests/test_correction/` - Tests de scripts de corrección
- `tests/test_analysis/` - Tests de scripts de análisis
- `tests/test_lib/` - Tests de bibliotecas

## Ejecutar Tests

```bash
# Todos los tests
pytest

# Con coverage
pytest --cov=scripts --cov-report=html

# Solo tests de corrección
pytest tests/test_correction/

# Un script específico
pytest tests/test_correction/test_fix_heading_levels.py

# Con verbose
pytest -v
```
```

## 5. Interfaces y Contratos

### 5.1 Interfaz de Scripts de Corrección

Todos los scripts de corrección seguirán este contrato:

```python
# Signature estándar
def process_file(
    path: Path,
    dry_run: bool = True,
    verbose: bool = False
) -> Tuple[bool, List[str]]:
    """
    Procesa un archivo RST aplicando correcciones.
    
    Args:
        path: Ruta al archivo RST
        dry_run: Si True, solo reporta cambios sin aplicar
        verbose: Si True, output detallado
    
    Returns:
        Tuple de (success: bool, changes: List[str])
        - success: True si no hubo errores
        - changes: Lista de cambios aplicados/sugeridos
    
    Raises:
        ValueError: Si archivo no es RST válido
        IOError: Si no se puede leer/escribir archivo
    """
    ...

# CLI estándar
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path, help='File or directory to process')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default: dry-run)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()
    
    dry_run = not args.apply
    # ... process
```

**Ejemplo de uso consistente**:
```bash
# Todos los scripts usan la misma interfaz
python scripts/fix_heading_levels.py source/ --dry-run -v
python scripts/fix_section_structure.py source/01_fundamentos/ --apply
python scripts/fix_indentation_errors.py source/docs_maestros/file.rst --dry-run
```

### 5.2 Interfaz de rst_utils

**parser.py**:
```python
from typing import List
from .types import Block

def parse_rst_file(content: str) -> List[Block]:
    """Parsea contenido RST a lista de bloques estructurados."""
    ...

def parse_block(lines: List[str]) -> Block:
    """Parsea líneas a un bloque específico."""
    ...
```

**renderer.py**:
```python
from typing import List
from .types import Block

def render_blocks(blocks: List[Block]) -> str:
    """Renderiza bloques a contenido RST."""
    ...

def render_block(block: Block) -> str:
    """Renderiza un bloque individual."""
    ...
```

**analyzer.py**:
```python
from typing import List, Dict
from .types import Block, Issue

def detect_heading_levels(blocks: List[Block]) -> List[Issue]:
    """Detecta problemas en niveles de encabezados."""
    ...

def detect_title_issues(blocks: List[Block]) -> List[Issue]:
    """Detecta problemas en títulos (underlines, etc)."""
    ...
```

**types.py**:
```python
from dataclasses import dataclass
from typing import Literal, Optional

@dataclass(frozen=True)  # Inmutable
class Block:
    """Bloque genérico de contenido RST."""
    type: Literal['heading', 'paragraph', 'list', 'code', 'directive']
    content: str
    line_number: int

@dataclass(frozen=True)
class Heading(Block):
    """Bloque de encabezado."""
    type: Literal['heading'] = 'heading'
    level: int = 1
    underline_char: str = '='
    overline: bool = False

@dataclass(frozen=True)
class Issue:
    """Problema detectado."""
    file: str
    line: int
    severity: Literal['critical', 'error', 'warning']
    category: str
    message: str
    suggested_fix: Optional[str] = None
```

### 5.3 Contrato de Tests

```python
# Cada script debe tener estos tests mínimos

def test_parse_valid_input():
    """Parser maneja input válido."""
    ...

def test_parse_invalid_input():
    """Parser maneja input inválido gracefully."""
    ...

def test_fix_single_issue():
    """Corrección de un issue simple."""
    ...

def test_fix_multiple_issues():
    """Corrección de múltiples issues."""
    ...

def test_no_false_positives():
    """No corrige contenido ya correcto."""
    ...

def test_dry_run_no_side_effects():
    """Dry-run no modifica archivos."""
    ...

def test_full_pipeline_with_fixture():
    """Pipeline completo con archivo real."""
    ...
```

## 6. Dependencias

### 6.1 Dependencias de Ejecución

**Python packages** (ya instalados):
- Python 3.10+
- pathlib (stdlib)
- argparse (stdlib)
- functools (stdlib)
- itertools (stdlib)
- dataclasses (stdlib)
- typing (stdlib)
- re (stdlib) - para regex

**Dependencias externas** (verificar instalación):
- pytest >= 7.0
- pytest-cov >= 4.0
- mypy >= 1.0
- black >= 23.0

**Dependencias opcionales**:
- rich (para output coloreado en CLI)
- difflib (stdlib, para mejor diff output)

### 6.2 Dependencias entre Scripts

```
scripts/lib/rst_utils/ (biblioteca base)
    ↓
scripts/lib/regex_patterns.py (patrones compartidos)
    ↓
    ├── scripts/correction/fix_heading_levels.py
    ├── scripts/correction/fix_section_structure.py
    ├── scripts/correction/fix_title_underlines.py
    ├── scripts/correction/fix_indentation_errors.py
    ├── scripts/correction/resolve_image_references.py
    ├── scripts/correction/fix_list_spacing.py
    └── ... (otros scripts de corrección)

scripts/analysis/analyze_build_log.py (independiente)

scripts/validar_estructura.sh (independiente)
```

**Importaciones típicas**:
```python
# En scripts de corrección
from scripts.lib.rst_utils import parse_rst_file, render_blocks
from scripts.lib.rst_utils.analyzer import detect_heading_levels
from scripts.lib.regex_patterns import TITLE_WITH_UNDERLINE, INDENT_PATTERN

# En tests
import pytest
from scripts.correction.fix_heading_levels import process_file
```

### 6.3 Dependencias de Orden de Ejecución

Algunos lotes dependen de otros:

```
L1 (Section Structure) → L2 (Title Underlines)
    ↓                         ↓
    L3 (Indentation)     L6 (Heading Levels)
         ↓                    ↓
    L4-L5 (Manual)       L7-L13 (Resto)
```

**Lotes independientes** (pueden ejecutarse en paralelo si se desea):
- L7 (Missing Images)
- L8 (List Formatting)
- L10 (Duplicate Labels)
- L11 (List Tables)

### 6.4 Dependencias de Regex y Herramientas

**Bibliotecas estándar**:
```python
import re                    # Regex básico
from typing import Pattern   # Type hints para regex
import difflib              # Fuzzy matching
from enum import Enum       # State machines
```

**No se requieren**:
- ❌ spaCy (NLP pesado)
- ❌ transformers (ML innecesario)
- ❌ nltk (overkill para RST)

**Filosofía**: Usar regex y programación funcional primero. NLP/ML solo si es absolutamente necesario (probablemente no lo sea para RST).

## 7. Impacto

### 7.1 Cambios Breaking

**Ninguno**. Las correcciones son de formato, no de contenido semántico.

### 7.2 Cambios de Formato (No-Breaking)

**Archivos RST**:
- Niveles de encabezados normalizados
- Underlines de títulos ajustados
- Indentación corregida
- Listas reformateadas
- Labels duplicados renombrados

**Impacto en renderizado HTML**:
- ✅ Navegación mejorada (TOC correcto)
- ✅ Jerarquía visual correcta
- ✅ Imágenes visibles (si rutas corregidas)
- ✅ Listas y tablas bien formateadas

### 7.3 Migración

**No requiere migración** ya que:
- Scripts modifican archivos existentes in-place
- Estructura de directorios no cambia
- Nombres de archivos no cambian
- Formato final sigue siendo RST válido

### 7.4 Compatibilidad

**Sphinx 8.2.3**: ✅ Compatible (versión actual)
**Extensiones**: ✅ Compatible (sin cambios en configuración)
**Tema Furo**: ✅ Compatible (sin cambios)
**CI/CD**: ✅ Compatible (build sigue siendo `make html`)

## 8. Plan de Rollback

### 8.1 Rollback por Lote

Cada lote se comitea independientemente:

```bash
# Si L3 falla, rollback solo L3
git log --oneline | head -5
# abc123 fix(error): correct indentation errors (L3)
# def456 fix(critical): correct title underlines (L2)
# ghi789 fix(critical): correct section structure (L1)

# Rollback L3
git revert abc123

# O reset hard si no se pusheó
git reset --hard def456
```

### 8.2 Rollback Completo

Si todo falla, rollback a commit inicial:

```bash
# Tag antes de empezar
git tag -a before-build-fixes -m "Estado antes de correcciones"

# Si todo falla
git reset --hard before-build-fixes

# O revert todos los commits
git revert abc123..HEAD
```

### 8.3 Rollback de Script

Si un script daña archivos:

```bash
# 1. Identificar archivos afectados
git diff --name-only

# 2. Checkout archivos específicos
git checkout HEAD -- source/path/to/file.rst

# 3. O checkout directorio completo
git checkout HEAD -- source/
```

### 8.4 Checkpoints

Crear tags en puntos clave:

```bash
git tag -a after-critical-fixes -m "CRITICAL (33) eliminados"
git tag -a after-error-fixes -m "ERROR (72) eliminados"
git tag -a after-warning-fixes -m "WARNING críticos eliminados"
git tag -a build-fixes-complete -m "Todas las correcciones aplicadas"
```

## 9. Testing

### 9.1 Casos de Prueba por Script

#### fix_section_structure.py

**TC-001: Título de sección inesperado**
```rst
# Input:
Párrafo normal
------ 
Siguiente párrafo

# Expected:
Párrafo normal

Siguiente párrafo

# Validación: Eliminar underline incorrecto
```

**TC-002: Jerarquía de sección rota**
```rst
# Input:
Título Principal
================

Subtítulo Nivel 3
^^^^^^^^^^^^^^^^^

# Expected:
Título Principal
================

Subtítulo Nivel 2
-----------------

# Validación: Corregir nivel de underline
```

#### fix_title_underlines.py

**TC-003: Underline más corto**
```rst
# Input:
Título Largo
------

# Expected:
Título Largo
------------

# Validación: Underline coincide con longitud
```

**TC-004: Underline más largo**
```rst
# Input:
Título
----------

# Expected:
Título
------

# Validación: Underline coincide con longitud
```

#### fix_heading_levels.py

**TC-005: Header empieza en H2**
```rst
# Input:
Documento
---------

# Expected:
Documento
=========

# Validación: Primer header es H1
```

**TC-006: Salto de nivel (H1 → H3)**
```rst
# Input:
Título
======

Subtítulo
^^^^^^^^^

# Expected:
Título
======

Subtítulo
---------

# Validación: Niveles consecutivos
```

#### fix_indentation_errors.py

**TC-007: Indentación inesperada en lista**
```rst
# Input:
- Item 1
  - Item 2
    Continúa item 2

# Expected:
- Item 1
  - Item 2
    
    Continúa item 2

# Validación: Línea en blanco antes de continuar
```

#### resolve_image_references.py

**TC-008: Variable sin expandir**
```rst
# Input:
.. image:: {{site.imageurl}}/diagram.png

# Expected (opción 1):
.. image:: _static/images/diagram.png

# Expected (opción 2):
.. note:: [IMAGEN FALTANTE: diagram.png]

# Validación: Ruta válida o placeholder
```

### 9.2 Tests de Integración

**TI-001: Pipeline completo**
```python
def test_full_correction_pipeline():
    """Aplica todos los scripts en orden."""
    # 1. Estado inicial
    issues_before = count_issues('build_before.log')
    
    # 2. Aplicar correcciones
    for script in SCRIPTS_IN_ORDER:
        run_script(script, dry_run=False)
    
    # 3. Validar
    run_make_html()
    issues_after = count_issues('build_after.log')
    
    # 4. Aserciones
    assert issues_after < issues_before * 0.05  # Reducción > 95%
    assert count_critical(issues_after) == 0
    assert count_errors(issues_after) == 0
```

**TI-002: Idempotencia**
```python
def test_scripts_are_idempotent():
    """Aplicar script 2 veces produce mismo resultado."""
    content_original = read_file('test.rst')
    
    # Primera aplicación
    run_script('fix_heading_levels.py', 'test.rst')
    content_after_1 = read_file('test.rst')
    
    # Segunda aplicación
    run_script('fix_heading_levels.py', 'test.rst')
    content_after_2 = read_file('test.rst')
    
    # Debe ser idéntico
    assert content_after_1 == content_after_2
```

### 9.3 Criterios de Validación

**Validación de script individual**:
- ✅ Tests unitarios pasan (pytest)
- ✅ Coverage > 80%
- ✅ Mypy sin errores
- ✅ Black formatting OK
- ✅ Dry-run reporta cambios esperados
- ✅ Apply modifica solo archivos esperados

**Validación de lote**:
- ✅ `make html` completa con exit code 0
- ✅ Reducción neta de issues (no aumenta)
- ✅ No nuevos CRITICAL/ERROR
- ✅ Diff es reviewable y razonable

**Validación final**:
- ✅ Issues < 50 (objetivo: < 50)
- ✅ CRITICAL = 0
- ✅ ERROR = 0
- ✅ Reducción > 95%
- ✅ Build time ~25s ±10%

## 10. Referencias

### 10.1 Referencias Internas

**Requirements**:
- RF-001 → Section Title Issues (L1)
- RF-002 → Title Underline (L2)
- RF-003 → Indentation (L3)
- RF-004 → Content Block Parsing (L4)
- RF-005 → Missing Content (L5)
- RF-006 → Document Heading Levels (L6)
- RF-007 → Missing Images (L7)
- RF-008 → List Formatting (L8)
- RF-009 → Title Formatting (cubierto por L2)
- RF-010 → Duplicate Labels (L10)
- RF-011 → Evaluar scripts existentes
- RF-012 → Desarrollar scripts funcionales
- RF-013 → Generar reporte

**Decisiones**:
- DA-001 → Lotes categorizados
- DA-002 → Programación funcional
- DA-003 → Dry-run obligatorio
- DA-004 → Tests con pytest
- DA-005 → Validación continua
- DA-006 → Scripts como biblioteca
- DA-007 → Estrategia híbrida
- DA-008 → Uso de regex y herramientas avanzadas (NUEVO v1.1.0)

### 10.2 Referencias Externas

**Documentación Sphinx**:
- [RST Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [RST Directives](https://docutils.sourceforge.io/docs/ref/rst/directives.html)

**Programación Funcional Python**:
- [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [functools](https://docs.python.org/3/library/functools.html)
- [itertools](https://docs.python.org/3/library/itertools.html)

**Testing**:
- [Pytest Documentation](https://docs.pytest.org/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)

**Type Hints**:
- [Mypy Documentation](https://mypy.readthedocs.io/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)

### 10.3 Skills del Proyecto

- `.codex/skills/spec-driven-dev/SKILL.md`
- `.codex/skills/sphinx-expert/SKILL.md`
- `.codex/skills/validation-suite/SKILL.md`

## 11. Próximos Pasos

Una vez este documento de Design sea **APROBADO**:

1. ➡️ Proceder a **FASE 3: Tasks**
2. Crear archivo: `2026-01-30-XX-XX-tasks-corregir-errores-build.md`
3. Detallar tareas específicas paso a paso:
   - TASK-001 a TASK-NNN
   - Comandos exactos
   - Archivos afectados
   - Criterios de éxito
   - Checkpoints
4. **SOLICITAR APROBACIÓN** antes de FASE 4: Implementation

---

**Archivo**: `.mywork/changes/2026-01-30-corregir-errores-build-sphinx/2026-01-30-03-43-design-corregir-errores-build.md`

**Versión**: 1.1.0

**Estado**: Draft → **Esperando Aprobación del Usuario**

**Autor**: Claude (AI Assistant)

**Proyecto**: ADT Documentation v1.7.1

**Basado en**: Requirements v1.0.0

**Fecha de Creación**: 2026-01-30 03:43

**Última Actualización**: 2026-01-30 03:52

**Estimación de Complejidad**: Alta

**Estimación de Tiempo** (actualizada v1.1.0):
- Reorganización de scripts existentes: 1-2 horas
- Desarrollo de scripts nuevos (5): 6-8 horas
- Desarrollo de rst_utils + regex_patterns: 3-4 horas
- Refactorización de scripts existentes (3): 2-3 horas
- Testing (> 80% coverage): 4-5 horas
- Aplicación de correcciones: 4-6 horas
- Validación y refinamiento: 2-3 horas
- **Total estimado**: 18-25 horas (incremento por reorganización)

**Cambios en v1.1.0**:
- **Tests movidos** de `scripts/tests/` a `/tests/` (hermana de scripts/)
- **Scripts organizados** en subcarpetas lógicas:
  - `scripts/correction/` - Scripts que corrigen
  - `scripts/analysis/` - Scripts que analizan
  - `scripts/lib/` - Bibliotecas compartidas
- **Nueva DA-008**: Uso de regex y herramientas avanzadas para casos complejos
- **Nuevo componente**: `scripts/lib/regex_patterns.py` con patrones compartidos
- **Actualizada estructura** de archivos completa
- **Actualizados archivos** de configuración (pytest.ini, mypy.ini, pyproject.toml)
- **Agregado README.md** de scripts con explicación de organización
- **Clarificada filosofía**: Regex primero, NLP/ML solo si es necesario

**Riesgos Principales**:
- Scripts pueden no cubrir todos los edge cases (mitigado con tests + regex avanzado)
- Correcciones pueden introducir nuevos errores (mitigado con validación continua)
- Reorganización de scripts puede romper imports (mitigado con tests)
- Casos manuales pueden ser más de lo estimado (mitigado con estrategia híbrida)
