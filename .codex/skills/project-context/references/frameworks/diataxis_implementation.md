# Implementacion de Diataxis en ADT

Basado en: source/diataxis/

## Que es Diataxis

Diataxis es un framework sistematico para crear documentacion tecnica de calidad, desarrollado por Daniele Procida.

Organiza la documentacion en 4 cuadrantes segun dos ejes:
- EJE HORIZONTAL: Practical steps vs Theoretical knowledge
- EJE VERTICAL: Serving our study vs Serving our work

## Los 4 Cuadrantes

```
 STUDY WORK
 | |
PRACTICAL +--------+--------+ +-------+--------+
STEPS | TUTORIALS | | HOW-TO GUIDES |
 | Learning | | Task-oriented |
 +-----------------+ +----------------+
 | |
THEORETICAL +--------+--------+ +-------+--------+
KNOWLEDGE | EXPLANATION | | REFERENCE |
 | Understanding | | Information |
 +-----------------+ +----------------+
```

## 1. Tutorials (Learning-oriented)

### Proposito

Guiar a un principiante a traves de sus primeros pasos, asegurando exito temprano.

FOCO: Aprendizaje, no objetivos
META: Que el usuario logre HACER algo y sienta confianza

### Caracteristicas

PEDAGOGICO:
- Paso a paso muy claro
- Resultados garantizados
- Sin opciones, un camino claro
- Motivacion y confianza

COMPLETO:
- Todo el contexto necesario
- Sin asumir conocimiento previo
- Explicaciones inline
- Resolucion de problemas comunes

### Ubicacion

source/diataxis/tutorials/

### Estructura Tipica

```rst
Tutorial: Mi Primer [X]
=======================

Objetivos de Aprendizaje
-------------------------

Al completar este tutorial, seras capaz de:

- [ ] Objetivo 1
- [ ] Objetivo 2
- [ ] Objetivo 3

Prerequisitos
-------------

- Requisito 1
- Requisito 2

Tiempo estimado: 30 minutos

Paso 1: Configuracion Inicial
------------------------------

.. note::
 Este paso configura tu entorno. Si encuentras errores,
 consulta la seccion de troubleshooting al final.

[Instrucciones muy claras]

.. code-block:: bash

 comando-exacto-a-ejecutar

**Resultado esperado:**
Deberias ver...

Paso 2: [Siguiente accion]
---------------------------

[Continuar paso a paso]

Verificacion Final
------------------

Verifica que has completado:

- [x] Objetivo 1: Verificacion especifica
- [x] Objetivo 2: Verificacion especifica

Proximos Pasos
--------------

Ahora que dominas [X], puedes:

- Explorar :doc:`../how_to_guides/tarea_avanzada`
- Leer :doc:`../explanation/conceptos_profundos`
```

### Ejemplo Real

Tutorial: Traducir tu Primera Seccion arc42

```rst
Tutorial: Traducir tu Primera Seccion arc42
============================================

Objetivos
---------

- [ ] Comprender workflow de traduccion ADT
- [ ] Traducir seccion 01 de arc42
- [ ] Validar resultado
- [ ] Hacer commit

Tiempo: 45 minutos

Paso 1: Preparar Entorno
-------------------------

.. code-block:: bash

 cd ADT/
 git checkout -b traduccion-arc42-01

Paso 2: Analizar Seccion
-------------------------

.. code-block:: bash

 python scripts/analizar_seccion.py \
 source/biblioteca/arc42/sections/01_introduction_goals/

[Continuar...]
```

## 2. How-to Guides (Task-oriented)

### Proposito

Resolver un problema especifico que el usuario ya enfrenta.

FOCO: Objetivo concreto, no aprendizaje
META: Que el usuario LOGRE su objetivo rapidamente

### Caracteristicas

DIRECTO AL PUNTO:
- Sin explicaciones largas
- Pasos practicos
- Minimo contexto necesario
- Asume conocimiento base

ORIENTADO A RESULTADOS:
- Clara descripcion del objetivo
- Pasos eficientes
- Multiples caminos si aplica
- Troubleshooting inline

### Ubicacion

source/diataxis/how_to_guides/

### Estructura Tipica

```rst
Como [Hacer X]
==============

Problema
--------

Necesitas [descripcion breve del problema]

Solucion
--------

Metodo 1: [Rapido]
~~~~~~~~~~~~~~~~~~

1. Paso 1
2. Paso 2
3. Paso 3

Metodo 2: [Completo]
~~~~~~~~~~~~~~~~~~~~

[Alternativa con mas opciones]

Verificacion
------------

Para confirmar que funciono:

```bash
comando-verificacion
```

Troubleshooting
---------------

Si encuentras [error X]:
- Verificar [Y]
- Ejecutar [Z]
```

### Ejemplo Real

Como Validar Estructura del Proyecto

```rst
Como Validar Estructura del Proyecto
=====================================

Problema
--------

Necesitas verificar que la estructura del proyecto cumple con
REGLAS_ESTRUCTURA_PROYECTO.rst antes de hacer commit.

Solucion Rapida
---------------

```bash
bash scripts/validar_estructura.sh
```

Solucion Completa (con build)
------------------------------

```bash
# Validar estructura
bash scripts/validar_estructura.sh

# Build completo
make clean html

# Validar enlaces
make linkcheck
```

Interpretar Resultados
----------------------

ESTRUCTURA: OK -> Continuar
ESTRUCTURA: ERRORES -> Revisar output para detalles

Si reporta archivos huerfanos:
- Agregar a toctree apropiado
- O mover a ubicacion correcta
```

## 3. Reference (Information-oriented)

### Proposito

Describir el sistema de manera precisa y completa.

FOCO: Informacion exacta
META: Que el usuario ENCUENTRE datos especificos

### Caracteristicas

PRECISION:
- Informacion exacta y verificable
- Sin ambiguedad
- Completitud
- Actualizado

ORGANIZACION:
- Estructura por componentes
- Facil busqueda
- Indices y tablas
- Cross-references

### Ubicacion

source/diataxis/reference/

### Estructura Tipica

```rst
Referencia de [Sistema/Componente]
===================================

Descripcion General
-------------------

[Breve overview neutral]

Componentes
-----------

Component 1
~~~~~~~~~~~

**Proposito:** [Que hace]

**Ubicacion:** [Donde esta]

**Parametros:**

.. list-table::
 :header-rows: 1

 * - Parametro
 - Tipo
 - Descripcion
 - Defecto
 * - param1
 - str
 - [Descripcion]
 - None

**Retorno:** [Que devuelve]

**Ejemplo:**

```python
ejemplo_uso()
```

Component 2
~~~~~~~~~~~

[Similar estructura]

Indice Alfabetico
-----------------

- :ref:`component-1`
- :ref:`component-2`
```

### Ejemplo Real

Referencia de Scripts de Traduccion

```rst
Referencia de Scripts de Traduccion
====================================

Scripts Disponibles
-------------------

adt_translator.py
~~~~~~~~~~~~~~~~~

**Proposito:** Traduccion general siguiendo metodologia ADT

**Ubicacion:** scripts/traduccion/adt_translator.py

**Uso:**

```bash
python scripts/traduccion/adt_translator.py \
 --input <fuente> \
 --output <destino> \
 --mode <modo> \
 --framework <framework>
```

**Parametros:**

.. list-table::
 :header-rows: 1

 * - Parametro
 - Requerido
 - Valores
 - Descripcion
 * - --input
 - Si
 - path
 - Archivo fuente
 * - --output
 - Si
 - path
 - Archivo destino
 * - --mode
 - No
 - alta_fidelidad, marcado_visual, enriquecimiento
 - Modo de traduccion (defecto: alta_fidelidad)
 * - --framework
 - No
 - diataxis, arc42, custom
 - Framework aplicado

**Salida:** Archivo RST en ubicacion especificada

arc42_scraper_python.py
~~~~~~~~~~~~~~~~~~~~~~~

[Similar estructura]
```

## 4. Explanation (Understanding-oriented)

### Proposito

Clarificar y profundizar en conceptos, decisiones y contexto.

FOCO: Comprension del "por que"
META: Que el usuario ENTIENDA profundamente

### Caracteristicas

CONTEXTO E HISTORIA:
- Por que existe esto
- Que problema resuelve
- Alternativas consideradas

PROFUNDIDAD:
- Explicaciones detalladas
- Relaciones entre conceptos
- Trade-offs y decisiones

### Ubicacion

source/diataxis/explanation/

### Estructura Tipica

```rst
Explicacion: [Concepto/Decision]
=================================

Contexto
--------

[Por que este tema es importante]

El Problema
-----------

[Que problema estamos abordando]

Por Que [Decision X]
--------------------

[Explicacion de la decision tomada]

Alternativas Consideradas
--------------------------

Opcion A: [Descripcion]
~~~~~~~~~~~~~~~~~~~~~~~

Ventajas:
- [Pro 1]

Desventajas:
- [Contra 1]

Por que NO: [Razon]

Opcion B: [Descripcion]
~~~~~~~~~~~~~~~~~~~~~~~

[Similar]

Decision Final
--------------

Se eligio [X] porque:

1. [Razon 1]
2. [Razon 2]

Implicaciones
-------------

Esta decision implica:

- [Implicacion 1]
- [Implicacion 2]

Ver Tambien
-----------

- :doc:`../reference/componente_relacionado`
- :doc:`../tutorials/tutorial_aplicacion`
```

### Ejemplo Real

Explicacion: Por Que ADT Usa Tres Modos de Traduccion

```rst
Por Que ADT Usa Tres Modos de Traduccion
=========================================

Contexto
--------

La traduccion documental tecnica no es un proceso uniforme.
Diferentes tipos de contenido requieren diferentes estrategias.

El Problema
-----------

Traduccion tradicional aplica el mismo enfoque a todo tipo de
contenido, resultando en:

- Especificaciones tecnicas "sobre-explicadas"
- Tutoriales demasiado rigidos
- Material de referencia sin contexto

Evolucion del Enfoque
---------------------

Version 1.0: Un Solo Modo
~~~~~~~~~~~~~~~~~~~~~~~~~

Inicialmente usamos solo "traduccion literal".

Problemas:
- Tutoriales poco amigables
- Referencias confusas
- No aprovechaba capacidades de RST

Version 1.5: Dos Modos
~~~~~~~~~~~~~~~~~~~~~~

Agregamos "con enriquecimiento".

Mejora:
- Tutoriales mas claros
- Pero especificaciones se volvieron verbosas

Version 1.7: Tres Modos (Actual)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dividimos en: Alta Fidelidad, Marcado Visual, Enriquecimiento

Resultado:
- Cada contenido recibe tratamiento apropiado
- Mejor usabilidad por tipo
- Flexibilidad manteniendo estandares

Decision Final
--------------

Tres modos porque:

1. Especificaciones requieren precision maxima
2. Tutoriales benefician de guia visual
3. Material conceptual necesita profundizacion
4. Un tamaño NO sirve para todos

Implicaciones
-------------

- Traductores deben DECIDIR modo apropiado
- Metadata debe indicar modo aplicado
- Validacion depende del modo usado

Ver matrices de decision: source/04_reglas_operativas/matrices_decision/
```

## Aplicacion en ADT

### Organizacion del Contenido

FUNDAMENTOS -> Explanation
- Metodologia ADT
- Principios semioticos
- Teoria de transformacion

PROCEDIMIENTOS -> How-to + Tutorials
- Workflows de traduccion
- Guias paso a paso

ESTANDARES -> Reference
- Criterios de calidad
- Terminologia

CASOS PRACTICOS -> Tutorials
- Ejemplos completos
- Ejercicios guiados

GUIAS DE USO -> How-to + Tutorials
- Troubleshooting
- FAQ

REFERENCIAS -> Reference
- Cheatsheets
- Comandos

## Referencias

Diataxis oficial: https://diataxis.fr/

Implementacion local: source/diataxis/

Documentacion sobre organizacion: source/01_fundamentos/

## Notas Importantes

- Diataxis NO es rigido, es un framework
- Contenido puede tener elementos de multiples cuadrantes
- Lo importante es el FOCO principal
- Etiquetar claramente que tipo de documento es
- Respetar expectativas del usuario segun tipo
