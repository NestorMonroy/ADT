---
name: translation-workflow
description: "Workflow completo de traduccion siguiendo metodologia ADT. Usar cuando el usuario necesite traducir contenido, aplicar modos de traduccion, o ejecutar proceso de transformacion documental."
---

# Translation Workflow - Metodologia ADT

## Cuando usar

- Usuario pide traducir documento
- Transformar contenido a RST
- Aplicar modo de traduccion especifico
- Generar metadata de traduccion
- Integrar contenido en estructura Sphinx

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
