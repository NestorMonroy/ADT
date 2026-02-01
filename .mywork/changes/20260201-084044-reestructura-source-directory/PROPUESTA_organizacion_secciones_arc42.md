# Propuesta: Organización de Secciones arc42

**Fecha**: 2026-02-01  
**Análisis de**: sections/01_introduction_goals/traduccion/

---

## 📊 CONTENIDO ENCONTRADO

### Tipos de archivos (32 archivos totales):

**1. Secciones principales** (4 archivos - contenido core):
- `seccion_01_introduccion_objetivos.rst` (3.3K)
- `seccion_1_1_requisitos.rst` (2.5K)
- `seccion_1_2_quality_goals.rst` (4.8K)
- `seccion_1_3_stakeholders.rst` (4.7K)

**2. Tips** (24 archivos - consejos prácticos):
- `introduccion_tip-1.rst` hasta `introduccion_tip-24.rst`
- Tamaños: 1K - 3K cada uno
- Total: ~24 tips

**3. Ejemplos** (4 archivos - casos prácticos):
- `introduccion_ejemplo-3.rst` (3.9K)
- `introduccion_ejemplo-htmlsc-1.rst` (2.3K)
- `requisitos_calidad_ejemplo-1.rst` (2.1K)
- `requisitos_calidad_ejemplo-3.rst` (1.6K)

---

## 🎯 PROPUESTAS DE ORGANIZACIÓN

### OPCIÓN A: Por Tipo de Contenido ⭐ (RECOMENDADA)

```
01_introduction_goals/
│
├── index.rst                           ← Índice de la sección
│
├── secciones/                          ← Contenido principal
│   ├── introduccion_objetivos.rst
│   ├── requisitos.rst
│   ├── quality_goals.rst
│   └── stakeholders.rst
│
├── tips/                               ← Consejos prácticos
│   ├── tip-01.rst
│   ├── tip-02.rst
│   └── ... (24 tips)
│
└── ejemplos/                           ← Casos prácticos
    ├── introduccion_ejemplo-3.rst
    ├── introduccion_ejemplo-htmlsc-1.rst
    ├── requisitos_calidad_ejemplo-1.rst
    └── requisitos_calidad_ejemplo-3.rst
```

**Ventajas**:
- ✅ Separación clara por tipo de contenido
- ✅ Fácil navegar: "quiero ver ejemplos" → ir a `ejemplos/`
- ✅ Escalable: si agregan "ejercicios", crear carpeta nueva
- ✅ Los nombres de archivo ya tienen prefijos que indican tipo

**Desventajas**:
- Requiere renombrar archivos (quitar prefijos redundantes)

---

### OPCIÓN B: Plano Simple

```
01_introduction_goals/
├── index.rst
├── introduccion_objetivos.rst
├── requisitos.rst
├── quality_goals.rst
├── stakeholders.rst
├── tip-01.rst
├── tip-02.rst
├── ... (24 tips)
├── ejemplo-introduccion-3.rst
├── ejemplo-introduccion-htmlsc-1.rst
├── ejemplo-requisitos-calidad-1.rst
└── ejemplo-requisitos-calidad-3.rst
```

**Ventajas**:
- ✅ Todos los archivos al mismo nivel
- ✅ Más simple (sin subdirectorios)

**Desventajas**:
- ❌ 32 archivos en un solo directorio (difícil navegar)
- ❌ No agrupa contenido relacionado

---

### OPCIÓN C: Híbrida - Core + Recursos

```
01_introduction_goals/
│
├── index.rst
├── introduccion_objetivos.rst          ← Core al nivel raíz
├── requisitos.rst
├── quality_goals.rst
├── stakeholders.rst
│
└── recursos/                           ← Tips y ejemplos juntos
    ├── tips/
    │   └── ... (24 tips)
    └── ejemplos/
        └── ... (4 ejemplos)
```

**Ventajas**:
- ✅ Contenido principal accesible directamente
- ✅ Recursos agrupados pero separados

**Desventajas**:
- Nivel extra "recursos/" puede ser innecesario

---

## 🎯 RECOMENDACIÓN: OPCIÓN A

**Por qué**:
1. **Clara jerarquía**: Secciones (must read) > Tips (helpful) > Ejemplos (practical)
2. **Navegación intuitiva**: Usuario busca ejemplos → va a `ejemplos/`
3. **Mantenible**: Agregar nuevo tip → agregar en `tips/`
4. **Consistente**: Mismo patrón en TODAS las 12 secciones de arc42

---

## 📋 ESTRUCTURA COMPLETA RESULTANTE

### PÚBLICO (source/biblioteca)

```
arc42_documentation/
│
├── index.rst                           ← Índice general arc42
│
├── 01_introduction_goals/
│   ├── index.rst                       ← Índice sección 1
│   ├── secciones/
│   │   ├── introduccion_objetivos.rst
│   │   ├── requisitos.rst
│   │   ├── quality_goals.rst
│   │   └── stakeholders.rst
│   ├── tips/
│   │   ├── tip-01.rst ... tip-24.rst
│   └── ejemplos/
│       └── ... (4 ejemplos)
│
├── 02_constraints/
│   ├── index.rst
│   ├── secciones/
│   ├── tips/
│   └── ejemplos/
│
└── ... (hasta 12_glossary)
```

**Patrón repetido** en cada sección:
```
XX_nombre_seccion/
├── index.rst
├── secciones/      ← Contenido principal
├── tips/           ← Consejos
└── ejemplos/       ← Casos prácticos
```

---

## 🔄 PLAN DE RENOMBRADO

### Paso 1: Renombrar archivos de secciones (quitar prefijo "seccion_")

```bash
cd traduccion/

# Renombrar secciones principales
mv seccion_01_introduccion_objetivos.rst secciones/introduccion_objetivos.rst
mv seccion_1_1_requisitos.rst secciones/requisitos.rst
mv seccion_1_2_quality_goals.rst secciones/quality_goals.rst
mv seccion_1_3_stakeholders.rst secciones/stakeholders.rst
```

### Paso 2: Renombrar tips (quitar prefijo "introduccion_", numerar correctamente)

```bash
# Tips
mv introduccion_tip-1.rst tips/tip-01.rst
mv introduccion_tip-2.rst tips/tip-02.rst
mv introduccion_tip-3.rst tips/tip-03.rst
# ... etc hasta tip-24
```

### Paso 3: Organizar ejemplos

```bash
# Ejemplos
mv introduccion_ejemplo-3.rst ejemplos/introduccion_ejemplo-3.rst
mv introduccion_ejemplo-htmlsc-1.rst ejemplos/introduccion_ejemplo-htmlsc-1.rst
mv requisitos_calidad_ejemplo-1.rst ejemplos/requisitos_calidad_ejemplo-1.rst
mv requisitos_calidad_ejemplo-3.rst ejemplos/requisitos_calidad_ejemplo-3.rst
```

### Paso 4: Crear index.rst para la sección

```bash
cat > index.rst << 'EOF'
Sección 1: Introduction and Goals
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contenido Principal
   
   secciones/introduccion_objetivos
   secciones/requisitos
   secciones/quality_goals
   secciones/stakeholders

.. toctree::
   :maxdepth: 1
   :caption: Tips y Consejos
   
   tips/tip-01
   tips/tip-02
   ... (hasta tip-24)

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos Prácticos
   
   ejemplos/introduccion_ejemplo-3
   ejemplos/introduccion_ejemplo-htmlsc-1
   ejemplos/requisitos_calidad_ejemplo-1
   ejemplos/requisitos_calidad_ejemplo-3
EOF
```

---

## 🎯 RESULTADO VISUAL

### Usuario navega en HTML generado:

```
arc42 Documentation
│
└── 1. Introduction and Goals
    │
    ├── Contenido Principal
    │   ├── Introducción y Objetivos
    │   ├── Requisitos
    │   ├── Quality Goals
    │   └── Stakeholders
    │
    ├── Tips y Consejos (24)
    │   ├── Tip 1: ...
    │   ├── Tip 2: ...
    │   └── ...
    │
    └── Ejemplos Prácticos (4)
        ├── Ejemplo: Introducción...
        ├── Ejemplo: HTML Scaffold...
        └── ...
```

**Navegación clara**: 
- Quiero leer contenido → "Contenido Principal"
- Busco consejo → "Tips y Consejos"  
- Necesito ejemplo → "Ejemplos Prácticos"

---

## ⚠️ ALTERNATIVA MÁS SIMPLE

Si prefieres menos subdirectorios:

```
01_introduction_goals/
├── index.rst
├── introduccion_objetivos.rst          ← 4 archivos principales
├── requisitos.rst
├── quality_goals.rst
├── stakeholders.rst
├── tip-01.rst ... tip-24.rst          ← 24 tips con prefijo
└── ejemplo-*.rst                       ← 4 ejemplos con prefijo
```

**Pros**: Más simple  
**Contras**: 32 archivos en un directorio

---

## 🤔 TU DECISIÓN

**¿Qué estructura prefieres?**

- **Opción A**: Subdirectorios por tipo (secciones/, tips/, ejemplos/)
- **Opción B**: Todo plano (32 archivos en raíz de sección)
- **Opción C**: Otra organización que prefieras

**Una vez decidas, actualizo el plan completo de migración.**

