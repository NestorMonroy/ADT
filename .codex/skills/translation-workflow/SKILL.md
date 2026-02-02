---
name: translation-workflow
description: "Workflow completo de traduccion siguiendo metodologia ADT. Usar cuando el usuario necesite traducir contenido, aplicar modos de traduccion, o ejecutar proceso de transformacion documental."
version: 1.4.0
created: 2026-01-29
updated: 2026-02-01
---

# Translation Workflow - Metodologia ADT

## Cuando usar

- Usuario pide traducir documento
- Transformar contenido a RST
- Aplicar modo de traduccion especifico
- Generar metadata de traduccion
- Integrar contenido en estructura Sphinx

---

## Decision Framework: ¿Qué Modo de Traducción Usar?

**Usa este framework para decidir el modo correcto**:

1. **¿El documento es altamente técnico con estructura específica?**
   → `alta_fidelidad` (preserva estructura exacta)

2. **¿El contenido tiene elementos visuales importantes (tabs, admonitions)?**
   → `marcado_visual` (añade marcas de estructura visual)

3. **¿Necesitas mejorar/explicar conceptos para audiencia local?**
   → `enriquecimiento` (añade contexto y explicaciones)

4. **¿Es documentación de referencia (API, comandos)?**
   → `alta_fidelidad` (exactitud crítica)

5. **¿Es tutorial o guía práctica?**
   → `enriquecimiento` (beneficia de contexto adicional)

6. **¿Es arc42 o framework con estructura fija?**
   → `alta_fidelidad` + framework específico

7. **¿No estás seguro?**
   → Empieza con `alta_fidelidad` (más seguro)

**Regla de oro**: **Si dudas → alta_fidelidad**

---

## Trigger Patterns

### Señales Explícitas
- Usuario dice: "traduce este documento"
- Usuario dice: "convierte a RST"
- Usuario proporciona URL o archivo para traducir
- Usuario dice: "aplica modo [X]"
- Usuario menciona framework (Diataxis, arc42)

### Señales Implícitas
- Usuario habla de documentación en otro idioma
- Usuario menciona sección de arc42 específica
- Usuario quiere agregar contenido a Sphinx
- Contexto indica transformación documental necesaria

### Trigger Words
- "traducir", "translate", "convertir"
- "RST", "reStructuredText", "Sphinx"
- "arc42", "Diataxis"
- "modo", "alta fidelidad", "enriquecimiento"
- "sección", "documento", "contenido"

**Anti-triggers** (NO usar este workflow):
- Solo pregunta sobre traducción (no ejecutar todavía)
- Usuario ya tiene RST (solo validar formato)
- Cambios menores de texto (editar directamente)
- Traducción de 1-2 párrafos (hacer directamente)

---

## Self-Check Before Translation

**OBLIGATORIO antes de empezar traducción**:

### Pre-Translation Checks
- [ ] ¿Leí project-context skill?
- [ ] ¿Tengo el documento fuente disponible?
- [ ] ¿Confirmé ubicación destino en Sphinx?
- [ ] ¿Identifiqué framework correcto? (Diataxis/arc42)
- [ ] ¿Determiné modo de traducción apropiado?
- [ ] ¿Verifiqué prerequisitos?

**Si NO → STOP - Preparar antes de traducir**

### During Translation Checks
- [ ] ¿Estoy usando el script correcto?
- [ ] ¿Los parámetros del script son correctos?
- [ ] ¿Estoy generando metadata apropiada?
- [ ] ¿El output tiene formato RST válido?
- [ ] ¿Estoy preservando estructura según modo elegido?

**Si NO → PAUSE - Verificar configuración y corregir**

### Post-Translation Checks
- [ ] ¿El build de Sphinx pasa sin errores?
- [ ] ¿La metadata está completa y correcta?
- [ ] ¿El contenido está integrado en toctree?
- [ ] ¿Los enlaces internos funcionan?
- [ ] ¿Hice commit con mensaje descriptivo?
- [ ] ¿Creé work log si fue significativo?

**Si NO → COMPLETAR antes de considerar terminado**

---

## Prerequisitos

1. Leer project-context skill
2. Tener documento fuente disponible
3. Confirmar ubicacion destino en Sphinx
4. Verificar framework (Diataxis/arc42)

---

## 🔄 FLUJO END-TO-END: Usuario → Contenido Publicado

### Visión General

```
USUARIO SOLICITA → ANÁLISIS → TRADUCCIÓN → VALIDACIÓN → INTEGRACIÓN → PUBLICACIÓN
     (Fase 0)      (Fase 1)    (Fase 2-3)    (Fase 4)     (Fase 5)      (Build)
```

### Flujo Completo Paso a Paso

```
┌─────────────────────────────────────────────────────────────────────┐
│ FASE 0: RECEPCIÓN Y ANÁLISIS DE SOLICITUD                          │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Usuario dice "traduce X" o provee URL/archivo               │
│                                                                     │
│ 1. IDENTIFICAR solicitud:                                          │
│    - ¿Qué tipo de contenido? (arc42, tutorial, referencia)        │
│    - ¿Fuente disponible? (URL, archivo, clonar)                   │
│    - ¿Framework? (arc42, Diataxis, general)                       │
│                                                                     │
│ 2. CONFIRMAR con usuario:                                          │
│    - Destino en biblioteca (ruta específica)                       │
│    - Modo de traducción preferido                                  │
│    - Cualquier requisito especial                                  │
│                                                                     │
│ 3. PREPARAR entorno:                                               │
│    - Verificar scripts disponibles                                 │
│    - Confirmar estructura destino existe                           │
│    - Leer skill translation-workflow (este archivo)                │
│                                                                     │
│ OUTPUT: Plan de traducción claro → Ir a FASE 1                    │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ FASE 1: ANÁLISIS DE DOCUMENTO FUENTE                               │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Documento fuente identificado                                │
│                                                                     │
│ 1. OBTENER original:                                               │
│    Arc42:                                                          │
│      cp pipeline_docs_work/.../originales/por_seccion/XX/original/ │
│    Web:                                                            │
│      wget <URL> -O /tmp/original.html                             │
│    Archivo:                                                        │
│      cp <ruta_usuario> /tmp/original.md                           │
│                                                                     │
│ 2. ANALIZAR estructura:                                            │
│    - Identificar secciones principales                             │
│    - Detectar elementos especiales (code, tables, images)         │
│    - Verificar idioma fuente                                       │
│    - Determinar complejidad                                        │
│                                                                     │
│ 3. DETERMINAR modo:                                                │
│    Técnico + estructura fija → alta_fidelidad                     │
│    Con tabs/admonitions → marcado_visual                          │
│    Tutorial/guía → enriquecimiento                                │
│                                                                     │
│ 4. VALIDAR coherencia:                                             │
│    - ¿Destino correcto en biblioteca?                             │
│    - ¿Framework compatible?                                        │
│    - ¿Terminología consistente?                                    │
│                                                                     │
│ OUTPUT: Modo seleccionado + ruta destino → Ir a FASE 2            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ FASE 2: CONFIGURACIÓN DE TRANSFORMACIÓN                            │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Modo + Framework + Documento original                       │
│                                                                     │
│ 1. SELECCIONAR script:                                             │
│    Arc42 → scripts/traduccion/arc42_scraper_python.py            │
│    Web   → scripts/traduccion/translate_web_content.sh           │
│    Gral  → scripts/traduccion/adt_translator.py                  │
│                                                                     │
│ 2. CONFIGURAR parámetros:                                          │
│    --section XX (si arc42)                                        │
│    --mode <alta_fidelidad|marcado_visual|enriquecimiento>        │
│    --framework <arc42|diataxis|general>                          │
│    --output <ruta_temporal>                                       │
│                                                                     │
│ 3. PREPARAR recursos:                                              │
│    - Cargar glosario terminológico                                │
│    - Configurar prompts de traducción                             │
│    - Definir reglas de transformación                             │
│                                                                     │
│ OUTPUT: Script configurado → Ir a FASE 3                          │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ FASE 3: EJECUCIÓN DE TRANSFORMACIÓN                                │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Script configurado + Documento original                     │
│                                                                     │
│ 1. EJECUTAR traducción:                                            │
│    Arc42 ejemplo:                                                  │
│      python scripts/traduccion/arc42_scraper_python.py \         │
│        --section 02 \                                             │
│        --mode alta_fidelidad \                                    │
│        --output pipeline_docs_work/.../trabajo/borradores/02/    │
│                                                                     │
│ 2. GENERAR archivos:                                               │
│    Por tipo de contenido:                                          │
│      - secciones/seccion_XX.rst (contenido principal)             │
│      - tips/tip_XX_*.rst (consejos)                               │
│      - ejemplos/ejemplo_XX_*.rst (casos)                          │
│      - diagramas/ (visualizaciones)                                │
│      - figuras/ (imágenes)                                         │
│                                                                     │
│ 3. GENERAR metadata:                                               │
│    Crear archivo YAML:                                             │
│      seccion: XX                                                   │
│      titulo: [Título original]                                     │
│      modo_traduccion: alta_fidelidad                              │
│      framework: arc42                                              │
│      fecha: 2026-02-01                                            │
│      archivos: [lista de .rst generados]                          │
│                                                                     │
│ 4. GENERAR reporte:                                                │
│    REPORTE_seccion_XX.rst con:                                     │
│      - Análisis del original                                       │
│      - Decisiones tomadas                                          │
│      - Problemas encontrados                                       │
│      - Próximos pasos                                              │
│                                                                     │
│ OUTPUT: Archivos .rst en trabajo/borradores/ → Ir a FASE 4        │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ FASE 4: VALIDACIÓN DE SALIDA                                       │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Archivos .rst en trabajo/borradores/                        │
│                                                                     │
│ 1. VALIDAR sintaxis RST:                                           │
│    - Copiar temporalmente a source/                               │
│    - Ejecutar: make clean && make html                            │
│    - Verificar 0 ERRORES                                           │
│    - Revisar WARNINGS (aceptables < 5)                            │
│                                                                     │
│ 2. VERIFICAR estructura:                                            │
│    - Archivos en subdirectorios correctos:                         │
│      ✓ secciones/ tiene contenido principal                       │
│      ✓ tips/ tiene consejos (si aplica)                           │
│      ✓ ejemplos/ tiene casos (si aplica)                          │
│    - Naming conventions:                                           │
│      ✓ seccion_XX_nombre.rst                                      │
│      ✓ tip_XX_nombre.rst                                          │
│      ✓ ejemplo_XX_nombre.rst                                      │
│                                                                     │
│ 3. VALIDAR calidad:                                                │
│    - Coherencia terminológica (glosario)                          │
│    - Completitud del contenido                                     │
│    - Enlaces internos funcionan                                    │
│    - Imágenes referenciadas existen                               │
│                                                                     │
│ 4. REVISAR metadata:                                               │
│    - Archivo .yaml completo                                        │
│    - Reporte generado y claro                                      │
│    - Decisiones documentadas                                       │
│                                                                     │
│ 5. SI TODO OK:                                                      │
│      mv trabajo/borradores/XX/* trabajo/validaciones/XX/         │
│    SI HAY ERRORES:                                                 │
│      Corregir y repetir FASE 4                                     │
│                                                                     │
│ OUTPUT: Archivos validados en trabajo/validaciones/ → Ir a FASE 5 │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ FASE 5: INTEGRACIÓN EN PROYECTO                                    │
├─────────────────────────────────────────────────────────────────────┤
│ INPUT: Archivos validados en trabajo/validaciones/                 │
│                                                                     │
│ 1. COPIAR a destino público:                                       │
│    FROM: pipeline_docs_work/.../trabajo/validaciones/02/         │
│    TO:   source/biblioteca/.../arc42_documentation/02_*/         │
│                                                                     │
│    Estructura destino:                                             │
│      02_constraints/                                               │
│        ├── index.rst (actualizar)                                 │
│        ├── secciones/ (copiar aquí)                               │
│        ├── tips/ (copiar aquí)                                     │
│        ├── ejemplos/ (copiar aquí)                                 │
│        ├── diagramas/ (copiar aquí)                                │
│        └── figuras/ (copiar aquí)                                  │
│                                                                     │
│ 2. ACTUALIZAR index.rst:                                           │
│    .. toctree::                                                    │
│       :maxdepth: 2                                                 │
│       :glob:                                                       │
│                                                                     │
│       secciones/*                                                  │
│       tips/*                                                       │
│       ejemplos/*                                                   │
│                                                                     │
│ 3. GENERAR cross-references (si necesario):                        │
│    .. _sec-02-constraints:                                        │
│                                                                     │
│    Restricciones de Arquitectura                                   │
│    ==============================                                   │
│                                                                     │
│ 4. ACTUALIZAR glosario (si aplica):                                │
│    Agregar términos nuevos a:                                      │
│    source/biblioteca/.../12_glossary/secciones/glosario.rst      │
│                                                                     │
│ 5. BUILD final:                                                     │
│    cd /tmp/ADT                                                     │
│    make clean                                                      │
│    make html                                                       │
│    → Verificar 0 ERRORES                                           │
│                                                                     │
│ 6. DOCUMENTAR:                                                      │
│    - Crear work-log con work-logger skill                         │
│    - Actualizar PROGRESO en reportes/                             │
│                                                                     │
│ 7. COMMIT:                                                          │
│    git add source/biblioteca/.../02_*                             │
│    git commit -m "docs(arc42): traducir seccion 02 constraints"  │
│                                                                     │
│ 8. ARCHIVAR trabajo:                                               │
│    mv metadata/seccion_02_metadata.yaml metadata/FINAL/          │
│    mv reportes/REPORTE_seccion_02.rst reportes/FINAL/            │
│    # trabajo/ queda en .gitignore                                 │
│                                                                     │
│ OUTPUT: Contenido integrado, build OK, commit creado ✅            │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ RESULTADO FINAL                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ ✅ Contenido traducido en: source/biblioteca/.../XX_nombre/       │
│ ✅ Build Sphinx exitoso (0 errores)                                │
│ ✅ Metadata archivada en: metadata/FINAL/                          │
│ ✅ Reporte disponible en: reportes/FINAL/                          │
│ ✅ Commit git creado con mensaje descriptivo                       │
│ ✅ Usuario puede ver contenido en documentación HTML               │
│                                                                     │
│ PUBLICACIÓN:                                                        │
│   make html → _build/html/biblioteca/.../XX_nombre/index.html     │
└─────────────────────────────────────────────────────────────────────┘
```

### Decisiones Clave en Cada Fase

**FASE 0 (Recepción)**:
- ¿Es solicitud válida? → Verificar que tenemos fuente
- ¿Framework correcto? → arc42 vs Diataxis vs general
- ¿Usuario confirmó destino? → Evitar reorganizar después

**FASE 1 (Análisis)**:
- ¿Qué modo usar? → Decision Framework (ver arriba)
- ¿Estructura compatible? → Validar vs estructura destino

**FASE 2-3 (Transformación)**:
- ¿Script correcto? → arc42_scraper vs adt_translator
- ¿Output temporal primero? → SÍ, siempre a trabajo/borradores/

**FASE 4 (Validación)**:
- ¿Build pasa? → Si no, corregir antes de continuar
- ¿Metadata completa? → Esencial para trazabilidad

**FASE 5 (Integración)**:
- ¿Destino correcto? → Verificar estructura XX_nombre/
- ¿Commit descriptivo? → Conventional commits

---

## Fases del Workflow

### FASE 1: Analisis de Documento Fuente

PASOS:

1. Identificar tipo (Tutorial, How-to, Reference, Explanation, arc42)
2. Analizar estructura
   ```bash
   python scripts/analizar_seccion.py <ruta>
   ```
3. Determinar modo (alta_fidelidad, marcado_visual, enriquecimiento)
4. Validar coherencia con destino

### FASE 2: Configuracion de Transformacion

PASOS:

1. Seleccionar script:
   - arc42: `scripts/traduccion/arc42_scraper_python.py`
   - Web: `scripts/traduccion/translate_web_content.sh`
   - General: `scripts/traduccion/adt_translator.py`

2. Configurar parametros (modo, framework, categoria)

3. Preparar glosario terminologico
   Ver: `pipeline_docs/procedimientos/10_apendices/glosario_adt.rst`

### FASE 3: Ejecucion de Transformacion

EJEMPLO arc42:
```bash
python scripts/traduccion/arc42_scraper_python.py \
  --section 02 \
  --mode alta_fidelidad \
  --output source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/02_constraints/
```

**NOTA IMPORTANTE**: Estructura arc42 reorganizada (v1.0.0):
- Contenido PUBLIC

O → source/biblioteca/.../arc42_documentation/XX_nombre/
  - secciones/ (contenido principal)
  - tips/ (consejos practicos)
  - ejemplos/ (casos practicos)
  - diagramas/ (visualizaciones)
  - figuras/ (imagenes de apoyo)
- Contenido PRIVADO → pipeline_docs_work/.../arc42_documentation/
  - originales/ (archivos fuente)
  - metadata/ (clasificacion)
  - reportes/ (reportes de progreso)
  - trabajo/ (borradores, validaciones)

MODOS:
- Alta Fidelidad: Preservar estructura exacta
- Marcado Visual: Agregar admoniciones (note, warning, tip)
- Enriquecimiento: Expandir conceptos

GENERAR METADATA:
```rst
.. meta::
   :description: [Descripcion]
   :keywords: [palabras clave]
   :author: [Autor original]
   :source: [URL]

:Documento Original: [Referencia]
:Modo de Traduccion: [modo]
:Framework: [framework]
:Categoria: [categoria]
```

### FASE 4: Validacion de Salida

PASOS:

1. Validar sintaxis RST: `make html`
2. Verificar estructura: `bash scripts/validar_estructura.sh`
3. Validar calidad (coherencia terminologica, completitud)
4. Revisar metadata

### FASE 5: Integracion en Proyecto

PASOS:

1. Actualizar toctree del capitulo
   ```rst
   .. toctree::
      :maxdepth: 2
      
      nuevo_contenido
   ```

2. Generar cross-references
   ```rst
   .. _label-nuevo:
   
   Seccion
   -------
   ```

3. Actualizar glosario si aplica

4. Documentar con work-logger skill

5. Commit con commit-helper skill

## Matrices de Decision

Ver: `source/04_reglas_operativas/matrices_decision/`

MD_001: Seleccion de modo
MD_002: Cuando enriquecer
MD_003: Nivel segmentacion
MD_004: Traducir vs conservar

## Casos Especiales

CODIGO (nunca se traduce):
```rst
.. code-block:: python

   # Comentarios SI se traducen
   def funcion_original():  # Nombres conservar
       """Docstring SI se traduce."""
       pass
```

DIAGRAMAS:
```rst
.. figure:: /_static/diagrama.png
   :alt: Texto alternativo traducido
   
   Pie de figura traducido
```

## Salida Esperada

```
RESUMEN DE TRADUCCION

DOCUMENTO: [Nombre]
UBICACION: source/[ruta]
MODO: [modo]
FRAMEWORK: [framework]

TRANSFORMACIONES APLICADAS:
- [Transformacion 1]

METADATA: Generada
VALIDACION: Exitosa
BUILD: Sin errores

ARCHIVOS MODIFICADOS:
- source/.../nuevo.rst (NUEVO)
- source/.../index.rst (toctree)
```

## Referencias

**NOTA**: Reorganización v1.0.0 - estructura actualizada
- pipeline_docs/procedimientos/02_procedimientos/workflow_general.rst
- pipeline_docs/procedimientos/04_reglas_operativas/matrices_decision/
- scripts/traduccion/
- pipeline_docs/procedimientos/03_estandares/calidad/
- source/biblioteca/ → Contenido público traducido

## Notas

- Consultar project-context primero
- Validar build siempre
- Documentar decisiones
- Mantener coherencia terminologica
- Usar scripts existentes

---

## Optimización para Documentos Grandes

Para traducción de documentos grandes (arc42 completo, documentación técnica extensa), consultar:

**`.codex/skills/anthropic-best-practices/long-context-tips.md`**

### Cuándo Consultar

**Situaciones donde long-context-tips.md es útil**:
- Traducir arc42 completo (13 secciones, 25,000 palabras)
- Trabajar con documentación técnica >5,000 palabras
- Necesitas preservar cross-references entre múltiples secciones
- Validar consistencia a través de documento largo

### Técnicas Relevantes de long-context-tips.md

**Estructura Óptima para Traducción**:
```xml
<documento-original lang="en">
  <section id="01-introduction">
    [contenido completo section 1]
  </section>
  <section id="02-constraints">
    [contenido completo section 2]
  </section>
  ...
</documento-original>

Instrucciones:
Traducir usando modo Alta Fidelidad.
Procesar sección por sección con checkpoints.
```

**Principio clave**: Data at top, query at end → 30% mejora en accuracy.

**Ground Responses in Quotes**:
Para validar calidad de traducción, pedir que Claude cite original y traducción lado a lado:
```
Para cada párrafo:
Original:
> [texto original]

Traducción:
> [texto traducido]

Evaluación: [accuracy, terminología, mejoras]
```

**Checkpoints Incrementales**:
```
Workflow de traducción arc42 completo:
1. Traducir section 01
2. CHECKPOINT - validar antes de continuar
3. Traducir section 02
4. CHECKPOINT - validar
...
```

### Caso de Uso Específico

Ver long-context-tips.md caso de uso **"Traducción de arc42 Completo"** para:
- Estructura XML completa recomendada
- Metadata del proyecto
- Workflow de checkpoints por sección
- Preservación de labels y referencias
- Integración con glossary

### Beneficio

Aplicar técnicas de long-context-tips.md en traducciones:
- 30% mejora en accuracy de traducción
- Mejor preservación de estructura y referencias
- Validación incremental previene re-trabajo
- Consistencia terminológica a través de todo el documento

---

## Changelog

### v1.4.0 - 2026-02-01 - Integración con anthropic-best-practices

**Agregado**:
- Sección "Optimización para Documentos Grandes"
- Referencia a anthropic-best-practices/long-context-tips.md
- Técnicas relevantes para traducción de docs grandes
- Caso de uso específico: Traducción de arc42 completo

**Contenido de nueva sección**:
- Cuándo consultar long-context-tips.md
- Técnicas relevantes (estructura XML, data at top, ground en quotes, checkpoints)
- Beneficio cuantificable: 30% mejora en accuracy

**Beneficio**:
- Usuarios traducen documentos grandes más efectivamente
- Estructura óptima para arc42 completo (25,000 palabras)
- Validación incremental previene re-trabajo
- Mejor preservación de referencias y estructura

### v1.3.0 - 2026-02-01 - Flujo End-to-End Completo

**Nueva sección**: Flujo End-to-End (Usuario → Publicación)

✅ **FASE 0: Recepción y Análisis de Solicitud** (NUEVO):
- Cómo identificar solicitud del usuario
- Confirmar destino y requisitos
- Preparar entorno de trabajo
- INPUT/OUTPUT claros

✅ **Diagrama de flujo ASCII completo**:
- 6 fases visualizadas (0-5 + Resultado)
- Cada fase con INPUT → PASOS → OUTPUT
- Decisiones clave en cada fase
- Rutas de archivos específicas post-reorganización

✅ **Mejoras en fases existentes**:
- FASE 1: Detalles de cómo obtener originales (arc42/web/archivo)
- FASE 3: Estructura de archivos generados por tipo
- FASE 4: Criterios de validación específicos (0 errores, <5 warnings)
- FASE 5: Proceso completo de integración (8 pasos)

✅ **Rutas actualizadas a estructura v1.0.0**:
- trabajo/borradores/ → trabajo/validaciones/ → source/biblioteca/
- Metadata y reportes en directorios específicos
- .gitignore de trabajo/ documentado

✅ **Decisiones documentadas**:
- Tabla de decisiones clave por fase
- Cuándo usar cada script
- Criterios de calidad
- Conventional commits

**Líneas agregadas**: ~270 líneas
**Beneficio principal**:
- Flujo completo desde solicitud de usuario hasta publicación
- Claude puede seguir paso a paso sin ambigüedad
- Usuario entiende proceso completo end-to-end
- Trazabilidad total del proceso

### v1.2.0 - 2026-02-01 - Reorganización Estructura ADT

**Cambios por reorganización biblioteca v1.0.0**:

✅ **Rutas actualizadas**:
- arc42 ahora en: `source/biblioteca/.../arc42_documentation/XX_nombre/`
- Estructura por tipo: secciones/, tips/, ejemplos/, diagramas/, figuras/
- Eliminada carpeta sections/ y traduccion/

✅ **Separación público/privado**:
- Contenido PÚBLICO → source/biblioteca/
- Contenido PRIVADO → pipeline_docs_work/
  - originales/ (archivos fuente)
  - metadata/ (clasificación)
  - reportes/ (progreso)
  - trabajo/ (borradores)

✅ **Referencias actualizadas**:
- Procedimientos → pipeline_docs/procedimientos/
- Glosario → pipeline_docs/procedimientos/10_apendices/
- Matrices decisión → pipeline_docs/procedimientos/04_reglas_operativas/

**Breaking Changes**:
- Rutas de output para scripts deben actualizarse
- NO usar sections/traduccion/ → usar XX_nombre/secciones|tips|ejemplos/

### v1.1.0 - 2026-02-01 - FASE 2

**Mejoras de usabilidad y decision-making**:

✅ **Decision Framework** - ¿Qué Modo de Traducción Usar?
- 7 preguntas para elegir modo correcto
- Mapeo claro: técnico → alta_fidelidad, tutorial → enriquecimiento
- Regla de oro: "Si dudas → alta_fidelidad"

✅ **Trigger Patterns** - Cuándo usar este workflow
- Señales explícitas (usuario dice "traduce")
- Señales implícitas (mención de frameworks, documentación)
- Trigger words específicos
- Anti-triggers para evitar ejecución incorrecta

✅ **Self-Check Mechanisms** - 3 niveles de checks
- Pre-Translation (requisitos, documento fuente, destino)
- During Translation (script correcto, parámetros, formato RST)
- Post-Translation (build Sphinx, metadata, integración)

**Líneas agregadas**: ~95 líneas

**Beneficio principal**:
- Usuarios eligen modo de traducción correcto desde inicio
- Workflow más guiado y predecible
- Previene errores comunes de configuración y omisiones

### v1.0.0 - 2026-01-30
- Versión inicial
- Workflow completo de traducción
- Modos: alta_fidelidad, marcado_visual, enriquecimiento
- Integración con scripts de traducción
