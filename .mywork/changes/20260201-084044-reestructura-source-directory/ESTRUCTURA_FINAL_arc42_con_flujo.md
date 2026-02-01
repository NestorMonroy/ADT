# Estructura Final: arc42_documentation con Flujo de Trabajo

**Fecha**: 2026-02-01  
**Clasificación**: ING.ARQ.ARC.001 (Ingeniería > Arquitectura > arc42)

---

## 🎯 FLUJO DE TRABAJO

### INPUT (Lo que recibes)
```
📥 Usuario entrega:
   ├── arc42_template.zip (archivos por secciones)
   ├── arc42_full.pdf (documento completo)
   └── arc42_site.zip (archivos HTML)
```

### PROCESO (pipeline_docs_work)
```
🔧 Trabajo en progreso:
   ├── Originales extraídos
   ├── Metadata de clasificación
   ├── Reportes de traducción
   └── Archivos de apoyo
```

### OUTPUT (source/biblioteca)
```
✅ Resultado público:
   └── Contenido traducido organizado
```

---

## 📁 ESTRUCTURA PROPUESTA

### PÚBLICO (source/biblioteca)

```
source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/
│
├── index.rst                           ← Índice principal arc42
│
├── 01_introduction_goals/              ← ✅ Solo traducción
│   ├── introduccion_objetivos.rst
│   ├── requisitos_calidad.rst
│   └── stakeholders.rst
│
├── 02_constraints/                     ← ✅ Solo traducción
│   ├── restricciones_tecnicas.rst
│   └── restricciones_organizativas.rst
│
├── 03_context/                         ← ✅ Solo traducción
├── 04_strategy/                        ← ✅ Solo traducción
├── 05_building_blocks/                 ← ✅ Solo traducción
├── 06_runtime/                         ← ✅ Solo traducción
├── 07_deployment/                      ← ✅ Solo traducción
├── 08_concepts/                        ← ✅ Solo traducción
├── 09_decisions/                       ← ✅ Solo traducción
├── 10_quality/                         ← ✅ Solo traducción
├── 11_risks/                           ← ✅ Solo traducción
└── 12_glossary/                        ← ✅ Solo traducción
```

**Sin**:
- ❌ Carpeta "sections/" (eliminada)
- ❌ Carpetas "original/" (movidas a pipeline_docs_work)
- ❌ Carpetas "traduccion/" (contenido subido un nivel)
- ❌ Archivos REPORTE_*.rst (movidos a pipeline_docs_work)

---

### PRIVADO (pipeline_docs_work)

```
pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/
│
├── README.md                           ← Explicación del workflow
│
├── originales/                         ← 🔒 Archivos fuente
│   ├── full_site/                      ← Site completo original
│   │   ├── _posts/
│   │   │   ├── 01-requirements/
│   │   │   ├── 02-constraints/
│   │   │   └── ... (12 secciones)
│   │   ├── assets/
│   │   └── _includes/
│   │
│   └── por_seccion/                    ← Originales organizados
│       ├── 01_introduction_goals/
│       ├── 02_constraints/
│       └── ... (12 secciones)
│
├── metadata/                           ← 🔒 Metadata del proceso
│   ├── clasificacion.rst               ← De _metadata_biblioteca
│   ├── guia_organizacion.rst
│   └── esquema_codificacion.rst
│
├── reportes/                           ← 🔒 Reportes de traducción
│   ├── REPORTE_LOTE_1_COMPLETADO.rst
│   ├── REPORTE_LOTE_2_COMPLETADO.rst
│   ├── REPORTE_01_introduction_goals.rst
│   ├── REPORTE_02_constraints.rst
│   └── ...
│
└── trabajo/                            ← 🔒 Archivos temporales
    ├── borradores/
    ├── validaciones/
    └── notas/
```

---

## 🔄 WORKFLOW DETALLADO

### Paso 1: Recepción de Originales

```bash
# Usuario entrega ZIP
cd /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation

# Extraer a originales/
unzip arc42_template.zip -d originales/full_site/

# O extraer secciones
unzip arc42_sections.zip -d originales/por_seccion/
```

### Paso 2: Clasificación

```bash
# Consultar metadata para clasificar
# Según META_BIB_001: ING.ARQ.ARC.001

# Código resultante:
# ING = Ingeniería
# ARQ = Arquitectura  
# ARC = arc42
# 001 = Primer libro arc42
```

### Paso 3: Traducción

```bash
# Trabajar sección por sección
# Leer: originales/por_seccion/01_introduction_goals/
# Traducir con metodología ADT
# Generar: trabajo/borradores/01_introduction_goals/
```

### Paso 4: Validación y Reporte

```bash
# Validar traducción
# Generar reporte
echo "LOTE 1 COMPLETADO" > reportes/REPORTE_01_introduction_goals.rst
```

### Paso 5: Publicación

```bash
# Mover traducción validada a público
mv trabajo/borradores/01_introduction_goals/*.rst \
   /tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/01_introduction_goals/
```

---

## 📊 COMPARACIÓN: ANTES vs DESPUÉS

### ANTES (Actual - Confuso)

```
source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/
├── original/              ← 🔴 PRIVADO mezclado con PÚBLICO
│   └── _posts/...
│
├── _metadata_biblioteca/  ← 🔴 En lugar incorrecto
│
└── sections/              ← 🔴 Nivel innecesario
    ├── 01_introduction_goals/
    │   ├── original/      ← 🔴 PRIVADO
    │   ├── traduccion/    ← ✅ PÚBLICO
    │   └── REPORTE_*.rst  ← 🔴 PRIVADO
    └── ...
```

### DESPUÉS (Propuesto - Claro)

```
source/biblioteca/.../arc42_documentation/
├── 01_introduction_goals/  ← ✅ Solo traducción
├── 02_constraints/         ← ✅ Solo traducción
└── ...

pipeline_docs_work/.../arc42_documentation/
├── originales/             ← 🔒 Todo lo privado
├── metadata/               ← 🔒 Metadata
├── reportes/               ← 🔒 Reportes
└── trabajo/                ← 🔒 Temporal
```

---

## ✅ VENTAJAS DE ESTA ESTRUCTURA

1. **Separación total**: Público en source/, privado en pipeline_docs_work/
2. **Sin redundancia**: No hay "traduccion/traduccion" 
3. **Refleja workflow**: Estructura espeja el proceso real de trabajo
4. **Escalable**: Si agregas más libros, mismo patrón
5. **Clasificación clara**: Sigue META_BIB_001 exactamente

---

## 🎯 NOMENCLATURA CORRECTA

### ❌ INCORRECTO (lo que estaba haciendo)
- `pipeline_docs/arc42/` ← "arc42" es el LIBRO, no la carpeta
- `sections/` ← Nivel innecesario

### ✅ CORRECTO (propuesta final)
- `pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/`
- Refleja que es TRABAJO (work) del pipeline
- Mantiene nombre completo del libro: `arc42_documentation`
- Estructura paralela a source/biblioteca

---

## 📝 NOMBRES ALTERNATIVOS (si prefieres)

### Para el directorio raíz privado:

**Opción 1**: `pipeline_docs_work` ⭐ (recomendado)
- Refleja: documentos del pipeline + trabajo en progreso

**Opción 2**: `translation_work`
- Refleja: trabajo de traducción

**Opción 3**: `biblioteca_work`
- Refleja: trabajo sobre la biblioteca

**Opción 4**: `docs_privadas`
- Refleja: documentación privada

---

## 🚀 PLAN DE MIGRACIÓN

### FASE 1: Crear estructura pipeline_docs_work

```bash
cd /tmp/ADT

# Crear estructura completa
mkdir -p pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/{originales/{full_site,por_seccion},metadata,reportes,trabajo/{borradores,validaciones,notas}}
```

### FASE 2: Mover contenido PRIVADO

```bash
cd /tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation

# 1. Mover original/ completo
mv original/ /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/originales/full_site/

# 2. Mover metadata
mv /tmp/ADT/source/biblioteca/_metadata_biblioteca/* \
   /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/metadata/

# 3. Mover reportes de cada sección
find sections/ -name "REPORTE_*.rst" -exec mv {} \
   /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/reportes/ \;

# 4. Mover original/ de cada sección
for section in sections/*/; do
    section_name=$(basename "$section")
    if [ -d "$section/original" ]; then
        mv "$section/original" \
           /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/originales/por_seccion/$section_name/
    fi
done
```

### FASE 3: Limpiar PÚBLICO (solo traducción)

```bash
cd /tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation

# Promover traduccion/ al nivel de sección y eliminar "sections/"
for section in sections/*/; do
    section_name=$(basename "$section")
    
    # Mover contenido de traduccion/ directamente a la sección
    if [ -d "$section/traduccion" ]; then
        mv "$section/traduccion" "../temp_$section_name"
    fi
done

# Eliminar sections/ viejo
rm -rf sections/

# Renombrar temp_* a nombres finales
for dir in ../temp_*/; do
    section_name=$(basename "$dir" | sed 's/temp_//')
    mv "$dir" "$section_name"
done
```

### FASE 4: Crear README en pipeline_docs_work

```bash
cat > /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/README.md << 'EOF'
# arc42_documentation - Archivos de Trabajo

**Clasificación**: ING.ARQ.ARC.001  
**Estado**: En traducción  
**Audiencia**: Equipo interno

---

## Estructura

- **originales/**: Archivos fuente (ZIP/PDF/HTML recibidos)
- **metadata/**: Sistema de clasificación y organización  
- **reportes/**: Reportes de progreso por sección
- **trabajo/**: Borradores y validaciones

---

## Workflow

1. Originales → `originales/`
2. Traducción → `trabajo/borradores/`
3. Validación → `trabajo/validaciones/`
4. Reporte → `reportes/`
5. Publicación → `/source/biblioteca/.../arc42_documentation/`

EOF
```

---

## 🎯 RESULTADO FINAL

### source/biblioteca (PÚBLICO - Se publica con Sphinx)

```
ingenieria/sistemas/arquitectura/arc42_documentation/
├── index.rst
├── 01_introduction_goals/
│   └── [archivos .rst traducidos]
├── 02_constraints/
│   └── [archivos .rst traducidos]
└── ... (hasta 12_glossary)
```

### pipeline_docs_work (PRIVADO - No se publica)

```
ingenieria/sistemas/arquitectura/arc42_documentation/
├── README.md
├── originales/
│   ├── full_site/
│   └── por_seccion/
├── metadata/
├── reportes/
└── trabajo/
```

---

## 🤔 DECISIÓN FINAL NECESARIA

**¿Nombre del directorio raíz privado?**

- [ ] `pipeline_docs_work` (trabajo del pipeline)
- [ ] `translation_work` (trabajo de traducción)
- [ ] `biblioteca_work` (trabajo de biblioteca)
- [ ] `docs_privadas` (documentación privada)
- [ ] Otro: _______________

**Una vez decidas, ejecuto la migración completa.**

