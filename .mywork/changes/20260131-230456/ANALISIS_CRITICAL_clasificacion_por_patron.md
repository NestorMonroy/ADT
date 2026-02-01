# Análisis Completo de CRITICAL - Clasificación por Patrón

**Fecha**: 2026-02-01 02:45  
**Total CRITICAL**: 31  
**Archivos afectados**: 5

---

## 📊 CLASIFICACIÓN POR TIPO DE PROBLEMA

### TIPO 1: Code-Block Sin Indentar Correctamente ⚠️

**Descripción**: Contenido dentro de `.. code-block::` que NO está indentado (o tiene solo 1 espacio).

**RST correcto**:
```rst
.. code-block:: rst

   Contenido debe estar indentado 3+ espacios
   ==========================================
```

**RST incorrecto** (causa CRITICAL):
```rst
.. code-block:: rst

 Contenido con solo 1 espacio
 =============================
```

**Archivos afectados**:

#### error_01_omisiones.rst
- **Líneas**: 155, 159, 163, 167, 179 (sección 1)
- **Líneas**: 432, 436, 440, 444, 448, 452, 456, 460, 464, 468, 472, 476, 480, 484, 488, 492 (sección 2)
- **Total**: 22 CRITICAL

**Patrón observado**:
```rst
.. code-block:: rst




 7. Vista de Despliegue    ← Solo 1 espacio de indentación ❌
=======================

 Introducción              ← Solo 1 espacio de indentación ❌
 =============
```

**Corrección requerida**:
```rst
.. code-block:: rst

   7. Vista de Despliegue    ← 3 espacios de indentación ✅
   =======================

   Introducción              ← 3 espacios de indentación ✅
   =============
```

**Complejidad**: MODERADA  
**Estrategia**: Indentar todo el bloque +2 espacios (de 1 a 3)  
**Tiempo estimado**: 30-40 minutos (muchas líneas)

---

### TIPO 2: Títulos Fuera de Estructura ⚠️

**Descripción**: Títulos que están en contexto incorrecto, sin estar dentro de code-block.

**Archivos afectados**:

#### workflow_general.rst - Líneas 3407, 3409

**Contexto**:
```rst
 .. toctree::
 :maxdepth: 1

 tip_1

 tip_2          ← Sphinx piensa que es un título ❌
 ======
 tip_N          ← Sphinx piensa que es un título ❌
 ======
```

**Problema**: `tip_2` y `tip_N` tienen underlines `======` que Sphinx interpreta como títulos de sección, pero están en contexto de toctree.

**Corrección requerida**: Eliminar los underlines (no son necesarios en toctree)

```rst
 .. toctree::
 :maxdepth: 1

 tip_1
 tip_2          ← Solo el nombre ✅
 tip_N          ← Solo el nombre ✅
```

**Complejidad**: TRIVIAL  
**Tiempo estimado**: 2 minutos

---

#### WORKFLOW_v1_6_0_ACTUALIZACION.rst - Línea 634

**Contexto**:
```rst
 .. toctree::
 :maxdepth: 1

 tip_1

 tip_2
======          ← Underline incorrecto ❌
 tip_N
```

**Problema**: Mismo que workflow_general.rst

**Corrección**: Eliminar underline

**Complejidad**: TRIVIAL  
**Tiempo estimado**: 1 minuto

---

### TIPO 3: Título con Underline Incorrecto 🔴

**Descripción**: Título donde el underline no coincide con la estructura esperada.

**Archivos afectados**:

#### workflow_general.rst - Líneas 1363, 3080, 3083

##### Línea 1363:
```rst
 EVITAR TRADUCCIÓN LITERAL:
===========================       ← Underline NO está indentado como título ❌
```

**Problema**: Título tiene 1 espacio inicial, underline NO tiene espacio inicial → No alineados.

**Corrección**: Alinear título con underline

**Opción A** - Eliminar espacio del título:
```rst
EVITAR TRADUCCIÓN LITERAL:
===========================
```

**Opción B** - Agregar espacio al underline:
```rst
 EVITAR TRADUCCIÓN LITERAL:
 ===========================
```

**Complejidad**: TRIVIAL  
**Tiempo estimado**: 1 minuto por línea

##### Líneas 3080, 3083:
```rst
   TRANSLATED FILES (X TOTAL)
   ===========================

   SUBSECTIONS (X files):
   =======================
```

**Problema**: Títulos indentados 3 espacios (dentro de bloque) pero Sphinx no espera títulos ahí.

**Análisis necesario**: Verificar si están dentro de un bloque (code-block, note, etc.)

---

#### guia_rapida.rst - Línea ~307

**Contexto**:
```rst
 Comparación
 ============

 .. list-table::
    :header-rows: 1

    * - Aspecto
      - Simple
      - Complejo
    * - Entendimiento
   - Rápido (< 1 hora)    ← Indentación incorrecta ❌
```

**Problema**: Celda de tabla mal indentada (solo 3 espacios cuando necesita 4+)

**Corrección**: Corregir indentación de la celda

**Complejidad**: TRIVIAL  
**Tiempo estimado**: 2 minutos

---

#### GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst

**Necesita análisis más detallado** - No vi CRITICAL en el contexto mostrado.

---

## 📋 RESUMEN POR TIPO

| Tipo | Archivos | CRITICAL | Complejidad | Tiempo Est. |
|------|----------|----------|-------------|-------------|
| **TIPO 1**: Code-block sin indentar | 1 | 22 | MODERADA | 30-40 min |
| **TIPO 2**: Títulos en toctree | 2 | 3 | TRIVIAL | 3 min |
| **TIPO 3**: Título/underline desalineados | 1 | 4 | TRIVIAL | 5 min |
| **TIPO 3**: List-table mal indentada | 1 | 1 | TRIVIAL | 2 min |
| **PENDIENTE**: Análisis | 1 | 1 | ? | ? |

**Total**: 31 CRITICAL

---

## 🎯 ORDEN DE CORRECCIÓN RECOMENDADO

### 1. TIPO 2 - Títulos en toctree (QUICK WIN) ⭐

**Archivos**:
- workflow_general.rst (2 CRITICAL)
- WORKFLOW_v1_6_0_ACTUALIZACION.rst (1 CRITICAL)

**Total**: 3 CRITICAL  
**Tiempo**: 3 minutos  
**Complejidad**: TRIVIAL  
**Estrategia**: Eliminar underlines `======`

**Impacto**: Quick win para generar momentum

---

### 2. TIPO 3 - List-table + Desalineaciones (QUICK WIN)

**Archivos**:
- guia_rapida.rst (1 CRITICAL - list-table)
- workflow_general.rst (1 CRITICAL - línea 1363)

**Total**: 2 CRITICAL  
**Tiempo**: 3-4 minutos  
**Complejidad**: TRIVIAL  

---

### 3. TIPO 3 - Títulos indentados (ANALIZAR PRIMERO)

**Archivos**:
- workflow_general.rst (2 CRITICAL - líneas 3080, 3083)

**Total**: 2 CRITICAL  
**Tiempo**: Pendiente análisis  
**Acción**: Verificar contexto antes de corregir

---

### 4. TIPO 1 - Code-block sin indentar (COMPLEJO)

**Archivos**:
- error_01_omisiones.rst (22 CRITICAL)

**Total**: 22 CRITICAL  
**Tiempo**: 30-40 minutos  
**Complejidad**: MODERADA (muchas líneas)  
**Estrategia**: Indentar bloques de código +2 espacios

---

## 📊 ESTADÍSTICAS FINALES

### Por Complejidad

| Complejidad | CRITICAL | % Total | Tiempo |
|-------------|----------|---------|--------|
| TRIVIAL | 8 | 26% | ~10 min |
| MODERADA | 22 | 71% | ~40 min |
| PENDIENTE | 1 | 3% | ? |

### Por Estrategia

| Estrategia | CRITICAL | Descripción |
|------------|----------|-------------|
| Eliminar líneas | 3 | Quitar underlines de toctree |
| Alinear/Indentar | 6 | Corregir indentación |
| Indentar bloque | 22 | Indentar code-blocks |

---

## ✅ CONCLUSIÓN

**Confirmado**: NO todos los CRITICAL son el mismo problema.

**Patrones identificados**: 3 tipos distintos

**Recomendación**:
1. ✅ Empezar con TIPO 2 y 3 (quick wins, 10 min total)
2. ✅ Analizar TIPO 3 pendientes (workflow 3080, 3083)
3. ✅ Terminar con TIPO 1 (code-block, 40 min)

**Tiempo total estimado**: ~50-60 minutos para los 31 CRITICAL

---

**Próximo paso**: ¿Empezamos con quick wins (TIPO 2 - toctrees)?
