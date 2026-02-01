# Análisis CORRECTO - Proyecto Biblioteca Pública

**Fecha**: 2026-02-01  
**Perspectiva corregida**: Este es un proyecto de BIBLIOTECA pública

---

## 🎯 ENTENDIMIENTO CORRECTO

### Propósito del Proyecto

**PÚBLICO (lo que se publica con Sphinx)**:
- `biblioteca/` - Contenido traducido (libros, documentos)
- Este es el **producto final** para usuarios

**PRIVADO (documentación interna del equipo)**:
- `01-10/` - Pipeline de traducción (cómo lo hacemos)
- `docs_maestros/` - Metodología, arquitectura (cómo lo diseñamos)
- Solo para el equipo de traducción

**A ARCHIVAR (no se usa)**:
- `diataxis/` - Vacío, experimento no usado
- `docs/` - Meta-docs obsoletos

---

## 📊 ANÁLISIS ACTUAL

### ¿Qué está en source/ ahora?

```bash
source/
├── 01_fundamentos/           ← PRIVADO (no debería publicarse)
├── 02_procedimientos/        ← PRIVADO (no debería publicarse)
├── 03_estandares/            ← PRIVADO (no debería publicarse)
├── 04_reglas_operativas/     ← PRIVADO (no debería publicarse)
├── 05_herramientas_medios/   ← PRIVADO (no debería publicarse)
├── 06_casos_practicos/       ← PRIVADO (no debería publicarse)
├── 07_guias_uso/             ← PRIVADO (no debería publicarse)
├── 08_prompts/               ← PRIVADO (no debería publicarse)
├── 09_referencias/           ← PRIVADO (no debería publicarse)
├── 10_apendices/             ← PRIVADO (no debería publicarse)
├── biblioteca/               ← ✅ PÚBLICO (se DEBE publicar)
├── diataxis/                 ← ❌ ARCHIVAR (vacío)
├── docs/                     ← ❌ ARCHIVAR (obsoleto)
├── docs_maestros/            ← PRIVADO (parte del pipeline)
├── _static/                  ← ✅ Necesario Sphinx
└── _templates/               ← ✅ Necesario Sphinx
```

### 🔴 PROBLEMA CRÍTICO

**TODO el pipeline (01-10) se está PUBLICANDO con Sphinx**

Actualmente cuando haces `make html`:
- Se publica `01_fundamentos/` ← No debería
- Se publica `02_procedimientos/` ← No debería
- Se publica `03_estandares/` ← No debería
- etc.

**Estos son documentos INTERNOS del equipo, no para usuarios finales.**

---

## ✅ ESTRUCTURA CORRECTA

### Propuesta: Separar Público de Privado

```
/tmp/ADT/
│
├── source/                    ← Solo contenido PÚBLICO
│   ├── biblioteca/           ← ✅ Libros traducidos (SE PUBLICA)
│   │   ├── ciencias/
│   │   ├── informatica/
│   │   └── ingenieria/
│   ├── _static/              ← Necesario Sphinx
│   ├── _templates/           ← Necesario Sphinx
│   └── index.rst             ← Índice simple: solo biblioteca
│
├── pipeline-docs/            ← NUEVO: Docs PRIVADAS del equipo
│   ├── metodologia/          ← Mover docs_maestros aquí
│   │   ├── ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
│   │   ├── METODO_TRADUCCION_PESHITTA_ZACHARIAS.md
│   │   └── ...
│   ├── procedimientos/       ← Mover 01-10 aquí
│   │   ├── 01_fundamentos/
│   │   ├── 02_procedimientos/
│   │   ├── 03_estandares/
│   │   ├── 04_reglas_operativas/
│   │   ├── 05_herramientas_medios/
│   │   ├── 06_casos_practicos/
│   │   ├── 07_guias_uso/
│   │   ├── 08_prompts/
│   │   ├── 09_referencias/
│   │   └── 10_apendices/
│   └── README.md             ← Índice del pipeline interno
│
├── archivados/               ← Contenido obsoleto
│   ├── 20260201-diataxis/
│   └── 20260201-docs/
│
└── .codex/skills/            ← Ya existe (correcto)
```

---

## 🎯 BENEFICIOS

### Antes (Problemático)
```
make html → Publica:
  - biblioteca/ ✅ (correcto)
  - 01_fundamentos/ ❌ (no debería)
  - 02_procedimientos/ ❌ (no debería)
  - docs_maestros/ ❌ (no debería)
  - ... etc
```

### Después (Correcto)
```
make html → Publica:
  - biblioteca/ ✅ (solo esto)
```

### Claridad

| Directorio | Propósito | Audiencia |
|------------|-----------|-----------|
| `source/biblioteca/` | Contenido traducido | **Usuarios públicos** |
| `pipeline-docs/` | Cómo traducimos | **Equipo interno** |
| `archivados/` | Experimentos fallidos | Nadie |

---

## 📋 PLAN DE MIGRACIÓN

### FASE 0: Backup (CRÍTICO)

```bash
cd /tmp/ADT
git add -A
git commit -m "backup: antes de reorganización biblioteca pública"
git tag backup-antes-reorganizacion
```

### FASE 1: Crear Estructura Nueva (2 min)

```bash
cd /tmp/ADT

# Crear directorios
mkdir -p pipeline-docs/metodologia
mkdir -p pipeline-docs/procedimientos
mkdir -p archivados/20260201-diataxis
mkdir -p archivados/20260201-docs
```

### FASE 2: Mover Pipeline FUERA de source/ (5 min)

```bash
cd /tmp/ADT/source

# Mover 01-10 a pipeline-docs/procedimientos/
for dir in 01_fundamentos 02_procedimientos 03_estandares 04_reglas_operativas 05_herramientas_medios 06_casos_practicos 07_guias_uso 08_prompts 09_referencias 10_apendices; do
    mv $dir ../pipeline-docs/procedimientos/$dir
done

# Mover docs_maestros a pipeline-docs/metodologia/
mv docs_maestros/* ../pipeline-docs/metodologia/
rmdir docs_maestros
```

### FASE 3: Archivar Obsoletos (1 min)

```bash
cd /tmp/ADT/source

# Archivar diataxis (vacío)
mv diataxis ../archivados/20260201-diataxis/

# Archivar docs (obsoleto)
mv docs ../archivados/20260201-docs/
```

### FASE 4: Actualizar index.rst de source/ (3 min)

```bash
cd /tmp/ADT/source

# NUEVO index.rst - SOLO biblioteca
cat > index.rst << 'EOF'
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
EOF
```

### FASE 5: Crear README.md en pipeline-docs/ (2 min)

```bash
cd /tmp/ADT/pipeline-docs

cat > README.md << 'EOF'
# Pipeline de Traducción ADT - Documentación Interna

**AUDIENCIA**: Equipo de traducción (PRIVADO, no se publica)

Este directorio contiene la documentación del pipeline de traducción:
- Metodología
- Procedimientos
- Herramientas
- Decisiones arquitectónicas

**NO se publica con Sphinx** - solo para uso interno del equipo.

## Estructura

- **metodologia/**: Arquitectura, métodos maestros
- **procedimientos/**: Guías operativas (01-10)

## Diferencia con source/

| Directorio | Contenido | Audiencia |
|------------|-----------|-----------|
| `source/` | Biblioteca (contenido traducido) | Usuarios públicos |
| `pipeline-docs/` | Cómo traducimos | Equipo interno |
EOF
```

### FASE 6: Verificar Build Sphinx (5 min)

```bash
cd /tmp/ADT

# Limpiar build anterior
make clean

# Build nuevo (SOLO debería compilar biblioteca)
make html

# Verificar output
ls -R build/html/

# ¿Se publicó SOLO biblioteca? ✅
# ¿NO se publicaron 01-10? ✅
```

### FASE 7: Commit (2 min)

```bash
cd /tmp/ADT

git add -A
git commit -m "refactor(estructura): separar biblioteca pública de pipeline privado

- source/ ahora solo contiene biblioteca/ (contenido público)
- pipeline-docs/ contiene docs internas (01-10, docs_maestros)
- archivados/ contiene diataxis y docs obsoletos
- Build Sphinx ahora publica SOLO biblioteca

BREAKING CHANGE: Estructura completamente reorganizada"
```

---

## ✅ RESULTADO FINAL

### Estructura DESPUÉS

```
/tmp/ADT/
├── source/                    ✅ Solo biblioteca pública
│   ├── biblioteca/
│   ├── _static/
│   ├── _templates/
│   └── index.rst
│
├── pipeline-docs/            ✅ Docs privadas del equipo
│   ├── metodologia/
│   └── procedimientos/
│
├── archivados/               ✅ Obsoletos archivados
│   ├── 20260201-diataxis/
│   └── 20260201-docs/
│
└── build/html/               ✅ Publica SOLO biblioteca
    └── biblioteca/
```

### Build Sphinx

**Antes**: Publicaba 16 secciones (biblioteca + 01-10 + docs_maestros + ...)

**Después**: Publica 1 sección (solo biblioteca)

---

## 🚨 PREGUNTAS CRÍTICAS

### P1: ¿Alguno de 01-10 debería ser público?

Si alguna sección de 01-10 tiene valor para usuarios finales:
- ¿Guías de uso?
- ¿Referencias?

**Opciones**:
a) Mover esa sección específica de vuelta a `source/`
b) Crear `source/guias/` para documentación pública selecta
c) Mantener TODO en pipeline-docs/ (privado)

**Tu decisión**: ?

### P2: ¿Necesitas versión pública del pipeline?

Si quieres publicar la metodología para la comunidad:
- Crear `source/metodologia/` con versión simplificada
- Mantener detalles técnicos en `pipeline-docs/`

**Tu decisión**: ?

### P3: ¿Cómo manejar el README del proyecto?

Actualmente `/tmp/ADT/README.md` probablemente describe todo.

**Opciones**:
a) Actualizar para reflejar que proyecto es principalmente la BIBLIOTECA
b) Mantener mención del pipeline pero indicar que es privado
c) Crear README separados (uno público, uno privado)

**Tu decisión**: ?

---

## 📊 COMPARACIÓN

| Aspecto | Estructura Vieja | Estructura Nueva |
|---------|------------------|------------------|
| **Propósito** | ❌ Confuso | ✅ Claro: Biblioteca pública |
| **Contenido público** | ❌ Todo (16 secciones) | ✅ Solo biblioteca |
| **Docs privadas** | ❌ Mezcladas en source/ | ✅ En pipeline-docs/ |
| **Build Sphinx** | ❌ Publica todo | ✅ Solo biblioteca |
| **Navegación** | ❌ 16 secciones abrumadoras | ✅ Simple y clara |
| **Mantenimiento** | ❌ Confuso dónde poner docs | ✅ Ubicación obvia |

---

## 🎯 RECOMENDACIÓN

**EJECUTAR esta reorganización**

**Razones**:
1. Separa claramente público (biblioteca) de privado (pipeline)
2. Build Sphinx publica solo lo necesario
3. Más profesional para usuarios finales
4. Facilita mantenimiento futuro

**Tiempo**: 20 minutos  
**Riesgo**: Bajo (con backup de git)  
**Beneficio**: Alto (claridad total)

---

## 📝 SIGUIENTE PASO

**¿Quieres que ejecute este plan?**

Antes de ejecutar, necesito tus respuestas a:
- P1: ¿Alguna sección de 01-10 debería ser pública?
- P2: ¿Versión pública de la metodología?
- P3: ¿Actualizar README principal?

O simplemente: **"Ejecuta todo, todo es privado excepto biblioteca"**

