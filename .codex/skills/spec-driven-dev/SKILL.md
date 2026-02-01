---
name: spec-driven-dev
description: "Desarrollo guiado por especificaciones en 4 fases. Usar para features complejas, cambios arquitectonicos, o cualquier trabajo que requiera planificacion estructurada."
version: 1.2.0
created: 2026-01-29
updated: 2026-02-01
---

# Spec-Driven Development

## Cuando usar

- Features complejas
- Cambios arquitectonicos
- Traducciones grandes (multi-seccion)
- Refactorings importantes
- Implementacion de workflows nuevos

---

## Decision Framework: ¿Necesito Spec-Driven Development?

**Usa este framework para decidir si aplicar metodología spec-driven**:

1. **¿El trabajo tomará >2 horas?**
   → Sí, usar spec-driven (planificación vale la pena)

2. **¿Hay múltiples pasos o fases?**
   → Sí, spec-driven (estructura 4 fases ayuda)

3. **¿Afecta arquitectura o estructura importante?**
   → Sí, spec-driven (diseño crítico)

4. **¿Necesitas aprobación o revisión antes de implementar?**
   → Sí, spec-driven (specs documentadas facilitan)

5. **¿Es cambio simple de 1 archivo <30 min?**
   → No, hacerlo directamente sin spec-driven

6. **¿Ya sabes exactamente cómo implementar?**
   → Depende: si complejo aún así usa spec-driven

7. **¿Hay riesgo de regresiones o efectos secundarios?**
   → Sí, spec-driven (plan de testing)

8. **¿Necesitas tracking de progreso en múltiples sesiones?**
   → Sí, spec-driven (tasks estructuradas)

**Regla de oro**: **>2 horas O complejo → spec-driven**

---

## Trigger Patterns

### Señales Explícitas
- Usuario dice: "vamos a implementar X"
- Usuario dice: "necesito planificar..."
- Usuario menciona: "feature", "proyecto grande", "cambio arquitectónico"
- Usuario pregunta: "¿cómo organizo esto?"
- Trabajo claramente multi-fase o multi-sesión

### Señales Implícitas
- Usuario describe trabajo complejo
- Múltiples componentes afectados
- Usuario usa tiempo futuro ("vamos a...", "implementaremos...")
- Contexto indica planificación necesaria
- Usuario menciona riesgos o incertidumbre

### Trigger Words
- "feature", "proyecto", "implementar", "desarrollar"
- "planificar", "diseñar", "especificar"
- "cambio arquitectónico", "refactoring grande"
- "traducción multi-sección", "workflow nuevo"

**Anti-triggers** (NO usar spec-driven):
- Hotfix urgente (<30 min)
- Cambio trivial de 1-2 líneas
- "fix rápido", "typo", "cambio menor"
- Usuario ya tiene plan completo claro
- Experimentación rápida (usar branches temporales)

---

## Self-Check Before Starting Spec-Driven

**OBLIGATORIO antes de iniciar metodología**:

### Pre-Planning Checks
- [ ] ¿El trabajo tomará >2 horas?
- [ ] ¿Es suficientemente complejo para justificar planificación?
- [ ] ¿Tengo tiempo para hacer las 4 fases correctamente?
- [ ] ¿Creé directorio con timestamp en `.mywork/changes/`?
- [ ] ¿Tengo claro el objetivo general?

**Si NO a mayoría → Considerar hacerlo directamente sin spec-driven**

### During Spec-Driven Checks

**FASE 1 (Requirements)**:
- [ ] ¿Documenté contexto y problema?
- [ ] ¿Definí objetivos claros y medibles?
- [ ] ¿Listé requisitos funcionales?
- [ ] ¿Especificé criterios de aceptación?

**FASE 2 (Design)**:
- [ ] ¿Propuse solución técnica?
- [ ] ¿Documenté alternativas consideradas?
- [ ] ¿Identifiqué archivos a modificar/crear?
- [ ] ¿Tengo plan de implementación?

**FASE 3 (Tasks)**:
- [ ] ¿Descompuse en tareas atómicas?
- [ ] ¿Cada tarea tiene criterio de "done"?
- [ ] ¿Ordené tareas por dependencias?
- [ ] ¿Estimé tiempos realistas?

**FASE 4 (Implementation)**:
- [ ] ¿Sigo el plan documentado?
- [ ] ¿Marco tareas como completadas?
- [ ] ¿Hago commits por tarea?
- [ ] ¿Valido después de cada tarea?

**Si NO en cualquier fase → PAUSE - Completar antes de continuar**

### Post-Implementation Checks
- [ ] ¿Todas las tareas marcadas como done?
- [ ] ¿Los criterios de aceptación se cumplen?
- [ ] ¿Documenté decisiones importantes?
- [ ] ¿Creé work log del proyecto?
- [ ] ¿El directorio refleja trabajo completado?

**Si NO → COMPLETAR antes de cerrar proyecto**

---

## Metodologia en 4 Fases

### FASE 1: Requirements (Requerimientos)

OBJETIVO: Definir QUE se necesita

DIRECTORIO: `.mywork/changes/YYYY-MM-DD-HH-MM-brief-desc/`

**Nota**: Usar formato con timestamp completo según `changes-directory-management`

ARCHIVO: `YYYY-MM-DD-HH-MM-titulo.md`

CONTENIDO:
```markdown
# Requirements: [Titulo]

Fecha: YYYY-MM-DD
Estado: Draft

## 1. Contexto

[Situacion actual, por que es necesario]

## 2. Problema

[Problema especifico a resolver]

## 3. Objetivos

### 3.1 Objetivo Principal

### 3.2 Objetivos Secundarios

## 4. Requisitos Funcionales

RF-001: [Descripcion]
- Prioridad: Alta/Media/Baja
- Criterio aceptacion: [Como validar]

RF-002: [Descripcion]
...

## 5. Requisitos No Funcionales

RNF-001: [Descripcion]
...

## 6. Restricciones

- [Restriccion 1]
- [Restriccion 2]

## 7. Fuera de Alcance

- [No incluido 1]
- [No incluido 2]

## 8. Stakeholders

- [Stakeholder 1]: [Interes]

## 9. Referencias

- [Doc 1]
```

PROCESO:
1. Crear directorio de trabajo (ver `changes-directory-management` para procedimiento)
   ```bash
   TIMESTAMP=$(date "+%Y-%m-%d-%H-%M")
   NOMBRE="brief-desc"
   mkdir -p ".mywork/changes/${TIMESTAMP}-${NOMBRE}"
   ```
2. Generar archivo `YYYY-MM-DD-HH-MM-titulo.md`
3. **SOLICITAR APROBACION AL USUARIO**
4. **NO CONTINUAR SIN APROBACION EXPLICITA**

### FASE 2: Design (Diseño)

OBJETIVO: Definir COMO se implementara

ARCHIVO: `YYYY-MM-DD-HH-MM-titulo.md`

CONTENIDO:
```markdown
# Design: [Titulo]

Basado en: archivo de requirements (YYYY-MM-DD-HH-MM-titulo.md)
Fecha: YYYY-MM-DD
Estado: Draft

## 1. Vision General

[Overview de la solucion]

## 2. Decisiones Arquitectonicas

DA-001: [Titulo]
- Contexto: [Por que surge]
- Decision: [Que se decidio]
- Alternativas: [Opciones consideradas]
- Consecuencias: [Impacto]

DA-002: [Titulo]
...

## 3. Componentes Afectados

### 3.1 Nuevos Componentes

### 3.2 Componentes Modificados

### 3.3 Componentes Deprecados

## 4. Estructura de Archivos

```
path/to/
+-- new_file.rst
+-- modified_file.rst
```

## 5. Interfaces y Contratos

[Como interactuan componentes]

## 6. Dependencias

- [Dependencia 1]

## 7. Impacto

### 7.1 Cambios Breaking

### 7.2 Migracion

## 8. Plan de Rollback

[Como revertir si falla]

## 9. Testing

### 9.1 Casos de Prueba

TC-001: [Descripcion]
- Input: [Entrada]
- Output esperado: [Salida]

### 9.2 Criterios de Validacion

- [Criterio 1]

## 10. Referencias

- DA-001 -> requirements (YYYY-MM-DD-HH-MM-titulo.md) RF-003
```

PROCESO:
1. Generar archivo `YYYY-MM-DD-HH-MM-titulo.md`
2. **SOLICITAR APROBACION AL USUARIO**
3. **NO CONTINUAR SIN APROBACION EXPLICITA**

### FASE 3: Tasks (Tareas)

OBJETIVO: Definir pasos EXACTOS de implementacion

ARCHIVO: `YYYY-MM-DD-HH-MM-titulo.md`

CONTENIDO:
```markdown
# Tasks: [Titulo]

Basado en: archivo de design (YYYY-MM-DD-HH-MM-titulo.md)
Fecha: YYYY-MM-DD

## Resumen

Total tareas: 15
Estimacion total: 8 horas

## Fase Preparacion (1h)

TASK-001: Crear estructura de directorios
- Descripcion: Crear directorios segun design (YYYY-MM-DD-HH-MM-titulo.md)
- Archivos afectados: [Ninguno, solo mkdir]
- Comandos:
 ```bash
 mkdir -p source/path/to/
 ```
- Criterios exito: Directorios creados
- Dependencias: Ninguna
- Estimacion: 5 min

TASK-002: Crear archivos base
...

## Fase Implementacion Core (5h)

TASK-003: Implementar componente X
- Descripcion: [Detalle]
- Archivos afectados:
 - source/path/file.rst (NUEVO)
- Comandos:
 ```bash
 cat > source/path/file.rst <<'EOF'
 [contenido]
 EOF
 ```
- Criterios exito:
 - Archivo existe
 - Build sin errores
- Dependencias: TASK-001, TASK-002
- Estimacion: 45 min

...

## Fase Validacion (2h)

TASK-014: Validar build completo
- Descripcion: make clean html, linkcheck
- Comandos:
 ```bash
 make clean html
 make linkcheck
 ```
- Criterios exito: Exit code 0
- Dependencias: TASK-001 a TASK-013

TASK-015: Commit final
...

## Orden de Ejecucion

Secuencia:
1. TASK-001
2. TASK-002, TASK-003 (paralelo)
3. TASK-004 (depende de 002, 003)
...

## Checkpoints

CHECKPOINT-1: Despues de TASK-003
- Validar: Build exitoso

CHECKPOINT-2: Despues de TASK-010
- Validar: Tests pasan

## Rollback Points

Si falla TASK-005:
- Revertir commits desde TASK-003
- Eliminar archivos creados

## Notas

- Crear branch: feature/brief-desc
- Commits frecuentes (cada 2-3 tasks)
```

PROCESO:
1. Generar archivo `YYYY-MM-DD-HH-MM-titulo.md` detallado
2. **SOLICITAR APROBACION AL USUARIO**
3. **NO CONTINUAR SIN APROBACION EXPLICITA**

### FASE 4: Implementation (Implementacion)

OBJETIVO: EJECUTAR tareas definidas

DIRECTORIO: `implementation/`

PROCESO:
```bash
# Para cada TASK:

1. Anunciar: "EJECUTANDO TASK-XXX: [nombre]"

2. Seguir pasos EXACTOS de tasks (YYYY-MM-DD-HH-MM-titulo.md)

3. Validar criterios de exito

4. Commit (si indicado):
 git add [archivos]
 git commit -m "feat(scope): implement TASK-XXX - [nombre]"

5. Marcar como completada en tasks (YYYY-MM-DD-HH-MM-titulo.md):
 - [x] TASK-XXX: [nombre]

# Al finalizar:
1. Validacion final completa
2. Documentar en work-log
3. Mover a .mywork/specs/YYYY-MM-DD-brief-desc/
```

MANEJO DE ERRORES:

Si tarea falla:
1. Diagnosticar problema
2. Documentar en QUESTIONS.md
3. Decidir accion:
 - Fix inmediato y continuar
 - Pausar e investigar
 - Rollback a checkpoint anterior

Si design insuficiente:
1. Pausar implementacion
2. Volver a FASE 2
3. Actualizar design (YYYY-MM-DD-HH-MM-titulo.md)
4. Re-aprobar design
5. Actualizar tasks (YYYY-MM-DD-HH-MM-titulo.md)
6. Continuar implementacion

## Convenciones

### Naming

DIRECTORIO: `YYYY-MM-DD-brief-description`
- YYYY-MM-DD: Fecha de inicio
- brief-description: Kebab-case, max 30 chars

ARCHIVOS: `YYYY-MM-DD-HH-MM-titulo.md`
- HH-MM: hora/minuto de creacion
- titulo: kebab-case, max 50 chars (debe indicar fase: requirements/design/tasks)

EJEMPLOS:
- 2026-01-28-traducir-arc42-section-10
- 2026-01-28-refactor-sphinx-structure

### Estados

- Draft: En elaboracion
- Review: En revision
- Approved: Aprobado para implementacion
- In Progress: En implementacion
- Completed: Completado

### Referencias Entre Fases

Incluir en cada documento:
```markdown
Basado en: [archivo anterior]
Referencias:
- RF-001 (requirements YYYY-MM-DD-HH-MM-titulo.md)
- DA-003 (design YYYY-MM-DD-HH-MM-titulo.md)
```

## Ejemplo Completo

### 2026-01-28-09-10-requirements-traducir-arc42-sec-10.md
```markdown
# Requirements: Traducir arc42 Section 10

## Problema
Necesitamos documentacion de Quality Requirements traducida.

## Objetivos
Traducir seccion 10 de arc42 a español.

## Requisitos Funcionales

RF-001: Traducir todos los archivos de section 10
- Prioridad: Alta
- Criterio: Todos los .md traducidos a .rst

RF-002: Generar metadata completa
...
```

### 2026-01-28-10-00-design-traducir-arc42-sec-10.md
```markdown
# Design: Traducir arc42 Section 10

Basado en: archivo de requirements (YYYY-MM-DD-HH-MM-titulo.md)

## Decisiones

DA-001: Usar modo Alta Fidelidad
- Contexto: Es especificacion tecnica
- Decision: Aplicar alta_fidelidad
- Razon: Requiere precision maxima

## Estructura

```
sections/10_quality_requirements/
+-- original/
+-- traduccion/
| +-- index.rst
| +-- quality_tree.rst
| +-- scenarios.rst
+-- analisis_seccion.json
```
```

### 2026-01-28-10-30-tasks-traducir-arc42-sec-10.md
```markdown
# Tasks: Traducir arc42 Section 10

TASK-001: Analizar seccion
```bash
python scripts/analizar_seccion.py sections/10_quality_requirements/
```

TASK-002: Traducir con arc42_scraper
```bash
python scripts/traduccion/arc42_scraper_python.py --section 10
```

...
```

## Templates

Ver:
- templates/requirements.md.template (si aplica)
- templates/design.md.template (si aplica)
- templates/tasks.md.template (si aplica)

## Referencias

Metodologia basada en:
- TDD (Test-Driven Development)
- BDD (Behavior-Driven Development)
- ADR (Architecture Decision Records)

## Notas

- Spec-Driven NO es overhead, es inversion
- Ahorra tiempo en implementacion
- Documenta decisiones para futuro
- Facilita onboarding
- Permite rollback seguro

---

## Relaciones con Otras Skills

### changes-directory-management
- **Uso**: Crear y gestionar directorios en `.mywork/changes/`
- **Cuándo**: En FASE 1 (Requirements), al crear directorio de trabajo
- **Formato**: Usar `YYYY-MM-DD-HH-MM-brief-desc/` con timestamp completo
- **Referencia**: Ver `changes-directory-management` para procedimiento completo

### work-logger
- **Diferencia**: spec-driven-dev es para trabajo EN PROGRESO
- **Cuándo usar work-logger**: Al completar las 4 fases, crear log final
- **Flujo**:
  1. Trabajar en `.mywork/changes/YYYY-MM-DD-HH-MM-proyecto/` (spec-driven-dev)
  2. Al completar, crear `.mywork/work-logs/YYYY-MM-DD-HH-MM-proyecto.md` (work-logger)

### commit-helper
- **Uso**: Commits con mensajes estándar durante implementación
- **Cuándo**: En FASE 4 (Implementation), al hacer commits

---

## Changelog

### v1.1.0 - 2026-01-30

**Actualizaciones de formato**:
- ✅ DIRECTORIO actualizado: `YYYY-MM-DD-brief-desc/` → `YYYY-MM-DD-HH-MM-brief-desc/`
- ✅ Proceso FASE 1 actualizado con comando para crear directorio
- ✅ Añadida referencia a `changes-directory-management`
- ✅ Sección "Relaciones con Otras Skills" añadida

**Razón**:
- Estandarizar formato de directorios con timestamp completo
- Consistencia con `changes-directory-management` v1.0.0
- Mejorar trazabilidad temporal de proyectos

**Referencias**:
- changes-directory-management v1.0.0
- Renombrado de directorio actual (2026-01-30-15-17-correccion-completa-manual)

### v1.0.0 - 2026-01-29

- Versión inicial
- Metodología en 4 fases
- Templates y ejemplos
- Proceso de aprobación

---

## Changelog

### v1.2.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y decision-making**:

✅ **Decision Framework** - ¿Necesito Spec-Driven Development?
- 8 preguntas para decidir si usar metodología
- Regla de oro: ">2 horas O complejo → spec-driven"
- Clarifica cuándo NO usar (hotfixes, cambios triviales)

✅ **Trigger Patterns** - Cuándo aplicar spec-driven
- Señales explícitas (usuario dice "vamos a implementar")
- Señales implícitas (trabajo multi-fase, complejidad)
- Trigger words específicos
- Anti-triggers para evitar over-engineering

✅ **Self-Check Mechanisms** - Checks por fase
- Pre-Planning (justificar metodología, preparación)
- Durante cada FASE (1-4): checklists específicos
- Post-Implementation (completitud, criterios cumplidos)

**Líneas agregadas**: ~120 líneas

**Beneficio principal**:
- Usuarios deciden correctamente cuándo usar spec-driven
- Cada fase tiene checklist clara
- Previene planificación excesiva en cambios simples
- Asegura completitud en proyectos complejos

### v1.1.0 - 2026-01-30
- Actualización de templates
- Mejoras en estructura de fases
- Integración con changes-directory-management

### v1.0.0 - 2026-01-29
- Versión inicial
- Metodología en 4 fases
- Templates para Requirements, Design, Tasks
