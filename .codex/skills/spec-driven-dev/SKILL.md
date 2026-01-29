---
name: spec-driven-dev
description: "Desarrollo guiado por especificaciones en 4 fases. Usar para features complejas, cambios arquitectonicos, o cualquier trabajo que requiera planificacion estructurada."
---

# Spec-Driven Development

## Cuando usar

- Features complejas
- Cambios arquitectonicos
- Traducciones grandes (multi-seccion)
- Refactorings importantes
- Implementacion de workflows nuevos

## Metodologia en 4 Fases

### FASE 1: Requirements (Requerimientos)

OBJETIVO: Definir QUE se necesita

DIRECTORIO: `.mywork/changes/YYYY-MM-DD-brief-desc/`

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
1. Crear directorio de trabajo
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
