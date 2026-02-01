# Flujo Metodológico Correcto - Corrección Incremental

**Basado en**: incremental-correction-methodology v1.3.0  
**Actualizado**: 2026-02-01 con convención de nombres  
**Versión anterior**: 2026-01-31 con lección aprendida

---

## 📝 CONVENCIÓN DE NOMBRES

**NUEVO (2026-02-01)**: Todos los archivos creados deben seguir convención específica.

**Ver documentación completa**: `CONVENCION_NOMBRES.md`

**Regla de Oro**:
> El nombre del archivo debe responder: "¿QUÉ es esto y de QUÉ trata?"

**Formato general**:
```
<TIPO>_<CONTEXTO_ESPECIFICO>_<VERSION>.<ext>
```

**Patrones principales por tipo**:
- **Fases**: `FASE<N>_<NOMBRE>.md`
- **Análisis**: `ANALISIS_<TIPO>_<contexto>.md`
- **Scripts**: `SCRIPT_<ACCION>_<nombre_script>.md`
- **Errores**: `ERROR_<descripcion_especifica>.md`
- **Decisiones**: `DECISIONES.md` o `DECISIONES_<contexto>.md`

---

## FLUJO COMPLETO

```
FASE 0: PREPARACIÓN (15-20 min)
├── Leer incremental-correction-methodology COMPLETO
├── Leer skill(s) específico(s) del dominio (ej: sphinx-expert)
├── Identificar skills complementarios
├── Crear directorio de trabajo
├── Verificar git status limpio
└── Checklist 8/8 ✅
    ↓
FASE 1: ANÁLISIS INICIAL (30-45 min)
├── Build/análisis inicial (make clean && make html)
├── Extracción de issues (grep WARNING/ERROR/CRITICAL)
├── Categorización automática (sort | uniq -c)
└── Análisis de distribución
    ↓
GENERAR DOCUMENTO: ANALISIS_COMPLETO_BUILD.md ⚠️ OBLIGATORIO
├── Conteo total de issues
├── Análisis CRITICAL (archivos afectados, distribución, detalles)
├── Análisis ERROR (archivos afectados, distribución, detalles)
├── Análisis WARNING (categorización, archivos, distribución)
├── Resumen consolidado
├── Conclusiones y recomendaciones
└── Archivos de referencia y comandos útiles
    ↓
FASE 2: CATEGORIZACIÓN (15-20 min) ← Basada en ANALISIS
├── Agrupar issues similares (usando datos del ANALISIS)
├── Asignar complejidad (TRIVIAL/MODERADO/COMPLEJO)
├── Evaluar riesgo automatización (BAJO/MEDIO/ALTO)
├── Definir estrategia (Manual/Script/Híbrido)
└── Identificar procedimientos disponibles
    ↓
FASE 3: PRIORIZACIÓN (5-10 min)
├── Aplicar criterios (Facilidad > Cantidad, CRITICAL > ERROR > WARNING)
├── Identificar quick wins
├── Definir orden de ejecución
└── Estimar tiempo por categoría
    ↓
FASE 4: EJECUCIÓN INCREMENTAL
├── Aplicar 8 Protecciones Obligatorias
├── Un archivo a la vez (o lotes pequeños)
├── Commit después de cada archivo/lote
├── Validar que issues disminuyen
└── Documentar decisiones
```

---

## ⚠️ REGLA CRÍTICA AÑADIDA

**FASE 2 NO PUEDE EJECUTARSE SIN ANALISIS_COMPLETO_BUILD.md**

### Por Qué Es Crítico

**Problema observado** (sesión 2026-01-31):
- FASE 2 original usó estimaciones: "~5-6 archivos", "Muchos archivos"
- Resultado: Números incorrectos, priorización subóptima
- Causa raíz: Categorizar sin datos reales

**Solución implementada**:
- FASE 1 → Genera ANALISIS_COMPLETO_BUILD.md PRIMERO
- ANALISIS contiene TODOS los archivos, distribución exacta, concentración medida
- FASE 2 usa datos del ANALISIS (no estimaciones)

### Qué Debe Contener ANALISIS_COMPLETO_BUILD.md

**Mínimo obligatorio**:
1. ✅ Conteo total (WARNING/ERROR/CRITICAL)
2. ✅ Listado COMPLETO de archivos afectados por cada categoría
3. ✅ Distribución de issues por archivo (ej: cuántos CRITICAL en cada archivo)
4. ✅ Detalles completos de cada issue (ubicación, tipo)
5. ✅ Archivos con concentración alta (ej: 61% en workflow_general.rst)
6. ✅ Resumen consolidado y estadísticas

**Sin este documento**: FASE 2 será imprecisa → FASE 3 será incorrecta → FASE 4 será ineficiente

---

## DIFERENCIAS: ANTES vs AHORA

### ANTES (Flujo incorrecto)

```
FASE 1: Análisis Inicial
    ↓
FASE 2: Categorización (con estimaciones)
    ↓
FASE 3: Priorización
```

**Problema**:
- FASE 2 usa "~5 archivos", "muchos archivos"
- No hay datos exactos de distribución
- No se identifica concentración

### AHORA (Flujo correcto)

```
FASE 1: Análisis Inicial
    ↓
GENERAR: ANALISIS_COMPLETO_BUILD.md (con TODOS los datos)
    ↓
FASE 2: Categorización (basada en ANALISIS)
    ↓
FASE 3: Priorización
```

**Mejora**:
- FASE 2 usa datos reales: "5 archivos exactos"
- Distribución medida: "61% en workflow_general.rst"
- Concentración identificada: permite priorizar mejor

---

## EJEMPLO REAL DE LA DIFERENCIA

### CATEGORÍA: Section Structure (CRITICAL)

**SIN ANALISIS (estimación)**:
```markdown
**Archivos afectados**: 5
**Distribución**: No conocida
**Estrategia**: Manual puro
```

**CON ANALISIS (datos reales)**:
```markdown
**Archivos afectados**: 5 archivos exactos:
- workflow_general.rst: 19 issues (61%)
- WORKFLOW_v1_6_0_ACTUALIZACION.rst: 3 issues
- guia_rapida.rst: 3 issues
- GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst: 3 issues
- error_01_omisiones.rst: 3 issues

**Concentración**: 61% en 1 archivo
**Implicación**: Corregir workflow_general.rst primero = máximo impacto
**Estrategia**: Manual puro, empezar por archivo con 19 issues
```

**Impacto**: Con datos reales, sabemos que corregir 1 archivo resuelve 61% del problema.

---

## VALIDACIÓN DEL FLUJO

### Checklist ANTES de FASE 2

```
□ FASE 0 completada (8/8 checklist)
□ FASE 1 completada (análisis inicial)
□ ANALISIS_COMPLETO_BUILD.md existe
□ ANALISIS contiene archivos exactos por categoría
□ ANALISIS contiene distribución por archivo
□ ANALISIS identifica concentración
□ ANALISIS tiene resumen consolidado
```

**Adhesión mínima**: 7/7 (100%)

Si NO cumples 100%, **NO procedas a FASE 2**.

---

## COMANDOS DE VALIDACIÓN

### Verificar que ANALISIS existe y está completo

```bash
cd /tmp/ADT/.mywork/changes/TIMESTAMP

# 1. Verificar que existe
ls -lh ANALISIS_COMPLETO_BUILD.md

# 2. Verificar secciones mínimas
grep "^## " ANALISIS_COMPLETO_BUILD.md

# 3. Verificar que tiene archivos listados
grep -c "source.*\.rst" ANALISIS_COMPLETO_BUILD.md

# 4. Verificar que tiene distribución
grep -c "issues" ANALISIS_COMPLETO_BUILD.md
```

**Output esperado**:
- Archivo existe (>500 líneas típicamente)
- Al menos 6 secciones principales
- Múltiples archivos listados
- Estadísticas de distribución presentes

### Verificar archivos de datos generados

```bash
# Deben existir estos archivos de FASE 1
ls -1 *.txt *.tmp

# Esperado:
# critical.txt
# errors.txt
# warnings.txt
# critical_files.tmp
# error_files.tmp
# headers_files.tmp
# blanklines_files.tmp
# lexers_files.tmp
```

---

## ANTI-PATRÓN DOCUMENTADO

### ❌ Anti-Patrón: "Categorizar Sin Análisis Completo"

**Error cometido**: 2026-01-31 durante FASE 2 inicial

**Síntoma**:
- FASE 2 usa estimaciones: "~5 archivos"
- No tiene datos de distribución
- No identifica concentración
- Usa "muchos archivos" sin conteo

**Causa raíz**:
- Saltar directamente de FASE 1 a FASE 2
- No generar documento ANALISIS intermedio
- Asumir que "ya tenemos los datos"

**Consecuencia**:
- Categorización imprecisa
- Priorización subóptima
- Estimaciones incorrectas
- Plan de ejecución ineficiente

**Corrección**:
```bash
# ❌ MAL: FASE 1 → FASE 2 directo
fase1_analisis_inicial()
categorizar_issues()  # Usa estimaciones

# ✅ BIEN: FASE 1 → ANALISIS → FASE 2
fase1_analisis_inicial()
generar_analisis_completo()  # Documento con TODOS los datos
categorizar_issues()  # Usa datos del ANALISIS
```

**Lección**:
> 📊 **No puedes categorizar lo que no has medido completamente**
>
> FASE 2 requiere datos EXACTOS, no estimaciones.
> El documento ANALISIS_COMPLETO es el puente entre FASE 1 y FASE 2.

**Validación**:
- ✅ FASE2_CATEGORIZACION_V2.md usa datos reales del ANALISIS
- ✅ Incluye archivos exactos, distribución, concentración
- ✅ Hallazgos del ANALISIS incorporados

---

## TIEMPO ESTIMADO POR FASE (Actualizado)

| Fase | Actividad | Tiempo | Output |
|------|-----------|--------|--------|
| 0 | Preparación | 15-20 min | Checklist 8/8, git limpio |
| 1 | Análisis Inicial | 30-45 min | critical.txt, errors.txt, warnings.txt |
| **1.5** | **Generar ANALISIS** | **15-20 min** | **ANALISIS_COMPLETO_BUILD.md** |
| 2 | Categorización | 15-20 min | FASE2_CATEGORIZACION.md (con datos reales) |
| 3 | Priorización | 5-10 min | PLAN.md con orden y estimaciones |
| 4 | Ejecución | Variable | Commits, correcciones |

**Total preparación**: 80-115 min (ANTES de empezar correcciones)

**ROI**: Validado en sesión 2026-01-31
- Con preparación completa: 0 errores, plan correcto
- Sin preparación: 4 errores, 70 min perdidos

---

## TEMPLATE DE VERIFICACIÓN

Antes de proceder de FASE 1 a FASE 2, ejecutar:

```bash
#!/bin/bash
# verificar_antes_fase2.sh

echo "=== VERIFICACIÓN PRE-FASE 2 ==="
echo ""

# 1. Verificar ANALISIS existe
if [ ! -f "ANALISIS_COMPLETO_BUILD.md" ]; then
    echo "❌ BLOQUEADOR: ANALISIS_COMPLETO_BUILD.md NO EXISTE"
    echo "   Debes generar el análisis completo primero"
    exit 1
fi

# 2. Verificar tamaño mínimo
LINES=$(wc -l < ANALISIS_COMPLETO_BUILD.md)
if [ "$LINES" -lt 500 ]; then
    echo "❌ BLOQUEADOR: ANALISIS muy corto ($LINES líneas)"
    echo "   Análisis completo debe tener >500 líneas"
    exit 1
fi

# 3. Verificar secciones
SECTIONS=$(grep -c "^## " ANALISIS_COMPLETO_BUILD.md)
if [ "$SECTIONS" -lt 6 ]; then
    echo "❌ BLOQUEADOR: Faltan secciones ($SECTIONS/6 mínimo)"
    exit 1
fi

# 4. Verificar archivos de datos
for f in critical.txt errors.txt warnings.txt; do
    if [ ! -f "$f" ]; then
        echo "❌ BLOQUEADOR: Falta $f"
        exit 1
    fi
done

echo "✅ Todas las verificaciones pasaron"
echo "✅ Listo para proceder a FASE 2"
exit 0
```

---

## RESUMEN

**Nueva regla del flujo**:
```
FASE 1 (Análisis) → GENERAR ANALISIS_COMPLETO → FASE 2 (Categorización)
                          ↑
                    OBLIGATORIO
```

**Sin el ANALISIS_COMPLETO**:
- ❌ No puedes categorizar correctamente
- ❌ No puedes priorizar óptimamente
- ❌ No puedes estimar realísticamente

**Con el ANALISIS_COMPLETO**:
- ✅ Categorización basada en datos reales
- ✅ Priorización con concentración medida
- ✅ Estimaciones precisas
- ✅ Plan de ejecución óptimo

**Tiempo de inversión**: +15-20 min generar ANALISIS  
**ROI**: Ahorro de horas en ejecución ineficiente + 0 errores

---

**Fecha**: 2026-01-31  
**Validado en**: Sesión 20260131-230456  
**Metodología**: incremental-correction-methodology v1.2.0  
**Próxima actualización**: Cuando se identifique otra mejora del flujo
