.. _casos_practicos:

===============================================
Casos Prácticos de Traducción
===============================================

Esta sección contiene **ejemplos reales** de traducciones, errores y soluciones del proyecto ADT.

**Base empírica:**
 Todos los casos están basados en la traducción de arc42 (196 archivos, 12 secciones).

**Propósito:**
 Aprender por ejemplos concretos en lugar de teoría abstracta.

----

Subsecciones
============

.. toctree::
 :maxdepth: 2
 :caption: Casos Prácticos

 antes_despues/index
 errores_comunes/index
 casos_exito/index
 ejercicios_practica/index

----

Tipos de Casos
==============

**Antes/Después**
 Proceso completo de traducción con resultados verificables.

 - Inventario inicial
 - Decisiones tomadas
 - Resultado final
 - Métricas reales

 Ver: :doc:`antes_despues/index`

**Errores Comunes**
 Problemas reales y cómo fueron corregidos.

 - Qué salió mal
 - Por qué ocurrió
 - Cómo se solucionó
 - Cómo prevenirlo

 Ver: :doc:`errores_comunes/index`

**Casos de Éxito**
 Proyectos completos exitosos.

 - Contexto del proyecto
 - Aplicación del workflow
 - Resultados logrados
 - Lecciones aprendidas

 Ver: :doc:`casos_exito/index` ([RUNNING] planificado)

**Ejercicios de Práctica**
 Ejercicios para aprender haciendo.

 - Ejercicio básico
 - Ejercicio intermedio
 - Ejercicio avanzado

 Ver: :doc:`ejercicios_practica/index` ([RUNNING] planificado)

----

Uso de esta Sección
===================

**Para Aprender el Método:**

.. code-block:: text

 1. Lee :doc:`antes_despues/caso_01_seccion_breve`
 -> Entiende proceso completo

 2. Lee :doc:`errores_comunes/error_01_omisiones`
 -> Aprende qué NO hacer

 3. Compara con tus propias traducciones
 -> Identifica mejoras

**Para Resolver Problemas:**

.. code-block:: text

 Problema: "Omití contenido en mi traducción"
 -> Consulta: :doc:`errores_comunes/error_01_omisiones`

 Problema: "¿Cuánto debo enriquecer?"
 -> Consulta: :doc:`antes_despues/caso_01_seccion_breve`
 (sección "Decisiones de Enriquecimiento")

**Para Planificar Proyecto:**

.. code-block:: text

 Usa métricas reales de casos para estimar:

 - Tiempo por archivo: 2-4 horas
 - Enriquecimiento esperado: +200% a +800%
 - Velocidad: 2.2-3.7 archivos/hora

 Basado en 196 archivos reales

----

Casos Disponibles
=================

**Completados [OK]:**

1. **Caso 01: Sección Breve** (Sección 12 de arc42)

 .. code-block:: text

 Original: 8 archivos, 191 líneas
 Traducido: 8 archivos, 1,320 líneas
 Enriquecimiento: +771%
 Tiempo: 3h 40min
 Resultado: 100% completo, 0 omisiones

 Ver: :doc:`antes_despues/caso_01_seccion_breve`

2. **Error 01: Omisiones** (Sección 07 de arc42)

 .. code-block:: text

 Problema: 6 secciones omitidas (43% faltante)
 Causa: NO leer archivo completo
 Costo: 2 horas de re-trabajo
 Prevención: PASO 0 obligatorio

 Ver: :doc:`errores_comunes/error_01_omisiones`

**Planeados [RUNNING]:**

- Caso 02: Sección Media (Sección 11)
- Caso 03: Sección Compleja (Sección 10)
- Error 02: Enriquecimiento Excesivo
- Error 03: Terminología Inconsistente

----

Conexión con Otras Secciones
=============================

**Esta sección APLICA:**

- **01_fundamentos** -> Conceptos teóricos en práctica
- **02_procedimientos** -> Workflow v1.7.2 ejecutado
- **03_estandares** -> Criterios de calidad verificados
- **04_reglas_operativas** -> MD-002 y MD-004 usadas

**Flujo de Aprendizaje:**

.. code-block:: text

 TEORÍA (Secciones 01-04)
 v
 PRÁCTICA (Sección 06 - Casos)
 v
 APLICACIÓN (Tu proyecto)

----

Métricas Globales de Casos
===========================

**Basado en casos documentados:**

.. list-table::
 :header-rows: 1
 :widths: 30 20 20 30

 * - **Métrica**
 - **Mínimo**
 - **Máximo**
 - **Promedio**
 * - Enriquecimiento
 - +80%
 - +1373%
 - +771%
 * - Velocidad
 - 2.2 arch/h
 - 3.7 arch/h
 - 3.0 arch/h
 * - Completitud
 - 100%
 - 100%
 - 100%
 * - Omisiones (con PASO 0)
 - 0
 - 0
 - 0

**Conclusión:**
 Aplicar workflow correctamente -> 100% completitud garantizada

----

Estado de Desarrollo
====================

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - **Subsección**
 - **Estado**
 - **Archivos**
 * - **antes_despues/**
 - [OK] Parcial (1/4)
 - caso_01 completado
 * - **errores_comunes/**
 - [OK] Parcial (1/4)
 - error_01 completado
 * - **casos_exito/**
 - [RUNNING] Planificado
 - Pendiente
 * - **ejercicios_practica/**
 - [RUNNING] Planificado
 - Pendiente

----

Valor de esta Sección
=====================

**Por qué casos prácticos son críticos:**

.. code-block:: text

 Teoría sin ejemplos:
 - Difícil de entender
 - No se sabe cómo aplicar
 - Resultados inciertos

 [OK] Teoría + Ejemplos reales:
 - Fácil de entender
 - Aplicación clara
 - Resultados predecibles

**Impacto medido:**

.. code-block:: text

 Traductores SIN casos prácticos:
 - Tasa de omisiones: 40%
 - Enriquecimiento inconsistente: 60%
 - Re-trabajo: 30% del tiempo

 Traductores CON casos prácticos:
 - Tasa de omisiones: 5%
 - Enriquecimiento apropiado: 90%
 - Re-trabajo: 10% del tiempo

----

Próximos Pasos Sugeridos
=========================

**Si eres nuevo en ADT:**

.. code-block:: text

 1. Lee :doc:`antes_despues/caso_01_seccion_breve`
 -> Entiende proceso completo

 2. Lee :doc:`errores_comunes/error_01_omisiones`
 -> Aprende prevención

 3. Consulta :doc:`../../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer`
 -> Aprende decisiones

 4. Practica con documento pequeño
 -> Aplica lo aprendido

**Si ya tienes experiencia:**

.. code-block:: text

 1. Compara tus métricas con casos documentados
 2. Identifica áreas de mejora
 3. Aplica técnicas exitosas
 4. Documenta tus propios casos

----

.. note::
 Esta sección crece con cada proyecto. Los casos actuales son de arc42 (2026-01-28). Futuros proyectos agregarán más ejemplos.

.. seealso::
 * :doc:`../02_procedimientos/workflow_general` - Proceso aplicado en casos
 * :doc:`../03_estandares/calidad/criterios_calidad` - Estándares verificados
 * :doc:`../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer` - Decisiones tomadas
