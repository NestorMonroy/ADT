# ANÁLISIS CRÍTICO: Script fix_critical_titles.sh Dañó Archivos Correctos

**Fecha**: 2026-02-01 02:25  
**Severidad**: 🚨 CRÍTICO  
**Archivos afectados**: 5 de 6 (dañados incorrectamente)  
**Status**: ❌ REVERTIR CAMBIOS NECESARIO

---

## 🚨 RESUMEN EJECUTIVO

El script `fix_critical_titles.sh` modificó contenido que estaba DENTRO de bloques `code-block`, removiendo espacios que eran **parte de ejemplos de código** mostrados al lector.

**Impacto**: 5 archivos dañados, 1 archivo corregido correctamente.

---

## 📊 ANÁLISIS POR ARCHIVO

### Archivo 1: error_01_omisiones.rst ❌ DAÑADO

**Líneas modificadas**: 154-178, 431-503 (24 títulos)

**Contexto ANTES del cambio**:
```rst
.. code-block:: rst




 7. Vista de Despliegue
=======================

 Introducción
 =============
 [Traducido]
```

**Contexto DESPUÉS del cambio**:
```rst
.. code-block:: rst




7. Vista de Despliegue         ← ❌ Removió espacios del EJEMPLO
=======================

Introducción                   ← ❌ Removió espacios del EJEMPLO
=============
[Traducido]
```

**Problema**: Los espacios eran PARTE del ejemplo de código RST mostrado al lector.

**Impacto**: El ejemplo ahora muestra código **incorrectamente formateado**.

---

### Archivo 2: metodo_por_defecto.rst ❌ DAÑADO

**Líneas modificadas**: 436, 471 (2 títulos)

**Contexto**:
```rst
.. code-block:: rst

 Introducción        ← Espacio es parte del EJEMPLO
 ============
```

**DESPUÉS**:
```rst
.. code-block:: rst

Introducción         ← ❌ Removió espacios del EJEMPLO
============
```

**Problema**: Igual que archivo 1 - espacios eran parte del ejemplo.

---

### Archivo 3: workflow_general.rst ✅ CORREGIDO (ÚNICO CASO VÁLIDO)

**Líneas modificadas**: 3406, 3408 (2 títulos)

**Contexto**:
```rst
 .. toctree::
 :maxdepth: 1

 tip_1

 tip_2              ← Espacio inicial INCORRECTO (fuera de toctree)
 ======
 tip_N              ← Espacio inicial INCORRECTO
 ======
```

**DESPUÉS**:
```rst
tip_2               ← ✅ Espacios removidos correctamente
======
tip_N               ← ✅ Espacios removidos correctamente
======
```

**Problema**: Este era un ERROR real de formato RST.

**Impacto**: ✅ CORRECCIÓN VÁLIDA (pero underlines tienen 1 `=` de más)

---

### Archivo 4: guia_rapida.rst ❌ DAÑADO

**Líneas modificadas**: 306 (1 título)

**Contexto**:
```rst
.. code-block:: rst




 Mantén la Simplicidad
======================

...

 Comparación         ← Espacio es parte del EJEMPLO
 ============
```

**DESPUÉS**:
```rst
Comparación          ← ❌ Removió espacios del EJEMPLO
============
```

**Problema**: Espacios eran parte del ejemplo de código.

---

### Archivo 5: index.rst ❌ DAÑADO

**Líneas modificadas**: 192 (1 título)

**Contexto**:
```rst
.. code-block:: text

 FUNDAMENTOS ADT     ← Espacio es parte del EJEMPLO
 ================
```

**DESPUÉS**:
```rst
.. code-block:: text

FUNDAMENTOS ADT      ← ❌ Removió espacios del EJEMPLO
================
```

**Problema**: Espacios eran parte del ejemplo.

---

### Archivo 6: seccion_1_2_quality_goals.rst ❌ DAÑADO

**Líneas modificadas**: 82 (1 título)

**Contexto**:
```rst
.. code-block:: rst

 1.2 Atributos de Calidad Objetivo   ← Espacio es parte del EJEMPLO
 ==================================
```

**DESPUÉS**:
```rst
.. code-block:: rst

1.2 Atributos de Calidad Objetivo    ← ❌ Removió espacios del EJEMPLO
==================================
```

**Problema**: Espacios eran parte del ejemplo.

---

## 📊 RESUMEN DE IMPACTO

| Archivo | Títulos | Dentro de code-block | Corrección | Status |
|---------|---------|---------------------|------------|--------|
| error_01_omisiones.rst | 24 | ✅ SÍ | ❌ INCORRECTA | DAÑADO |
| metodo_por_defecto.rst | 2 | ✅ SÍ | ❌ INCORRECTA | DAÑADO |
| workflow_general.rst | 2 | ❌ NO | ✅ CORRECTA* | OK* |
| guia_rapida.rst | 1 | ✅ SÍ | ❌ INCORRECTA | DAÑADO |
| index.rst | 1 | ✅ SÍ | ❌ INCORRECTA | DAÑADO |
| seccion_1_2_quality_goals.rst | 1 | ✅ SÍ | ❌ INCORRECTA | DAÑADO |

**Total**: 
- ❌ Archivos dañados: 5 (29 títulos incorrectamente modificados)
- ✅ Archivos corregidos: 1 (2 títulos, pero con underlines con 1 `=` de más)

\* workflow_general.rst tiene corrección válida pero underlines tienen longitud incorrecta.

---

## 🔍 CAUSA RAÍZ DEL ERROR

### El Script NO Verificó Contexto

```bash
detect_issues() {
    local file="$1"
    
    # Find lines where:
    # - Current line starts with space + letter/number
    # - Next line starts with space + equals signs
    awk '
        /^ [A-Za-z0-9]/ {
            title_line = NR
            title = $0
            getline
            if (/^ =+$/) {
                print title_line
            }
        }
    ' "$file"
}
```

**Problema**: El regex busca cualquier línea con espacios iniciales, **SIN verificar**:
- ❌ Si está dentro de un `code-block`
- ❌ Si está dentro de un `literal block`
- ❌ Si es parte de contenido indentado válido
- ❌ El contexto estructural RST

**Resultado**: Modificó código de EJEMPLOS que estaban correctos.

---

## ⚠️ ANTI-PATRÓN COMETIDO

**Anti-patrón**: "Corregir Con Regex Sin Entender Contexto RST"

**Síntomas**:
1. ✅ Script detecta patrón (espacio + título)
2. ❌ Script NO verifica contexto estructural
3. ❌ Script NO distingue código real vs ejemplo
4. ❌ Script aplica cambios indiscriminadamente

**Lección**: 
> **RST es un lenguaje estructurado**. No se puede corregir con simples búsquedas de patrones. 
> Necesitas parsear la estructura para entender el contexto.

---

## 🎯 ACCIÓN REQUERIDA

### OPCIÓN A: Revertir TODO ⭐ RECOMENDADO

```bash
# Revertir los 6 archivos
git restore source/01_fundamentos/_metodologias/metodo_por_defecto.rst
git restore source/01_fundamentos/index.rst
git restore source/02_procedimientos/workflow_general.rst
git restore source/06_casos_practicos/errores_comunes/error_01_omisiones.rst
git restore source/07_guias_uso/guia_rapida.rst
git restore source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/traduccion/seccion_1_2_quality_goals.rst
```

**Justificación**:
- 5 archivos están dañados
- 1 archivo tiene corrección parcial (underlines incorrectos)
- NO vale la pena mantener 1 corrección parcial a costa de 5 archivos dañados

---

### OPCIÓN B: Revertir 5, Mantener 1

```bash
# Revertir los 5 dañados
git restore source/01_fundamentos/_metodologias/metodo_por_defecto.rst
git restore source/01_fundamentos/index.rst
git restore source/06_casos_practicos/errores_comunes/error_01_omisiones.rst
git restore source/07_guias_uso/guia_rapida.rst
git restore source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/traduccion/seccion_1_2_quality_goals.rst

# Mantener workflow_general.rst (luego corregir underlines manualmente)
```

**Luego corregir workflow_general.rst**:
```bash
# Línea 3407: tip_2
# Cambiar: ====== (6 signos) → ===== (5 signos)

# Línea 3409: tip_N
# Cambiar: ====== (6 signos) → ===== (5 signos)
```

---

### OPCIÓN C: Mantener TODO y Revertir Code-Blocks Manualmente

**NO RECOMENDADO** - Demasiado trabajo manual para revertir 29 títulos en 5 archivos.

---

## 📋 RECOMENDACIÓN FINAL

**OPCIÓN A**: Revertir TODO

**Razones**:
1. Script dañó más de lo que arregló (5 dañados vs 1 corregido)
2. La corrección parcial (workflow_general.rst) tiene problemas de underlines
3. Los archivos originales estaban CORRECTOS
4. Es más rápido revertir y empezar de cero

**Próximos pasos después de revertir**:
1. Hacer `make clean && make html` 
2. Ver QUÉ reporta Sphinx como CRITICAL/ERROR
3. Analizar CONTEXTO de cada error reportado
4. Decidir correcciones basadas en errores REALES de Sphinx

---

## 🔧 LECCIÓN PARA FUTURO SCRIPT

Si se crea un script de corrección RST:

1. ✅ Parsear estructura RST (no solo regex)
2. ✅ Detectar bloques (code-block, literal-block, etc.)
3. ✅ Ignorar contenido dentro de bloques
4. ✅ Verificar contexto antes de modificar
5. ✅ Dry-run con análisis de contexto visible
6. ✅ Verificar con `make html` ANTES de script

---

**Status**: 🚨 CRÍTICO - REQUIERE REVERSIÓN  
**Decisión pendiente**: Usuario debe elegir Opción A o B  
**Fecha**: 2026-02-01 02:25
