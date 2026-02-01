# Análisis del System Prompt - Sección de Skills

## 📍 Ubicación del System Prompt

**Sistema**: Inyectado por Anthropic al inicio de cada conversación
**Accesible vía filesystem**: ❌ No
**Visible para Claude**: ✅ Sí (en contexto)
**Visible para usuario**: ❌ No (es interno)

---

## 📋 Sección <available_skills> Completa

La sección de mi system prompt lista SOLO estos skills:

```xml
<available_skills>
  <skill>
    <name>docx</name>
    <location>/mnt/skills/public/docx/SKILL.md</location>
  </skill>
  
  <skill>
    <name>pdf</name>
    <location>/mnt/skills/public/pdf/SKILL.md</location>
  </skill>
  
  <skill>
    <name>pptx</name>
    <location>/mnt/skills/public/pptx/SKILL.md</location>
  </skill>
  
  <skill>
    <name>xlsx</name>
    <location>/mnt/skills/public/xlsx/SKILL.md</location>
  </skill>
  
  <skill>
    <name>product-self-knowledge</name>
    <location>/mnt/skills/public/product-self-knowledge/SKILL.md</location>
  </skill>
  
  <skill>
    <name>frontend-design</name>
    <location>/mnt/skills/public/frontend-design/SKILL.md</location>
  </skill>
  
  <skill>
    <name>skill-creator</name>
    <location>/mnt/skills/examples/skill-creator/SKILL.md</location>
  </skill>
</available_skills>
```

**Total**: 7 skills (todos en `/mnt/skills/`)

---

## ❌ LO QUE FALTA

### Instrucciones que NO existen:

1. **Descubrimiento de skills del proyecto**:
   ```
   ❌ "Si trabajas en un proyecto, busca primero skills locales"
   ❌ "Revisa si existe .codex/skills/ o similar"
   ❌ "Prioriza skills del proyecto sobre skills del sistema"
   ```

2. **Contexto del proyecto**:
   ```
   ❌ "Lee README.md del proyecto antes de empezar"
   ❌ "Busca metodologías específicas del proyecto"
   ❌ "Pregunta si hay convenciones locales"
   ```

3. **Jerarquía de skills**:
   ```
   ❌ "Skills del proyecto > Skills del sistema"
   ❌ "Si hay conflicto, sigue las reglas del proyecto"
   ```

---

## 🎯 IMPLICACIÓN

**El system prompt actual**:
- ✅ Me dice QUÉ skills existen en /mnt/skills
- ✅ Me dice que los lea antes de trabajar
- ❌ NO me dice que busque skills del proyecto
- ❌ NO me dice cómo descubrir metodologías locales

**Resultado**:
- Dependo de mi "inteligencia" para descubrir `.codex/skills/`
- No hay un flujo mandatorio de "buscar contexto local primero"
- Fácilmente ignoro metodologías del proyecto si no las busco activamente

---

## 📊 COMPARACIÓN

| Aspecto | System Prompt Dice | Debería Decir |
|---------|-------------------|---------------|
| Skills del sistema | ✅ Lista 7 skills en /mnt | ✅ (correcto) |
| Skills del proyecto | ❌ No menciona | ✅ "Busca primero en el proyecto" |
| Prioridad | ❌ No especifica | ✅ "Proyecto > Sistema" |
| Descubrimiento | ❌ No instruye | ✅ "Busca .codex/, .claude/, etc" |
| Validación | ❌ No requiere | ✅ "Pregunta si hay metodologías" |

---

## ✅ PROPUESTA DE MEJORA

### Sección adicional que DEBERÍA existir:

```xml
<project_skills_discovery>
  <rule priority="critical">
    BEFORE using any /mnt/skills, check if the project has local skills:
    
    1. Search for common skill directories:
       - .codex/skills/
       - .claude/skills/
       - docs/skills/
       - .ai/skills/
    
    2. If found:
       a. Read the skills README first
       b. Load project-specific skills
       c. Follow project methodologies
       d. Project skills OVERRIDE system skills
    
    3. If not found:
       - Ask user if there are project-specific methodologies
       - Then use /mnt/skills as fallback
  </rule>
</project_skills_discovery>
```

---

## 🔍 VERIFICACIÓN

Puedo verificar que esto es correcto buscando en /mnt/skills:

\`\`\`bash
ls -la /mnt/skills/
# Resultado: public/, private/, examples/
# NO hay: "user/", "project/", "local/"
\`\`\`

El sistema solo conoce skills "globales" en /mnt/skills.
NO tiene concepto de skills "por proyecto".

---

## 🎯 CONCLUSIÓN

**Por qué no vi `/tmp/ADT/.codex/skills/`**:
1. ❌ Mi system prompt no me dice que busque
2. ❌ No hay instrucción de priorizar proyecto
3. ❌ No hay flujo de "descubrimiento local primero"
4. ✅ Solo tenía listados skills en /mnt/skills/

**Pero esto NO me exime de responsabilidad**:
- ✅ Pude haber sido proactivo
- ✅ Pude haber explorado el proyecto
- ✅ Pude haber preguntado
- ✅ Es mi responsabilidad descubrir contexto

**La falta de instrucción explícita NO justifica ignorar el contexto del proyecto.**

---

**Fecha**: 2026-02-01
**Propósito**: Documentar limitación actual del system prompt para skills de proyecto
