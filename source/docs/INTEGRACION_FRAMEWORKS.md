# GUÍA DE INTEGRACIÓN ADT
## Arc42 + Diátaxis + Traducción en un Solo Proyecto

Versión: 1.0.0
Fecha: 2026-01-25

---

## [TARGET] OBJETIVO

Esta guía muestra cómo integrar los tres frameworks del sistema ADT en un proyecto real de documentación técnica traducida.

---

## [TABLE] CASO DE USO: Traducción de Libro "Modern Full-Stack Development"

### CONTEXTO

- **Libro Original:** Modern Full-Stack Development (Zammetti, 2nd Ed)
- **Idioma:** Inglés -> Español Mexicano
- **Formato Original:** PDF
- **Formato Destino:** Sphinx/reStructuredText
- **Público:** Desarrolladores full-stack hispanohablantes

### FRAMEWORKS APLICADOS

1. **arc42** -> Documentar la arquitectura del proyecto de traducción
2. **Diátaxis** -> Organizar tipos de documentación generada
3. **Traducción** -> Procedimientos de traducción técnica

---

## ESTRUCTURA INTEGRADA

```
biblioteca/informatica/programacion/full_stack/
+-- Modern_Full_Stack_Development_Zammetti_2ed/
 |
 +-- arc42/ <- DOCUMENTACIÓN ARQUITECTÓNICA
 | +-- 01_introduction_goals/
 | | +-- project_goals.rst (Objetivos del proyecto de traducción)
 | +-- 03_context/
 | | +-- translation_context.rst (Contexto: libro técnico -> documentación web)
 | +-- 04_solution_strategy/
 | | +-- translation_strategy.rst (Estrategia: alta fidelidad + marcado visual)
 | +-- 08_concepts/
 | | +-- glossary_management.rst (Gestión de glosarios)
 | | +-- term_marking.rst (Sistema de marcado de términos)
 | +-- 09_decisions/
 | | +-- ADR-001-use-sphinx.rst
 | | +-- ADR-002-alta-fidelidad.rst
 | | +-- ADR-003-marcado-visual.rst
 | +-- 11_risks_tech_debt/
 | +-- TDR-001-capitulos-sin-terminar.rst
 | +-- RISK-001-inconsistencia-terminologica.rst
 |
 +-- diataxis/ <- DOCUMENTACIÓN POR PROPÓSITO
 | +-- tutorials/
 | | +-- getting_started_fullstack.rst (Tutorial: Primeros pasos)
 | +-- how_to_guides/
 | | +-- setup_node_environment.rst (Cómo configurar Node)
 | | +-- create_react_app.rst (Cómo crear app React)
 | | +-- deploy_docker.rst (Cómo desplegar con Docker)
 | +-- reference/
 | | +-- npm_commands.rst (Referencia de comandos NPM)
 | | +-- react_hooks.rst (Referencia de React Hooks)
 | | +-- docker_commands.rst (Referencia de comandos Docker)
 | +-- explanation/
 | +-- fullstack_architecture.rst (Explicación: Arquitectura)
 | +-- react_ecosystem.rst (Explicación: Ecosistema React)
 | +-- typescript_benefits.rst (Explicación: Beneficios de TS)
 |
 +-- traduccion/ <- CONTENIDO TRADUCIDO ORIGINAL
 | +-- Chapter_01_Server_Side_Action/
 | | +-- original/chapter_01.pdf
 | | +-- traduccion/capitulo_01.rst
 | | +-- glosario_capitulo.rst
 | | +-- figuras/
 | +-- Chapter_02_Advanced_Node_NPM/
 | +-- Chapter_03_Client_Side_React/
 | +-- [...14 capítulos total...]
 | +-- glosario_acumulativo.rst
 |
 +-- metadata_libro.rst <- METADATOS
 +-- index.rst <- ÍNDICE PRINCIPAL
 +-- conf.py <- CONFIGURACIÓN SPHINX
```

---

## [LIST] FLUJO DE TRABAJO INTEGRADO

### FASE 1: PLANIFICACIÓN (arc42)

**Documento: arc42/01_introduction_goals/project_goals.rst**

```rst
==========================================
Objetivos del Proyecto de Traducción
==========================================

**Objetivo Principal:**
Traducir "Modern Full-Stack Development" al español mexicano,
creando una experiencia de aprendizaje completa para desarrolladores
hispanohablantes.

**Quality Goals:**

1. **Fidelidad Técnica** (Prioridad: Crítica)
 - Preservar 100% de conceptos técnicos
 - Mantener exactitud de ejemplos de código
 - Conservar estructura del libro original

2. **Accesibilidad** (Prioridad: Alta)
 - Terminología en español sin perder precisión técnica
 - Marcado visual de términos en primera aparición
 - Glosario acumulativo navegable

3. **Navegabilidad** (Prioridad: Alta)
 - Sistema de referencias cruzadas funcional
 - Búsqueda en español efectiva
 - Tabla de contenidos jerárquica

**Stakeholders:**

.. list-table::
 :header-rows: 1

 * - Rol
 - Expectativa
 * - Desarrolladores hispanohablantes
 - Contenido técnico preciso y comprensible
 * - Instructores
 - Material didáctico en español
 * - Traductores futuros
 - Metodología documentada y replicable
```

### FASE 2: DECISIONES ARQUITECTÓNICAS (arc42)

**Documento: arc42/09_decisions/ADR-002-alta-fidelidad.rst**

```rst
ADR-002: Modo de Traducción de Alta Fidelidad
==============================================

**Status:** Accepted
**Date:** 2026-01-25
**Decision Makers:** Equipo de Traducción

**Context:**
Necesitamos decidir el modo de traducción para el libro técnico.
Opciones disponibles:
- Alta fidelidad (preservación estricta)
- Adaptación cultural (modificación de contenido)
- Traducción libre (reescritura)

**Decision:**
Usar **Modo de Alta Fidelidad** con Marcado Visual.

**Rationale:**
1. El contenido es técnico y didáctico
2. Los ejemplos de código deben preservarse exactamente
3. La estructura del libro es pedagógicamente efectiva
4. Los lectores necesitan términos técnicos precisos

**Consequences:**

**Positivas:**
+ Máxima fidelidad al contenido original
+ Términos técnicos preservados correctamente
+ Referencias cruzadas funcionales
+ Reproducibilidad del contenido

**Negativas:**
- Mayor esfuerzo de traducción
- Texto más denso en algunos casos
- Requiere glosario exhaustivo

**Compliance:**
- STD_001: Estándares de terminología
- PROC_002: Procedimiento alta fidelidad
- RT_001: Regla de primera aparición
```

### FASE 3: TRADUCCIÓN (Procedimientos)

**Aplicar: traduccion/source/02_procedimientos/modo_alta_fidelidad/**

```rst
Checklist por Capítulo:

[OK] Paso 1: Extraer texto de PDF original
[OK] Paso 2: Identificar términos técnicos (187 términos en Cap 1)
[OK] Paso 3: Crear glosario del capítulo
[OK] Paso 4: Traducir texto preservando estructura
[OK] Paso 5: Marcar primera aparición de cada término
[OK] Paso 6: Convertir a reStructuredText
[OK] Paso 7: Agregar directivas Sphinx (.. note::, .. code-block::)
[OK] Paso 8: Verificar referencias cruzadas
[OK] Paso 9: Prueba de compilación (make html)
[OK] Paso 10: Revisión técnica
```

### FASE 4: ORGANIZACIÓN POR TIPO (Diátaxis)

**Generar contenido derivado según tipo:**

#### Tutorial (learning-oriented)

**Archivo: diataxis/tutorials/getting_started_fullstack.rst**

```rst
=========================================
Tutorial: Primeros Pasos con Full-Stack
=========================================

**Tiempo estimado:** 30 minutos
**Nivel:** Principiante
**Prerequisitos:** Conocimientos básicos de JavaScript

Este tutorial te guiará paso a paso en la creación de tu primera
aplicación full-stack usando las tecnologías del libro.

Paso 1: Instalar Node.js
-------------------------

1. Ve a https://nodejs.org
2. Descarga la versión LTS
3. Ejecuta el instalador
4. Verifica la instalación:

 .. code-block:: bash

 node --version
 npm --version

[...pasos siguientes...]

**Lo que aprendiste:**
- Configurar entorno Node.js
- Crear proyecto con NPM
- Ejecutar primer servidor
- Hacer tu primera petición HTTP

**Siguiente paso:**
Ve al tutorial :doc:`react_first_component` para crear tu primer
componente React.
```

#### How-To Guide (goal-oriented)

**Archivo: diataxis/how_to_guides/deploy_docker.rst**

```rst
===============================
Cómo Desplegar con Docker
===============================

**Objetivo:** Desplegar tu aplicación full-stack usando Docker
**Tiempo:** 15 minutos
**Prerequisitos:** Docker instalado

Pasos
-----

1. **Crear Dockerfile:**

 .. code-block:: docker

 FROM node:16
 WORKDIR /app
 COPY package*.json ./
 RUN npm install
 COPY . .
 EXPOSE 3000
 CMD ["npm", "start"]

2. **Construir imagen:**

 .. code-block:: bash

 docker build -t mi-app .

3. **Ejecutar contenedor:**

 .. code-block:: bash

 docker run -p 3000:3000 mi-app

4. **Verificar:**

 Abre http://localhost:3000

**Ver también:**
- :doc:`../reference/docker_commands` - Referencia completa de Docker
- :doc:`../explanation/container_benefits` - Por qué usar contenedores
```

#### Reference (information-oriented)

**Archivo: diataxis/reference/npm_commands.rst**

```rst
===========================
Referencia de Comandos NPM
===========================

Esta es la referencia completa de comandos NPM mencionados en el libro.

.. glossary::

 npm init
 Inicializa un nuevo proyecto Node.js

 **Sintaxis:**

 .. code-block:: bash

 npm init [--yes]

 **Opciones:**

 - ``--yes`` / ``-y``: Acepta todos los valores por defecto

 **Ejemplo:**

 .. code-block:: bash

 npm init --yes

 npm install
 Instala dependencias del proyecto

 **Sintaxis:**

 .. code-block:: bash

 npm install [paquete][@versión] [opciones]

 **Opciones:**

 - ``--save`` / ``-S``: Guardar en dependencies
 - ``--save-dev`` / ``-D``: Guardar en devDependencies
 - ``--global`` / ``-g``: Instalación global

 **Ejemplos:**

 .. code-block:: bash

 npm install express
 npm install -D jest
 npm install -g typescript

[...más comandos...]

**Ver también:**
- Documentación oficial: https://docs.npmjs.com
- :doc:`../how_to_guides/manage_dependencies` - Gestionar dependencias
```

#### Explanation (understanding-oriented)

**Archivo: diataxis/explanation/fullstack_architecture.rst**

```rst
=========================================
Explicación: Arquitectura Full-Stack
=========================================

¿Qué es Full-Stack?
-------------------

El término :term:`full-stack` se refiere al conjunto completo de tecnologías
necesarias para construir una aplicación web moderna. Tradicionalmente,
se divide en dos grandes áreas:

**Frontend (Cliente):**
 La parte de la aplicación que se ejecuta en el navegador del usuario.
 Incluye:

 - HTML/CSS para estructura y presentación
 - JavaScript para interactividad
 - Frameworks como React para gestión de estado

**Backend (Servidor):**
 La parte que se ejecuta en el servidor. Incluye:

 - API para comunicación con el frontend
 - Lógica de negocio
 - Acceso a bases de datos
 - Autenticación y autorización

Arquitectura del Libro
-----------------------

Este libro sigue una arquitectura específica que combina:

.. mermaid::

 graph TB
 A[Cliente React] -->|HTTP| B[API Node.js]
 B -->|Query| C[Base de Datos]
 D[TypeScript] -->|Compila| A
 D -->|Compila| B
 E[Webpack] -->|Empaqueta| A
 F[Docker] -->|Contiene| B
 F -->|Contiene| C

**Decisiones arquitectónicas clave:**

1. **TypeScript en lugar de JavaScript puro**

 - Tipado estático reduce errores
 - Mejor experiencia de desarrollo (IDE)
 - Código más mantenible

2. **React en lugar de otros frameworks**

 - Ecosistema maduro
 - Gran comunidad
 - Componentes reutilizables

3. **Node.js en backend**

 - Mismo lenguaje frontend/backend (JavaScript)
 - Event-driven non-blocking I/O
 - NPM ecosystem

4. **Docker para deployment**

 - Entornos consistentes
 - Fácil escalabilidad
 - Portabilidad

**Por qué esta arquitectura funciona:**

Esta combinación de tecnologías proporciona:

[OK] **Consistencia:** JavaScript en todo el stack
[OK] **Modernidad:** Herramientas state-of-the-art
[OK] **Escalabilidad:** Arquitectura probada en producción
[OK] **Productividad:** Reutilización de código y conocimiento

**Ver también:**
- :doc:`../tutorials/getting_started_fullstack` - Empezar con esta arquitectura
- :doc:`../reference/tech_stack` - Referencia completa del stack
```

---

## [LINK] MAPEO COMPLETO

### arc42 -> Diátaxis

| arc42 Sección | Genera Diátaxis Tipo | Ejemplo |
|---------------|----------------------|---------|
| 01 Introduction & Goals | Explanation | Explicación de objetivos del proyecto |
| 03 Context | Explanation | Explicación del contexto técnico |
| 04 Solution Strategy | Explanation | Explicación de estrategia general |
| 05 Building Blocks | Reference | Referencia de componentes |
| 06 Runtime View | How-To Guide | Cómo ejecutar escenarios |
| 07 Deployment | How-To Guide | Cómo desplegar sistema |
| 08 Concepts | Explanation | Explicación de conceptos crosscutting |
| 09 Decisions (ADRs) | Explanation | Explicación de decisiones |
| 10 Quality | Reference | Referencia de requisitos de calidad |
| 12 Glossary | Reference | Referencia de términos |

### Traducción -> Diátaxis

| Contenido Traducido | Genera Diátaxis Tipo | Ejemplo |
|---------------------|----------------------|---------|
| Capítulo tutorial (ej: Cap 1 Node) | Tutorial | Getting Started with Node |
| Sección procedimiento | How-To Guide | How to Install NPM |
| Referencia técnica | Reference | NPM Commands Reference |
| Sección conceptual | Explanation | Understanding Event Loop |

---

## [INFO] BENEFICIOS DE LA INTEGRACIÓN

### 1. Trazabilidad Completa

```
Decisión de diseño (arc42/ADR)
 v
Procedimiento aplicado (traduccion/PROC)
 v
Contenido generado (traduccion/Chapter_XX)
 v
Documentación derivada (diataxis/tipo)
```

### 2. Múltiples Vistas del Mismo Contenido

**Mismo tema "Node.js" en diferentes formas:**

- **Tutorial:** Primeros pasos con Node (learning)
- **How-To:** Instalar Node en diferentes OS (goal)
- **Reference:** API de Node (information)
- **Explanation:** ¿Qué es Node y por qué usarlo? (understanding)

### 3. Gestión de Calidad Estructurada

**arc42 Section 11 (Risks & Technical Debt):**

```rst
TDR-001: Capítulos 6-14 Sin Terminar
-------------------------------------

**Status:** Active
**Priority:** High
**Impact:** Proyecto incompleto

**Description:**
Solo capítulos 1-5 traducidos (35% del libro)

**Consequences:**
- Experiencia de aprendizaje incompleta
- Referencias cruzadas rotas a capítulos posteriores

**Plan:**
1. Completar Cap 6 (fecha: 2026-02-15)
2. Completar Cap 7-8 (fecha: 2026-03-15)
3. Completar Cap 9-14 (fecha: 2026-04-30)

**Owner:** Equipo de Traducción
```

---

## [START] CÓMO USAR ESTA INTEGRACIÓN

### Paso 1: Crear Estructura

```bash
cd /tmp/ADT
./scripts/utils/create_book_structure.sh \
 "biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed"
```

### Paso 2: Documentar con arc42

```bash
# Crear objetivos del proyecto
nvim biblioteca/.../arc42/01_introduction_goals/project_goals.rst

# Documentar decisiones
nvim biblioteca/.../arc42/09_decisions/ADR-002-alta-fidelidad.rst
```

### Paso 3: Traducir Aplicando Procedimientos

```bash
# Traducir capítulo 1
./scripts/traduccion/translate_chapter.sh \
 original/chapter_01.pdf \
 traduccion/Chapter_01_Server_Side_Action/
```

### Paso 4: Generar Documentación Diátaxis

```bash
# Extraer tutorial del capítulo traducido
./scripts/diataxis/generate_tutorial.sh \
 traduccion/Chapter_01_Server_Side_Action/capitulo_01.rst \
 diataxis/tutorials/getting_started_node.rst
```

### Paso 5: Build Todo

```bash
cd biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed
make html
```

---

## [TABLE] RESULTADO FINAL

**Sitio web generado con:**

- **Documentación arquitectónica** (arc42)
 - Objetivos del proyecto
 - Decisiones de diseño
 - Conceptos clave
 - Riesgos y deuda técnica

- **Libro traducido** (traducción)
 - 14 capítulos en español
 - Glosario acumulativo
 - Referencias cruzadas funcionales

- **Documentación derivada** (Diátaxis)
 - 10+ tutoriales paso a paso
 - 20+ guías how-to
 - Referencias completas
 - Explicaciones conceptuales

**TODO navegable desde un solo sitio Sphinx**

---

**¿Listo para aplicar?** Ve a `/tmp/ADT` y empieza tu proyecto integrado.
