# Estructura arc42 en ADT

Basado en: source/biblioteca/arc42/

## Que es arc42

arc42 es un template de documentacion arquitectonica libre y de codigo abierto, creado por Dr. Gernot Starke y Dr. Peter Hruschka.

Proporciona una estructura estandar en 12 secciones para documentar arquitecturas de software.

## Ubicacion en el Proyecto

Base: source/biblioteca/arc42/

Estructura completa:
```
arc42/
+-- index.rst (indice principal del libro)
+-- metadata_libro.rst (metadata completa del libro)
+-- glosario_acumulativo.rst (terminos consolidados)
+-- sections/ (las 12 secciones)
 +-- 01_introduction_goals/
 +-- 02_constraints/
 +-- 03_context_scope/
 +-- 04_solution_strategy/
 +-- 05_building_blocks/
 +-- 06_runtime_view/
 +-- 07_deployment_view/
 +-- 08_crosscutting_concepts/
 +-- 09_architecture_decisions/
 +-- 10_quality_requirements/
 +-- 11_risks_technical_debt/
 +-- 12_glossary/
```

Cada seccion contiene:
```
0X_nombre_seccion/
+-- original/ (archivos fuente .md del repo arc42)
+-- traduccion/ (archivos .rst traducidos)
+-- figuras/ (imagenes)
+-- diagramas/ (diagramas especificos)
+-- glosario_seccion.rst (terminos de esta seccion)
+-- notas_traduccion.rst (decisiones tomadas)
+-- analisis_seccion.json (output de analizar_seccion.py)
```

## Las 12 Secciones

### 01. Introduction and Goals

CONTENIDO:
- Proposito del sistema
- Stakeholders principales
- Objetivos de calidad top 3-5
- Contexto de negocio

PREGUNTAS QUE RESPONDE:
- Que problema resuelve el sistema?
- Quienes son los stakeholders?
- Cuales son los requisitos de calidad mas importantes?

UBICACION: sections/01_introduction_goals/

### 02. Constraints

CONTENIDO:
- Restricciones organizacionales (procesos, recursos, tiempo)
- Restricciones tecnicas (tecnologias, plataformas, estandares)
- Convenciones obligatorias

PREGUNTAS QUE RESPONDE:
- Que restricciones limitan las decisiones arquitectonicas?
- Que convenciones deben seguirse?

UBICACION: sections/02_constraints/

### 03. Context and Scope

CONTENIDO:
- Contexto de negocio (actores externos, sistemas externos)
- Contexto tecnico (interfaces tecnicas)
- Delimitacion del sistema (que esta dentro, que fuera)

PREGUNTAS QUE RESPONDE:
- Como se comunica el sistema con su entorno?
- Cuales son los limites del sistema?

UBICACION: sections/03_context_scope/

### 04. Solution Strategy

CONTENIDO:
- Decisiones arquitectonicas fundamentales
- Estrategia general de solucion
- Como se alcanzan los objetivos de calidad

PREGUNTAS QUE RESPONDE:
- Cual es el enfoque arquitectonico principal?
- Como se satisfacen los requisitos clave?

UBICACION: sections/04_solution_strategy/

### 05. Building Blocks View

CONTENIDO:
- Descomposicion estatica del sistema
- Jerarquia de componentes (whitebox/blackbox)
- Responsabilidades de cada componente
- Interfaces entre componentes

PREGUNTAS QUE RESPONDE:
- Cuales son los bloques de construccion principales?
- Como se relacionan entre si?

UBICACION: sections/05_building_blocks/

### 06. Runtime View

CONTENIDO:
- Comportamiento en tiempo de ejecucion
- Escenarios importantes (casos de uso dinamicos)
- Flujos de control y datos
- Secuencias de interaccion

PREGUNTAS QUE RESPONDE:
- Como se comporta el sistema en ejecucion?
- Cuales son los flujos importantes?

UBICACION: sections/06_runtime_view/

### 07. Deployment View

CONTENIDO:
- Infraestructura fisica o virtual
- Mapeo de software a hardware
- Distribucion y topologia
- Canales de comunicacion

PREGUNTAS QUE RESPONDE:
- Donde se ejecuta el sistema?
- Como se distribuyen los componentes?

UBICACION: sections/07_deployment_view/

### 08. Crosscutting Concepts

CONTENIDO:
- Conceptos transversales (aplicables a multiples partes)
- Patrones de diseno aplicados
- Reglas y principios generales
- Aspectos tecnicos recurrentes

PREGUNTAS QUE RESPONDE:
- Que conceptos se aplican en todo el sistema?
- Que patrones se usan consistentemente?

UBICACION: sections/08_crosscutting_concepts/

### 09. Architecture Decisions

CONTENIDO:
- ADRs (Architecture Decision Records)
- Decisiones importantes y sus razones
- Alternativas consideradas
- Consecuencias

PREGUNTAS QUE RESPONDE:
- Por que se tomo cada decision arquitectonica importante?
- Que alternativas se consideraron?

UBICACION: sections/09_architecture_decisions/

### 10. Quality Requirements

CONTENIDO:
- Escenarios de calidad concretos
- Arbol de calidad (quality tree)
- Requisitos de calidad cuantificados
- Metricas relevantes

PREGUNTAS QUE RESPONDE:
- Como se definen y miden los requisitos de calidad?
- Que escenarios validan la calidad?

UBICACION: sections/10_quality_requirements/

### 11. Risks and Technical Debt

CONTENIDO:
- Riesgos identificados
- Probabilidad e impacto
- Deuda tecnica conocida
- Estrategias de mitigacion

PREGUNTAS QUE RESPONDE:
- Que riesgos existen?
- Donde esta la deuda tecnica?

UBICACION: sections/11_risks_technical_debt/

### 12. Glossary

CONTENIDO:
- Terminologia del dominio
- Definiciones de terminos tecnicos
- Acronimos y abreviaciones

PREGUNTAS QUE RESPONDE:
- Que significa cada termino del dominio?

UBICACION: sections/12_glossary/

## Proceso de Traduccion arc42

### Fase 1: Obtencion del Original

```bash
# Si aun no esta en original/
# Obtener del repositorio oficial arc42
git clone https://github.com/arc42/arc42-template.git
```

### Fase 2: Analisis

```bash
python scripts/analizar_seccion.py \
 source/biblioteca/arc42/sections/XX_nombre_seccion/
```

Output: analisis_seccion.json con:
- Lista de archivos
- Jerarquia de headings
- Elementos especiales
- Estadisticas

### Fase 3: Traduccion

Usar modo ALTA FIDELIDAD (preservar estructura exacta):

```bash
python scripts/traduccion/arc42_scraper_python.py \
 --section XX \
 --mode alta_fidelidad \
 --output source/biblioteca/arc42/sections/XX_nombre_seccion/traduccion/
```

### Fase 4: Metadata

Generar metadata para cada archivo traducido:

```rst
.. meta::
 :description: [Seccion XX de arc42]
 :keywords: arc42, arquitectura, [seccion]

:Documento Original: https://arc42.org/section/XX
:Modo de Traduccion: Alta Fidelidad
:Framework: arc42
:Seccion: XX
:Fecha Traduccion: YYYY-MM-DD
```

### Fase 5: Integracion

1. Actualizar glosario_acumulativo.rst
2. Actualizar index.rst de arc42
3. Agregar cross-references entre secciones
4. Validar build

## Metadata de Libro

Archivo: source/biblioteca/arc42/metadata_libro.rst

Contiene:
- Informacion del libro completo
- Progreso de traduccion por seccion
- Decisiones globales
- Referencias al repositorio original

## Glosario Acumulativo

Archivo: source/biblioteca/arc42/glosario_acumulativo.rst

Consolida terminos de todas las secciones:

```rst
Glosario Acumulativo arc42
===========================

.. glossary::

 ADR
 Architecture Decision Record. Documento que captura una
 decision arquitectonica importante.

 Seccion: 09

 Building Block
 Componente o modulo del sistema.

 Seccion: 05

 Constraint
 Restriccion que limita decisiones arquitectonicas.

 Seccion: 02
```

## Scripts Especificos para arc42

### arc42_scraper_python.py

Script especializado para extraer y traducir secciones arc42.

USO:
```bash
python scripts/traduccion/arc42_scraper_python.py \
 --section <numero_seccion> \
 --mode <modo> \
 --output <directorio_destino>
```

PARAMETROS:
- section: Numero de seccion (01-12)
- mode: Modo de traduccion (recomendar alta_fidelidad)
- output: Directorio de salida

### analizar_seccion.py

Analiza estructura de cualquier seccion.

USO PARA ARC42:
```bash
python scripts/analizar_seccion.py \
 source/biblioteca/arc42/sections/02_constraints/
```

## Convenciones arc42 en ADT

### Nomenclatura

SECCIONES: XX_nombre_seccion/ (numero con cero padding)
ARCHIVOS ORIGINALES: Conservar nombres del repo arc42
ARCHIVOS TRADUCIDOS: Mismo nombre con extension .rst

### Estructura de Archivos

PREFERENCIA: Un archivo por subseccion importante

MALO:
```
traduccion/
+-- seccion_completa.rst (todo en un archivo)
```

BIEN:
```
traduccion/
+-- index.rst (overview)
+-- subseccion_1.rst
+-- subseccion_2.rst
+-- subseccion_3.rst
```

### Cross-References

Entre secciones arc42:

```rst
.. seealso::

 Restricciones relacionadas en :doc:`../02_constraints/index`

 Decisiones que afectan esto en :doc:`../09_architecture_decisions/index`
```

## Ejemplo Completo: Seccion 02

```
02_constraints/
+-- original/ (del repo arc42)
| +-- 02-constraint-example-1.md
| +-- 2016-03-01-t-2-1.md (tip 2-1)
| +-- 2016-03-01-t-2-2.md (tip 2-2)
| +-- 2016-03-01-t-2-3.md (tip 2-3)
| +-- 2016-03-01-t-2-4.md (tip 2-4)
| +-- 2016-03-01-t-2-5.md (tip 2-5)
| +-- README.md
|
+-- traduccion/ (generado por traduccion)
| +-- index.rst (overview de la seccion)
| +-- restricciones_organizacionales.rst
| +-- restricciones_tecnicas.rst
| +-- convenciones.rst
| +-- ejemplos.rst
|
+-- figuras/ (si aplica)
+-- diagramas/ (si aplica)
|
+-- glosario_seccion.rst (terminos de esta seccion)
+-- notas_traduccion.rst (decisiones tomadas)
+-- analisis_seccion.json (output analisis)
```

## Progreso de Traduccion

Tracking en metadata_libro.rst:

```rst
Progreso de Traduccion
=======================

.. list-table::
 :header-rows: 1

 * - Seccion
 - Estado
 - Archivos
 - Fecha
 * - 01. Introduction and Goals
 - Completado
 - 5/5
 - 2026-01-15
 * - 02. Constraints
 - Completado
 - 6/6
 - 2026-01-28
 * - 03. Context and Scope
 - En Progreso
 - 2/4
 - -
 * - ...
```

## Referencias

arc42 oficial:
- https://arc42.org/
- https://github.com/arc42/arc42-template

Documentacion local:
- source/biblioteca/arc42/metadata_libro.rst
- source/biblioteca/arc42/index.rst

Scripts:
- scripts/traduccion/arc42_scraper_python.py
- scripts/analizar_seccion.py

## Notas Importantes

- arc42 es un TEMPLATE, adaptable a cada proyecto
- Las 12 secciones son OBLIGATORIAS en el template
- Orden de traduccion recomendado: 01 -> 02 -> ... -> 12
- Usar MODO ALTA FIDELIDAD para preservar estructura arc42
- Mantener trazabilidad al repositorio original
- Actualizar glosario_acumulativo.rst con cada seccion
