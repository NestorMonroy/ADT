# Plan de Ejecución - Reorganización Biblioteca Pública

**Fecha**: 2026-02-01  
**Tiempo estimado**: 20 minutos  
**Correcciones aplicadas**:
- Nombre: `pipeline_docs/` (underscore, NO guión)
- `/tmp/ADT/archivados` ya existe (no crear)

---

## 🎯 OBJETIVO

**Separar público de privado**:
- `source/` → Solo `biblioteca/` (se publica)
- `pipeline_docs/` → 01-10 + docs_maestros (privado)
- `archivados/` → diataxis + docs (obsoletos)

---

## 📋 PASOS

### FASE 0: Backup Git (CRÍTICO - 1 min)

```bash
cd /tmp/ADT
git add -A
git commit -m "backup: antes de reorganización biblioteca pública"
git tag backup-antes-reorganizacion-20260201
```

---

### FASE 1: Crear Estructura (1 min)

```bash
cd /tmp/ADT

# Crear directorios para docs privadas
mkdir -p pipeline_docs/metodologia
mkdir -p pipeline_docs/procedimientos

# Crear subdirectorios en archivados (ya existe la raíz)
mkdir -p archivados/20260201-diataxis
mkdir -p archivados/20260201-docs
```

---

### FASE 2: Mover 01-10 a pipeline_docs/ (5 min)

```bash
cd /tmp/ADT/source

# Mover directorios numerados a pipeline_docs/procedimientos/
for dir in 01_fundamentos 02_procedimientos 03_estandares 04_reglas_operativas 05_herramientas_medios 06_casos_practicos 07_guias_uso 08_prompts 09_referencias 10_apendices; do
    echo "Moviendo $dir..."
    mv "$dir" ../pipeline_docs/procedimientos/
done

echo "✅ 01-10 movidos a pipeline_docs/procedimientos/"
```

---

### FASE 3: Mover docs_maestros a pipeline_docs/ (2 min)

```bash
cd /tmp/ADT/source

# Mover contenido de docs_maestros a pipeline_docs/metodologia/
echo "Moviendo docs_maestros..."
mv docs_maestros/* ../pipeline_docs/metodologia/
rmdir docs_maestros

echo "✅ docs_maestros movido a pipeline_docs/metodologia/"
```

---

### FASE 4: Archivar diataxis y docs (2 min)

```bash
cd /tmp/ADT/source

# Archivar diataxis (vacío)
echo "Archivando diataxis..."
mv diataxis ../archivados/20260201-diataxis/

# Archivar docs (obsoleto)
echo "Archivando docs..."
mv docs ../archivados/20260201-docs/

echo "✅ diataxis y docs archivados"
```

---

### FASE 5: Actualizar source/index.rst (3 min)

```bash
cd /tmp/ADT/source

# Backup del index.rst actual
cp index.rst index.rst.backup

# Crear NUEVO index.rst - SOLO biblioteca
cat > index.rst << 'EOFINDEX'
Biblioteca Digital ADT
======================

Bienvenido a la Biblioteca Digital del proyecto ADT.

Colección de contenido traducido organizado por disciplina.

.. toctree::
   :maxdepth: 2
   :caption: Biblioteca
   
   biblioteca/index

Índices y tablas
================

* :ref:`genindex`
* :ref:`search`
EOFINDEX

echo "✅ source/index.rst actualizado (solo biblioteca)"
```

---

### FASE 6: Crear README.md en pipeline_docs/ (2 min)

```bash
cd /tmp/ADT/pipeline_docs

cat > README.md << 'EOFREADME'
# Pipeline de Traducción ADT - Documentación Interna

**AUDIENCIA**: Equipo de traducción (PRIVADO, no se publica con Sphinx)

---

## 📁 Estructura

### procedimientos/
Guías operativas del pipeline (01-10):
- 01_fundamentos/
- 02_procedimientos/
- 03_estandares/
- 04_reglas_operativas/
- 05_herramientas_medios/
- 06_casos_practicos/
- 07_guias_uso/
- 08_prompts/
- 09_referencias/
- 10_apendices/

### metodologia/
Arquitectura y métodos maestros:
- ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
- METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
- PROMPT_MAESTRO_SPHINX_TRADUCCION.md
- Etc.

---

## 🔒 Privacidad

**Este directorio NO se publica con Sphinx.**

Solo para uso interno del equipo de traducción.

---

## 📊 Diferencia con source/

| Directorio | Contenido | Audiencia | Se Publica |
|------------|-----------|-----------|------------|
| `source/biblioteca/` | Contenido traducido | Usuarios públicos | ✅ SÍ |
| `pipeline_docs/` | Cómo traducimos | Equipo interno | ❌ NO |
| `archivados/` | Obsoletos | Nadie | ❌ NO |

---

**Nota**: Si necesitas acceder a estos documentos, están aquí y en git.
EOFREADME

echo "✅ pipeline_docs/README.md creado"
```

---

### FASE 7: Verificar Estructura (1 min)

```bash
cd /tmp/ADT

echo "=== VERIFICACIÓN ESTRUCTURA ==="
echo ""

echo "✅ source/ (solo biblioteca):"
ls -1 source/ | grep -v "^_" | grep -v ".rst"
echo ""

echo "✅ pipeline_docs/procedimientos/:"
ls -1 pipeline_docs/procedimientos/ | head -5
echo "..."
echo ""

echo "✅ pipeline_docs/metodologia/:"
ls -1 pipeline_docs/metodologia/ | head -5
echo "..."
echo ""

echo "✅ archivados/:"
ls -1 archivados/
```

---

### FASE 8: Build Sphinx de Prueba (3 min)

```bash
cd /tmp/ADT

echo "Limpiando build anterior..."
make clean

echo "Generando HTML (solo debería compilar biblioteca)..."
make html

echo ""
echo "=== VERIFICACIÓN BUILD ==="
echo ""

# Verificar que SOLO se publicó biblioteca
echo "Contenido publicado en build/html/:"
ls -1 build/html/ | grep -v "^_" | grep -v ".html" | grep -v ".js"

echo ""
echo "✅ Si solo ves 'biblioteca' o 'biblioteca/' → CORRECTO"
echo "❌ Si ves 01_fundamentos, etc. → ALGO FALLÓ"
```

---

### FASE 9: Commit (2 min)

```bash
cd /tmp/ADT

echo "Añadiendo cambios a git..."
git add -A

echo "Creando commit..."
git commit -m "refactor(estructura): separar biblioteca pública de pipeline privado

CAMBIOS:
- source/ ahora solo contiene biblioteca/ (contenido público)
- Creado pipeline_docs/ con docs internas (01-10, docs_maestros)
- Archivados diataxis/ y docs/ (obsoletos)
- Actualizado source/index.rst (solo apunta a biblioteca)
- Build Sphinx ahora publica SOLO biblioteca

ESTRUCTURA:
- source/biblioteca/          → Contenido público (SE PUBLICA)
- pipeline_docs/procedimientos/ → 01-10 (privado)
- pipeline_docs/metodologia/    → docs_maestros (privado)
- archivados/                 → diataxis + docs

BREAKING CHANGE: Estructura completamente reorganizada
Build Sphinx ahora genera solo biblioteca, no pipeline"

echo ""
echo "✅ REORGANIZACIÓN COMPLETADA"
```

---

## ✅ RESULTADO ESPERADO

### Estructura DESPUÉS

```
/tmp/ADT/
├── source/
│   ├── biblioteca/           ✅ ÚNICO contenido público
│   ├── _static/
│   ├── _templates/
│   └── index.rst             ✅ Apunta solo a biblioteca
│
├── pipeline_docs/            ✅ NUEVO: Docs privadas
│   ├── procedimientos/       ✅ 01-10 movidos aquí
│   ├── metodologia/          ✅ docs_maestros movidos aquí
│   └── README.md
│
├── archivados/
│   ├── 20260201-diataxis/    ✅ Archivado
│   └── 20260201-docs/        ✅ Archivado
│
└── build/html/
    └── biblioteca/           ✅ Solo esto se publica
```

### Build Sphinx

**Antes**: 16 secciones publicadas (biblioteca + 01-10 + docs_maestros + ...)

**Después**: 1 sección publicada (solo biblioteca)

---

## 🚨 VALIDACIÓN POST-EJECUCIÓN

### Check 1: Estructura correcta

```bash
# Debe mostrar SOLO: biblioteca, _static, _templates
ls -1 source/ | grep -v "\.rst"
```

**Esperado**: Solo 3 directorios

### Check 2: Build solo publica biblioteca

```bash
# Debe mostrar SOLO biblioteca
ls -1 build/html/ | grep -v "^_" | grep -v "\.html"
```

**Esperado**: Solo `biblioteca/`

### Check 3: Pipeline privado existe

```bash
# Debe mostrar 10 directorios
ls -1 pipeline_docs/procedimientos/
```

**Esperado**: 01_fundamentos hasta 10_apendices

### Check 4: Git limpio

```bash
git status
```

**Esperado**: "nothing to commit, working tree clean"

---

## ⏱️ TIEMPO TOTAL

| Fase | Tiempo |
|------|--------|
| FASE 0: Backup | 1 min |
| FASE 1: Crear estructura | 1 min |
| FASE 2: Mover 01-10 | 5 min |
| FASE 3: Mover docs_maestros | 2 min |
| FASE 4: Archivar | 2 min |
| FASE 5: Actualizar index | 3 min |
| FASE 6: README pipeline_docs | 2 min |
| FASE 7: Verificar | 1 min |
| FASE 8: Build prueba | 3 min |
| FASE 9: Commit | 2 min |
| **TOTAL** | **22 min** |

---

## 🎯 LISTO PARA EJECUTAR

**¿Procedo con la ejecución?**

Responde:
- **"Ejecuta"** → Inicio inmediatamente
- **"Espera"** → Quieres revisar algo más
- **"Modifica X"** → Ajustes necesarios

