# Design: Crear Templates para Skills Faltantes + anthropic-best-practices

Basado en: 20260201-192709-requirements-crear-templates.md (v0.2)
Fecha: 2026-02-01
Autor: Claude (AI Assistant)
Estado: Draft

## 1. Vision General

Este diseño implementa una solución de doble objetivo:

**Objetivo 1**: Crear templates para 3 skills de alta prioridad (commit-helper, skills-management, incremental-correction-methodology) que guiarán la generación de documentos estructurados y asegurarán consistencia en el proyecto.

**Objetivo 2**: Crear skill anthropic-best-practices que consolida conocimiento oficial de Anthropic sobre skill authoring, prompting y manejo de contexto largo, transformado del archivo llms-full.txt.

La solución aprovecha sinergia entre ambos objetivos: los templates se diseñarán siguiendo los principios de anthropic-best-practices, y el skill de best practices proporcionará la base teórica para crear mejores skills en el futuro.

Arquitectura general:
- Templates usan progressive disclosure pattern (de spec-driven-dev)
- anthropic-best-practices sigue mismo patrón con 4 archivos de referencia
- Integración con skills existentes mediante referencias cruzadas
- Todo el contenido en español (idioma del proyecto)

## 2. Decisiones Arquitectonicas

### DA-001: Estructura de Templates - Archivos Individuales vs Directorio templates/

**Contexto**: Cada skill necesita templates accesibles. Opciones son: (A) archivos sueltos en raíz del skill, (B) directorio templates/ dentro del skill, (C) directorio templates/ global compartido.

**Decision**: Usar directorio templates/ dentro de cada skill (opción B)

**Alternativas consideradas**:
- Alternativa A (archivos sueltos): Rechazada porque contamina directorio raíz del skill, dificulta organización cuando hay múltiples templates
- Alternativa C (templates/ global): Rechazada porque acopla skills innecesariamente, dificulta portabilidad individual de skills

**Consecuencias**:
- Positivas: 
  * Organización clara (templates/ es obvio)
  * Portabilidad (copiar skill incluye sus templates)
  * Escalabilidad (fácil agregar más templates)
  * Consistencia (spec-driven-dev y work-logger ya usan este patrón)
- Negativas:
  * Un directorio más por skill (overhead mínimo)

**Referencias**: RF-001 a RF-011, patrón de spec-driven-dev

---

### DA-002: Naming Convention para Templates - .template vs .md.template

**Contexto**: Archivos template necesitan extensión que indique: (1) que son templates, (2) qué tipo de archivo generan.

**Decision**: Usar formato nombre.tipo.template (ej: commit-message.template, SKILL.md.template)

**Alternativas consideradas**:
- Alternativa A (solo .template): Rechazada porque no indica tipo de archivo resultante
- Alternativa B (.tpl): Rechazada porque .template es más explícito y auto-documentado

**Consecuencias**:
- Positivas:
  * Auto-documentado (se ve claramente qué genera)
  * Sintaxis highlighting funciona (editores reconocen .md)
  * Consistente con spec-driven-dev
- Negativas:
  * Nombre de archivo más largo (aceptable)

**Referencias**: RF-001 a RF-011

---

### DA-003: anthropic-best-practices - Progressive Disclosure Pattern

**Contexto**: anthropic-best-practices contendrá ~1500 líneas de contenido transformado. Opciones: (A) todo en SKILL.md, (B) SKILL.md + archivos de referencia, (C) múltiples skills separados.

**Decision**: SKILL.md (150-200 líneas) + 3 archivos de referencia (opción B)

**Alternativas consideradas**:
- Alternativa A (todo en SKILL.md): Rechazada porque viola principio "Keep SKILL.md under 500 lines" de Anthropic best practices
- Alternativa C (skills separados): Rechazada porque fragmenta conocimiento cohesivo y aumenta mantenimiento

**Consecuencias**:
- Positivas:
  * Sigue best practice oficial (SKILL.md <500 líneas)
  * Claude solo carga archivo relevante cuando necesario
  * Estructura modular fácil de mantener
  * Decision framework en SKILL.md guía a archivos específicos
- Negativas:
  * Usuario debe navegar entre archivos (mitigado con decision framework claro)

**Referencias**: RF-012, líneas 27212-28500 de llms-full.txt

---

### DA-004: Transformación de Contenido - Extracción vs Copia Literal

**Contexto**: llms-full.txt contiene documentación de API con ejemplos específicos. Necesitamos contenido útil para ADT sin copiar literalmente.

**Decision**: Proceso de transformación en 4 pasos: (1) Extraer principios clave, (2) Adaptar a contexto ADT, (3) Crear decision frameworks, (4) Agregar ejemplos ADT

**Alternativas consideradas**:
- Alternativa A (copia literal): Rechazada porque contenido es específico de API, no aplicable directamente a ADT
- Alternativa B (parafraseo simple): Rechazada porque pierde oportunidad de adaptar a workflows ADT

**Consecuencias**:
- Positivas:
  * Contenido relevante y accionable para ADT
  * Ejemplos específicos de arc42, Sphinx, RST
  * Decision frameworks útiles
  * No viola copyright (contenido transformado)
- Negativas:
  * Requiere más esfuerzo que copia (aceptable, valor justifica)

**Referencias**: RF-012, ANALISIS_LLMS_FULL_TRANSFORMACION.md

---

### DA-005: Nivel de Detalle en Templates - Completo vs Minimalista

**Contexto**: Templates pueden ser exhaustivos (como spec-driven-dev 111 líneas) o minimalistas (20-30 líneas).

**Decision**: Templates completos para skills-management, moderados para commit-helper e incremental-correction

**Alternativas consideradas**:
- Alternativa A (todos minimalistas): Rechazada porque usuarios omiten secciones importantes
- Alternativa B (todos exhaustivos): Rechazada porque intimida en casos simples

**Consecuencias**:
- Positivas:
  * skills-management template es referencia completa (alta calidad)
  * commit-helper template es conciso (apropiado para uso frecuente)
  * Balance entre guía y usabilidad
- Negativas:
  * Mantener templates grandes requiere más esfuerzo

**Referencias**: RF-003, RF-006 a RF-009

---

### DA-006: Integración con Skills Existentes - Referencias vs Duplicación

**Contexto**: anthropic-best-practices tiene conocimiento que beneficia skills-management, project-context, translation-workflow.

**Decision**: Referencias cruzadas explícitas en SKILL.md de cada skill afectado

**Alternativas consideradas**:
- Alternativa A (duplicar contenido): Rechazada porque dificulta mantenimiento y actualización
- Alternativa B (no integrar): Rechazada porque usuarios no descubrirían sinergias

**Consecuencias**:
- Positivas:
  * Una fuente de verdad (anthropic-best-practices)
  * Fácil descubrimiento de conocimiento relevante
  * Actualización centralizada
- Negativas:
  * Requiere mantener referencias actualizadas cuando skills cambian

**Referencias**: RF-013

---

### DA-007: Idioma de Templates y Best Practices - Español vs Inglés

**Contexto**: Proyecto ADT está en español, pero llms-full.txt está en inglés.

**Decision**: Todo contenido en español, incluyendo transformación de llms-full.txt

**Alternativas consideradas**:
- Alternativa A (inglés): Rechazada porque rompe consistencia del proyecto
- Alternativa B (bilingüe): Rechazada porque duplica mantenimiento sin beneficio claro

**Consecuencias**:
- Positivas:
  * Consistencia total del proyecto
  * Accesible para colaboradores hispanohablantes
- Negativas:
  * Traducción de conceptos técnicos requiere cuidado (pero ya hay convención establecida en ADT)

**Referencias**: Convenciones del proyecto, RF-012

---

### DA-008: Versionamiento de Templates - Incluir vs Omitir

**Contexto**: Templates pueden cambiar con el tiempo. Necesitamos forma de trackear cambios.

**Decision**: Sin versionamiento individual de templates, usar versionamiento de skill contenedor

**Alternativas consideradas**:
- Alternativa A (versión en cada template): Rechazada porque aumenta complejidad innecesariamente
- Alternativa B (sin tracking): Rechazada porque dificulta entender evolución

**Consecuencias**:
- Positivas:
  * Simplicidad (solo SKILL.md tiene versión)
  * Changelog de skill documenta cambios en templates
  * Menos overhead
- Negativas:
  * No se puede ver versión de template individual aisladamente (aceptable)

**Referencias**: RNF-004 (Mantenibilidad)

---

### DA-009: Naming Convention - Nombres Específicos Auto-documentados

**Contexto**: Archivos en directorios de trabajo (.mywork/changes/) necesitan nombres que documenten su propósito sin necesidad de abrir el archivo.

**Decision**: Usar nombres específicos auto-documentados en formato TIPO_descripcion_especifica.md

**Regla de oro**: Nombre debe ser auto-documentado sin ver contenido

**Ejemplos correctos**:
- PLAN_estrategia_correccion.md (NO solo PLAN.md)
- ANALISIS_230_warnings_sphinx.md (NO solo ANALISIS.md)
- DECISIONES_manual_vs_script.md (NO solo DECISIONES.md)
- FASE-0-preparacion.md (específico)
- 20260201-192709-requirements-crear-templates.md (específico con timestamp)

**Excepción**: Templates dentro de .codex/skills/
- .codex/skills/commit-helper/templates/commit-message.template (OK - genérico)
- .codex/skills/skills-management/templates/SKILL.md.template (OK - genérico)
- .codex/skills/*/templates/README.md (OK - contexto claro por ubicación)

**Alternativas consideradas**:
- Alternativa A (nombres genéricos siempre): Rechazada porque dificulta navegación en directorios con múltiples archivos
- Alternativa B (nombres específicos siempre, incluso templates): Rechazada porque templates ya tienen contexto por ubicación

**Consecuencias**:
- Positivas:
  * Archivos auto-documentados (ls -la es suficiente para entender contenido)
  * Fácil búsqueda (grep por nombre de archivo)
  * Menos confusión en directorios con múltiples documentos
- Negativas:
  * Nombres de archivo más largos (aceptable, claridad > brevedad)

**Referencias**: Convención de proyecto ADT, evitar antipatrón de nombres genéricos

## 3. Componentes Afectados

### 3.1 Nuevos Componentes

| Componente | Ubicacion | Proposito |
|------------|-----------|-----------|
| commit-helper templates/ | .codex/skills/commit-helper/templates/ | Directorio de templates para commit-helper |
| commit-message.template | .codex/skills/commit-helper/templates/commit-message.template | Template de mensaje Conventional Commits |
| skills-management templates/ | .codex/skills/skills-management/templates/ | Directorio de templates para skills-management |
| SKILL.md.template | .codex/skills/skills-management/templates/SKILL.md.template | Template completo para crear skills |
| skills-management README | .codex/skills/skills-management/templates/README.md | Guía de uso de templates |
| incremental-correction templates/ | .codex/skills/incremental-correction-methodology/templates/ | Directorio de templates para metodología |
| analysis-phase.md.template | .codex/skills/incremental-correction-methodology/templates/analysis-phase.md.template | Template análisis inicial |
| categorization-plan.md.template | .codex/skills/incremental-correction-methodology/templates/categorization-plan.md.template | Template plan de categorización |
| execution-log.md.template | .codex/skills/incremental-correction-methodology/templates/execution-log.md.template | Template log de ejecución |
| final-report.md.template | .codex/skills/incremental-correction-methodology/templates/final-report.md.template | Template reporte final |
| incremental README | .codex/skills/incremental-correction-methodology/templates/README.md | Guía de workflow de templates |
| anthropic-best-practices/ | .codex/skills/anthropic-best-practices/ | Nuevo skill completo |
| anthropic SKILL.md | .codex/skills/anthropic-best-practices/SKILL.md | Overview + decision framework |
| skill-authoring.md | .codex/skills/anthropic-best-practices/skill-authoring.md | Best practices de creación de skills |
| prompting-tips.md | .codex/skills/anthropic-best-practices/prompting-tips.md | Tips de prompting para Claude 4.5 |
| long-context-tips.md | .codex/skills/anthropic-best-practices/long-context-tips.md | Tips para documentos largos |
| anthropic README | .codex/skills/anthropic-best-practices/README.md | Guía de uso del skill |

### 3.2 Componentes Modificados

| Componente | Ubicacion | Cambios |
|------------|-----------|---------|
| commit-helper SKILL.md | .codex/skills/commit-helper/SKILL.md | Agregar sección "Templates" con referencia a commit-message.template |
| skills-management SKILL.md | .codex/skills/skills-management/SKILL.md | Agregar sección "Templates" y referencia a anthropic-best-practices |
| incremental-correction SKILL.md | .codex/skills/incremental-correction-methodology/SKILL.md | Agregar sección "Templates" con workflow de uso |
| project-context SKILL.md | .codex/skills/project-context/SKILL.md | Agregar referencia a anthropic-best-practices/prompting-tips.md |
| translation-workflow SKILL.md | .codex/skills/translation-workflow/SKILL.md | Agregar referencia a anthropic-best-practices/long-context-tips.md |

### 3.3 Componentes Deprecados

Ninguno. Este proyecto solo agrega componentes nuevos.

## 4. Estructura de Archivos

```
.codex/skills/
├── commit-helper/
│   ├── SKILL.md (MODIFICADO - agrega sección Templates)
│   └── templates/ (NUEVO)
│       └── commit-message.template (NUEVO - 30-50 líneas)
│
├── skills-management/
│   ├── SKILL.md (MODIFICADO - agrega sección Templates + ref a anthropic-bp)
│   └── templates/ (NUEVO)
│       ├── SKILL.md.template (NUEVO - 150-200 líneas)
│       └── README.md (NUEVO - 100 líneas)
│
├── incremental-correction-methodology/
│   ├── SKILL.md (MODIFICADO - agrega sección Templates)
│   └── templates/ (NUEVO)
│       ├── analysis-phase.md.template (NUEVO - 60-80 líneas)
│       ├── categorization-plan.md.template (NUEVO - 50-70 líneas)
│       ├── execution-log.md.template (NUEVO - 80-100 líneas)
│       ├── final-report.md.template (NUEVO - 70-90 líneas)
│       └── README.md (NUEVO - 100 líneas)
│
├── anthropic-best-practices/ (NUEVO SKILL COMPLETO)
│   ├── SKILL.md (NUEVO - 150-200 líneas)
│   │   Frontmatter YAML
│   │   Description + Cuándo Usar
│   │   Decision Framework (cuándo consultar cada archivo)
│   │   Trigger Patterns
│   │   Self-Check
│   │   Referencias a archivos
│   │   Changelog
│   │
│   ├── skill-authoring.md (NUEVO - 400-500 líneas transformadas)
│   │   Principios (conciso, degrees of freedom, testing)
│   │   Estructura (naming, descriptions)
│   │   Progressive disclosure patterns
│   │   Workflows y feedback loops
│   │   Content guidelines
│   │   Common patterns
│   │   Evaluation and iteration
│   │   Ejemplos ADT (arc42, Sphinx, RST)
│   │
│   ├── prompting-tips.md (NUEVO - 300-400 líneas transformadas)
│   │   General principles (be explicit, add context)
│   │   Long-horizon reasoning
│   │   Context awareness (Claude 4.5)
│   │   Multi-window workflows
│   │   State management
│   │   Communication style
│   │   Tool usage patterns
│   │   Ejemplos ADT
│   │
│   ├── long-context-tips.md (NUEVO - 200-300 líneas transformadas)
│   │   Essential tips (data at top, query at end)
│   │   XML structure for documents
│   │   Ground responses in quotes
│   │   Ejemplos ADT (traducción arc42)
│   │
│   └── README.md (NUEVO - 100 líneas)
│       Overview del skill
│       Cuándo consultar cada archivo
│       Flujo de uso recomendado
│       Integración con otros skills
│
├── project-context/
│   └── SKILL.md (MODIFICADO - agrega referencia a anthropic-bp/prompting-tips.md)
│
└── translation-workflow/
    └── SKILL.md (MODIFICADO - agrega referencia a anthropic-bp/long-context-tips.md)
```

## 5. Interfaces y Contratos

### 5.1 Template → Usuario

**Input**: Usuario necesita crear documento estructurado

**Proceso**:
1. Usuario identifica necesidad (ej: crear commit, crear skill, documentar metodología)
2. Usuario abre template apropiado
3. Usuario reemplaza placeholders con contenido específico
4. Usuario guarda archivo generado con nombre apropiado

**Output**: Documento completo siguiendo estructura estándar

**Contrato**:
- Templates DEBEN tener placeholders descriptivos con formato [descripcion]
- Templates DEBEN incluir comentarios guía donde necesario
- Templates DEBEN ser válidos en sintaxis (Markdown, YAML)

### 5.2 anthropic-best-practices → Skills Existentes

**Input**: Skill existente necesita conocimiento de best practices

**Proceso**:
1. SKILL.md del skill referencia archivo específico de anthropic-bp
2. Usuario lee archivo cuando necesario
3. Usuario aplica principios a su trabajo

**Output**: Trabajo de mayor calidad siguiendo best practices oficiales

**Contrato**:
- Referencias DEBEN ser explícitas (path completo)
- Contenido referenciado DEBE ser estable (no cambiar frecuentemente)

## 6. Flujos de Datos

### 6.1 Flujo de Creación de Commit

```
Usuario necesita commit
  → Lee commit-helper/SKILL.md
  → Abre commit-helper/templates/commit-message.template
  → Reemplaza placeholders (type, scope, subject, body, footer)
  → Copia contenido generado
  → Ejecuta git commit con mensaje
```

### 6.2 Flujo de Creación de Skill Nuevo

```
Usuario necesita crear skill
  → Lee skills-management/SKILL.md
  → Consulta anthropic-best-practices/skill-authoring.md (opcional pero recomendado)
  → Abre skills-management/templates/SKILL.md.template
  → Reemplaza placeholders
  → Guarda como .codex/skills/nuevo-skill/SKILL.md
  → Skill creado siguiendo best practices
```

### 6.3 Flujo de Optimización de Prompts

```
Usuario tiene problema con respuestas de Claude
  → Lee anthropic-best-practices/SKILL.md
  → Decision framework sugiere prompting-tips.md
  → Lee sección relevante
  → Aplica técnica (ej: "be more explicit", "add context")
  → Respuestas mejoran
```

### 6.4 Flujo de Trabajo con Documento Largo

```
Usuario necesita analizar/traducir documento grande
  → Lee anthropic-best-practices/SKILL.md
  → Decision framework sugiere long-context-tips.md
  → Lee tips (data at top, query at end, XML structure)
  → Aplica estructura recomendada
  → Análisis/traducción mejora 30%
```

## 7. Dependencias

### 7.1 Dependencias Internas

**Templates dependen de**:
- spec-driven-dev/templates/ (modelo de referencia)
- work-logger/templates/ (modelo de referencia)
- Convenciones de naming del proyecto

**anthropic-best-practices depende de**:
- llms-full.txt (fuente de contenido)
- ANALISIS_LLMS_FULL_TRANSFORMACION.md (guía de transformación)
- Convenciones de terminología de ADT

**Skills modificados dependen de**:
- anthropic-best-practices existiendo (para referencias)

### 7.2 Dependencias Externas

Ninguna. Todo el contenido es interno al proyecto ADT.

### 7.3 Dependencias de Datos

**Para crear templates**:
- Acceso a spec-driven-dev/templates/ (leer modelos existentes)
- Acceso a work-logger/templates/ (leer modelo existente)

**Para crear anthropic-best-practices**:
- Acceso a /mnt/user-data/uploads/llms-full.txt (lectura)
- Capacidad de extraer líneas específicas (27212-28500, 2382-2900, 47737-47950)

## 8. Impacto

### 8.1 Cambios Breaking

Ninguno. Este proyecto solo agrega funcionalidad nueva, no modifica comportamiento existente.

| Cambio | Afecta a | Accion requerida |
|--------|----------|------------------|
| N/A | N/A | Ninguna |

### 8.2 Plan de Migracion

No aplica. No hay cambios breaking.

### 8.3 Backward Compatibility

- [x] Mantiene compatibilidad con version anterior (100%)
- [x] NO requiere migracion manual
- [x] Skills existentes siguen funcionando sin cambios

## 9. Plan de Rollback

### 9.1 Pasos de Rollback

Si la implementación resulta problemática:

1. Eliminar directorios templates/ creados:
   ```bash
   rm -rf .codex/skills/commit-helper/templates
   rm -rf .codex/skills/skills-management/templates
   rm -rf .codex/skills/incremental-correction-methodology/templates
   ```

2. Eliminar skill anthropic-best-practices:
   ```bash
   rm -rf .codex/skills/anthropic-best-practices
   ```

3. Revertir modificaciones a SKILL.md:
   ```bash
   git checkout HEAD -- \
     .codex/skills/commit-helper/SKILL.md \
     .codex/skills/skills-management/SKILL.md \
     .codex/skills/incremental-correction-methodology/SKILL.md \
     .codex/skills/project-context/SKILL.md \
     .codex/skills/translation-workflow/SKILL.md
   ```

4. Verificar que proyecto funciona:
   ```bash
   cd /tmp/ADT
   # Verificar que skills cargan correctamente
   ls -la .codex/skills/*/SKILL.md
   ```

### 9.2 Criterios de Rollback

Ejecutar rollback si:
- Templates contienen errores graves que impiden su uso
- anthropic-best-practices causa confusión en lugar de clarificación
- Referencias cruzadas rompen funcionalidad de skills existentes
- Usuarios reportan que cambios empeoran workflow

### 9.3 Estado Post-Rollback

Después del rollback:
- Proyecto vuelve a estado anterior (15 skills)
- Solo spec-driven-dev y work-logger tienen templates
- No hay skill anthropic-best-practices
- SKILL.md de skills modificados vuelven a versión anterior

## 10. Testing

### 10.1 Casos de Prueba

**TC-001: Template commit-message es usable**
- Descripcion: Verificar que template de commit genera mensaje válido
- Precondiciones: commit-helper/templates/commit-message.template existe
- Input: Reemplazar placeholders con: type=feat, scope=auth, subject=add login
- Pasos:
  1. Abrir commit-message.template
  2. Reemplazar [type] con feat
  3. Reemplazar [scope] con auth
  4. Reemplazar [subject] con add login endpoint
  5. Copiar resultado
- Output esperado: "feat(auth): add login endpoint" (formato válido Conventional Commits)
- Referencias: RF-001

**TC-002: Template SKILL.md genera skill válido**
- Descripcion: Verificar que template de skill genera SKILL.md correcto
- Precondiciones: skills-management/templates/SKILL.md.template existe
- Input: Crear skill test-skill con descripción "Test skill"
- Pasos:
  1. Copiar SKILL.md.template
  2. Reemplazar placeholders en frontmatter
  3. Completar secciones obligatorias
  4. Guardar como test-skill/SKILL.md
  5. Verificar sintaxis YAML válida
- Output esperado: Archivo SKILL.md con frontmatter válido y estructura completa
- Referencias: RF-003

**TC-003: anthropic-best-practices es accesible**
- Descripcion: Verificar que skill anthropic-bp puede ser leído
- Precondiciones: anthropic-best-practices/SKILL.md existe
- Input: Leer SKILL.md
- Pasos:
  1. Ejecutar view .codex/skills/anthropic-best-practices/SKILL.md
  2. Verificar que tiene frontmatter válido
  3. Verificar que tiene decision framework
  4. Verificar que referencia archivos (skill-authoring.md, etc)
- Output esperado: SKILL.md completo y legible
- Referencias: RF-012

**TC-004: Decision framework funciona**
- Descripcion: Decision framework guía correctamente a archivo relevante
- Precondiciones: anthropic-bp completo
- Input: Usuario pregunta "¿cómo escribir mejor skill?"
- Pasos:
  1. Leer decision framework en SKILL.md
  2. Framework sugiere skill-authoring.md
  3. Leer skill-authoring.md
  4. Verificar contenido es relevante
- Output esperado: skill-authoring.md contiene principios de creación de skills
- Referencias: RF-012

**TC-005: Contenido transformado es diferente de original**
- Descripcion: Verificar que no se copió literalmente llms-full.txt
- Precondiciones: anthropic-bp creado
- Input: Comparar líneas de skill-authoring.md con llms-full.txt líneas 27212-28500
- Pasos:
  1. Tomar muestra de 10 líneas de skill-authoring.md
  2. Buscar texto exacto en llms-full.txt
  3. Verificar que NO hay coincidencia literal
  4. Verificar que principios están pero con palabras diferentes
- Output esperado: Contenido transformado, no copiado
- Referencias: RF-012, DA-004

**TC-006: Ejemplos son específicos de ADT**
- Descripcion: Ejemplos mencionan arc42, Sphinx, RST (no API)
- Precondiciones: anthropic-bp completo
- Input: Buscar ejemplos en archivos
- Pasos:
  1. grep "arc42\|Sphinx\|RST" anthropic-best-practices/*.md
  2. Verificar que hay ejemplos
  3. Verificar que NO hay ejemplos de API calls
- Output esperado: Ejemplos contextualizados a ADT
- Referencias: RF-012, DA-004

**TC-007: Referencias cruzadas funcionan**
- Descripcion: Referencias desde skills existentes a anthropic-bp son correctas
- Precondiciones: Todos los skills modificados
- Input: Leer skills-management/SKILL.md
- Pasos:
  1. Encontrar referencia a anthropic-best-practices
  2. Verificar path es correcto
  3. Verificar que archivo referenciado existe
  4. Repetir para project-context y translation-workflow
- Output esperado: Todas las referencias apuntan a archivos existentes
- Referencias: RF-013

### 10.2 Criterios de Validacion

- [x] Todos los RF de requirements.md cubiertos (RF-001 a RF-013)
- [x] Templates generan documentos válidos
- [x] anthropic-best-practices SKILL.md <200 líneas
- [x] Contenido transformado (no copiado)
- [x] Ejemplos específicos de ADT
- [x] Referencias cruzadas correctas
- [x] Sintaxis Markdown válida en todos los archivos
- [x] Frontmatter YAML válido donde corresponde
- [x] Documentación actualizada en cada SKILL.md modificado

### 10.3 Testing Manual vs Automatico

| Aspecto | Tipo | Como se valida |
|---------|------|----------------|
| Templates generan docs válidos | Manual | Usar template y verificar output |
| Sintaxis Markdown | Automatico | Linter Markdown |
| Sintaxis YAML | Automatico | yaml-lint en frontmatter |
| Contenido transformado | Manual | Comparar con llms-full.txt (sampling) |
| Ejemplos ADT | Manual | Revisar que mencionen arc42/Sphinx/RST |
| Referencias cruzadas | Automatico | Verificar paths existen |
| Usabilidad templates | Manual | User testing con casos reales |

## 11. Performance y Escalabilidad

### 11.1 Consideraciones de Performance

No aplica significativamente. Archivos estáticos no tienen overhead de performance.

- Tiempo para abrir template: <1 segundo (archivo texto)
- Tiempo para leer anthropic-bp archivo: <2 segundos (archivos medianos)
- Impacto en memoria: Mínimo (solo cuando archivo abierto)

### 11.2 Optimizaciones

- Progressive disclosure en anthropic-bp asegura que solo se carga contenido necesario
- SKILL.md pequeño (<200 líneas) carga rápido
- Archivos de referencia solo se leen cuando necesarios

## 12. Seguridad

### 12.1 Consideraciones de Seguridad

No hay consideraciones significativas de seguridad. Contenido es educativo/referencia.

Verificaciones:
- Templates NO contienen información sensible (passwords, keys)
- anthropic-bp NO revela información confidencial de Anthropic
- Contenido es apropiado para repositorio público (si ADT se hace público)

### 12.2 Secrets Management

No aplica. Ningún archivo contiene o requiere secrets.

## 13. Documentacion

### 13.1 Documentacion a Crear/Actualizar

- [x] commit-helper/SKILL.md - Agregar sección Templates
- [x] commit-helper/templates/commit-message.template - Crear con comentarios guía
- [x] skills-management/SKILL.md - Agregar sección Templates + ref a anthropic-bp
- [x] skills-management/templates/SKILL.md.template - Crear template completo
- [x] skills-management/templates/README.md - Guía de uso
- [x] incremental-correction-methodology/SKILL.md - Agregar sección Templates
- [x] incremental-correction-methodology/templates/* - Crear 4 templates
- [x] incremental-correction-methodology/templates/README.md - Workflow de templates
- [x] anthropic-best-practices/SKILL.md - Crear skill completo
- [x] anthropic-best-practices/skill-authoring.md - Transformar de llms-full.txt
- [x] anthropic-best-practices/prompting-tips.md - Transformar de llms-full.txt
- [x] anthropic-best-practices/long-context-tips.md - Transformar de llms-full.txt
- [x] anthropic-best-practices/README.md - Guía de uso
- [x] project-context/SKILL.md - Agregar referencia a prompting-tips
- [x] translation-workflow/SKILL.md - Agregar referencia a long-context-tips
- [x] Work-log de implementación en .mywork/work-logs/

### 13.2 Comentarios en Templates

Todos los templates DEBEN incluir:
- Comentarios en formato Markdown que explican cada sección
- Placeholders descriptivos con formato [descripcion-clara]
- Ejemplos inline donde útil
- Referencias a SKILL.md del skill para más contexto

Ejemplo de comentario en template:
```markdown
<!-- Este es un placeholder - reemplazar con tu contenido -->
[Descripción clara de qué poner aquí]

<!-- Ejemplo: -->
<!-- feat(auth): implement JWT-based authentication -->
```

## 14. Referencias

### 14.1 Documentos Relacionados

- 20260201-192709-requirements-crear-templates.md (v0.2) - Requirements de este proyecto
- ANALISIS_TEMPLATES_SKILLS.md - Análisis de templates existentes
- ANALISIS_LLMS_FULL_TRANSFORMACION.md - Análisis de llms-full.txt
- FASE-0-preparacion.md - Preparación del proyecto
- spec-driven-dev/templates/*.md.template - Modelos de referencia
- work-logger/templates/work-log.md.template - Modelo de referencia

### 14.2 Recursos Externos

- llms-full.txt (líneas 27212-28500) - Skill Authoring Best Practices de Anthropic
- llms-full.txt (líneas 2382-2900) - Prompting Best Practices de Anthropic
- llms-full.txt (líneas 47737-47950) - Long Context Tips de Anthropic
- Conventional Commits specification - Para commit-message.template

### 14.3 Decisiones que Afectan Otras Areas

- DA-003 (progressive disclosure) afecta a: Cómo futuros skills se estructuran
- DA-004 (transformación) establece: Patrón para futuros skills de referencia
- DA-006 (referencias cruzadas) establece: Patrón de integración entre skills

## 15. Aprobacion

- [ ] Revisado por: Usuario
- [ ] Aprobado por: Usuario
- [ ] Fecha de aprobacion: 2026-02-01

SOLICITAR APROBACION ANTES DE CONTINUAR A FASE 3 (Tasks)

## Historial de Cambios

| Fecha | Version | Cambios | Autor |
|-------|---------|---------|-------|
| 2026-02-01 | 0.1 | Creacion inicial | Claude (AI Assistant) |
| 2026-02-01 | 0.2 | Agregada DA-009 sobre naming conventions especificos | Claude (AI Assistant) |

---

Estado: Draft - Pendiente de aprobacion
Proxima fase: FASE 3 - Tasks (tras aprobacion)

NOTA: Archivo FASE 3 seguirá convención DA-009: 20260201-tasks-crear-templates.md (NO solo tasks.md)
