# Estructura Final COMPLETA: arc42_documentation

**Fecha**: 2026-02-01  
**Incluye**: Secciones, Tips, Ejemplos, Diagramas, Figuras

---

## 📁 ESTRUCTURA PÚBLICA (source/biblioteca)

```
arc42_documentation/
│
├── index.rst                           ← Índice general arc42
│
├── 01_introduction_goals/
│   ├── index.rst                       ← Índice sección 1
│   │
│   ├── secciones/                      ← ✅ Contenido principal
│   │   ├── introduccion_objetivos.rst
│   │   ├── requisitos.rst
│   │   ├── quality_goals.rst
│   │   └── stakeholders.rst
│   │
│   ├── tips/                           ← ✅ Consejos prácticos (24)
│   │   ├── tip-01.rst
│   │   ├── tip-02.rst
│   │   └── ... hasta tip-24.rst
│   │
│   ├── ejemplos/                       ← ✅ Casos prácticos (4)
│   │   ├── introduccion_ejemplo-3.rst
│   │   ├── introduccion_ejemplo-htmlsc-1.rst
│   │   ├── requisitos_calidad_ejemplo-1.rst
│   │   └── requisitos_calidad_ejemplo-3.rst
│   │
│   ├── diagramas/                      ← ✅ Diagramas (SVG, PNG, etc.)
│   │   └── [archivos de diagramas]
│   │
│   └── figuras/                        ← ✅ Figuras/Imágenes
│       └── [archivos de imágenes]
│
├── 02_constraints/
│   ├── index.rst
│   ├── secciones/
│   ├── tips/
│   ├── ejemplos/
│   ├── diagramas/
│   └── figuras/
│
├── 03_context_scope/
│   ├── index.rst
│   ├── secciones/
│   ├── tips/
│   ├── ejemplos/
│   ├── diagramas/
│   └── figuras/
│
└── ... (hasta 12_glossary)
```

---

## 🎯 PATRÓN ESTÁNDAR (se repite en las 12 secciones)

```
XX_nombre_seccion/
│
├── index.rst           ← Índice de la sección
│
├── secciones/          ← Contenido core (must read)
│   └── [archivos .rst principales]
│
├── tips/               ← Consejos prácticos (helpful)
│   └── [tip-01.rst, tip-02.rst, ...]
│
├── ejemplos/           ← Casos prácticos (learn by doing)
│   └── [ejemplo-*.rst]
│
├── diagramas/          ← Diagramas técnicos
│   └── [.svg, .png, .drawio, etc.]
│
└── figuras/            ← Imágenes/Figuras
    └── [.png, .jpg, .svg, etc.]
```

---

## 📊 TIPOS DE CONTENIDO

### 1. Secciones (Contenido Core)
**Qué es**: Contenido principal de la sección  
**Formato**: .rst  
**Ejemplos**: introduccion_objetivos.rst, quality_goals.rst  
**Audiencia**: Todos (lectura obligatoria)

### 2. Tips (Consejos)
**Qué es**: Consejos prácticos, mejores prácticas  
**Formato**: .rst  
**Ejemplos**: tip-01.rst, tip-02.rst  
**Audiencia**: Usuarios buscando guidance

### 3. Ejemplos (Casos Prácticos)
**Qué es**: Ejemplos concretos, casos de uso  
**Formato**: .rst  
**Ejemplos**: introduccion_ejemplo-3.rst  
**Audiencia**: Usuarios aprendiendo con ejemplos

### 4. Diagramas (Visualizaciones Técnicas)
**Qué es**: Diagramas de arquitectura, flujos, UML  
**Formato**: .svg, .png, .drawio, .puml  
**Audiencia**: Usuarios visuales, arquitectos

### 5. Figuras (Imágenes)
**Qué es**: Capturas de pantalla, fotos, gráficos  
**Formato**: .png, .jpg, .gif  
**Audiencia**: Todos (apoyo visual)

---

## 🗂️ DIFERENCIA: diagramas/ vs figuras/

### diagramas/
**Contenido**:
- Diagramas de arquitectura (C4, UML)
- Diagramas de flujo
- Diagramas de secuencia
- Modelos de datos
- Diagramas editables (.drawio, .puml)

**Características**:
- Técnicos
- Generados con herramientas
- Editables (fuentes disponibles)

### figuras/
**Contenido**:
- Capturas de pantalla
- Fotos
- Gráficos estáticos
- Ilustraciones
- Imágenes de referencia

**Características**:
- Visuales
- No editables (formatos finales)
- De apoyo documental

---

## 🔄 PLAN DE MIGRACIÓN ACTUALIZADO

### PASO 1: Crear estructura completa

```bash
cd /tmp/ADT/source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation

# Para cada sección
for section in sections/*/; do
    section_name=$(basename "$section")
    
    # Crear subdirectorios en raíz (sin "sections/")
    mkdir -p "$section_name"/{secciones,tips,ejemplos}
    
    # Mover diagramas y figuras (ya existen)
    if [ -d "$section/diagramas" ]; then
        mv "$section/diagramas" "$section_name/"
    fi
    
    if [ -d "$section/figuras" ]; then
        mv "$section/figuras" "$section_name/"
    fi
done
```

### PASO 2: Organizar contenido de traduccion/

```bash
for section in sections/*/; do
    section_name=$(basename "$section")
    
    cd "$section/traduccion"
    
    # Mover secciones principales
    mv seccion_*.rst ../../$section_name/secciones/ 2>/dev/null
    
    # Mover tips
    mv *_tip-*.rst ../../$section_name/tips/ 2>/dev/null
    
    # Mover ejemplos
    mv *_ejemplo-*.rst ../../$section_name/ejemplos/ 2>/dev/null
    
    cd -
done
```

### PASO 3: Mover contenido PRIVADO

```bash
# Mover original/ de cada sección
for section in sections/*/; do
    section_name=$(basename "$section")
    
    if [ -d "$section/original" ]; then
        mv "$section/original" \
           /tmp/ADT/pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/originales/por_seccion/$section_name/
    fi
done
```

### PASO 4: Eliminar estructura vieja

```bash
# Eliminar sections/ completo (ya vaciado)
rm -rf sections/
```

---

## ✅ RESULTADO FINAL

### PÚBLICO (Usuario ve en HTML)

```
arc42 Documentation
│
└── 1. Introduction and Goals
    │
    ├── 📄 Contenido Principal (4 documentos)
    │   ├── Introducción y Objetivos
    │   ├── Requisitos
    │   ├── Quality Goals
    │   └── Stakeholders
    │
    ├── 💡 Tips y Consejos (24)
    │   ├── Tip 1: Define clear goals
    │   ├── Tip 2: Stakeholder analysis
    │   └── ...
    │
    ├── 📝 Ejemplos Prácticos (4)
    │   ├── Ejemplo: Sistema de E-commerce
    │   ├── Ejemplo: HTML Scaffold
    │   └── ...
    │
    ├── 📊 Diagramas
    │   └── [diagramas técnicos]
    │
    └── 🖼️ Figuras
        └── [imágenes de apoyo]
```

### PRIVADO (En pipeline_docs_work)

```
pipeline_docs_work/.../arc42_documentation/
├── originales/
│   ├── full_site/
│   └── por_seccion/
│       ├── 01_introduction_goals/
│       ├── 02_constraints/
│       └── ...
├── metadata/
├── reportes/
└── trabajo/
```

---

## 🎯 VENTAJAS DE ESTA ESTRUCTURA

### Para Usuarios (Público)
- ✅ **Clara navegación**: Sé dónde encontrar cada tipo de contenido
- ✅ **Progresiva**: Leo secciones → consulto tips → veo ejemplos → analizo diagramas
- ✅ **Visual**: Diagramas y figuras accesibles fácilmente
- ✅ **Completa**: Todo el contenido organizado lógicamente

### Para Equipo (Privado)
- ✅ **Separación total**: Trabajo interno no se publica
- ✅ **Trazabilidad**: Originales archivados por sección
- ✅ **Workflow claro**: De originales → trabajo → público
- ✅ **Escalable**: Agregar nuevo contenido es obvio dónde va

### Para Mantenimiento
- ✅ **Consistente**: Mismo patrón en 12 secciones
- ✅ **Extensible**: Agregar nuevo tipo (ej: ejercicios/) es fácil
- ✅ **Sphinx-friendly**: Estructura clara para toctrees
- ✅ **Git-friendly**: Cambios localizados, fácil de revisar

---

## 📝 ÍNDICE DE SECCIÓN (Ejemplo completo)

```rst
Sección 1: Introduction and Goals
==================================

Esta sección describe los requisitos fundamentales y objetivos del sistema.

.. toctree::
   :maxdepth: 2
   :caption: 📄 Contenido Principal
   
   secciones/introduccion_objetivos
   secciones/requisitos
   secciones/quality_goals
   secciones/stakeholders

.. toctree::
   :maxdepth: 1
   :caption: 💡 Tips y Consejos
   :glob:
   
   tips/tip-*

.. toctree::
   :maxdepth: 1
   :caption: 📝 Ejemplos Prácticos
   :glob:
   
   ejemplos/*

.. toctree::
   :maxdepth: 1
   :caption: 📊 Recursos Visuales
   
   Diagramas <diagramas/index>
   Figuras <figuras/index>
```

---

## 🚀 ESTADO ACTUAL

**Estructura identificada**:
- ✅ secciones/ (contenido core)
- ✅ tips/ (consejos)
- ✅ ejemplos/ (casos prácticos)
- ✅ diagramas/ (visualizaciones técnicas)
- ✅ figuras/ (imágenes de apoyo)

**Próximo paso**: Ejecutar migración completa

---

## 🤔 CONFIRMACIÓN FINAL

**¿Esta estructura completa está correcta?**

Si confirmas, ejecuto la migración completa:
1. Reorganizar arc42 (con diagramas/ y figuras/)
2. Mover privados a pipeline_docs_work
3. Finalizar 9 fases pendientes
4. Build final y commit

**¿Procedo?**

