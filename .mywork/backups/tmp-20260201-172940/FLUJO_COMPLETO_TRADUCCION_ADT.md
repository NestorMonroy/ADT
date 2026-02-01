# Flujo Completo de Traducción ADT

**Versión**: 1.0.0  
**Fecha**: 2026-02-01  
**Proyecto**: ADT Documentation  
**Skills**: translation-workflow v1.3.0 + sphinx-expert v1.9.0

---

## 📋 Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Diagrama de Flujo Completo](#diagrama-de-flujo-completo)
3. [Fase 0: Recepción](#fase-0-recepción-y-análisis-de-solicitud)
4. [Fase 1: Análisis](#fase-1-análisis-de-documento-fuente)
5. [Fase 2: Configuración](#fase-2-configuración-de-transformación)
6. [Fase 3: Ejecución](#fase-3-ejecución-de-transformación)
7. [Fase 4: Validación](#fase-4-validación-de-salida)
8. [Fase 5: Integración](#fase-5-integración-en-proyecto)
9. [Resultado Final](#resultado-final)
10. [Casos de Uso](#casos-de-uso)
11. [Troubleshooting](#troubleshooting)

---

## 🎯 Visión General

### ¿Qué es este flujo?

Proceso **end-to-end** para traducir contenido técnico desde su fuente original (web, archivo, repositorio) hasta su publicación en la documentación HTML generada por Sphinx.

### Alcance

- **Entrada**: Usuario solicita traducción de contenido
- **Salida**: Contenido traducido, validado, integrado y publicado
- **Tiempo estimado**: 1-3 horas dependiendo de complejidad

### Frameworks Soportados

1. **Arc42**: Arquitectura de software (13 secciones)
2. **Diataxis**: Documentación técnica (Tutorial, How-to, Reference, Explanation)
3. **General**: Cualquier contenido técnico

---

## 🔄 Diagrama de Flujo Completo

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    FLUJO COMPLETO DE TRADUCCIÓN                          │
│                    Usuario → Contenido Publicado                         │
└──────────────────────────────────────────────────────────────────────────┘

       USUARIO SOLICITA TRADUCCIÓN
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ FASE 0: RECEPCIÓN Y ANÁLISIS DE SOLICITUD                            ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ INPUT: "Traduce la sección 02 de arc42" / URL / archivo              ┃
┃                                                                        ┃
┃ Acciones:                                                              ┃
┃ 1. ¿Qué tipo? → arc42 / Diataxis / general                           ┃
┃ 2. ¿Fuente? → URL / archivo / ya clonado                             ┃
┃ 3. ¿Destino? → Confirmar ruta en biblioteca                          ┃
┃ 4. ¿Modo? → alta_fidelidad / marcado_visual / enriquecimiento        ┃
┃                                                                        ┃
┃ OUTPUT: Plan de traducción → FASE 1                                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ FASE 1: ANÁLISIS DE DOCUMENTO FUENTE                                 ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ INPUT: Documento fuente identificado                                  ┃
┃                                                                        ┃
┃ Acciones:                                                              ┃
┃ 1. OBTENER original:                                                  ┃
┃    • Arc42: pipeline_docs_work/.../originales/por_seccion/XX/        ┃
┃    • Web: wget <URL> -O /tmp/original.html                           ┃
┃    • Archivo: cp <ruta> /tmp/original.md                             ┃
┃                                                                        ┃
┃ 2. ANALIZAR estructura:                                               ┃
┃    • Identificar secciones principales                                ┃
┃    • Detectar code blocks, tablas, imágenes                          ┃
┃    • Verificar idioma fuente                                          ┃
┃    • Determinar complejidad                                           ┃
┃                                                                        ┃
┃ 3. DETERMINAR modo:                                                   ┃
┃    → Técnico + estructura fija = alta_fidelidad                      ┃
┃    → Con tabs/admonitions = marcado_visual                           ┃
┃    → Tutorial/guía = enriquecimiento                                 ┃
┃                                                                        ┃
┃ OUTPUT: Modo seleccionado + ruta destino → FASE 2                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ FASE 2: CONFIGURACIÓN DE TRANSFORMACIÓN                              ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ INPUT: Modo + Framework + Documento original                          ┃
┃                                                                        ┃
┃ Acciones:                                                              ┃
┃ 1. SELECCIONAR script:                                                ┃
┃    • Arc42 → scripts/traduccion/arc42_scraper_python.py             ┃
┃    • Web → scripts/traduccion/translate_web_content.sh               ┃
┃    • General → scripts/traduccion/adt_translator.py                  ┃
┃                                                                        ┃
┃ 2. CONFIGURAR parámetros:                                             ┃
┃    --section XX (si arc42)                                           ┃
┃    --mode alta_fidelidad|marcado_visual|enriquecimiento             ┃
┃    --framework arc42|diataxis|general                                ┃
┃    --output pipeline_docs_work/.../trabajo/borradores/              ┃
┃                                                                        ┃
┃ 3. PREPARAR recursos:                                                 ┃
┃    • Glosario terminológico                                           ┃
┃    • Prompts de traducción                                            ┃
┃    • Reglas de transformación                                         ┃
┃                                                                        ┃
┃ OUTPUT: Script configurado → FASE 3                                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ FASE 3: EJECUCIÓN DE TRANSFORMACIÓN                                  ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ INPUT: Script configurado + Documento original                        ┃
┃                                                                        ┃
┃ Acciones:                                                              ┃
┃ 1. EJECUTAR traducción:                                               ┃
┃    $ python scripts/traduccion/arc42_scraper_python.py \             ┃
┃        --section 02 \                                                 ┃
┃        --mode alta_fidelidad \                                        ┃
┃        --output pipeline_docs_work/.../trabajo/borradores/02/        ┃
┃                                                                        ┃
┃ 2. GENERAR archivos por tipo:                                         ┃
┃    trabajo/borradores/02_constraints/                                 ┃
┃      ├── seccion_02_restricciones.rst                                ┃
┃      ├── tip_02_decisiones.rst                                        ┃
┃      └── ejemplo_02_caso_real.rst                                     ┃
┃                                                                        ┃
┃ 3. GENERAR metadata:                                                  ┃
┃    metadata/seccion_02_metadata.yaml:                                 ┃
┃      seccion: 02                                                      ┃
┃      titulo: Architecture Constraints                                 ┃
┃      modo_traduccion: alta_fidelidad                                 ┃
┃      framework: arc42                                                 ┃
┃      archivos: [seccion_02_*.rst, tip_02_*.rst, ...]                 ┃
┃                                                                        ┃
┃ 4. GENERAR reporte:                                                   ┃
┃    reportes/REPORTE_seccion_02.rst                                    ┃
┃                                                                        ┃
┃ OUTPUT: Archivos .rst en trabajo/borradores/ → FASE 4                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ FASE 4: VALIDACIÓN DE SALIDA                                         ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ INPUT: Archivos .rst en trabajo/borradores/                           ┃
┃ SKILL: sphinx-expert v1.9.0                                           ┃
┃                                                                        ┃
┃ Acciones:                                                              ┃
┃ 1. COPIAR temporalmente a source/:                                    ┃
┃    $ cp -r pipeline_docs_work/.../trabajo/borradores/02/* \          ┃
┃            source/biblioteca/.../02_constraints/                      ┃
┃                                                                        ┃
┃ 2. BUILD limpio (OBLIGATORIO):                                        ┃
┃    $ cd /tmp/ADT                                                      ┃
┃    $ make clean                                                       ┃
┃    $ make html 2>&1 | tee /tmp/build_validation.log                  ┃
┃                                                                        ┃
┃ 3. VERIFICAR errores:                                                 ┃
┃    $ grep "ERROR:" /tmp/build_validation.log                         ┃
┃    → DEBE ser 0 errores ✅                                            ┃
┃                                                                        ┃
┃ 4. VERIFICAR warnings:                                                ┃
┃    $ grep "WARNING:" /tmp/build_validation.log | wc -l              ┃
┃    → Debe ser < 5 warnings ⚠️                                         ┃
┃                                                                        ┃
┃ 5. VALIDAR calidad:                                                   ┃
┃    ✓ Coherencia terminológica                                         ┃
┃    ✓ Enlaces internos funcionan                                       ┃
┃    ✓ Imágenes referenciadas existen                                   ┃
┃    ✓ Metadata completa                                                ┃
┃                                                                        ┃
┃ 6. DECISIÓN:                                                          ┃
┃    SI build OK (0 errores):                                           ┃
┃      $ mv trabajo/borradores/02 trabajo/validaciones/02              ┃
┃      → FASE 5 ✅                                                       ┃
┃    SI build FALLA:                                                    ┃
┃      → Corregir errores (usar sphinx-expert)                         ┃
┃      → Repetir build hasta 0 errores                                  ┃
┃      → Loop en FASE 4 🔄                                              ┃
┃                                                                        ┃
┃ OUTPUT: Archivos validados en trabajo/validaciones/ → FASE 5         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ FASE 5: INTEGRACIÓN EN PROYECTO                                      ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ INPUT: Archivos validados en trabajo/validaciones/                    ┃
┃                                                                        ┃
┃ Acciones:                                                              ┃
┃ 1. COPIAR a destino público:                                          ┃
┃    $ cp -r pipeline_docs_work/.../trabajo/validaciones/02/* \        ┃
┃            source/biblioteca/.../arc42_documentation/02_constraints/  ┃
┃                                                                        ┃
┃    Estructura destino:                                                 ┃
┃    02_constraints/                                                     ┃
┃      ├── index.rst                                                    ┃
┃      ├── secciones/                                                   ┃
┃      │   └── seccion_02_restricciones.rst                            ┃
┃      ├── tips/                                                        ┃
┃      │   └── tip_02_decisiones.rst                                    ┃
┃      └── ejemplos/                                                    ┃
┃          └── ejemplo_02_caso_real.rst                                 ┃
┃                                                                        ┃
┃ 2. ACTUALIZAR index.rst:                                              ┃
┃    .. toctree::                                                       ┃
┃       :maxdepth: 2                                                    ┃
┃       :glob:                                                          ┃
┃                                                                        ┃
┃       secciones/*                                                     ┃
┃       tips/*                                                          ┃
┃       ejemplos/*                                                      ┃
┃                                                                        ┃
┃ 3. GENERAR cross-references:                                          ┃
┃    .. _sec-02-constraints:                                           ┃
┃                                                                        ┃
┃ 4. ACTUALIZAR glosario (si aplica):                                   ┃
┃    Agregar términos a 12_glossary/secciones/glosario.rst             ┃
┃                                                                        ┃
┃ 5. BUILD final:                                                        ┃
┃    $ make clean && make html                                          ┃
┃    → Verificar 0 ERRORES ✅                                            ┃
┃                                                                        ┃
┃ 6. DOCUMENTAR (work-logger):                                          ┃
┃    .mywork/work-logs/2026-02-01-traduccion-seccion-02.md             ┃
┃                                                                        ┃
┃ 7. COMMIT (conventional commits):                                     ┃
┃    $ git add source/biblioteca/.../02_constraints/                   ┃
┃    $ git commit -m "docs(arc42): traducir seccion 02 constraints     ┃
┃                                                                        ┃
┃      - Traducción modo alta_fidelidad                                 ┃
┃      - Estructura por tipo (secciones/tips/ejemplos)                  ┃
┃      - Build exitoso (0 errores)                                      ┃
┃      - Metadata y reporte generados"                                  ┃
┃                                                                        ┃
┃ 8. ARCHIVAR trabajo:                                                  ┃
┃    $ mv metadata/seccion_02_metadata.yaml metadata/FINAL/            ┃
┃    $ mv reportes/REPORTE_seccion_02.rst reportes/FINAL/              ┃
┃    # trabajo/ queda en .gitignore                                     ┃
┃                                                                        ┃
┃ OUTPUT: Contenido integrado → RESULTADO FINAL ✅                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
               ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ RESULTADO FINAL                                                       ┃
┃ ───────────────────────────────────────────────────────────────────── ┃
┃ ✅ Contenido traducido en: source/biblioteca/.../02_constraints/     ┃
┃ ✅ Build Sphinx exitoso (0 errores)                                   ┃
┃ ✅ Metadata archivada: metadata/FINAL/seccion_02_metadata.yaml       ┃
┃ ✅ Reporte disponible: reportes/FINAL/REPORTE_seccion_02.rst         ┃
┃ ✅ Commit git creado con mensaje descriptivo                          ┃
┃ ✅ Usuario puede ver contenido en HTML:                               ┃
┃    _build/html/biblioteca/.../arc42_documentation/02_constraints/    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

```

---

## 📊 FASE 0: Recepción y Análisis de Solicitud

### Objetivo

Entender exactamente qué quiere el usuario y preparar el plan de trabajo.

### Trigger Patterns (Cuándo iniciar)

**Señales explícitas**:
- Usuario dice: "traduce X"
- Usuario provee URL
- Usuario sube archivo
- Usuario menciona framework (arc42, Diataxis)

**Señales implícitas**:
- Usuario habla de contenido en otro idioma
- Usuario menciona sección específica de arc42
- Usuario quiere agregar contenido a biblioteca

### Acciones

#### 1. Identificar solicitud

```
Preguntas clave:
- ¿Qué tipo de contenido? → arc42 / Diataxis / tutorial / referencia / general
- ¿Fuente disponible? → URL / archivo subido / ya clonado
- ¿Framework específico? → arc42 sección XX / Diataxis tipo / ninguno
```

**Ejemplos**:

```
Usuario: "Traduce la sección 02 de arc42"
→ Tipo: arc42
→ Fuente: Ya clonada en pipeline_docs_work/.../originales/
→ Framework: arc42 sección 02

Usuario: "Traduce este tutorial de Python" + archivo.md
→ Tipo: Tutorial
→ Fuente: Archivo subido
→ Framework: Diataxis (Tutorial)

Usuario: "Traduce https://example.com/api-docs"
→ Tipo: Referencia
→ Fuente: URL
→ Framework: Diataxis (Reference) o general
```

#### 2. Confirmar con usuario

```
Preguntas a hacer:
1. ¿Dónde quieres que se publique?
   → Ruta específica en biblioteca
   → Ejemplo: source/biblioteca/.../arc42_documentation/02_constraints/

2. ¿Qué modo de traducción prefieres?
   → alta_fidelidad (preservar estructura exacta)
   → marcado_visual (añadir admonitions)
   → enriquecimiento (explicar conceptos)

3. ¿Algún requisito especial?
   → Términos específicos a conservar
   → Secciones a omitir
   → Énfasis en ciertos aspectos
```

#### 3. Preparar entorno

```bash
# Verificar skills disponibles
ls .codex/skills/translation-workflow/SKILL.md
ls .codex/skills/sphinx-expert/SKILL.md

# Confirmar estructura destino existe
ls -la source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/

# Leer translation-workflow skill
view .codex/skills/translation-workflow/SKILL.md
```

### Output

**Plan de traducción claro**:

```yaml
solicitud:
  tipo: arc42_seccion_02
  fuente: pipeline_docs_work/.../originales/por_seccion/02_constraints/original/
  destino: source/biblioteca/.../arc42_documentation/02_constraints/
  modo: alta_fidelidad
  framework: arc42
  
siguiente_paso: FASE 1 - Análisis de documento fuente
```

---

## 🔍 FASE 1: Análisis de Documento Fuente

### Objetivo

Obtener y analizar el documento original para determinar la mejor estrategia de traducción.

### Input

- Documento fuente identificado (URL, archivo, o ruta local)
- Framework confirmado (arc42, Diataxis, general)

### Acciones

#### 1. OBTENER original

**Caso A: Arc42 (ya clonado)**

```bash
# Original completo disponible en:
ls pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/originales/

# Por sección:
cd pipeline_docs_work/.../originales/por_seccion/02_constraints/original/
ls -la
# → Archivos .md originales de arc42.org
```

**Caso B: URL Web**

```bash
# Descargar página
wget https://example.com/docs/api.html -O /tmp/original.html

# O si es sitio completo
wget -r -np -k https://example.com/docs/ -P /tmp/original_site/
```

**Caso C: Archivo del usuario**

```bash
# Ya disponible en uploads
ls /mnt/user-data/uploads/

# Copiar a temporal
cp /mnt/user-data/uploads/tutorial.md /tmp/original.md
```

#### 2. ANALIZAR estructura

```bash
# Ver contenido
cat /tmp/original.md | head -50

# Identificar:
# - Secciones principales (headers #, ##, ###)
# - Code blocks (```python, ```bash)
# - Tablas (|---|---|)
# - Imágenes (![alt](url))
# - Enlaces ([text](url))
# - Listas (-, *, 1.)
```

**Preguntas clave**:
- ¿Cuántas secciones tiene?
- ¿Hay code blocks? (no traducir código)
- ¿Hay tablas complejas?
- ¿Imágenes con caption?
- ¿Enlaces a otros documentos?

#### 3. DETERMINAR modo

**Decision Framework**:

```
¿Documento técnico con estructura fija?
  SÍ → alta_fidelidad
    Ejemplo: Arc42, API reference, especificación técnica
    
¿Tiene tabs, admonitions, elementos visuales?
  SÍ → marcado_visual
    Ejemplo: Tutorial con warnings, tips, notes
    
¿Es guía/tutorial que beneficia de explicaciones?
  SÍ → enriquecimiento
    Ejemplo: Tutorial para principiantes, guía práctica
    
¿No estás seguro?
  → Usar alta_fidelidad (más seguro)
```

#### 4. VALIDAR coherencia

```
Checklist:
✓ ¿Destino correcto en biblioteca?
  → source/biblioteca/.../XX_nombre/
  
✓ ¿Framework compatible con contenido?
  → Arc42 para arquitectura
  → Diataxis para documentación técnica
  
✓ ¿Terminología consistente?
  → Revisar glosario existente
  → Mantener términos técnicos en inglés si es estándar
```

### Output

```yaml
analisis:
  documento: "02-constraints.md"
  secciones: 5
  complejidad: media
  elementos_especiales:
    - tablas: 2
    - code_blocks: 0
    - imagenes: 1
  modo_seleccionado: alta_fidelidad
  rationale: "Estructura fija de arc42, preservar formato exacto"
  
siguiente_paso: FASE 2 - Configuración
```

---

## ⚙️ FASE 2: Configuración de Transformación

### Objetivo

Seleccionar el script correcto y configurar todos los parámetros necesarios.

### Input

- Modo seleccionado (alta_fidelidad, marcado_visual, enriquecimiento)
- Framework (arc42, Diataxis, general)
- Documento original

### Acciones

#### 1. SELECCIONAR script

**Decision Tree**:

```
¿Es arc42?
  SÍ → scripts/traduccion/arc42_scraper_python.py
        Optimizado para estructura arc42
        
¿Es URL web?
  SÍ → scripts/traduccion/translate_web_content.sh
        Extrae HTML y traduce
        
¿Es archivo general?
  SÍ → scripts/traduccion/adt_translator.py
        Traductor genérico
```

#### 2. CONFIGURAR parámetros

**Para arc42_scraper_python.py**:

```bash
python scripts/traduccion/arc42_scraper_python.py \
  --section 02 \                    # Número de sección
  --mode alta_fidelidad \            # Modo de traducción
  --framework arc42 \                # Framework
  --output pipeline_docs_work/.../trabajo/borradores/02_constraints/
```

**Para adt_translator.py**:

```bash
python scripts/traduccion/adt_translator.py \
  --input /tmp/original.md \
  --mode marcado_visual \
  --framework diataxis \
  --type tutorial \
  --output pipeline_docs_work/.../trabajo/borradores/tutorial_python/
```

#### 3. PREPARAR recursos

**Glosario terminológico**:

```bash
# Ver términos existentes
cat pipeline_docs/procedimientos/10_apendices/glosario_adt.rst

# Términos a preservar en inglés:
# - API, REST, HTTP
# - Nombres propios
# - Términos técnicos estándar
```

**Prompts de traducción**:

```yaml
prompts:
  sistema: "Eres un traductor técnico especializado en arquitectura de software"
  contexto: "Traduces documentación arc42 del inglés al español"
  estilo: "Mantén terminología técnica en inglés cuando sea estándar"
  formato: "Preserva estructura RST, code blocks, y tablas"
```

**Reglas de transformación**:

```yaml
reglas:
  code_blocks:
    accion: no_traducir
    excepcion: comentarios_en_codigo
    
  tablas:
    headers: traducir
    contenido: traducir_selectivamente
    
  imagenes:
    alt_text: traducir
    caption: traducir
    url: mantener
    
  enlaces:
    internos: actualizar_rutas
    externos: mantener
```

### Output

```yaml
configuracion:
  script: arc42_scraper_python.py
  parametros:
    section: "02"
    mode: alta_fidelidad
    framework: arc42
    output: pipeline_docs_work/.../trabajo/borradores/02_constraints/
  recursos_preparados:
    - glosario_cargado
    - prompts_configurados
    - reglas_definidas
    
siguiente_paso: FASE 3 - Ejecución
```

---

## 🚀 FASE 3: Ejecución de Transformación

### Objetivo

Ejecutar la traducción y generar todos los archivos necesarios.

### Input

- Script configurado
- Parámetros definidos
- Documento original

### Acciones

#### 1. EJECUTAR traducción

**Comando completo**:

```bash
cd /tmp/ADT

# Ejecutar script
python scripts/traduccion/arc42_scraper_python.py \
  --section 02 \
  --mode alta_fidelidad \
  --output pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/trabajo/borradores/02_constraints/

# Ver progreso
tail -f /tmp/traduccion.log
```

**Proceso interno del script**:

```
1. Leer documento original
2. Parsear estructura (headers, sections, code blocks)
3. Identificar elementos a traducir vs preservar
4. Llamar a API de traducción por secciones
5. Aplicar reglas de transformación
6. Generar archivos .rst por tipo
7. Guardar metadata
8. Crear reporte
```

#### 2. GENERAR archivos por tipo

**Estructura de salida**:

```
pipeline_docs_work/.../trabajo/borradores/02_constraints/
├── secciones/
│   ├── seccion_02_introduccion.rst
│   ├── seccion_02_restricciones_tecnicas.rst
│   └── seccion_02_restricciones_organizacionales.rst
├── tips/
│   ├── tip_02_identificar_restricciones.rst
│   └── tip_02_documentar_decisiones.rst
└── ejemplos/
    ├── ejemplo_02_restriccion_tecnologica.rst
    └── ejemplo_02_restriccion_tiempo.rst
```

**Contenido típico de seccion_02_introduccion.rst**:

```rst
.. _sec-02-intro:

Introducción a Restricciones
=============================

.. meta::
   :description: Introducción a las restricciones de arquitectura en arc42
   :keywords: restricciones, arquitectura, arc42, limitaciones
   :author: arc42.org
   :source: https://arc42.org/overview/#section-2

:Documento Original: `Section 2: Architecture Constraints <https://arc42.org/section-2/>`_
:Modo de Traducción: alta_fidelidad
:Framework: arc42
:Categoría: Introducción

Las restricciones de arquitectura son limitaciones impuestas al sistema...

```

#### 3. GENERAR metadata

**Archivo: metadata/seccion_02_metadata.yaml**

```yaml
seccion: 02
titulo: Architecture Constraints
titulo_es: Restricciones de Arquitectura

traduccion:
  modo: alta_fidelidad
  fecha: "2026-02-01"
  traductor: Claude
  revisor: pendiente
  
framework: arc42
categoria: restricciones

archivos_generados:
  secciones:
    - seccion_02_introduccion.rst
    - seccion_02_restricciones_tecnicas.rst
    - seccion_02_restricciones_organizacionales.rst
  tips:
    - tip_02_identificar_restricciones.rst
    - tip_02_documentar_decisiones.rst
  ejemplos:
    - ejemplo_02_restriccion_tecnologica.rst
    - ejemplo_02_restriccion_tiempo.rst

terminos_clave:
  - Technical Constraints
  - Organizational Constraints
  - Political Constraints
  - Legal Concerns
  - Framework
  
estado: borrador
notas: |
  Términos técnicos mantenidos en inglés por ser estándar.
  Tablas preservadas con formato original.
  Referencias internas actualizadas.
```

#### 4. GENERAR reporte

**Archivo: reportes/REPORTE_seccion_02.rst**

```rst
==========================================
Reporte: Traducción Sección 02 Arc42
==========================================

:Fecha: 2026-02-01
:Sección: 02 - Architecture Constraints
:Modo: alta_fidelidad
:Estado: Borrador

Resumen
-------

Traducción de sección 02 de arc42.org sobre restricciones de arquitectura.

Documento original dividido en 3 archivos principales + 2 tips + 2 ejemplos.

Análisis del Original
---------------------

**Estructura**:

- Introducción (200 palabras)
- Restricciones Técnicas (tabla con 5 entradas)
- Restricciones Organizacionales (lista de 8 items)
- Ejemplos (2 casos reales)

**Elementos especiales**:

- 1 tabla compleja (5 columnas)
- 2 code blocks (ejemplos de constraints)
- 3 imágenes (diagramas de restricciones)
- 15 enlaces internos a otras secciones

Decisiones Tomadas
------------------

1. **Modo alta_fidelidad**: Preservar estructura exacta por ser arc42
2. **Términos en inglés**: Mantener "constraints", "stakeholder", etc.
3. **División por tipo**: Separar introducción, tipos de restricciones, tips y ejemplos
4. **Tablas**: Formato preservado, solo traducir celdas de contenido

Problemas Encontrados
---------------------

1. **Tabla compleja**: Requirió ajuste manual de anchos de columna
2. **Enlaces rotos**: 2 enlaces a secciones aún no traducidas (pendiente)
3. **Imagen faltante**: restricciones-politicas.png no encontrada (comentada)

Próximos Pasos
--------------

1. Validar sintaxis RST (FASE 4)
2. Corregir warnings de build
3. Actualizar enlaces cuando se traduzcan secciones 01 y 03
4. Obtener imagen faltante o crear alternativa
5. Revisar terminología con experto dominio

Archivos Generados
------------------

- 3 archivos en secciones/
- 2 archivos en tips/
- 2 archivos en ejemplos/
- 1 metadata YAML
- 1 reporte (este archivo)

Total: 9 archivos
```

### Output

```
✅ Archivos generados en: pipeline_docs_work/.../trabajo/borradores/02_constraints/
✅ Metadata creada: metadata/seccion_02_metadata.yaml
✅ Reporte disponible: reportes/REPORTE_seccion_02.rst

siguiente_paso: FASE 4 - Validación
```

---

## ✅ FASE 4: Validación de Salida

### Objetivo

Asegurar que los archivos traducidos tienen sintaxis RST correcta y pasan el build de Sphinx sin errores.

### Input

- Archivos .rst en trabajo/borradores/
- Metadata generada
- Reporte de traducción

### Skill Usado

**sphinx-expert v1.9.0** (sección "Integración con Translation Workflow")

### Acciones

#### 1. COPIAR temporalmente a source/

```bash
# Backup de destino actual (si existe)
if [ -d "source/biblioteca/.../02_constraints/" ]; then
    cp -r source/biblioteca/.../02_constraints/ /tmp/backup_02/
fi

# Copiar borradores a source/
cp -r pipeline_docs_work/.../trabajo/borradores/02_constraints/* \
      source/biblioteca/.../arc42_documentation/02_constraints/
```

#### 2. BUILD limpio (OBLIGATORIO)

```bash
cd /tmp/ADT

# Limpiar build anterior
make clean

# Build completo con log
make html 2>&1 | tee /tmp/build_validation.log

# Ver resumen
tail -20 /tmp/build_validation.log
```

**Output esperado**:

```
building [html]: targets for 150 source files that are out of date
...
reading sources... [100%] biblioteca/.../02_constraints/index
...
writing output... [100%] biblioteca/.../02_constraints/index
...
build succeeded, 3 warnings.
```

#### 3. VERIFICAR errores

```bash
# Buscar errores
grep "ERROR:" /tmp/build_validation.log

# DEBE ser:
# (sin output) → 0 errores ✅
```

**Si hay errores**:

```bash
# Ver error específico
grep -A 5 "ERROR:" /tmp/build_validation.log

# Ejemplo de output:
# source/biblioteca/.../seccion_02.rst:45: ERROR: Unknown directive type "note"
#   → Corregir: cambiar "note" por ".. note::"

# Ir a archivo y corregir
# Repetir build hasta 0 errores
```

#### 4. VERIFICAR warnings

```bash
# Contar warnings
grep "WARNING:" /tmp/build_validation.log | wc -l

# Ver tipos de warnings
grep "WARNING:" /tmp/build_validation.log | sed 's/.*WARNING: //' | sort | uniq -c
```

**Criterios**:

```
ACEPTABLE (< 5 warnings):
  2  Enumerated list ends without a blank line
  1  term not in glossary: 'Stakeholder'
  → OK para continuar ✅

NO ACEPTABLE (≥ 5 warnings):
  15  Enumerated list ends without a blank line
  10  term not in glossary: 'Technical Constraints'
  3   ERROR parsing content block
  → Corregir antes de continuar ❌
```

#### 5. VALIDAR calidad

**Coherencia terminológica**:

```bash
# Verificar términos en glosario
grep -r ":term:\`" source/biblioteca/.../02_constraints/

# Cada término debe estar en:
# source/biblioteca/.../12_glossary/secciones/glosario.rst
```

**Enlaces internos**:

```bash
# Verificar referencias
grep -r ":ref:\`" source/biblioteca/.../02_constraints/

# Cada label debe existir en algún .rst
rg "^\.\. _" source/biblioteca/
```

**Imágenes**:

```bash
# Verificar que imágenes existen
grep -r ".. image::" source/biblioteca/.../02_constraints/ | \
  awk '{print $3}' | \
  xargs -I {} test -f {} && echo "OK" || echo "FALTA: {}"
```

#### 6. DECISIÓN

**SI build OK (0 errores, <5 warnings)**:

```bash
# Mover a validaciones
mv pipeline_docs_work/.../trabajo/borradores/02_constraints \
   pipeline_docs_work/.../trabajo/validaciones/02_constraints

echo "✅ FASE 4 completada → FASE 5"
```

**SI build FALLA (errores o ≥5 warnings)**:

```bash
# Identificar problema
cat /tmp/build_validation.log | grep -E "ERROR|WARNING" | head -10

# Usar sphinx-expert para corregir
view .codex/skills/sphinx-expert/SKILL.md

# Corregir archivo(s)
# Repetir build
# Loop en FASE 4 hasta OK
```

### Errores Comunes y Correcciones

**Error 1: Indentación en listas**

```rst
# ❌ INCORRECTO (1 espacio)
 * Item 1
 * Item 2

# ✅ CORRECTO (3 espacios)
   * Item 1
   * Item 2
```

**Error 2: List-table desalineada**

```rst
# ❌ INCORRECTO
.. list-table::
   :header-rows: 1

   * - Col1
   - Col2  # Falta indentación

# ✅ CORRECTO
.. list-table::
   :header-rows: 1

   * - Col1
     - Col2  # Alineado con Col1
```

**Error 3: Directiva sin línea en blanco**

```rst
# ❌ INCORRECTO
.. note::
   Texto importante
Siguiente párrafo

# ✅ CORRECTO
.. note::
   Texto importante

Siguiente párrafo  # Línea en blanco
```

**Error 4: Label duplicado**

```rst
# ❌ INCORRECTO (label existe en otro archivo)
.. _sec-intro:

# ✅ CORRECTO (label único)
.. _sec-02-intro:
```

### Output

```
✅ Build Sphinx: SUCCESS
✅ Errores: 0
✅ Warnings: 2 (aceptable)
✅ Archivos movidos a: trabajo/validaciones/02_constraints/

siguiente_paso: FASE 5 - Integración
```

---

## 🔗 FASE 5: Integración en Proyecto

### Objetivo

Copiar los archivos validados a su ubicación final en source/biblioteca/, actualizar índices, documentar, y crear commit.

### Input

- Archivos validados en trabajo/validaciones/
- Build Sphinx exitoso (0 errores)

### Acciones

#### 1. COPIAR a destino público

```bash
# FROM: Archivos validados
FROM="pipeline_docs_work/ingenieria/sistemas/arquitectura/arc42_documentation/trabajo/validaciones/02_constraints/"

# TO: Biblioteca pública
TO="source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/02_constraints/"

# Copiar por tipo
cp -r $FROM/secciones/* $TO/secciones/
cp -r $FROM/tips/* $TO/tips/
cp -r $FROM/ejemplos/* $TO/ejemplos/
cp -r $FROM/diagramas/* $TO/diagramas/ 2>/dev/null || true
cp -r $FROM/figuras/* $TO/figuras/ 2>/dev/null || true

# Verificar
ls -la $TO/
```

**Resultado**:

```
02_constraints/
├── index.rst
├── secciones/
│   ├── seccion_02_introduccion.rst
│   ├── seccion_02_restricciones_tecnicas.rst
│   └── seccion_02_restricciones_organizacionales.rst
├── tips/
│   ├── tip_02_identificar_restricciones.rst
│   └── tip_02_documentar_decisiones.rst
├── ejemplos/
│   ├── ejemplo_02_restriccion_tecnologica.rst
│   └── ejemplo_02_restriccion_tiempo.rst
├── diagramas/
└── figuras/
```

#### 2. ACTUALIZAR index.rst

**Archivo: source/biblioteca/.../02_constraints/index.rst**

```rst
.. _sec-02-constraints:

==================================
02. Restricciones de Arquitectura
==================================

.. meta::
   :description: Restricciones que limitan el diseño y decisiones de arquitectura
   :keywords: restricciones, arquitectura, arc42, limitaciones

Contenido
=========

.. toctree::
   :maxdepth: 2
   :caption: Secciones Principales
   :glob:

   secciones/*

.. toctree::
   :maxdepth: 1
   :caption: Tips y Consejos
   :glob:

   tips/*

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos Prácticos
   :glob:

   ejemplos/*

Sobre esta Sección
==================

Las restricciones de arquitectura son limitaciones que afectan...

:Documento Original: `arc42 Section 2 <https://arc42.org/section-2/>`_
:Modo de Traducción: alta_fidelidad
:Fecha: 2026-02-01
```

#### 3. GENERAR cross-references

**En cada archivo .rst principal**:

```rst
.. _sec-02-restricciones-tecnicas:

Restricciones Técnicas
======================

Las restricciones técnicas limitan...

Ver también: :ref:`sec-03-contexto` para entender el alcance del sistema.
```

**En otros archivos que referencien**:

```rst
Para más detalles sobre restricciones, ver :ref:`sec-02-constraints`.
```

#### 4. ACTUALIZAR glosario (si aplica)

**Archivo: source/biblioteca/.../12_glossary/secciones/glosario.rst**

```rst
.. glossary::

   Technical Constraints
      Restricciones técnicas que limitan las decisiones de arquitectura,
      como frameworks, plataformas, o protocolos obligatorios.
      
      Ver: :ref:`sec-02-restricciones-tecnicas`

   Organizational Constraints
      Limitaciones impuestas por la estructura organizacional,
      procesos, o decisiones de gestión.
      
      Ver: :ref:`sec-02-restricciones-organizacionales`

   Stakeholder
      Parte interesada en el sistema con influencia en decisiones
      de arquitectura.
```

#### 5. BUILD final

```bash
cd /tmp/ADT

# Build limpio final
make clean
make html 2>&1 | tee /tmp/build_final.log

# Verificar
grep "build succeeded" /tmp/build_final.log
# → build succeeded, 0 warnings. ✅

# Ver resultado
ls _build/html/biblioteca/.../arc42_documentation/02_constraints/index.html
```

#### 6. DOCUMENTAR (work-logger)

**Archivo: .mywork/work-logs/2026-02-01-traduccion-seccion-02.md**

```markdown
# Work Log: Traducción Sección 02 Arc42

**Fecha**: 2026-02-01
**Tipo**: Traducción
**Skill**: translation-workflow v1.3.0
**Duración**: 2 horas

## Objetivo

Traducir sección 02 (Architecture Constraints) de arc42.org al español
siguiendo metodología ADT.

## Trabajo Realizado

### FASE 0-3: Traducción
- Modo: alta_fidelidad
- Framework: arc42
- Archivos generados: 7 (.rst)

### FASE 4: Validación
- Build: SUCCESS (0 errores)
- Warnings: 2 (aceptable)
- Correcciones: 3 errores de indentación en listas

### FASE 5: Integración
- Archivos copiados a: source/biblioteca/.../02_constraints/
- Index.rst actualizado con toctrees
- Cross-references añadidas
- Glosario actualizado (3 términos nuevos)
- Build final: SUCCESS

## Archivos Creados

**Secciones** (3):
- seccion_02_introduccion.rst
- seccion_02_restricciones_tecnicas.rst
- seccion_02_restricciones_organizacionales.rst

**Tips** (2):
- tip_02_identificar_restricciones.rst
- tip_02_documentar_decisiones.rst

**Ejemplos** (2):
- ejemplo_02_restriccion_tecnologica.rst
- ejemplo_02_restriccion_tiempo.rst

**Metadata y Reportes**:
- metadata/FINAL/seccion_02_metadata.yaml
- reportes/FINAL/REPORTE_seccion_02.rst

## Decisiones Tomadas

DA-001: Términos técnicos en inglés
- Rationale: "Constraints", "Stakeholder" son estándar internacional

DA-002: División por tipo de contenido
- Rationale: Facilita navegación y mantenimiento

## Métricas

- Palabras traducidas: ~2,500
- Tablas procesadas: 2
- Imágenes: 1 (1 comentada por falta de archivo)
- Enlaces internos: 8
- Términos de glosario: 3

## Próximos Pasos

1. Traducir sección 03 (Context and Scope)
2. Actualizar enlaces rotos cuando secciones 01 y 03 estén listas
3. Obtener o recrear imagen faltante: restricciones-politicas.png

## Referencias

- Original: https://arc42.org/section-2/
- Commit: [próximo]
```

#### 7. COMMIT (conventional commits)

```bash
cd /tmp/ADT

# Agregar archivos
git add source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/02_constraints/
git add .mywork/work-logs/2026-02-01-traduccion-seccion-02.md

# Ver cambios
git status -s

# Commit con mensaje descriptivo
git commit -m "docs(arc42): traducir seccion 02 constraints

Traducción de Architecture Constraints (arc42 sección 02) del inglés
al español usando modo alta_fidelidad.

CONTENIDO:
- 3 archivos en secciones/ (introducción, técnicas, organizacionales)
- 2 archivos en tips/ (identificar, documentar)
- 2 archivos en ejemplos/ (tecnológica, tiempo)

ESTRUCTURA:
- División por tipo de contenido (secciones/tips/ejemplos)
- Index.rst con toctrees organizados
- Cross-references a otras secciones arc42

VALIDACIÓN:
- Build Sphinx: SUCCESS (0 errores, 0 warnings)
- Sintaxis RST: verificada
- Enlaces internos: validados
- Glosario actualizado (3 términos)

METADATA:
- Modo: alta_fidelidad
- Framework: arc42
- Metadata: seccion_02_metadata.yaml
- Reporte: REPORTE_seccion_02.rst

DECISIONES:
- DA-001: Mantener términos técnicos en inglés (estándar)
- DA-002: División por tipo para mejor navegación

Relacionado: reorganizacion-biblioteca-v1.0.0
Skill: translation-workflow v1.3.0
Work-log: .mywork/work-logs/2026-02-01-traduccion-seccion-02.md"

# Verificar commit
git log -1 --oneline
```

#### 8. ARCHIVAR trabajo

```bash
# Mover metadata a FINAL
mv pipeline_docs_work/.../metadata/seccion_02_metadata.yaml \
   pipeline_docs_work/.../metadata/FINAL/

# Mover reporte a FINAL
mv pipeline_docs_work/.../reportes/REPORTE_seccion_02.rst \
   pipeline_docs_work/.../reportes/FINAL/

# Limpiar trabajo/borradores/ (opcional, ya está en .gitignore)
# Los archivos en trabajo/validaciones/ pueden quedarse o eliminarse

# Verificar
ls pipeline_docs_work/.../metadata/FINAL/
ls pipeline_docs_work/.../reportes/FINAL/
```

### Output

```
✅ Contenido integrado en: source/biblioteca/.../02_constraints/
✅ Index.rst actualizado con toctrees
✅ Cross-references añadidas
✅ Glosario actualizado (3 términos)
✅ Build final: SUCCESS (0 errores)
✅ Work-log creado: .mywork/work-logs/2026-02-01-traduccion-seccion-02.md
✅ Commit creado: docs(arc42): traducir seccion 02 constraints
✅ Metadata archivada: metadata/FINAL/seccion_02_metadata.yaml
✅ Reporte archivado: reportes/FINAL/REPORTE_seccion_02.rst

→ RESULTADO FINAL ✅
```

---

## 🎉 RESULTADO FINAL

### Estado del Proyecto

**CONTENIDO TRADUCIDO**:
```
source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/02_constraints/
├── index.rst
├── secciones/ (3 archivos)
├── tips/ (2 archivos)
└── ejemplos/ (2 archivos)
```

**BUILD SPHINX**:
```bash
make html
# → build succeeded, 0 warnings.

ls _build/html/biblioteca/.../arc42_documentation/02_constraints/
# → index.html
# → secciones/seccion_02_introduccion.html
# → tips/tip_02_identificar_restricciones.html
# → ejemplos/ejemplo_02_restriccion_tecnologica.html
```

**GIT**:
```bash
git log -1 --oneline
# → abc1234 docs(arc42): traducir seccion 02 constraints

git show --stat
# → 7 files changed, 542 insertions(+)
```

**METADATA ARCHIVADA**:
```
pipeline_docs_work/.../metadata/FINAL/seccion_02_metadata.yaml
pipeline_docs_work/.../reportes/FINAL/REPORTE_seccion_02.rst
```

### Usuario Puede Ver

**HTML Publicado**:
```
_build/html/biblioteca/.../arc42_documentation/02_constraints/index.html
```

**Navegación**:
- Índice general de arc42
- Sección 02: Restricciones de Arquitectura
  - Introducción
  - Restricciones Técnicas
  - Restricciones Organizacionales
  - Tips: Identificar Restricciones
  - Tips: Documentar Decisiones
  - Ejemplos: Restricción Tecnológica
  - Ejemplos: Restricción de Tiempo

**Links funcionan**:
- Enlaces internos a otras secciones arc42 ✅
- Referencias de glosario ✅
- Cross-references ✅

---

## 💼 Casos de Uso

### Caso 1: Traducir Nueva Sección Arc42

**Solicitud**:
```
Usuario: "Traduce la sección 03 de arc42"
```

**Flujo**:
```
FASE 0: Identificar arc42 sección 03
FASE 1: Original en pipeline_docs_work/.../originales/por_seccion/03_context_scope/
FASE 2: Script arc42_scraper_python.py con --section 03
FASE 3: Generar archivos en trabajo/borradores/03_context_scope/
FASE 4: Build limpio → 0 errores
FASE 5: Integrar en source/biblioteca/.../03_context_scope/
```

**Tiempo**: 1.5-2 horas

---

### Caso 2: Traducir Tutorial desde URL

**Solicitud**:
```
Usuario: "Traduce este tutorial de FastAPI: https://fastapi.tiangolo.com/tutorial/"
```

**Flujo**:
```
FASE 0: Identificar tipo=tutorial, framework=Diataxis
FASE 1: wget URL → /tmp/original.html
FASE 2: Script translate_web_content.sh con --type tutorial
FASE 3: Generar archivos en trabajo/borradores/tutorial_fastapi/
FASE 4: Build limpio → corregir 3 warnings de formato
FASE 5: Integrar en source/biblioteca/informatica/web/fastapi/tutorial/
```

**Tiempo**: 2-3 horas (por complejidad del sitio web)

---

### Caso 3: Traducir Documento de Usuario

**Solicitud**:
```
Usuario: "Traduce este documento de API" + uploads/api-spec.md
```

**Flujo**:
```
FASE 0: Identificar tipo=referencia, framework=general
FASE 1: Archivo en /mnt/user-data/uploads/api-spec.md
FASE 2: Script adt_translator.py con --type reference
FASE 3: Generar archivos en trabajo/borradores/api_spec/
FASE 4: Build limpio → 0 errores
FASE 5: Integrar en source/biblioteca/informatica/api/especificacion/
```

**Tiempo**: 1-1.5 horas

---

## 🔧 Troubleshooting

### Problema 1: Build Falla en FASE 4

**Síntoma**:
```
ERROR: Unknown directive type "admonition"
```

**Causa**:
Directiva mal escrita

**Solución**:
```bash
# Buscar archivo
grep -r "admonition" source/biblioteca/.../02_constraints/

# Corregir
# ❌ .. admonition::
# ✅ .. note::

# Re-build
make html
```

---

### Problema 2: Warnings Excesivos

**Síntoma**:
```
build succeeded, 25 warnings.
```

**Causa**:
Formato de listas o términos no en glosario

**Solución**:
```bash
# Ver tipos de warnings
grep "WARNING:" /tmp/build_final.log | sed 's/.*WARNING: //' | sort | uniq -c

# Si son de listas:
python scripts/fix_list_spacing.py source/biblioteca/.../02_constraints/**/*.rst

# Si son de glosario:
# Agregar términos a 12_glossary/secciones/glosario.rst

# Re-build
make html
```

---

### Problema 3: Script No Encuentra Original

**Síntoma**:
```
FileNotFoundError: No such file: 'pipeline_docs_work/.../originales/por_seccion/02_constraints/original/'
```

**Causa**:
Original no clonado o ruta incorrecta

**Solución**:
```bash
# Verificar estructura
ls pipeline_docs_work/.../originales/

# Si falta original, clonar
git clone https://github.com/arc42/arc42.org-site.git /tmp/arc42_site

# Copiar a originales
cp -r /tmp/arc42_site/_posts/02-constraints/ \
      pipeline_docs_work/.../originales/por_seccion/02_constraints/original/

# Repetir FASE 1
```

---

### Problema 4: Metadata Incompleta

**Síntoma**:
Falta información en metadata YAML

**Causa**:
Script no generó metadata completa

**Solución**:
```bash
# Editar manualmente
vi pipeline_docs_work/.../metadata/seccion_02_metadata.yaml

# Agregar campos faltantes
cat >> pipeline_docs_work/.../metadata/seccion_02_metadata.yaml << 'EOF'
archivos_generados:
  secciones:
    - seccion_02_introduccion.rst
  tips:
    - tip_02_identificar.rst
terminos_clave:
  - Technical Constraints
EOF

# Verificar
cat pipeline_docs_work/.../metadata/seccion_02_metadata.yaml
```

---

### Problema 5: Enlaces Rotos

**Síntoma**:
```
WARNING: undefined label: 'sec-01-introduction'
```

**Causa**:
Sección referenciada aún no traducida

**Solución**:
```bash
# Opción 1: Comentar referencia temporalmente
sed -i 's/Ver :ref:`sec-01-introduction`/.. Ver :ref:`sec-01-introduction` (pendiente traducción)/' \
    source/biblioteca/.../seccion_02.rst

# Opción 2: Traducir sección 01 primero
# (repetir flujo completo para sección 01)

# Opción 3: Usar enlace externo
# :ref:`sec-01-introduction` → `Section 01 <https://arc42.org/section-1/>`_

# Re-build
make html
```

---

## 📚 Referencias

### Skills

- `.codex/skills/translation-workflow/SKILL.md` (v1.3.0)
- `.codex/skills/sphinx-expert/SKILL.md` (v1.9.0)
- `.codex/skills/work-logger/SKILL.md`
- `.codex/skills/commit-helper/SKILL.md`

### Scripts

- `scripts/traduccion/arc42_scraper_python.py`
- `scripts/traduccion/translate_web_content.sh`
- `scripts/traduccion/adt_translator.py`
- `scripts/fix_list_spacing.py`

### Documentación

- `pipeline_docs_work/README.md`
- `pipeline_docs_work/.../arc42_documentation/README.md`
- `source/biblioteca/.../arc42_documentation/index.rst`

### Estructura

```
/tmp/ADT/
├── source/biblioteca/                # PÚBLICO
│   └── .../arc42_documentation/
│       └── XX_nombre/
│           ├── index.rst
│           ├── secciones/
│           ├── tips/
│           ├── ejemplos/
│           ├── diagramas/
│           └── figuras/
├── pipeline_docs_work/               # PRIVADO
│   └── .../arc42_documentation/
│       ├── originales/
│       ├── metadata/
│       ├── reportes/
│       └── trabajo/
│           ├── borradores/
│           └── validaciones/
└── scripts/traduccion/               # HERRAMIENTAS
```

---

## ✅ Checklist Completo

**FASE 0**:
- [ ] Solicitud identificada
- [ ] Tipo de contenido determinado
- [ ] Framework confirmado
- [ ] Destino acordado con usuario
- [ ] Modo de traducción seleccionado

**FASE 1**:
- [ ] Original obtenido
- [ ] Estructura analizada
- [ ] Elementos especiales identificados
- [ ] Modo validado

**FASE 2**:
- [ ] Script seleccionado
- [ ] Parámetros configurados
- [ ] Glosario preparado
- [ ] Reglas definidas

**FASE 3**:
- [ ] Traducción ejecutada
- [ ] Archivos generados por tipo
- [ ] Metadata creada
- [ ] Reporte generado

**FASE 4**:
- [ ] Archivos copiados a source/ (temporal)
- [ ] Build limpio ejecutado
- [ ] 0 errores verificados
- [ ] <5 warnings confirmados
- [ ] Calidad validada
- [ ] Archivos movidos a validaciones/

**FASE 5**:
- [ ] Archivos copiados a destino final
- [ ] Index.rst actualizado
- [ ] Cross-references añadidas
- [ ] Glosario actualizado
- [ ] Build final exitoso
- [ ] Work-log creado
- [ ] Commit realizado
- [ ] Metadata archivada

**RESULTADO**:
- [ ] Contenido publicado
- [ ] HTML generado
- [ ] Git commit creado
- [ ] Usuario puede ver contenido

---

**FIN DEL FLUJO COMPLETO** ✅
