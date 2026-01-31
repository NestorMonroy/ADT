# Requirements: Corrección de Errores de Build Sphinx

**Versión**: 1.0.0
**Fecha**: 2026-01-30
**Estado**: Draft
**Tipo**: Refactoring / Quality Assurance

## Control de Versiones

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0.0 | 2026-01-30 | Claude | Versión inicial con sistema de versionado semántico. Consideración de actualización/creación de scripts con programación funcional |

## 1. Contexto

### 1.1 Situación Actual

El proyecto ADT Documentation cuenta con 730 archivos fuente (RST/MD) compilados con Sphinx 8.2.3. Un análisis exhaustivo del build HTML reveló **949 issues** categorizados en tres niveles de severidad:

- **CRITICAL**: 33 (3.5%) - Problemas estructurales graves
- **ERROR**: 72 (7.6%) - Errores que afectan el renderizado
- **WARNING**: 844 (88.9%) - Advertencias de calidad

**Documentación del análisis**:
- Work-log: `.mywork/work-logs/2026-01-30-03-27-analisis-completo-build-sphinx-errores-warnings.md`
- Reporte detallado: `build_validation_report.md`
- Log completo: `build_output_full.log`

### 1.2 Estado del Build

Actualmente el build **completa con exit code 0** pero contiene:
- 105 issues bloqueantes (CRITICAL + ERROR)
- 844 warnings que degradan la calidad
- Archivos HTML generados pero con defectos de renderizado

### 1.3 Impacto en el Proyecto

**Problemas actuales**:
- Estructura de secciones rota en múltiples documentos
- Imágenes no cargadas (142 referencias rotas)
- Navegación confusa por niveles de encabezados incorrectos
- Referencias ambiguas por labels duplicados
- Contenido mal formateado (listas, tablas, bloques)

**Deuda técnica**:
- Imposibilidad de detectar nuevos errores en el ruido
- Riesgo de propagar problemas a nuevas traducciones
- Dificultad para validar calidad de contribuciones
- Barrera para nuevos colaboradores

### 1.4 Por Qué Es Necesario

1. **Calidad profesional**: La documentación debe ser un referente
2. **Mantenibilidad**: Reducir deuda técnica acumulada
3. **Baseline establecida**: Partir de estado limpio para mejoras futuras
4. **Validación efectiva**: CI/CD requiere builds limpios
5. **Experiencia de usuario**: Navegación y presentación correctas

## 2. Problema

### 2.1 Definición del Problema

**Problema principal**: El build de Sphinx contiene 949 issues que degradan la calidad de la documentación y generan deuda técnica.

**Subproblemas identificados**:

1. **Estructura documental rota** (33 CRITICAL + 28 ERROR indentación)
   - Secciones con jerarquía incorrecta
   - Títulos mal formados
   - Bloques de contenido mal parseados

2. **Contenido visual deficiente** (142 WARNING imágenes)
   - Referencias a imágenes no resueltas
   - Variables de template sin expandir

3. **Formato inconsistente** (188 WARNING listas/tablas)
   - Listas terminadas sin línea en blanco
   - Tablas con sintaxis incorrecta
   - Markup inline mal formado

4. **Navegación problemática** (339 WARNING heading levels)
   - Headers que empiezan en nivel incorrecto
   - Saltos de niveles no consecutivos
   - Afecta TOC y estructura

5. **Referencias ambiguas** (43 WARNING labels duplicados)
   - autosectionlabel genera conflictos
   - Enlaces pueden apuntar a lugar incorrecto

### 2.2 Usuarios Afectados

- **Lectores de la documentación**: Navegación confusa, contenido mal formado
- **Contribuidores**: Difícil validar sus cambios
- **Mantenedores**: Ruido impide detectar nuevos problemas
- **CI/CD**: Imposible establecer thresholds de calidad

### 2.3 Situación Deseada

Build de Sphinx que:
- ✅ Completa con 0 CRITICAL
- ✅ Completa con 0 ERROR
- ✅ Tiene < 50 WARNING (solo los inevitables)
- ✅ Genera HTML correctamente estructurado
- ✅ Permite validación efectiva en CI/CD

## 3. Objetivos

### 3.1 Objetivo Principal

**Reducir los issues del build de Sphinx de 949 a < 50, eliminando todos los CRITICAL y ERROR, para establecer una baseline de calidad que permita mantenimiento efectivo del proyecto.**

### 3.2 Objetivos Secundarios

1. **Objetivo S1**: Eliminar 100% de CRITICAL (33 issues)
   - Reparar estructura de secciones
   - Corregir títulos mal formados

2. **Objetivo S2**: Eliminar 100% de ERROR (72 issues)
   - Corregir indentación (28)
   - Parsear correctamente bloques de contenido (18)
   - Resolver contenido faltante (11)

3. **Objetivo S3**: Reducir WARNING críticos (prioridad alta)
   - Corregir 339 heading levels
   - Resolver 142 imágenes faltantes
   - Normalizar 100 listas mal formadas

4. **Objetivo S4**: Documentar proceso
   - Generar specs completos (4 fases)
   - Registrar decisiones técnicas
   - Crear guías para evitar regresión

5. **Objetivo S5**: Establecer prevención
   - Aplicar scripts de normalización
   - Configurar validación pre-commit
   - Documentar reglas preventivas

## 4. Requisitos Funcionales

### RF-001: Eliminar CRITICAL - Section Title Issues (25)
- **Descripción**: Corregir títulos de sección inesperados y estructura jerárquica
- **Prioridad**: CRÍTICA
- **Categoría afectada**: Section Title Issues (25 CRITICAL)
- **Archivos afectados**: ~25 archivos RST
- **Criterio de aceptación**: 
  - `grep "CRITICAL.*Section title" build_log.txt` retorna 0 resultados
  - Estructura de secciones sigue jerarquía correcta
  - Build completo sin CRITICAL

### RF-002: Eliminar CRITICAL - Title Underline (8)
- **Descripción**: Corregir underlines de títulos que no coinciden con longitud
- **Prioridad**: CRÍTICA
- **Categoría afectada**: Title Underline (8 CRITICAL)
- **Criterio de aceptación**:
  - Todos los underlines coinciden con título
  - `grep "CRITICAL.*underline" build_log.txt` retorna 0 resultados

### RF-003: Eliminar ERROR - Indentation (28)
- **Descripción**: Corregir indentación inesperada en bloques RST
- **Prioridad**: ALTA
- **Archivos principales**:
  - `02_procedimientos/workflow_general.rst`
  - `04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer.rst`
  - `05_herramientas_medios/equivalencias/latex_rst_equivalencias.rst`
- **Criterio de aceptación**:
  - `grep "ERROR.*Unexpected indentation" build_log.txt` retorna 0 resultados
  - Todos los bloques correctamente indentados según RST spec

### RF-004: Eliminar ERROR - Content Block Parsing (18)
- **Descripción**: Corregir bloques de contenido mal formados
- **Prioridad**: ALTA
- **Criterio de aceptación**:
  - Directivas con sintaxis correcta
  - `grep "ERROR.*parsing content block" build_log.txt` retorna 0 resultados

### RF-005: Eliminar ERROR - Missing Content (11)
- **Descripción**: Agregar contenido faltante en directivas que lo requieren
- **Prioridad**: ALTA
- **Criterio de aceptación**:
  - Todas las directivas tienen contenido requerido
  - `grep "ERROR.*Content block expected" build_log.txt` retorna 0 resultados

### RF-006: Corregir WARNING - Document Heading Levels (339)
- **Descripción**: Normalizar niveles de encabezados para que empiecen correctamente
- **Prioridad**: ALTA
- **Impacto**: 35.7% de todos los warnings
- **Estrategia**: Uso de script de normalización automática
- **Criterio de aceptación**:
  - Headers empiezan en nivel apropiado (H1 para documentos)
  - Reducción de 339 a < 10 warnings de este tipo

### RF-007: Resolver WARNING - Missing Images (142)
- **Descripción**: Resolver referencias a imágenes no encontradas
- **Prioridad**: MEDIA
- **Subcasos**:
  - Variables `{{site.imageurl}}` sin expandir
  - Rutas incorrectas a archivos de imagen
- **Criterio de aceptación**:
  - Variables de template configuradas o reemplazadas
  - Todas las rutas de imágenes válidas
  - Reducción de 142 a < 5 warnings

### RF-008: Normalizar WARNING - List Formatting (100)
- **Descripción**: Corregir listas mal formateadas
- **Prioridad**: MEDIA
- **Estrategia**: Uso de `scripts/fix_list_spacing.py`
- **Criterio de aceptación**:
  - Listas terminan con línea en blanco
  - Formato consistente según RST spec
  - Reducción de 100 a < 5 warnings

### RF-009: Corregir WARNING - Title Formatting (88)
- **Descripción**: Normalizar formato de títulos (overline/underline)
- **Prioridad**: MEDIA
- **Criterio de aceptación**:
  - Underlines de longitud correcta
  - Caracteres de subrayado consistentes por nivel
  - Reducción de 88 a 0 warnings

### RF-010: Resolver WARNING - Duplicate Labels (43)
- **Descripción**: Eliminar o renombrar labels duplicados
- **Prioridad**: MEDIA
- **Estrategia**: Uso de `scripts/find_duplicate_labels.py` para identificar
- **Criterio de aceptación**:
  - Cada label único en el árbol `source/`
  - Referencias funcionan sin ambigüedad
  - 0 labels duplicados

### RF-011: Evaluar y Aplicar Scripts de Normalización
- **Descripción**: Evaluar efectividad de scripts existentes y aplicar/actualizar según necesidad
- **Prioridad**: MEDIA
- **Scripts existentes a evaluar**:
  - `scripts/fix_list_spacing.py`
  - `scripts/fix_list_table_spacing.py`
  - `scripts/fix_glossary_indentation.py`
  - `scripts/fix_unknown_lexers.py`
  - `scripts/find_duplicate_labels.py`
  - `scripts/find_duplicate_toctree.py`
- **Consideración crítica**: Los scripts existentes **pueden no resolver completamente** los problemas detectados
- **Acciones requeridas**:
  - Validar efectividad de cada script contra issues detectados
  - Actualizar scripts que no funcionen correctamente
  - Crear nuevos scripts si los existentes son insuficientes
- **Criterio de aceptación**:
  - Scripts validados contra casos reales del proyecto
  - Scripts actualizados usan programación funcional
  - Nuevos scripts (si necesarios) siguen estándares del proyecto
  - Todos los scripts ejecutados sin errores
  - Validación post-ejecución demuestra reducción de issues

### RF-012: Desarrollar/Actualizar Scripts con Programación Funcional
- **Descripción**: Crear o actualizar scripts de corrección siguiendo paradigma funcional
- **Prioridad**: ALTA
- **Paradigma requerido**: Programación funcional
- **Principios a seguir**:
  - Funciones puras (sin efectos secundarios)
  - Inmutabilidad de datos
  - Composición de funciones
  - Expresividad y legibilidad
  - Testabilidad (unit tests con pytest)
- **Scripts que probablemente requieren actualización**:
  - `fix_list_spacing.py` - Puede no cubrir todos los casos de listas
  - `fix_list_table_spacing.py` - Puede no manejar todas las variantes de list-table
  - `fix_glossary_indentation.py` - Puede no normalizar correctamente todos los casos
- **Scripts que probablemente requieren creación**:
  - `fix_heading_levels.py` - Para normalizar 339 warnings de heading levels
  - `fix_title_underlines.py` - Para corregir underlines de títulos
  - `fix_section_structure.py` - Para reparar estructura de secciones
  - `fix_indentation_errors.py` - Para corregir 28 errors de indentación
  - `resolve_image_references.py` - Para resolver 142 referencias de imágenes
- **Estándares de código**:
  - Type hints completos (Python 3.10+)
  - Docstrings en formato Google
  - Tests con pytest (coverage > 80%)
  - Linting con mypy + black
- **Criterio de aceptación**:
  - Scripts siguen principios de programación funcional
  - Tests automatizados con > 80% coverage
  - Documentación completa (docstrings + README)
  - Validación en dry-run mode antes de aplicar cambios
  - Scripts reusables para mantenimiento futuro

### RF-013: Generar Reporte de Progreso
- **Descripción**: Generar reporte comparable antes/después
- **Prioridad**: BAJA
- **Criterio de aceptación**:
  - Reporte inicial (baseline): 949 issues
  - Reporte final: < 50 issues
  - Métrica de mejora: > 95% reducción

## 5. Requisitos No Funcionales

### RNF-001: Preservación de Contenido
- **Descripción**: Las correcciones NO deben alterar el contenido semántico
- **Restricción**: Solo cambios de formato, nunca de significado
- **Validación**: Diff manual de archivos críticos

### RNF-002: Reproducibilidad
- **Descripción**: El proceso debe ser reproducible
- **Criterio**: Todos los pasos documentados en specs
- **Validación**: Otro colaborador puede replicar el proceso

### RNF-003: Reversibilidad
- **Descripción**: Debe ser posible revertir cambios
- **Estrategia**: 
  - Commits atómicos por categoría
  - Tags en puntos de checkpoint
  - Backup antes de modificaciones masivas
- **Validación**: Plan de rollback documentado

### RNF-004: Performance del Build
- **Descripción**: Correcciones no deben degradar tiempo de build
- **Métrica**: Tiempo actual ~25s debe mantenerse
- **Validación**: Benchmark antes/después

### RNF-005: Compatibilidad
- **Descripción**: Mantener compatibilidad con Sphinx 8.2.3
- **Restricción**: No cambiar versiones de dependencias
- **Validación**: Build en entorno existente

### RNF-006: Calidad del Código
- **Descripción**: Correcciones siguen best practices de RST
- **Referencia**: `.codex/skills/sphinx-expert/SKILL.md`
- **Validación**: Revisión contra reglas documentadas

### RNF-007: Paradigma de Programación Funcional en Scripts
- **Descripción**: Todos los scripts deben seguir paradigma de programación funcional
- **Principios obligatorios**:
  - **Funciones puras**: Sin efectos secundarios, mismo input → mismo output
  - **Inmutabilidad**: Datos no se modifican, se crean nuevas versiones
  - **Composición**: Funciones pequeñas combinadas en pipelines
  - **Declarativo**: Enfoque en "qué" no en "cómo"
  - **Type safety**: Type hints completos y validados con mypy
- **Patrones recomendados**:
  - `map()`, `filter()`, `reduce()` sobre loops imperativos
  - List/dict comprehensions cuando apropiado
  - `functools` y `itertools` para composición
  - Pattern matching (Python 3.10+)
  - Closures y higher-order functions
- **Evitar**:
  - Variables globales mutables
  - Loops con side-effects
  - Modificación in-place de estructuras
  - Estado compartido entre funciones
- **Beneficios esperados**:
  - Código más testeable (funciones puras)
  - Menos bugs (sin efectos secundarios)
  - Más reusable (composición)
  - Más mantenible (declarativo)
- **Validación**:
  - Code review verifica principios funcionales
  - Tests unitarios cubren funciones puras
  - Mypy valida type hints sin errores
  - Ejemplos de uso en docstrings

## 6. Restricciones

### 6.1 Técnicas

- **R1**: NO modificar `conf.py` excepto si es esencial
- **R2**: NO cambiar versiones de paquetes Python
- **R3**: NO alterar estructura de directorios existente
- **R4**: EVALUAR scripts existentes antes de crear duplicados
- **R5**: RESPETAR nomenclatura de archivos (XX_nombre/)
- **R6**: MANTENER metadata existente en archivos
- **R7**: USAR programación funcional en todos los scripts (nuevos y actualizados)
- **R8**: VALIDAR scripts en dry-run mode antes de aplicar cambios reales

### 6.2 Proceso

- **R7**: Correcciones incrementales por categoría
- **R8**: Validación después de cada lote
- **R9**: Commits frecuentes (cada 5-10 archivos)
- **R10**: Documentación de decisiones no obvias
- **R11**: Aprobación de usuario entre fases de spec

### 6.3 Alcance

- **R12**: Solo archivos en `source/` (no tocar raíz del proyecto)
- **R13**: Solo correcciones de errores (no mejoras de contenido)
- **R14**: Solo issues detectados en análisis actual
- **R15**: No agregar nueva funcionalidad

## 7. Fuera de Alcance

Las siguientes actividades **NO** están incluidas en este spec:

### Explícitamente Excluidas

- ❌ Traducción de nuevo contenido
- ❌ Mejora del contenido existente (reescritura)
- ❌ Actualización de versiones de Sphinx o extensiones
- ❌ Cambios en `conf.py` no relacionados con errores
- ❌ Reorganización de estructura de carpetas
- ❌ Creación de nuevos documentos de contenido
- ❌ Migración a nuevo tema o template
- ❌ Optimización de performance del build (más allá de mantener tiempo actual)

### Explícitamente Incluidas (para claridad)

- ✅ Desarrollo/actualización de scripts de corrección con programación funcional
- ✅ Tests automatizados para scripts (pytest)
- ✅ Documentación de scripts creados/actualizados
- ✅ Validación de efectividad de scripts existentes
- ✅ Corrección manual cuando scripts sean insuficientes

### Para Abordar en Futuro

- 📋 Intersphinx warnings (2) - requiere configuración de red
- 📋 Pygments lexers desconocidos (22) - requiere instalación de extensiones
- 📋 Glossary terms faltantes (17) - requiere decisión de contenido
- 📋 Warnings de "Other" (32) - requieren análisis caso por caso

## 8. Stakeholders

### Usuario Principal
- **Rol**: Propietario del proyecto ADT
- **Interés**: Documentación de calidad profesional
- **Responsabilidad**: Aprobar cada fase de spec
- **Criterio de satisfacción**: Build limpio, contenido preservado

### Contribuidores Futuros
- **Rol**: Desarrolladores que trabajarán en el proyecto
- **Interés**: Baseline limpia, proceso documentado
- **Beneficio**: Entender decisiones técnicas, replicar proceso

### Lectores de la Documentación
- **Rol**: Usuarios finales de la documentación HTML
- **Interés**: Navegación correcta, contenido bien presentado
- **Beneficio**: Experiencia de lectura profesional

### Sistema de CI/CD (futuro)
- **Rol**: Automatización de validación
- **Interés**: Build predecible, thresholds establecidos
- **Beneficio**: Puede bloquear regresiones

## 9. Métricas de Éxito

### Métricas Cuantitativas

| Métrica | Baseline | Objetivo | Medición |
|---------|----------|----------|----------|
| CRITICAL | 33 | 0 | grep count en log |
| ERROR | 72 | 0 | grep count en log |
| WARNING | 844 | < 50 | grep count en log |
| Total Issues | 949 | < 50 | suma de arriba |
| Reducción % | 0% | > 95% | (baseline - actual) / baseline |
| Build Time | ~25s | ~25s ±10% | time make html |
| Exit Code | 0 | 0 | $? después de make |

### Métricas Cualitativas

- ✅ Documentación profesional y navegable
- ✅ Proceso documentado y reproducible
- ✅ Scripts de normalización aplicados
- ✅ Decisiones técnicas registradas
- ✅ Reglas preventivas documentadas

## 10. Referencias

### Documentación Previa

- **Análisis completo**: `.mywork/work-logs/2026-01-30-03-27-analisis-completo-build-sphinx-errores-warnings.md`
- **Reporte de issues**: `build_validation_report.md`
- **Log de build**: `build_output_full.log`

### Skills y Metodología

- **Spec-Driven Dev**: `.codex/skills/spec-driven-dev/SKILL.md`
- **Sphinx Expert**: `.codex/skills/sphinx-expert/SKILL.md`
- **Validation Suite**: `.codex/skills/validation-suite/SKILL.md`
- **Work Logger**: `.codex/skills/work-logger/SKILL.md`

### Scripts Disponibles (a evaluar y posiblemente actualizar)

Los siguientes scripts existen pero **pueden requerir actualización o extensión**:

**Scripts de corrección existentes**:
- `scripts/fix_list_spacing.py` - Corrección de espaciado en listas
- `scripts/fix_list_table_spacing.py` - Corrección de tablas list-table
- `scripts/fix_glossary_indentation.py` - Normalización de glosarios
- `scripts/fix_unknown_lexers.py` - Reemplazo de lexers desconocidos
- `scripts/fix_meta_transition.py` - Corrección de transiciones meta
- `scripts/fix_blanklines_and_listtable_fp.py` - Corrección de líneas en blanco
- `scripts/fix_list_table_blocks_fp.py` - Corrección de bloques list-table
- `scripts/fix_list_table_indent_fp.py` - Corrección de indentación list-table

**Scripts de análisis existentes**:
- `scripts/find_duplicate_labels.py` - Detección de labels duplicados
- `scripts/find_duplicate_toctree.py` - Detección de toctree duplicados
- `scripts/validar_estructura.sh` - Validación de estructura de directorios

**Consideraciones importantes**:
1. ⚠️ Scripts existentes fueron creados para casos específicos pasados
2. ⚠️ Pueden no cubrir todos los casos detectados en análisis actual (949 issues)
3. ⚠️ Requieren validación contra issues reales antes de confiar en ellos
4. ⚠️ Pueden necesitar actualización para usar programación funcional
5. ⚠️ Algunos issues (ej. 339 heading levels) no tienen script correspondiente

**Estrategia recomendada**:
1. **Evaluar** cada script existente contra subset de issues detectados
2. **Actualizar** scripts que funcionan parcialmente pero necesitan mejoras
3. **Crear** nuevos scripts para categorías sin herramienta existente
4. **Refactorizar** a programación funcional si usan estilo imperativo
5. **Testear** todos los scripts con pytest antes de aplicar masivamente

### Documentación Sphinx

- [Sphinx RST Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [reStructuredText Directives](https://docutils.sourceforge.io/docs/ref/rst/directives.html)

## 11. Riesgos y Mitigaciones

### Riesgo 1: Romper Contenido Existente
- **Probabilidad**: Media
- **Impacto**: Alto
- **Mitigación**: 
  - Validación incremental después de cada lote
  - Commits atómicos por categoría
  - Backup antes de cambios masivos
  - Revisión manual de archivos críticos

### Riesgo 2: Correcciones Incompletas
- **Probabilidad**: Baja
- **Impacto**: Medio
- **Mitigación**:
  - Scripts automatizados cuando sea posible
  - Checklist detallada en Tasks
  - Validación con métricas cuantitativas

### Riesgo 3: Tiempo Subestimado
- **Probabilidad**: Media
- **Impacto**: Bajo
- **Mitigación**:
  - Priorización clara (CRITICAL → ERROR → WARNING)
  - Posibilidad de pausar después de cada categoría
  - Documentación permite reanudar fácilmente

### Riesgo 4: Nuevos Errores Introducidos
- **Probabilidad**: Baja
- **Impacto**: Medio
- **Mitigación**:
  - Validación continua con `make html`
  - Comparación de diff antes de commit
  - Tests de scripts con pytest cuando existan

### Riesgo 5: Scripts Existentes Insuficientes o Defectuosos
- **Probabilidad**: Media-Alta
- **Impacto**: Alto
- **Descripción**: Scripts existentes pueden no resolver los issues o introducir nuevos problemas
- **Mitigación**:
  - Validar cada script contra muestra de archivos reales
  - Ejecutar en dry-run mode primero
  - Comparar output esperado vs. obtenido
  - Actualizar o reescribir scripts según necesidad
  - Crear tests unitarios para validar comportamiento
  - Aplicar programación funcional para reducir side-effects
  - Revisión manual de cambios críticos
- **Plan de contingencia**:
  - Si script falla: Corrección manual + documentar para futuro script
  - Si script daña archivos: Rollback desde commit previo
  - Si script es insuficiente: Desarrollo de nuevo script funcional

## 12. Criterios de Aceptación Global

Este spec será considerado **COMPLETADO** cuando:

### Criterios Obligatorios (MUST)

1. ✅ Build de Sphinx completa con 0 CRITICAL
2. ✅ Build de Sphinx completa con 0 ERROR
3. ✅ Total de WARNING < 50
4. ✅ Exit code de `make html` = 0
5. ✅ Contenido semántico preservado (validación manual)
6. ✅ Todas las fases de spec completadas y aprobadas
7. ✅ Work-log final documentando el proceso
8. ✅ Commits en repositorio con mensajes descriptivos
9. ✅ Scripts desarrollados/actualizados usan programación funcional
10. ✅ Scripts tienen tests automatizados con pytest (coverage > 80%)

### Criterios Deseables (SHOULD)

1. 📝 WARNING reducidos a < 30
2. 📝 Todos los scripts evaluados y validados contra issues reales
3. 📝 Scripts nuevos documentados con docstrings completos
4. 📝 Guía de prevención de regresiones documentada
5. 📝 Reporte antes/después con métricas
6. 📝 Scripts tienen type hints completos validados con mypy

### Criterios Opcionales (COULD)

1. 💡 Dashboard de métricas de calidad
2. 💡 Hooks pre-commit configurados con scripts
3. 💡 Integración básica en CI/CD
4. 💡 Scripts optimizados para performance (procesamiento paralelo)

## 13. Próximos Pasos

Una vez este documento de Requirements sea **APROBADO**:

1. ➡️ Proceder a **FASE 2: Design**
2. Crear archivo: `2026-01-30-XX-XX-design-corregir-errores-build.md`
3. Definir estrategia técnica, orden de corrección, plan de validación
4. **SOLICITAR APROBACIÓN** antes de FASE 3

---

**Archivo**: `.mywork/changes/2026-01-30-corregir-errores-build-sphinx/2026-01-30-03-31-requirements-corregir-errores-build.md`

**Versión**: 1.0.0

**Estado**: Draft → **Esperando Aprobación del Usuario**

**Autor**: Claude (AI Assistant)

**Proyecto**: ADT Documentation v1.7.1

**Tipo de Cambio**: Refactoring / Quality Assurance

**Estimación de Impacto**: Alto - Afecta 949 issues en 730 archivos

**Fecha de Creación**: 2026-01-30 03:31

**Última Actualización**: 2026-01-30 03:40

**Cambios en v1.0.0**:
- Agregado sistema de versionado semántico (x.x.x)
- Actualizado RF-011: Considerar que scripts pueden necesitar actualización
- Agregado RF-012: Desarrollo/actualización de scripts con programación funcional
- Agregado RNF-007: Requisito de paradigma funcional en scripts
- Actualizado R7-R8: Restricciones sobre programación funcional y dry-run
- Actualizado Riesgo 5: Scripts existentes pueden ser insuficientes
- Clarificado alcance: Desarrollo de scripts está INCLUIDO
- Actualizados criterios de aceptación: Scripts con tests y type hints
