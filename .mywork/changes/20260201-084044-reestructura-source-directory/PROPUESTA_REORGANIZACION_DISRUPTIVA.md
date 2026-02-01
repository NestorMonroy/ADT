# Propuesta de Reorganización DISRUPTIVA - Proyecto ADT

**Fecha**: 2026-02-01  
**Versión**: 1.0.0  
**Objetivo**: Clarificar estructura para un pipeline reproducible de traducción

---

## 🎯 VISIÓN CLARA

El proyecto ADT tiene **DOS propósitos fundamentales**:

1. **Documentar CÓMO usar el pipeline** de traducción
2. **Almacenar el CONTENIDO traducido** (la biblioteca)

**TODO lo demás** debe servir a uno de estos dos propósitos.

---

## 📊 ESTADO ACTUAL (Problemático)

### Contenido Actual en `/tmp/ADT/source`

| Directorio | Archivos | Tamaño | Propósito Actual | ¿Está claro? |
|------------|----------|--------|------------------|--------------|
| `01_fundamentos` | 10 | 93K | Documentación pipeline | ✅ SÍ |
| `02_procedimientos` | 3 | 167K | Documentación pipeline | ✅ SÍ |
| `03_estandares` | 8 | 56K | Documentación pipeline | ✅ SÍ |
| `04_reglas_operativas` | 9 | 76K | Documentación pipeline | ✅ SÍ |
| `05_herramientas_medios` | 7 | 29K | Documentación pipeline | ✅ SÍ |
| `06_casos_practicos` | 7 | 52K | Documentación pipeline | ✅ SÍ |
| `07_guias_uso` | 6 | 79K | Documentación pipeline | ✅ SÍ |
| `08_prompts` | 3 | 13K | Documentación pipeline | ✅ SÍ |
| `09_referencias` | 5 | 34K | Documentación pipeline | ✅ SÍ |
| `10_apendices` | 2 | 13K | Documentación pipeline | ✅ SÍ |
| **`biblioteca`** | 650 | 25M | **Contenido traducido** | ✅ SÍ |
| **`_static`** | - | - | Utilidades Sphinx | ✅ SÍ |
| **`_templates`** | - | - | Utilidades Sphinx | ✅ SÍ |
| **`diataxis`** | 1 | 4.5K | ??? Estructura vacía | ❌ **CONFUSO** |
| **`docs`** | 3 | 23K | ??? Meta-docs | ❌ **CONFUSO** |
| **`docs_maestros`** | 15 | 326K | ??? Arquitectura | ❌ **CONFUSO** |

### 🔴 PROBLEMAS IDENTIFICADOS

1. **`diataxis/`**: Estructura planeada pero **VACÍA** (solo 1 archivo)
   - ¿Es un framework que nunca se usó?
   - ¿Debería eliminarse o poblarse?

2. **`docs/`**: 3 archivos de meta-documentación
   - INTEGRACION_FRAMEWORKS.md
   - PHANTOMJS_STATUS.md
   - index.rst
   - ¿Es documentación SOBRE el proyecto o DEL pipeline?

3. **`docs_maestros/`**: 15 archivos de arquitectura y metodología
   - ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
   - METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
   - PROMPT_MAESTRO_SPHINX_TRADUCCION.md
   - etc.
   - ¿Son documentos maestros o deberían estar en 01-10?

**Resultado**: Confusión sobre **DÓNDE poner nuevos documentos**.

---

## 💡 PROPUESTA DISRUPTIVA

### Principio Fundamental

> **Todo contenido debe tener UNA ubicación obvia e inequívoca**

### Nueva Estructura Propuesta

```
/tmp/ADT/
├── source/
│   ├── pipeline/               ← NUEVO: Documentación de cómo usar ADT
│   │   ├── 01_fundamentos/
│   │   ├── 02_procedimientos/
│   │   ├── 03_estandares/
│   │   ├── 04_reglas_operativas/
│   │   ├── 05_herramientas_medios/
│   │   ├── 06_casos_practicos/
│   │   ├── 07_guias_uso/
│   │   ├── 08_prompts/
│   │   ├── 09_referencias/
│   │   ├── 10_apendices/
│   │   └── index.rst           ← Índice del pipeline
│   │
│   ├── biblioteca/              ← Contenido traducido (SIN CAMBIOS)
│   │   ├── ciencias/
│   │   ├── informatica/
│   │   ├── ingenieria/
│   │   └── ...
│   │
│   ├── _static/                 ← Utilidades Sphinx (SIN CAMBIOS)
│   ├── _templates/              ← Utilidades Sphinx (SIN CAMBIOS)
│   │
│   └── index.rst                ← Índice RAÍZ (apunta a pipeline + biblioteca)
│
├── docs/                        ← NUEVO: Documentación DEL PROYECTO (meta)
│   ├── arquitectura/            ← Migrar docs_maestros AQUÍ
│   │   ├── ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
│   │   ├── METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
│   │   └── ...
│   ├── desarrollo/              ← Migrar docs AQUÍ
│   │   ├── INTEGRACION_FRAMEWORKS.md
│   │   ├── PHANTOMJS_STATUS.md
│   │   └── ...
│   └── README.md                ← Índice de documentación del proyecto
│
└── .codex/                      ← Skills del proyecto (YA EXISTE)
    └── skills/
```

---

## 🎯 DECISIONES CLAVE

### DECISIÓN 1: Crear `/source/pipeline/`

**Razón**:
- Clarifica que 01-10 son documentación DEL pipeline
- NO son el proyecto en sí, son CÓMO USAR el proyecto
- Diferencia clara: `source/pipeline` vs `source/biblioteca`

**Migración**:
```bash
mv source/01_fundamentos source/pipeline/01_fundamentos
mv source/02_procedimientos source/pipeline/02_procedimientos
# ... etc para 03-10
```

### DECISIÓN 2: ELIMINAR `source/diataxis/`

**Razón**:
- Estructura vacía (solo 1 archivo index.rst)
- Framework Diátaxis **YA se usa** en 01-10:
  - 01_fundamentos = Explanation
  - 02_procedimientos = How-to guides
  - 09_referencias = Reference
  - 06_casos_practicos = Tutorials
- NO necesitamos un directorio separado para esto

**Acción**:
```bash
# Archivar por si acaso
mv source/diataxis archivados/diataxis-eliminado-20260201/

# O simplemente eliminar
rm -rf source/diataxis
```

### DECISIÓN 3: Mover `source/docs/` a `/docs/desarrollo/`

**Razón**:
- `docs/` contiene documentación SOBRE el proyecto (meta)
- NO es documentación para usuarios del pipeline
- Debe estar FUERA de `source/` (no se publica con Sphinx)

**Contenido a mover**:
- INTEGRACION_FRAMEWORKS.md → `/docs/desarrollo/`
- PHANTOMJS_STATUS.md → `/docs/desarrollo/`
- index.rst → ELIMINAR (ya no necesario)

### DECISIÓN 4: Mover `source/docs_maestros/` a `/docs/arquitectura/`

**Razón**:
- Documentos maestros son META-documentación del proyecto
- Describen arquitectura, metodología, planes
- NO son para usuarios finales del pipeline
- Deben estar en `/docs/` (fuera de source/)

**Contenido a mover**:
- ARQUITECTURA_DOCUMENTAL_TRADUCCION.md → `/docs/arquitectura/`
- METODO_TRADUCCION_PESHITTA_ZACHARIAS.md → `/docs/arquitectura/`
- PROMPT_MAESTRO_SPHINX_TRADUCCION.md → `/docs/arquitectura/`
- GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst → `/docs/arquitectura/`
- PLAN_*.md → `/docs/arquitectura/` o `/docs/desarrollo/`
- PROPUESTA_*.md → `/docs/arquitectura/`
- etc.

### DECISIÓN 5: Crear `/docs/README.md`

**Razón**:
- Índice de documentación del proyecto
- Explica qué va en cada directorio
- Guía para desarrolladores/mantenedores

**Contenido**:
```markdown
# Documentación del Proyecto ADT

## Directorios

- **arquitectura/**: Decisiones arquitectónicas, metodología
- **desarrollo/**: Notas técnicas, integraciones, status

## Diferencia con source/

- `/docs/`: Documentación SOBRE el proyecto (para desarrolladores)
- `/source/`: Documentación DEL pipeline (para usuarios)
```

---

## 📋 PLAN DE MIGRACIÓN

### FASE 1: Preparación (5 min)

```bash
# 1. Crear backup completo
cd /tmp/ADT
git add -A
git commit -m "backup: antes de reorganización disruptiva"

# 2. Crear directorios nuevos
mkdir -p source/pipeline
mkdir -p docs/arquitectura
mkdir -p docs/desarrollo
mkdir -p archivados/reorganizacion-20260201
```

### FASE 2: Migrar 01-10 a pipeline/ (10 min)

```bash
cd /tmp/ADT/source

# Mover directorios numerados
for dir in 01_fundamentos 02_procedimientos 03_estandares 04_reglas_operativas 05_herramientas_medios 06_casos_practicos 07_guias_uso 08_prompts 09_referencias 10_apendices; do
    mv $dir pipeline/$dir
done

# Crear index.rst para pipeline
cat > pipeline/index.rst << 'EOF'
Pipeline de Traducción ADT
==========================

.. toctree::
   :maxdepth: 2
   
   01_fundamentos/index
   02_procedimientos/index
   03_estandares/index
   04_reglas_operativas/index
   05_herramientas_medios/index
   06_casos_practicos/index
   07_guias_uso/index
   08_prompts/index
   09_referencias/index
   10_apendices/index
EOF
```

### FASE 3: Eliminar diataxis/ (1 min)

```bash
cd /tmp/ADT/source

# Archivar diataxis
mv diataxis ../archivados/reorganizacion-20260201/diataxis-eliminado/
```

### FASE 4: Migrar docs/ y docs_maestros/ (5 min)

```bash
cd /tmp/ADT

# Mover docs/ a docs/desarrollo/
mv source/docs/INTEGRACION_FRAMEWORKS.md docs/desarrollo/
mv source/docs/PHANTOMJS_STATUS.md docs/desarrollo/
rm source/docs/index.rst  # Ya no necesario
rmdir source/docs

# Mover docs_maestros/ a docs/arquitectura/
mv source/docs_maestros/* docs/arquitectura/
rmdir source/docs_maestros
```

### FASE 5: Actualizar index.rst raíz (5 min)

```bash
cd /tmp/ADT/source

# Actualizar index.rst principal
cat > index.rst << 'EOF'
Proyecto ADT - Arquitectura Documental para Traducción
=======================================================

Bienvenido al proyecto ADT (Arquitectura Documental para Traducción).

.. toctree::
   :maxdepth: 2
   :caption: Pipeline de Traducción
   
   pipeline/index

.. toctree::
   :maxdepth: 2
   :caption: Biblioteca de Contenido Traducido
   
   biblioteca/index
EOF
```

### FASE 6: Crear docs/README.md (3 min)

```bash
cd /tmp/ADT/docs

cat > README.md << 'EOF'
# Documentación del Proyecto ADT

Este directorio contiene documentación SOBRE el proyecto ADT (meta-documentación para desarrolladores y mantenedores).

## Estructura

- **arquitectura/**: Decisiones arquitectónicas, metodología, planes maestros
- **desarrollo/**: Notas técnicas, integraciones, status de herramientas

## Diferencia con `/source/`

| Directorio | Audiencia | Propósito |
|------------|-----------|-----------|
| `/docs/` | Desarrolladores/Mantenedores | Documentación SOBRE el proyecto |
| `/source/` | Usuarios del pipeline | Documentación DEL pipeline de traducción |

EOF
```

### FASE 7: Verificar y Commit (5 min)

```bash
cd /tmp/ADT

# Verificar estructura nueva
tree -L 2 source/
tree -L 2 docs/

# Hacer build de prueba
make clean
make html

# Si todo OK, commit
git add -A
git commit -m "refactor(estructura): reorganización disruptiva source/ y docs/"
```

---

## ✅ RESULTADO ESPERADO

### Estructura DESPUÉS de la reorganización

```
/tmp/ADT/
├── source/
│   ├── pipeline/               ✅ Documentación de cómo usar ADT
│   │   ├── 01_fundamentos/
│   │   ├── 02_procedimientos/
│   │   ├── ...
│   │   └── 10_apendices/
│   ├── biblioteca/              ✅ Contenido traducido
│   ├── _static/                 ✅ Utilidades
│   ├── _templates/              ✅ Utilidades
│   └── index.rst                ✅ Índice raíz
│
├── docs/                        ✅ NUEVO: Meta-documentación
│   ├── arquitectura/            ✅ Arquitectura y metodología
│   ├── desarrollo/              ✅ Notas técnicas
│   └── README.md                ✅ Índice
│
└── .codex/skills/               ✅ Skills del proyecto
```

### Beneficios

| Beneficio | Antes | Después |
|-----------|-------|---------|
| **Claridad** | ❌ 3 directorios confusos | ✅ Estructura clara |
| **Navegación** | ❌ ¿Dónde va esto? | ✅ Ubicación obvia |
| **Separación** | ❌ Todo mezclado en source/ | ✅ source/ vs docs/ |
| **Mantenimiento** | ❌ Difícil encontrar docs | ✅ Fácil localizar |
| **Build Sphinx** | ❌ Problemas con paths | ✅ Paths claros |

---

## 🚨 ALTERNATIVA CONSERVADORA (Si prefieres)

Si la propuesta anterior es muy disruptiva, aquí una **versión conservadora**:

### Opción B: Solo mover docs_maestros y eliminar diataxis

```bash
# Mover docs_maestros a 00_arquitectura dentro de source
mkdir source/00_arquitectura
mv source/docs_maestros/* source/00_arquitectura/

# Eliminar diataxis
mv source/diataxis archivados/

# Mover docs a 00_arquitectura/desarrollo
mkdir source/00_arquitectura/desarrollo
mv source/docs/* source/00_arquitectura/desarrollo/
```

**Resultado**:
```
source/
├── 00_arquitectura/          ← Meta-docs del proyecto
│   ├── ARQUITECTURA_*.md
│   ├── METODO_*.md
│   └── desarrollo/
│       └── INTEGRACION_*.md
├── 01_fundamentos/
├── ...
└── biblioteca/
```

**Pros**: Menos cambios  
**Contras**: Sigue mezclando meta-docs con docs de usuario

---

## 🎯 RECOMENDACIÓN FINAL

**PROPUESTA PRINCIPAL** (Disruptiva):
- ✅ Separación clara: `source/pipeline/` vs `source/biblioteca/` vs `/docs/`
- ✅ Eliminar confusión de diataxis/docs/docs_maestros
- ✅ Escalable para futuro

**CUÁNDO USAR ALTERNATIVA**:
- Si tienes poco tiempo ahora
- Si quieres cambio gradual
- Si hay dependencias externas en paths actuales

---

## 📝 PRÓXIMOS PASOS

1. **Decidir**: ¿Propuesta principal o alternativa?
2. **Ejecutar**: Plan de migración paso a paso
3. **Verificar**: Build de Sphinx funciona
4. **Documentar**: Actualizar README principal con nueva estructura
5. **Crear skill**: Nuevo skill "project-structure" para documentar esto

---

**¿Quieres que ejecute la reorganización? ¿O prefieres discutir primero?**
