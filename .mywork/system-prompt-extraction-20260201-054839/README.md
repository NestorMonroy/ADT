# System Prompt de Claude Sonnet 4.5 - Extracción Completa

**Fecha de extracción**: 2026-02-01 05:48:39  
**Carpeta**: `.mywork/system-prompt-extraction-20260201-054839/`

---

## 📋 Contenido

Este directorio contiene la **extracción completa** del system prompt que Claude Sonnet 4.5 tiene inyectado en su contexto de conversación.

### Archivo Principal

- **CLAUDE_SYSTEM_PROMPT_COMPLETE.txt** (1,146 líneas, 82KB)
  - System prompt completo tal como Claude lo ve
  - Todas las secciones incluidas
  - Sin modificaciones

---

## 🎯 Estructura del System Prompt

El system prompt contiene las siguientes secciones principales:

### 1. Información Básica
- Identidad de Claude
- Fecha actual
- Interfaz (claude.ai)

### 2. `<past_chats_tools>`
- Herramientas para buscar conversaciones pasadas
- conversation_search
- recent_chats

### 3. `<computer_use>` ⭐ (Sección más grande)
- `<skills>` - Instrucciones sobre skills
- `<file_creation_advice>`
- `<file_handling_rules>` - /mnt/user-data/uploads, /home/claude, /mnt/user-data/outputs
- `<producing_outputs>`
- `<sharing_files>`
- `<artifacts>` - HTML, React, Markdown, etc.
- `<package_management>`
- `<network_configuration>`
- `<filesystem_configuration>`

### 4. `<available_skills>` ⭐⭐
Lista de 7 skills disponibles:
- docx
- pdf
- pptx
- xlsx
- product-self-knowledge
- frontend-design
- skill-creator

**Ubicación**: Todos en `/mnt/skills/public/` o `/mnt/skills/examples/`

### 5. `<anthropic_api_in_artifacts>`
- Cómo usar la API de Anthropic en artifacts
- Web search tool
- Manejo de archivos

### 6. `<persistent_storage_for_artifacts>`
- window.storage API
- Almacenamiento persistente

### 7. `<citation_instructions>`
- Cómo citar resultados de web_search

### 8. `<search_instructions>` ⭐⭐
- Cuándo buscar vs no buscar
- Cómo hacer queries
- COPYRIGHT COMPLIANCE (reglas estrictas)

### 9. `<CRITICAL_COPYRIGHT_COMPLIANCE>` ⚠️⚠️⚠️
**Sección crítica con reglas absolutas**:
- 15+ palabras de una fuente = SEVERE VIOLATION
- UNA cita por fuente MÁXIMO
- NUNCA reproducir lyrics, poems, haikus
- Default a parafrasear

### 10. `<memory_system>`
- Sistema de memoria (deshabilitado para este usuario)

### 11. `<claude_behavior>` ⭐
- `<product_information>` - Info sobre Anthropic
- `<refusal_handling>` - Qué no puede hacer
- `<legal_and_financial_advice>` - Caveats
- `<tone_and_formatting>` - Cuándo usar listas/bullets
- `<user_wellbeing>` - Mental health
- `<knowledge_cutoff>` - Enero 2025
- `<anthropic_reminders>` - Warnings del sistema
- `<evenhandedness>` - Balance político
- `<additional_info>` - Thumbs down, respeto

---

## ❌ LO QUE FALTA

**Búsqueda en el system prompt completo**:

| Concepto | Aparece? | Contexto |
|----------|----------|----------|
| "project skills" | ❌ NO | - |
| "local skills" | ❌ NO | - |
| ".codex" | ❌ NO | - |
| "user-defined" | ❌ NO | - |
| "project-specific" | ❌ NO | - |
| "discover methodology" | ❌ NO | - |

**Conclusión**: El system prompt **NO contiene** instrucciones para:
- Buscar skills en el proyecto del usuario
- Priorizar metodologías locales
- Descubrir contexto específico del proyecto
- Leer `.codex/skills/` o similar

---

## 🔍 Hallazgos Clave

### Sobre Skills

**Lo que SÍ dice**:
```
"We've found that Claude's efforts are greatly aided by reading 
the documentation available in the skill BEFORE writing any code"
```

**Pero solo lista**: 7 skills en `/mnt/skills/`

**NO menciona**:
- Skills del proyecto
- Búsqueda de skills locales
- Jerarquía proyecto > sistema

### Sobre File Locations

**Directorios definidos**:
1. `/mnt/user-data/uploads` - Archivos del usuario
2. `/home/claude` - Workspace temporal de Claude
3. `/mnt/user-data/outputs` - Archivos finales para compartir

**Directorios read-only**:
- `/mnt/user-data/uploads`
- `/mnt/transcripts`
- `/mnt/skills/public`
- `/mnt/skills/private`
- `/mnt/skills/examples`

### Sobre Copyright

**Reglas más estrictas del system prompt**:
```
LIMIT 1: 15+ words from any single source = SEVERE VIOLATION
LIMIT 2: ONE quote per source MAXIMUM
LIMIT 3: NEVER reproduce song lyrics, poems, haikus
```

---

## 📊 Estadísticas

| Aspecto | Valor |
|---------|-------|
| **Tamaño total** | 82 KB |
| **Líneas** | 1,146 |
| **Formato** | XML/texto mixto |
| **Skills listados** | 7 (todos en /mnt/skills) |
| **Sección más grande** | `<computer_use>` |
| **Regla más estricta** | COPYRIGHT (15 words max) |

---

## 🎯 Implicaciones para el Proyecto ADT

**Problema identificado**:
- El project tiene 11 skills en `.codex/skills/`
- El system prompt NO instruye a Claude a buscarlos
- Claude depende de su "criterio" para descubrirlos

**Recomendación**:
- Claude DEBE ser proactivo en buscar skills locales
- Aunque el system prompt no lo requiera
- Responsabilidad de Claude descubrir contexto del proyecto

---

## 📝 Notas

1. Este contenido está **inyectado por Anthropic** al inicio de cada conversación
2. **NO existe** como archivo en el filesystem de Claude
3. Claude puede **verlo** en su contexto pero **no modificarlo**
4. Esta es una **extracción manual** para análisis

---

**Creado**: 2026-02-01 05:48:39  
**Propósito**: Documentar system prompt para análisis de comportamiento de Claude
