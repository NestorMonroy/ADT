---
name: validation-suite
description: "Suite completa de validación para Sphinx y contenido RST. Usar para verificar builds, validar estructura, detectar errores, y asegurar calidad antes de commits."
version: 1.1.0
created: 2026-01-29
updated: 2026-02-01
---

# Validation Suite - Quality Assurance

**Versión**: 1.1.0  
**Ubicación**: `/tmp/ADT/.codex/skills/validation-suite/`  
**Aplicable a**: Validación de builds Sphinx, estructura RST, calidad de documentación

---

## Cuándo Usar Esta Skill

### ✅ SIEMPRE usar cuando:
- Antes de hacer commit (OBLIGATORIO)
- Después de traducir contenido
- Al modificar estructura de directorios
- Cuando build falla
- Antes de merge a main
- Auditorías periódicas de calidad

### ❌ NO necesitas usar cuando:
- Solo lees documentación (sin cambios)
- Haces cambios triviales (<5 líneas)
- Estás en rama experimental temporal
- Solo actualizas comentarios en código

---

## Decision Framework: ¿Qué Nivel de Validación Usar?

**Usa este framework para decidir qué validaciones ejecutar**:

1. **¿Hiciste cambios en archivos .rst?**
   → SÍ: Ejecutar NIVEL 1 (Build Básico) como MÍNIMO

2. **¿Modificaste estructura de directorios o toctree?**
   → SÍ: Ejecutar NIVEL 1 + NIVEL 2 (Estructural)

3. **¿Agregaste o modificaste enlaces/referencias?**
   → SÍ: Ejecutar NIVEL 1 + NIVEL 3 (Enlaces)

4. **¿Tradujiste contenido nuevo?**
   → SÍ: Ejecutar NIVEL 1 + NIVEL 4 (Calidad Traducción)

5. **¿Modificaste metadata en archivos?**
   → SÍ: Ejecutar NIVEL 1 + NIVEL 5 (Metadata)

6. **¿Vas a hacer commit a main?**
   → SÍ: Ejecutar TODOS los niveles (1-5)

7. **¿Solo quieres verificar estado general?**
   → Ejecutar NIVEL 1 + NIVEL 6 (Coverage)

**Regla de oro**: Si dudas → Ejecutar NIVEL 1 como mínimo

---

## Trigger Patterns

### Señales Explícitas
- Usuario dice: "valida el build"
- Usuario dice: "verifica que todo esté correcto"
- Usuario dice: "antes de commit"
- Usuario pregunta: "¿está listo para commit?"
- Usuario dice: "revisa la calidad"

### Señales Implícitas
- Usuario acaba de hacer cambios en .rst
- Usuario acaba de traducir contenido
- Usuario pregunta "¿funcionará?"
- Usuario menciona "build", "errores", "warnings"
- Usuario está a punto de hacer commit

### Trigger Words
- "valida", "verifica", "revisa", "chequea"
- "build", "compile", "make"
- "errores", "warnings", "problemas"
- "commit", "merge", "push"

---

## Self-Check Before Running Validation

- [ ] ¿Estoy en `/tmp/ADT/`?
- [ ] ¿Tengo cambios sin guardar?
- [ ] ¿Hice `git add` de los archivos?
- [ ] ¿Sé qué nivel de validación necesito?
- [ ] ¿Tengo tiempo suficiente?

**Si NO**: Corregir antes de validar

---

## Niveles de Validación

### NIVEL 1: Build Básico (OBLIGATORIO)

```bash
cd /tmp/ADT
make clean
make html
```

**Resultado esperado**: "build succeeded"  
**Tiempo**: ~1-2 minutos

**Si falla**: Consultar `sphinx-expert` skill

---

### NIVEL 2: Validación Estructural

```bash
bash scripts/validar_estructura.sh
```

**Verifica**:
- Nomenclatura archivos
- Existencia index.rst
- Archivos huérfanos
- Directorios vacíos

**Tiempo**: ~30 segundos

---

### NIVEL 3: Validación de Enlaces

```bash
make linkcheck
```

**Verifica**:
- Cross-references internos
- Enlaces externos
- Downloads, imágenes

**Tiempo**: ~2-3 minutos

Ver: `build/linkcheck/output.txt`

---

### NIVEL 4: Calidad de Traducción

**Checklist manual**:

Coherencia:
- [ ] Términos consistentes
- [ ] Nombres propios conservados
- [ ] Código sin traducir

Completitud:
- [ ] Todas secciones presentes
- [ ] Metadata completa
- [ ] Referencias actualizadas

Modo ADT:
- [ ] Admoniciones apropiadas
- [ ] Nivel de detalle correcto

**Tiempo**: 5-10 minutos

---

### NIVEL 5: Validación de Metadata

```bash
python scripts/generate_section_metadata.py --validate source/
```

**Campos requeridos**:
- description, keywords, author, date
- Documento Original (si traducción)
- Modo de Traducción (si traducción)

**Tiempo**: ~1 minuto

---

### NIVEL 6: Coverage

```bash
make coverage
```

**Verifica**:
- Secciones sin contenido
- TODOs pendientes

Ver: `build/coverage/python.txt`

**Tiempo**: ~1-2 minutos

---

## Proceso Pre-Commit (OBLIGATORIO)

```bash
# PASO 1: Ubicación
cd /tmp/ADT

# PASO 2: Build limpio
make clean
make html

# PASO 3: Verificar resultado
# Debe decir "build succeeded"

# PASO 4: Validación estructural (si aplica)
bash scripts/validar_estructura.sh

# PASO 5: Si TODO OK
git add <archivos>
git commit -m "mensaje"
```

**Tiempo total**: ~2-3 minutos

---

## Métricas de Calidad

| Métrica | Threshold | Criticidad |
|---------|-----------|------------|
| Build success | 100% | 🔴 CRÍTICA |
| Exit code | 0 | 🔴 CRÍTICA |
| Broken links | 0 | 🟡 Alta |
| Metadata coverage | >95% | 🟡 Alta |
| Orphan files | 0 | 🟢 Media |

🔴 CRÍTICA: NO commit si falla  
🟡 Alta: Resolver antes de commit  
🟢 Media: Puede esperar

---

## Troubleshooting

### Build falla con "Unknown directive"
1. Verificar sintaxis: `.. directiva::`
2. Verificar indentación
3. Verificar extensión Sphinx habilitada
4. Consultar `sphinx-expert`

### Enlaces rotos internos
1. Buscar definición: `grep -r ".. _label:" source/`
2. Verificar typos
3. Verificar archivo en toctree

### Enlaces externos rotos
1. Verificar URL en navegador
2. Puede ser timeout → retry
3. Verificar CI también

---

## When NOT to Use

❌ Solo lees documentación  
❌ Cambios triviales en comentarios  
❌ Rama experimental temporal  
❌ Ya validaste hace <5 min  

✅ Cambios en .rst  
✅ Antes de commit a main

---

## Ejemplos

### Example 1: Cambio Simple
```bash
make clean html  # ✅ build succeeded
git commit -m "docs: fix typo"
```
Tiempo: ~2 min

### Example 2: Traducción Completa
```bash
make clean html       # NIVEL 1
bash scripts/validar  # NIVEL 2
make linkcheck       # NIVEL 3
# Manual checklist   # NIVEL 4
python scripts/meta  # NIVEL 5
git commit
```
Tiempo: ~10-15 min

### Example 3: Pre-Merge a Main
```bash
# TODOS los niveles (1-6)
make clean html
bash scripts/validar
make linkcheck
# checklist manual
python scripts/meta
make coverage
git merge
```
Tiempo: ~15 min

---

## Antipatrones

### ❌ Commit sin validar
**Problema**: Build roto en CI

### ❌ Ignorar WARNING
**Problema**: 200+ WARNING acumulados

### ❌ No leer output completo
**Problema**: Enlaces rotos en prod

### ❌ Validar solo en feature branch
**Problema**: Falla en merge

### ❌ "Lo validaré después"
**Problema**: "Después" nunca llega

---

## Referencias

- `scripts/validar_estructura.sh`
- `scripts/generate_section_metadata.py`
- `Makefile`
- `sphinx-expert` skill
- `source/07_guias_uso/troubleshooting.rst`

---

## Notas

- Validación NO sustituye revisión manual
- WARNING pueden indicar problemas reales
- Linkcheck puede tener falsos positivos
- Build local puede diferir de CI

---

## Versionamiento

### v1.1.0 (2026-02-01) - FASE 2
- ✅ Decision Framework
- ✅ Trigger Patterns
- ✅ Self-Check Mechanisms
- ✅ "When NOT to Use"
- ✅ Examples (3 ejemplos)
- ✅ Antipatrones (5 antipatrones)
- ✅ Troubleshooting expandido

### v1.0.0 (2026-01-30)
- ✅ Versión inicial
- ✅ 6 niveles de validación

---

**Última actualización**: 2026-02-01  
**Mantenedor**: ADT Team
