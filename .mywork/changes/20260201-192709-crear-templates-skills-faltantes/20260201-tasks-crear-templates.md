# Tasks: Crear Templates para Skills Faltantes + anthropic-best-practices

Basado en: 20260201-200000-design-crear-templates.md (v0.2)
Fecha: 2026-02-01
Autor: Claude (AI Assistant)
Estado: Draft

## Resumen

Total de tareas: 28
Estimacion total: 8.5 horas (sin buffer)
Buffer recomendado: +20% = 10.2 horas
Fecha inicio estimada: 2026-02-01
Fecha fin estimada: 2026-02-01 (mismo día, sesión de trabajo)

## Fases de Implementacion

### FASE 1: Preparacion (Estimacion: 15 min)

**TASK-001: Crear directorios de templates para commit-helper**
- Descripcion: Crear estructura de directorio templates/ en commit-helper
- Archivos afectados:
  - .codex/skills/commit-helper/templates/ (NUEVO directorio)
- Comandos a ejecutar:
  ```bash
  cd /tmp/ADT
  mkdir -p .codex/skills/commit-helper/templates
  ```
- Criterios de exito:
  - Directorio .codex/skills/commit-helper/templates/ existe
  - Permisos correctos (755)
- Dependencias: Ninguna
- Estimacion: 2 minutos
- Estado: [ ] Pendiente

**TASK-002: Crear directorios de templates para skills-management**
- Descripcion: Crear estructura de directorio templates/ en skills-management
- Archivos afectados:
  - .codex/skills/skills-management/templates/ (NUEVO directorio)
- Comandos a ejecutar:
  ```bash
  cd /tmp/ADT
  mkdir -p .codex/skills/skills-management/templates
  ```
- Criterios de exito:
  - Directorio existe
- Dependencias: Ninguna
- Estimacion: 2 minutos
- Estado: [ ] Pendiente

**TASK-003: Crear directorios de templates para incremental-correction**
- Descripcion: Crear estructura de directorio templates/ en incremental-correction-methodology
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/templates/ (NUEVO directorio)
- Comandos a ejecutar:
  ```bash
  cd /tmp/ADT
  mkdir -p .codex/skills/incremental-correction-methodology/templates
  ```
- Criterios de exito:
  - Directorio existe
- Dependencias: Ninguna
- Estimacion: 2 minutos
- Estado: [ ] Pendiente

**TASK-004: Crear directorio para anthropic-best-practices**
- Descripcion: Crear estructura completa del nuevo skill
- Archivos afectados:
  - .codex/skills/anthropic-best-practices/ (NUEVO directorio)
- Comandos a ejecutar:
  ```bash
  cd /tmp/ADT
  mkdir -p .codex/skills/anthropic-best-practices
  ```
- Criterios de exito:
  - Directorio existe
- Dependencias: Ninguna
- Estimacion: 2 minutos
- Estado: [ ] Pendiente

**TASK-005: Verificar acceso a llms-full.txt**
- Descripcion: Confirmar que llms-full.txt está accesible para extracción
- Archivos afectados:
  - Ninguno (solo verificación)
- Comandos a ejecutar:
  ```bash
  ls -lh /mnt/user-data/uploads/llms-full.txt
  wc -l /mnt/user-data/uploads/llms-full.txt
  ```
- Criterios de exito:
  - Archivo existe
  - Tamaño correcto (~24MB)
  - Accesible para lectura
- Dependencias: Ninguna
- Estimacion: 1 minuto
- Estado: [ ] Pendiente

### FASE 2: Templates commit-helper (Estimacion: 30 min)

**TASK-006: Crear commit-message.template**
- Descripcion: Crear template de mensaje de commit Conventional Commits
- Archivos afectados:
  - .codex/skills/commit-helper/templates/commit-message.template (NUEVO)
- Contenido a incluir:
  - Formato: type(scope): subject
  - Secciones opcionales: body, footer
  - Comentarios guía con ejemplos de types (feat, fix, docs, style, refactor, test, chore)
  - Lista de scopes comunes del proyecto
  - Reglas: imperativo, no punto final, max 50 chars en subject
  - Ejemplos concretos
- Criterios de exito:
  - Template creado (30-50 líneas)
  - Sintaxis Markdown válida
  - Placeholders con formato [descripcion]
  - Comentarios guía claros
- Dependencias: TASK-001
- Estimacion: 20 minutos
- Estado: [ ] Pendiente

**TASK-007: Actualizar commit-helper/SKILL.md con sección Templates**
- Descripcion: Agregar sección documentando template en SKILL.md
- Archivos afectados:
  - .codex/skills/commit-helper/SKILL.md (MODIFICADO)
- Cambios a realizar:
  - Agregar sección "Templates" antes de "Changelog"
  - Referenciar commit-message.template
  - Ejemplo de uso del template
  - Workflow recomendado
- Criterios de exito:
  - Sección "Templates" agregada
  - Referencia correcta al archivo
  - Ejemplo claro de uso
- Dependencias: TASK-006
- Estimacion: 10 minutos
- Estado: [ ] Pendiente

### FASE 3: Templates skills-management (Estimacion: 1.5 horas)

**TASK-008: Crear SKILL.md.template**
- Descripcion: Crear template completo para crear skills
- Archivos afectados:
  - .codex/skills/skills-management/templates/SKILL.md.template (NUEVO)
- Contenido a incluir:
  - Frontmatter YAML (name, description, version, created, updated)
  - Secciones: Descripción, Cuándo usar, Trigger Patterns
  - Decision Framework
  - Self-Check
  - Procedimiento
  - Ejemplos
  - Relaciones con otros skills
  - Changelog
  - Placeholders descriptivos con [corchetes]
  - Comentarios guía basados en anthropic best practices
- Criterios de exito:
  - Template creado (150-200 líneas)
  - Estructura completa
  - Frontmatter YAML válido
  - Siguiendo patrón de spec-driven-dev y work-logger
- Dependencias: TASK-002
- Estimacion: 45 minutos
- Estado: [ ] Pendiente

**TASK-009: Crear README.md en skills-management/templates/**
- Descripcion: Crear guía de uso de templates
- Archivos afectados:
  - .codex/skills/skills-management/templates/README.md (NUEVO)
- Contenido a incluir:
  - Propósito de cada template
  - Guía de uso paso a paso
  - Mejores prácticas para usar templates
  - Referencia a anthropic-best-practices/skill-authoring.md
  - Ejemplos de creación de skill usando template
- Criterios de exito:
  - README creado (~100 líneas)
  - Guía clara y completa
  - Ejemplos específicos
- Dependencias: TASK-008
- Estimacion: 25 minutos
- Estado: [ ] Pendiente

**TASK-010: Actualizar skills-management/SKILL.md**
- Descripcion: Agregar sección Templates + referencia a anthropic-bp
- Archivos afectados:
  - .codex/skills/skills-management/SKILL.md (MODIFICADO)
- Cambios a realizar:
  - Agregar sección "Templates Disponibles"
  - Documentar SKILL.md.template
  - Referencia a anthropic-best-practices/skill-authoring.md
  - Workflow completo de creación de skill usando template
- Criterios de exito:
  - Sección agregada
  - Referencias correctas
  - Workflow documentado
- Dependencias: TASK-009
- Estimacion: 20 minutos
- Estado: [ ] Pendiente

### FASE 4: Templates incremental-correction (Estimacion: 2.5 horas)

**TASK-011: Crear analysis-phase.md.template**
- Descripcion: Template para análisis inicial de issues
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/templates/analysis-phase.md.template (NUEVO)
- Contenido a incluir:
  - Build output completo
  - Tabla de categorización (tipo, severidad, archivos)
  - Métricas: Total issues, por categoría, por prioridad
  - Análisis de patterns
  - Placeholders descriptivos
- Criterios de exito:
  - Template creado (60-80 líneas)
  - Tablas estructuradas
  - Secciones claras
- Dependencias: TASK-003
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

**TASK-012: Crear categorization-plan.md.template**
- Descripcion: Template para plan de categorización
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/templates/categorization-plan.md.template (NUEVO)
- Contenido a incluir:
  - Estrategia de categorización
  - Criterios de priorización
  - Plan de lotes (cuántos, tamaño, orden)
  - Estimación de tiempo por lote
- Criterios de exito:
  - Template creado (50-70 líneas)
  - Estructura lógica
  - Placeholders claros
- Dependencias: TASK-003
- Estimacion: 25 minutos
- Estado: [ ] Pendiente

**TASK-013: Crear execution-log.md.template**
- Descripcion: Template para log de ejecución por lotes
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/templates/execution-log.md.template (NUEVO)
- Contenido a incluir:
  - Por lote: Issues abordados, Archivos modificados
  - Problemas encontrados
  - Checkpoints de validación (build, linkcheck)
  - Métricas de progreso
  - Tabla de tracking
- Criterios de exito:
  - Template creado (80-100 líneas)
  - Tablas para tracking
  - Checkboxes para validación
- Dependencias: TASK-003
- Estimacion: 35 minutos
- Estado: [ ] Pendiente

**TASK-014: Crear final-report.md.template**
- Descripcion: Template para reporte final
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/templates/final-report.md.template (NUEVO)
- Contenido a incluir:
  - Resumen ejecutivo
  - Métricas finales (antes/después)
  - Lecciones aprendidas
  - Problemas críticos encontrados
  - Recomendaciones para futuro
  - Tabla comparativa
- Criterios de exito:
  - Template creado (70-90 líneas)
  - Métricas cuantificables
  - Secciones de learnings
- Dependencias: TASK-003
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

**TASK-015: Crear README.md en incremental-correction/templates/**
- Descripcion: Guía de workflow de uso de los 4 templates
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/templates/README.md (NUEVO)
- Contenido a incluir:
  - Explicación del flujo: analysis → categorization → execution → final-report
  - Cuándo usar cada template
  - Orden de ejecución
  - Ejemplos de uso
- Criterios de exito:
  - README creado (~100 líneas)
  - Flujo claro
  - Orden de uso documentado
- Dependencias: TASK-011, TASK-012, TASK-013, TASK-014
- Estimacion: 20 minutos
- Estado: [ ] Pendiente

**TASK-016: Actualizar incremental-correction/SKILL.md**
- Descripcion: Agregar sección Templates con workflow
- Archivos afectados:
  - .codex/skills/incremental-correction-methodology/SKILL.md (MODIFICADO)
- Cambios a realizar:
  - Agregar sección "Templates"
  - Referenciar los 4 templates
  - Documentar workflow de uso
  - Integrar con metodología existente
- Criterios de exito:
  - Sección agregada
  - Referencias a 4 templates
  - Workflow integrado
- Dependencias: TASK-015
- Estimacion: 20 minutos
- Estado: [ ] Pendiente

### FASE 5: anthropic-best-practices (Estimacion: 3.5 horas)

**TASK-017: Extraer y transformar skill-authoring content**
- Descripcion: Transformar líneas 27212-28500 de llms-full.txt a contenido ADT
- Archivos afectados:
  - .codex/skills/anthropic-best-practices/skill-authoring.md (NUEVO)
- Proceso de transformación:
  1. Extraer sección de llms-full.txt
  2. Identificar principios clave
  3. Adaptar ejemplos a contexto ADT (arc42, Sphinx, RST)
  4. Crear decision frameworks accionables
  5. Eliminar referencias a API calls
  6. Traducir a español
- Contenido a incluir:
  - Principios (conciso, degrees of freedom, testing)
  - Estructura de skills (naming, descriptions)
  - Progressive disclosure patterns
  - Workflows y feedback loops
  - Content guidelines
  - Common patterns
  - Evaluation and iteration
  - Ejemplos ADT
- Criterios de exito:
  - Archivo creado (400-500 líneas)
  - Contenido TRANSFORMADO (no copiado)
  - Ejemplos específicos de ADT
  - En español
  - Decision frameworks presentes
- Dependencias: TASK-004, TASK-005
- Estimacion: 1 hora
- Estado: [ ] Pendiente

**TASK-018: Extraer y transformar prompting-tips content**
- Descripcion: Transformar líneas 2382-2900 de llms-full.txt a contenido ADT
- Archivos afectados:
  - .codex/skills/anthropic-best-practices/prompting-tips.md (NUEVO)
- Proceso de transformación:
  1. Extraer sección de llms-full.txt
  2. Identificar técnicas de prompting Claude 4.5
  3. Adaptar a workflows de ADT
  4. Crear ejemplos con contexto ADT
  5. Traducir a español
- Contenido a incluir:
  - General principles (be explicit, add context)
  - Long-horizon reasoning
  - Context awareness (Claude 4.5 específico)
  - Multi-window workflows
  - State management best practices
  - Communication style
  - Tool usage patterns
  - Ejemplos ADT
- Criterios de exito:
  - Archivo creado (300-400 líneas)
  - Contenido transformado
  - Tips específicos Claude 4.5
  - Ejemplos ADT
  - En español
- Dependencias: TASK-004, TASK-005
- Estimacion: 1 hora
- Estado: [ ] Pendiente

**TASK-019: Extraer y transformar long-context-tips content**
- Descripcion: Transformar líneas 47737-47950 de llms-full.txt a contenido ADT
- Archivos afectados:
  - .codex/skills/anthropic-best-practices/long-context-tips.md (NUEVO)
- Proceso de transformación:
  1. Extraer sección de llms-full.txt
  2. Identificar técnicas para documentos largos
  3. Adaptar a casos de uso ADT (traducción arc42, análisis docs)
  4. Crear ejemplos con XML structure para ADT
  5. Traducir a español
- Contenido a incluir:
  - Essential tips (data at top, query at end)
  - XML structure for documents
  - Ground responses in quotes
  - Ejemplos ADT (traducción de sections, análisis de documentación)
  - Decision framework
- Criterios de exito:
  - Archivo creado (200-300 líneas)
  - Contenido transformado
  - Ejemplos específicos de traducción y análisis
  - En español
- Dependencias: TASK-004, TASK-005
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

**TASK-020: Crear anthropic-best-practices/SKILL.md**
- Descripcion: Crear SKILL.md overview con decision framework
- Archivos afectados:
  - .codex/skills/anthropic-best-practices/SKILL.md (NUEVO)
- Contenido a incluir:
  - Frontmatter YAML (name, description, version, created, updated)
  - Description + Cuándo Usar
  - Decision Framework (guía a skill-authoring, prompting-tips o long-context-tips)
  - Trigger Patterns
  - Self-Check
  - Referencias a los 3 archivos
  - Changelog
- Criterios de exito:
  - SKILL.md creado (150-200 líneas)
  - Decision framework claro
  - Referencias correctas a 3 archivos
  - Frontmatter válido
- Dependencias: TASK-017, TASK-018, TASK-019
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

**TASK-021: Crear anthropic-best-practices/README.md**
- Descripcion: Crear guía de uso del skill
- Archivos afectados:
  - .codex/skills/anthropic-best-practices/README.md (NUEVO)
- Contenido a incluir:
  - Overview del skill
  - Cuándo consultar cada archivo
  - Flujo de uso recomendado
  - Integración con otros skills
  - Ejemplos de casos de uso
- Criterios de exito:
  - README creado (~100 líneas)
  - Guía clara
  - Casos de uso documentados
- Dependencias: TASK-020
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

### FASE 6: Integracion (Estimacion: 30 min)

**TASK-022: Actualizar project-context/SKILL.md**
- Descripcion: Agregar referencia a anthropic-bp/prompting-tips.md
- Archivos afectados:
  - .codex/skills/project-context/SKILL.md (MODIFICADO)
- Cambios a realizar:
  - Agregar sección sobre prompting best practices
  - Referencia a anthropic-best-practices/prompting-tips.md
  - Cuándo consultar
- Criterios de exito:
  - Referencia agregada
  - Path correcto
  - Contexto claro de cuándo usar
- Dependencias: TASK-021
- Estimacion: 10 minutos
- Estado: [ ] Pendiente

**TASK-023: Actualizar translation-workflow/SKILL.md**
- Descripcion: Agregar referencia a anthropic-bp/long-context-tips.md
- Archivos afectados:
  - .codex/skills/translation-workflow/SKILL.md (MODIFICADO)
- Cambios a realizar:
  - Agregar sección sobre trabajar con documentos largos
  - Referencia a anthropic-best-practices/long-context-tips.md
  - Integrar con workflow de traducción
- Criterios de exito:
  - Referencia agregada
  - Path correcto
  - Integración con workflow existente
- Dependencias: TASK-021
- Estimacion: 10 minutos
- Estado: [ ] Pendiente

**TASK-024: Verificar referencias cruzadas**
- Descripcion: Validar que todas las referencias entre skills funcionan
- Comandos a ejecutar:
  ```bash
  # Verificar que archivos referenciados existen
  cd /tmp/ADT/.codex/skills
  
  # Buscar todas las referencias
  grep -r "anthropic-best-practices" */SKILL.md
  
  # Verificar que paths son correctos
  # Para cada referencia, verificar que archivo existe
  ```
- Criterios de exito:
  - Todas las referencias apuntan a archivos existentes
  - Paths correctos
  - Sin referencias rotas
- Dependencias: TASK-022, TASK-023
- Estimacion: 10 minutos
- Estado: [ ] Pendiente

### FASE 7: Validacion (Estimacion: 1 hora)

**TASK-025: Validar sintaxis de templates**
- Descripcion: Verificar que templates tienen sintaxis válida
- Comandos a ejecutar:
  ```bash
  cd /tmp/ADT
  
  # Verificar sintaxis Markdown
  for template in .codex/skills/*/templates/*.template; do
    # Linter Markdown (si disponible)
    echo "Validando: $template"
  done
  
  # Verificar frontmatter YAML en SKILL.md.template
  ```
- Criterios de exito:
  - Sintaxis Markdown válida en todos los templates
  - Frontmatter YAML válido donde aplica
  - Sin errores de formato
- Dependencias: TASK-006, TASK-008, TASK-011, TASK-012, TASK-013, TASK-014
- Estimacion: 15 minutos
- Estado: [ ] Pendiente

**TASK-026: Validar anthropic-best-practices skill**
- Descripcion: Verificar que skill anthropic-bp es válido y completo
- Comandos a ejecutar:
  ```bash
  cd /tmp/ADT/.codex/skills/anthropic-best-practices
  
  # Verificar estructura
  ls -la
  
  # Verificar SKILL.md tiene frontmatter válido
  head -20 SKILL.md
  
  # Verificar que archivos referenciados existen
  grep -o '\[.*\.md\]' SKILL.md
  ```
- Criterios de exito:
  - SKILL.md con frontmatter válido
  - 3 archivos de contenido existen
  - README.md existe
  - Decision framework funciona
  - Referencias internas correctas
- Dependencias: TASK-017, TASK-018, TASK-019, TASK-020, TASK-021
- Estimacion: 15 minutos
- Estado: [ ] Pendiente

**TASK-027: Testing de casos de prueba del Design**
- Descripcion: Ejecutar casos de prueba TC-001 a TC-007 del Design
- Casos a probar:
  - TC-001: Template commit-message es usable
  - TC-002: Template SKILL.md genera skill válido
  - TC-003: anthropic-bp es accesible
  - TC-004: Decision framework funciona
  - TC-005: Contenido transformado (no literal)
  - TC-006: Ejemplos son específicos de ADT
  - TC-007: Referencias cruzadas funcionan
- Criterios de exito:
  - Todos los TC pasan
  - Templates generan documentos válidos
  - anthropic-bp es usable
  - Contenido transformado correctamente
- Dependencias: TASK-025, TASK-026
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

### FASE 8: Finalizacion (Estimacion: 45 min)

**TASK-028: Crear work-log de implementación**
- Descripcion: Documentar todo el trabajo realizado
- Archivos afectados:
  - .mywork/work-logs/2026-02-01-[timestamp]-crear-templates-anthropic-bp.md (NUEVO)
- Contenido a incluir:
  - Resumen ejecutivo
  - Contexto (por qué se hizo)
  - Trabajo realizado (todas las fases)
  - Decisiones tomadas (referencias a Design)
  - Problemas encontrados (si hubo)
  - Archivos afectados (lista completa)
  - Comandos clave
  - Resultados (métricas)
  - Aprendizajes
  - Referencias
  - Próximos pasos
- Criterios de exito:
  - Work-log creado usando template de work-logger
  - Completo y detallado
  - Decisiones documentadas
  - Problemas registrados
- Dependencias: TASK-027
- Estimacion: 30 minutos
- Estado: [ ] Pendiente

## Orden de Ejecucion

Representacion de dependencias (DAG):

```
FASE 1 (Preparacion):
TASK-001, TASK-002, TASK-003, TASK-004, TASK-005 (paralelo)
   |        |         |         |         |
   v        v         v         v         v

FASE 2:    FASE 3:   FASE 4:   FASE 5:
TASK-006   TASK-008  TASK-011  TASK-017
   |          |       TASK-012  TASK-018
TASK-007   TASK-009  TASK-013  TASK-019
           TASK-010  TASK-014     |
                        |         v
                     TASK-015  TASK-020
                        |         |
                     TASK-016  TASK-021
                                  |
                                  v
FASE 6 (Integracion):
TASK-022, TASK-023
   |        |
   v        v
TASK-024
   |
   v
FASE 7 (Validacion):
TASK-025, TASK-026
   |        |
   v        v
TASK-027
   |
   v
FASE 8 (Finalizacion):
TASK-028
```

Secuencia lineal recomendada:
1. FASE 1: TASK-001 a TASK-005 (preparación - pueden ejecutarse en paralelo)
2. FASE 2: TASK-006 a TASK-007 (commit-helper templates)
3. FASE 3: TASK-008 a TASK-010 (skills-management templates)
4. FASE 4: TASK-011 a TASK-016 (incremental-correction templates)
5. FASE 5: TASK-017 a TASK-021 (anthropic-best-practices completo)
6. FASE 6: TASK-022 a TASK-024 (integración)
7. FASE 7: TASK-025 a TASK-027 (validación)
8. FASE 8: TASK-028 (finalización)

## Checkpoints

**CHECKPOINT-1: Después de TASK-007 (commit-helper completo)**
- Validar: Template commit-message existe y es usable
- Ejecutar: Abrir template y verificar placeholders
- Resultado esperado: Template funcional

**CHECKPOINT-2: Después de TASK-010 (skills-management completo)**
- Validar: Template SKILL.md es completo
- Ejecutar: Verificar todas las secciones presentes
- Resultado esperado: Template de 150-200 líneas funcional

**CHECKPOINT-3: Después de TASK-016 (incremental-correction completo)**
- Validar: 4 templates + README funcionan
- Ejecutar: Verificar workflow documentado
- Resultado esperado: Suite completa de templates

**CHECKPOINT-4: Después de TASK-021 (anthropic-bp completo)**
- Validar: Skill completo con 3 archivos de contenido
- Ejecutar: Verificar decision framework y referencias
- Resultado esperado: Skill funcional y usable

**CHECKPOINT-5: Después de TASK-024 (integración completa)**
- Validar: Referencias cruzadas funcionan
- Ejecutar: Verificar paths correctos
- Resultado esperado: Sin referencias rotas

**CHECKPOINT-6: Después de TASK-027 (validación completa)**
- Validar: Todos los TC pasan
- Ejecutar: Suite completa de testing
- Resultado esperado: 7/7 casos de prueba pasan

## Rollback Points

**Si falla TASK-006 o TASK-008 (templates principales):**
- Eliminar template incompleto
- Revisar Design para estructura correcta
- Re-crear template

**Si falla TASK-017, TASK-018 o TASK-019 (transformación de llms-full.txt):**
- Revisar proceso de transformación (Design DA-004)
- Asegurar que no se está copiando literalmente
- Verificar que ejemplos son específicos de ADT
- Re-transformar sección

**Si falla TASK-027 (testing):**
- Identificar qué TC específico falla
- Revisar task relacionada
- Corregir issue
- Re-ejecutar testing

**Si falla TASK-024 (referencias cruzadas):**
- Verificar paths uno por uno
- Corregir referencias incorrectas
- Re-validar

## Estimacion de Tiempo

| Fase | Tareas | Estimacion |
|------|--------|------------|
| Preparacion | TASK-001 a TASK-005 | 15 min |
| commit-helper | TASK-006 a TASK-007 | 30 min |
| skills-management | TASK-008 a TASK-010 | 1.5h |
| incremental-correction | TASK-011 a TASK-016 | 2.5h |
| anthropic-best-practices | TASK-017 a TASK-021 | 3.5h |
| Integracion | TASK-022 a TASK-024 | 30 min |
| Validacion | TASK-025 a TASK-027 | 1h |
| Finalizacion | TASK-028 | 45 min |
| **TOTAL** | 28 tareas | **8.5h** |

Buffer recomendado: +20% = **10.2 horas total**

## Notas de Implementacion

### Estrategia de Ejecución

**Opción A: Secuencial completa** (recomendada)
- Ejecutar todas las tareas en orden
- Checkpoints después de cada fase
- Más seguro, menos riesgo

**Opción B: Por fases**
- Completar FASE 2, validar, continuar
- Commits por fase
- Permite pausar entre fases

**Opción C: Paralelo parcial**
- TASK-006 a TASK-021 pueden ejecutarse en paralelo si hay recursos
- FASE 7 y 8 deben ser secuenciales

### Commits

Hacer commit después de cada checkpoint:
- Después de CHECKPOINT-1: `feat(commit-helper): add commit-message template`
- Después de CHECKPOINT-2: `feat(skills-management): add SKILL.md template and README`
- Después de CHECKPOINT-3: `feat(incremental-correction): add 4 templates and workflow`
- Después de CHECKPOINT-4: `feat(anthropic-best-practices): add new skill with best practices`
- Después de CHECKPOINT-5: `feat(integration): add cross-references to anthropic-bp`
- Después de CHECKPOINT-6: `test: validate all templates and anthropic-bp skill`
- Después de TASK-028: `docs: add work-log for templates and anthropic-bp implementation`

Formato de commits: `type(scope): brief description`

### Manejo de Errores

**Si template es muy largo (>esperado)**:
- Revisar DA-005 del Design (nivel de detalle)
- Considerar split si >500 líneas
- Documentar decisión

**Si transformación de llms-full.txt resulta en copia literal**:
- STOP inmediatamente
- Revisar DA-004 proceso de transformación
- Re-hacer transformación correctamente
- CRÍTICO: NO copiar literalmente

**Si referencias cruzadas no funcionan**:
- Verificar paths relativos vs absolutos
- Usar paths relativos desde skill
- Ejemplo: `../anthropic-best-practices/skill-authoring.md`

### Comunicacion

- Anunciar inicio de cada fase
- Reportar completion de cada checkpoint
- Alertar de problemas inmediatamente (especialmente transformación literal)

## QUESTIONS.md (Pendientes Durante Implementacion)

Si surgen preguntas durante implementacion, documentar aqui:

[Espacio para documentar preguntas que surjan durante ejecución]

## Aprobacion

- [ ] Tasks revisadas
- [ ] Estimaciones validadas
- [ ] Orden de ejecucion verificado
- [ ] Aprobado por: Usuario
- [ ] Fecha aprobacion: 2026-02-01

## Historial de Cambios

| Fecha | Cambios | Autor |
|-------|---------|-------|
| 2026-02-01 | Creacion inicial | Claude (AI Assistant) |

---

Estado: Draft - Pendiente de aprobacion
Proxima fase: FASE 4 - Implementation (tras aprobacion)

NOTA: Archivo sigue convención DA-009 (naming auto-documentado)
