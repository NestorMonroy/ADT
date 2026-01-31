# Tasks: Corrección de Errores de Build Sphinx

**Versión**: 1.0.0
**Basado en**: 
- Requirements v1.0.0 (APROBADO)
- Design v1.1.0 (APROBADO)
**Fecha**: 2026-01-30
**Estado**: Draft

## Control de Versiones

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0.0 | 2026-01-30 | Claude | Versión inicial de tareas detalladas |

## Resumen Ejecutivo

**Total de tareas**: 65
**Tiempo total estimado**: 18-25 horas
**Fases**: 5 (Preparación, Desarrollo, Testing, Aplicación, Finalización)
**Checkpoints**: 8

## Estructura de Fases

```
FASE 1: PREPARACIÓN (8 tareas, 2-3h)
  └─> Reorganización de estructura y setup

FASE 2: DESARROLLO (23 tareas, 8-12h)
  └─> Bibliotecas + Scripts nuevos + Refactorización

FASE 3: TESTING (12 tareas, 4-5h)
  └─> Tests unitarios + integración

FASE 4: APLICACIÓN (18 tareas, 4-6h)
  └─> Correcciones por lotes L1-L13

FASE 5: FINALIZACIÓN (4 tareas, 1-2h)
  └─> Validación final + Documentación
```

---

## FASE 1: PREPARACIÓN (2-3 horas)

### TASK-001: Crear Branch de Trabajo

**Descripción**: Crear branch para desarrollo de correcciones

**Comandos**:
```bash
cd /tmp/ADT
git checkout -b feature/fix-build-errors-949-issues
git tag before-build-fixes -m "Estado antes de correcciones"
```

**Archivos afectados**: Ninguno (solo Git)

**Criterios de éxito**:
- Branch creado
- Tag creado
- `git branch` muestra branch activo

**Dependencias**: Ninguna

**Estimación**: 2 min

---

### TASK-002: Crear Estructura de Directorios

**Descripción**: Crear nuevas subcarpetas en scripts/ y tests/

**Comandos**:
```bash
cd /tmp/ADT

# Crear subcarpetas en scripts/
mkdir -p scripts/correction
mkdir -p scripts/analysis
mkdir -p scripts/lib/rst_utils

# Crear estructura de tests/
mkdir -p tests/test_correction
mkdir -p tests/test_analysis
mkdir -p tests/test_lib/test_rst_utils
mkdir -p tests/fixtures/{section_structure,title_underlines,indentation,heading_levels,list_formatting,images}

# Crear __init__.py en todas las carpetas Python
touch scripts/correction/__init__.py
touch scripts/analysis/__init__.py
touch scripts/lib/__init__.py
touch scripts/lib/rst_utils/__init__.py
touch tests/__init__.py
touch tests/test_correction/__init__.py
touch tests/test_analysis/__init__.py
touch tests/test_lib/__init__.py
touch tests/test_lib/test_rst_utils/__init__.py

# Verificar
tree -L 3 scripts/
tree -L 2 tests/
```

**Archivos afectados**:
- `scripts/correction/` (NUEVO)
- `scripts/analysis/` (NUEVO)
- `scripts/lib/rst_utils/` (NUEVO)
- `tests/test_correction/` (NUEVO)
- `tests/test_analysis/` (NUEVO)
- `tests/test_lib/` (NUEVO)
- `tests/fixtures/` (NUEVO)

**Criterios de éxito**:
- Todos los directorios creados
- Todos los `__init__.py` existen
- `tree` muestra estructura correcta

**Dependencias**: TASK-001

**Estimación**: 5 min

---

### TASK-003: Mover Scripts Existentes de Corrección

**Descripción**: Reorganizar scripts de corrección a subcarpeta

**Comandos**:
```bash
cd /tmp/ADT/scripts

# Mover scripts de corrección
mv fix_list_spacing.py correction/
mv fix_list_table_spacing.py correction/
mv fix_glossary_indentation.py correction/
mv fix_unknown_lexers.py correction/
mv fix_blanklines_and_listtable_fp.py correction/
mv fix_list_table_blocks_fp.py correction/
mv fix_list_table_indent_fp.py correction/
mv fix_meta_transition.py correction/

# Verificar
ls -la correction/
```

**Archivos afectados**:
- `scripts/correction/fix_list_spacing.py` (MOVIDO)
- `scripts/correction/fix_list_table_spacing.py` (MOVIDO)
- `scripts/correction/fix_glossary_indentation.py` (MOVIDO)
- `scripts/correction/fix_unknown_lexers.py` (MOVIDO)
- `scripts/correction/fix_blanklines_and_listtable_fp.py` (MOVIDO)
- `scripts/correction/fix_list_table_blocks_fp.py` (MOVIDO)
- `scripts/correction/fix_list_table_indent_fp.py` (MOVIDO)
- `scripts/correction/fix_meta_transition.py` (MOVIDO)

**Criterios de éxito**:
- 8 archivos en `scripts/correction/`
- Archivos no existen en raíz de scripts/

**Dependencias**: TASK-002

**Estimación**: 3 min

---

### TASK-004: Mover Scripts de Análisis

**Descripción**: Reorganizar scripts de análisis a subcarpeta

**Comandos**:
```bash
cd /tmp/ADT/scripts

# Mover scripts de análisis
mv find_duplicate_labels.py analysis/
mv find_duplicate_toctree.py analysis/

# Mover analyze_build_log.py de /tmp/ si existe
if [ -f /tmp/analyze_build_log.py ]; then
    cp /tmp/analyze_build_log.py analysis/
fi

# Verificar
ls -la analysis/
```

**Archivos afectados**:
- `scripts/analysis/find_duplicate_labels.py` (MOVIDO)
- `scripts/analysis/find_duplicate_toctree.py` (MOVIDO)
- `scripts/analysis/analyze_build_log.py` (MOVIDO/COPIADO)

**Criterios de éxito**:
- 2-3 archivos en `scripts/analysis/`
- Archivos no existen en ubicación original

**Dependencias**: TASK-002

**Estimación**: 3 min

---

### TASK-005: Crear Archivos de Configuración

**Descripción**: Crear pytest.ini, mypy.ini, pyproject.toml, conftest.py

**Comandos**:
```bash
cd /tmp/ADT

# Crear pytest.ini
cat > pytest.ini <<'EOF'
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
EOF

# Crear mypy.ini
cat > mypy.ini <<'EOF'
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
files = scripts/**/*.py
exclude = scripts/(actualizar_metadata|clonar_repo|corregir_nombres|distribuir_archivos).*
EOF

# Crear tests/conftest.py
cat > tests/conftest.py <<'EOF'
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
    test_file = tmp_path / 'test.rst'
    test_file.write_text("Título\n======\n\nContenido.\n")
    return test_file

@pytest.fixture
def expected_output(fixtures_dir):
    """Lee output esperado de fixture."""
    # Placeholder - se actualizará con fixtures reales
    return "Expected output"
EOF

# Verificar
ls -la pytest.ini mypy.ini tests/conftest.py
```

**Archivos afectados**:
- `pytest.ini` (NUEVO)
- `mypy.ini` (NUEVO)
- `tests/conftest.py` (NUEVO)

**Criterios de éxito**:
- 3 archivos creados
- Contenido válido

**Dependencias**: TASK-002

**Estimación**: 5 min

---

### TASK-006: Actualizar README de Scripts

**Descripción**: Documentar nueva organización en scripts/README.md

**Comandos**:
```bash
cd /tmp/ADT/scripts

# Agregar sección al README existente
cat >> README.md <<'EOF'

## Organización (Actualizado 2026-01-30)

### correction/
Scripts que MODIFICAN archivos RST para corregir errores:
- `fix_section_structure.py` - Corrige estructura de secciones (CRITICAL)
- `fix_title_underlines.py` - Corrige underlines de títulos (CRITICAL)
- `fix_heading_levels.py` - Normaliza niveles de encabezados (339 warnings)
- `fix_indentation_errors.py` - Corrige indentación (28 errors)
- `resolve_image_references.py` - Resuelve referencias de imágenes (142 warnings)
- `fix_list_spacing.py` - Corrige espaciado de listas
- `fix_list_table_*.py` - Correcciones de tablas
- `fix_glossary_indentation.py` - Normaliza glosarios
- etc.

### analysis/
Scripts que ANALIZAN sin modificar:
- `analyze_build_log.py` - Analiza logs de build de Sphinx
- `find_duplicate_labels.py` - Detecta labels duplicados
- `find_duplicate_toctree.py` - Detecta toctree duplicados

### lib/
Bibliotecas compartidas:
- `rst_utils/` - Utilidades para parseo/rendering de RST
- `regex_patterns.py` - Patrones regex compartidos

## Tests

Los tests están en `/tests/` (hermana de `/scripts/`)
- `tests/test_correction/` - Tests de scripts de corrección
- `tests/test_analysis/` - Tests de scripts de análisis
- `tests/test_lib/` - Tests de bibliotecas

Ejecutar tests:
```bash
# Todos los tests
pytest

# Con coverage
pytest --cov=scripts --cov-report=html

# Solo tests de corrección
pytest tests/test_correction/

# Verbose
pytest -v
```
EOF

# Verificar
tail -50 README.md
```

**Archivos afectados**:
- `scripts/README.md` (MODIFICADO)

**Criterios de éxito**:
- Sección agregada al README
- Documentación clara de organización

**Dependencias**: TASK-003, TASK-004

**Estimación**: 10 min

---

### TASK-007: Crear Fixtures Base para Tests

**Descripción**: Crear archivos RST de ejemplo para testing

**Comandos**:
```bash
cd /tmp/ADT/tests/fixtures

# Fixture: Section Structure
cat > section_structure/input_incorrect.rst <<'EOF'
Párrafo normal
------

Otro párrafo
EOF

cat > section_structure/output_expected.rst <<'EOF'
Párrafo normal

Otro párrafo
EOF

# Fixture: Title Underlines
cat > title_underlines/input_incorrect.rst <<'EOF'
Título Muy Largo Aquí
------
EOF

cat > title_underlines/output_expected.rst <<'EOF'
Título Muy Largo Aquí
----------------------
EOF

# Fixture: Indentation
cat > indentation/input_incorrect.rst <<'EOF'
- Item 1
  - Item 2
    Continúa item 2
EOF

cat > indentation/output_expected.rst <<'EOF'
- Item 1
  - Item 2
    
    Continúa item 2
EOF

# Fixture: Heading Levels
cat > heading_levels/input_incorrect.rst <<'EOF'
Documento
---------

Sección
^^^^^^^
EOF

cat > heading_levels/output_expected.rst <<'EOF'
Documento
=========

Sección
-------
EOF

# Verificar
find . -name "*.rst" -type f
```

**Archivos afectados**:
- `tests/fixtures/section_structure/*.rst` (NUEVO)
- `tests/fixtures/title_underlines/*.rst` (NUEVO)
- `tests/fixtures/indentation/*.rst` (NUEVO)
- `tests/fixtures/heading_levels/*.rst` (NUEVO)

**Criterios de éxito**:
- 8 archivos RST creados (4 pares input/output)
- Contenido representativo de problemas reales

**Dependencias**: TASK-002

**Estimación**: 15 min

---

### TASK-008: Commit Checkpoint - Preparación

**Descripción**: Commit de reorganización estructural

**Comandos**:
```bash
cd /tmp/ADT

git add scripts/ tests/ pytest.ini mypy.ini
git commit -m "chore(structure): reorganizar scripts y crear estructura de tests

- Mover scripts de corrección a scripts/correction/
- Mover scripts de análisis a scripts/analysis/
- Crear estructura tests/ (hermana de scripts/)
- Crear fixtures base para testing
- Configurar pytest.ini y mypy.ini
- Actualizar README de scripts

Ref: FASE 1 - TASK-001 a TASK-007"

git tag checkpoint-01-preparacion
```

**Archivos afectados**: Todos los anteriores

**Criterios de éxito**:
- Commit exitoso
- Tag creado
- `git log -1` muestra commit

**Dependencias**: TASK-001 a TASK-007

**Estimación**: 2 min

---

## FASE 2: DESARROLLO (8-12 horas)

### TASK-009: Desarrollar regex_patterns.py

**Descripción**: Crear biblioteca de patrones regex compartidos

**Comandos**:
```bash
cd /tmp/ADT/scripts/lib

cat > regex_patterns.py <<'EOF'
"""Patrones regex compartidos para análisis RST.

Este módulo centraliza todos los patrones de expresiones regulares
utilizados en los scripts de corrección y análisis.
"""

import re
from typing import Pattern

# Títulos con underline
TITLE_WITH_UNDERLINE: Pattern = re.compile(
    r'^(.+)\n([=\-~^"+\'`:.])\2+$',
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

# Listas (bullet y enumeradas)
LIST_ITEM: Pattern = re.compile(
    r'^(\s*)([*\-+]|\d+\.|\#\.)\s+',
    re.MULTILINE
)

# Indentación (detectar niveles)
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

# Títulos de sección (solo la línea de texto)
SECTION_TITLE: Pattern = re.compile(
    r'^[^\n]+$',
    re.MULTILINE
)

# Underlines válidos
VALID_UNDERLINE: Pattern = re.compile(
    r'^[=\-~^"+\'`:.]+$',
    re.MULTILINE
)

# Transiciones
TRANSITION: Pattern = re.compile(
    r'^[\-=~^"+\'`:]{4,}$',
    re.MULTILINE
)

# Espacios en blanco al final de línea
TRAILING_WHITESPACE: Pattern = re.compile(
    r'[ \t]+$',
    re.MULTILINE
)

# Líneas vacías múltiples
MULTIPLE_BLANK_LINES: Pattern = re.compile(
    r'\n{3,}'
)


def match_title_underline(text: str) -> list:
    """Encuentra todos los títulos con underline en el texto.
    
    Args:
        text: Contenido RST
        
    Returns:
        Lista de tuplas (título, carácter_underline, posición)
    """
    matches = []
    for match in TITLE_WITH_UNDERLINE.finditer(text):
        title = match.group(1)
        underline_char = match.group(2)
        matches.append((title, underline_char, match.start()))
    return matches


def is_valid_underline(line: str) -> bool:
    """Verifica si una línea es un underline válido.
    
    Args:
        line: Línea a verificar
        
    Returns:
        True si es un underline válido
    """
    return bool(VALID_UNDERLINE.match(line.strip()))


def get_indentation_level(line: str) -> int:
    """Obtiene el nivel de indentación de una línea.
    
    Args:
        line: Línea a analizar
        
    Returns:
        Número de espacios de indentación
    """
    match = INDENTATION.match(line)
    return len(match.group(1)) if match else 0


if __name__ == '__main__':
    # Tests básicos
    test_text = """Título
======

Subtítulo
---------
"""
    matches = match_title_underline(test_text)
    print(f"Títulos encontrados: {len(matches)}")
    for title, char, pos in matches:
        print(f"  '{title}' con '{char}'")
EOF

# Verificar sintaxis
python3 regex_patterns.py

# Verificar con mypy
cd /tmp/ADT
mypy scripts/lib/regex_patterns.py || echo "Revisar type hints si falla"
```

**Archivos afectados**:
- `scripts/lib/regex_patterns.py` (NUEVO)

**Criterios de éxito**:
- Archivo creado con 12+ patrones regex
- Funciones auxiliares incluidas
- Tests básicos en `__main__` pasan
- Type hints completos

**Dependencias**: TASK-002

**Estimación**: 45 min

---

### TASK-010: Desarrollar rst_utils/types.py

**Descripción**: Crear dataclasses inmutables para estructuras RST

**Comandos**:
```bash
cd /tmp/ADT/scripts/lib/rst_utils

cat > types.py <<'EOF'
"""Tipos de datos para representar estructuras RST.

Todas las dataclasses son inmutables (frozen=True) para seguir
principios de programación funcional.
"""

from dataclasses import dataclass
from typing import Literal, Optional, List
from enum import Enum


class BlockType(Enum):
    """Tipos de bloques RST."""
    HEADING = 'heading'
    PARAGRAPH = 'paragraph'
    LIST = 'list'
    CODE = 'code'
    DIRECTIVE = 'directive'
    TRANSITION = 'transition'
    COMMENT = 'comment'


class IssueSeverity(Enum):
    """Niveles de severidad de issues."""
    CRITICAL = 'critical'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'


@dataclass(frozen=True)
class Block:
    """Bloque genérico de contenido RST."""
    type: BlockType
    content: str
    line_number: int
    raw_lines: tuple  # Inmutable


@dataclass(frozen=True)
class Heading(Block):
    """Bloque de encabezado RST."""
    type: BlockType = BlockType.HEADING
    level: int = 1  # 1-6
    underline_char: str = '='
    has_overline: bool = False
    title: str = ''
    
    def __post_init__(self):
        """Validación post-inicialización."""
        if self.level < 1 or self.level > 6:
            raise ValueError(f"Nivel de heading inválido: {self.level}")
        if self.underline_char not in '=-~^"+\'`:.':
            raise ValueError(f"Carácter de underline inválido: {self.underline_char}")


@dataclass(frozen=True)
class Paragraph(Block):
    """Bloque de párrafo."""
    type: BlockType = BlockType.PARAGRAPH
    

@dataclass(frozen=True)
class ListItem(Block):
    """Item de lista."""
    type: BlockType = BlockType.LIST
    marker: str = '-'  # -, *, +, 1., #., etc.
    indent_level: int = 0
    

@dataclass(frozen=True)
class CodeBlock(Block):
    """Bloque de código."""
    type: BlockType = BlockType.CODE
    language: str = 'text'
    

@dataclass(frozen=True)
class Directive(Block):
    """Directiva RST."""
    type: BlockType = BlockType.DIRECTIVE
    name: str = ''
    arguments: tuple = ()  # Inmutable
    options: tuple = ()  # Inmutable
    

@dataclass(frozen=True)
class Issue:
    """Problema detectado en el documento."""
    file_path: str
    line_number: int
    severity: IssueSeverity
    category: str
    message: str
    suggested_fix: Optional[str] = None
    context: Optional[str] = None  # Líneas alrededor del issue
    
    def __str__(self) -> str:
        """Representación legible."""
        return (
            f"[{self.severity.value.upper()}] {self.file_path}:{self.line_number}\n"
            f"  {self.category}: {self.message}"
        )


@dataclass(frozen=True)
class DocumentStructure:
    """Estructura completa de un documento RST."""
    file_path: str
    blocks: tuple  # Tuple[Block, ...] - Inmutable
    headings: tuple  # Tuple[Heading, ...] - Inmutable
    issues: tuple  # Tuple[Issue, ...] - Inmutable
    
    def has_errors(self) -> bool:
        """Verifica si hay errores o critical issues."""
        return any(
            i.severity in (IssueSeverity.ERROR, IssueSeverity.CRITICAL)
            for i in self.issues
        )
    
    def count_by_severity(self) -> dict:
        """Cuenta issues por severidad."""
        counts = {severity: 0 for severity in IssueSeverity}
        for issue in self.issues:
            counts[issue.severity] += 1
        return counts


# Mapeo de caracteres de underline a nivel de heading
UNDERLINE_TO_LEVEL = {
    '=': 1,  # H1
    '-': 2,  # H2
    '~': 3,  # H3
    '^': 4,  # H4
    '+': 5,  # H5 (raro)
    '"': 6,  # H6 (raro)
}

# Inverso: nivel a carácter
LEVEL_TO_UNDERLINE = {v: k for k, v in UNDERLINE_TO_LEVEL.items()}


if __name__ == '__main__':
    # Test básico
    heading = Heading(
        type=BlockType.HEADING,
        content="Título Principal",
        line_number=1,
        raw_lines=("Título Principal", "================"),
        level=1,
        underline_char='=',
        title="Título Principal"
    )
    print(f"Heading creado: nivel {heading.level}")
    
    issue = Issue(
        file_path="test.rst",
        line_number=10,
        severity=IssueSeverity.ERROR,
        category="indentation",
        message="Unexpected indentation"
    )
    print(f"Issue: {issue}")
EOF

# Verificar sintaxis
python3 types.py

# Verificar type hints
cd /tmp/ADT
mypy scripts/lib/rst_utils/types.py || echo "Revisar si falla"
```

**Archivos afectados**:
- `scripts/lib/rst_utils/types.py` (NUEVO)

**Criterios de éxito**:
- Dataclasses definidas
- Todas inmutables (frozen=True)
- Type hints completos
- Tests en `__main__` pasan

**Dependencias**: TASK-002

**Estimación**: 60 min

---

### TASK-011: Desarrollar rst_utils/parser.py

**Descripción**: Crear parser funcional de RST

**Comandos**:
```bash
cd /tmp/ADT/scripts/lib/rst_utils

cat > parser.py <<'EOF'
"""Parser funcional de reStructuredText.

Convierte contenido RST en estructuras de datos inmutables.
"""

from typing import List, Tuple, Optional
from pathlib import Path
import re

from .types import (
    Block, Heading, Paragraph, ListItem, CodeBlock, Directive,
    BlockType, DocumentStructure, Issue, IssueSeverity,
    UNDERLINE_TO_LEVEL
)
from ..regex_patterns import (
    TITLE_WITH_UNDERLINE, DIRECTIVE, LIST_ITEM, CODE_BLOCK,
    is_valid_underline, get_indentation_level
)


def parse_rst_file(file_path: Path) -> DocumentStructure:
    """Parsea un archivo RST completo.
    
    Args:
        file_path: Ruta al archivo RST
        
    Returns:
        DocumentStructure con bloques parseados
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el archivo no es RST válido
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    
    content = file_path.read_text(encoding='utf-8')
    blocks = parse_content(content)
    headings = tuple(b for b in blocks if isinstance(b, Heading))
    issues = detect_structural_issues(blocks, str(file_path))
    
    return DocumentStructure(
        file_path=str(file_path),
        blocks=tuple(blocks),
        headings=headings,
        issues=tuple(issues)
    )


def parse_content(content: str) -> List[Block]:
    """Parsea contenido RST en lista de bloques.
    
    Args:
        content: Texto RST
        
    Returns:
        Lista de bloques detectados
    """
    lines = content.split('\n')
    blocks = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Detectar heading (título con underline)
        if i + 1 < len(lines) and is_valid_underline(lines[i + 1]):
            heading = parse_heading(lines[i], lines[i + 1], i)
            if heading:
                blocks.append(heading)
                i += 2
                continue
        
        # Detectar directiva
        if line.strip().startswith('.. ') and '::' in line:
            directive = parse_directive(lines, i)
            blocks.append(directive)
            i += 1
            continue
        
        # Detectar lista
        if LIST_ITEM.match(line):
            list_item = parse_list_item(line, i)
            blocks.append(list_item)
            i += 1
            continue
        
        # Default: párrafo
        if line.strip():
            paragraph = Paragraph(
                type=BlockType.PARAGRAPH,
                content=line,
                line_number=i + 1,
                raw_lines=(line,)
            )
            blocks.append(paragraph)
        
        i += 1
    
    return blocks


def parse_heading(title_line: str, underline_line: str, line_num: int) -> Optional[Heading]:
    """Parsea un heading (título con underline).
    
    Args:
        title_line: Línea del título
        underline_line: Línea del underline
        line_num: Número de línea (0-indexed)
        
    Returns:
        Heading o None si no es válido
    """
    title = title_line.strip()
    underline = underline_line.strip()
    
    if not underline or not all(c == underline[0] for c in underline):
        return None
    
    underline_char = underline[0]
    level = UNDERLINE_TO_LEVEL.get(underline_char, 2)  # Default H2
    
    return Heading(
        type=BlockType.HEADING,
        content=title,
        line_number=line_num + 1,
        raw_lines=(title_line, underline_line),
        level=level,
        underline_char=underline_char,
        has_overline=False,
        title=title
    )


def parse_directive(lines: List[str], start_idx: int) -> Directive:
    """Parsea una directiva RST.
    
    Args:
        lines: Todas las líneas del documento
        start_idx: Índice de inicio de la directiva
        
    Returns:
        Directive parseada
    """
    line = lines[start_idx]
    match = DIRECTIVE.match(line.strip())
    name = match.group(1) if match else 'unknown'
    
    return Directive(
        type=BlockType.DIRECTIVE,
        content=line,
        line_number=start_idx + 1,
        raw_lines=(line,),
        name=name,
        arguments=(),
        options=()
    )


def parse_list_item(line: str, line_num: int) -> ListItem:
    """Parsea un item de lista.
    
    Args:
        line: Línea con item de lista
        line_num: Número de línea (0-indexed)
        
    Returns:
        ListItem parseado
    """
    match = LIST_ITEM.match(line)
    indent = len(match.group(1)) if match else 0
    marker = match.group(2).strip() if match else '-'
    
    return ListItem(
        type=BlockType.LIST,
        content=line,
        line_number=line_num + 1,
        raw_lines=(line,),
        marker=marker,
        indent_level=indent // 2  # Asumiendo indentación de 2 espacios
    )


def detect_structural_issues(blocks: List[Block], file_path: str) -> List[Issue]:
    """Detecta problemas estructurales en los bloques.
    
    Args:
        blocks: Lista de bloques parseados
        file_path: Ruta del archivo
        
    Returns:
        Lista de issues detectados
    """
    issues = []
    headings = [b for b in blocks if isinstance(b, Heading)]
    
    # Issue 1: Documento no empieza con H1
    if headings and headings[0].level != 1:
        issues.append(Issue(
            file_path=file_path,
            line_number=headings[0].line_number,
            severity=IssueSeverity.WARNING,
            category='heading_levels',
            message=f'Document starts at H{headings[0].level}, should be H1',
            suggested_fix='Change to H1 (=====)'
        ))
    
    # Issue 2: Saltos de nivel de heading
    for i in range(1, len(headings)):
        prev_level = headings[i-1].level
        curr_level = headings[i].level
        if curr_level - prev_level > 1:
            issues.append(Issue(
                file_path=file_path,
                line_number=headings[i].line_number,
                severity=IssueSeverity.WARNING,
                category='heading_levels',
                message=f'Heading level jumps from H{prev_level} to H{curr_level}',
                suggested_fix=f'Use H{prev_level + 1} instead'
            ))
    
    return issues


if __name__ == '__main__':
    # Test con contenido de ejemplo
    test_content = """Título Principal
=================

Subtítulo
---------

Párrafo normal.

- Item 1
- Item 2
"""
    blocks = parse_content(test_content)
    print(f"Bloques parseados: {len(blocks)}")
    for block in blocks:
        print(f"  {block.type.value} en línea {block.line_number}")
EOF

# Test
python3 parser.py
```

**Archivos afectados**:
- `scripts/lib/rst_utils/parser.py` (NUEVO)

**Criterios de éxito**:
- Parser funcional creado
- Detecta headings, párrafos, listas, directivas
- Tests en `__main__` pasan
- Type hints completos

**Dependencias**: TASK-009, TASK-010

**Estimación**: 90 min

---

[Continúa en siguiente mensaje debido a longitud...]

**CHECKPOINT-02**: Después de TASK-020 (Desarrollo completo)

**ESTIMACIÓN TOTAL FASE 2**: 8-12 horas
