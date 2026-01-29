# Comando: sphinx-init-chapter

Inicializa estructura completa de un nuevo capitulo en source/

## Uso

```
sphinx-init-chapter <numero> <nombre> [opciones]
```

## Parametros

### Requeridos

- **numero**: Numero del capitulo (01-99, con cero padding)
- **nombre**: Nombre del capitulo (snake_case, sin espacios)

### Opcionales

- `--framework <diataxis|arc42|custom>`: Framework de organizacion (defecto: custom)
- `--with-metadata`: Incluir directorio _metadata/
- `--dry-run`: Mostrar que haria sin ejecutar

## Ejemplos

### Capitulo Simple

```bash
sphinx-init-chapter 11 nuevos_conceptos
```

Crea:
```
source/11_nuevos_conceptos/
+-- index.rst
+-- intro.rst
+-- _metadata/
```

### Capitulo con Diataxis

```bash
sphinx-init-chapter 12 tutoriales_avanzados --framework diataxis
```

Crea:
```
source/12_tutoriales_avanzados/
+-- index.rst
+-- tutorials/
| +-- index.rst
+-- how_to_guides/
| +-- index.rst
+-- reference/
| +-- index.rst
+-- explanation/
| +-- index.rst
+-- _metadata/
```

### Capitulo arc42

```bash
sphinx-init-chapter 13 arquitectura_proyecto --framework arc42
```

Crea:
```
source/13_arquitectura_proyecto/
+-- index.rst
+-- 01_introduction_goals/
+-- 02_constraints/
+-- ... (12 subdirectorios)
+-- _metadata/
```

### Dry Run

```bash
sphinx-init-chapter 11 nuevos_conceptos --dry-run
```

Muestra:
```
DRY RUN - No se ejecutaran cambios

Se crearian:
- source/11_nuevos_conceptos/
- source/11_nuevos_conceptos/index.rst
- source/11_nuevos_conceptos/intro.rst
- source/11_nuevos_conceptos/_metadata/

Se modificaria:
- source/index.rst (agregar a toctree)
```

## Proceso Completo

### 1. Validacion de Parametros

Valida que:
- Numero este en rango 01-99
- Nombre sea snake_case valido
- Directorio no exista ya

Si algun parametro invalido:
```
ERROR: Numero debe estar entre 01 y 99
ERROR: Nombre debe ser snake_case sin espacios
ERROR: Directorio source/11_nuevos_conceptos/ ya existe
```

### 2. Creacion de Estructura

Segun framework:

**CUSTOM (defecto):**
```
XX_nombre/
+-- index.rst
+-- intro.rst
+-- _metadata/
 +-- original.rst
```

**DIATAXIS:**
```
XX_nombre/
+-- index.rst
+-- tutorials/
| +-- index.rst
+-- how_to_guides/
| +-- index.rst
+-- reference/
| +-- index.rst
+-- explanation/
| +-- index.rst
+-- _metadata/
```

**ARC42:**
```
XX_nombre/
+-- index.rst
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
+-- _metadata/
```

### 3. Generacion de index.rst

Template para capitulo custom:

```rst
===================
[Titulo del Capitulo]
===================

:Capitulo: [Numero]
:Autor: [Auto-detectado o "Sistema"]
:Fecha Creacion: [YYYY-MM-DD]
:Actualizacion: [YYYY-MM-DD]

.. toctree::
 :maxdepth: 2
 :caption: Contenido

 intro

Introduccion
============

Este capitulo cubre [descripcion placeholder].

Ver :doc:`intro` para comenzar.
```

Template para Diataxis:

```rst
===================
[Titulo del Capitulo]
===================

Este capitulo organiza contenido segun framework Diataxis.

.. toctree::
 :maxdepth: 2
 :caption: Tipos de Contenido

 tutorials/index
 how_to_guides/index
 reference/index
 explanation/index

Ver :doc:`../diataxis/index` para entender la organizacion.
```

### 4. Creacion de intro.rst

```rst
Introduccion
============

[Contenido placeholder para intro.rst]

Descripcion general del capitulo [nombre].

Objetivos
---------

- Objetivo 1
- Objetivo 2

Estructura
----------

Este capitulo esta organizado en:

1. Seccion 1
2. Seccion 2

Prerequisitos
-------------

- [Prerequisito 1]

Referencias
-----------

- :doc:`../01_fundamentos/index`
```

### 5. Creacion de _metadata/

Si `--with-metadata` o por defecto:

```rst
Metadata del Capitulo [Numero]
===============================

:Capitulo: [Numero]
:Nombre: [Nombre]
:Framework: [Framework]
:Fecha Creacion: [YYYY-MM-DD]
:Estado: Draft

Informacion General
-------------------

Proposito
~~~~~~~~~

[Descripcion del proposito del capitulo]

Alcance
~~~~~~~

[Que incluye y que no incluye]

Audiencia
~~~~~~~~~

[Para quien esta dirigido]

Historia
--------

[Historial de cambios importantes]
```

### 6. Actualizacion de source/index.rst

Agrega al toctree principal:

```rst
.. toctree::
 :maxdepth: 2
 :caption: Capitulos

 01_fundamentos/index
 02_procedimientos/index
 ...
 10_apendices/index
 11_nuevos_conceptos/index # NUEVO
```

### 7. Validacion de Build

Ejecuta:
```bash
make html
```

Verifica:
- Exit code 0
- Sin errores de build
- Nuevo capitulo en HTML generado

### 8. Reporte de Resultados

```
CAPITULO INICIALIZADO

Numero: 11
Nombre: nuevos_conceptos
Framework: custom
Ubicacion: source/11_nuevos_conceptos/

Archivos creados:
- source/11_nuevos_conceptos/index.rst
- source/11_nuevos_conceptos/intro.rst
- source/11_nuevos_conceptos/_metadata/original.rst

Archivos modificados:
- source/index.rst (toctree actualizado)

Build: EXITOSO
HTML generado: build/html/11_nuevos_conceptos/index.html

PROXIMOS PASOS:
1. Editar source/11_nuevos_conceptos/index.rst
2. Agregar contenido en source/11_nuevos_conceptos/
3. Actualizar metadata segun necesidad
4. Commit:
 git add source/11_nuevos_conceptos/ source/index.rst
 git commit -m "feat(estructura): agregar capitulo 11 nuevos_conceptos"
```

## Manejo de Errores

### Error: Directorio Existe

```
ERROR: Directorio source/11_nuevos_conceptos/ ya existe

Opciones:
1. Usar numero diferente
2. Eliminar directorio existente (CUIDADO)
3. Renombrar directorio existente
```

### Error: Numero Invalido

```
ERROR: Numero debe ser 01-99 con cero padding

Ejemplos validos:
- 01, 02, ..., 09, 10, 11, ..., 99

Ejemplos INVALIDOS:
- 1 (falta cero padding)
- 100 (fuera de rango)
- abc (no es numero)
```

### Error: Nombre Invalido

```
ERROR: Nombre debe ser snake_case sin espacios

Ejemplos validos:
- nuevos_conceptos
- arquitectura_sistemas
- tutoriales_avanzados

Ejemplos INVALIDOS:
- Nuevos Conceptos (espacios, mayusculas)
- nuevos-conceptos (kebab-case)
- nuevosConceptos (camelCase)
```

### Error: Build Falla

```
WARNING: Build fallo despues de crear capitulo

Posibles causas:
1. Toctree mal formado
2. Referencias rotas
3. Sintaxis RST incorrecta

Accion:
1. Revisar output de make html
2. Corregir errores
3. Re-ejecutar make html
```

## Scripts Relacionados

- scripts/init_capitulo.sh (si existe, este comando lo usa)
- scripts/validar_estructura.sh (para validar resultado)

## Referencias

- REGLAS_ESTRUCTURA_PROYECTO.rst
- source/docs_maestros/
- Skill: project-context

## Notas

- Siempre crear desde raiz del proyecto (ADT/)
- Validar build despues de creacion
- Commit estructura antes de agregar contenido
- Preferir numeros secuenciales (11, 12, 13...)
- Respetar convenciones de nomenclatura del proyecto
