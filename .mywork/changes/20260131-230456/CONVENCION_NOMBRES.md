# Convención de Nombres - .mywork/changes/

**Directorio**: `/tmp/ADT/.mywork/changes/<session-id>/`  
**Propósito**: Documentar sesiones de trabajo de forma clara y organizada  
**Versión**: 1.0.0  
**Fecha**: 2026-02-01

---

## REGLA GENERAL

**Cada archivo DEBE tener un nombre que identifique claramente su contexto o propósito**

### ❌ MAL (Genérico)
```
SCRIPT_RESUMEN.md          ← ¿Resumen de qué script?
ANALISIS.md                ← ¿Análisis de qué?
ERROR.md                   ← ¿Qué error?
```

### ✅ BIEN (Específico)
```
SCRIPT_RESUMEN_fix_critical_titles.md      ← Claro: resumen del script fix_critical_titles
ANALISIS_CRITICAL_error_01_omisiones.md    ← Claro: análisis de CRITICAL en ese archivo
ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md ← Claro: qué error se detectó
```

---

## PATRONES DE NOMBRES

### 1. Archivos de Fase (Metodología)

**Formato**: `FASE<N>_<NOMBRE_FASE>.md`

**Ejemplos**:
```
FASE0_PREPARACION.md
FASE1_ANALISIS_INICIAL.md
FASE2_CATEGORIZACION.md
FASE2_CATEGORIZACION_V2.md          ← Con versión si hay múltiples
FASE3_PRIORIZACION.md
FASE3_REVISION_ANTIPATRONES.md      ← Con subtarea específica
FASE4_EJECUCION.md
```

**Subcategorías de fase**:
```
FASE<N>_<SUBTAREA>_<CONTEXTO>.md
└─────┘ └────────┘ └─────────┘
  |        |           └─ Contexto específico (opcional)
  |        └─ Nombre descriptivo de la subtarea
  └─ Número de fase
```

---

### 2. Análisis Específicos

**Formato**: `ANALISIS_<TIPO>_<ARCHIVO_O_CONTEXTO>.md`

**Ejemplos**:
```
ANALISIS_COMPLETO_BUILD.md                 ← Análisis del build completo
ANALISIS_CRITICAL_error_01_omisiones.md    ← Análisis de CRITICAL en archivo específico
ANALISIS_WARNING_headers.md                ← Análisis de WARNING de tipo headers
ANALISIS_DISTRIBUCION_issues.md            ← Análisis de distribución de issues
```

---

### 3. Scripts y Herramientas

**Formato**: `SCRIPT_<ACCION>_<NOMBRE_SCRIPT>.md` o `.txt`

**Ejemplos**:
```
SCRIPT_RESUMEN_fix_critical_titles.md      ← Resumen del script
SCRIPT_DRY_RUN_fix_critical_titles.txt     ← Output del dry-run
SCRIPT_DESARROLLO_validate_rst.md          ← Desarrollo/diseño del script
SCRIPT_EJECUCION_fix_blank_lines.log       ← Log de ejecución
```

---

### 4. Errores y Problemas

**Formato**: `ERROR_<DESCRIPCION_ESPECIFICA>.md`

**Ejemplos**:
```
ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md  ← Error detectado en análisis
ERROR_BUILD_sphinx_warnings.md               ← Error durante build
ERROR_SCRIPT_sed_pattern_mismatch.md         ← Error en script
```

---

### 5. Decisiones

**Formato**: `DECISIONES_<CONTEXTO>.md` o `DECISIONES.md` (si es general de sesión)

**Ejemplos**:
```
DECISIONES.md                               ← Decisiones generales de la sesión
DECISIONES_PRIORIZACION.md                  ← Decisiones de priorización
DECISIONES_TECNOLOGIA_script_vs_manual.md   ← Decisión técnica específica
```

---

### 6. Planes y Tracking

**Formato**: `PLAN_<CONTEXTO>.md` o `TRACKING_<CONTEXTO>.md`

**Ejemplos**:
```
PLAN.md                                     ← Plan general de sesión
PLAN_FASE4_EJECUCION.md                     ← Plan de ejecución específico
TRACKING.md                                 ← Tracking general
TRACKING_ISSUES_resueltos.md                ← Tracking de issues resueltos
```

---

### 7. Reportes y Resúmenes

**Formato**: `RESUMEN_<CONTEXTO>.md` o `REPORTE_<CONTEXTO>.md`

**Ejemplos**:
```
RESUMEN_SESION.md                           ← Resumen general
RESUMEN_CORRECCIONES_critical.md            ← Resumen de correcciones
REPORTE_MENSUAL_enero_2026.md               ← Reporte periódico
```

---

### 8. Datos y Logs

**Formato**: `<tipo>.txt` o `<tipo>_<contexto>.txt`

**Ejemplos**:
```
critical.txt                                ← Issues CRITICAL del build
errors.txt                                  ← Issues ERROR del build
warnings.txt                                ← Issues WARNING del build
critical_files.tmp                          ← Archivo temporal con lista de archivos
build_output.log                            ← Log de build
```

---

### 9. Flujos y Metodología

**Formato**: `FLUJO_<NOMBRE>.md` o `METODOLOGIA_<NOMBRE>.md`

**Ejemplos**:
```
FLUJO_METODOLOGICO.md                       ← Flujo general de metodología
FLUJO_CORRECCION_incremental.md             ← Flujo específico de corrección
METODOLOGIA_ANALISIS_issues.md              ← Metodología de análisis
```

---

## ESTRUCTURA DE NOMBRES COMPUESTOS

Cuando un archivo tiene múltiples contextos, usa guiones bajos:

**Formato**: `<TIPO>_<CONTEXTO1>_<CONTEXTO2>_<VERSION>.md`

**Ejemplos**:
```
ANALISIS_CRITICAL_workflow_general_v1.md
SCRIPT_RESUMEN_fix_titles_dry_run.txt
FASE2_CATEGORIZACION_error_omisiones_V2.md
```

---

## VERSIONES

Cuando hay múltiples versiones del mismo documento:

**Formato**: Agregar `_V<N>` o `_v<N>` al final (antes de la extensión)

**Ejemplos**:
```
FASE2_CATEGORIZACION.md         ← Primera versión
FASE2_CATEGORIZACION_V2.md      ← Segunda versión (corregida)
ANALISIS_v1.md                  ← Versión 1
ANALISIS_v2.md                  ← Versión 2
```

---

## ARCHIVOS TEMPORALES

Los archivos temporales deben usar extensión `.tmp`:

**Ejemplos**:
```
critical_files.tmp
processing_queue.tmp
temp_analysis.tmp
```

**IMPORTANTE**: Los `.tmp` NO se commitean a git.

---

## EJEMPLOS REALES DE ESTA SESIÓN

### ✅ CORRECTO (Después del rename)

```
FASE0_PREPARACION.md                        ← Fase específica
FASE1_ANALISIS_INICIAL.md                   ← Fase específica
ANALISIS_COMPLETO_BUILD.md                  ← Análisis del build
ANALISIS_CRITICAL_error_01_omisiones.md     ← Análisis específico de archivo
FASE2_CATEGORIZACION_V2.md                  ← Versión corregida
FASE3_PRIORIZACION.md                       ← Fase específica
FASE3_REVISION_ANTIPATRONES.md              ← Subtarea de Fase 3
SCRIPT_RESUMEN_fix_critical_titles.md       ← Resumen de script específico
SCRIPT_DRY_RUN_fix_critical_titles.txt      ← Output de dry-run
ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md  ← Error específico
DECISIONES.md                               ← Decisiones generales
PLAN.md                                     ← Plan general
```

### ❌ INCORRECTO (Antes del rename)

```
SCRIPT_RESUMEN.md              ← Demasiado genérico
ANALISIS_22_CRITICAL.md        ← Falta contexto de archivo
ERROR_ANALISIS_DETECTADO.md    ← No dice qué tipo de error
```

---

## CHECKLIST ANTES DE CREAR UN ARCHIVO

```
□ ¿El nombre indica claramente el propósito?
□ ¿El nombre incluye el contexto específico?
□ ¿Si es de una fase, incluye FASE<N>?
□ ¿Si es de un script, incluye el nombre del script?
□ ¿Si es un análisis, indica qué se analizó?
□ ¿Si hay versiones, está marcada la versión?
□ ¿Un humano puede entender el contenido solo por el nombre?
```

Si respondiste SÍ a todo → ✅ Nombre correcto

---

## ORGANIZACIÓN POR CATEGORÍAS

Dentro de cada sesión, los archivos se pueden agrupar mentalmente por categoría:

### Metodología (FASE*)
```
FASE0_PREPARACION.md
FASE1_ANALISIS_INICIAL.md
FASE2_CATEGORIZACION_V2.md
FASE3_PRIORIZACION.md
FASE3_REVISION_ANTIPATRONES.md
```

### Análisis (ANALISIS_*)
```
ANALISIS_COMPLETO_BUILD.md
ANALISIS_CRITICAL_error_01_omisiones.md
```

### Scripts (SCRIPT_*)
```
SCRIPT_RESUMEN_fix_critical_titles.md
SCRIPT_DRY_RUN_fix_critical_titles.txt
```

### Gestión de Sesión
```
PLAN.md
DECISIONES.md
TRACKING.md
RESUMEN_SESION.md
```

### Datos
```
critical.txt
errors.txt
warnings.txt
```

---

## NOMBRES A EVITAR

❌ Nombres demasiado genéricos:
```
output.txt
data.md
temp.txt
test.md
notas.md
```

❌ Nombres con fechas/timestamps en el nombre del archivo:
```
analisis_20260201.md         ← NO: la fecha ya está en el directorio
script_010203.md             ← NO: confuso
```

✅ En su lugar:
```
ANALISIS_COMPLETO_BUILD.md   ← El directorio ya tiene la fecha
SCRIPT_RESUMEN_fix_titles.md
```

---

## RESUMEN

**Regla de Oro**: 
> El nombre del archivo debe responder: "¿QUÉ es esto y de QUÉ trata?"

**Formato general**:
```
<TIPO>_<CONTEXTO_ESPECIFICO>_<VERSION_OPCIONAL>.<ext>
```

**Verificación rápida**:
Si alguien lee solo el nombre del archivo, ¿puede saber qué contiene sin abrirlo? 

- SÍ → ✅ Buen nombre
- NO → ❌ Mejorar el nombre

---

**Última actualización**: 2026-02-01  
**Versión**: 1.0.0
