
META_BIB_003: Esquema de Codificación - Tabla Maestra de Códigos
=================================================================

:Código: META_BIB_003
:Versión: 1.0.0
:Fecha: 2026-01-28
:Estado: NORMATIVO
:Tipo: Referencia Técnica
:Autor: Sistema ADT
:Base: META_BIB_001, ISO 12620-2:2022

.. contents:: Tabla de Contenido
 :depth: 3
 :local:




Propósito
=========

Este documento es la **tabla maestra autoritativa** de todos los códigos de
clasificación utilizados en el sistema de biblioteca ADT.

**Funciones:**

1. Registro oficial de todos los códigos asignados
2. Referencia rápida para clasificadores
3. Prevención de colisiones de códigos
4. Historial de códigos aprobados




Formato de Código
=================

Estructura General
==================

.. code-block:: text

 XXX.XXX.XXX.NNN
 | | | +-- NÚMERO (001-999)
 | | +----- ESPECIALIDAD (3 letras mayúsculas)
 | +--------- SUBCATEGORÍA (3 letras mayúsculas)
 +------------- CATEGORÍA (3 letras mayúsculas)

Reglas de Formación
===================

1. **Categorías, Subcategorías, Especialidades:**

 - Exactamente **3 letras MAYÚSCULAS**
 - Sin espacios, sin guiones
 - Caracteres alfabéticos A-Z solamente

2. **Número Secuencial:**

 - Exactamente **3 dígitos numéricos**
 - Rango: ``001`` a ``999``
 - Con ceros a la izquierda
 - Sin saltos en la secuencia

3. **Separadores:**

 - Punto (``.``) entre cada componente
 - Sin espacios antes o después de puntos

**Ejemplos Válidos:**

.. code-block:: text

 INF.PRG.FST.001 [OK]
 ING.ARQ.MIC.023 [OK]
 CIE.MAT.ALG.147 [OK]

**Ejemplos Inválidos:**

.. code-block:: text

 inf.prg.fst.001 [ERROR] Minúsculas
 INF.PROG.FST.001 [ERROR] Subcategoría 4 letras
 INF.PRG.FS.001 [ERROR] Especialidad 2 letras
 INF.PRG.FST.1 [ERROR] Número sin ceros
 INF PRG FST 001 [ERROR] Espacios en lugar de puntos
 INF-PRG-FST-001 [ERROR] Guiones en lugar de puntos




Tabla Maestra: Categorías
=========================

.. list-table:: Categorías (Nivel 1)
 :header-rows: 1
 :widths: 10 25 60 5

 * - Código
   - Nombre
   - Ámbito
   - Estado
 * - **INF**
   - Informática
   - Ciencias de la Computación, Programación, IA, Redes
   - [OK]
 * - **ING**
   - Ingeniería
   - Ingeniería de Software, Arquitectura, Sistemas
   - [OK]
 * - **CIE**
   - Ciencias
   - Matemáticas, Estadística, Física, Biología Computacional
   - [OK]

**Total Categorías Activas:** 3




Tabla Maestra: Subcategorías
============================

Informática (INF)
=================

.. list-table:: Subcategorías INF
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **PRG**
   - Programación
   - Lenguajes, frameworks, paradigmas
   - [OK]
 * - **IAR**
   - Inteligencia Artificial
   - ML, DL, NLP, Computer Vision, Reinforcement Learning
   - [OK]
 * - **RED**
   - Redes
   - Protocolos, TCP/IP, seguridad de red
   - [OK]
 * - **SEG**
   - Seguridad
   - Ciberseguridad, criptografía, ethical hacking
   - [OK]
 * - **BDD**
   - Bases de Datos
   - SQL, NoSQL, diseño de esquemas, optimización
   - [OK]
 * - **SOP**
   - Sistemas Operativos
   - Linux, Windows, administración de sistemas
   - [OK]
 * - **WEB**
   - Desarrollo Web
   - HTML, CSS, desarrollo web general
   - [OK]
 * - **MOV**
   - Desarrollo Móvil
   - iOS, Android, multiplataforma
   - [OK]
 * - **DVC**
   - DevOps y Cloud
   - Docker, Kubernetes, CI/CD, AWS, Azure
   - [OK]
 * - **ALG**
   - Algoritmos
   - Estructuras de datos, análisis de complejidad
   - [OK]

**Total Subcategorías INF:** 10

Ingeniería (ING)
================

.. list-table:: Subcategorías ING
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **SIS**
   - Sistemas
   - Diseño de sistemas, sistemas distribuidos
   - [OK]
 * - **ARQ**
   - Arquitectura
   - Patrones arquitectónicos, microservicios
   - [OK]
 * - **MET**
   - Metodologías
   - Agile, Scrum, DevOps, Lean, Kanban
   - [OK]
 * - **REQ**
   - Requisitos
   - Ingeniería de requisitos, análisis
   - [OK]
 * - **PRU**
   - Pruebas
   - Testing, QA, TDD, automatización
   - [OK]
 * - **MOD**
   - Modelado
   - UML, BPMN, especificación formal
   - [OK]

**Total Subcategorías ING:** 6

Ciencias (CIE)
==============

.. list-table:: Subcategorías CIE
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **MAT**
   - Matemáticas
   - Álgebra, cálculo, matemáticas aplicadas
   - [OK]
 * - **EST**
   - Estadística
   - Probabilidad, análisis estadístico, inferencia
   - [OK]
 * - **FIS**
   - Física
   - Física computacional, simulaciones
   - [OK]
 * - **BIO**
   - Biología
   - Bioinformática, genómica, biología computacional
   - [OK]

**Total Subcategorías CIE:** 4

**TOTAL SUBCATEGORÍAS SISTEMA:** 20




Tabla Maestra: Especialidades
=============================

Programación (INF.PRG)
======================

.. list-table:: Especialidades INF.PRG
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **FST**
   - Full-Stack
   - Desarrollo completo (frontend + backend)
   - [OK]
 * - **FRE**
   - Frontend
   - Interfaces de usuario, UX
   - [OK]
 * - **BAC**
   - Backend
   - Lógica del servidor, APIs
   - [OK]
 * - **PYT**
   - Python
   - Lenguaje Python (general)
   - [OK]
 * - **JAV**
   - JavaScript
   - Lenguaje JavaScript (general)
   - [OK]
 * - **TSC**
   - TypeScript
   - Lenguaje TypeScript
   - [OK]
 * - **REA**
   - React
   - Biblioteca React / React ecosystem
   - [OK]
 * - **VUE**
   - Vue.js
   - Framework Vue
   - [OK]
 * - **ANG**
   - Angular
   - Framework Angular
   - [OK]
 * - **NOD**
   - Node.js
   - Runtime Node.js, desarrollo backend
   - [OK]
 * - **DJA**
   - Django
   - Framework Django (Python)
   - [OK]
 * - **FLA**
   - Flask
   - Framework Flask (Python)
   - [OK]
 * - **SPR**
   - Spring
   - Framework Spring (Java)
   - [OK]
 * - **NET**
   - .NET
   - Plataforma .NET y C#
   - [OK]
 * - **RUS**
   - Rust
   - Lenguaje Rust
   - [OK]
 * - **GOL**
   - Go
   - Lenguaje Go
   - [OK]
 * - **CPP**
   - C++
   - Lenguaje C++
   - [OK]
 * - **FUN**
   - Funcional
   - Programación funcional (Haskell, Lisp, Scala)
   - [OK]
 * - **GEN**
   - General
   - Múltiples tecnologías o programación general
   - [OK]

**Total Especialidades PRG:** 19

Inteligencia Artificial (INF.IAR)
=================================

.. list-table:: Especialidades INF.IAR
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **MLF**
   - Machine Learning Fundamentals
   - Machine Learning básico, algoritmos tradicionales
   - [OK]
 * - **DLE**
   - Deep Learning
   - Redes neuronales profundas, CNN, RNN
   - [OK]
 * - **NLP**
   - Natural Language Processing
   - Procesamiento de lenguaje natural, LLMs
   - [OK]
 * - **CVS**
   - Computer Vision
   - Visión por computadora, procesamiento de imágenes
   - [OK]
 * - **RFO**
   - Reinforcement Learning
   - Aprendizaje por refuerzo, Q-learning
   - [OK]

**Total Especialidades IAR:** 5

DevOps y Cloud (INF.DVC)
========================

.. list-table:: Especialidades INF.DVC
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **DOC**
   - Docker
   - Containerización con Docker
   - [OK]
 * - **KUB**
   - Kubernetes
   - Orquestación de contenedores
   - [OK]
 * - **AWS**
   - Amazon Web Services
   - Plataforma cloud de Amazon
   - [OK]
 * - **AZU**
   - Microsoft Azure
   - Plataforma cloud de Microsoft
   - [OK]
 * - **GCP**
   - Google Cloud Platform
   - Plataforma cloud de Google
   - [OK]
 * - **TER**
   - Terraform
   - Infrastructure as Code
   - [OK]
 * - **ANS**
   - Ansible
   - Automatización y configuration management
   - [OK]
 * - **JEN**
   - Jenkins
   - CI/CD y automatización
   - [OK]
 * - **GIT**
   - Git/GitHub/GitLab
   - Control de versiones
   - [OK]

**Total Especialidades DVC:** 9

Arquitectura (ING.ARQ)
======================

.. list-table:: Especialidades ING.ARQ
 :header-rows: 1
 :widths: 10 30 50 10

 * - Código
   - Nombre
   - Descripción
   - Estado
 * - **MIC**
   - Microservicios
   - Arquitectura de microservicios
   - [OK]
 * - **CLE**
   - Clean Architecture
   - Clean Architecture de Uncle Bob
   - [OK]
 * - **DDD**
   - Domain-Driven Design
   - Diseño guiado por dominio
   - [OK]
 * - **ARC**
   - arc42
   - Plantilla de documentación arc42
   - [OK]
 * - **HEX**
   - Hexagonal Architecture
   - Arquitectura hexagonal / Ports & Adapters
   - [OK]
 * - **GEN**
   - General
   - Arquitectura general o múltiples patrones
   - [OK]

**Total Especialidades ARQ:** 6

Otras Especialidades
====================

**Bases de Datos (INF.BDD):**

.. code-block:: text

 SQL -> Sistemas SQL (PostgreSQL, MySQL, etc.)
 NOS -> Sistemas NoSQL (MongoDB, Redis, etc.)
 GRA -> Bases de datos de grafos (Neo4j, etc.)
 GEN -> General / Múltiples sistemas

**Algoritmos (INF.ALG):**

.. code-block:: text

 STR -> Estructuras de datos
 SOR -> Algoritmos de ordenamiento
 GRA -> Algoritmos de grafos
 DYN -> Programación dinámica
 GEN -> General / Múltiples temas

**Sistemas (ING.SIS):**

.. code-block:: text

 DIS -> Sistemas distribuidos
 EMB -> Sistemas embebidos
 TRO -> Troubleshooting
 ARC -> Arquitectura de sistemas
 GEN -> General

**TOTAL ESPECIALIDADES DEFINIDAS:** 50+




Proceso de Aprobación de Nuevos Códigos
=======================================

Propuesta de Nueva Especialidad
===============================

**Plantilla:**

.. code-block:: rst

 PROPUESTA DE NUEVA ESPECIALIDAD
================================

 Solicitante: [Nombre]
 Fecha: [YYYY-MM-DD]

 Código Propuesto: [XXX]
 Nombre: [Nombre Completo]
 Categoría: [INF/ING/CIE]
 Subcategoría: [XXX]

 Justificación:
 - ¿Por qué se necesita?
 - ¿Cuántos libros potenciales?
 - ¿Es tendencia sostenida?

 Verificación de Colisiones:
 - ¿Código XXX ya existe? [NO]
 - ¿Especialidad similar ya existe? [NO]

 Libros que Usarían Este Código:
 1. [Libro 1]
 2. [Libro 2]

 Decisión: [ ] Aprobado [ ] Rechazado
 Fecha Decisión: [YYYY-MM-DD]
 Aprobado por: [Nombre]

Criterios de Aprobación
=======================

**SE APRUEBA si:**

[OK] Existe demanda real (3+ libros potenciales)
[OK] No existe especialidad similar
[OK] Código de 3 letras disponible y nemotécnico
[OK] Tecnología/área con momentum sostenido
[OK] No puede clasificarse en especialidad existente

**SE RECHAZA si:**

[ERROR] Solo 1-2 libros potenciales
[ERROR] Ya existe especialidad que cubre el tema
[ERROR] Tecnología muy nicho o temporal
[ERROR] Código propuesto ya en uso
[ERROR] Puede usar especialidad GEN (General)

Proceso de Registro
===================

**Pasos al aprobar nuevo código:**

1. **Actualizar META_BIB_003** (este documento)

 - Agregar a tabla correspondiente
 - Marcar estado como [OK]
 - Actualizar contador de especialidades

2. **Actualizar META_BIB_001**

 - Agregar a lista de códigos
 - Incluir en documentación

3. **Notificar al equipo**

 - Email a traductores
 - Actualizar wiki/documentación

4. **Actualizar herramientas**

 - Script de clasificación
 - Validadores

5. **Documentar en historial**

 - Registrar en changelog de este documento




Códigos Reservados
==================

Códigos NO Disponibles
======================

**Reservados para uso futuro:**

.. code-block:: text

 INF.BCK -> Blockchain (si surge demanda)
 INF.IOT -> Internet of Things
 INF.GAM -> Desarrollo de Videojuegos
 INF.VRA -> Realidad Virtual y Aumentada

 ING.OPS -> Operations / SRE
 ING.SEC -> DevSecOps

 CIE.QUI -> Química Computacional
 CIE.GEO -> Geociencias / GIS

**NO usar sin aprobación previa.**

Códigos Obsoletos
=================

**Actualmente:** Ninguno

*Si un código se marca como obsoleto, se documentará aquí con:*

- Código obsoleto
- Fecha de obsolescencia
- Razón
- Código de reemplazo (si aplica)




Tabla de Referencia Rápida
==========================

Códigos por Frecuencia de Uso Estimada
======================================

.. list-table:: Top 20 Especialidades (estimado)
 :header-rows: 1
 :widths: 5 15 30 50

 * - #
   - Código
   - Nombre
   - Código Completo Ejemplo
 * - 1
   - PYT
   - Python
   - INF.PRG.PYT.XXX
 * - 2
   - FST
   - Full-Stack
   - INF.PRG.FST.XXX
 * - 3
   - REA
   - React
   - INF.PRG.REA.XXX
 * - 4
   - JAV
   - JavaScript
   - INF.PRG.JAV.XXX
 * - 5
   - MLF
   - Machine Learning
   - INF.IAR.MLF.XXX
 * - 6
   - DOC
   - Docker
   - INF.DVC.DOC.XXX
 * - 7
   - KUB
   - Kubernetes
   - INF.DVC.KUB.XXX
 * - 8
   - NOD
   - Node.js
   - INF.PRG.NOD.XXX
 * - 9
   - TSC
   - TypeScript
   - INF.PRG.TSC.XXX
 * - 10
   - DJA
   - Django
   - INF.PRG.DJA.XXX
 * - 11
   - MIC
   - Microservicios
   - ING.ARQ.MIC.XXX
 * - 12
   - DLE
   - Deep Learning
   - INF.IAR.DLE.XXX
 * - 13
   - AWS
   - AWS
   - INF.DVC.AWS.XXX
 * - 14
   - CLE
   - Clean Architecture
   - ING.ARQ.CLE.XXX
 * - 15
   - NLP
   - NLP
   - INF.IAR.NLP.XXX
 * - 16
   - ANG
   - Angular
   - INF.PRG.ANG.XXX
 * - 17
   - VUE
   - Vue.js
   - INF.PRG.VUE.XXX
 * - 18
   - SQL
   - SQL Databases
   - INF.BDD.SQL.XXX
 * - 19
   - ARC
   - arc42
   - ING.ARQ.ARC.XXX
 * - 20
   - DDD
   - DDD
   - ING.ARQ.DDD.XXX

Índice Alfabético de Códigos
============================

.. code-block:: text

 ALG -> Algoritmos (INF.ALG)
 ANG -> Angular (INF.PRG.ANG)
 ANS -> Ansible (INF.DVC.ANS)
 ARC -> arc42 (ING.ARQ.ARC)
 ARQ -> Arquitectura (ING.ARQ)
 AWS -> Amazon Web Services (INF.DVC.AWS)
 AZU -> Microsoft Azure (INF.DVC.AZU)

 BAC -> Backend (INF.PRG.BAC)
 BDD -> Bases de Datos (INF.BDD)
 BIO -> Biología (CIE.BIO)

 CIE -> Ciencias (CIE)
 CLE -> Clean Architecture (ING.ARQ.CLE)
 CPP -> C++ (INF.PRG.CPP)
 CVS -> Computer Vision (INF.IAR.CVS)

 DDD -> Domain-Driven Design (ING.ARQ.DDD)
 DJA -> Django (INF.PRG.DJA)
 DLE -> Deep Learning (INF.IAR.DLE)
 DOC -> Docker (INF.DVC.DOC)
 DVC -> DevOps y Cloud (INF.DVC)

 EST -> Estadística (CIE.EST)

 FIS -> Física (CIE.FIS)
 FLA -> Flask (INF.PRG.FLA)
 FRE -> Frontend (INF.PRG.FRE)
 FST -> Full-Stack (INF.PRG.FST)
 FUN -> Funcional (INF.PRG.FUN)

 GCP -> Google Cloud Platform (INF.DVC.GCP)
 GEN -> General (múltiples subcategorías)
 GIT -> Git/GitHub/GitLab (INF.DVC.GIT)
 GOL -> Go (INF.PRG.GOL)

 HEX -> Hexagonal Architecture (ING.ARQ.HEX)

 IAR -> Inteligencia Artificial (INF.IAR)
 INF -> Informática (INF)
 ING -> Ingeniería (ING)

 JAV -> JavaScript (INF.PRG.JAV)
 JEN -> Jenkins (INF.DVC.JEN)

 KUB -> Kubernetes (INF.DVC.KUB)

 MAT -> Matemáticas (CIE.MAT)
 MET -> Metodologías (ING.MET)
 MIC -> Microservicios (ING.ARQ.MIC)
 MLF -> Machine Learning Fundamentals (INF.IAR.MLF)
 MOD -> Modelado (ING.MOD)
 MOV -> Desarrollo Móvil (INF.MOV)

 NET -> .NET (INF.PRG.NET)
 NLP -> Natural Language Processing (INF.IAR.NLP)
 NOD -> Node.js (INF.PRG.NOD)

 PRG -> Programación (INF.PRG)
 PRU -> Pruebas (ING.PRU)
 PYT -> Python (INF.PRG.PYT)

 REA -> React (INF.PRG.REA)
 RED -> Redes (INF.RED)
 REQ -> Requisitos (ING.REQ)
 RFO -> Reinforcement Learning (INF.IAR.RFO)
 RUS -> Rust (INF.PRG.RUS)

 SEG -> Seguridad (INF.SEG)
 SIS -> Sistemas (ING.SIS)
 SOP -> Sistemas Operativos (INF.SOP)
 SPR -> Spring (INF.PRG.SPR)

 TER -> Terraform (INF.DVC.TER)
 TSC -> TypeScript (INF.PRG.TSC)

 VUE -> Vue.js (INF.PRG.VUE)

 WEB -> Desarrollo Web (INF.WEB)




Estadísticas del Sistema
========================

Conteo Actual
=============

.. code-block:: text

 Total Categorías: 3
 Total Subcategorías: 20
 Total Especialidades: 50+

 Códigos Activos: 73+
 Códigos Reservados: 8
 Códigos Obsoletos: 0

 Combinaciones Posibles: 17,280 códigos únicos por categoría
 Capacidad Total Sistema: ~51,000 libros antes de colisiones

Distribución
============

.. code-block:: text

 INFORMÁTICA (INF):
 - Subcategorías: 10
 - Especialidades: ~40
 - Porcentaje: ~70%

 INGENIERÍA (ING):
 - Subcategorías: 6
 - Especialidades: ~10
 - Porcentaje: ~20%

 CIENCIAS (CIE):
 - Subcategorías: 4
 - Especialidades: ~5
 - Porcentaje: ~10%




Referencias
===========

Documentos Relacionados
=======================

- :doc:`META_BIB_001_Sistema_Clasificacion_1_0_0` - Sistema de clasificación
- :doc:`META_BIB_002_Guia_Organizacion_1_0_0` - Guía de organización
- :doc:`catalogo_numeros` - Registro de números asignados

Estándares
==========

- ISO 12620-2:2022 - Data category specifications
- Unicode Technical Standard #35 - Locale Data Markup Language




Historial de Versiones
======================

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
   - Versión inicial - 73+ códigos definidos




**Documento:** META_BIB_003_Esquema_Codificacion_1_0_0.rst
**Ubicación:** ``/biblioteca/_metadata_biblioteca/``
**Estado:** NORMATIVO
**Próxima revisión:** 2026-07-28
