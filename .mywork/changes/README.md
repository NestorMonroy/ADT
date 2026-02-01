# Sistema de Organización - .mywork/changes/

**Propósito**: Organizar sesiones de trabajo de forma estructurada y trazable  
**Versión**: 1.0.0  
**Fecha**: 2026-02-01

---

## ESTRUCTURA DE DIRECTORIOS

```
.mywork/
└── changes/
    ├── 20260131-230456/           ← Session ID (timestamp)
    │   ├── CONVENCION_NOMBRES.md  ← Esta guía de convención
    │   ├── FASE0_*.md             ← Archivos de fase 0
    │   ├── FASE1_*.md             ← Archivos de fase 1
    │   ├── FASE2_*.md             ← Archivos de fase 2
    │   ├── FASE3_*.md             ← Archivos de fase 3
    │   ├── ANALISIS_*.md          ← Análisis específicos
    │   ├── SCRIPT_*.md            ← Documentación de scripts
    │   ├── DECISIONES.md          ← Decisiones de la sesión
    │   ├── PLAN.md                ← Plan de la sesión
    │   ├── TRACKING.md            ← Seguimiento
    │   ├── RESUMEN_SESION.md      ← Resumen al finalizar
    │   ├── *.txt                  ← Datos y logs
    │   └── *.tmp                  ← Temporales (no commitear)
    │
    └── 20260201-140000/           ← Próxima sesión
        └── ...
```

---

## SESSION ID

Cada sesión tiene un directorio con timestamp como ID:

**Formato**: `YYYYMMDD-HHMMSS`

**Ejemplo**: `20260131-230456`
- 2026-01-31 a las 23:04:56
- Identifica única e inequívocamente la sesión
- Ordenación cronológica automática

---

## ARCHIVOS OBLIGATORIOS POR SESIÓN

Cada sesión DEBE tener como mínimo:

### 1. PLAN.md
**Propósito**: Qué se va a hacer en esta sesión  
**Contenido mínimo**:
- Objetivo de la sesión
- Fases planificadas
- Tiempo estimado

### 2. DECISIONES.md
**Propósito**: Documentar todas las decisiones tomadas  
**Contenido mínimo**:
- Qué se decidió
- Por qué se decidió
- Alternativas consideradas
- Trade-offs

### 3. RESUMEN_SESION.md
**Propósito**: Resumen al finalizar la sesión  
**Contenido mínimo**:
- Qué se hizo
- Qué se logró
- Issues resueltos
- Próximos pasos

---

## ARCHIVOS OPCIONALES (SEGÚN NECESIDAD)

### Metodología
- `FASE<N>_*.md` - Documentos por fase
- `FLUJO_*.md` - Flujos de trabajo

### Análisis
- `ANALISIS_*.md` - Análisis específicos
- `*.txt` - Datos brutos (critical.txt, errors.txt, etc.)

### Scripts
- `SCRIPT_RESUMEN_*.md` - Documentación de scripts
- `SCRIPT_DRY_RUN_*.txt` - Outputs de dry-run

### Errores y Problemas
- `ERROR_*.md` - Errores detectados y documentados

### Tracking
- `TRACKING.md` - Seguimiento de progreso
- `TRACKING_*.md` - Tracking específico

---

## FLUJO DE TRABAJO TÍPICO

### 1. Inicio de Sesión

```bash
# Crear directorio de sesión
SESSION_ID=$(date +%Y%m%d-%H%M%S)
mkdir -p .mywork/changes/$SESSION_ID
cd .mywork/changes/$SESSION_ID

# Copiar convención de nombres (opcional)
cp ../CONVENCION_NOMBRES.md .

# Crear archivos base
touch PLAN.md DECISIONES.md TRACKING.md
```

### 2. Durante la Sesión

```bash
# Ir creando archivos según avanzas
# Seguir convención de nombres
# Documentar decisiones en DECISIONES.md
# Actualizar TRACKING.md con progreso
```

### 3. Fin de Sesión

```bash
# Crear resumen
cat > RESUMEN_SESION.md << EOF
# Resumen - Sesión $SESSION_ID
...
EOF

# Commit (opcional)
git add .
git commit -m "docs: sesión $SESSION_ID - [descripción]"
```

---

## CONVENCIÓN DE NOMBRES

**Ver**: `CONVENCION_NOMBRES.md` para detalles completos

**Regla de Oro**:
> Cada archivo debe tener un nombre que identifique claramente su contexto

**Ejemplos**:
- ✅ `SCRIPT_RESUMEN_fix_critical_titles.md`
- ✅ `ANALISIS_CRITICAL_error_01_omisiones.md`
- ❌ `SCRIPT_RESUMEN.md` (demasiado genérico)
- ❌ `ANALISIS.md` (falta contexto)

---

## BUENAS PRÁCTICAS

### 1. Nombres Descriptivos
```
✅ ANALISIS_CRITICAL_error_01_omisiones.md
❌ analisis.md
```

### 2. Versionado Explícito
```
✅ FASE2_CATEGORIZACION_V2.md
❌ FASE2_CATEGORIZACION_nuevo.md
```

### 3. Contexto en el Nombre
```
✅ SCRIPT_DRY_RUN_fix_critical_titles.txt
❌ output.txt
```

### 4. Separadores Consistentes
```
✅ ANALISIS_CRITICAL_workflow_general.md
❌ ANALISIS-CRITICAL_workflow.general.md
```

### 5. Extensiones Apropiadas
```
✅ .md para documentos
✅ .txt para datos/logs
✅ .tmp para temporales
❌ .doc, .docx (usar .md)
```

---

## INTEGRACIÓN CON GIT

### Qué Commitear

✅ **SÍ commitear**:
- `*.md` - Documentos
- `PLAN.md`, `DECISIONES.md`, `RESUMEN_SESION.md`
- `FASE*.md` - Documentos de fases
- Archivos de análisis importantes

❌ **NO commitear**:
- `*.tmp` - Temporales
- Archivos muy grandes (>1MB)
- Datos duplicados

### .gitignore Recomendado

```gitignore
# Temporales
*.tmp

# Logs muy grandes
*.log

# Datos brutos (si son muy grandes)
# critical.txt
# errors.txt
# warnings.txt
```

---

## LIMPIEZA DE SESIONES ANTIGUAS

### Política de Retención

**Sesiones recientes** (< 30 días):
- Mantener TODO

**Sesiones antiguas** (30-90 días):
- Mantener: PLAN, DECISIONES, RESUMEN_SESION
- Archivar o eliminar: Datos brutos, temporales

**Sesiones muy antiguas** (> 90 días):
- Archivar a `.mywork/archived/`
- O comprimir: `tar -czf session.tar.gz 20260131-230456/`

### Comando de Limpieza

```bash
# Eliminar archivos temporales de todas las sesiones
find .mywork/changes/ -name "*.tmp" -delete

# Comprimir sesiones antiguas (>90 días)
find .mywork/changes/ -maxdepth 1 -type d -mtime +90 \
  -exec tar -czf {}.tar.gz {} \; \
  -exec rm -rf {} \;
```

---

## BÚSQUEDA Y NAVEGACIÓN

### Buscar por Contenido

```bash
# Buscar todas las decisiones sobre "scripts"
grep -r "script" .mywork/changes/*/DECISIONES.md

# Buscar análisis de CRITICAL
find .mywork/changes/ -name "ANALISIS_CRITICAL_*.md"
```

### Buscar por Fecha

```bash
# Sesiones de enero 2026
ls -d .mywork/changes/202601*

# Última sesión
ls -td .mywork/changes/*/ | head -1
```

### Listar por Tipo

```bash
# Todos los planes
find .mywork/changes/ -name "PLAN.md"

# Todos los scripts
find .mywork/changes/ -name "SCRIPT_*.md"
```

---

## EJEMPLO COMPLETO: SESIÓN 20260131-230456

```
.mywork/changes/20260131-230456/
├── CONVENCION_NOMBRES.md                      ← Guía de convención
├── PLAN.md                                    ← Plan de sesión
├── DECISIONES.md                              ← Decisiones tomadas
├── TRACKING.md                                ← Seguimiento
├── RESUMEN_SESION.md                          ← Resumen final
│
├── FASE0_PREPARACION.md                       ← Metodología
├── FASE1_ANALISIS_INICIAL.md
├── ANALISIS_COMPLETO_BUILD.md
├── FASE2_CATEGORIZACION.md
├── FASE2_CATEGORIZACION_V2.md
├── FASE3_PRIORIZACION.md
├── FASE3_REVISION_ANTIPATRONES.md
│
├── ANALISIS_CRITICAL_error_01_omisiones.md    ← Análisis específicos
├── ERROR_ANALISIS_CONCENTRACION_INCORRECTA.md
│
├── SCRIPT_RESUMEN_fix_critical_titles.md      ← Scripts
├── SCRIPT_DRY_RUN_fix_critical_titles.txt
│
├── FLUJO_METODOLOGICO.md                      ← Flujos
├── ACTUALIZACION_SKILL_v1.3.0.md              ← Actualizaciones
│
├── critical.txt                               ← Datos
├── errors.txt
├── warnings.txt
└── *.tmp                                      ← Temporales (no commitear)
```

---

## TEMPLATES

### Template: PLAN.md

```markdown
# Plan - Sesión <SESSION_ID>

**Fecha**: YYYY-MM-DD  
**Objetivo**: [Objetivo principal de la sesión]

## Contexto

[Contexto de por qué se hace esta sesión]

## Fases Planificadas

- [ ] FASE 0: Preparación
- [ ] FASE 1: Análisis
- [ ] FASE 2: Categorización
- [ ] FASE 3: Priorización
- [ ] FASE 4: Ejecución

## Tiempo Estimado

- Total: X horas
- Por fase: [desglose]

## Recursos Necesarios

- Skills: [lista]
- Scripts: [lista]
- Datos: [lista]
```

### Template: DECISIONES.md

```markdown
# Decisiones - Sesión <SESSION_ID>

## DECISIÓN 1: [Título]

**QUÉ**: [Qué se decidió]
**POR QUÉ**: [Razones]
**ALTERNATIVAS**: [Qué más se consideró]
**TRADE-OFFS**: [Pros/contras]
**DECISIÓN FINAL**: [Decisión tomada]

---

## DECISIÓN 2: ...
```

### Template: RESUMEN_SESION.md

```markdown
# Resumen - Sesión <SESSION_ID>

**Fecha**: YYYY-MM-DD  
**Duración**: X horas

## Objetivo

[Objetivo de la sesión]

## Qué se Hizo

[Resumen de actividades]

## Qué se Logró

- Issues resueltos: X
- Archivos modificados: X
- Documentos generados: X

## Decisiones Importantes

[Lista de decisiones clave]

## Próximos Pasos

[Qué queda pendiente]

## Lecciones Aprendidas

[Aprendizajes de la sesión]
```

---

## AYUDA Y SOPORTE

**Documentación**:
- `CONVENCION_NOMBRES.md` - Guía de nombres
- Este README - Guía de organización

**Contacto**:
- Issues del proyecto
- Documentación del skill `incremental-correction-methodology`

---

**Última actualización**: 2026-02-01  
**Versión**: 1.0.0
