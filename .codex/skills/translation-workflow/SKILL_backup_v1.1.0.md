---
name: translation-workflow
description: "Workflow completo de traduccion siguiendo metodologia ADT. Usar cuando el usuario necesite traducir contenido, aplicar modos de traduccion, o ejecutar proceso de transformacion documental."
version: 1.1.0
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
   Ver: `source/10_apendices/glosario_adt.rst`

### FASE 3: Ejecucion de Transformacion

EJEMPLO arc42:
```bash
python scripts/traduccion/arc42_scraper_python.py \
  --section 02 \
  --mode alta_fidelidad \
  --output source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentationsections/02_constraints/traduccion/
```

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

- source/02_procedimientos/workflow_general.rst
- source/04_reglas_operativas/matrices_decision/
- scripts/traduccion/
- source/03_estandares/calidad/

## Notas

- Consultar project-context primero
- Validar build siempre
- Documentar decisiones
- Mantener coherencia terminologica
- Usar scripts existentes

---

## Changelog

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
