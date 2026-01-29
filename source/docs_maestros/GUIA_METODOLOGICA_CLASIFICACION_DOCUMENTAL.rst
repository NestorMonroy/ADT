==================================================================================
Guía Metodológica de Clasificación Documental
==================================================================================

:Código: META_BIB_001
:Versión: 1.0.0
:Fecha: 2026-01-28
:Estado: NORMATIVO
:Ámbito: Biblioteca de Documentos Traducidos ADT
:Autor: Sistema ADT
:Base: ISO 12620-2:2022, Dewey Decimal Classification

.. contents:: Tabla de Contenido
 :depth: 4
 :local:

----

Resumen Ejecutivo
=================

Esta guía establece el **sistema de clasificación jerárquica** para organizar
libros técnicos traducidos en el proyecto ADT. Define categorías, subcategorías,
especialidades y códigos de clasificación que garantizan una organización consistente
y escalable de la biblioteca.

**Propósito Principal:**
 Proporcionar una metodología sistemática para clasificar cualquier documento
 técnico nuevo, asignándole una ubicación única y predecible en la jerarquía
 de ``/biblioteca``.

**Usuarios Objetivo:**
 - Traductores que organizan nuevos libros
 - Administradores de la biblioteca
 - Desarrolladores de herramientas de automatización
 - Usuarios que buscan documentos específicos

----

Parte 1: Fundamentos de Clasificación
======================================

1.1. Objetivo del Sistema de Clasificación
-------------------------------------------

El sistema de clasificación documental ADT busca:

1. **Organización Lógica:**
 Agrupar documentos por área de conocimiento, facilitando la navegación

2. **Escalabilidad:**
 Soportar crecimiento ilimitado de la biblioteca sin reestructuración

3. **Consistencia:**
 Garantizar que dos traductores clasifiquen el mismo libro de manera idéntica

4. **Búsqueda Eficiente:**
 Permitir localización rápida por código o por navegación jerárquica

5. **Interoperabilidad:**
 Facilitar integración con sistemas externos (catálogos, bases de datos)

1.2. Principios Rectores
-------------------------

**Principio 1: Jerarquía de 4 Niveles**

.. code-block:: text

 Nivel 1: CATEGORÍA -> Informática, Ingeniería, Ciencias
 Nivel 2: SUBCATEGORÍA -> Programación, IA, Redes, Sistemas
 Nivel 3: ESPECIALIDAD -> Full-Stack, Python, React, DevOps
 Nivel 4: LIBRO -> Identificador único secuencial

**Principio 2: Un Solo Camino**

Cada libro tiene **exactamente una ubicación** en la jerarquía.
No se permiten clasificaciones múltiples.

**Principio 3: Códigos Alfanuméricos**

Sistema de códigos basado en abreviaturas nemotécnicas:

.. code-block:: text

 INF.PRG.FST.001
 | | | +-- Número secuencial (001-999)
 | | +----- Especialidad (FST = Full-Stack)
 | +--------- Subcategoría (PRG = Programación)
 +------------- Categoría (INF = Informática)

**Principio 4: Carpeta = Libro Completo**

Cada libro ocupa **una carpeta completa** que contiene:

- Capítulos originales
- Capítulos traducidos
- Metadata
- Glosarios
- Figuras
- Notas de traducción

1.3. Base Teórica
-----------------

El sistema ADT se inspira en:

**Dewey Decimal Classification (DDC):**
 Sistema decimal jerárquico de 10 categorías principales

**Library of Congress Classification (LCC):**
 Notación alfanumérica para bibliotecas académicas

**ISO 12620-2:2022:**
 Gestión de repositorios terminológicos

**Adaptaciones Específicas para ADT:**

1. **Foco en Tecnología:**
 Prioridad a Informática, Ingeniería Software y Ciencias Aplicadas

2. **Granularidad por Especialidad:**
 Nivel adicional para tecnologías específicas (React, Docker, Python)

3. **Multilingüismo:**
 Estructura original + traducción en cada libro

4. **Integración con Traducción:**
 Metadata de progreso, glosarios acumulativos, notas de traducción

----

Parte 2: Taxonomía Completa
============================

2.1. Categorías Principales (Nivel 1)
--------------------------------------

El sistema ADT define **3 categorías principales** expandibles a futuro:

.. list-table:: Categorías Nivel 1
 :header-rows: 1
 :widths: 15 15 70

 * - Código
   - Nombre
   - Ámbito
 * - **INF**
   - Informática
   - Ciencias de la Computación, Programación, IA, Redes, Seguridad
 * - **ING**
   - Ingeniería
   - Ingeniería de Software, Sistemas, Arquitectura, Metodologías
 * - **CIE**
   - Ciencias
   - Ciencias Aplicadas, Matemáticas, Física, Biología Computacional

**Criterios de Clasificación Nivel 1:**

.. code-block:: rst

 ¿El libro trata principalmente de...?

 -> Programación, algoritmos, IA, redes, bases de datos?
 [OK] INFORMÁTICA (INF)

 -> Arquitectura de software, metodologías, procesos de desarrollo?
 [OK] INGENIERÍA (ING)

 -> Matemáticas aplicadas, modelado científico, física computacional?
 [OK] CIENCIAS (CIE)

**Casos Límite:**

- **"Machine Learning" (IA + Matemáticas):** INF (prioridad a aplicación)
- **"Software Architecture" (código + metodología):** ING (prioridad a proceso)
- **"Computational Biology":** CIE (prioridad a dominio científico)

2.2. Subcategorías Informática (Nivel 2)
-----------------------------------------

.. list-table:: Subcategorías INF
 :header-rows: 1
 :widths: 15 20 65

 * - Código
   - Nombre
   - Ámbito y Ejemplos
 * - **PRG**
   - Programación
   - Lenguajes, paradigmas, desarrollo de software

 *Ej: Python, JavaScript, Functional Programming*
 * - **IAR**
   - Inteligencia Artificial
   - Machine Learning, Deep Learning, NLP, Computer Vision

 *Ej: TensorFlow, PyTorch, Neural Networks*
 * - **RED**
   - Redes
   - Protocolos, arquitecturas de red, comunicaciones

 *Ej: TCP/IP, HTTP, Network Security*
 * - **SEG**
   - Seguridad
   - Ciberseguridad, criptografía, ethical hacking

 *Ej: Penetration Testing, Cryptography, Security Audit*
 * - **BDD**
   - Bases de Datos
   - SQL, NoSQL, diseño de esquemas, optimización

 *Ej: PostgreSQL, MongoDB, Database Design*
 * - **SOP**
   - Sistemas Operativos
   - Linux, Windows, administración de sistemas

 *Ej: Linux Kernel, System Administration, Shell Scripting*
 * - **WEB**
   - Desarrollo Web
   - Frontend, Backend, Full-Stack (cuando no cabe en PRG)

 *Ej: HTML5, CSS3, Web APIs (si es genérico)*
 * - **MOV**
   - Desarrollo Móvil
   - iOS, Android, multiplataforma

 *Ej: Swift, Kotlin, React Native*
 * - **DVC**
   - DevOps y Cloud
   - CI/CD, containerización, orquestación, cloud computing

 *Ej: Kubernetes, AWS, Azure, DevOps Practices*
 * - **ALG**
   - Algoritmos
   - Estructuras de datos, algoritmos, complejidad

 *Ej: Data Structures, Algorithm Analysis*

**Expansión Futura:**

El sistema permite agregar nuevas subcategorías según necesidad:

.. code-block:: text

 INF.BCK -> Blockchain y Criptomonedas
 INF.IOT -> Internet of Things
 INF.GAM -> Desarrollo de Videojuegos
 INF.VRA -> Realidad Virtual y Aumentada

2.3. Subcategorías Ingeniería (Nivel 2)
----------------------------------------

.. list-table:: Subcategorías ING
 :header-rows: 1
 :widths: 15 20 65

 * - Código
   - Nombre
   - Ámbito y Ejemplos
 * - **SIS**
   - Sistemas
   - Arquitectura de sistemas, diseño de sistemas complejos

 *Ej: System Design, Distributed Systems*
 * - **ARQ**
   - Arquitectura
   - Arquitectura de software, patrones arquitectónicos

 *Ej: Clean Architecture, Microservices, arc42*
 * - **MET**
   - Metodologías
   - Agile, Scrum, DevOps, metodologías de desarrollo

 *Ej: Scrum Guide, Agile Practices, Lean Software*
 * - **REQ**
   - Requisitos
   - Ingeniería de requisitos, análisis de requisitos

 *Ej: Requirements Engineering, User Stories*
 * - **PRU**
   - Pruebas
   - Testing, QA, automatización de pruebas

 *Ej: Test-Driven Development, Unit Testing, QA*
 * - **MOD**
   - Modelado
   - UML, modelado de procesos, especificación formal

 *Ej: UML Guide, BPMN, Formal Methods*

2.4. Subcategorías Ciencias (Nivel 2)
--------------------------------------

.. list-table:: Subcategorías CIE
 :header-rows: 1
 :widths: 15 20 65

 * - Código
   - Nombre
   - Ámbito y Ejemplos
 * - **MAT**
   - Matemáticas
   - Matemáticas aplicadas, cálculo, álgebra para CS

 *Ej: Linear Algebra for ML, Calculus for CS*
 * - **EST**
   - Estadística
   - Estadística, probabilidad, análisis de datos

 *Ej: Statistical Analysis, Probability Theory*
 * - **FIS**
   - Física
   - Física computacional, simulaciones

 *Ej: Computational Physics, Simulations*
 * - **BIO**
   - Biología
   - Bioinformática, biología computacional

 *Ej: Bioinformatics, Genomics Analysis*

2.5. Especialidades Programación (Nivel 3)
-------------------------------------------

Especialidades más comunes en **INF.PRG**:

.. list-table:: Especialidades INF.PRG
 :header-rows: 1
 :widths: 15 25 60

 * - Código
   - Nombre
   - Descripción
 * - **FST**
   - Full-Stack
   - Desarrollo completo (frontend + backend)
 * - **FRE**
   - Frontend
   - Desarrollo de interfaces de usuario
 * - **BAC**
   - Backend
   - Desarrollo del lado del servidor
 * - **PYT**
   - Python
   - Lenguaje Python (general)
 * - **JAV**
   - JavaScript
   - JavaScript (general, no específico a framework)
 * - **TSC**
   - TypeScript
   - Lenguaje TypeScript
 * - **REA**
   - React
   - Framework React
 * - **VUE**
   - Vue.js
   - Framework Vue
 * - **ANG**
   - Angular
   - Framework Angular
 * - **NOD**
   - Node.js
   - Runtime Node.js y desarrollo backend
 * - **DJA**
   - Django
   - Framework Django (Python)
 * - **FLA**
   - Flask
   - Framework Flask (Python)
 * - **SPR**
   - Spring
   - Framework Spring (Java)
 * - **NET**
   - .NET
   - Plataforma .NET y C#
 * - **RUS**
   - Rust
   - Lenguaje Rust
 * - **GOL**
   - Go
   - Lenguaje Go
 * - **CPP**
   - C++
   - Lenguaje C++
 * - **FUN**
   - Funcional
   - Programación funcional (Haskell, Lisp, Scala)

**Expansión por Demanda:**

Cuando aparezca un nuevo framework/lenguaje relevante:

.. code-block:: text

 INF.PRG.SWI -> Swift (iOS)
 INF.PRG.KOT -> Kotlin (Android)
 INF.PRG.ELM -> Elm (Frontend funcional)

2.6. Especialidades Otras Subcategorías
----------------------------------------

**Inteligencia Artificial (INF.IAR):**

.. code-block:: text

 INF.IAR.MLF -> Machine Learning Fundamentals
 INF.IAR.DLE -> Deep Learning
 INF.IAR.NLP -> Natural Language Processing
 INF.IAR.CVS -> Computer Vision
 INF.IAR.RFO -> Reinforcement Learning

**DevOps (INF.DVC):**

.. code-block:: text

 INF.DVC.DOC -> Docker
 INF.DVC.KUB -> Kubernetes
 INF.DVC.AWS -> Amazon Web Services
 INF.DVC.AZU -> Microsoft Azure
 INF.DVC.GCP -> Google Cloud Platform
 INF.DVC.TER -> Terraform
 INF.DVC.ANS -> Ansible

**Arquitectura (ING.ARQ):**

.. code-block:: text

 ING.ARQ.MIC -> Microservicios
 ING.ARQ.CLE -> Clean Architecture
 ING.ARQ.DDD -> Domain-Driven Design
 ING.ARQ.ARC -> arc42 (plantilla documentación)
 ING.ARQ.HEX -> Hexagonal Architecture

----

Parte 3: Proceso de Clasificación
==================================

3.1. Flujo de Decisión Principal
---------------------------------

**Diagrama de Flujo:**

.. code-block:: text

 +-------------------------------------+
 | NUEVO LIBRO A CLASIFICAR |
 +--------------+----------------------+
 |

 +-------------------------------------+
 | PASO 1: Determinar CATEGORÍA |
 | |
 | ¿Informática, Ingeniería o Ciencias?|
 +--------------+----------------------+
 |

 +-------------------------------------+
 | PASO 2: Determinar SUBCATEGORÍA |
 | |
 | ¿Qué área específica? |
 +--------------+----------------------+
 |

 +-------------------------------------+
 | PASO 3: Determinar ESPECIALIDAD |
 | |
 | ¿Qué tecnología/metodología? |
 +--------------+----------------------+
 |

 +-------------------------------------+
 | PASO 4: Asignar NÚMERO SECUENCIAL |
 | |
 | Verificar último número usado |
 +--------------+----------------------+
 |

 +-------------------------------------+
 | RESULTADO: Código de Clasificación |
 | |
 | Ejemplo: INF.PRG.FST.001 |
 +-------------------------------------+

3.2. Paso 1: Determinar Categoría
----------------------------------

**Método: Análisis del Título y Contenido**

1. **Leer título completo del libro**

2. **Leer tabla de contenidos (TOC)**

3. **Analizar palabras clave del título**

4. **Aplicar criterios de clasificación:**

.. code-block:: rst

 INFORMÁTICA (INF) si predomina:
 [OK] Programación
 [OK] Lenguajes de programación
 [OK] Frameworks
 [OK] Algoritmos
 [OK] Inteligencia Artificial
 [OK] Redes y seguridad
 [OK] Bases de datos

 INGENIERÍA (ING) si predomina:
 [OK] Arquitectura de software
 [OK] Diseño de sistemas
 [OK] Metodologías (Agile, Scrum)
 [OK] Procesos de desarrollo
 [OK] Patrones arquitectónicos
 [OK] Modelado (UML, BPMN)

 CIENCIAS (CIE) si predomina:
 [OK] Matemáticas aplicadas
 [OK] Estadística y probabilidad
 [OK] Física computacional
 [OK] Bioinformática
 [OK] Modelado científico

**Ejemplos Resueltos:**

.. list-table::
 :header-rows: 1
 :widths: 50 15 35

 * - Título del Libro
   - Categoría
   - Justificación
 * - "Modern Full-Stack Development with TypeScript and React"
   - **INF**
   - Programación, frameworks específicos
 * - "Software Architecture: The Hard Parts"
   - **ING**
   - Arquitectura y diseño de sistemas
 * - "Linear Algebra for Machine Learning"
   - **CIE**
   - Matemáticas aplicadas (aunque para ML)
 * - "Python for Data Science"
   - **INF**
   - Programación con Python (domina sobre ciencia)
 * - "Designing Data-Intensive Applications"
   - **ING**
   - Diseño de sistemas (domina sobre implementación)

3.3. Paso 2: Determinar Subcategoría
-------------------------------------

**Método: Análisis de Temas Principales**

1. **Identificar tema dominante** del libro

2. **Revisar tabla de contenidos** para confirmar

3. **Buscar coincidencia** con subcategorías existentes

4. **Si no existe subcategoría:** proponer nueva

**Árbol de Decisión para INFORMÁTICA:**

.. code-block:: text

 ¿El libro trata de...?

 +- Lenguajes de programación (Python, Java, C++)?
 | +--> INF.PRG (Programación)
 |
 +- Machine Learning, Deep Learning, NLP?
 | +--> INF.IAR (Inteligencia Artificial)
 |
 +- Protocolos de red, comunicaciones?
 | +--> INF.RED (Redes)
 |
 +- Seguridad, criptografía, hacking ético?
 | +--> INF.SEG (Seguridad)
 |
 +- SQL, NoSQL, diseño de BD?
 | +--> INF.BDD (Bases de Datos)
 |
 +- Linux, Windows, administración de sistemas?
 | +--> INF.SOP (Sistemas Operativos)
 |
 +- HTML, CSS, desarrollo web general?
 | +--> INF.WEB (Desarrollo Web)
 |
 +- iOS, Android, apps móviles?
 | +--> INF.MOV (Desarrollo Móvil)
 |
 +- Docker, Kubernetes, CI/CD, Cloud?
 | +--> INF.DVC (DevOps y Cloud)
 |
 +- Estructuras de datos, algoritmos?
 +--> INF.ALG (Algoritmos)

**Casos Especiales:**

.. code-block:: rst

 Libro: "Full-Stack Development with Python and React"

 Análisis:
 - ¿Es sobre Python específicamente? NO (usa Python + React)
 - ¿Es sobre React específicamente? NO (usa Python + React)
 - ¿Es sobre desarrollo web? SÍ, pero FULL-STACK

 Decisión:
 -> INF.PRG (Programación) porque cubre múltiples tecnologías
 -> Especialidad: FST (Full-Stack)

3.4. Paso 3: Determinar Especialidad
-------------------------------------

**Método: Identificar Tecnología/Framework Principal**

1. **Extraer tecnologías** mencionadas en el título

2. **Priorizar según peso** en el contenido

3. **Buscar coincidencia** con especialidades existentes

4. **Crear nueva especialidad** si es tecnología emergente relevante

**Criterios de Priorización:**

.. code-block:: rst

 Peso 1 (MÁS IMPORTANTE): Tecnología en el título principal
 Peso 2: Tecnología en subtítulo
 Peso 3: Tecnología con capítulos dedicados
 Peso 4: Tecnología mencionada secundariamente

**Ejemplos Resueltos:**

.. code-block:: rst

 Título: "Modern Full-Stack Development: Using TypeScript, React,
 Node.js, Webpack, Python, Django, and Docker"

 Análisis:
 - Peso 1: "Full-Stack Development" -> FST
 - Peso 2: TypeScript, React, Node.js, Python, Django, Docker
 - Decisión: ESPECIALIDAD = FST (domina sobre tecnologías específicas)

 Clasificación: INF.PRG.FST

----

.. code-block:: rst

 Título: "React Advanced Patterns and Best Practices"

 Análisis:
 - Peso 1: "React" -> REA
 - Decisión: ESPECIALIDAD = REA

 Clasificación: INF.PRG.REA

----

.. code-block:: rst

 Título: "Python for Machine Learning"

 Análisis:
 - Peso 1: "Python" y "Machine Learning"
 - ¿Es libro de Python? -> SÍ, aplicado a ML
 - ¿Es libro de ML? -> SÍ, usando Python

 Decisión según contexto:
 - Si domina sintaxis Python -> INF.PRG.PYT
 - Si domina algoritmos ML -> INF.IAR.MLF

 -> Revisar TOC para decidir

**Tabla de Prioridades Comunes:**

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - Combinación en Título
   - Subcategoría
   - Especialidad
 * - "Full-Stack + [tecnologías]"
   - PRG
   - FST
 * - "React + [otros frameworks]"
   - PRG
   - REA (si React domina)
 * - "Python + Data Science"
   - PRG
   - PYT (si domina sintaxis)
 * - "Machine Learning + Python"
   - IAR
   - MLF (si domina algoritmos)
 * - "Docker + Kubernetes"
   - DVC
   - DOC o KUB (según peso)
 * - "Microservices Architecture"
   - ARQ
   - MIC

3.5. Paso 4: Asignar Número Secuencial
---------------------------------------

**Método: Verificación de Últimos Números Usados**

1. **Listar libros existentes** en la especialidad

 .. code-block:: bash

 ls /biblioteca/informatica/programacion/full_stack/

2. **Identificar último número** usado

 .. code-block:: text

 Modern_Full_Stack_Development_Zammetti_2ed/ -> INF.PRG.FST.001
 Full_Stack_React_TypeScript_2023/ -> INF.PRG.FST.002
 [vacío] -> Próximo: 003

3. **Asignar siguiente número** secuencial

4. **Formato del número:**

 .. code-block:: text

 - 3 dígitos con ceros a la izquierda
 - Rango: 001-999
 - Ejemplos: 001, 002, 023, 147, 999

**Reglas de Numeración:**

.. code-block:: rst

 [OK] Números correlativos: 001, 002, 003, ...
 [OK] Sin saltos: No usar 001, 005, 010
 [ERROR] No reutilizar números de libros eliminados
 [OK] Si se elimina 003, el próximo es 004 (no reusar 003)

**Registro de Números Asignados:**

Mantener archivo de catálogo:

.. code-block:: rst

 # biblioteca/_metadata_biblioteca/catalogo_numeros.txt

 INF.PRG.FST.001 -> Modern_Full_Stack_Development_Zammetti_2ed
 INF.PRG.FST.002 -> Full_Stack_React_TypeScript_2023
 INF.PRG.REA.001 -> React_Advanced_Patterns_Lee_2024
 INF.PRG.PYT.001 -> Python_Complete_Guide_2025
 INF.IAR.MLF.001 -> Machine_Learning_Basics_2024

----

Parte 4: Estructura de Carpetas
================================

4.1. Jerarquía Completa
-----------------------

**Plantilla de Estructura:**

.. code-block:: text

 /biblioteca/
 |
 +-- _metadata_biblioteca/ # [PRIVADO]
 | +-- META_BIB_001_Sistema_Clasificacion_1_0_0.rst
 | +-- META_BIB_002_Guia_Organizacion_1_0_0.rst
 | +-- META_BIB_003_Esquema_Codificacion_1_0_0.rst
 | +-- catalogo_completo.rst # Listado de todos los libros
 | +-- catalogo_numeros.txt # Registro de números asignados
 | +-- estadisticas_biblioteca.rst # Métricas y reportes
 |
 +-- informatica/ # CATEGORÍA: INF
 | |
 | +-- programacion/ # SUBCATEGORÍA: PRG
 | | |
 | | +-- full_stack/ # ESPECIALIDAD: FST
 | | | |
 | | | +-- Modern_Full_Stack_Development_Zammetti_2ed/ # LIBRO: 001
 | | | | +-- metadata_libro.rst
 | | | | +-- index.rst
 | | | | +-- glosario_acumulativo.rst
 | | | | +-- Chapter_01_*/
 | | | | +-- Chapter_02_*/
 | | | | +-- ...
 | | | |
 | | | +-- Full_Stack_React_TypeScript_2023/ # LIBRO: 002
 | | | +-- ...
 | | |
 | | +-- react/ # ESPECIALIDAD: REA
 | | | +-- React_Advanced_Patterns_Lee_2024/ # LIBRO: 001
 | | |
 | | +-- python/ # ESPECIALIDAD: PYT
 | | | +-- Python_Complete_Guide_2025/ # LIBRO: 001
 | | | +-- Python_For_Data_Science_2024/ # LIBRO: 002
 | | |
 | | +-- typescript/ # ESPECIALIDAD: TSC
 | | +-- TypeScript_Deep_Dive_Chen_2023/ # LIBRO: 001
 | |
 | +-- inteligencia_artificial/ # SUBCATEGORÍA: IAR
 | | +-- machine_learning/ # ESPECIALIDAD: MLF
 | | | +-- ML_Handbook_Smith_2025/
 | | |
 | | +-- deep_learning/ # ESPECIALIDAD: DLE
 | | +-- Deep_Learning_Goodfellow_2024/
 | |
 | +-- devops/ # SUBCATEGORÍA: DVC
 | +-- docker/ # ESPECIALIDAD: DOC
 | | +-- Docker_Complete_Guide_Kumar_2024/
 | |
 | +-- kubernetes/ # ESPECIALIDAD: KUB
 | +-- Kubernetes_Up_Running_Burns_2023/
 |
 +-- ingenieria/ # CATEGORÍA: ING
 | |
 | +-- arquitectura/ # SUBCATEGORÍA: ARQ
 | | +-- microservicios/ # ESPECIALIDAD: MIC
 | | | +-- Microservices_Patterns_Richardson_2023/
 | | |
 | | +-- clean_architecture/ # ESPECIALIDAD: CLE
 | | +-- Clean_Architecture_Martin_2024/
 | |
 | +-- sistemas/ # SUBCATEGORÍA: SIS
 | +-- arc42/ # ESPECIALIDAD: ARC
 | +-- arc42_documentation/
 |
 +-- ciencias/ # CATEGORÍA: CIE
 +-- matematicas/ # SUBCATEGORÍA: MAT
 +-- algebra_lineal/ # ESPECIALIDAD: ALG
 +-- Linear_Algebra_for_ML_2024/

4.2. Estructura Interna de Libro
---------------------------------

**Cada carpeta de libro contiene:**

.. code-block:: text

 Libro_Ejemplo/
 |
 +-- metadata_libro.rst # [STAR] Información bibliográfica
 +-- index.rst # [STAR] Índice del libro completo
 +-- glosario_acumulativo.rst # [STAR] Todos los términos del libro
 |
 +-- Chapter_01_Titulo/ # Capítulo 1
 | +-- original/
 | | +-- chapter_01.pdf # PDF original (inglés)
 | |
 | +-- traduccion/
 | | +-- capitulo_01.rst # Traducción (español)
 | |
 | +-- glosario_capitulo.rst # Términos del capítulo
 | +-- notas_traduccion.rst # Notas específicas
 | |
 | +-- figuras/
 | +-- fig_01_01.png
 | +-- fig_01_02.png
 |
 +-- Chapter_02_Titulo/ # Capítulo 2
 | +-- original/
 | +-- traduccion/
 | +-- glosario_capitulo.rst
 | +-- notas_traduccion.rst
 | +-- figuras/
 |
 +-- [... más capítulos ...]
 |
 +-- appendices/ # Apéndices
 | +-- appendix_A/
 | +-- appendix_B/
 |
 +-- front_matter/ # Material preliminar
 | +-- about_author.rst
 | +-- acknowledgments.rst
 | +-- introduction.rst
 |
 +-- back_matter/ # Material final
 +-- index_alfabetico.rst

**Archivos Obligatorios:**

.. code-block:: rst

 [OK] metadata_libro.rst -> Información bibliográfica + código clasificación
 [OK] index.rst -> Índice navegable del libro
 [OK] glosario_acumulativo.rst -> Glosario completo del libro

 Opcional pero recomendado:
 [WARNING] glosario_capitulo.rst (por capítulo)
 [WARNING] notas_traduccion.rst (por capítulo)

----

Parte 5: Codificación y Nomenclatura
=====================================

5.1. Formato del Código de Clasificación
-----------------------------------------

**Estructura Completa:**

.. code-block:: text

 CATEGORÍA.SUBCATEGORÍA.ESPECIALIDAD.NÚMERO
 | | | |
 | | | +- 001-999 (secuencial)
 | | +--------------- 3 letras mayúsculas
 | +---------------------------- 3 letras mayúsculas
 +-------------------------------------- 3 letras mayúsculas

**Ejemplos Válidos:**

.. code-block:: text

 INF.PRG.FST.001 [OK]
 INF.IAR.MLF.023 [OK]
 ING.ARQ.MIC.005 [OK]
 CIE.MAT.ALG.147 [OK]

**Ejemplos Inválidos:**

.. code-block:: text

 inf.prg.fst.001 [ERROR] (minúsculas)
 INF.PROG.FST.001 [ERROR] (subcategoría 4 letras)
 INF.PRG.FS.001 [ERROR] (especialidad 2 letras)
 INF.PRG.FST.1 [ERROR] (número sin ceros)
 INF.PRG.FST.1000 [ERROR] (número > 999)

5.2. Abreviaturas Estándar
---------------------------

**Categorías (3 letras):**

.. code-block:: text

 INF -> Informática
 ING -> Ingeniería
 CIE -> Ciencias

**Subcategorías Comunes (3 letras):**

.. code-block:: text

 PRG -> Programación
 IAR -> Inteligencia Artificial
 RED -> Redes
 SEG -> Seguridad
 BDD -> Bases de Datos
 SOP -> Sistemas Operativos
 WEB -> Desarrollo Web
 MOV -> Desarrollo Móvil
 DVC -> DevOps y Cloud
 ALG -> Algoritmos

 SIS -> Sistemas
 ARQ -> Arquitectura
 MET -> Metodologías
 REQ -> Requisitos
 PRU -> Pruebas
 MOD -> Modelado

 MAT -> Matemáticas
 EST -> Estadística
 FIS -> Física
 BIO -> Biología

**Especialidades Comunes (3 letras):**

.. code-block:: text

 FST -> Full-Stack
 FRE -> Frontend
 BAC -> Backend
 PYT -> Python
 JAV -> JavaScript
 TSC -> TypeScript
 REA -> React
 VUE -> Vue.js
 ANG -> Angular
 NOD -> Node.js
 DJA -> Django

 MLF -> Machine Learning Fundamentals
 DLE -> Deep Learning
 NLP -> Natural Language Processing
 CVS -> Computer Vision

 DOC -> Docker
 KUB -> Kubernetes
 AWS -> Amazon Web Services
 AZU -> Microsoft Azure
 GCP -> Google Cloud Platform

 MIC -> Microservicios
 CLE -> Clean Architecture
 DDD -> Domain-Driven Design
 ARC -> arc42

5.3. Reglas de Creación de Abreviaturas
----------------------------------------

**Para Nuevas Subcategorías/Especialidades:**

1. **Usar exactamente 3 letras mayúsculas**

2. **Priorizar primeras letras** del nombre

 .. code-block:: text

 Machine Learning -> MLF (Machine Learning Fundamentals)
 TypeScript -> TSC
 React -> REA

3. **Si colisión, usar letra significativa adicional:**

 .. code-block:: text

 Angular -> ANG (no ANU, no ANR)
 Vue.js -> VUE (no VUJ, no VJS)

4. **Evitar ambigüedades:**

 .. code-block:: text

 [ERROR] MAT para "Material Design" (ya es Matemáticas)
 [OK] MDG para "Material Design"

5. **Documentar siempre** en tabla de abreviaturas

**Proceso de Aprobación:**

.. code-block:: rst

 1. Proponer nueva abreviatura
 2. Verificar NO colisión con existentes
 3. Documentar en META_BIB_003_Esquema_Codificacion
 4. Actualizar tabla maestra de códigos
 5. Aprobar en revisión de metadata

----

Parte 6: Metadata del Libro
============================

6.1. Plantilla metadata_libro.rst
----------------------------------

**Archivo:** ``metadata_libro.rst``

**Contenido Completo:**

.. code-block:: rst

 .. meta::
 :libro_id: LIB_INF_FST_001
 :tipo: Libro_Tecnico
 :estado: En_Traduccion
 :progreso: 35%
 :clasificacion: INF.PRG.FST.001

 ==========================================================================
 [Título Traducido del Libro]
 ==========================================================================

 Información Bibliográfica
 ==========================

 Título Original
 [Título completo en idioma original]

 Título Traducido
 [Título completo traducido]

 Autor
 [Nombre del autor o autores]

 Editorial
 [Editorial original]

 Año Publicación
 [Año de publicación]

 ISBN
 [ISBN-13]

 Páginas
 [Número total de páginas]

 Idiomas
 - Fuente: [Inglés (en), etc.]
 - Destino: [Español (es), etc.]

 Clasificación según Guía Metodológica
 ======================================

 Código Clasificación
 [INF.PRG.FST.001]

 Categoría Principal
 [Informática / Ingeniería / Ciencias]

 Subcategoría
 [Programación / IA / Arquitectura / etc.]

 Especialidad
 [Full-Stack / React / Python / etc.]

 Subtemas
 - [Subtema 1]
 - [Subtema 2]
 - [...]

 Nivel
 [Principiante / Intermedio / Avanzado / Experto]

 Público Objetivo
 [Descripción del público objetivo]

 Palabras Clave
 [lista, de, palabras, clave, separadas, por, comas]

 Estado de Traducción
 =====================

 Progreso Global
 [XX% completado (Y de Z capítulos)]

 Capítulos Completados
 [OK] [Listado de capítulos completados]

 Capítulos En Proceso
 [PROCESSING] [Listado de capítulos en proceso con %]

 Capítulos Pendientes
 [RUNNING] [Listado de capítulos pendientes]

 Fecha Inicio
 [YYYY-MM-DD]

 Fecha Estimada Finalización
 [YYYY-MM-DD]

 Equipo de Traducción
 ====================

 Traductor Principal
 [Nombre]

 Revisores Técnicos
 - [Nombre] ([Ámbito])
 - [...]

 Especialistas Consultados
 - [Nombre] ([Área de especialidad])
 - [...]

 Estadísticas de Traducción
 ===========================

 Total Páginas Original
 [XXX páginas]

 Total Páginas Traducidas
 [XXX páginas (XX%)]

 Términos Técnicos Identificados
 [XXX términos únicos]

 Términos en Glosario
 [XXX términos documentados]

 Figuras
 - Total: [XXX figuras]
 - Traducidas: [XXX figuras]
 - Adaptadas: [XXX figuras]

 Tablas
 - Total: [XXX tablas]
 - Traducidas: [XXX tablas]

 Ejemplos de Código
 - Total: [XXX ejemplos]
 - Sin traducir (preservados): [XXX ejemplos]
 - Comentarios traducidos: [XXX ejemplos]

 Procedimientos Aplicados
 =========================

 Workflow
 :doc:`/procedimientos/PROC_001_Workflow_General_1_0_0`

 Modo Traducción
 [Alta Fidelidad / Marcado Visual / Combinado]

 Marcado Términos
 [Descripción de estrategia de marcado]

 Formato Destino
 reStructuredText (Sphinx)

 Control de Calidad
 ==================

 Verificaciones por Capítulo
 - [OK] Checklist contenido completo
 - [OK] Checklist términos marcados
 - [OK] Checklist formato preservado
 - [OK] Checklist fidelidad estructural
 - [OK] Checklist referencias cruzadas

 Revisiones
 - 1ª revisión técnica: [Estado]
 - 2ª revisión estilo: [Estado]

 Errores Detectados
 [Listado por capítulo]

 Enlaces y Referencias
 =====================

 Repositorio Original
 [URL del repositorio o fuente]

 Carpeta Traducción
 ``/biblioteca/[ruta]/[nombre_libro]/``

 Glosario Acumulativo
 :doc:`glosario_acumulativo`

 Build Sphinx
 ``make html`` en carpeta raíz del libro

 Notas Especiales
 ================

 Consideraciones Técnicas
 [Notas específicas del libro]

 Terminología Específica
 [Decisiones de traducción de términos clave]

 Decisiones de Traducción
 [Criterios aplicados en este libro específico]

 Referencias Cruzadas
 ====================

 Libros Relacionados en Biblioteca
 [Enlaces a libros relacionados]

 Procedimientos de Traducción Relacionados
 [Enlaces a procedimientos aplicados]

 Historial de Versiones Traducción
 ==================================

 .. list-table::
 :widths: 10 15 15 60
 :header-rows: 1

 * - Versión
   - Fecha
 - Responsable
 - Cambios
 * - [X.XX.X]
   - [YYYY-MM-DD]
 - [Nombre]
 - [Descripción de cambios]

 ----

 **Última actualización:** [YYYY-MM-DD]

6.2. Campos Obligatorios vs Opcionales
---------------------------------------

**Campos OBLIGATORIOS (sin estos, metadata inválida):**

.. code-block:: rst

 [OK] libro_id (meta tag)
 [OK] clasificacion (meta tag)
 [OK] Título Original
 [OK] Título Traducido
 [OK] Autor
 [OK] Año Publicación
 [OK] Código Clasificación
 [OK] Categoría Principal
 [OK] Subcategoría
 [OK] Especialidad
 [OK] Progreso Global
 [OK] Fecha Inicio

**Campos RECOMENDADOS:**

.. code-block:: rst

 [WARNING] Editorial
 [WARNING] ISBN
 [WARNING] Páginas
 [WARNING] Nivel
 [WARNING] Público Objetivo
 [WARNING] Palabras Clave
 [WARNING] Traductor Principal
 [WARNING] Términos en Glosario
 [WARNING] Procedimientos Aplicados

**Campos OPCIONALES:**

.. code-block:: rst

 [INFO] Revisores Técnicos
 [INFO] Especialistas Consultados
 [INFO] Figuras (estadísticas)
 [INFO] Tablas (estadísticas)
 [INFO] Repositorio Original
 [INFO] Notas Especiales
 [INFO] Referencias Cruzadas

----

Parte 7: Casos de Uso Completos
================================

7.1. Caso 1: Clasificar "Modern Full-Stack Development (2nd Edition)"
----------------------------------------------------------------------

**Información del Libro:**

.. code-block:: text

 Título: Modern Full-Stack Development: Using TypeScript, React,
 Node.js, Webpack, Python, Django, and Docker (Second Edition)
 Autor: Frank Zammetti
 Editorial: Apress
 Año: 2024
 Temas: TypeScript, React, Node.js, Python, Django, Docker

**PASO 1: Determinar Categoría**

.. code-block:: rst

 ¿El libro trata de programación con frameworks específicos?
 -> SÍ -> INFORMÁTICA (INF)

**PASO 2: Determinar Subcategoría**

.. code-block:: rst

 ¿Es sobre un lenguaje específico o desarrollo general?
 -> Cubre múltiples lenguajes y frameworks
 -> Enfoque en desarrollo completo (frontend + backend)
 -> PROGRAMACIÓN (PRG)

**PASO 3: Determinar Especialidad**

.. code-block:: rst

 ¿Cuál es el enfoque principal?
 -> "Full-Stack Development" en el título
 -> Cubre frontend (React) + backend (Node.js, Django)
 -> FULL-STACK (FST)

**PASO 4: Asignar Número**

.. code-block:: bash

 # Verificar libros existentes
 $ ls /biblioteca/informatica/programacion/full_stack/

 # Resultado: vacío (primer libro en esta especialidad)
 # Asignar: 001

**RESULTADO FINAL:**

.. code-block:: text

 Código Clasificación: INF.PRG.FST.001

 Ruta Completa:
 /biblioteca/informatica/programacion/full_stack/
 Modern_Full_Stack_Development_Zammetti_2ed/

**Metadata:**

.. code-block:: rst

 .. meta::
 :libro_id: LIB_INF_FST_001
 :clasificacion: INF.PRG.FST.001

7.2. Caso 2: Clasificar "Machine Learning with Python"
-------------------------------------------------------

**Información del Libro:**

.. code-block:: text

 Título: Machine Learning with Python: A Comprehensive Guide
 Autor: Sarah Johnson
 Editorial: O'Reilly
 Año: 2025
 Temas: Machine Learning, Python, scikit-learn, TensorFlow

**PASO 1: Determinar Categoría**

.. code-block:: rst

 ¿Es principalmente sobre algoritmos de ML o sobre Python?
 -> Enfoque: Algoritmos de Machine Learning
 -> Python es la herramienta, NO el tema principal
 -> INFORMÁTICA (INF)

**PASO 2: Determinar Subcategoría**

.. code-block:: rst

 ¿Es sobre programación o IA?
 -> Tema central: Machine Learning (rama de IA)
 -> INTELIGENCIA ARTIFICIAL (IAR)

**PASO 3: Determinar Especialidad**

.. code-block:: rst

 ¿Qué tipo de IA?
 -> Machine Learning (no Deep Learning, no NLP específico)
 -> MACHINE LEARNING FUNDAMENTALS (MLF)

**PASO 4: Asignar Número**

.. code-block:: bash

 $ ls /biblioteca/informatica/inteligencia_artificial/machine_learning/
 # Vacío -> 001

**RESULTADO FINAL:**

.. code-block:: text

 Código Clasificación: INF.IAR.MLF.001

 Ruta:
 /biblioteca/informatica/inteligencia_artificial/machine_learning/
 Machine_Learning_with_Python_Johnson_2025/

7.3. Caso 3: Clasificar "Software Architecture: The Hard Parts"
----------------------------------------------------------------

**Información del Libro:**

.. code-block:: text

 Título: Software Architecture: The Hard Parts
 Autor: Neal Ford, Mark Richards
 Editorial: O'Reilly
 Año: 2023
 Temas: Arquitectura de software, trade-offs, patrones

**PASO 1: Determinar Categoría**

.. code-block:: rst

 ¿Es sobre programación (código) o sobre arquitectura (diseño)?
 -> Enfoque: Diseño de sistemas, patrones arquitectónicos
 -> NO trata de código específico
 -> INGENIERÍA (ING)

**PASO 2: Determinar Subcategoría**

.. code-block:: rst

 ¿Dentro de ingeniería, cuál es el tema?
 -> "Software Architecture" explícito en título
 -> ARQUITECTURA (ARQ)

**PASO 3: Determinar Especialidad**

.. code-block:: rst

 ¿Qué tipo de arquitectura?
 -> Libro general sobre arquitectura (no específico de microservicios, etc.)
 -> Crear especialidad: GEN (General Architecture)

 NOTA: Si existe especialidad más específica, usarla

**RESULTADO FINAL:**

.. code-block:: text

 Código Clasificación: ING.ARQ.GEN.001

 Ruta:
 /biblioteca/ingenieria/arquitectura/general/
 Software_Architecture_Hard_Parts_Ford_2023/

7.4. Caso 4: Clasificar "arc42 Documentation Template"
-------------------------------------------------------

**Información del Libro:**

.. code-block:: text

 Título: arc42: Effective Software Architecture Documentation
 Autor: Gernot Starke, Peter Hruschka
 Editorial: Leanpub
 Año: 2023
 Temas: Documentación de arquitectura, plantilla arc42

**PASO 1: Categoría**

.. code-block:: rst

 -> INGENIERÍA (ING) (arquitectura y documentación)

**PASO 2: Subcategoría**

.. code-block:: rst

 -> ARQUITECTURA (ARQ) (plantilla de arquitectura)

**PASO 3: Especialidad**

.. code-block:: rst

 -> ARC (arc42 específico)

**PASO 4: Número**

.. code-block:: bash

 $ ls /biblioteca/ingenieria/sistemas/arquitectura/arc42/
 # Ya existe: arc42_documentation/ -> Este es 001

 # Si hubiera otro libro de arc42:
 # arc42_examples/ -> Sería 002

**RESULTADO:**

.. code-block:: text

 Código: ING.SIS.ARC.001

 Ruta (ya existente):
 /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/

7.5. Caso 5: Clasificar "Docker Deep Dive"
-------------------------------------------

**Información del Libro:**

.. code-block:: text

 Título: Docker Deep Dive
 Autor: Nigel Poulton
 Editorial: Docker Inc.
 Año: 2024
 Temas: Docker, containerización, orquestación básica

**PASO 1: Categoría**

.. code-block:: rst

 ¿Es programación o DevOps?
 -> DevOps (Docker es herramienta de despliegue)
 -> INFORMÁTICA (INF)

**PASO 2: Subcategoría**

.. code-block:: rst

 -> DEVOPS Y CLOUD (DVC)

**PASO 3: Especialidad**

.. code-block:: rst

 -> DOCKER (DOC)

**PASO 4: Número**

.. code-block:: bash

 $ ls /biblioteca/informatica/devops/docker/
 # Vacío -> 001

**RESULTADO:**

.. code-block:: text

 Código: INF.DVC.DOC.001

 Ruta:
 /biblioteca/informatica/devops/docker/
 Docker_Deep_Dive_Poulton_2024/

----

Parte 8: Mantenimiento y Evolución
===================================

8.1. Actualización de la Taxonomía
-----------------------------------

**¿Cuándo agregar nueva categoría/subcategoría/especialidad?**

.. code-block:: rst

 AGREGAR NUEVA ESPECIALIDAD cuando:
 [OK] Aparecen 3+ libros del mismo tema sin especialidad adecuada
 [OK] Tecnología emergente con momentum (ej: "Svelte" si hay demanda)
 [OK] Área de conocimiento bien delimitada

 NO AGREGAR cuando:
 [ERROR] Solo 1 libro (usar especialidad general o más cercana)
 [ERROR] Tecnología muy nicho o temporal
 [ERROR] Puede clasificarse en especialidad existente

**Proceso de Aprobación:**

.. code-block:: rst

 1. Proponer nueva especialidad en reunión de metadata
 2. Justificar necesidad (cuántos libros, tendencia)
 3. Definir código de 3 letras (verificar no colisión)
 4. Documentar en META_BIB_003
 5. Actualizar catálogo maestro
 6. Comunicar a equipo de traducción

8.2. Reorganización de Libros
------------------------------

**¿Qué pasa si cambiamos la clasificación de un libro?**

.. code-block:: rst

 EJEMPLO: Movemos "ML with Python" de INF.PRG.PYT a INF.IAR.MLF

 PASOS:
 1. Crear nueva ubicación:
 /informatica/inteligencia_artificial/machine_learning/

 2. Mover carpeta completa del libro

 3. Actualizar metadata_libro.rst:
 - Cambiar :clasificacion: INF.IAR.MLF.001
 - Actualizar Código Clasificación en cuerpo

 4. Actualizar catálogo_numeros.txt

 5. Actualizar referencias cruzadas en otros libros

 6. Regenerar índices y catálogos

 7. Documentar cambio en historial

**Regla de Oro:**

.. code-block:: rst

 [WARNING] EVITAR reclasificaciones frecuentes

 -> Pensar bien la clasificación inicial
 -> Solo reclasificar si error evidente
 -> Documentar siempre el motivo del cambio

8.3. Control de Versiones de la Guía
-------------------------------------

**Versionado Semántico de la Guía:**

.. code-block:: text

 MAJOR.MINOR.PATCH

 MAJOR: Cambios incompatibles (nueva categoría, reestructuración)
 MINOR: Nuevas especialidades, nuevas reglas (compatible)
 PATCH: Correcciones, clarificaciones, ejemplos

**Historial de Versiones:**

.. code-block:: rst

 v1.0.0 (2026-01-28): Versión inicial
 - 3 categorías (INF, ING, CIE)
 - 16 subcategorías
 - 30+ especialidades
 - Sistema de codificación completo

 [Versiones futuras aquí]

8.4. Métricas y Reportes
-------------------------

**Estadísticas a Mantener:**

.. code-block:: rst

 [TABLE] estadisticas_biblioteca.rst

 Total de Libros: XXX

 Por Categoría:
 - Informática: XXX libros
 - Ingeniería: XXX libros
 - Ciencias: XXX libros

 Top 5 Subcategorías:
 1. Programación: XXX libros
 2. Inteligencia Artificial: XXX libros
 3. Arquitectura: XXX libros
 4. DevOps: XXX libros
 5. Bases de Datos: XXX libros

 Top 5 Especialidades:
 1. Python: XXX libros
 2. Full-Stack: XXX libros
 3. React: XXX libros
 4. Machine Learning: XXX libros
 5. Docker: XXX libros

 Progreso de Traducción:
 - Completados: XXX libros
 - En proceso: XXX libros
 - Pendientes: XXX libros

 Total Páginas Traducidas: XXX páginas
 Total Términos en Glosarios: XXX términos

----

Parte 9: Herramientas y Automatización
=======================================

9.1. Script de Clasificación Asistida
--------------------------------------

**Pseudocódigo:**

.. code-block:: python

 def clasificar_libro(titulo, autor, contenido_toc):
 """
 Asiste en la clasificación de un nuevo libro
 """
 # PASO 1: Analizar título
 palabras_clave = extraer_palabras_clave(titulo)

 # PASO 2: Sugerir categoría
 categoria_sugerida = inferir_categoria(palabras_clave)
 categoria = input(f"Categoría sugerida: {categoria_sugerida}. ¿Confirmar? (S/n)")

 # PASO 3: Sugerir subcategoría
 subcategorias_disponibles = obtener_subcategorias(categoria)
 subcategoria_sugerida = inferir_subcategoria(palabras_clave, contenido_toc)
 subcategoria = seleccionar(subcategorias_disponibles, subcategoria_sugerida)

 # PASO 4: Sugerir especialidad
 especialidades_disponibles = obtener_especialidades(categoria, subcategoria)
 especialidad_sugerida = inferir_especialidad(palabras_clave, contenido_toc)
 especialidad = seleccionar(especialidades_disponibles, especialidad_sugerida)

 # PASO 5: Asignar número
 ultimo_numero = obtener_ultimo_numero(categoria, subcategoria, especialidad)
 numero = ultimo_numero + 1

 # PASO 6: Generar código
 codigo = f"{categoria}.{subcategoria}.{especialidad}.{numero:03d}"

 # PASO 7: Generar ruta
 ruta = generar_ruta(categoria, subcategoria, especialidad, titulo, autor)

 # PASO 8: Crear estructura
 crear_estructura_libro(ruta)

 # PASO 9: Generar metadata_libro.rst
 generar_metadata(ruta, codigo, titulo, autor)

 # PASO 10: Actualizar catálogo
 actualizar_catalogo(codigo, titulo, autor)

 return {
 'codigo': codigo,
 'ruta': ruta,
 'categoria': categoria,
 'subcategoria': subcategoria,
 'especialidad': especialidad,
 'numero': numero
 }

9.2. Script de Validación
--------------------------

**Verificar Integridad de la Biblioteca:**

.. code-block:: python

 def validar_biblioteca():
 """
 Verifica que todos los libros cumplan las reglas
 """
 errores = []

 for libro in recorrer_biblioteca():
 # Verificar metadata_libro.rst existe
 if not existe(f"{libro}/metadata_libro.rst"):
 errores.append(f"{libro}: Falta metadata_libro.rst")

 # Verificar código válido
 codigo = extraer_codigo(libro)
 if not validar_formato_codigo(codigo):
 errores.append(f"{libro}: Código inválido {codigo}")

 # Verificar consistencia ruta vs código
 ruta_esperada = generar_ruta_desde_codigo(codigo)
 if libro != ruta_esperada:
 errores.append(f"{libro}: Ruta no coincide con código")

 # Verificar número secuencial
 if not verificar_numero_secuencial(codigo):
 errores.append(f"{libro}: Número no secuencial")

 return errores

9.3. Generador de Catálogos
----------------------------

**Generar Catálogo Completo:**

.. code-block:: python

 def generar_catalogo():
 """
 Genera catálogo completo en RST
 """
 catalogo = []

 catalogo.append("=" * 80)
 catalogo.append("Catálogo Completo de la Biblioteca ADT")
 catalogo.append("=" * 80)
 catalogo.append("")

 for categoria in CATEGORIAS:
 catalogo.append(f"{categoria.nombre}")
 catalogo.append("=" * len(categoria.nombre))
 catalogo.append("")

 for subcategoria in categoria.subcategorias:
 catalogo.append(f"{subcategoria.nombre}")
 catalogo.append("-" * len(subcategoria.nombre))
 catalogo.append("")

 for especialidad in subcategoria.especialidades:
 if especialidad.libros:
 catalogo.append(f"**{especialidad.nombre}**")
 catalogo.append("")

 for libro in especialidad.libros:
 catalogo.append(f"- {libro.codigo}: {libro.titulo}")
 catalogo.append(f" {libro.autor} ({libro.año})")
 catalogo.append(f" Estado: {libro.estado} ({libro.progreso}%)")
 catalogo.append("")

 escribir_archivo("catalogo_completo.rst", "\n".join(catalogo))

----

Parte 10: Casos Especiales y FAQ
=================================

10.1. Casos Especiales
-----------------------

**Caso 1: Libro Multidominio**

.. code-block:: rst

 Pregunta: "AI for Web Development" - ¿Es IA o Web?

 Respuesta:
 - Analizar peso de cada tema en el TOC
 - ¿60% IA, 40% Web? -> INF.IAR
 - ¿40% IA, 60% Web? -> INF.WEB
 - ¿50/50? -> Elegir tema PRIMARIO del título

**Caso 2: Serie de Libros**

.. code-block:: rst

 Pregunta: "Python Vol 1" y "Python Vol 2" - ¿Mismo código?

 Respuesta:
 - Cada volumen = Libro independiente
 - Asignar números secuenciales:
 * Python_Complete_Guide_Vol1 -> INF.PRG.PYT.001
 * Python_Complete_Guide_Vol2 -> INF.PRG.PYT.002

**Caso 3: Reediciones**

.. code-block:: rst

 Pregunta: "Docker 1st Ed" y "Docker 2nd Ed" - ¿Reemplazar o agregar?

 Respuesta:
 - Cada edición = Libro NUEVO (contenido diferente)
 - Asignar números secuenciales:
 * Docker_Deep_Dive_1ed -> INF.DVC.DOC.001
 * Docker_Deep_Dive_2ed -> INF.DVC.DOC.002

 - En metadata, referenciar edición anterior

**Caso 4: Libro sin Clasificación Clara**

.. code-block:: rst

 Pregunta: "The Art of Computer Programming" - ¿Dónde?

 Respuesta:
 - Revisar TOC detenidamente
 - Si es ALGORITMOS fundamentales -> INF.ALG
 - Si es PROGRAMACIÓN general -> INF.PRG.GEN
 - Consultar con equipo si duda persiste

10.2. Preguntas Frecuentes (FAQ)
---------------------------------

**P1: ¿Puedo cambiar la clasificación después de asignarla?**

.. code-block:: rst

 R: SÍ, pero:
 - Requiere aprobación de coordinador
 - Implica mover carpeta, actualizar metadata, regenerar catálogos
 - Evitar si es posible (pensar bien la clasificación inicial)

**P2: ¿Qué hago si no existe la especialidad que necesito?**

.. code-block:: rst

 R: Proceso:
 1. Verificar que NO existe especialidad cercana
 2. Proponer nueva especialidad (nombre + código 3 letras)
 3. Esperar aprobación de coordinador
 4. Documentar en META_BIB_003
 5. Usar la nueva especialidad

**P3: ¿Los números deben ser consecutivos sin saltos?**

.. code-block:: rst

 R: SÍ.
 - No saltar números: 001, 002, 003 (no 001, 005, 010)
 - No reutilizar números de libros eliminados
 - Si se elimina 003, el próximo es 004 (no reusar 003)

**P4: ¿Qué pasa cuando llego a 999?**

.. code-block:: rst

 R: Dos opciones:
 1. Crear sub-especialidad más granular
 Ej: INF.PRG.PYT.999 -> Dividir en PYT.WEB, PYT.DAT, etc.
 2. Extender a 4 dígitos (requiere cambio MAJOR en guía)

**P5: ¿Puedo tener un libro en dos categorías?**

.. code-block:: rst

 R: NO.
 - Cada libro tiene UNA sola ubicación
 - Si es multidominio, elegir dominio principal
 - Usar referencias cruzadas en metadata

**P6: ¿Cómo clasifico un libro de ejercicios/companion?**

.. code-block:: rst

 R: Dos opciones:
 1. Libro independiente con su propio código
 2. Parte del libro principal (en carpeta companion/)

 Preferir opción 1 si tiene ISBN propio

**P7: ¿Mayúsculas o minúsculas en códigos?**

.. code-block:: rst

 R: SIEMPRE MAYÚSCULAS.
 - INF.PRG.FST.001 [OK]
 - inf.prg.fst.001 [ERROR]

**P8: ¿Qué hacer con libros antiguos/obsoletos?**

.. code-block:: rst

 R: NO eliminar.
 - Marcar como "Obsoleto" en metadata
 - Mantener para referencia histórica
 - Numero NO se reutiliza

**P9: ¿Cómo busco un libro si no recuerdo el código?**

.. code-block:: rst

 R: Tres métodos:
 1. Navegar jerarquía de carpetas
 2. Buscar en catalogo_completo.rst
 3. Buscar por título/autor en catalogo_numeros.txt

**P10: ¿Puedo usar códigos personalizados fuera del sistema?**

.. code-block:: rst

 R: NO recomendado.
 - Seguir siempre esta guía
 - Si necesitas extensión, proponer cambio a la guía

----

Conclusiones y Recomendaciones
===============================

Resumen de Puntos Clave
------------------------

Esta Guía Metodológica de Clasificación Documental establece:

1. **Sistema jerárquico de 4 niveles** (Categoría -> Subcategoría -> Especialidad -> Número)

2. **Códigos alfanuméricos consistentes** (ej: INF.PRG.FST.001)

3. **Proceso de clasificación claro** en 4 pasos repetibles

4. **Taxonomía extensible** pero estructurada

5. **Metadata estandarizada** para cada libro

6. **Mantenimiento y evolución** del sistema

Beneficios del Sistema
----------------------

.. code-block:: rst

 [OK] ORGANIZACIÓN: Estructura lógica y escalable
 [OK] CONSISTENCIA: Dos traductores clasifican igual
 [OK] BÚSQUEDA: Localización rápida por código o navegación
 [OK] ESCALABILIDAD: Soporta crecimiento ilimitado
 [OK] INTEROPERABILIDAD: Integración con sistemas externos
 [OK] PROFESIONALISMO: Base sólida para biblioteca técnica

Próximos Pasos
--------------

1. **Aplicar esta guía** a todos los libros nuevos

2. **Reclasificar libros existentes** si es necesario

3. **Mantener actualizada** la taxonomía según demanda

4. **Automatizar** con scripts de clasificación asistida

5. **Documentar cambios** en historial de versiones

----

Referencias
===========

Estándares y Metodologías
--------------------------

- **ISO 12620-2:2022** - Data category specifications for language resources
- **Dewey Decimal Classification** - Sistema decimal de clasificación bibliográfica
- **Library of Congress Classification** - Sistema de notación alfanumérica
- **Dublin Core Metadata** - Estándar de metadata para recursos digitales

Documentos Relacionados ADT
----------------------------

- :doc:`ARQUITECTURA_TRADUCCION_IACT` - Arquitectura completa del sistema
- :doc:`SINTESIS_METODOLOGICA_ADT` - Base metodológica del proyecto
- :doc:`PLAN_CONTENIDO` - Plan de contenidos en 5 fases
- :doc:`REGLAS_ESTRUCTURA_PROYECTO` - Reglas operativas de estructura

Archivos de la Biblioteca
--------------------------

- ``/biblioteca/_metadata_biblioteca/META_BIB_002_Guia_Organizacion_1_0_0.rst``
- ``/biblioteca/_metadata_biblioteca/META_BIB_003_Esquema_Codificacion_1_0_0.rst``
- ``/biblioteca/_metadata_biblioteca/catalogo_completo.rst``
- ``/biblioteca/_metadata_biblioteca/catalogo_numeros.txt``

----

Apéndice A: Tabla Maestra de Códigos
=====================================

A.1. Categorías (3 letras)
---------------------------

.. list-table::
 :header-rows: 1
 :widths: 15 30 55

 * - Código
   - Nombre
   - Descripción
 * - INF
   - Informática
   - Ciencias de la Computación
 * - ING
   - Ingeniería
   - Ingeniería de Software
 * - CIE
   - Ciencias
   - Ciencias Aplicadas

A.2. Subcategorías Completas
-----------------------------

**INFORMÁTICA (INF):**

.. list-table::
 :widths: 15 35 50
 :header-rows: 1

 * - Código
   - Nombre
   - Ámbito
 * - PRG
   - Programación
   - Lenguajes, paradigmas
 * - IAR
   - Inteligencia Artificial
   - ML, DL, NLP, CV
 * - RED
   - Redes
   - Protocolos, comunicaciones
 * - SEG
   - Seguridad
   - Ciberseguridad, criptografía
 * - BDD
   - Bases de Datos
   - SQL, NoSQL, diseño
 * - SOP
   - Sistemas Operativos
   - Linux, Windows, admin
 * - WEB
   - Desarrollo Web
   - Frontend, Backend, Full-Stack
 * - MOV
   - Desarrollo Móvil
   - iOS, Android, multiplataforma
 * - DVC
   - DevOps y Cloud
   - CI/CD, containers, orquestación
 * - ALG
   - Algoritmos
   - Estructuras de datos, complejidad

**INGENIERÍA (ING):**

.. list-table::
 :widths: 15 35 50
 :header-rows: 1

 * - Código
   - Nombre
   - Ámbito
 * - SIS
   - Sistemas
   - Diseño de sistemas
 * - ARQ
   - Arquitectura
   - Patrones arquitectónicos
 * - MET
   - Metodologías
   - Agile, Scrum, DevOps
 * - REQ
   - Requisitos
   - Ingeniería de requisitos
 * - PRU
   - Pruebas
   - Testing, QA
 * - MOD
   - Modelado
   - UML, BPMN

**CIENCIAS (CIE):**

.. list-table::
 :widths: 15 35 50
 :header-rows: 1

 * - Código
   - Nombre
   - Ámbito
 * - MAT
   - Matemáticas
   - Matemáticas aplicadas
 * - EST
   - Estadística
   - Probabilidad, análisis
 * - FIS
   - Física
   - Física computacional
 * - BIO
   - Biología
   - Bioinformática

A.3. Especialidades Más Comunes
--------------------------------

**Programación (INF.PRG):**

.. code-block:: text

 FST -> Full-Stack
 FRE -> Frontend
 BAC -> Backend
 PYT -> Python
 JAV -> JavaScript
 TSC -> TypeScript
 REA -> React
 VUE -> Vue.js
 ANG -> Angular
 NOD -> Node.js
 DJA -> Django
 FLA -> Flask
 SPR -> Spring
 NET -> .NET
 RUS -> Rust
 GOL -> Go
 CPP -> C++

**Inteligencia Artificial (INF.IAR):**

.. code-block:: text

 MLF -> Machine Learning Fundamentals
 DLE -> Deep Learning
 NLP -> Natural Language Processing
 CVS -> Computer Vision
 RFO -> Reinforcement Learning

**DevOps (INF.DVC):**

.. code-block:: text

 DOC -> Docker
 KUB -> Kubernetes
 AWS -> Amazon Web Services
 AZU -> Microsoft Azure
 GCP -> Google Cloud Platform
 TER -> Terraform
 ANS -> Ansible

**Arquitectura (ING.ARQ):**

.. code-block:: text

 MIC -> Microservicios
 CLE -> Clean Architecture
 DDD -> Domain-Driven Design
 ARC -> arc42
 HEX -> Hexagonal Architecture

----

Apéndice B: Plantillas
=======================

B.1. Plantilla Propuesta Nueva Especialidad
--------------------------------------------

.. code-block:: rst

 PROPUESTA DE NUEVA ESPECIALIDAD
 ================================

 Fecha: [YYYY-MM-DD]
 Propuesto por: [Nombre]

 Nombre de la Especialidad
 --------------------------
 [Nombre completo]

 Código Propuesto (3 letras)
 ----------------------------
 [XXX]

 Verificación de Colisiones
 ---------------------------
 ¿Existe código XXX? [NO]
 ¿Existe especialidad similar? [NO]

 Categoría y Subcategoría
 -------------------------
 Categoría: [INF/ING/CIE]
 Subcategoría: [XXX]

 Justificación
 -------------
 [¿Por qué necesitamos esta especialidad?]
 [¿Cuántos libros potenciales?]
 [¿Es tendencia sostenida?]

 Libros que se Clasificarían Aquí
 ----------------------------------
 1. [Libro 1]
 2. [Libro 2]
 3. [...]

 Especialidad Alternativa (si no se aprueba)
 --------------------------------------------
 [¿Dónde clasificaríamos estos libros si no se crea?]

 Decisión
 --------
 [ ] Aprobado
 [ ] Rechazado
 [ ] Requiere más discusión

 Comentarios
 -----------
 [Comentarios del comité]

B.2. Checklist de Clasificación
--------------------------------

.. code-block:: rst

 CHECKLIST DE CLASIFICACIÓN
 ===========================

 Libro: [Título del libro]
 Clasificador: [Nombre]
 Fecha: [YYYY-MM-DD]

 [ ] PASO 1: Categoría determinada
 Categoría: [ ] INF [ ] ING [ ] CIE
 Justificación: _______________________

 [ ] PASO 2: Subcategoría determinada
 Subcategoría: ___________
 Justificación: _______________________

 [ ] PASO 3: Especialidad determinada
 Especialidad: ___________
 ¿Existe? [ ] Sí [ ] No (proponer nueva)

 [ ] PASO 4: Número asignado
 Último número usado: ___
 Número asignado: ___

 [ ] Código completo generado
 Código: ___.___.___.___

 [ ] Ruta de carpeta generada
 Ruta: /biblioteca/___/___/___/___/

 [ ] Estructura de carpetas creada

 [ ] metadata_libro.rst creado

 [ ] Catálogo actualizado

 [ ] Revisión por segundo clasificador
 Revisor: _______
 ¿Aprobado? [ ] Sí [ ] No

 [ ] Clasificación finalizada

 Comentarios
 -----------
 ________________________________
 ________________________________

----

**FIN DE LA GUÍA**

----

Metadata del Documento
======================

:Documento: GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
:Código: META_BIB_001
:Versión: 1.0.0
:Fecha Creación: 2026-01-28
:Última Actualización: 2026-01-28
:Estado: NORMATIVO
:Autor: Sistema ADT
:Revisores: Pendiente
:Ubicación: ``/biblioteca/_metadata_biblioteca/``
:Referencias:
 - ISO 12620-2:2022
 - Dewey Decimal Classification
 - Library of Congress Classification
 - ARQUITECTURA_TRADUCCION_IACT.rst
 - SINTESIS_METODOLOGICA_ADT.rst

Historial de Versiones
-----------------------

.. list-table::
 :widths: 10 15 15 60
 :header-rows: 1

 * - Versión
   - Fecha
   - Autor
   - Cambios
 * - 1.0.0
   - 2026-01-28
   - Sistema ADT
   - Versión inicial completa de la guía metodológica
