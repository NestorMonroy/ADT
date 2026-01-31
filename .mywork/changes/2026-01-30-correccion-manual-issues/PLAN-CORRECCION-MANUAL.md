# Plan de Corrección Manual de Issues Sphinx

**Fecha**: 2026-01-30  
**Estrategia**: Corrección manual archivo por archivo  
**Validación**: Build incremental después de cada lote  

---

## 📊 Estado Actual (2026-01-30 05:34:16)

### Issues Totales: 1,123

- **CRITICAL**: 93
- **ERROR**: 111  
- **WARNING**: 919

### Logs Guardados

- Build log: `.mywork/build-logs/build-log-2026-01-30-05-34-16.txt`
- Análisis: `.mywork/build-logs/analysis-2026-01-30-05-34-21.txt`

---

## 🎯 Objetivos Realistas

**Meta Principal**: Reducir issues críticos a CERO

- ✅ CRITICAL: 93 → 0 (eliminación completa)
- ✅ ERROR: 111 → 0 (eliminación completa)
- 🎯 WARNING: 919 → < 200 (reducción sustancial)

**Total esperado**: 1,123 → < 200 issues

---

## 📋 Estrategia de Corrección

### Cambio de Enfoque

**❌ Estrategia anterior (FALLIDA)**:
- Scripts automáticos que corregían cosméticamente
- No se validaba el resultado
- Se reportaban resultados sin verificación

**✅ Nueva estrategia (REALISTA)**:
- Corrección manual archivo por archivo
- Validación incremental con `make html` después de cada lote
- Documentación real de resultados con timestamps
- Priorización por severidad: CRITICAL → ERROR → WARNING

---

## 🗂️ Archivos Prioritarios (CRITICAL + ERROR)

### Lote 1: Top 5 archivos más problemáticos

1. **workflow_general.rst** (103 issues)
   - 12 CRITICAL (underlines)
   - 7 ERROR (directivas vacías)
   - 84 WARNING (varios)

2. **GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst** (78 issues)
   - 13 CRITICAL (underlines)
   - 17 ERROR (indentación)
   - 48 WARNING (varios)

3. **latex_rst_equivalencias.rst** (66 issues)
   - 5 CRITICAL (underlines)
   - 17 ERROR (list-table)
   - 44 WARNING (varios)

4. **error_01_omisiones.rst** (58 issues)
   - 23 CRITICAL (underlines)
   - 35 WARNING (varios)

5. **SINTESIS_METODOLOGICA_ADT.rst** (31 issues)
   - 7 CRITICAL (underlines)
   - 1 ERROR (target desconocido)
   - 23 WARNING (varios)

**Total Lote 1**: 336 issues (30% del total)

### Lote 2: Archivos con CRITICAL restantes

6. caso_01_seccion_breve.rst (9 CRITICAL)
7. ARQUITECTURA_TRADUCCION_IACT.rst (5 CRITICAL)
8. traduccion_como_transformacion.rst (4 CRITICAL)
9. WORKFLOW_v1_6_0_ACTUALIZACION.rst (3 CRITICAL)
10. tutorial_completo.rst (2 CRITICAL)

**Total Lote 2**: ~60 issues

### Lote 3: Archivos con ERROR restantes

11. MD_002_cuando_enriquecer.rst (6 ERROR)
12. metadata_libro.rst (2 ERROR)
13. seccion_3_2_contexto_tecnico.rst (2 ERROR malformed table)
14. Otros archivos con ERROR únicos

**Total Lote 3**: ~40 issues

---

## 🔧 Tipos de Correcciones Necesarias

### CRITICAL (93 issues)

**Tipo principal**: Missing matching underline (88/93)

**Causa**: Subrayados de títulos desalineados

**Corrección manual**:
```rst
# MAL:
===========
Título
===========

# BIEN:
===========
Título
===========
(mismo número de caracteres)
```

### ERROR (111 issues)

**Tipos principales**:
1. Unexpected indentation (30 issues)
2. Missing content in directives (16 issues)
3. list-table parsing errors (16 issues)

**Correcciones**:
1. Revisar indentación (espacios vs tabs)
2. Agregar contenido a directivas vacías o eliminarlas
3. Corregir formato de list-table

### WARNING (919 issues)

**Tipos principales**:
1. Missing images (98 issues)
2. Duplicate labels (25 issues)
3. List formatting (8 issues)

**Correcciones selectivas** (prioridad baja)

---

## 📅 Plan de Ejecución

### Fase 1: Corrección Lote 1 (2-3 horas)

**Archivos**: Top 5 más problemáticos

**Proceso**:
1. Abrir archivo en editor
2. Buscar CRITICAL issues en build log
3. Corregir manualmente cada issue
4. Guardar
5. Ejecutar `make clean && make html > build-log-TIMESTAMP.txt 2>&1`
6. Analizar nuevo log con `analyze_build_log.py`
7. Verificar que issues DISMINUYERON
8. Commit: `fix(manual): corregir [archivo] - X issues resueltos`
9. Repetir con siguiente archivo

**Criterio de éxito**: Reducir al menos 250 issues

### Fase 2: Corrección Lote 2 (1-2 horas)

**Archivos**: CRITICAL restantes

**Proceso**: Mismo que Fase 1

**Criterio de éxito**: 0 CRITICAL issues

### Fase 3: Corrección Lote 3 (1-2 horas)

**Archivos**: ERROR restantes

**Proceso**: Mismo que Fase 1

**Criterio de éxito**: 0 ERROR issues

### Fase 4: WARNING selectivos (1 hora)

**Enfoque**: Solo los más frecuentes

**Criterio de éxito**: < 200 WARNING totales

---

## ✅ Criterios de Validación

**Cada lote debe**:
1. Reducir issues, no aumentarlos
2. Tener build log guardado con timestamp
3. Tener análisis guardado con timestamp
4. Tener commit descriptivo

**Al final del proceso**:
1. 0 CRITICAL
2. 0 ERROR
3. < 200 WARNING
4. Build HTML exitoso
5. Documentación real de resultados

---

## 📝 Registro de Progreso

### Baseline (2026-01-30 05:34:16)

```
CRITICAL:   93
ERROR:     111
WARNING:   919
TOTAL:   1,123
```

### Lote 1 - [PENDIENTE]

**Archivos corregidos**: 
- [ ] workflow_general.rst
- [ ] GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
- [ ] latex_rst_equivalencias.rst
- [ ] error_01_omisiones.rst
- [ ] SINTESIS_METODOLOGICA_ADT.rst

**Resultado**: [pendiente]

### Lote 2 - [PENDIENTE]

**Resultado**: [pendiente]

### Lote 3 - [PENDIENTE]

**Resultado**: [pendiente]

### Lote 4 - [PENDIENTE]

**Resultado**: [pendiente]

---

## 🚀 Próximos Pasos

1. ✅ Crear este plan
2. ⏳ Comenzar con Lote 1 - workflow_general.rst
3. ⏳ Validar con build incremental
4. ⏳ Continuar con resto de Lote 1

---

## 📚 Referencias

- Build log: `.mywork/build-logs/build-log-2026-01-30-05-34-16.txt`
- Script de análisis: `scripts/analysis/analyze_build_log.py`
- Documentación RST: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
