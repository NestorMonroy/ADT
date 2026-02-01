# FASE 3: Tasks - Reorganización Completa ADT

**Fecha**: 2026-02-01  
**Basado en**: 
- Requirements: 2026-02-01-08-41-requirements-reestructura-source.md
- Design: ESTRUCTURA_FINAL_arc42_COMPLETA.md

**Estado**: Ready to Execute  
**Estimación total**: 2 horas

---

## 📋 TAREAS ORGANIZADAS

### GRUPO A: Reorganización arc42_documentation (1 hora)

#### A1: Crear estructura pipeline_docs_work ⏱️ 5 min
- [ ] Crear `pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/`
- [ ] Subdirectorios: `originales/{full_site,por_seccion}`, `metadata/`, `reportes/`, `trabajo/`
- **Criterio**: Directorios creados y verificados con `ls`

#### A2: Mover contenido PRIVADO de arc42 ⏱️ 15 min
- [ ] Mover `original/` completo → `pipeline_docs_work/.../originales/full_site/`
- [ ] Mover `_metadata_biblioteca/` → `pipeline_docs_work/.../metadata/`
- [ ] Mover todos `REPORTE_*.rst` → `pipeline_docs_work/.../reportes/`
- [ ] Mover `sections/*/original/` → `pipeline_docs_work/.../originales/por_seccion/`
- **Criterio**: `pipeline_docs_work/` contiene todo lo privado

#### A3: Reorganizar PÚBLICO - arc42 (30 min)
Para CADA una de las 12 secciones:
- [ ] Crear estructura: `XX_nombre/` con `secciones/`, `tips/`, `ejemplos/`
- [ ] Mover `diagramas/` y `figuras/` (ya existen)
- [ ] Organizar contenido de `traduccion/`:
  - `seccion_*.rst` → `secciones/`
  - `*_tip-*.rst` → `tips/`
  - `*_ejemplo-*.rst` → `ejemplos/`
- [ ] Eliminar `sections/` y `traduccion/` vacios
- **Criterio**: Estructura limpia sin `sections/`, solo 12 directorios XX_nombre

#### A4: Crear índices .rst (10 min)
- [ ] Crear `arc42_documentation/index.rst` (general)
- [ ] Crear `XX_nombre/index.rst` para cada sección (12 archivos)
- [ ] Sin emojis en archivos .rst (CRÍTICO)
- **Criterio**: 13 archivos index.rst creados, build Sphinx funciona

---

### GRUPO B: Finalizar reorganización general (30 min)

#### B1: Actualizar source/index.rst ⏱️ 5 min
- [ ] Actualizar para apuntar SOLO a `biblioteca/`
- [ ] Sin referencias a 01-10, docs_maestros
- **Criterio**: index.rst apunta solo a biblioteca

#### B2: Crear README en pipeline_docs_work ⏱️ 5 min
- [ ] `pipeline_docs_work/README.md` general
- [ ] `pipeline_docs_work/.../arc42_documentation/README.md` específico
- **Criterio**: READMEs explican workflow y estructura

#### B3: Verificar estructura final ⏱️ 10 min
- [ ] `source/biblioteca/` solo contiene biblioteca (público)
- [ ] `pipeline_docs_work/` contiene todo privado
- [ ] `archivados/` contiene obsoletos
- **Criterio**: `tree` muestra estructura esperada

#### B4: Limpiar archivos temporales ⏱️ 10 min
- [ ] Eliminar `.backup` files
- [ ] Eliminar directorios `temp_*`
- [ ] Verificar no hay archivos sueltos
- **Criterio**: Git status limpio (solo cambios intencionales)

---

### GRUPO C: Validación y Documentación (30 min)

#### C1: Build Sphinx ⏱️ 10 min
- [ ] `make clean`
- [ ] `make html`
- [ ] Verificar SOLO biblioteca/ se publicó
- [ ] 0 ERRORES, warnings aceptables
- **Criterio**: Build exitoso, output solo contiene biblioteca

#### C2: Verificación estructura ⏱️ 10 min
- [ ] Navegar HTML generado
- [ ] Verificar arc42 estructura: secciones, tips, ejemplos, diagramas, figuras
- [ ] Verificar índices funcionan
- [ ] Sin emojis en páginas .rst
- **Criterio**: HTML navegable y correcto

#### C3: Documentar trabajo (work-logger) ⏱️ 10 min
- [ ] Crear work-log de la sesión
- [ ] Documentar decisiones clave
- [ ] Listar archivos afectados
- **Criterio**: Work-log creado en `.mywork/work-logs/`

---

### GRUPO D: Git y Cierre (Variable)

#### D1: Commits organizados ⏱️ 15 min
**Commit 1**: Reorganización general
```
refactor(estructura): separar biblioteca pública de pipeline privado

- source/ ahora solo contiene biblioteca/ (contenido público)
- pipeline_docs_work/ contiene docs internas
  - procedimientos/ (01-10)
  - metodologia/ (docs_maestros)
  - arc42 work files
- archivados/ contiene diataxis y docs obsoletos
- Build Sphinx publica SOLO biblioteca

BREAKING CHANGE: Estructura completamente reorganizada
```

**Commit 2**: Reorganización arc42
```
refactor(arc42): reorganizar por tipo de contenido

- Eliminada carpeta sections/
- Estructura por sección: secciones/, tips/, ejemplos/, diagramas/, figuras/
- Contenido privado movido a pipeline_docs_work
- Índices creados sin emojis

Patrón repetido en 12 secciones de arc42
```

- **Criterio**: 2 commits con mensajes conventional commits

#### D2: Tag de versión ⏱️ 2 min
- [ ] `git tag reorganizacion-biblioteca-v1.0.0`
- **Criterio**: Tag creado

---

## 📊 CHECKLIST DE COMPLETITUD

### Estructura Final Esperada

**PÚBLICO** (`source/biblioteca`):
```
✅ ingenieria/sistemas/arquitectura/arc42_documentation/
   ✅ index.rst
   ✅ 01_introduction_goals/
      ✅ index.rst
      ✅ secciones/
      ✅ tips/
      ✅ ejemplos/
      ✅ diagramas/
      ✅ figuras/
   ✅ 02_constraints/...
   ✅ ... (hasta 12_glossary)
```

**PRIVADO** (`pipeline_docs_work`):
```
✅ ingenieria/sistemas/arquitectura/arc42_documentation/
   ✅ README.md
   ✅ originales/
   ✅ metadata/
   ✅ reportes/
   ✅ trabajo/
```

**GENERAL** (`source/`):
```
✅ index.rst (solo apunta a biblioteca)
✅ biblioteca/ (único contenido)
✅ _static/
✅ _templates/
✅ NO hay 01-10/
✅ NO hay docs_maestros/
✅ NO hay diataxis/
```

### Build Sphinx
```
✅ make html → SUCCESS
✅ 0 ERRORES
✅ build/html/ contiene SOLO biblioteca/
✅ NO contiene 01-10, docs_maestros
```

### Git
```
✅ 2 commits creados
✅ Tag creado
✅ Git status limpio
✅ Backup tag anterior existe
```

---

## ⚠️ RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Romper build Sphinx | Media | Alto | Validar después de cada grupo de tareas |
| Perder contenido | Baja | Crítico | Backup git existe (tag backup-antes-reorganizacion-20260201) |
| Referencias rotas en .rst | Alta | Medio | Verificar índices y toctrees |
| Emojis en .rst | Media | Bajo | Revisar manualmente archivos creados |

---

## 🎯 ORDEN DE EJECUCIÓN

**SECUENCIAL** (no paralelizable):
1. GRUPO A (arc42) → 1 hora
2. GRUPO B (general) → 30 min
3. GRUPO C (validación) → 30 min
4. GRUPO D (git) → 15-20 min

**Total estimado**: 2 horas 15 min

---

## 📝 NOTAS

- **CRÍTICO**: NO usar emojis en archivos .rst
- Validar build después de Grupo A y Grupo B
- Si algo falla, rollback con: `git reset --hard backup-antes-reorganizacion-20260201`
- Documentar cualquier desviación del plan

---

**Estado**: ✅ LISTO PARA FASE 4 (Implementation)  
**Aprobación usuario**: PENDIENTE

