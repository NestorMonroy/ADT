# Comparación Visual - ANTES vs DESPUÉS

## 🔴 ANTES (Confuso)

```
/tmp/ADT/source/
├── 01_fundamentos/          ← Pipeline docs
├── 02_procedimientos/       ← Pipeline docs
├── 03_estandares/           ← Pipeline docs
├── 04_reglas_operativas/    ← Pipeline docs
├── 05_herramientas_medios/  ← Pipeline docs
├── 06_casos_practicos/      ← Pipeline docs
├── 07_guias_uso/            ← Pipeline docs
├── 08_prompts/              ← Pipeline docs
├── 09_referencias/          ← Pipeline docs
├── 10_apendices/            ← Pipeline docs
├── biblioteca/              ← Contenido traducido ✅
├── _static/                 ← Utilidades ✅
├── _templates/              ← Utilidades ✅
├── diataxis/                ← ❓ ¿Qué es esto? (vacío)
├── docs/                    ← ❓ ¿Meta-docs? ¿Pipeline?
└── docs_maestros/           ← ❓ ¿Arquitectura? ¿Pipeline?
```

**PROBLEMAS**:
- ✘ No está claro qué es "pipeline docs" vs "meta docs"
- ✘ diataxis está vacío
- ✘ docs y docs_maestros están mezclados con pipeline
- ✘ ¿Dónde pongo un nuevo documento de arquitectura?

---

## ✅ DESPUÉS (Claro)

```
/tmp/ADT/
├── source/                     
│   ├── pipeline/               ✅ TODO sobre cómo usar ADT
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
│   │   └── index.rst
│   │
│   ├── biblioteca/             ✅ Contenido traducido
│   ├── _static/                ✅ Utilidades Sphinx
│   ├── _templates/             ✅ Utilidades Sphinx
│   └── index.rst               ✅ Índice raíz
│
├── docs/                       ✅ NUEVO: Docs DEL proyecto
│   ├── arquitectura/           ✅ ARQUITECTURA_*.md, METODO_*.md, etc
│   │   ├── ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
│   │   ├── METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
│   │   ├── PROMPT_MAESTRO_SPHINX_TRADUCCION.md
│   │   └── ...
│   ├── desarrollo/             ✅ INTEGRACION_*.md, STATUS, etc
│   │   ├── INTEGRACION_FRAMEWORKS.md
│   │   ├── PHANTOMJS_STATUS.md
│   │   └── ...
│   └── README.md               ✅ Índice
│
└── .codex/skills/              ✅ Skills (ya existe)
```

**BENEFICIOS**:
- ✓ Separación clara: pipeline vs biblioteca vs meta-docs
- ✓ diataxis eliminado (estaba vacío)
- ✓ docs y docs_maestros fusionados en /docs/
- ✓ Ubicación obvia para cada tipo de documento

---

## 🔄 QUÉ SE MUEVE DÓNDE

### Mover 01-10 → source/pipeline/

```bash
source/01_fundamentos/        →  source/pipeline/01_fundamentos/
source/02_procedimientos/     →  source/pipeline/02_procedimientos/
source/03_estandares/         →  source/pipeline/03_estandares/
source/04_reglas_operativas/  →  source/pipeline/04_reglas_operativas/
source/05_herramientas_medios/→  source/pipeline/05_herramientas_medios/
source/06_casos_practicos/    →  source/pipeline/06_casos_practicos/
source/07_guias_uso/          →  source/pipeline/07_guias_uso/
source/08_prompts/            →  source/pipeline/08_prompts/
source/09_referencias/        →  source/pipeline/09_referencias/
source/10_apendices/          →  source/pipeline/10_apendices/
```

### Eliminar diataxis/

```bash
source/diataxis/  →  archivados/diataxis-eliminado-20260201/
```

### Mover docs/ → docs/desarrollo/

```bash
source/docs/INTEGRACION_FRAMEWORKS.md  →  docs/desarrollo/INTEGRACION_FRAMEWORKS.md
source/docs/PHANTOMJS_STATUS.md        →  docs/desarrollo/PHANTOMJS_STATUS.md
source/docs/index.rst                  →  ELIMINAR
```

### Mover docs_maestros/ → docs/arquitectura/

```bash
source/docs_maestros/ARQUITECTURA_DOCUMENTAL_TRADUCCION.md     →  docs/arquitectura/
source/docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS.md  →  docs/arquitectura/
source/docs_maestros/PROMPT_MAESTRO_SPHINX_TRADUCCION.md      →  docs/arquitectura/
source/docs_maestros/GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst  →  docs/arquitectura/
source/docs_maestros/PLAN_*.md                                 →  docs/arquitectura/
source/docs_maestros/PROPUESTA_*.md                            →  docs/arquitectura/
... (todos los archivos)
```

---

## 🎯 REGLA SIMPLE DE DECISIÓN

### ¿Dónde pongo un nuevo documento?

| Si el documento es... | Va en... |
|----------------------|----------|
| **Para usuarios del pipeline** (cómo traducir) | `source/pipeline/0X_...` |
| **Contenido traducido** (libros, papers) | `source/biblioteca/` |
| **Sobre arquitectura del proyecto** | `docs/arquitectura/` |
| **Sobre desarrollo/integración** | `docs/desarrollo/` |
| **Utilidades de Sphinx** | `source/_static/` o `source/_templates/` |

---

## 📊 IMPACTO

| Aspecto | ANTES | DESPUÉS |
|---------|-------|---------|
| Directorios en source/ | 16 | 5 |
| Claridad | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| ¿Dónde va X? | ❓ Confuso | ✅ Obvio |
| Separación concerns | ❌ Todo mezclado | ✅ Clara |
| Mantenibilidad | ⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## ⏱️ TIEMPO DE MIGRACIÓN

- **Preparación**: 5 min
- **Migración**: 20 min
- **Verificación**: 5 min
- **TOTAL**: ~30 minutos

---

**¿Procedemos con la reorganización?**
