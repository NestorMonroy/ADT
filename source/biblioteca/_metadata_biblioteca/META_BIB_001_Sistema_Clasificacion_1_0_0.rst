==================================================================================
META_BIB_001: Sistema de Clasificación Documental ADT
==================================================================================

:Código: META_BIB_001
:Versión: 1.0.0
:Fecha: 2026-01-28
:Estado: NORMATIVO
:Tipo: Guía Metodológica de Clasificación
:Autor: Sistema ADT

.. note::
 Este es el documento maestro del sistema de clasificación.
 Para la guía completa detallada, ver: ``GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst``
 en ``/mnt/user-data/outputs/``

.. contents:: Tabla de Contenido
 :depth: 3
 :local:

----

Resumen Ejecutivo
=================

Sistema de clasificación jerárquica de 4 niveles para organizar libros técnicos
traducidos en el proyecto ADT.

**Formato del Código:**

.. code-block:: text

 CATEGORÍA.SUBCATEGORÍA.ESPECIALIDAD.NÚMERO
 INF . PRG . FST . 001

 Ejemplo: INF.PRG.FST.001
 +-- Modern Full-Stack Development (Zammetti)

----

Categorías Principales
======================

.. list-table:: Categorías Nivel 1
 :header-rows: 1
 :widths: 15 25 60

 * - Código
   - Nombre
 - Ámbito
 * - **INF**
   - Informática
 - Programación, IA, Redes, Seguridad, DevOps
 * - **ING**
   - Ingeniería
 - Arquitectura, Sistemas, Metodologías, Procesos
 * - **CIE**
   - Ciencias
 - Matemáticas, Estadística, Física, Biología

----

Subcategorías Informática (INF)
================================

.. list-table::
 :header-rows: 1
 :widths: 15 30 55

 * - Código
   - Nombre
 - Descripción
 * - PRG
   - Programación
 - Lenguajes, frameworks, paradigmas
 * - IAR
   - Inteligencia Artificial
 - ML, DL, NLP, Computer Vision
 * - RED
   - Redes
 - Protocolos, comunicaciones, seguridad de red
 * - SEG
   - Seguridad
 - Ciberseguridad, criptografía, ethical hacking
 * - BDD
   - Bases de Datos
 - SQL, NoSQL, diseño de esquemas
 * - SOP
   - Sistemas Operativos
 - Linux, Windows, administración
 * - WEB
   - Desarrollo Web
 - Frontend, Backend, Full-Stack general
 * - MOV
   - Desarrollo Móvil
 - iOS, Android, multiplataforma
 * - DVC
   - DevOps y Cloud
 - Docker, Kubernetes, CI/CD, Cloud
 * - ALG
   - Algoritmos
 - Estructuras de datos, complejidad

Subcategorías Ingeniería (ING)
===============================

.. list-table::
 :header-rows: 1
 :widths: 15 30 55

 * - Código
   - Nombre
 - Descripción
 * - SIS
   - Sistemas
 - Diseño de sistemas complejos
 * - ARQ
   - Arquitectura
 - Patrones arquitectónicos, microservicios
 * - MET
   - Metodologías
 - Agile, Scrum, DevOps, Lean
 * - REQ
   - Requisitos
 - Ingeniería de requisitos, análisis
 * - PRU
   - Pruebas
 - Testing, QA, automatización
 * - MOD
   - Modelado
 - UML, BPMN, especificación formal

Subcategorías Ciencias (CIE)
=============================

.. list-table::
 :header-rows: 1
 :widths: 15 30 55

 * - Código
   - Nombre
 - Descripción
 * - MAT
   - Matemáticas
 - Álgebra, cálculo, matemáticas aplicadas
 * - EST
   - Estadística
 - Probabilidad, análisis estadístico
 * - FIS
   - Física
 - Física computacional, simulaciones
 * - BIO
   - Biología
 - Bioinformática, biología computacional

----

Especialidades Principales
===========================

Programación (INF.PRG)
----------------------

.. code-block:: text

 FST -> Full-Stack Development
 FRE -> Frontend Development
 BAC -> Backend Development
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
 NET -> .NET / C#
 RUS -> Rust
 GOL -> Go
 CPP -> C++
 GEN -> General/Multitecnología

Inteligencia Artificial (INF.IAR)
----------------------------------

.. code-block:: text

 MLF -> Machine Learning Fundamentals
 DLE -> Deep Learning
 NLP -> Natural Language Processing
 CVS -> Computer Vision
 RFO -> Reinforcement Learning

DevOps y Cloud (INF.DVC)
-------------------------

.. code-block:: text

 DOC -> Docker
 KUB -> Kubernetes
 AWS -> Amazon Web Services
 AZU -> Microsoft Azure
 GCP -> Google Cloud Platform
 TER -> Terraform
 ANS -> Ansible
 JEN -> Jenkins
 GIT -> Git/GitHub/GitLab

Arquitectura (ING.ARQ)
----------------------

.. code-block:: text

 MIC -> Microservicios
 CLE -> Clean Architecture
 DDD -> Domain-Driven Design
 ARC -> arc42 (plantilla documentación)
 HEX -> Hexagonal Architecture
 GEN -> General/Múltiples patrones

----

Proceso de Clasificación
=========================

Flujo en 4 Pasos
----------------

.. code-block:: text

 +-------------------------------------+
 | PASO 1: Determinar CATEGORÍA |
 | ¿INF, ING o CIE? |
 +--------------+----------------------+

 +-------------------------------------+
 | PASO 2: Determinar SUBCATEGORÍA |
 | ¿PRG, IAR, ARQ, etc.? |
 +--------------+----------------------+

 +-------------------------------------+
 | PASO 3: Determinar ESPECIALIDAD |
 | ¿FST, PYT, REA, etc.? |
 +--------------+----------------------+

 +-------------------------------------+
 | PASO 4: Asignar NÚMERO SECUENCIAL |
 | 001, 002, 003... |
 +--------------+----------------------+

 CÓDIGO COMPLETO: XXX.XXX.XXX.NNN

Reglas de Clasificación
------------------------

1. **Un libro = Una ubicación** (no clasificación múltiple)
2. **Códigos SIEMPRE en MAYÚSCULAS**
3. **Números secuenciales sin saltos** (001, 002, 003...)
4. **No reutilizar números** de libros eliminados
5. **Exactamente 3 letras** para cada nivel
6. **Formato del número:** 3 dígitos con ceros a la izquierda (001-999)

Ejemplos de Códigos
--------------------

.. code-block:: text

 [OK] Válidos:
 INF.PRG.FST.001 -> Modern Full-Stack Development
 INF.IAR.MLF.023 -> Machine Learning Handbook
 ING.ARQ.ARC.001 -> arc42 Documentation
 CIE.MAT.ALG.005 -> Linear Algebra for ML

 [ERROR] Inválidos:
 inf.prg.fst.001 -> Minúsculas
 INF.PROG.FST.001 -> Subcategoría 4 letras
 INF.PRG.FS.001 -> Especialidad 2 letras
 INF.PRG.FST.1 -> Número sin ceros
 INF.PRG.FST.1000 -> Número > 999

----

Estructura de Carpetas
=======================

Jerarquía Completa
------------------

.. code-block:: text

 /biblioteca/
 |
 +-- _metadata_biblioteca/ # Sistema de clasificación
 | +-- META_BIB_001_Sistema_Clasificacion_1_0_0.rst
 | +-- META_BIB_002_Guia_Organizacion_1_0_0.rst
 | +-- META_BIB_003_Esquema_Codificacion_1_0_0.rst
 | +-- catalogo_completo.rst
 | +-- catalogo_numeros.txt
 | +-- estadisticas_biblioteca.rst
 |
 +-- informatica/ # CATEGORÍA: INF
 | +-- programacion/ # SUBCATEGORÍA: PRG
 | | +-- full_stack/ # ESPECIALIDAD: FST
 | | +-- python/ # ESPECIALIDAD: PYT
 | | +-- react/ # ESPECIALIDAD: REA
 | |
 | +-- inteligencia_artificial/ # SUBCATEGORÍA: IAR
 | +-- devops/ # SUBCATEGORÍA: DVC
 |
 +-- ingenieria/ # CATEGORÍA: ING
 | +-- arquitectura/ # SUBCATEGORÍA: ARQ
 | +-- sistemas/ # SUBCATEGORÍA: SIS
 | +-- arquitectura/
 | +-- arc42_documentation/ # LIBRO EXISTENTE
 |
 +-- ciencias/ # CATEGORÍA: CIE
 +-- matematicas/ # SUBCATEGORÍA: MAT

Estructura Interna de Libro
----------------------------

.. code-block:: text

 Nombre_Libro/
 +-- metadata_libro.rst [STAR] OBLIGATORIO
 +-- index.rst [STAR] OBLIGATORIO
 +-- glosario_acumulativo.rst [STAR] OBLIGATORIO
 |
 +-- Chapter_XX_Titulo/
 | +-- original/
 | | +-- chapter_XX.pdf
 | +-- traduccion/
 | | +-- capitulo_XX.rst
 | +-- glosario_capitulo.rst
 | +-- notas_traduccion.rst
 | +-- figuras/
 |
 +-- appendices/
 +-- front_matter/
 +-- back_matter/

----

Referencias
===========

Documentos Relacionados
-----------------------

- :doc:`META_BIB_002_Guia_Organizacion_1_0_0` - Guía de organización jerárquica
- :doc:`META_BIB_003_Esquema_Codificacion_1_0_0` - Tabla maestra de códigos
- :doc:`catalogo_completo` - Catálogo de todos los libros
- :doc:`estadisticas_biblioteca` - Métricas y reportes

Documentos Externos
-------------------

- Guía completa: ``source/docs_maestros/GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst``
- Resumen ejecutivo: ``source/docs_maestros/RESUMEN_GUIA_CLASIFICACION.md``

Estándares Base
---------------

- ISO 12620-2:2022 - Gestión de repositorios terminológicos
- Dewey Decimal Classification
- Library of Congress Classification

----

Historial de Versiones
=======================

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
 - Versión inicial del sistema de clasificación

----

**Documento:** META_BIB_001_Sistema_Clasificacion_1_0_0.rst
**Ubicación:** ``/biblioteca/_metadata_biblioteca/``
**Estado:** NORMATIVO
**Próxima revisión:** 2026-07-28
