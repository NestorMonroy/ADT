📚 ESTRUCTURA DE BIBLIOTECA - Versión Correcta
Cada Libro = Carpeta Completa
biblioteca/
│
├── _metadata_biblioteca/              # [PRIVADO] Metodología clasificación
│   ├── META_BIB_001_Sistema_Clasificacion_1_0_0.rst
│   ├── META_BIB_002_Guia_Organizacion_Jerarquica_1_0_0.rst
│   └── META_BIB_003_Esquema_Codificacion_1_0_0.rst
│
├── informatica/                        # Categoría principal (tu guía)
│   ├── programacion/                   # Subcategoría (tu guía)
│   │   ├── full_stack/                 # Especialidad (tu guía)
│   │   │   │
│   │   │   └── Modern_Full_Stack_Development_Zammetti_2ed/  # ✅ LIBRO COMPLETO
│   │   │       │
│   │   │       ├── metadata_libro.rst              # Info bibliográfica
│   │   │       ├── index.rst                       # Índice del libro
│   │   │       ├── glosario_acumulativo.rst        # Glosario completo
│   │   │       │
│   │   │       ├── Chapter_01_Server_Side_Action/
│   │   │       │   ├── original/
│   │   │       │   │   └── chapter_01.pdf         # Original en inglés
│   │   │       │   ├── traduccion/
│   │   │       │   │   └── capitulo_01.rst        # Traducción español
│   │   │       │   ├── glosario_capitulo.rst      # Términos del capítulo
│   │   │       │   ├── notas_traduccion.rst       # Notas específicas
│   │   │       │   └── figuras/
│   │   │       │       ├── fig_01_01.png
│   │   │       │       └── fig_01_02.png
│   │   │       │
│   │   │       ├── Chapter_02_Advanced_Node_NPM/
│   │   │       │   ├── original/
│   │   │       │   ├── traduccion/
│   │   │       │   ├── glosario_capitulo.rst
│   │   │       │   ├── notas_traduccion.rst
│   │   │       │   └── figuras/
│   │   │       │
│   │   │       ├── Chapter_03_Client_Side_React/
│   │   │       │   ├── original/
│   │   │       │   ├── traduccion/
│   │   │       │   ├── glosario_capitulo.rst
│   │   │       │   ├── notas_traduccion.rst
│   │   │       │   └── figuras/
│   │   │       │
│   │   │       ├── Chapter_04_Advanced_React/
│   │   │       ├── Chapter_05_TypeScript_Foundation/
│   │   │       ├── Chapter_06_Advanced_TypeScript/
│   │   │       ├── Chapter_07_Webpack/
│   │   │       ├── Chapter_08_MailBag_Server/
│   │   │       ├── Chapter_09_MailBag_Client/
│   │   │       ├── Chapter_10_BattleJong_Server/
│   │   │       ├── Chapter_11_BattleJong_Client/
│   │   │       ├── Chapter_12_Docker/
│   │   │       ├── Chapter_13_Fooderator_Server/
│   │   │       ├── Chapter_14_Fooderator_Client/
│   │   │       │
│   │   │       ├── appendices/
│   │   │       │   ├── appendix_A/
│   │   │       │   └── appendix_B/
│   │   │       │
│   │   │       ├── front_matter/
│   │   │       │   ├── about_author.rst
│   │   │       │   ├── about_technical_reviewer.rst
│   │   │       │   ├── acknowledgments.rst
│   │   │       │   └── introduction.rst
│   │   │       │
│   │   │       └── back_matter/
│   │   │           └── index_alfabetico.rst
│   │   │
│   │   └── python/
│   │       └── Python_Programming_Doe_2024/
│   │
│   └── inteligencia_artificial/
│       └── ML_Handbook_Smith_2025/
│
├── ingenieria/
│   └── sistemas/
│       └── SysML_Guide_Jones_2023/
│
└── ciencias/
    └── biologia/
        └── Systems_Biology_Brown_2022/

📋 METADATA DEL LIBRO
metadata_libro.rst
rst.. meta::
   :libro_id: LIB_INF_FST_001
   :tipo: Libro_Tecnico
   :estado: En_Traduccion
   :progreso: 35%
   :clasificacion: INF.PRG.FST.001

==========================================================================
Modern Full-Stack Development (2nd Edition)
==========================================================================

Información Bibliográfica
==========================

Título Original
   Modern Full-Stack Development: Using TypeScript, React, Node.js, 
   Webpack, Python, Django, and Docker (Second Edition)

Título Traducido
   Desarrollo Full-Stack Moderno: Usando TypeScript, React, Node.js,
   Webpack, Python, Django y Docker (Segunda Edición)

Autor
   Frank Zammetti

Editorial
   Apress

Año Publicación
   2024

ISBN
   978-1-4842-xxxx-x

Páginas
   517 páginas

Idiomas
   - Fuente: Inglés (en)
   - Destino: Español (es)

Clasificación según Guía Metodológica
======================================

Código Clasificación
   INF.PRG.FST.001

Categoría Principal
   Informática

Subcategoría
   Programación

Especialidad
   Full-Stack Development

Subtemas
   - TypeScript
   - React
   - Node.js
   - Webpack
   - Python
   - Django
   - Docker

Nivel
   Intermedio-Avanzado

Público Objetivo
   Desarrolladores web, Ingenieros de software

Palabras Clave
   Full-stack, TypeScript, React, Node.js, Python, Django, Docker,
   Desarrollo web, Aplicaciones modernas

Estado de Traducción
=====================

Progreso Global
   35% completado (5 de 14 capítulos)

Capítulos Completados
   ✅ Chapter 01: Server-Side Action: Node and NPM
   ✅ Chapter 02: A Few More Words: Advanced Node and NPM
   ✅ Chapter 03: Client-Side Adventures: React
   ✅ Chapter 04: A Few More Words: Advanced React
   ✅ Chapter 05: Building a Strong Foundation: TypeScript

Capítulos En Proceso
   🔄 Chapter 06: A Few More Words: Advanced TypeScript (60%)

Capítulos Pendientes
   ⏳ Chapter 07: Tying It Up in a Bow: Webpack
   ⏳ Chapter 08: Delivering the Goods: MailBag, the Server
   ⏳ Chapter 09: Delivering the Goods: MailBag, the Client
   ⏳ Chapter 10: Time for Fun: BattleJong, the Server
   ⏳ Chapter 11: Time for Fun: BattleJong, the Client
   ⏳ Chapter 12: Bringing the Dev Ship into Harbor: Docker
   ⏳ Chapter 13: Feed Your Face: Fooderator, the Server
   ⏳ Chapter 14: Feed Your Face: Fooderator, the Client

Fecha Inicio
   2025-11-15

Fecha Estimada Finalización
   2026-03-30

Equipo de Traducción
====================

Traductor Principal
   María García

Revisores Técnicos
   - Juan Pérez (Capítulos 1-7)
   - Ana López (Capítulos 8-14)

Especialistas Consultados
   - Carlos Ruiz (TypeScript/JavaScript)
   - Laura Martínez (Python/Django)
   - Diego Fernández (Docker/DevOps)

Estadísticas de Traducción
===========================

Total Páginas Original
   517 páginas

Total Páginas Traducidas
   180 páginas (35%)

Términos Técnicos Identificados
   1,247 términos únicos

Términos en Glosario
   892 términos documentados

Figuras
   - Total: 127 figuras
   - Traducidas: 45 figuras
   - Adaptadas: 45 figuras

Tablas
   - Total: 68 tablas
   - Traducidas: 24 tablas

Ejemplos de Código
   - Total: 312 ejemplos
   - Sin traducir (preservados): 312 ejemplos
   - Comentarios traducidos: 156 ejemplos

Procedimientos Aplicados
=========================

Workflow
   :doc:`/procedimientos/PROC_001_Workflow_General_1_0_0`

Modo Traducción
   Alta Fidelidad + Marcado Visual
   :doc:`/procedimientos/PROC_002_Alta_Fidelidad_1_0_0`

Marcado Términos
   Primera aparición marcada con marcado visual
   :doc:`/procedimientos/PROC_003_Marcado_Visual_1_0_0`

Formato Destino
   reStructuredText (Sphinx)
   :doc:`/herramientas_medios/sphinx/REF_005_Directivas_RST_1_0_0`

Control de Calidad
==================

Verificaciones por Capítulo
   - ✅ Checklist contenido completo
   - ✅ Checklist términos marcados primera aparición
   - ✅ Checklist formato preservado
   - ✅ Checklist fidelidad estructural
   - ✅ Checklist referencias cruzadas

Revisiones
   - 1ª revisión técnica: Completada (Capítulos 1-5)
   - 2ª revisión estilo: Pendiente

Errores Detectados
   - Capítulo 1: 2 errores corregidos
   - Capítulo 2: 1 error corregido
   - Capítulo 3: 3 errores corregidos
   - Capítulo 4: 1 error corregido
   - Capítulo 5: 2 errores corregidos

Archivos y Recursos
===================

Archivo Fuente Original
   ``/uploads/modern_fullstack_dev_2ed.pdf``

Repositorio Fuente (si existe)
   https://github.com/Apress/modern-full-stack-development-2ed

Carpeta Traducción
   ``/biblioteca/informatica/programacion/full_stack/Modern_Full_Stack_Development_Zammetti_2ed/``

Glosario Acumulativo
   :doc:`glosario_acumulativo`

Build Sphinx
   ``make html`` en carpeta raíz del libro

Notas Especiales
================

Consideraciones Técnicas
   - Ejemplos de código NO se traducen (preservar sintaxis)
   - Comentarios de código SÍ se traducen
   - Nombres de variables NO se traducen
   - Nombres de archivos NO se traducen
   - URLs NO se traducen

Terminología Específica
   - "Full-stack" se mantiene sin traducir (anglicismo aceptado)
   - "Framework" se mantiene sin traducir
   - "Docker container" → "contenedor Docker"
   - "Webpack" NO se traduce (nombre propio)

Decisiones de Traducción
   - Tú formal (usted) vs informal (tú): INFORMAL (coherente con estilo original)
   - Voz pasiva: Minimizar (preferir voz activa)
   - Género: Lenguaje inclusivo cuando sea posible

Referencias Cruzadas
====================

Libros Relacionados en Biblioteca
   - :doc:`../react/React_Advanced_Patterns_Lee_2024/index`
   - :doc:`../typescript/TypeScript_Deep_Dive_Chen_2023/index`
   - :doc:`../../devops/docker/Docker_Complete_Guide_Kumar_2024/index`

Procedimientos de Traducción Relacionados
   - :doc:`/procedimientos/PROC_001_Workflow_General_1_0_0`
   - :doc:`/reglas_operativas/RT_001_Primera_Aparicion_Terminos_1_0_0`
   - :doc:`/casos_practicos/SUCCESS_001_Full_Stack_Book_1_0_0`

Historial de Versiones Traducción
==================================

.. list-table::
   :widths: 10 15 15 60
   :header-rows: 1

   * - Versión
     - Fecha
     - Responsable
     - Cambios
   * - 0.35.0
     - 2026-01-08
     - M. García
     - Completado Capítulo 5, iniciado Capítulo 6
   * - 0.28.0
     - 2025-12-20
     - M. García
     - Completado Capítulo 4
   * - 0.21.0
     - 2025-12-05
     - M. García
     - Completado Capítulo 3
   * - 0.14.0
     - 2025-11-25
     - M. García
     - Completado Capítulo 2
   * - 0.07.0
     - 2025-11-20
     - M. García
     - Completado Capítulo 1, setup inicial

----

**Última actualización:** 2026-01-08

📂 ESTRUCTURA DE CAPÍTULO
Chapter_01_Server_Side_Action/traduccion/capitulo_01.rst
rst.. meta::
   :capitulo: 01
   :titulo_original: Server-Side Action: Node and NPM
   :estado: Completado
   :fecha_traduccion: 2025-11-20
   :revisor: Juan Pérez

===============================================
Capítulo 1: Acción del Lado del Servidor: Node y NPM
===============================================

.. contents:: Contenido del Capítulo
   :depth: 3
   :local:

----

De los Entornos de Ejecución de JavaScript y la Construcción de (Mayormente) Servidores
========================================================================================

JavaScript, durante mucho tiempo, fue el lenguaje de programación que vivía
exclusivamente en el navegador web. Sin embargo, en 2009, Ryan Dahl introdujo
**Node.js** (en su :term:`primera aparición <Node.js>`\ [#primera_nodejs]_), un entorno
de ejecución que permite ejecutar JavaScript fuera del navegador...

[Contenido traducido del capítulo...]

Primeros Pasos con Node: Instalación
====================================

Para comenzar a trabajar con Node, primero necesitas instalarlo. El proceso
de instalación varía según tu sistema operativo...

[Contenido traducido...]

.. [#primera_nodejs] **Node.js**: Entorno de ejecución de JavaScript construido
   sobre el motor V8 de Chrome, que permite ejecutar JavaScript del lado del
   servidor. Véase :ref:`glosario-nodejs`.

.. _seccion-npm:

El Compañero del Crimen de Node: NPM
=====================================

**NPM** (en su :term:`primera aparición <NPM>`\ [#primera_npm]_) significa
**Node Package Manager**...

[Contenido traducido...]

.. [#primera_npm] **NPM** (Node Package Manager): Gestor de paquetes predeterminado
   para Node.js, que facilita la instalación, actualización y gestión de
   bibliotecas y dependencias. Véase :ref:`glosario-npm`.

🔤 GLOSARIO DEL CAPÍTULO
Chapter_01_Server_Side_Action/glosario_capitulo.rst
rst.. _glosario-capitulo-01:

========================================
Glosario - Capítulo 1: Node y NPM
========================================

Este glosario contiene todos los términos técnicos identificados en el
Capítulo 1, con su primera aparición marcada en el texto principal.

.. glossary::
   :sorted:

   Node.js
      Entorno de ejecución de JavaScript construido sobre el motor V8 de Chrome.
      Permite ejecutar código JavaScript fuera del navegador, típicamente del
      lado del servidor.
      
      **Primera aparición:** Página 2, Sección "De los Entornos de Ejecución"
      
      **Contexto:** "Ryan Dahl introdujo Node.js en 2009..."
      
      **Ver también:** :term:`V8 Engine`, :term:`JavaScript Runtime`

   NPM
   Node Package Manager
      Gestor de paquetes predeterminado para el ecosistema Node.js. Facilita
      la instalación, actualización, y gestión de bibliotecas y dependencias
      de JavaScript.
      
      **Primera aparición:** Página 9, Sección "El Compañero del Crimen de Node"
      
      **Sinónimos:** Node Package Manager
      
      **Comandos principales:**
      
      - ``npm install``: Instala dependencias
      - ``npm init``: Inicializa proyecto
      - ``npm update``: Actualiza paquetes
      
      **Ver también:** :term:`package.json`, :term:`node_modules`

   package.json
      Archivo de configuración en formato JSON que describe un proyecto Node.js.
      Contiene metadata del proyecto y lista de dependencias.
      
      **Primera aparición:** Página 12, Sección "Inicializando un Nuevo Proyecto"
      
      **Estructura básica:**
      
      .. code-block:: json
      
         {
           "name": "mi-proyecto",
           "version": "1.0.0",
           "dependencies": {}
         }
      
      **Ver también:** :term:`npm`, :term:`semantic versioning`

   semantic versioning
   versionado semántico
      Sistema de versionado que utiliza tres números: MAJOR.MINOR.PATCH
      (por ejemplo, 2.1.5).
      
      **Primera aparición:** Página 16, Sección "Aside: Semantic Versioning"
      
      **Reglas:**
      
      - **MAJOR**: Cambios incompatibles en API
      - **MINOR**: Nueva funcionalidad compatible
      - **PATCH**: Correcciones de errores compatibles
      
      **Ejemplo:** ``^1.2.3`` permite versiones ``>=1.2.3 <2.0.0``

   V8 Engine
   motor V8
      Motor de JavaScript de código abierto desarrollado por Google, utilizado
      en Chrome y Node.js para ejecutar código JavaScript.
      
      **Primera aparición:** Página 3, Sección "Runtimes de JavaScript"
      
      **Características:**
      
      - Compilación Just-In-Time (JIT)
      - Optimización de rendimiento
      - Gestión de memoria

   JavaScript Runtime
   entorno de ejecución de JavaScript
      Entorno que proporciona las capacidades necesarias para ejecutar código
      JavaScript, incluyendo el motor de JavaScript, APIs y event loop.
      
      **Primera aparición:** Página 2, Título de sección

[... más términos ...]

----

**Total de términos en este capítulo:** 42 términos
**Términos nuevos (no aparecen en capítulos anteriores):** 42 términos
```

---

## 📊 APLICACIÓN DE TU GUÍA METODOLÓGICA

### 1. Ámbito General
**¿Qué organizo?** → Libros técnicos traducidos

### 2. Categorías Principales
- Informática
- Ingeniería
- Ciencias

### 3. Subcategorías (Informática)
- Programación
- Inteligencia Artificial
- Redes
- Seguridad

### 4. Subniveles (Programación)
- Full-Stack
- Frontend
- Backend
- Python
- JavaScript/TypeScript

### 5. Códigos de Clasificación
```
INF.PRG.FST.001 → Modern Full-Stack Development
│   │   │   │
│   │   │   └── Número secuencial
│   │   └────── Especialidad (FST = Full-Stack)
│   └────────── Subcategoría (PRG = Programación)
└────────────── Categoría (INF = Informática)