---
name: changes-directory-management
description: "Gestión de directorios de trabajo en .mywork/changes/. Usar para crear, renombrar y organizar directorios de proyectos activos."
version: 1.1.0
created: 2026-01-30
updated: 2026-02-01
author: ADT Team
related_skills:
  - work-logger: "Para logs de trabajo completado"
  - spec-driven-dev: "Metodología que usa estos directorios"
  - skills-management: "Para gestión de skills"
---

# Changes Directory Management - Gestión de Directorios de Trabajo

**Versión**: 1.1.0  
**Ubicación**: `/tmp/ADT/.codex/skills/changes-directory-management/`  
**Proyecto**: ADT Documentation (ubicado en `/tmp/ADT`)

## ⚠️ RECORDATORIO CRÍTICO

**Proyecto ubicado en**: `/tmp/ADT`

```bash
cd /tmp/ADT  # Siempre verificar
pwd          # Debe mostrar /tmp/ADT
```

---

## Cuando Usar

Usar esta skill cuando:
- Necesites crear un nuevo directorio de trabajo en `.mywork/changes/`
- Vayas a renombrar un directorio existente con timestamp
- Necesites organizar directorios de proyectos activos
- Quieras documentar cambios en progreso

**NO usar para**:
- Work logs completados (usar `work-logger` en `.mywork/work-logs/`)
- Skills (usar `skills-management` en `.codex/skills/`)
- Documentación permanente (ubicar en `source/`)

---

## Decision Framework: ¿Cómo Nombrar el Directorio?

**Usa este framework para decidir el nombre correcto**:

1. **¿El trabajo es simple y corto (<2 horas)?**
   → Nombre descriptivo corto: `fix-sphinx-warnings`
   → NO necesita timestamp

2. **¿El trabajo es complejo o largo (>2 horas)?**
   → Timestamp OBLIGATORIO: `20260201-143022-implementar-validacion`
   → Formato: `YYYYMMDD-HHMMSS-descripcion`

3. **¿El trabajo está en progreso activo?**
   → Usar timestamp actual
   → Crear PLAN.md dentro

4. **¿El trabajo está pausado/completado?**
   → Renombrar agregando `_completed` o `_paused`
   → Mover a subdirectorio `archived/` si es muy viejo

5. **¿Necesito varios directorios para el mismo tema?**
   → Usar timestamp diferente + descripción específica
   → Ejemplo: `20260201-120000-sphinx-fase1`, `20260201-140000-sphinx-fase2`

6. **¿No estoy seguro?**
   → Usar timestamp siempre (más seguro)
   → Mejor tener timestamp de más que de menos

**Regla de oro**: Cuando dudes → **USA TIMESTAMP**

---

## Trigger Patterns

### Señales Explícitas

- Usuario dice: "voy a trabajar en X"
- Usuario dice: "vamos a implementar Y"
- Usuario dice: "necesito planificar Z"
- Usuario menciona: "crear directorio de trabajo"
- Usuario pregunta: "¿dónde documento esto?"

### Señales Implícitas

- Usuario describe un cambio complejo
- Usuario está a punto de empezar trabajo >2 horas
- Usuario menciona "plan", "diseño", "spec"
- Usuario usa futuro: "vamos a...", "voy a..."
- Contexto indica trabajo nuevo comenzando

### Trigger Words

**Palabras de acción**:
- "implementar", "desarrollar", "crear", "construir"
- "cambio", "modificación", "refactor"
- "proyecto", "tarea", "trabajo"

**Palabras de planificación**:
- "plan", "diseño", "spec", "propuesta"
- "documentar", "registrar", "tracking"

**Palabras temporales**:
- "voy a", "vamos a", "empezar", "iniciar"
- "nuevo", "próximo", "siguiente"

**Anti-triggers** (NO crear directorio si solo dicen):
- "¿cómo funciona X?" (solo pregunta)
- "explícame Y" (solo información)
- Fix trivial de 1 línea (no requiere directorio)

---

## Self-Check Before Creating Directory

**OBLIGATORIO antes de crear directorio en .mywork/changes/**:

### Pre-Creación
- [ ] ¿Estoy en `/tmp/ADT/`?
- [ ] ¿El trabajo es >30 min de duración?
- [ ] ¿Necesito documentar un plan?
- [ ] ¿El nombre sigue las convenciones?
- [ ] ¿Ya existe un directorio similar?

**Si NO al trabajo >30 min → Probablemente no necesitas directorio**

### Sobre el Nombre
- [ ] ¿Usé timestamp si el trabajo es >2 horas?
- [ ] ¿El nombre es descriptivo?
- [ ] ¿El nombre es <50 caracteres?
- [ ] ¿Evité espacios y caracteres especiales?
- [ ] ¿Usé minúsculas y guiones?

**Si NO → Corregir nombre antes de crear**

### Post-Creación
- [ ] ¿Creé PLAN.md dentro del directorio?
- [ ] ¿Documenté el objetivo del trabajo?
- [ ] ¿Agregué la estructura básica?
- [ ] ¿Está en la lista de directorios activos?

**Si NO → Completar estructura básica ahora**

---

## Estructura de .mywork/changes/

### Propósito

Los directorios en `.mywork/changes/` contienen documentación de **trabajo EN PROGRESO**:
- Planes de cambios
- Tracking de ejecución
- Resultados intermedios
- Decisiones tomadas durante el trabajo

### Diferencia con .mywork/work-logs/

| Aspecto | .mywork/changes/ | .mywork/work-logs/ |
|---------|------------------|-------------------|
| Contenido | Trabajo EN PROGRESO | Trabajo COMPLETADO |
| Estructura | DIRECTORIOS | ARCHIVOS individuales |
| Formato | YYYY-MM-DD-HH-MM-nombre/ | YYYY-MM-DD-HH-MM-titulo.md |
| Duración | Mientras dure el trabajo | Permanente |
| Archivos | Múltiples (.md) | Uno por trabajo |

---

## Formato de Nombres de Directorios

### Formato Estándar

```
YYYY-MM-DD-HH-MM-nombre-descriptivo/
```

**Componentes**:
- `YYYY`: Año (4 dígitos)
- `MM`: Mes (2 dígitos, 01-12)
- `DD`: Día (2 dígitos, 01-31)
- `HH`: Hora (2 dígitos, 00-23)
- `MM`: Minuto (2 dígitos, 00-59)
- `nombre-descriptivo`: Descripción kebab-case (minúsculas, guiones)

### Ejemplos Válidos

```
2026-01-30-16-35-correccion-completa-manual/
2026-01-29-17-50-plan-pendientes-work-logs/
2026-01-30-03-31-corregir-errores-build-sphinx/
```

### ❌ Ejemplos Incorrectos

```
❌ 2026-01-30-correccion-manual/           (sin timestamp)
❌ 2026-1-30-16-35-trabajo/                 (mes sin cero)
❌ 2026-01-30-16-35-Trabajo_Importante/     (mayúsculas, guion bajo)
❌ correccion-manual/                       (sin fecha)
```

---

## Crear Nuevo Directorio

### Paso 1: Generar Timestamp

```bash
cd /tmp/ADT

# Generar timestamp actual
TIMESTAMP=$(date "+%Y-%m-%d-%H-%M")
echo "Timestamp: $TIMESTAMP"
# Ejemplo output: 2026-01-30-16-35
```

### Paso 2: Crear Directorio

```bash
# Definir nombre descriptivo (kebab-case, max 50 chars)
NOMBRE="descripcion-breve-del-trabajo"

# Crear directorio
DIR_NAME="${TIMESTAMP}-${NOMBRE}"
mkdir -p ".mywork/changes/${DIR_NAME}"

echo "✅ Directorio creado: .mywork/changes/${DIR_NAME}/"
```

### Paso 3: Crear Archivos Base

```bash
cd ".mywork/changes/${DIR_NAME}"

# Crear archivos estándar
touch RESUMEN-EJECUTIVO.md
touch PLAN-[NOMBRE-PROYECTO].md
touch TRACKING-EJECUCION.md

ls -la
```

### Ejemplo Completo

```bash
cd /tmp/ADT

# Timestamp + nombre
TIMESTAMP=$(date "+%Y-%m-%d-%H-%M")
NOMBRE="implementar-nueva-feature"
DIR_NAME="${TIMESTAMP}-${NOMBRE}"

# Crear y poblar
mkdir -p ".mywork/changes/${DIR_NAME}"
cd ".mywork/changes/${DIR_NAME}"

# Crear archivos
cat > RESUMEN-EJECUTIVO.md <<'EOF'
# Resumen Ejecutivo - [Nombre del Proyecto]

**Fecha**: YYYY-MM-DD
**Estado**: EN PROGRESO

## Objetivo

[Descripción breve]
EOF

echo "✅ Directorio listo: ${DIR_NAME}/"
```

---

## Renombrar Directorio Existente con Timestamp

### ⚠️ CUÁNDO RENOMBRAR

Renombrar un directorio existente cuando:
- Fue creado sin timestamp (formato antiguo: `YYYY-MM-DD-nombre`)
- Necesitas añadir timestamp para mejor trazabilidad
- Quieres estandarizar según convención actual

### Procedimiento de Renombrado

#### Paso 1: Verificar Estado Actual

```bash
cd /tmp/ADT

# Ver directorios actuales
ls -la .mywork/changes/

# Identificar directorio a renombrar
OLD_DIR="2026-01-30-correccion-completa-manual"
ls -la ".mywork/changes/${OLD_DIR}/"
```

#### Paso 2: Verificar Git Status

**CRÍTICO**: Verificar que no hay cambios sin commitear

```bash
git status

# Si hay cambios:
git add .mywork/changes/
git commit -m "docs: cambios antes de renombrar directorio"
```

#### Paso 3: Generar Timestamp de Inicio del Trabajo

**IMPORTANTE**: Usar timestamp del **inicio del trabajo**, no el actual

Opciones:

**Opción A**: Extraer de primer archivo creado
```bash
cd /tmp/ADT
OLD_DIR="2026-01-30-correccion-completa-manual"

# Ver timestamp del primer archivo
ls -lt ".mywork/changes/${OLD_DIR}/" | tail -1
# O usar stat
stat -c %y ".mywork/changes/${OLD_DIR}/PLAN-*.md" | cut -d' ' -f1,2 | tr ' :' '--'
```

**Opción B**: Usar timestamp de inicio conocido
```bash
# Si conoces la hora de inicio (ej: 15:17)
FECHA="2026-01-30"
HORA="15-17"
TIMESTAMP="${FECHA}-${HORA}"
```

**Opción C**: Extraer de git log
```bash
# Ver primer commit relacionado
git log --oneline --all --grep="correccion-completa-manual" | tail -1
# Ver timestamp de ese commit
git show [commit-hash] --format="%ai" | head -1
```

#### Paso 4: Renombrar Directorio

```bash
cd /tmp/ADT

# Variables
OLD_DIR="2026-01-30-correccion-completa-manual"
TIMESTAMP="2026-01-30-15-17"  # Timestamp de inicio del trabajo
NOMBRE="correccion-completa-manual"
NEW_DIR="${TIMESTAMP}-${NOMBRE}"

# Renombrar
mv ".mywork/changes/${OLD_DIR}" ".mywork/changes/${NEW_DIR}"

# Verificar
ls -la ".mywork/changes/${NEW_DIR}/"
echo "✅ Renombrado: ${OLD_DIR} → ${NEW_DIR}"
```

#### Paso 5: Actualizar Referencias Internas

**IMPORTANTE**: Actualizar rutas en archivos que referencien el directorio

```bash
cd /tmp/ADT

NEW_DIR="2026-01-30-15-17-correccion-completa-manual"

# Buscar referencias al nombre antiguo
grep -r "2026-01-30-correccion-completa-manual" ".mywork/changes/${NEW_DIR}/"

# Actualizar si es necesario (ejemplo)
find ".mywork/changes/${NEW_DIR}/" -name "*.md" -exec sed -i \
  's|2026-01-30-correccion-completa-manual|2026-01-30-15-17-correccion-completa-manual|g' {} +
```

#### Paso 6: Commit del Renombrado

```bash
cd /tmp/ADT

git add ".mywork/changes/"
git commit -m "refactor(docs): renombrar directorio con timestamp

Renombrado:
  2026-01-30-correccion-completa-manual/
  → 2026-01-30-15-17-correccion-completa-manual/

Razón: Estandarizar formato según changes-directory-management
Timestamp: Hora de inicio del trabajo (15:17)

Ref: .codex/skills/changes-directory-management/"
```

---

## Ejemplo Completo: Renombrar Directorio Actual

### Contexto

Directorio actual: `2026-01-30-correccion-completa-manual/`  
Necesita: Añadir timestamp de inicio (15:17)

### Ejecución

```bash
cd /tmp/ADT

# 1. Verificar estado
git status
# (asegurar que está limpio o hacer commit)

# 2. Definir variables
OLD_DIR="2026-01-30-correccion-completa-manual"
TIMESTAMP="2026-01-30-15-17"  # Hora de inicio conocida
NOMBRE="correccion-completa-manual"
NEW_DIR="${TIMESTAMP}-${NOMBRE}"

# 3. Renombrar
mv ".mywork/changes/${OLD_DIR}" ".mywork/changes/${NEW_DIR}"

# 4. Verificar contenido
ls -la ".mywork/changes/${NEW_DIR}/"

# 5. Actualizar referencias (si hay)
grep -r "${OLD_DIR}" ".mywork/changes/${NEW_DIR}/" || echo "No hay referencias"

# 6. Commit
git add ".mywork/changes/"
git commit -m "refactor(docs): renombrar directorio con timestamp

${OLD_DIR}/ → ${NEW_DIR}/

Estandarización según changes-directory-management v1.0.0"

echo "✅ Renombrado completado"
```

---

## Archivos Estándar en Directorios

### Archivos Recomendados

```
.mywork/changes/YYYY-MM-DD-HH-MM-nombre/
├── RESUMEN-EJECUTIVO.md        # Resumen del proyecto
├── PLAN-[NOMBRE].md            # Plan detallado
├── TRACKING-EJECUCION.md       # Tracking en tiempo real
├── RESULTADOS-[TIPO].md        # Resultados (opcional)
└── [otros archivos específicos]
```

### Convenciones de Nombres de Archivos

- **MAYÚSCULAS-CON-GUIONES.md**: Documentos principales
- **kebab-case.md**: Archivos auxiliares
- Evitar espacios, acentos, caracteres especiales

---

## Mantenimiento de Directorios

### Archivar Proyectos Completados

Cuando un proyecto en `.mywork/changes/` está completado:

**Opción A**: Mover a work-logs como archivo único

```bash
cd /tmp/ADT

# Generar work log final
TIMESTAMP=$(date "+%Y-%m-%d-%H-%M")
cat ".mywork/changes/2026-01-30-15-17-proyecto/" > \
  ".mywork/work-logs/${TIMESTAMP}-proyecto-completado.md"
```

**Opción B**: Mover a directorio archive

```bash
mkdir -p .mywork/changes/archive/2026-01/
mv .mywork/changes/2026-01-30-15-17-proyecto/ \
   .mywork/changes/archive/2026-01/
```

**Opción C**: Mantener como referencia

```bash
# No mover, mantener para futuras referencias
# Marcar como completado en RESUMEN-EJECUTIVO.md
```

---

## Comandos Útiles

### Listar Directorios Activos

```bash
cd /tmp/ADT

# Listar todos
ls -lt .mywork/changes/ | grep "^d"

# Solo directorios de hoy
TODAY=$(date "+%Y-%m-%d")
ls -d .mywork/changes/${TODAY}*

# Contar directorios
ls -d .mywork/changes/*/ | wc -l
```

### Buscar en Directorios

```bash
# Buscar texto en todos los directorios
grep -r "palabra" .mywork/changes/

# Buscar en directorios de fecha específica
grep -r "palabra" .mywork/changes/2026-01-30*

# Listar archivos modificados recientemente
find .mywork/changes/ -name "*.md" -mtime -1
```

### Verificar Formato de Nombres

```bash
# Verificar que siguen formato correcto
ls .mywork/changes/ | grep -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-.+" \
  || echo "Algunos directorios no siguen formato estándar"
```

---

## Relaciones con Otras Skills

### work-logger
- **Diferencia**: work-logger es para trabajo COMPLETADO
- **Relación**: Después de completar trabajo en `.mywork/changes/`, crear work log en `.mywork/work-logs/`
- **Flujo**:
  1. Trabajar en `.mywork/changes/YYYY-MM-DD-HH-MM-proyecto/`
  2. Al completar, crear `.mywork/work-logs/YYYY-MM-DD-HH-MM-proyecto-completado.md`

### spec-driven-dev
- **Relación**: Usa directorios en `.mywork/changes/` para fases del proyecto
- **Formato**: spec-driven-dev define archivos, esta skill define directorios

### skills-management
- **Relación**: Ambas gestionan estructura de documentación
- **Diferencia**: skills-management para `.codex/skills/`, esta para `.mywork/changes/`

---

## Troubleshooting

### Problema: Directorio sin timestamp

**Síntoma**: Directorio en formato `YYYY-MM-DD-nombre` sin `HH-MM`

**Solución**: Seguir procedimiento de renombrado (ver sección arriba)

### Problema: No sé qué timestamp usar

**Solución**:
1. Revisar primer archivo creado: `ls -lt directorio/ | tail -1`
2. Revisar git log: `git log --oneline --all -- directorio/`
3. Usar timestamp aproximado de inicio del día si no hay info

### Problema: Referencias rotas después de renombrar

**Síntoma**: Enlaces o paths en archivos apuntan al nombre antiguo

**Solución**:
```bash
# Buscar referencias
grep -r "nombre-antiguo" nuevo-directorio/

# Reemplazar
find nuevo-directorio/ -name "*.md" -exec sed -i \
  's|nombre-antiguo|nombre-nuevo|g' {} +
```

---

## Checklist de Renombrado

- `[ ]` Git status limpio (o commit previo)
- `[ ]` Timestamp de inicio identificado
- `[ ]` Directorio renombrado con `mv`
- `[ ]` Contenido verificado (`ls -la`)
- `[ ]` Referencias internas actualizadas
- `[ ]` Commit realizado
- `[ ]` Verificar que todo funciona

---

## Changelog

### v1.0.0 - 2026-01-30

**Versión inicial**

- Formato estándar de directorios: YYYY-MM-DD-HH-MM-nombre/
- Procedimiento completo de renombrado con timestamp
- Diferencia entre .mywork/changes/ y .mywork/work-logs/
- Comandos útiles de gestión
- Archivos estándar recomendados
- Mantenimiento y archivado
- Troubleshooting común

**Razón de Creación**:
- Necesidad identificada durante corrección completa manual
- Estandarizar formato de directorios de trabajo
- Documentar procedimiento de renombrado con timestamp
- Diferenciar claramente de work-logger

**Referencias**:
- Observación de directorios existentes en `.mywork/changes/`
- Convenciones de `work-logger`
- Formato usado en `spec-driven-dev`
- Solicitud de usuario para renombrar con timestamp

---

**Notas**:
- Esta skill complementa work-logger (para trabajo completado)
- Timestamp permite trazabilidad temporal precisa
- Formato estandarizado facilita scripts y búsquedas
- Mantener consistencia con convenciones del proyecto

---

## Versionamiento

### v1.1.0 (2026-02-01) - FASE 2

**Mejoras de usabilidad y naming**:

✅ **Decision Framework** - ¿Cómo Nombrar el Directorio?
- 6 preguntas para decidir naming correcto
- Regla: Simple (<2h) = no timestamp, Complejo (>2h) = timestamp
- Regla de oro: "Cuando dudes → USA TIMESTAMP"

✅ **Trigger Patterns** - Cuándo crear directorio
- Señales explícitas (usuario dice "voy a trabajar en X")
- Señales implícitas (usuario describe cambio complejo)
- Trigger words de acción y planificación
- Anti-triggers para evitar directorios innecesarios

✅ **Self-Check Mechanisms** - Checklist antes de crear
- Pre-Creación (ubicación, duración, necesidad)
- Sobre el Nombre (timestamp, descriptivo, formato)
- Post-Creación (PLAN.md, objetivo, estructura)

**Líneas agregadas**: ~90 líneas

**Beneficio principal**:
- Naming consistente y correcto
- Usuarios saben cuándo crear directorio
- Estructura básica garantizada

**Cambios en estructura**:
- Decision Framework para naming
- Trigger Patterns agregados
- Self-Checks previenen naming incorrecto

### v1.0.0 (2026-01-30)

- Versión inicial
- Convenciones de naming
- Estructura de directorios
- Ejemplos de uso

---

**Última actualización**: 2026-02-01  
**Mantenedor**: ADT Team  
**Ubicación del Proyecto**: `/tmp/ADT`
