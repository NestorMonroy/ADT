.. _MD_003_nivel_segmentacion:




MD-003: Nivel de Segmentación
=============================

:ID: MD-003
:Tipo: Matriz de Decisión
:Pregunta: ¿Qué nivel de granularidad debo usar al dividir el contenido?
:Frecuencia: Por sección traducida
:Impacto: Medio-Alto (afecta navegabilidad y mantenibilidad)

.. contents:: Contenido
 :depth: 3
 :local:




Pregunta Central
================

**¿Cuántos archivos debo crear y cómo dividir el contenido?**

Esta decisión afecta:
- **Navegabilidad:** Facilidad para encontrar contenido
- **Mantenibilidad:** Facilidad para actualizar
- **Performance:** Tiempo de compilación
- **Experiencia del usuario:** Claridad de la estructura




Los Tres Niveles
================

Nivel 1: Monolítico (Un solo archivo grande)
============================================

**Filosofía:** Todo el contenido en un archivo único

**Características:**

.. code-block:: text

 [OK] Simple de gestionar
 [OK] Búsqueda en un solo lugar
 [OK] No hay duplicación de headers
 [WARNING] Difícil de navegar si es muy largo
 [WARNING] Slow scrolling en archivos grandes
 [ERROR] Difícil colaboración simultánea

**Ejemplo:**

.. code-block:: text

 seccion_completa.rst (500 líneas)
 +- Introducción
 +- Concepto 1
 +- Concepto 2
 +- Concepto 3
 +- ...
 +- Conclusión

**Cuándo usar:**
- Contenido < 300 líneas
- Narrativa lineal continua
- Un solo autor

Nivel 2: Moderado (Archivos por subsección principal)
=====================================================

**Filosofía:** Dividir por subsecciones lógicas principales

**Características:**

.. code-block:: text

 [OK] Balance entre simplicidad y navegabilidad
 [OK] Archivos manejables (50-150 líneas)
 [OK] Facilita colaboración
 [OK] Navegación clara
 [WARNING] Requiere índice (toctree)

**Ejemplo:**

.. code-block:: text

 seccion_08/
 +- index.rst
 +- concepto_seguridad.rst
 +- concepto_persistencia.rst
 +- concepto_validacion.rst
 +- concepto_logging.rst

**Cuándo usar:**
- Contenido 300-1000 líneas
- Subsecciones claramente diferenciadas
- Equipo colaborativo

Nivel 3: Granular (Archivo por cada elemento)
=============================================

**Filosofía:** Máxima división, un archivo por tip/ejemplo/concepto

**Características:**

.. code-block:: text

 [OK] Máxima modularidad
 [OK] Reutilización fácil
 [OK] Navegación muy específica
 [OK] Ideal para referencias
 [WARNING] Muchos archivos pequeños
 [WARNING] Overhead de gestión
 [ERROR] Puede fragmentar narrativa

**Ejemplo:**

.. code-block:: text

 seccion_12/
 +- index.rst
 +- seccion_12_glosario.rst
 +- glossary_tip_1.rst
 +- glossary_tip_2.rst
 +- glossary_tip_3.rst
 +- glossary_tip_4.rst
 +- glossary_tip_5.rst
 +- glossary_tip_6.rst
 +- glossary_ejemplo_htmlsc.rst

**Cuándo usar:**
- Documentación de referencia (tips, ejemplos)
- Contenido reutilizable
- Proyecto grande (100+ archivos)




Matriz de Decisión
==================

Por Tamaño de Contenido
=======================

.. list-table::
 :header-rows: 1
 :widths: 25 25 25 25

 * - **Tamaño Total**
   - **Nivel 1**
   - **Nivel 2**
   - **Nivel 3**
 * - < 300 líneas
   - [OK] **Recomendado**
   - [WARNING] Opcional
   - [ERROR] Excesivo
 * - 300-1000 líneas
   - [WARNING] Posible
   - [OK] **Recomendado**
   - [WARNING] Posible
 * - 1000-3000 líneas
   - [ERROR] Muy largo
   - [OK] **Recomendado**
   - [OK] Bueno
 * - > 3000 líneas
   - [ERROR] No
   - [WARNING] Con cuidado
   - [OK] **Recomendado**

Por Tipo de Contenido
=====================

.. list-table::
 :header-rows: 1
 :widths: 35 20 25 20

 * - **Tipo de Contenido**
   - **Nivel 1**
   - **Nivel 2**
   - **Nivel 3**
 * - Narrativa continua
   - [OK]
   - [WARNING]
   - [ERROR]
 * - Conceptos independientes
   - [WARNING]
   - [OK]
   - [OK]
 * - Tips/Consejos breves
   - [ERROR]
   - [WARNING]
   - [OK]
 * - Tutorial paso a paso
   - [OK]
   - [WARNING]
   - [ERROR]
 * - Documentación referencia
   - [ERROR]
   - [WARNING]
   - [OK]
 * - Manual de usuario
   - [WARNING]
   - [OK]
   - [WARNING]

Por Contexto de Proyecto
========================

.. list-table::
 :header-rows: 1
 :widths: 40 20 20 20

 * - **Factor**
   - **Nivel 1**
   - **Nivel 2**
   - **Nivel 3**
 * - Un solo autor
   - [OK]
   - [OK]
   - [WARNING]
 * - Equipo pequeño (2-5)
   - [WARNING]
   - [OK]
   - [OK]
 * - Equipo grande (5+)
   - [ERROR]
   - [OK]
   - [OK]
 * - Actualizaciones frecuentes
   - [WARNING]
   - [OK]
   - [OK]
 * - Contenido estable
   - [OK]
   - [OK]
   - [WARNING]




Árbol de Decisión
=================

Proceso Paso a Paso
===================

.. code-block:: text

 INICIO: ¿Qué nivel de segmentación?
 v
 PASO 1: Contar líneas totales
 +- < 300 líneas -> Nivel 1 [OK] (Un archivo)
 +- 300-1000 -> Continuar a PASO 2
 +- > 1000 -> Continuar a PASO 2

 PASO 2: ¿Tipo de contenido?
 +- Narrativa continua -> Nivel 1 [OK]
 +- Tutorial paso a paso -> Nivel 1 [OK]
 +- Otros -> Continuar a PASO 3

 PASO 3: ¿Tiene subsecciones claras?
 +- SÍ (3-10 subsecciones) -> Nivel 2 [OK]
 +- SÍ (>10 subsecciones) -> Nivel 3 [OK]
 +- NO -> Nivel 1 [OK]

 PASO 4: ¿Equipo o individual?
 +- Individual -> Nivel 2 [OK]
 +- Equipo -> Nivel 3 [OK]

**Regla de oro:** Cuando dudes, usa **Nivel 2** (balance óptimo)




Casos Reales de arc42
=====================

Sección 12: Glosario (Nivel 3)
==============================

**Decisión:** Nivel 3 (Granular)

**Contexto:**

.. code-block:: text

 Original: 44 líneas + 6 tips + 1 ejemplo
 Total: 8 archivos
 Estructura: Tips independientes reutilizables

**Razón de la decisión:**

.. code-block:: text

 [OK] Cada tip es independiente
 [OK] Tips reutilizables en otros contextos
 [OK] Navegación específica por tip
 [OK] Facilita encontrar consejo específico

**Resultado:**

.. code-block:: text

 seccion_12_glosario/
 +- index.rst
 +- seccion_12_glosario.rst (principal)
 +- glossary_tip_1.rst
 +- glossary_tip_2.rst
 +- glossary_tip_3.rst
 +- glossary_tip_4.rst
 +- glossary_tip_5.rst
 +- glossary_tip_6.rst
 +- glossary_ejemplo_htmlsc.rst

**Éxito:** [OK] 8/8 archivos, navegación excelente

Sección 10: Quality Requirements (Nivel 2)
==========================================

**Decisión:** Nivel 2 (Moderado)

**Contexto:**

.. code-block:: text

 Original: 78 líneas + 8 tips
 Estructura: Tips relacionados al concepto calidad

**Razón de la decisión:**

.. code-block:: text

 [OK] Contenido medio (78 líneas)
 [OK] Tips relacionados entre sí
 [OK] Balance navegabilidad/cohesión
 [WARNING] Nivel 3 fragmentaría narrativa

**Estructura elegida:**

.. code-block:: text

 seccion_10_quality/
 +- index.rst
 +- seccion_10_requisitos_calidad.rst (principal + tips integrados)
 +- quality_ejemplo_escenarios.rst (ejemplo separado)

Sección 01: Introduction (Nivel 1)
==================================

**Decisión:** Nivel 1 (Monolítico)

**Contexto:**

.. code-block:: text

 Original: 120 líneas
 Estructura: Narrativa continua introductoria

**Razón de la decisión:**

.. code-block:: text

 [OK] Narrativa continua y coherente
 [OK] Lectura secuencial esperada
 [ERROR] Dividir rompería flujo
 [ERROR] No hay subsecciones independientes claras

**Estructura elegida:**

.. code-block:: text

 seccion_01_introduccion/
 +- seccion_01_introduccion.rst (todo en un archivo)




Ventajas y Desventajas
======================

Comparación Detallada
=====================

.. list-table::
 :header-rows: 1
 :widths: 25 25 25 25

 * - **Aspecto**
   - **Nivel 1**
   - **Nivel 2**
   - **Nivel 3**
 * - **Simplicidad**
   - [STAR][STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR]
 * - **Navegabilidad**
   - [STAR][STAR]
   - [STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR][STAR]
 * - **Mantenibilidad**
   - [STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR][STAR]
 * - **Colaboración**
   - [STAR][STAR]
   - [STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR][STAR]
 * - **Performance**
   - [STAR][STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR]
   - [STAR][STAR][STAR]
 * - **Reutilización**
   - [STAR][STAR]
   - [STAR][STAR][STAR]
   - [STAR][STAR][STAR][STAR][STAR]

Tiempo de Gestión
=================

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Actividad**
   - **Nivel 1**
   - **Nivel 2**
   - **Nivel 3**
 * - Crear estructura inicial
   - Rápido (5 min)
   - Medio (15 min)
   - Lento (30 min)
 * - Encontrar sección específica
   - Lento (scroll)
   - Rápido
   - Muy rápido
 * - Actualizar contenido
   - Rápido
   - Rápido
   - Muy rápido
 * - Reorganizar
   - Difícil
   - Medio
   - Fácil
 * - Merge de Git
   - Conflictos
   - Pocos conflictos
   - Muy pocos




Recomendaciones Prácticas
=========================

Guía Rápida
===========

**Usa Nivel 1 si:**

.. code-block:: text

 [OK] Documento < 300 líneas
 [OK] Narrativa continua
 [OK] Tutorial paso a paso
 [OK] Un solo autor
 [OK] Lectura secuencial esperada

**Usa Nivel 2 si:**

.. code-block:: text

 [OK] Documento 300-1000 líneas
 [OK] 3-10 subsecciones claras
 [OK] Equipo pequeño
 [OK] Balance navegabilidad/simplicidad
 [OK] Cuando dudes (opción segura)

**Usa Nivel 3 si:**

.. code-block:: text

 [OK] Documento > 1000 líneas
 [OK] Tips/ejemplos independientes
 [OK] Documentación de referencia
 [OK] Equipo grande
 [OK] Reutilización importante

Reglas de Oro
=============

**1. No sobre-segmentar**

.. code-block:: text

 [ERROR] MAL: 50 archivos de 5 líneas cada uno
 [OK] BIEN: 5 archivos de 50 líneas cada uno

**2. Mantener cohesión**

.. code-block:: text

 [ERROR] MAL: Dividir párrafos relacionados
 [OK] BIEN: Mantener conceptos juntos

**3. Facilitar búsqueda**

.. code-block:: text

 [OK] Archivos con nombres descriptivos
 [OK] Un concepto principal por archivo
 [OK] Índices claros (toctrees)

**4. Pensar en el usuario**

.. code-block:: text

 Pregunta: "¿El usuario encontrará esto fácilmente?"

 Si SÍ -> Estructura correcta [OK]
 Si NO -> Reorganizar

Checklist de Decisión
=====================

.. code-block:: text

 Antes de segmentar:

 [ ] Conté líneas totales
 [ ] Identifiqué subsecciones naturales
 [ ] Consideré tipo de contenido
 [ ] Pensé en colaboración
 [ ] Evalué actualizaciones futuras

 Después de segmentar:

 [ ] Nombres de archivo descriptivos
 [ ] Toctrees correctos
 [ ] Navegación lógica
 [ ] Fácil encontrar contenido
 [ ] Compilación exitosa




Errores Comunes
===============

Error 1: Sobre-segmentación
===========================

**Problema:**

.. code-block:: text

 100 archivos de 3-5 líneas cada uno

 Resultado:
 [ERROR] Difícil navegar
 [ERROR] Overhead excesivo
 [ERROR] Fragmentación extrema

**Solución:**

.. code-block:: text

 Consolidar archivos relacionados
 Usar Nivel 2 en lugar de Nivel 3

Error 2: Sub-segmentación
=========================

**Problema:**

.. code-block:: text

 Un archivo de 2000 líneas

 Resultado:
 [ERROR] Difícil navegar
 [ERROR] Slow scrolling
 [ERROR] Merge conflicts

**Solución:**

.. code-block:: text

 Dividir en subsecciones lógicas
 Usar Nivel 2 o Nivel 3

Error 3: Segmentación Arbitraria
================================

**Problema:**

.. code-block:: text

 Dividir sin seguir estructura lógica

 archivo_parte1.rst (líneas 1-100)
 archivo_parte2.rst (líneas 101-200)

**Solución:**

.. code-block:: text

 Dividir por CONCEPTO, no por líneas
 concepto_seguridad.rst
 concepto_performance.rst




Conclusión
==========

**Mensaje clave:**

.. important::
 El nivel de segmentación correcto hace el contenido **fácil de encontrar, mantener y colaborar**.

 **Nivel 2 es la opción más segura cuando dudes.**

**Reglas prácticas:**

.. code-block:: text

 < 300 líneas -> Nivel 1
 300-1000 líneas normales -> Nivel 2
 > 1000 o tips separados -> Nivel 3

**Próximos pasos:**

Después de decidir nivel:
- Crear estructura de directorios
- Nombrar archivos descriptivamente
- Crear índices (index.rst)
- Configurar toctrees




.. seealso::
 * :doc:`MD_001_modo_1_vs_modo_2` - Decisión de modo de traducción
 * :doc:`MD_002_cuando_enriquecer` - Decisión de enriquecimiento
 * :doc:`../../06_casos_practicos/antes_despues/caso_01_seccion_breve` - Ejemplo Nivel 3

.. note::
 Esta matriz se basa en experiencia de 196 archivos de arc42 con diferentes niveles de segmentación.
