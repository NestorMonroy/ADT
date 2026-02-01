---
name: work-logger
description: "Sistema de logging estructurado de trabajo. Usar cuando se complete tarea importante, traduccion, o implementacion que deba quedar documentada."
version: 1.1.0
created: 2026-01-29
updated: 2026-02-01
---

# Work Logger - Documentacion de Trabajo

## Cuando usar

- Usuario pide "documentar esto"
- Al completar traduccion significativa
- Despues de resolver problema complejo
- Al finalizar feature importante
- Para registrar decisiones tecnicas
- Cuando algo debe quedar para referencia futura

---

## Decision Framework: ¿Merece un Work Log?

**Usa este framework para decidir si documentar**:

1. **¿El trabajo tomó >30 minutos?**
   → Sí, probablemente merece log

2. **¿Es algo que necesitaré recordar en 1 mes?**
   → Sí, documentar

3. **¿Otros colaboradores se beneficiarían de conocerlo?**
   → Sí, documentar

4. **¿Resolví un problema complejo o no obvio?**
   → Sí, definitivamente documentar

5. **¿Tomé decisiones técnicas importantes?**
   → Sí, documentar las razones

6. **¿Es solo un typo o cambio trivial?**
   → No, skip work log

7. **¿Puedo explicarlo en una línea de commit?**
   → Si sí → skip work log
   → Si no → crear work log

8. **¿No estoy seguro?**
   → Documentar (mejor exceso que falta)

**Regla de oro**: Si dudas → **documenta**

---

## Trigger Patterns

### Señales Explícitas
- Usuario dice: "documenta esto"
- Usuario dice: "crea un work log"
- Usuario dice: "registra este trabajo"
- Usuario pregunta: "¿cómo documentamos?"
- Fin de sesión larga de trabajo (>2h)

### Señales Implícitas
- Trabajo complejo recién completado
- Problema resuelto después de debugging
- Feature implementada con decisiones técnicas
- Script creado o modificado significativamente
- Aprendizajes importantes descubiertos
- Usuario dice "para que no se olvide"

### Trigger Words
- "documentar", "registrar", "log"
- "para referencia", "para el futuro"
- "importante", "crítico", "decisión"
- "problema resuelto", "bug fixed"
- "aprendizaje", "lección"

**Anti-triggers** (NO crear work log):
- Usuario dice "cambio rápido"
- Usuario dice "solo un typo"
- Cambio de <10 líneas sin complejidad
- Update rutinario de dependencias
- Cambios cosméticos de formato

---

## Self-Check Before Creating Work Log

**OBLIGATORIO antes de crear work log**:

### Pre-Logging Checks
- [ ] ¿El trabajo está completado?
- [ ] ¿Tengo toda la información necesaria?
- [ ] ¿Sé qué archivos afecté?
- [ ] ¿Tengo commits relacionados identificados?
- [ ] ¿Hay decisiones que debo documentar?

**Si NO → Completar trabajo antes de documentar**

### During-Logging Checks
- [ ] ¿Usé el template correcto?
- [ ] ¿Resumen ejecutivo es claro?
- [ ] ¿Listé TODOS los archivos afectados?
- [ ] ¿Documenté decisiones NO obvias?
- [ ] ¿Incluí comandos/código relevante?
- [ ] ¿Sin información sensible (passwords, keys)?

**Si NO en alguno → Revisar y completar**

### Post-Logging Checks
- [ ] ¿El log está en `.mywork/work-logs/`?
- [ ] ¿Nombre sigue formato YYYY-MM-DD-HH-MM-titulo.md?
- [ ] ¿El archivo es legible y formateado?
- [ ] ¿Hice commit del work log?
- [ ] ¿Tags apropiados agregados?

**Si NO → Corregir antes de cerrar**

---

## Ubicacion

`.mywork/work-logs/YYYY-MM-DD-HH-MM-titulo.md`

## Proceso

### 1. Determinar si Merece Log

SI documentar:
- Traducciones completas
- Scripts nuevos o modificados
- Resolucion de problemas complejos
- Cambios arquitectonicos
- Decisiones importantes
- Workflows nuevos

NO documentar:
- Typos corregidos
- Cambios triviales de formato
- Updates menores

### 2. Generar Nombre

```bash
DATE=$(date "+%F-%H-%M") # YYYY-MM-DD-HH-MM
TITULO="breve-descripcion-kebab-case" # max 50 chars
ARCHIVO=".mywork/work-logs/${DATE}-${TITULO}.md"
```

Ejemplos:
- 2026-01-28-09-15-traducir-arc42-quality-requirements.md
- 2026-01-28-14-30-resolver-problema-build-sphinx.md

### 3. Usar Template

Ver: `.codex/skills/work-logger/templates/work-log.md.template`

Secciones principales:
- Resumen ejecutivo (OBLIGATORIO)
- Trabajo realizado (OBLIGATORIO)
- Archivos afectados (OBLIGATORIO)
- Decisiones tomadas (opcional)
- Problemas encontrados (opcional)
- Aprendizajes (opcional)

### 4. Reglas de Contenido

SEGURIDAD:
- NUNCA passwords, API keys, tokens
- Usar placeholders: `<valor de API_KEY>`

FORMATO:
- Markdown con sintaxis correcta
- Bloques de codigo con lenguaje especificado
- Titulos jerarquicos

LENGUAJE:
- Idioma principal: Español
- Terminos tecnicos: Sin traducir
- Comandos y rutas: Literales

### 5. Escribir Archivo

```bash
mkdir -p .mywork/work-logs

cat > .mywork/work-logs/YYYY-MM-DD-HH-MM-titulo.md <<'EOF'
[contenido del log]
EOF
```

### 6. Commit

```bash
git add .mywork/work-logs/YYYY-MM-DD-HH-MM-titulo.md
git commit -m "docs(work-log): documentar [trabajo realizado]"
```

## Template Basico

```markdown
# YYYY-MM-DD-HH-MM - Titulo del Trabajo

Fecha: YYYY-MM-DD HH:MM
Autor: [Nombre]
Proyecto: ADT Documentation

## Resumen Ejecutivo

[1-2 parrafos describiendo que se hizo y por que]

## Trabajo Realizado

### Paso 1: [Nombre]
[Descripcion]

```bash
comandos
```

[Resultado]

## Archivos Afectados

Creados:
- path/file.rst - [Descripcion]

Modificados:
- path/existing.rst - [Cambio]

## Aprendizajes

1. [Leccion 1]
2. [Leccion 2]

---

Tags: #tag1 #tag2
Estado: Completado
```

## Ejemplos

### Ejemplo: Traduccion

```markdown
# 2026-01-28 - Traduccion de arc42 Quality Requirements

Fecha: 2026-01-28 14:30
Autor: AI Assistant
Proyecto: ADT Documentation

## Resumen Ejecutivo

Traduccion completa de la seccion 10 del template arc42 (Quality
Requirements) del ingles al español, aplicando modo de Alta Fidelidad.

## Trabajo Realizado

### Paso 1: Analisis
Analice estructura del documento original.

```bash
python scripts/analizar_seccion.py \
 source/biblioteca/arc42/sections/10_quality_requirements/
```

### Paso 2: Traduccion
```bash
python scripts/traduccion/arc42_scraper_python.py \
 --section 10 \
 --mode alta_fidelidad
```

## Archivos Afectados

Creados:
- source/biblioteca/arc42/sections/10_quality_requirements/index.rst

Modificados:
- source/biblioteca/arc42/index.rst

## Resultados

- [x] Build exitoso
- [x] Linkcheck OK
- [x] Metadata completa

---

Tags: #traduccion #arc42
Estado: Completado
```

### Ejemplo: Resolucion de Problema

```markdown
# 2026-01-28 - Resolver ERROR Referencia Circular

## Resumen Ejecutivo

Resolucion de error critico en build causado por referencia
circular entre fundamentos/index.rst y metodologias/index.rst.

## Problemas Encontrados

### Problema: Referencia Circular
Sintomas: ERROR: circular toctree references

Causa: fundamentos/index.rst -> _metodologias/index.rst ->
fundamentos/index.rst

Solucion: Elimine toctree de _metodologias/index.rst

Prevencion: No usar toctree hacia arriba en jerarquia

## Archivos Afectados

Modificados:
- source/01_fundamentos/_metodologias/index.rst

## Aprendizajes

1. toctree debe formar DAG
2. Usar :doc: para refs hacia arriba

---

Tags: #bugfix #sphinx
Estado: Completado
```

## Busqueda en Logs

```bash
# Por tag
grep -r "#traduccion" .mywork/work-logs/

# Por termino
grep -r "arc42" .mywork/work-logs/

# Listar recientes
ls -lt .mywork/work-logs/ | head -10
```

## Mantenimiento

Archivar logs antiguos:

```bash
# Crear directorio archivo
mkdir -p .mywork/work-logs/archive/2025/

# Mover logs viejos (> 6 meses)
mv .mywork/work-logs/2025-*.md .mywork/work-logs/archive/2025/
```

## Notas

- Work logs son para HUMANOS, no parseo
- Priorizar claridad sobre brevedad
- Incluir suficiente contexto
- Documentar decisiones NO obvias
- Escribir pensando en "yo del futuro"

---

## Changelog

### v1.1.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y decision-making**:

✅ **Decision Framework** - ¿Merece un Work Log?
- 8 preguntas para decidir si documentar
- Regla de oro: "Si dudas → documenta"
- Clarifica cuándo NO crear work log (typos, cambios triviales)

✅ **Trigger Patterns** - Cuándo crear work log
- Señales explícitas (usuario dice "documenta")
- Señales implícitas (trabajo complejo completado)
- Trigger words específicos
- Anti-triggers para evitar over-documentation

✅ **Self-Check Mechanisms** - 3 niveles de checks
- Pre-Logging (trabajo completado, información lista)
- During-Logging (template, decisiones, sin info sensible)
- Post-Logging (ubicación, nombre, commit)

✅ **Corrección de referencia a template**
- De: `templates/work-log.md.template`
- A: `.codex/skills/work-logger/templates/work-log.md.template`

**Líneas agregadas**: ~95 líneas

**Beneficio principal**:
- Usuarios deciden correctamente cuándo documentar
- Checklist previene olvidos de información crítica
- Referencia correcta al template

### v1.0.0 - 2026-01-30
- Versión inicial con versionamiento añadido
- Estructura base de work logging
- Templates y ejemplos incluidos
- Integración con estructura .mywork/

