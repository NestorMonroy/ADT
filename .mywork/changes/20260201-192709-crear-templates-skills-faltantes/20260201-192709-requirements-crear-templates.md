# Requirements: Crear Templates para Skills Faltantes

Fecha: 2026-02-01
Autor: Claude (AI Assistant)
Estado: Draft

## 1. Contexto

El proyecto ADT tiene 15 skills en `.codex/skills/` que proporcionan metodologías y guías para el desarrollo. Actualmente, solo 2 skills (13%) tienen directorios `templates/` con plantillas reutilizables: spec-driven-dev (3 templates) y work-logger (1 template).

Un análisis exhaustivo identificó que 7 skills adicionales se beneficiarían significativamente de tener templates, con 3 clasificados como alta prioridad. La falta de templates en estos skills críticos reduce la consistencia, aumenta la curva de aprendizaje y genera deuda técnica estimada en 8-11 horas.

Los templates existentes en spec-driven-dev y work-logger han demostrado ser de excelente calidad (9/10) y siguen mejores prácticas que deberían replicarse en otros skills.

## 2. Problema

**Problema principal**: Skills críticos del proyecto carecen de templates que guíen la generación de documentos estructurados, resultando en:

1. **Inconsistencia**: Usuarios generan documentos con formatos diferentes
2. **Curva de aprendizaje alta**: Sin plantillas, usuarios deben inferir formato correcto
3. **Pérdida de calidad**: Sin guía, documentos pueden omitir secciones importantes
4. **Falta de escalabilidad**: Nuevos colaboradores luchan por seguir convenciones

**Skills afectados (alta prioridad)**:
- **commit-helper**: Sin template para mensajes de commit → inconsistencia en formato Conventional Commits
- **skills-management**: Sin template para crear skills → nuevos skills pueden tener estructura diferente
- **incremental-correction-methodology**: Sin templates para documentar metodología → difícil seguir proceso estructurado

## 3. Objetivos

### 3.1 Objetivo Principal

Crear templates de alta calidad para los 3 skills de prioridad alta (commit-helper, skills-management, incremental-correction-methodology) que:
- Guíen la generación de documentos estructurados
- Aseguren consistencia en formatos
- Reduzcan curva de aprendizaje
- Repliquen calidad de templates existentes (9/10)

### 3.2 Objetivos Secundarios

- Documentar convención de templates en skills-management
- Establecer patrón reutilizable para futuros templates (media/baja prioridad)
- Reducir deuda técnica de 8-11h a 3-5h (resolviendo alta prioridad)
- Actualizar SKILL.md de cada skill para referenciar sus templates
- Crear ejemplos de uso en documentación
- **Crear skill de best practices oficiales de Anthropic para mejorar calidad de todos los skills futuros**

## 4. Requisitos Funcionales

### commit-helper

RF-001: Template de mensaje de commit
- Descripción: Crear `commit-helper/templates/commit-message.template` con formato Conventional Commits
- Prioridad: Alta
- Criterio de aceptación: 
  * Template incluye formato: type(scope): subject
  * Incluye secciones opcionales: body, footer
  * Tiene comentarios guía con ejemplos de types válidos
  * Lista scopes comunes del proyecto
  * Explica reglas: imperativo, no punto final, max 50 chars en subject
  * Tamaño: 30-50 líneas

RF-002: Documentación de template en commit-helper/SKILL.md
- Descripción: Agregar sección de templates en SKILL.md
- Prioridad: Alta
- Criterio de aceptación:
  * Sección "Templates" agregada
  * Referencia a commit-message.template
  * Ejemplo de uso del template
  * Líneas 20-30 aproximadamente

### skills-management

RF-003: Template principal de SKILL.md
- Descripción: Crear `skills-management/templates/SKILL.md.template` completo
- Prioridad: Alta
- Criterio de aceptación:
  * Incluye frontmatter YAML (name, description, version, created, updated)
  * Secciones: Descripción, Cuándo usar, Trigger Patterns, Decision Framework
  * Secciones: Self-Check, Procedimiento, Ejemplos, Relaciones
  * Sección: Changelog
  * Placeholders descriptivos con [corchetes]
  * Tamaño: 150-200 líneas (referencia completa)

RF-004: README en templates/ de skills-management
- Descripción: Crear `skills-management/templates/README.md`
- Prioridad: Media
- Criterio de aceptación:
  * Explica propósito de cada template
  * Guía de uso paso a paso
  * Mejores prácticas para templates
  * Tamaño: 50-80 líneas

RF-005: Documentación de templates en skills-management/SKILL.md
- Descripción: Actualizar SKILL.md para documentar templates
- Prioridad: Alta
- Criterio de aceptación:
  * Sección "Templates Disponibles"
  * Cuándo usar cada template
  * Ejemplo completo de creación de skill usando template

### incremental-correction-methodology

RF-006: Template de análisis inicial
- Descripción: Crear `incremental-correction-methodology/templates/analysis-phase.md.template`
- Prioridad: Alta
- Criterio de aceptación:
  * Secciones: Build output completo, Categorización de issues
  * Tablas para clasificación (tipo, severidad, archivos afectados)
  * Métricas: Total issues, por categoría, por prioridad
  * Tamaño: 60-80 líneas

RF-007: Template de plan de categorización
- Descripción: Crear `incremental-correction-methodology/templates/categorization-plan.md.template`
- Prioridad: Alta
- Criterio de aceptación:
  * Estrategia de categorización
  * Criterios de priorización
  * Plan de lotes (cuántos, tamaño, orden)
  * Tamaño: 50-70 líneas

RF-008: Template de log de ejecución
- Descripción: Crear `incremental-correction-methodology/templates/execution-log.md.template`
- Prioridad: Alta
- Criterio de aceptación:
  * Por lote: Issues abordados, Archivos modificados, Problemas encontrados
  * Checkpoints de validación
  * Métricas de progreso
  * Tamaño: 80-100 líneas

RF-009: Template de reporte final
- Descripción: Crear `incremental-correction-methodology/templates/final-report.md.template`
- Prioridad: Alta
- Criterio de aceptación:
  * Resumen ejecutivo
  * Métricas finales (antes/después)
  * Lecciones aprendidas
  * Problemas críticos encontrados
  * Tamaño: 70-90 líneas

RF-010: README en templates/ de incremental-correction
- Descripción: Crear `incremental-correction-methodology/templates/README.md`
- Prioridad: Media
- Criterio de aceptación:
  * Explica flujo de uso de los 4 templates
  * Orden: analysis → categorization → execution → final-report
  * Cuándo usar cada uno

RF-011: Documentación de templates en incremental-correction/SKILL.md
- Descripción: Actualizar SKILL.md
- Prioridad: Alta
- Criterio de aceptación:
  * Sección "Templates" agregada
  * Referencia a los 4 templates
  * Workflow de uso

### anthropic-best-practices

RF-012: Skill de best practices de Anthropic
- Descripción: Crear nuevo skill `anthropic-best-practices` transformando conocimiento de llms-full.txt
- Prioridad: Alta
- Criterio de aceptación:
  * Directorio `.codex/skills/anthropic-best-practices/` creado
  * SKILL.md con frontmatter, descripción, decision framework (150-200 líneas)
  * skill-authoring.md transformado de llms-full.txt (400-500 líneas)
  * prompting-tips.md transformado de llms-full.txt (300-400 líneas)
  * long-context-tips.md transformado de llms-full.txt (200-300 líneas)
  * README.md con guía de uso (100 líneas)
  * Contenido TRANSFORMADO (no copiado) con ejemplos adaptados a ADT
  * Principios extraídos en decision frameworks accionables

RF-013: Integración de anthropic-best-practices con skills existentes
- Descripción: Actualizar skills-management y otros para referenciar anthropic-best-practices
- Prioridad: Media
- Criterio de aceptación:
  * skills-management/SKILL.md referencia anthropic-best-practices en sección de creación de skills
  * skills-management/templates/ usa principios de anthropic-best-practices
  * project-context/SKILL.md incluye referencia a prompting best practices
  * translation-workflow/SKILL.md incluye referencia a long-context tips

## 5. Requisitos No Funcionales

RNF-001: Calidad de Templates
- Descripción: Templates deben alcanzar calidad comparable a spec-driven-dev
- Métrica: Evaluación cualitativa (estructura, claridad, utilidad)
- Umbral: Mínimo 8/10 (spec-driven-dev es 9/10)

RNF-002: Usabilidad
- Descripción: Templates deben ser fáciles de usar sin documentación externa
- Métrica: Placeholders auto-explicativos, comentarios guía
- Umbral: Usuario nuevo puede usarlos sin consultar SKILL.md

RNF-003: Consistencia
- Descripción: Templates siguen mismas convenciones que spec-driven-dev
- Métrica: Estructura similar, mismo estilo de placeholders
- Umbral: 100% consistente con patrón establecido

RNF-004: Mantenibilidad
- Descripción: Templates fáciles de actualizar en futuro
- Métrica: Estructura modular, comentarios claros
- Umbral: Actualización de template toma <30 minutos

RNF-005: Completitud
- Descripción: Templates cubren todos los casos de uso del skill
- Métrica: % de casos cubiertos
- Umbral: >90% de casos de uso comunes

## 6. Restricciones

### Técnicas
- Templates deben ser archivos Markdown (.md.template)
- Deben funcionar con editores de texto estándar (sin herramientas especiales)
- Deben seguir sintaxis Markdown estándar
- Placeholders usan [corchetes] como convención existente

### Organizacionales
- Tiempo disponible: 7-10 horas (alta prioridad + anthropic-best-practices)
- Templates deben integrarse en estructura actual de skills
- No modificar skills existentes más allá de agregar templates/
- Mantener retrocompatibilidad con workflows actuales

### De Formato
- Usar mismo estilo que spec-driven-dev
- Comentarios en español (idioma del proyecto)
- Secciones numeradas cuando corresponda
- Incluir frontmatter YAML donde sea apropiado

### De Proceso
- Seguir spec-driven-dev para este proyecto
- Cada template requiere validación antes de commit
- Documentación en SKILL.md es obligatoria

## 7. Fuera de Alcance

Explícito que NO se incluye en este proyecto:

- Templates para skills de media prioridad (translation-workflow, bash-production-scripting)
- Templates para skills de baja prioridad (sphinx-expert, validation-suite)
- Refactorización de templates existentes en spec-driven-dev o work-logger
- Automatización de generación de documentos desde templates
- Integración con herramientas externas (IDEs, editores especializados)
- Traducción de templates a otros idiomas
- Versionamiento automático de templates
- Templates para skills que no generan documentos estructurados

## 8. Stakeholders

| Stakeholder | Rol | Interés |
|-------------|-----|---------|
| Desarrolladores ADT | Usuarios de skills | Templates facilitan su trabajo diario |
| Nuevos colaboradores | Usuarios nuevos | Curva de aprendizaje más baja |
| Mantenedores del proyecto | Administradores | Consistencia y calidad aseguradas |
| Claude (AI Assistant) | Ejecutor | Seguir metodologías documentadas correctamente |

## 9. Supuestos

- Templates en formato Markdown son suficientes (no se requiere formato binario)
- Usuarios tienen familiaridad básica con Markdown
- Estructura actual de skills (directorio templates/ dentro de cada skill) es correcta
- Patrón de spec-driven-dev es el modelo a seguir
- 4-6 horas son suficientes para completar alta prioridad
- Templates serán mantenidos manualmente (no automatización)
- Convención [corchetes] para placeholders es adecuada
- Español es idioma correcto para todos los templates

## 10. Dependencias

### Dependencias de Documentación
- spec-driven-dev/templates/ - Modelo de referencia
- work-logger/templates/ - Ejemplo adicional
- Análisis completado: ANALISIS_TEMPLATES_SKILLS.md
- **llms-full.txt** - Documentación oficial de Anthropic (923K líneas)
- **ANALISIS_LLMS_FULL_TRANSFORMACION.md** - Análisis de contenido relevante

### Dependencias de Skills
- skills-management SKILL.md - Entender qué skill hace
- commit-helper SKILL.md - Entender formato de commits
- incremental-correction-methodology SKILL.md - Entender metodología

### Dependencias de Proyecto
- Directorio .mywork/changes/ debe existir
- Estructura .codex/skills/ debe mantenerse
- Git debe estar disponible para commits

## 11. Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Templates demasiado largos o complejos | Media | Medio | Basarse en spec-driven-dev (demostrado exitoso). Validar con casos de uso reales |
| Inconsistencia con patrón existente | Baja | Alto | Revisión cuidadosa contra spec-driven-dev. Checklist de consistencia |
| Falta de adopción por usuarios | Media | Alto | Documentar bien en SKILL.md. Incluir ejemplos claros. Hacer templates intuitivos |
| Tiempo insuficiente (>6 horas) | Baja | Medio | Priorización estricta. Comenzar con commit-helper (30 min quick win) |
| Templates se vuelven obsoletos | Media | Bajo | Incluir versionamiento. Documentar cuándo actualizar |
| Placeholders ambiguos | Media | Medio | Usar placeholders muy descriptivos. Incluir comentarios guía |
| Transformación literal en lugar de adaptación | Alta | Alto | Seguir proceso: extraer principios → adaptar a ADT → crear frameworks. NO copiar ejemplos de API |
| anthropic-best-practices demasiado grande | Media | Medio | Usar progressive disclosure. Mantener SKILL.md <200 líneas. Split en archivos |

## 12. Referencias

### Documentación Existente
- `.codex/skills/spec-driven-dev/SKILL.md` - Metodología
- `.codex/skills/spec-driven-dev/templates/` - Modelo de templates (3)
- `.codex/skills/work-logger/templates/` - Ejemplo adicional (1)
- `ANALISIS_TEMPLATES_SKILLS.md` - Análisis completo
- `TEMPLATES_RESUMEN.md` - Resumen ejecutivo
- Work-log: `2026-02-01-19-25-analisis-templates-skills.md`
- **`llms-full.txt`** - Docs oficiales de Anthropic (24MB, 923K líneas)
- **`ANALISIS_LLMS_FULL_TRANSFORMACION.md`** - Análisis y propuesta de transformación

### Secciones Clave de llms-full.txt
- Skill Authoring Best Practices (líneas 27212-28500)
- Prompting Best Practices (líneas 2382-2900)
- Long Context Prompting Tips (líneas 47737-47950)

### Skills Relacionados
- commit-helper v1.1.0
- skills-management v1.1.0
- incremental-correction-methodology v1.4.0
- spec-driven-dev v1.2.0

### Convenciones del Proyecto
- Conventional Commits - Formato de mensajes
- Markdown para toda documentación
- Español como idioma principal

## 13. Aprobación

- [ ] Revisado por: Usuario
- [ ] Aprobado por: Usuario
- [ ] Fecha de aprobación: 2026-02-01

**Nota**: Solicitar aprobación explícita antes de continuar a FASE 2 (Design)

## Historial de Cambios

| Fecha | Versión | Cambios | Autor |
|-------|---------|---------|-------|
| 2026-02-01 | 0.1 | Creación inicial | Claude (AI Assistant) |
| 2026-02-01 | 0.2 | Agregado RF-012 (anthropic-best-practices) y RF-013 (integración). Actualizado alcance, objetivos, restricciones, dependencias y riesgos | Claude (AI Assistant) |

---

**Estado**: Draft - Pendiente de aprobación (versión 0.2 con anthropic-best-practices)
**Próxima fase**: FASE 2 - Design (tras aprobación)
