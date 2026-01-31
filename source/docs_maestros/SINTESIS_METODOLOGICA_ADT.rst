Síntesis Metodológica: Fundamentos Teóricos y Prácticos de ADT
==============================================================

:Autor: Equipo ADT
:Fecha: 2026-01-27
:Versión: 1.0
:Estado: NORMATIVO - Base Metodológica del Proyecto
:Tipo: Documento de Síntesis

.. contents:: Contenido
 :depth: 3
 :local:




Propósito de Este Documento
===========================

Este documento integra y sintetiza los **12 documentos maestros** del proyecto ADT,
estableciendo las conexiones entre teoría y práctica, y demostrando cómo los
fundamentos metodológicos de traducción se aplican específicamente a ADT.

**Pregunta central:**
 ¿Cómo traducimos documentación técnica preservando fidelidad semántica
 mientras adaptamos forma a nuevos medios (LaTeX->RST->HTML)?




Parte 1: Fundamentos Metodológicos
==================================

1.1. Base Teórica: Método de Traducción Peshitta
================================================

Del documento :doc:`METODO_TRADUCCION_PESHITTA_ZACHARIAS`:


**Método por Defecto** (Micheli, 2014):

.. code-block:: text

 SEGMENTACIÓN: Nivel de frase (phrase-level)
 RENDICIÓN: Nivel de palabra (word-level)
 PREFERENCIA: Signifié (sentido) sobre Signifiant (forma)

**Aplicación a ADT:**

.. list-table::
 :header-rows: 1
 :widths: 30 35 35

 * - Aspecto
   - Peshitta Zacarías
   - ADT (Traducción Técnica)
 * - **Segmentación**
   - Frase hebrea -> Frase siríaca
   - Sección LaTeX -> Sección RST
 * - **Rendición**
   - Palabra por palabra
   - Elemento por elemento (comando, entorno)
 * - **Preferencia**
   - Sentido sobre forma
   - Semántica sobre sintaxis

**Ejemplo Concreto:**

.. code-block:: latex

 % LaTeX (Texto Fuente)
 \textbf{importante}

 % Signifiant: La FORMA \textbf{}
 % Signifié: El SENTIDO "énfasis fuerte"

.. code-block:: rst

 # RST (Texto Destino)
 **importante**

 # Preserva: Signifié (énfasis fuerte) [OK]
 # Cambia: Signifiant (de \textbf{} a **) [OK]

1.2. Los Cuatro Objetivos de Traducción
=======================================

Del análisis Peshitta, aplicados a ADT:


**Objetivo 1: Domesticación**
 Adaptar al medio destino (RST/Sphinx) sin traicionar el contenido

 .. code-block:: rst

 % LaTeX: \begin{itemize} \item ... \end{itemize}

 # RST: - ... (domesticado a RST)

**Objetivo 2: Claridad**
 Hacer comprensible para lectores españoles sin conocimiento de LaTeX

 .. code-block:: rst

 % LaTeX: \ensuremath{\alpha}

 # RST: α (más claro en español)

**Objetivo 3: Consistencia**
 Resolver inconsistencias del original

 .. code-block:: rst

 % Capítulo 1: uses \textbf{}
 % Capítulo 5: uses \emph{} for same purpose

 # RST: Unificar a **énfasis** en ambos

**Objetivo 4: Simplificación**
 Reducir complejidad innecesaria

 .. code-block:: rst

 % LaTeX: \begin{center}\textbf{..}\end{center}

 # RST: **..** (centrado no semántico, se elimina)

1.3. Las 14+ Tácticas Identificadas
===================================

Del método Peshitta, mapeadas a ADT:

.. list-table::
 :header-rows: 1
 :widths: 20 30 50

 * - Táctica
   - Ejemplo Peshitta
   - Aplicación ADT
 * - **Adición**
   - Agregar artículo para claridad
   - ``.. note::`` para aclarar contexto
 * - **Omisión**
   - Omitir partícula redundante
   - Omitir ``\noindent`` (no semántico en RST)
 * - **Sustitución**
   - Sustituir nombre propio
   - ``\texttt{code}`` -> ````code````
 * - **Cambio orden**
   - Sujeto-Verbo -> Verbo-Sujeto
   - Mover figuras cerca del texto referido
 * - **Especificación**
   - "él" -> "José"
   - `:term:`concepto`` para términos técnicos
 * - **Generalización**
   - "José hijo de Jacob" -> "José"
   - ``\textbf{}`` + ``\emph{}`` -> ``**énfasis**``
 * - **Explicación**
   - Agregar glosa
   - Agregar ``:doc:`` para refs cruzadas
 * - **Normalización**
   - Unificar variantes
   - Unificar títulos de secciones

1.4. Niveles de Análisis (Macro vs Micro)
=========================================

**Nivel Macro (Global Translation Technique):**
 Decisiones estratégicas del libro completo

 - ¿Modo 1 (Alta Fidelidad) o Modo 2 (Marcado Visual)?
 - ¿Qué preservar? ¿Qué adaptar?
 - ¿Audiencia objetivo?

**Nivel Micro (Local Translation Technique):**
 Decisiones tácticas elemento por elemento

 - ¿Cómo traducir este ``\section{}`` específico?
 - ¿Este ``\emph{}`` es semántico o estilístico?
 - ¿Preservar este espacio vertical?




Parte 2: Arquitectura y Estructura
==================================

2.1. Arquitectura IACT v2.0.0
=============================

Del documento :doc:`ARQUITECTURA_TRADUCCION_IACT`:


**34 Prefijos de Nomenclatura:**

Organizados en 3 categorías:


1. **Procedimientos** (30 prefijos):
 
 - PROC: Procedimientos
 - STD: Estándares
 - RT: Reglas de traducción
 - MD: Matrices de decisión
 - etc.

2. **Metadata** (2 prefijos):
 
 - META: Metadata proyecto
 - METH: Metodologías

3. **Biblioteca** (4 prefijos):
 
 - LIB: Libros traducidos
 - CAT: Catálogos
 - META_BIB: Metadata biblioteca
 - GLOS_BIB: Glosarios biblioteca

**Base en Estándares ISO:**

.. list-table::
 :header-rows: 1
 :widths: 30 70

 * - Estándar
   - Aplicación en ADT
 * - ISO 1087:2019
   - Fundamentos conceptuales, ontología terminológica
 * - ISO 704:2022
   - Metodologías de traducción
 * - ISO 12620-2:2022
   - Gestión de repositorios terminológicos
 * - ISO 16642:2017
   - Terminological Markup Framework
 * - ISO 30042:2019
   - TermBase eXchange (TBX)

2.2. Estructura del Proyecto
============================

Del documento :doc:`REGLAS_ESTRUCTURA_PROYECTO`:


**Regla Maestra:**

.. important::
 Solo va a ``source/`` el contenido que se documenta/compila en HTML.

 Las herramientas y scripts de proyecto quedan en la raíz.

**Estructura Actual:**

.. code-block:: text

 /tmp/ADT/
 +-- source/ [STAR] TODO EL CONTENIDO
 | +-- 01-10_*/ Metodología (10 secciones)
 | +-- biblioteca/arc42/ arc42 (3/12 secciones)
 | +-- diataxis/ Framework
 | +-- docs/ Docs técnicas
 | +-- docs_maestros/ [STAR] 12 documentos fundamentales
 +-- config/ Configuraciones
 +-- scripts/ Automatización
 +-- tools/ Herramientas




Parte 3: Aplicación Práctica
============================

3.1. Del Método Peshitta a Procedimientos ADT
=============================================

**Traducción del Marco Conceptual:**

.. code-block:: text

   PESHITTA ZACARÍAS -> ADT
   =========================
   Texto fuente (hebreo) -> Documento LaTeX
   Texto destino (siríaco) -> Documento RST/HTML
   Técnica de traducción -> Procedimiento de conversión
   Método por defecto -> PROC_002: Workflow General
   Objetivos (4) -> STD_007: Criterios Fidelidad
   Tácticas (14+) -> RT_XXX: Reglas específicas
   Errores/Divergencias -> ERR_XXX: Errores comunes
   Validación -> Verificación de calidad

3.2. Creación de Procedimientos Basados en Método Peshitta
==========================================================

**PROC_002: Workflow General** (FASE 1 MVP)

Estructura basada en método Peshitta:


1. **Análisis del Texto Fuente**

 - Identificar estructura (secciones, subsecciones)
 - Mapear comandos LaTeX a elementos RST
 - Detectar inconsistencias originales

2. **Aplicar Método por Defecto**

 - Segmentación: Nivel de sección
 - Rendición: Nivel de comando
 - Preferencia: Signifié (semántica)

3. **Aplicar Tácticas según Objetivos**

 - Domesticación: Adaptar a RST
 - Claridad: Aclaraciones con ``.. note::``
 - Consistencia: Unificar nomenclatura
 - Simplificación: Eliminar no-semántico

4. **Validación**

 - Compilar Sphinx (``make html``)
 - Verificar preservación semántica
 - Revisar calidad tipográfica

**Ejemplo de Regla de Traducción:**

.. code-block:: rst

   RT_001: Traducción de Énfasis
   ==============================

   Método por Defecto:
   ====================
   LaTeX: \textbf{texto} -> RST: **texto**
   LaTeX: \emph{texto} -> RST: *texto*

   Tácticas:
   ==========
   - Si \textbf{} usado para definiciones -> ``:term:`texto```
   - Si \emph{} usado para código -> ````texto````
   - Si ambos en misma frase -> Unificar a uno solo

   Objetivo: Claridad + Consistencia

3.3. Integración con PLAN_CONTENIDO
===================================

**Actualización de FASE 1 (MVP):**

Con base en método Peshitta, los documentos CRÍTICOS de FASE 1 ahora tienen
fundamento metodológico explícito:


**01_fundamentos/glosario_traduccion.rst**
 Base: ISO 1087 + Terminología Peshitta

 Incluirá:
 
 - Signifiant vs Signifié
 - Segmentación
 - Rendición
 - Domesticación
 - etc.

**02_procedimientos/workflow_general.rst**
 Base: Método por Defecto (Micheli)

 Estructura:
 
 1. Análisis texto fuente
 2. Aplicar método por defecto
 3. Aplicar tácticas
 4. Validar

**08_prompts/prompt_maestro_latex.rst**
 Base: 14+ Tácticas Peshitta

 Incluirá:
 
 - Instrucciones para cada táctica
 - Objetivos de traducción
 - Casos de uso




Parte 4: Conexiones Entre Documentos Maestros
=============================================

4.1. Mapa de Relaciones
=======================

.. code-block:: text

 DOCUMENTOS MAESTROS (12)
=========================

 FUNDAMENTOS METODOLÓGICOS
 +- METODO_TRADUCCION_PESHITTA_ZACHARIAS [STAR] Base teórica
 +- ARQUITECTURA_DOCUMENTAL_TRADUCCION Aplicación práctica
 +- SINTESIS_METODOLOGICA_ADT [STAR] Este documento

 ARQUITECTURA Y ESTRUCTURA
 +- ARQUITECTURA_TRADUCCION_IACT Sistema completo
 +- REGLAS_ESTRUCTURA_PROYECTO Reglas operativas
 +- ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta Organización biblioteca

 PLANIFICACIÓN Y DESARROLLO
 +- PLAN_CONTENIDO Qué crear (FASES 1-5)
 +- PLAN_INCREMENTAL_CON_ARCHIVADO Cómo reorganizar
 +- PLAN_FINAL_REORGANIZACION Visión completa
 +- PROPUESTA_REORGANIZACION* Propuestas históricas

 HERRAMIENTAS Y PROMPTS
 +- PROMPT_MAESTRO_SPHINX_TRADUCCION Automatización

4.2. Flujo de Uso
=================

**Para un nuevo traductor:**

1. **Empezar con:** :doc:`SINTESIS_METODOLOGICA_ADT` (este documento)

 - Entender fundamentos Peshitta
 - Ver aplicación a ADT
 - Comprender objetivos y tácticas

2. **Revisar:** :doc:`METODO_TRADUCCION_PESHITTA_ZACHARIAS`

 - Profundizar en método
 - Estudiar ejemplos detallados
 - Entender conexiones MDA/MDE

3. **Consultar:** :doc:`ARQUITECTURA_TRADUCCION_IACT`

 - Aprender nomenclatura (34 prefijos)
 - Entender estructura carpetas
 - Conocer estándares ISO

4. **Aplicar:** :doc:`PLAN_CONTENIDO`

 - Ejecutar FASE 1 (MVP)
 - Crear documentos faltantes
 - Seguir procedimientos

5. **Usar:** :doc:`PROMPT_MAESTRO_SPHINX_TRADUCCION`

 - Automatizar traducciones
 - Aplicar tácticas consistentemente
 - Validar resultados




Parte 5: Isomorfismo Metodológico
=================================

5.1. Traducción ≈ Transformación de Modelos
===========================================

**Demostración del Isomorfismo:**

.. list-table::
 :header-rows: 1
 :widths: 30 35 35

 * - Concepto
   - Translation Studies
   - MDA/MDE
 * - **Entrada**
   - Texto fuente
   - Platform-Independent Model (PIM)
 * - **Salida**
   - Texto destino
   - Platform-Specific Model (PSM)
 * - **Proceso**
   - Técnica de traducción
   - Reglas de transformación
 * - **Método por defecto**
   - Segmentación + Rendición
   - Mapeo básico
 * - **Divergencias**
   - Tácticas para objetivos
   - Optimizaciones / Adaptaciones
 * - **Errores**
   - Divergencias no intencionales
   - Bugs en transformación
 * - **Validación**
   - Revisión semántica
   - Model checking / Testing

5.2. Valor de Esta Conexión
===========================

**¿Por qué importa el isomorfismo?**

1. **Rigor metodológico:**
  Translation Studies tiene 50+ años de investigación rigurosa

2. **Transferencia de conocimiento:**
  Técnicas probadas en traducción -> Aplicables a transformaciones

3. **Mejores prácticas:**
 - Método por defecto + divergencias
 - Objetivos explícitos
 - Tácticas catalogadas
 - Validación sistemática

4. **Base teórica sólida:**
  No "inventamos" metodología, la **adaptamos** de campo maduro




Parte 6: Aplicación Inmediata
=============================

6.1. Actualización de PLAN_CONTENIDO (FASE 1)
=============================================

**Con base metodológica Peshitta, FASE 1 ahora incluye:**

**01_fundamentos/** (3 documentos -> 5 documentos):

.. code-block:: text

 ANTES:
 +- index.rst
 +- glosario_traduccion.rst
 +- principios_fundamentales.rst

 AHORA (actualizado):
 +- index.rst
 +- glosario_traduccion.rst Incluye terminología Peshitta
 +- principios_fundamentales.rst Basado en método por defecto
 +- metodo_segmentacion.rst [STAR] NUEVO: De Peshitta
 +- objetivos_tacticas.rst [STAR] NUEVO: 4 objetivos, 14+ tácticas

**02_procedimientos/** (6 documentos):

.. code-block:: text

 +- index.rst
 +- workflow_general.rst Estructura de método Peshitta
 +- modo_alta_fidelidad/index.rst Basado en "Signifié"
 +- modo_marcado_visual/index.rst Basado en "Signifiant"
 +- verificacion_calidad/index.rst Validación sistemática
 +- correccion_errores/index.rst Tipos de divergencias

**08_prompts/** (6 documentos):

.. code-block:: text

 +- index.rst
 +- prompt_maestro_latex.rst 14+ tácticas implementadas
 +- prompt_maestro_sphinx.rst Ya existe en docs_maestros
 +- prompt_maestro_markdown.rst
 +- prompts_condicionales/index.rst
 +- plantillas/index.rst

6.2. Plantilla de Procedimiento Basado en Peshitta
==================================================

**Estructura estándar para PROC_XXX:**

.. code-block:: rst

   PROC_XXX: [Nombre del Procedimiento]
   =====================================

   :Base Metodológica: Método Peshitta (Micheli, 2014)
   :Objetivos: [Lista de objetivos aplicables]
   :Tácticas: [Lista de tácticas aplicables]

   1. Método por Defecto
   ======================

   Segmentación:
   ==============
   - Nivel: [frase/palabra/sección/capítulo]
   - Justificación: [...]

   Rendición:
   ===========
   - Nivel: [elemento/comando/palabra]
   - Preferencia: Signifié/Signifiant

   2. Aplicación de Tácticas
   ==========================

   Para Objetivo 1 (Domesticación):
   =================================
   - Táctica A: [...]
   - Táctica B: [...]

   Para Objetivo 2 (Claridad):
   ============================
   - Táctica C: [...]

   [etc.]

   3. Validación
   ==============

   - Verificar preservación semántica
   - Compilar y revisar HTML
   - Checklist de calidad

   4. Ejemplos
   ============

   [Ejemplos concretos paso a paso]




Parte 7: Conclusiones y Próximos Pasos
======================================

7.1. Síntesis de Síntesis
=========================

**Este proyecto ADT tiene ahora:**

1. **Base teórica sólida:**
 - Método Peshitta (50+ años Translation Studies)
 - Arquitectura IACT (estándares ISO)
 - Isomorfismo con MDA/MDE

2. **Base práctica clara:**
 - 34 prefijos de nomenclatura
 - Estructura de carpetas rigurosa
 - Plan de contenido en 5 fases

3. **Base metodológica explícita:**
 - Método por defecto
 - 4 objetivos
 - 14+ tácticas
 - Validación sistemática

4. **Base de conocimiento completa:**
 - 12 documentos maestros
 - Conexiones explícitas
 - Flujo de uso claro

7.2. Próximos Pasos Inmediatos
==============================

**FASE 1 (MVP) - Actualizada con Base Metodológica:**

1. **01_fundamentos/glosario_traduccion.rst** (2 horas)

 - Incluir terminología Peshitta
 - Definir Signifiant vs Signifié
 - Mapear a ADT

2. **01_fundamentos/principios_fundamentales.rst** (1 hora)

 - Basarse en método por defecto
 - Explicar segmentación/rendición
 - Aplicar a traducción técnica

3. **02_procedimientos/workflow_general.rst** (2 horas)

 - Estructura según Peshitta
 - 4 pasos principales
 - Ejemplos concretos

4. **08_prompts/prompt_maestro_latex.rst** (1.5 horas)

 - Implementar 14+ tácticas
 - Sistema de objetivos
 - Validación automática

**Total FASE 1:** 6.5 horas (reducido de 7-8h)

7.3. Valor Agregado de Esta Síntesis
====================================

**Antes de este documento:**
 - 12 documentos maestros independientes
 - Sin conexiones explícitas
 - Difícil de navegar

**Después de este documento:**
 - Base metodológica unificada
 - Conexiones claras entre documentos
 - Flujo de uso definido
 - Aplicación práctica inmediata
 - Fundamento teórico sólido




Referencias
===========

Documentos Maestros ADT
=======================

1. :doc:`METODO_TRADUCCION_PESHITTA_ZACHARIAS` - Base metodológica
2. :doc:`ARQUITECTURA_TRADUCCION_IACT` - Arquitectura completa
3. :doc:`ARQUITECTURA_DOCUMENTAL_TRADUCCION` - Aplicación práctica
4. :doc:`REGLAS_ESTRUCTURA_PROYECTO` - Reglas operativas
5. :doc:`ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta` - Organización biblioteca
6. :doc:`PLAN_CONTENIDO` - Plan de creación (FASES 1-5)
7. :doc:`PLAN_INCREMENTAL_CON_ARCHIVADO` - Reorganización
8. :doc:`PLAN_FINAL_REORGANIZACION` - Visión completa
9. :doc:`PROMPT_MAESTRO_SPHINX_TRADUCCION` - Automatización
10. :doc:`PROPUESTA_REORGANIZACION` - Propuestas históricas
11. :doc:`PROPUESTA_REORGANIZACION_CORRECTA` - Propuestas actualizadas
12. :doc:`README` - Información general

Referencias Externas
====================

- Micheli, D. (2014). *Translation Technique in Peshitta Zechariah*
- ISO 1087:2019 - Terminology work and terminology science
- ISO 704:2022 - Terminology work — Principles and methods
- MDA Guide v1.0.1 - OMG Model Driven Architecture




**Documento:** SINTESIS_METODOLOGICA_ADT.rst
**Ubicación:** source/docs_maestros/
**Tipo:** Normativo - Base Metodológica
**Estado:** Aprobado v1.0
**Última actualización:** 2026-01-27
