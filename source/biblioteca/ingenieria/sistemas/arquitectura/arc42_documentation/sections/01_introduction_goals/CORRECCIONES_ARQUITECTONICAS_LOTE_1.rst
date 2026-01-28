.. meta::
   :artefacto: CORRECCIONES_ARQUITECTONICAS_LOTE_1
   :tipo: Reporte de Correcciones
   :dominio: traduccion
   :estado: Completado
   :version: 1.0.0
   :fecha: 2026-01-27
   :autor: Equipo ADT
   :clasificacion: Interno

====================================================================
Correcciones Arquitectónicas Aplicadas - Lote 1
====================================================================

:Fecha: 2026-01-27
:Sección: 01 - Introducción y Objetivos
:Fase: FASE 4 - Aplicación de Tácticas
:Documento base: ADT_GUIA_TRADUCCION_ARQUITECTONICA.md
:Estado: ✅ COMPLETADO

----

Resumen Ejecutivo
=================

Se aplicaron correcciones arquitectónicas a todos los archivos traducidos del 
Lote 1, siguiendo la **Guía de Traducción Arquitectónica ADT**. Las correcciones 
reemplazaron traducciones literales por traducciones contextuales arquitectónicas.

**Resultado:** ✅ Terminología arquitectónica correcta aplicada en 5 archivos

----

Problema Identificado
=====================

Traducción Literal vs Contextual
---------------------------------

La traducción literal de términos arquitectónicos causa **ambigüedad semántica** 
y no refleja el significado real en el contexto de arquitectura de software.

Ejemplo del Problema
^^^^^^^^^^^^^^^^^^^^

.. code-block:: rst

   ❌ INCORRECTO (Literal):
   "Describe los requisitos relevantes y las fuerzas impulsoras que 
   los arquitectos de software deben considerar."

   ✅ CORRECTO (Contextual):
   "Describe los requisitos relevantes y los factores determinantes que 
   guían las decisiones de los arquitectos de software."

**Por qué es importante:**

- "fuerzas impulsoras" suena a física, no a arquitectura
- "factores determinantes" captura el concepto arquitectónico correcto
- Mejora la comprensión para arquitectos de software hispanohablantes

----

Correcciones Aplicadas
=======================

1. Driving Forces → Factores Determinantes
-------------------------------------------

**Término original:** ``driving forces``

**❌ Traducción literal:** "fuerzas impulsoras"

**✅ Traducción arquitectónica:** "factores determinantes"

**Archivos corregidos:**

.. list-table::
   :header-rows: 1
   :widths: 50 20 30

   * - Archivo
     - Líneas
     - Tipo
   * - introduccion_tip-1.rst
     - 3, 14
     - Metadata + subtítulo
   * - seccion_01_introduccion_objetivos.rst
     - 21
     - Texto principal
   * - glosario_seccion_01.rst
     - 36-43
     - Definición

**Contexto arquitectónico:**

.. note::
   En arquitectura de software, "driving forces" se refiere a:
   
   - Requisitos funcionales clave
   - Atributos de calidad críticos
   - Restricciones técnicas o de negocio
   - Factores que IMPULSAN decisiones arquitectónicas

**Justificación:**

No son "fuerzas" físicas sino **factores** que determinan y moldean la 
arquitectura. "Factores determinantes" es el término arquitectónico correcto.

----

2. Quality Goals → Atributos de Calidad Objetivo
-------------------------------------------------

**Término original:** ``quality goals``

**❌ Traducción literal:** "objetivos de calidad"

**✅ Traducción arquitectónica:** "atributos de calidad objetivo"

**Archivos corregidos:**

.. list-table::
   :header-rows: 1
   :widths: 50 20 30

   * - Archivo
     - Líneas
     - Tipo
   * - requisitos_calidad_ejemplo-1.rst
     - 25
     - Título de tabla
   * - requisitos_calidad_ejemplo-3.rst
     - 18, 23, 26
     - Nota + título + tabla
   * - seccion_01_introduccion_objetivos.rst
     - 16
     - Texto principal
   * - glosario_seccion_01.rst
     - 71-82
     - Definición

**Contexto arquitectónico:**

.. important::
   Los "quality goals" NO son simplemente "objetivos" - son ATRIBUTOS 
   MEDIBLES Y ESPECÍFICOS que la arquitectura debe exhibir.
   
   Ejemplos:
   
   - Performance: < 2 segundos response time
   - Availability: 99.9% uptime  
   - Maintainability: < 4 horas para hotfix

**Justificación:**

Son atributos de la ARQUITECTURA, no del proyecto. Deben ser específicos y 
medibles. "Atributos de calidad objetivo" refleja mejor esta naturaleza.

----

3. Stakeholder → Preservado
----------------------------

**Término original:** ``stakeholder``

**✅ Decisión:** Preservar sin traducir

**Archivo actualizado:**

.. list-table::
   :header-rows: 1
   :widths: 50 20 30

   * - Archivo
     - Acción
     - Tipo
   * - glosario_seccion_01.rst
     - Agregada definición
     - Nueva entrada
   * - seccion_01_introduccion_objetivos.rst
     - Ya correcto
     - Verificado

**Contexto arquitectónico:**

.. note::
   "Stakeholder" es término técnico internacional estándar en:
   
   - Gestión de proyectos (PMBoK)
   - Arquitectura de software (ISO/IEC 42010)
   - Ingeniería de software (SWEBOK)

**Justificación:**

Término establecido internacionalmente. Traducirlo a "interesado" o "parte 
interesada" reduce precisión técnica.

----

Glosario Actualizado
====================

Entradas Corregidas/Agregadas
------------------------------

1. **Driving forces (Factores determinantes)**
   
   - Definición arquitectónica completa
   - Nota de traducción explicativa
   - Ejemplos de factores determinantes

2. **Quality goals (Atributos de calidad objetivo)**
   
   - Definición con énfasis en medibilidad
   - Ejemplos concretos (Performance < 2s, etc.)
   - Nota de traducción arquitectónica

3. **Stakeholder** (NUEVA ENTRADA)
   
   - Definición de término técnico
   - Justificación de preservación en inglés
   - Referencias a estándares internacionales

----

Archivos Afectados - Resumen
=============================

.. list-table:: Archivos con Correcciones
   :header-rows: 1
   :widths: 40 20 40

   * - Archivo
     - Correcciones
     - Estado
   * - introduccion_tip-1.rst
     - 2
     - ✅ Corregido
   * - requisitos_calidad_ejemplo-1.rst
     - 1
     - ✅ Corregido
   * - requisitos_calidad_ejemplo-3.rst
     - 3
     - ✅ Corregido
   * - seccion_01_introduccion_objetivos.rst
     - 2
     - ✅ Corregido
   * - glosario_seccion_01.rst
     - 3
     - ✅ Actualizado
   * - notas_traduccion_seccion_01.rst
     - 1
     - ✅ Documentado

**Total:** 6 archivos actualizados | **12 correcciones aplicadas**

----

Metodología de Corrección
==========================

Proceso Seguido
---------------

1. **Identificación:** Búsqueda de términos problemáticos con grep
2. **Análisis:** Verificación de contexto arquitectónico
3. **Corrección:** Reemplazo con str_replace
4. **Validación:** Verificación de coherencia terminológica
5. **Documentación:** Actualización de glosario y notas

Herramientas Utilizadas
-----------------------

.. code-block:: bash

   # Búsqueda de términos
   grep -rn "fuerzas impulsoras" traduccion/*.rst
   grep -rn "objetivos de calidad" traduccion/*.rst
   
   # Corrección con str_replace
   str_replace(old="fuerzas impulsoras", new="factores determinantes")
   
   # Validación
   grep -rn "factores determinantes" traduccion/*.rst

----

Impacto de las Correcciones
============================

Mejora en Claridad Arquitectónica
----------------------------------

**Antes (literal):**

   Las fuerzas impulsoras y objetivos de calidad deben ser documentados.

**Después (arquitectónico):**

   Los factores determinantes y atributos de calidad objetivo deben ser 
   documentados.

**Resultado:**

- ✅ Terminología precisa y técnica
- ✅ Comprensible para arquitectos de software
- ✅ Alineado con estándares internacionales
- ✅ Coherente con ISO 25010 y SWEBOK

Alineación con Estándares
--------------------------

.. list-table:: Conformidad con Estándares
   :header-rows: 1
   :widths: 40 30 30

   * - Término
     - Estándar
     - Conformidad
   * - Factores determinantes
     - ISO/IEC 42010
     - ✅ Alineado
   * - Atributos de calidad
     - ISO 25010
     - ✅ Alineado
   * - Stakeholder
     - IEEE 1471
     - ✅ Alineado

----

Lecciones Aprendidas
====================

Para Futuras Traducciones
--------------------------

1. **Consultar Guía Arquitectónica ANTES de traducir**
   
   - No empezar traducción sin revisar guía
   - Verificar términos especializados primero

2. **Evitar traducción literal de términos técnicos**
   
   - Entender el CONTEXTO arquitectónico
   - Traducir el CONCEPTO, no las palabras

3. **Mantener coherencia terminológica**
   
   - Un término → Una traducción consistente
   - Documentar decisiones en glosario

4. **Validar con estándares internacionales**
   
   - ISO/IEC 42010, IEEE 1471, ISO 25010
   - SWEBOK para terminología de ingeniería

Aplicación a Futuros Lotes
---------------------------

.. important::
   **Para Lote 2 y siguientes:**
   
   1. ✅ Revisar Guía Arquitectónica ANTES de traducir
   2. ✅ Aplicar terminología contextual desde el inicio
   3. ✅ NO requerir correcciones post-traducción
   4. ✅ Documentar decisiones en tiempo real

----

Checklist de Calidad Arquitectónica
====================================

Verificación Post-Corrección
-----------------------------

- ✅ "driving forces" → "factores determinantes" (NO "fuerzas impulsoras")
- ✅ "quality goals" → "atributos de calidad objetivo" (NO solo "objetivos")
- ✅ "stakeholder" → preservado sin traducir
- ✅ Términos consistentes en toda la traducción
- ✅ Glosario actualizado con definiciones arquitectónicas
- ✅ Notas de traducción documentadas

Resultado
---------

**Calidad arquitectónica:** ✅ **APROBADA**

----

Referencias
===========

Documentos Aplicados
--------------------

- **ADT_GUIA_TRADUCCION_ARQUITECTONICA.md** (v1.0.0)
- :doc:`/02_procedimientos/workflow_general` (v1.4.0)

Estándares Consultados
----------------------

- ISO/IEC/IEEE 42010 (Architecture description)
- ISO/IEC 25010 (Systems and software Quality Models)
- IEEE 1471 (Architectural Description of Software)
- SWEBOK v3.0 (Software Engineering Body of Knowledge)

----

Conclusión
==========

Las correcciones arquitectónicas mejoraron significativamente la calidad técnica 
de la traducción del Lote 1. La terminología ahora es:

- ✅ Precisa arquitectónicamente
- ✅ Alineada con estándares internacionales
- ✅ Comprensible para profesionales
- ✅ Coherente y consistente

**FASE 4 completada exitosamente para Lote 1.**

----

Historial de Revisiones
========================

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Versión
     - Fecha
     - Cambios
   * - 1.0.0
     - 2026-01-27
     - Correcciones arquitectónicas aplicadas según guía ADT

----

.. note::
   **Guía aplicada:** ADT_GUIA_TRADUCCION_ARQUITECTONICA.md v1.0.0
   
   **Método:** Corrección contextual arquitectónica
   
   **Próxima fase:** FASE 5 - Validación con Sphinx
