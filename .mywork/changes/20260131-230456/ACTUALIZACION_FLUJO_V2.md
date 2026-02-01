# Actualización FLUJO_METODOLOGICO.md → V2.0

**Fecha**: 2026-02-01 01:20  
**Cambio**: Integración completa de convención de nombres  
**Versión**: 2.0 (anteriormente v1.3.0)

---

## 🎯 QUÉ SE ACTUALIZÓ

El **FLUJO_METODOLOGICO.md** ahora incluye:

1. ✅ Convención de nombres en la introducción
2. ✅ Archivos específicos a crear en CADA fase
3. ✅ Templates para cada tipo de archivo
4. ✅ Checklist de verificación de nombres
5. ✅ Ejemplos completos de sesión
6. ✅ Flujo visual con archivos
7. ✅ Referencias cruzadas a CONVENCION_NOMBRES.md y README.md

---

## 📊 COMPARACIÓN: V1 vs V2

### ANTES (V1.3.0)

```
FASE 0: PREPARACIÓN
├── Leer metodología
├── Crear directorio
└── Checklist 8/8
```

**Problema**: No especifica QUÉ archivos crear ni CÓMO nombrarlos.

---

### AHORA (V2.0)

```
FASE 0: PREPARACIÓN (15-20 min)
├── Crear: PLAN.md (obligatorio)
├── Crear: DECISIONES.md (obligatorio)
├── Crear: TRACKING.md (obligatorio)
├── Opcional: FASE0_PREPARACION.md
├── Leer: incremental-correction-methodology COMPLETO
└── Checklist 8/8 ✅
```

**Mejora**: Especifica archivos exactos con nombres correctos.

---

## 🆕 NUEVAS SECCIONES AGREGADAS

### 1. Convención de Nombres (Introducción)

```markdown
## 📝 CONVENCIÓN DE NOMBRES

**Regla de Oro**:
> El nombre del archivo debe responder: "¿QUÉ es esto y de QUÉ trata?"

**Formato**:
<TIPO>_<CONTEXTO_ESPECIFICO>_<VERSION>.<ext>

**Patrones**:
- Fases: FASE<N>_<NOMBRE>.md
- Análisis: ANALISIS_<TIPO>_<contexto>.md
- Scripts: SCRIPT_<ACCION>_<nombre_script>.md
...
```

---

### 2. Archivos por Fase (Detallado)

Cada fase ahora tiene:

**Para CADA FASE**:
- Archivos OBLIGATORIOS listados
- Archivos OPCIONALES listados
- Templates completos
- Ejemplos de nombres correctos
- Comandos de validación

**Ejemplo - FASE 1.5**:

```markdown
### FASE 1.5: ANÁLISIS COMPLETO ⚠️ OBLIGATORIO

**Archivo OBLIGATORIO**:
**`ANALISIS_COMPLETO_BUILD.md`**

**Tamaño esperado**: >500 líneas

**Estructura mínima**:
[Template completo con 8 secciones]

**Validación**:
wc -l ANALISIS_COMPLETO_BUILD.md  # >500
grep "^## " ANALISIS_COMPLETO_BUILD.md | wc -l  # >=6
```

---

### 3. Templates Integrados

**Templates incluidos para**:
- PLAN.md
- DECISIONES.md
- TRACKING.md
- ANALISIS_COMPLETO_BUILD.md
- FASE2_CATEGORIZACION.md
- FASE3_PRIORIZACION.md
- SCRIPT_RESUMEN_*.md
- ERROR_*.md
- ANALISIS_*.md
- RESUMEN_SESION.md

Cada template muestra:
- Estructura completa
- Secciones obligatorias
- Formato esperado
- Ejemplos

---

### 4. Checklist de Nombres

```markdown
## ✅ CHECKLIST DE NOMBRES

□ ¿Incluye TIPO al inicio?
□ ¿Incluye CONTEXTO específico?
□ ¿Si hay versiones, está marcada?
□ ¿Es claro qué contiene sin abrirlo?
□ ¿Sigue formato <TIPO>_<CONTEXTO>_<VERSION>?
□ ¿Evita nombres genéricos?
□ ¿Usa extensión correcta?
```

---

### 5. Ejemplo Completo de Sesión

```
.mywork/changes/20260131-230456/
├── PLAN.md
├── DECISIONES.md
├── TRACKING.md
├── ANALISIS_COMPLETO_BUILD.md
├── FASE2_CATEGORIZACION_V2.md
├── FASE3_PRIORIZACION.md
├── SCRIPT_RESUMEN_fix_critical_titles.md
├── SCRIPT_DRY_RUN_fix_critical_titles.txt
├── ANALISIS_CRITICAL_error_01_omisiones.md
├── ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md
└── RESUMEN_SESION.md
```

Con explicación de cada archivo.

---

### 6. Flujo Visual con Archivos

```
┌─────────────────────────────────────────────┐
│ FASE 0: PREPARACIÓN                         │
│ Crear: PLAN.md, DECISIONES.md, TRACKING.md │
└─────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────┐
│ FASE 1: ANÁLISIS INICIAL                    │
│ Generar: critical.txt, errors.txt, ...     │
└─────────────────────────────────────────────┘
          ↓
...
```

---

## 📈 MEJORAS CLAVE

### 1. Claridad

**ANTES**: "Crear documentos"  
**AHORA**: "Crear: PLAN.md, DECISIONES.md, TRACKING.md"

### 2. Consistencia

**ANTES**: Nombres variables ("output.md", "datos.txt")  
**AHORA**: Convención estricta (TIPO_CONTEXTO_VERSION.ext)

### 3. Completitud

**ANTES**: 361 líneas, enfocado en proceso  
**AHORA**: 715 líneas (+98%), incluye archivos y templates

### 4. Ejemplos

**ANTES**: Pocos ejemplos abstractos  
**AHORA**: Ejemplos completos de sesiones reales

### 5. Validación

**ANTES**: Sin comandos de verificación  
**AHORA**: Scripts de validación incluidos

---

## 🔄 CAMBIOS EN CADA FASE

### FASE 0: Preparación
- ✅ Lista exacta de archivos obligatorios
- ✅ Template para PLAN.md
- ✅ Template para DECISIONES.md
- ✅ Template para TRACKING.md

### FASE 1: Análisis Inicial
- ✅ Nombres de archivos de datos (.txt)
- ✅ Comandos de extracción
- ✅ Archivos temporales (.tmp)

### FASE 1.5: Análisis Completo
- ✅ Template completo ANALISIS_COMPLETO_BUILD.md
- ✅ Comandos de validación
- ✅ Estructura mínima obligatoria

### FASE 2: Categorización
- ✅ Versionado (_V2, _V3)
- ✅ Template FASE2_CATEGORIZACION.md
- ✅ Énfasis en usar datos (no estimaciones)

### FASE 3: Priorización
- ✅ Template FASE3_PRIORIZACION.md
- ✅ FASE3_REVISION_ANTIPATRONES.md opcional
- ✅ Formato de decisiones

### FASE 4: Ejecución
- ✅ Tipos de archivos por actividad:
  - Scripts: SCRIPT_DESARROLLO_*, SCRIPT_RESUMEN_*, SCRIPT_DRY_RUN_*
  - Errores: ERROR_<descripcion>.md
  - Análisis: ANALISIS_<tipo>_<contexto>.md
- ✅ Templates para cada tipo

### Finalización
- ✅ Template completo RESUMEN_SESION.md
- ✅ Secciones obligatorias
- ✅ Referencias cruzadas

---

## 📖 REFERENCIAS CRUZADAS

El flujo ahora incluye referencias a:

1. **CONVENCION_NOMBRES.md** - Guía completa de nombres
2. **README.md** - Sistema de organización
3. **incremental-correction-methodology** v1.3.0 - Skill base

**Beneficio**: Ecosistema de documentación integrado.

---

## 💡 CÓMO USAR EL NUEVO FLUJO

### Paso 1: Leer Flujo Completo
```bash
cat FLUJO_METODOLOGICO.md
```

### Paso 2: En Cada Fase, Seguir Archivos

**Ejemplo - Iniciar FASE 0**:
1. Lee sección "FASE 0: PREPARACIÓN"
2. Crea archivos obligatorios:
   - `PLAN.md` (usa template)
   - `DECISIONES.md` (usa template)
   - `TRACKING.md` (usa template)
3. Verifica checklist 8/8

### Paso 3: Validar Nombres

Antes de crear archivo:
1. Lee checklist de nombres
2. Verifica formato
3. Confirma que cumple convención

### Paso 4: Usar Templates

Copia template del flujo → Personaliza → Guarda con nombre correcto.

---

## 🎯 IMPACTO ESPERADO

### Para Usuario

**ANTES**:
- ❓ "¿Qué archivo creo?"
- ❓ "¿Cómo lo nombro?"
- ❓ "¿Qué debe contener?"

**AHORA**:
- ✅ Lista exacta de archivos por fase
- ✅ Convención clara de nombres
- ✅ Templates con estructura completa

### Para IA (Claude)

**ANTES**:
- Nombres inconsistentes
- Archivos faltantes
- Estructura variable

**AHORA**:
- Nombres predecibles
- Archivos completos
- Estructura estandarizada

### Para Proyecto

**ANTES**:
- Documentación fragmentada
- Difícil navegar sesiones
- Inconsistencia entre sesiones

**AHORA**:
- Documentación consistente
- Fácil navegación
- Predecibilidad entre sesiones

---

## 📊 ESTADÍSTICAS

| Métrica | V1 | V2 | Cambio |
|---------|----|----|--------|
| Líneas | 361 | 715 | +98% |
| Secciones | 12 | 18 | +50% |
| Templates | 0 | 10 | +10 |
| Ejemplos | 3 | 15+ | +400% |
| Referencias | 1 | 3 | +200% |

---

## ✅ VALIDACIÓN

**Archivo creado**: `FLUJO_METODOLOGICO.md` (v2.0)  
**Backup creado**: `FLUJO_METODOLOGICO_V1.md` (backup de v1.3.0)

**Contenido verificado**:
- ✅ 715 líneas (>500 esperadas)
- ✅ Convención integrada
- ✅ Templates incluidos
- ✅ Ejemplos completos
- ✅ Referencias cruzadas

---

## 🔄 PRÓXIMOS PASOS

### Inmediato
1. ✅ Flujo actualizado
2. ⏸️ Usar en resto de esta sesión
3. ⏸️ Validar en siguiente sesión

### Futuro
1. Actualizar skill `incremental-correction-methodology` con v2.0
2. Agregar más ejemplos de sesiones reales
3. Refinar templates basado en uso

---

## 📝 RESUMEN

**Actualización V2.0 del FLUJO_METODOLOGICO.md**:

- ✅ Convención de nombres integrada
- ✅ Archivos específicos por fase
- ✅ 10 templates incluidos
- ✅ Checklist de validación
- ✅ Ejemplos completos
- ✅ Flujo visual mejorado
- ✅ 715 líneas (+98% vs V1)

**Beneficio**: Flujo completo, autónomo y listo para usar en cualquier sesión.

---

**Fecha**: 2026-02-01 01:20  
**Cambio**: FLUJO_METODOLOGICO.md V1 → V2  
**Estado**: ✅ COMPLETADO
