# Revisión de Anti-Patrones Antes de FASE 3

**Fecha**: 2026-01-31 23:40  
**Contexto**: Antes de proceder a FASE 3 (Priorización)  
**Objetivo**: Verificar que NO estoy cometiendo ninguno de los 6 anti-patrones

---

## ANTI-PATRÓN 1: Scripts Sin Validación

**Qué es**: Ejecutar scripts que modifican archivos sin validación previa.

**Aplica a FASE 3**: ❌ NO
- FASE 3 es solo planificación (no ejecuta cambios)
- No hay scripts involucrados
- No se modifican archivos

**Estado**: ✅ NO APLICA (FASE 3 es solo decisión)

---

## ANTI-PATRÓN 2: Batch Masivo

**Qué es**: Modificar muchos archivos a la vez sin control.

**Aplica a FASE 3**: ❌ NO
- FASE 3 solo define ORDEN de ejecución
- No ejecuta cambios
- La ejecución será en FASE 4 (un archivo a la vez)

**Estado**: ✅ NO APLICA (FASE 3 es solo planificación)

---

## ANTI-PATRÓN 3: Asumir que Menos Issues = Mejor

**Qué es**: Medir éxito solo por reducción de conteo sin verificar nuevos issues.

**Aplica a FASE 3**: ⚠️ INDIRECTAMENTE
- FASE 3 decide QUÉ corregir y CUÁNDO
- Si priorizamos mal, podríamos corregir issues que introducen otros
- **Contramedida**: Priorizar según riesgo y procedimientos disponibles

**Cómo prevenirlo en FASE 3**:
1. ✅ Priorizar CRITICAL > ERROR > WARNING (gravedad)
2. ✅ Priorizar issues con procedimientos documentados (menos riesgo)
3. ✅ Evitar categorías de alto riesgo sin procedimientos
4. ✅ Planear validación (build) después de cada corrección

**Estado**: ✅ PREVENIDO (aplicando criterios de riesgo)

---

## ANTI-PATRÓN 4: No Documentar Decisiones

**Qué es**: No documentar el POR QUÉ de las decisiones tomadas.

**Aplica a FASE 3**: ✅ SÍ - MUY RELEVANTE
- FASE 3 toma decisiones críticas de priorización
- Estas decisiones afectan todo FASE 4
- **DEBO** documentar POR QUÉ priorizo en cierto orden

**Cómo prevenirlo en FASE 3**:
1. ✅ Documentar criterios de priorización
2. ✅ Explicar POR QUÉ cada categoría va en su orden
3. ✅ Documentar trade-offs considerados
4. ✅ Documentar en DECISIONES.md

**Estado**: ⚠️ REQUIERE ATENCIÓN (debo documentar decisiones)

**Acción**: Crear/actualizar DECISIONES.md durante FASE 3

---

## ANTI-PATRÓN 5: Empezar Sin Leer la Metodología

**Qué es**: No leer la metodología antes de empezar.

**Aplica a FASE 3**: ✅ SÍ
- Estoy leyendo anti-patrones AHORA ✅
- Ya leí incremental-correction-methodology en FASE 0 ✅
- Estoy verificando ANTES de actuar ✅

**Checklist de prevención**:
```
✅ ¿Leí incremental-correction-methodology COMPLETO? → SÍ (FASE 0)
✅ ¿Leí skill(s) del dominio COMPLETO(s)? → SÍ (sphinx-expert)
✅ ¿Entiendo las 8 Protecciones? → SÍ
✅ ¿Conozco los 6 Anti-patrones? → REVISANDO AHORA
✅ ¿Identifiqué skills complementarios? → SÍ
```

**Estado**: ✅ PREVENIDO (estoy siguiendo el proceso correcto)

**Evidencia**: Usuario pidió revisar anti-patrones ANTES de FASE 3 → Aplicando Protección #0

---

## ANTI-PATRÓN 6: Categorizar Sin Análisis Completo

**Qué es**: Hacer FASE 2 sin generar ANALISIS_COMPLETO primero.

**Aplica a FASE 3**: ⚠️ INDIRECTAMENTE
- Ya evitamos este anti-patrón en FASE 2 ✅
- Pero FASE 3 depende de datos de ANALISIS_COMPLETO
- **DEBO** usar datos del análisis, no estimaciones

**Cómo prevenirlo en FASE 3**:
1. ✅ Usar ANALISIS_COMPLETO_BUILD.md como fuente
2. ✅ Usar FASE2_CATEGORIZACION_V2.md (con datos reales)
3. ✅ NO usar estimaciones o suposiciones
4. ✅ Referenciar concentración identificada (61% en workflow_general.rst)

**Checklist de verificación**:
```
✅ ¿Tengo ANALISIS_COMPLETO_BUILD.md? → SÍ (793 líneas)
✅ ¿Tengo FASE2_CATEGORIZACION_V2.md? → SÍ (423 líneas)
✅ ¿Conozco archivos exactos afectados? → SÍ
✅ ¿Conozco distribución por archivo? → SÍ
✅ ¿Conozco concentración? → SÍ (61% en workflow_general.rst)
✅ ¿Tengo intersección CRITICAL+ERROR? → SÍ (3 archivos)
```

**Estado**: ✅ PREVENIDO (tengo todos los datos necesarios)

---

## ANTI-PATRONES ESPECÍFICOS DE PRIORIZACIÓN

### Riesgos específicos en FASE 3:

1. **Priorizar por cantidad en vez de impacto**
   - ❌ MAL: "Headers (309) antes que CRITICAL (31)" → más issues no = más importante
   - ✅ BIEN: "CRITICAL primero" → gravedad > cantidad

2. **Ignorar concentración**
   - ❌ MAL: Distribuir esfuerzo en 5 archivos equitativamente
   - ✅ BIEN: Corregir workflow_general.rst (61% CRITICAL) primero

3. **Ignorar riesgo de automatización**
   - ❌ MAL: Scripts para todo (headers, section structure, etc.)
   - ✅ BIEN: Manual para COMPLEJO, script solo para TRIVIAL con procedimiento

4. **No considerar dependencias**
   - ❌ MAL: Corregir WARNING antes que ERROR que podrían causar esos WARNING
   - ✅ BIEN: CRITICAL → ERROR → WARNING (gravedad)

5. **No considerar procedimientos disponibles**
   - ❌ MAL: Empezar por categoría sin procedimiento documentado
   - ✅ BIEN: Priorizar categorías con procedimientos en sphinx-expert

6. **No documentar criterios**
   - ❌ MAL: "Hago esto porque sí"
   - ✅ BIEN: "Priorizo CRITICAL primero porque: gravedad, bloquea build, etc."

---

## CRITERIOS DE PRIORIZACIÓN CORRECTOS

Basado en la metodología, debo aplicar:

### Criterio 1: Gravedad (CRÍTICO)
```
CRITICAL > ERROR > WARNING
```
**Razón**: CRITICAL bloquea build correcto

### Criterio 2: Facilidad (Momentum psicológico)
```
TRIVIAL > MODERADO > COMPLEJO
```
**Razón**: Quick wins generan momentum

### Criterio 3: Riesgo
```
BAJO riesgo automatización > MEDIO > ALTO
```
**Razón**: Evitar introducir regresiones

### Criterio 4: Concentración (NUEVO desde v1.3.0)
```
Archivos con alta concentración PRIMERO
```
**Razón**: workflow_general.rst tiene 61% CRITICAL → máximo impacto

### Criterio 5: Procedimientos
```
Con procedimiento documentado > Sin procedimiento
```
**Razón**: Menos riesgo, más eficiencia

### Criterio 6: Dependencias
```
Errores que causan otros > Errores independientes
```
**Razón**: Resolver causa resuelve efectos

---

## DECISIONES PREVIAS A FASE 3

### ¿Qué DEBO decidir en FASE 3?

1. **Orden de categorías** (basado en criterios arriba)
2. **Estrategia por categoría** (manual vs script)
3. **Agrupación de correcciones** (un archivo vs lotes)
4. **Criterio de "done"** (cuándo parar)
5. **Plan de validación** (cuándo hacer build)

### ¿Qué NO debo decidir en FASE 3?

1. ❌ Cómo corregir específicamente cada issue (eso es FASE 4)
2. ❌ Empezar a corregir (eso es FASE 4)
3. ❌ Modificar archivos (eso es FASE 4)

---

## CHECKLIST PRE-FASE 3

```
PREREQUISITOS:
✅ FASE 0 completada (8/8)
✅ FASE 1 completada
✅ ANALISIS_COMPLETO_BUILD.md generado (793 líneas)
✅ FASE 2 completada (V2 con datos reales)
✅ Anti-patrones revisados
✅ Criterios de priorización claros
✅ DECISIONES.md listo para documentar

VERIFICACIÓN DE ANTI-PATRONES:
✅ Anti-Patrón 1: No aplica (no hay scripts en FASE 3)
✅ Anti-Patrón 2: No aplica (no hay batch en FASE 3)
✅ Anti-Patrón 3: Prevenido (aplicando criterios de riesgo)
✅ Anti-Patrón 4: Requiere atención (debo documentar decisiones)
✅ Anti-Patrón 5: Prevenido (estoy leyendo metodología)
✅ Anti-Patrón 6: Prevenido (tengo ANALISIS_COMPLETO)

DATOS DISPONIBLES:
✅ Conteo total: 661 issues
✅ Archivos exactos por categoría
✅ Distribución por archivo
✅ Concentración: 61% CRITICAL en workflow_general.rst
✅ Intersección CRITICAL+ERROR: 3 archivos
✅ Procedimientos disponibles: 4 en sphinx-expert

LISTO PARA FASE 3: SÍ ✅
```

---

## COMPROMISO PARA FASE 3

Durante FASE 3 me comprometo a:

1. ✅ Aplicar los 6 criterios de priorización
2. ✅ Usar datos del ANALISIS_COMPLETO (no estimaciones)
3. ✅ Documentar TODAS las decisiones en DECISIONES.md
4. ✅ Explicar el POR QUÉ de cada decisión
5. ✅ Considerar riesgo de automatización
6. ✅ Priorizar concentración (workflow_general.rst)
7. ✅ NO empezar ejecución (eso es FASE 4)
8. ✅ Presentar plan al usuario para validación

---

**Revisión completada**: 2026-01-31 23:45  
**Anti-patrones identificados**: 6  
**Anti-patrones aplicables a FASE 3**: 2 (requieren atención)  
**Anti-patrones prevenidos**: 6/6 ✅

**LISTO PARA PROCEDER A FASE 3: SÍ** ✅
