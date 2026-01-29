# Fundamentos de ADT

Basado en: source/docs_maestros/ARQUITECTURA_DOCUMENTAL_TRADUCCION.md

## Que es ADT

ADT = Arquitectura Documental de Traduccion

Sistema metodologico para transformacion de documentacion tecnica que considera la traduccion como una operacion de transformacion entre sistemas semioticos, no como una simple transferencia de palabras entre idiomas.

## Principios Fundamentales

### 1. Transformacion no Traduccion

La traduccion es una TRANSFORMACION entre sistemas semioticos, no una transferencia literal de palabras.

Concepto clave: Signifiant vs Signifie

SIGNIFIANT (Significante):
- Forma material del signo
- Palabras, estructura, formato
- Representacion fisica del mensaje

SIGNIFIE (Significado):
- Contenido conceptual
- Ideas, conceptos transmitidos
- Mensaje subyacente

IMPLICACION:
En traduccion documental tecnica, debemos preservar el SIGNIFIE (significado, conceptos) adaptando el SIGNIFIANT (forma, estructura) al medio destino.

Ejemplo:
```
ORIGINAL (Ingles):
"The system shall provide..."

TRADUCCION LITERAL:
"El sistema debe proveer..."

TRANSFORMACION ADT:
"El sistema proporcionara..."
(Adapta forma al español natural manteniendo significado tecnico)
```

### 2. Fidelidad Estructural

No se trata de fidelidad palabra por palabra, sino de fidelidad a la ESTRUCTURA CONCEPTUAL.

Preservar:
- JERARQUIA de conceptos
- RELACIONES entre ideas
- COHERENCIA terminologica
- CONVENCIONES del medio destino

NO preservar necesariamente:
- Orden exacto de palabras
- Estructura gramatical original
- Modismos idiomaticos del origen

Ejemplo:
```rst
ORIGINAL:
Introduction
  Background
  Motivation
  Goals

TRADUCCION ESTRUCTURAL:
Introduccion
  Antecedentes
  Motivacion
  Objetivos

(Preserva jerarquia y relaciones, adapta terminos)
```

### 3. Enriquecimiento Contextual

Cuando apropiado y mejora la comprension, AGREGAR contexto explicito.

Cuando agregar:
- Metadata que mejora comprension
- Explicitar relaciones implicitas en el original
- Mantener trazabilidad al documento fuente
- Aclaraciones culturales o tecnicas necesarias

Cuando NO agregar:
- Informacion redundante
- Opiniones personales
- Contexto no relevante
- Material que altera el significado original

Ejemplo con admoniciones RST:
```rst
ORIGINAL (solo texto):
"Use the API endpoint carefully."

CON ENRIQUECIMIENTO:
.. warning::
   Use el endpoint de API con precaucion.
   
   Llamadas excesivas pueden resultar en rate limiting.

(Explicita consecuencia implicita en "carefully")
```

## Metodologia ADT en Practica

### Proceso de Transformacion

1. ANALISIS
   - Identificar Signifie (que se quiere comunicar)
   - Analizar estructura conceptual
   - Detectar convenciones del medio origen

2. PLANIFICACION
   - Determinar Signifiant apropiado para medio destino
   - Decidir nivel de enriquecimiento
   - Seleccionar modo de traduccion

3. TRANSFORMACION
   - Aplicar modo seleccionado
   - Preservar estructura conceptual
   - Adaptar forma al medio destino

4. VALIDACION
   - Verificar preservacion del Signifie
   - Confirmar coherencia estructural
   - Validar convenciones del medio destino

### Modos de Aplicacion

ADT define tres modos principales:

ALTA FIDELIDAD:
- Maxima preservacion de estructura original
- Minima adaptacion
- Para documentacion tecnica critica

MARCADO VISUAL:
- Enriquecimiento mediante admoniciones
- Mejora de navegabilidad
- Para material educativo

ENRIQUECIMIENTO:
- Expansion de conceptos
- Agregado de contexto
- Para material de referencia

Ver: translation_modes.md

## Aplicacion a Documentacion Tecnica

### Sphinx y RST

ADT se aplica especialmente bien a transformacion de documentacion a Sphinx/RST porque:

1. RST es SEMANTICO (marca significado, no solo formato)
2. Sphinx maneja ESTRUCTURA (toctree, cross-refs)
3. Permite ENRIQUECIMIENTO (admonitions, directives)

Ejemplo de transformacion semantica:
```rst
MARKDOWN ORIGINAL:
**Important:** Use HTTPS only

TRANSFORMACION ADT A RST:
.. important::
   Use unicamente HTTPS

(Convierte formato visual a estructura semantica)
```

### Frameworks Soportados

DIATAXIS:
- Organizacion por tipo de contenido
- 4 cuadrantes segun orientacion
- ADT respeta categorias Diataxis

ARC42:
- Template arquitectonico estructurado
- 12 secciones predefinidas
- ADT preserva estructura arc42

## Diferencias con Traduccion Convencional

TRADUCCION CONVENCIONAL:
- Foco en palabras
- Transferencia directa
- Minimal adaptacion

TRANSFORMACION ADT:
- Foco en conceptos (Signifie)
- Adaptacion estructural
- Enriquecimiento contextual

Ejemplo comparativo:
```
ORIGINAL INGLES:
"Click the button to proceed"

TRADUCCION CONVENCIONAL:
"Haga clic en el boton para proceder"

TRANSFORMACION ADT (Marcado Visual):
.. tip::
   Para continuar, haga clic en el boton "Siguiente"
   
(Explicita el nombre del boton, agrega contexto visual)
```

## Metricas de Calidad ADT

### Preservacion de Significado

Verificar que:
- Conceptos clave se mantienen
- Relaciones entre ideas preservadas
- Terminologia coherente

### Adaptacion al Medio

Verificar que:
- Convenciones RST respetadas
- Estructura Sphinx correcta
- Navegacion optimizada

### Enriquecimiento Apropiado

Verificar que:
- Metadata util agregada
- Admoniciones pertinentes
- Sin redundancia innecesaria

## Referencias

Documento completo:
- source/docs_maestros/ARQUITECTURA_DOCUMENTAL_TRADUCCION.md

Teoria semiotica:
- Saussure: Significante y Significado
- Jakobson: Traduccion intersemiotica

Metodologia:
- source/docs_maestros/SINTESIS_METODOLOGICA_ADT.rst

## Notas Importantes

- ADT es una METODOLOGIA, no solo un conjunto de reglas
- Requiere COMPRENSION del contenido, no solo conocimiento linguistico
- Se enfoca en CALIDAD sobre velocidad
- Prioriza USABILIDAD del documento final
- Es ITERATIVA: analisis, transformacion, validacion, refinamiento
