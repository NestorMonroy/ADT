# Templates de Incremental Correction Methodology

Directorio: `.codex/skills/incremental-correction-methodology/templates/`

---

## Propósito

Este directorio contiene templates para documentar el proceso completo de corrección incremental de issues (warnings, errores) en proyectos de documentación o código. La metodología divide la corrección en fases documentadas que permiten tracking y mejora continua.

---

## Templates Disponibles

### 1. analysis-phase.md.template

**Propósito**: Análisis inicial de todos los issues detectados en el build

**Contenido**:
- Build output completo
- Categorización de issues (tipo, severidad, archivo)
- Análisis de patterns recurrentes
- Métricas iniciales
- Issues detallados por tipo

**Tamaño**: ~75 líneas de estructura + contenido variable

**Cuándo usar**: Inmediatamente después de detectar issues en el build

---

### 2. categorization-plan.md.template

**Propósito**: Estrategia y planificación de cómo abordar los issues en lotes

**Contenido**:
- Estrategia de categorización elegida
- Criterios de priorización
- Definición de lotes (qué issues en cada lote)
- Estimación de tiempo por lote
- Plan de validación entre lotes

**Tamaño**: ~65 líneas de estructura + contenido variable

**Cuándo usar**: Después de completar analysis-phase.md

---

### 3. execution-log.md.template

**Propósito**: Log detallado de la ejecución de cada lote

**Contenido**:
- Tabla de tracking general de progreso
- Detalles de ejecución por lote (issues, archivos, comandos)
- Checkpoints de validación (build status)
- Problemas encontrados y decisiones tomadas
- Métricas de progreso
- Commits realizados

**Tamaño**: ~95 líneas de estructura + contenido variable

**Cuándo usar**: Durante toda la ejecución, actualizar después de cada lote

---

### 4. final-report.md.template

**Propósito**: Reporte final con resultados, métricas y lecciones aprendidas

**Contenido**:
- Resumen ejecutivo
- Métricas finales (antes vs después)
- Tabla comparativa de impacto
- Lecciones aprendidas
- Issues no resueltos (si aplica)
- Recomendaciones para futuro
- Conclusiones y próximos pasos

**Tamaño**: ~85 líneas de estructura + contenido variable

**Cuándo usar**: Al completar todos los lotes

---

## Workflow Completo

```
1. Detectar issues en build
   ↓
2. Crear analysis-phase.md
   - Ejecutar build completo
   - Copiar output
   - Categorizar todos los issues
   - Identificar patterns
   - Calcular métricas iniciales
   ↓
3. Crear categorization-plan.md
   - Definir estrategia (por tipo, archivo, severidad, etc.)
   - Crear lotes lógicos
   - Priorizar lotes
   - Estimar tiempo por lote
   - Establecer checkpoints de validación
   ↓
4. Crear execution-log.md
   - Iniciar con estado general
   - Por cada lote:
     * Documentar issues abordados
     * Registrar archivos modificados
     * Ejecutar comandos
     * Checkpoint de validación (build)
     * Problemas y decisiones
     * Commit
   - Actualizar métricas de progreso
   ↓
5. Crear final-report.md
   - Compilar resultados finales
   - Comparar antes vs después
   - Documentar lecciones aprendidas
   - Issues pendientes (si hay)
   - Recomendaciones futuras
   ↓
6. Proyecto completado con documentación completa
```

---

## Uso de los Templates

### Paso 1: Copiar Templates

```bash
# Copiar todos los templates a tu directorio de trabajo
cp .codex/skills/incremental-correction-methodology/templates/analysis-phase.md.template \
   .mywork/changes/[tu-proyecto]/ANALISIS_issues_[fecha].md

cp .codex/skills/incremental-correction-methodology/templates/categorization-plan.md.template \
   .mywork/changes/[tu-proyecto]/PLAN_categorizacion_[fecha].md

cp .codex/skills/incremental-correction-methodology/templates/execution-log.md.template \
   .mywork/changes/[tu-proyecto]/LOG_ejecucion_[fecha].md

# El final-report se copia al final
cp .codex/skills/incremental-correction-methodology/templates/final-report.md.template \
   .mywork/changes/[tu-proyecto]/REPORTE_final_[fecha].md
```

**Nota**: Usar nombres específicos siguiendo convención DA-009 (naming auto-documentado)

### Paso 2: Completar analysis-phase.md

1. Ejecutar build y capturar output:
   ```bash
   make clean
   make html 2>&1 | tee build-output.txt
   ```

2. Abrir ANALISIS_issues_[fecha].md

3. Completar:
   - Pegar build output completo
   - Contar issues por tipo
   - Categorizar por severidad
   - Identificar archivos más afectados
   - Identificar patterns recurrentes
   - Listar issues detallados por tipo

4. Calcular métricas:
   - Total de issues
   - Porcentajes por categoría
   - Top archivos afectados

### Paso 3: Completar categorization-plan.md

1. Revisar analysis-phase.md

2. Decidir estrategia:
   - Por tipo de issue (ej: todos los "reference not found" juntos)
   - Por archivo (ej: todos los issues de archivo X juntos)
   - Por severidad (ej: críticos primero)
   - Por complejidad (ej: fáciles primero o difíciles primero)

3. Crear lotes:
   - Agrupar issues según estrategia
   - Nombrar cada lote descriptivamente
   - Asignar prioridad a cada lote
   - Estimar tiempo por lote

4. Definir orden de ejecución basado en:
   - Prioridad
   - Dependencies entre lotes
   - Impacto en build

### Paso 4: Usar execution-log.md

1. Abrir LOG_ejecucion_[fecha].md

2. Antes de empezar:
   - Completar tabla de tracking general con todos los lotes
   - Estado inicial: todos "Pendiente"

3. Por cada lote:
   - Marcar estado "En progreso"
   - Documentar issues que se abordan
   - Listar archivos a modificar
   - Ejecutar correcciones
   - Pegar comandos ejecutados
   - **CHECKPOINT**: Ejecutar build validation
   - Pegar build output
   - Validar que se resolvieron issues del lote
   - Documentar problemas encontrados
   - Documentar decisiones tomadas
   - **COMMIT**: git commit con mensaje descriptivo
   - Marcar estado "Completado"
   - Actualizar métricas de progreso

4. Mantener actualizado durante toda la ejecución

### Paso 5: Completar final-report.md

1. Al terminar todos los lotes, copiar template

2. Compilar información de:
   - analysis-phase.md (métricas iniciales)
   - categorization-plan.md (plan vs realidad)
   - execution-log.md (qué pasó realmente)

3. Completar:
   - Resumen ejecutivo con logros principales
   - Tabla comparativa antes vs después
   - Métricas finales (reducción de issues)
   - Resumen de cada lote (éxitos y dificultades)
   - Problemas críticos encontrados
   - Lecciones aprendidas (qué funcionó, qué no)
   - Issues no resueltos (si hay)
   - Recomendaciones para futuro

---

## Mejores Prácticas

### Para analysis-phase.md

- **Ser exhaustivo**: Documentar TODOS los issues, no solo algunos
- **Categorizar bien**: Las categorías determinan los lotes futuros
- **Identificar patterns**: Patterns permiten soluciones en batch eficientes
- **No omitir**: Incluir build output completo, no resumido

### Para categorization-plan.md

- **Lotes pequeños**: Mejor muchos lotes pequeños que pocos grandes (fácil validar)
- **Priorizar impacto**: Resolver primero lo que más mejora el build
- **Ser realista**: Estimar tiempo conservadoramente (+20% buffer)
- **Validación frecuente**: Checkpoint después de cada lote, no al final

### Para execution-log.md

- **Actualizar frecuentemente**: Después de cada lote, no al final del día
- **Documentar problemas**: Especialmente los inesperados
- **Registrar decisiones**: Por qué se tomó X decisión vs Y
- **Commits frecuentes**: Un commit por lote, no todo junto al final
- **Build validation**: SIEMPRE validar build después de cada lote

### Para final-report.md

- **Ser honesto**: Documentar qué no funcionó también
- **Métricas claras**: Números concretos (X% de reducción, Yh invertidas)
- **Lecciones útiles**: Qué aplicar en próxima corrección incremental
- **Recomendaciones accionables**: Acciones específicas, no genéricas

---

## Beneficios de la Metodología

### Con Templates

- **Consistencia**: Todos los proyectos siguen mismo proceso documentado
- **Tracking**: Fácil ver progreso y estimar tiempo restante
- **Aprendizaje**: Lecciones aprendidas se documentan y replican
- **Calidad**: Checkpoints frecuentes previenen regresiones
- **Rollback**: Fácil revertir un lote si algo falla

### Sin Templates

- Documentación inconsistente o inexistente
- Difícil trackear progreso
- Lecciones se pierden
- Mayor riesgo de introducir nuevos bugs
- Difícil justificar tiempo invertido

---

## Ejemplo de Proyecto Real

### Escenario

Proyecto Sphinx con 230 warnings detectados en build.

### Aplicación de Templates

**1. ANALISIS_230_warnings_sphinx.md**:
- Build output completo capturado
- Categorizado: 120 "reference not found", 80 "duplicate label", 30 "toctree"
- 5 patterns identificados
- Top 10 archivos más afectados documentados

**2. PLAN_categorizacion_5_lotes.md**:
- Estrategia: Por tipo de issue
- 5 lotes definidos:
  * Lote 1: Referencias rotas críticas (50 issues, 2h)
  * Lote 2: Duplicate labels (80 issues, 3h)
  * Lote 3: Referencias rotas no críticas (70 issues, 2.5h)
  * Lote 4: Toctree issues (30 issues, 1.5h)
  * Lote 5: Validación final (limpieza, 1h)
- Total estimado: 10h

**3. LOG_ejecucion_230_warnings.md**:
- Lote 1: 50 issues resueltos, build pasó, commit realizado (2.2h real)
- Lote 2: 80 issues resueltos, 3 problemas encontrados, soluciones documentadas (3.5h real)
- Lote 3: 70 issues resueltos (2.8h real)
- Lote 4: 30 issues resueltos (1.3h real)
- Lote 5: Validación final, 2 issues menores encontrados y corregidos (1.2h real)
- Total real: 11h (vs 10h estimado, +10% variación aceptable)

**4. REPORTE_final_230_warnings.md**:
- Reducción: 230 → 2 warnings (99.1%)
- Lecciones: Pattern matching acelera corrección 3x
- Recomendación: Implementar pre-commit hook para prevenir duplicate labels
- Próximos pasos: Resolver 2 warnings restantes (requieren research adicional)

---

## Integración con Otros Skills

**Requiere**:
- `project-context`: Para entender estructura del proyecto
- `commit-helper`: Para commits consistentes después de cada lote

**Complementa a**:
- `validation-suite`: Checkpoints de validación usan validation-suite
- `work-logger`: Final report puede referenciar work-logs específicos

**Es usado por**:
- Proyectos de corrección de warnings
- Proyectos de refactoring incremental
- Proyectos de mejora de calidad

---

## FAQ

**Q: ¿Debo usar los 4 templates siempre?**

A: Para proyectos con >50 issues, SÍ. Para <50 issues, analysis + execution-log puede ser suficiente.

**Q: ¿Qué hago si un lote falla la validación?**

A: Documentar en execution-log, revertir cambios del lote (git reset), ajustar estrategia, re-intentar.

**Q: ¿Cuál es el tamaño ideal de lote?**

A: 15-30 issues por lote. Menos de 15 es demasiado granular, más de 30 dificulta validación.

**Q: ¿Debo seguir orden estricto de templates?**

A: SÍ. El orden es: analysis → categorization → execution → final-report. Cada uno depende del anterior.

**Q: ¿Qué hago con issues que no se pueden resolver?**

A: Documentar en execution-log por qué no se pueden resolver, incluir en final-report sección "Issues No Resueltos" con plan futuro.

---

## Soporte

Para dudas sobre cómo usar los templates:
1. Ver este README
2. Consultar `.codex/skills/incremental-correction-methodology/SKILL.md`
3. Revisar ejemplos en `.mywork/changes/` de proyectos anteriores

---

Última actualización: 2026-02-01
