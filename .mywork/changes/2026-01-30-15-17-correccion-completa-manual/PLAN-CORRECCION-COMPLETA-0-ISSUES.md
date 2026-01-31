# Plan de Corrección Completa Manual - Meta: 0 ERROR y 0 WARNING

**Fecha**: 2026-01-30  
**Estrategia**: Opción A - Corrección completa MANUAL  
**Meta**: 0 CRITICAL, 0 ERROR, 0 WARNING  
**Tiempo estimado**: 2-3 horas  
**Enfoque**: Corrección manual archivo por archivo, sin scripts automáticos  

---

## 📊 Estado Inicial (después de 23 commits previos)

**Issues corregidos hasta ahora**: ~409 issues eliminados (-36%)

**Estado actual estimado**:
- CRITICAL: ~15 restantes
- ERROR: ~19 restantes  
- WARNING: ~680 restantes
- **TOTAL: ~714 issues restantes**

**Base**: Log original con 1,123 issues totales

---

## 🎯 Decisiones Tomadas

### 1. Enfoque
- ✅ **Corrección completa**: Todos los issues, sin excepciones
- ✅ **Manual**: Sin scripts automáticos, control total
- ✅ **Archivo por archivo**: Revisión minuciosa

### 2. Archivos arc42 originales
- ✅ **Modificar**: Sí, corregir WARNING de headers en arc42/*
- ❌ **NO usar suppress_warnings**: Queremos 0 issues reales

### 3. Imágenes faltantes
- **Decisión pendiente** (se resolverá durante ejecución)
- Opciones disponibles:
  - Crear placeholders
  - Actualizar paths
  - Comentar referencias

### 4. Nivel de automatización
- ✅ **Mínimo**: Todo manual con validación continua

---

## 📋 Plan de Ejecución - 4 Fases

### FASE 1: Eliminar ERROR restantes (~19 issues)
**Tiempo estimado**: 30-60 minutos  
**Prioridad**: CRÍTICA  

**Estrategia**:
1. Identificar archivos exactos con ERROR
2. Analizar tipo de ERROR
3. Corregir uno por uno manualmente
4. Validar cada corrección
5. Commit incremental por grupo de archivos

**Archivos conocidos con ERROR**:
- introduccion_tip-21.rst (1 ERROR: list-table)
- glossary_tip_4.rst (2 ERROR: list-table vacío + parsing)
- Otros por identificar en build

**Patrones esperados**:
- List-tables malformados
- Directivas vacías
- Enlaces inválidos
- Targets no definidos

---

### FASE 2: Eliminar WARNING Categoría 1 - Espacios en blanco (~399 issues)
**Tiempo estimado**: 45-60 minutos  
**Prioridad**: ALTA  

**Tipos de WARNING**:

1. **Block quote ends without blank line (172 issues)**
   - Patrón: Bloque indentado seguido de texto sin línea en blanco
   - Solución: Añadir línea en blanco después de cada block quote
   
2. **Explicit markup ends without blank line (128 issues)**
   - Patrón: Directivas (`.. note::`, `.. code-block::`, etc.) seguidas de texto
   - Solución: Añadir línea en blanco después de directivas
   
3. **Enumerated list ends without blank line (85 issues)**
   - Patrón: Listas numeradas seguidas de texto
   - Solución: Añadir línea en blanco después de listas
   
4. **Bullet list ends without blank line (8 issues)**
   - Patrón: Listas con viñetas seguidas de texto
   - Solución: Añadir línea en blanco
   
5. **Field list ends without blank line (6 issues)**
   - Patrón: Field lists (`:campo: valor`) seguidas de texto
   - Solución: Añadir línea en blanco

**Estrategia**:
1. Usar build log para identificar líneas exactas
2. Editar archivo por archivo usando `str_replace`
3. Añadir línea en blanco donde Sphinx lo requiere
4. Validar en grupos de 10-15 archivos
5. Commit por lote de archivos

**Ejemplo de corrección**:
```rst
ANTES:
.. note::
   Contenido de la nota
Siguiente párrafo <- WARNING aquí

DESPUÉS:
.. note::
   Contenido de la nota

Siguiente párrafo <- OK
```

---

### FASE 3: Eliminar WARNING Categoría 2 - Jerarquía de Headers (~352 issues)
**Tiempo estimado**: 45-75 minutos  
**Prioridad**: ALTA  

**Tipos de WARNING**:

1. **Document starts at H3, not H1 (166 issues)**
   - Archivos que empiezan con `---` (H3 en algunos casos)
   - Solución: Añadir H1 al inicio O convertir primer header a H1

2. **Document starts at H2, not H1 (146 issues)**
   - Archivos que empiezan con headers `===` sin H1 previo
   - Solución: Añadir H1 al inicio O convertir a H1

3. **Document starts at H4, not H1 (27 issues)**
   - Menos común, requiere análisis individual
   - Solución: Reestructurar jerarquía

4. **Non-consecutive header increase (13 issues)**
   - Saltos de H1 a H3, etc.
   - Solución: Añadir nivel intermedio o ajustar niveles

**Estrategia**:

**Opción A - Conservadora** (preferida para arc42):
1. Añadir H1 al inicio del documento
2. Mantener estructura original intacta
3. Ejemplo:
   ```rst
   Nombre del Documento
   ====================
   
   (contenido original con sus headers)
   ```

**Opción B - Modificar jerarquía**:
1. Convertir primer header existente a H1
2. Ajustar todos los headers subsecuentes
3. Más invasivo pero más "correcto"

**Decisión**: Se evaluará caso por caso, priorizando Opción A para arc42

**Archivos afectados**:
- Mayoría en `biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/original/`
- Algunos en secciones traducidas

---

### FASE 4: Eliminar WARNING Categoría 3 - Otros (~168 issues)
**Tiempo estimado**: 30-60 minutos  
**Prioridad**: MEDIA  

**Tipos de WARNING**:

1. **Literal block expected; none found (24 issues)**
   - Patrón: `::` al final de línea pero sin bloque indentado
   - Solución: Añadir bloque indentado O eliminar `::`
   
2. **Missing images (~98 issues)**
   - Paths como `{{site.imageurl}}/...` o paths incorrectos
   - Soluciones:
     - Comentar la directiva `.. image::`
     - Crear placeholder (imagen 1x1 transparente)
     - Actualizar path si sabemos ubicación correcta
   
3. **Duplicate labels (25 issues)**
   - Labels con mismo nombre en múltiples archivos
   - Solución: Renombrar con prefijo único (nombre del archivo)
   - Ejemplo: `.. _introduccion:` → `.. _tip21_introduccion:`
   
4. **Footnotes (4 issues)**
   - Footnotes mal formateados
   - Solución: Corregir sintaxis caso por caso
   
5. **Otros (17 issues)**
   - Line block ends without blank line
   - Inline strong start-string without end-string
   - Solución: Caso por caso

**Estrategia**:
1. Identificar archivos exactos del build log
2. Priorizar: duplicate labels > literal blocks > images > footnotes
3. Corregir manualmente cada tipo
4. Validar después de cada grupo

---

## 🔄 Metodología de Trabajo

### Flujo por Fase

```
1. IDENTIFICAR issues (del build log)
   ↓
2. AGRUPAR por archivo/tipo
   ↓
3. CORREGIR manualmente (str_replace)
   ↓
4. COMMIT incremental
   ↓
5. Repetir hasta completar fase
   ↓
6. BUILD parcial para validar
```

### Commits

**Estrategia de commits**:
- Commits pequeños e incrementales
- 1 commit por cada 5-10 archivos corregidos
- Mensajes descriptivos con número de issues corregidos
- Formato: `fix(fase-X): descripción breve - N issues`

**Ejemplo**:
```
fix(fase-2): añadir líneas en blanco después de block quotes - 25 WARNING
fix(fase-3): añadir H1 a documentos arc42 - 15 WARNING  
```

### Validación

**Builds incrementales**:
- Build después de cada FASE completa
- Analizar resultados con `analyze_build_log.py`
- Comparar progreso vs fase anterior
- Ajustar estrategia si es necesario

**Criterio de éxito por fase**:
- FASE 1: 0 ERROR
- FASE 2: Reducción visible de WARNING categoría 1
- FASE 3: Reducción visible de WARNING categoría 2  
- FASE 4: 0 WARNING totales

---

## 📊 Tracking de Progreso

### Métricas por Fase

| Fase | Métrica Clave | Valor Inicial | Meta | Tiempo |
|------|---------------|---------------|------|--------|
| 1 | ERROR | ~19 | 0 | 30-60min |
| 2 | WARNING (espacios) | ~399 | 0 | 45-60min |
| 3 | WARNING (headers) | ~352 | 0 | 45-75min |
| 4 | WARNING (otros) | ~168 | 0 | 30-60min |

### Checkpoints

**Checkpoint 1 - Post Fase 1**:
- [ ] 0 ERROR verificado con build
- [ ] Log guardado en `.mywork/build-logs/`
- [ ] Commit de cierre de fase

**Checkpoint 2 - Post Fase 2**:
- [ ] WARNING espacios = 0 verificado
- [ ] Build limpio de categoría 1
- [ ] Commit de cierre de fase

**Checkpoint 3 - Post Fase 3**:
- [ ] WARNING headers = 0 verificado
- [ ] Jerarquía correcta en todos los docs
- [ ] Commit de cierre de fase

**Checkpoint 4 - Post Fase 4**:
- [ ] **0 TOTAL ISSUES** verificado con build final
- [ ] Informe final generado
- [ ] Documentación actualizada
- [ ] Commit final con celebración 🎉

---

## 🛠️ Herramientas y Scripts

### Scripts Disponibles (uso opcional)

**Análisis**:
- `scripts/analysis/analyze_build_log.py` - Analizar build log
- `scripts/analysis/categorize_warnings.py` - Categorizar WARNING (si existe)

**Validación**:
- `.mywork/changes/*/validate_and_log.sh` - Build con timestamp

**Helpers** (crear si es necesario):
- Script para contar issues por archivo
- Script para listar archivos con WARNING específico
- Template de corrección por tipo

### Comandos Útiles

**Ver issues de un archivo específico**:
```bash
grep "archivo.rst" build_log.txt
```

**Contar issues por tipo**:
```bash
grep "WARNING:" build_log.txt | cut -d: -f4 | sort | uniq -c | sort -rn
```

**Ver línea específica de archivo**:
```bash
sed -n 'N,Mp' source/ruta/archivo.rst
```

---

## 📝 Registro de Ejecución

### Log de Trabajo

**Formato**:
```
[TIMESTAMP] FASE-X: Iniciando
[TIMESTAMP] FASE-X: Archivo Y corregido (N issues)
[TIMESTAMP] FASE-X: Build validación - Z issues restantes
[TIMESTAMP] FASE-X: Completada - Commit ABC123
```

**Ubicación**: 
- `.mywork/changes/2026-01-30-15-17-correccion-completa-manual/TRACKING-EJECUCION.md`

---

## 🎯 Criterios de Éxito

### Definición de "Completado"

✅ **ÉXITO TOTAL**:
```
building [html]: targets for all source files
build succeeded.

The HTML pages are in build/html.
```

**Sin ningún**:
- CRITICAL
- ERROR
- WARNING

### Validación Final

**Build final limpio**:
```bash
cd /tmp/ADT
make clean
make html 2>&1 | tee build-final-clean.txt
```

**Resultado esperado**:
- Exit code: 0
- Mensaje: "build succeeded."
- Sin CRITICAL/ERROR/WARNING en el log

**Métricas finales**:
- Total issues: 0
- Commits realizados: ~30-40
- Archivos corregidos: ~80-100
- Tiempo total invertido: ~8-10 horas (incluyendo trabajo previo)

---

## 📚 Recursos y Referencias

### Documentación Sphinx

- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Sphinx Build Warnings](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-suppress_warnings)
- [Headers and Sections](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections)

### Archivos de Referencia Internos

- `source/09_referencias/cheatsheets/cheatsheet_rst.rst` - Cheatsheet RST
- `source/05_herramientas_medios/equivalencias/latex_rst_equivalencias.rst` - Equivalencias
- `source/07_guias_uso/troubleshooting.rst` - Solución de problemas

### Commits Previos

- Commits 1-23: Base de correcciones (ver `git log`)
- Patrones identificados en commits previos
- Lecciones aprendidas de correcciones exitosas

---

## 🚨 Riesgos y Mitigaciones

### Riesgos Identificados

1. **Romper referencias cruzadas**
   - Riesgo: Al renombrar labels
   - Mitigación: Buscar referencias antes de renombrar
   - Comando: `grep -r "ref_antiguo" source/`

2. **Modificar semántica de documentos arc42**
   - Riesgo: Cambiar estructura original
   - Mitigación: Opción A conservadora (añadir H1, no modificar resto)

3. **Tiempo excedido**
   - Riesgo: 2-3 horas estimadas pueden ser insuficientes
   - Mitigación: Priorizar FASE 1 y 2, FASE 3 y 4 opcional si necesario

4. **Issues nuevos introducidos**
   - Riesgo: Correcciones crean nuevos problemas
   - Mitigación: Builds incrementales después de cada fase

### Plan de Contingencia

Si después de 3 horas no se alcanza 0 issues:

**Plan B**:
1. Asegurar 0 ERROR (FASE 1 completada)
2. Asegurar WARNING críticos eliminados (FASE 2)
3. Documentar WARNING restantes con justificación
4. Usar `suppress_warnings` selectivo para WARNING no críticos

---

## 📅 Timeline Esperado

```
Hora 0:00 - Inicio FASE 1
Hora 0:30 - Checkpoint 1, inicio FASE 2
Hora 1:15 - Checkpoint 2, inicio FASE 3  
Hora 2:15 - Checkpoint 3, inicio FASE 4
Hora 2:45 - Checkpoint 4, build final
Hora 3:00 - Documentación y cierre
```

---

## ✅ Checklist Pre-inicio

Antes de comenzar, verificar:

- [x] Plan documentado en `.mywork/`
- [ ] Build log original disponible (`/tmp/build_log.txt`)
- [ ] Scripts de análisis funcionales
- [ ] Git en estado limpio (23 commits previos)
- [ ] Backup de archivos críticos (opcional)
- [ ] Entorno de trabajo listo

---

## 🎉 Mensaje de Cierre

Una vez completado:

```
╔════════════════════════════════════════════════════════════════╗
║                     🎊 ¡ÉXITO TOTAL! 🎊                       ║
║                                                                ║
║              BUILD SPHINX 100% LIMPIO                          ║
║          0 CRITICAL | 0 ERROR | 0 WARNING                      ║
║                                                                ║
║  Proyecto ADT - Documentación de Calidad Profesional          ║
╚════════════════════════════════════════════════════════════════╝

Issues corregidos: 1,123 → 0 (-100%)
Commits realizados: ~30-40
Archivos corregidos: ~80-100
Tiempo total: ~8-10 horas

¡Documentación lista para producción! 🚀
```

---

**Fin del Plan**  
**Próximo paso**: Ejecutar FASE 1
