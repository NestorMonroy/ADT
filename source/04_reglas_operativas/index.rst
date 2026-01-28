.. _reglas_operativas:

===============================================
Reglas Operativas de Traducción
===============================================

Esta sección contiene **reglas de decisión concretas** para situaciones específicas durante traducción.

**Base empírica:**
   Reglas derivadas de decisiones reales tomadas en 196 archivos de arc42.

**Propósito:**
   Proveer guía objetiva para decisiones en tiempo real durante traducción.

----

Subsecciones
============

.. toctree::
   :maxdepth: 2
   :caption: Reglas Operativas

   matrices_decision/index
   reglas_traduccion/index
   escenarios_traduccion/index

----

Tipos de Reglas
===============

**Matrices de Decisión** (MD-XXX)
   Árboles de decisión para preguntas frecuentes.
   
   Ejemplo: MD-002 "¿Cuánto enriquecer?"

**Reglas de Traducción** (RT-XXX)
   Reglas específicas para elementos particulares.
   
   Ejemplo: RT-001 "Cómo traducir terminología técnica"

**Escenarios de Traducción** (ET-XXX)
   Guías para tipos específicos de proyectos.
   
   Ejemplo: ET-001 "Documento breve"

----

Uso de esta Sección
===================

**Durante Traducción Activa:**

.. code-block:: text

   SITUACIÓN → CONSULTAR → APLICAR
   
   Ejemplo:
   "¿Traduzco 'Stakeholder'?" 
   → Consultar MD-004 
   → Conservar en inglés ✅

**Toma de Decisiones:**

1. Identifica el tipo de decisión
2. Busca la matriz/regla correspondiente
3. Sigue el proceso paso a paso
4. Documenta tu decisión

**Decisiones Más Frecuentes:**

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - **Decisión**
     - **Matriz/Regla**
   * - ¿Cuánto enriquecer?
     - :doc:`matrices_decision/MD_002_cuando_enriquecer`
   * - ¿Traducir o conservar término?
     - :doc:`matrices_decision/MD_004_traducir_vs_conservar`
   * - ¿Qué nivel de segmentación?
     - ⏳ MD-003 (planificado)
   * - ¿Cómo estructurar salida?
     - ⏳ MD-005 (planificado)

----

Estado de Desarrollo
====================

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - **Subsección**
     - **Estado**
     - **Archivos**
   * - **matrices_decision/**
     - ✅ Parcial (2/5)
     - MD-002, MD-004 completados
   * - **reglas_traduccion/**
     - ⏳ Planificado
     - Pendiente
   * - **escenarios_traduccion/**
     - ⏳ Planificado
     - Pendiente

----

Relación con Otras Secciones
=============================

* **01_fundamentos** - Base teórica de las reglas
* **02_procedimientos** - Workflow que aplica estas reglas
* **03_estandares** - Estándares que justifican decisiones
* **06_casos_practicos** - Ejemplos de aplicación

----

Próximas Reglas Planeadas
==========================

**Matrices de Decisión:**

- ⏳ MD-001: Modo 1 vs Modo 2
- ⏳ MD-003: Nivel de segmentación
- ⏳ MD-005: Estructura de salida

**Reglas de Traducción:**

- ⏳ RT-001: Terminología técnica
- ⏳ RT-002: Referencias cruzadas
- ⏳ RT-003: Código y ejemplos
- ⏳ RT-004: Títulos y secciones

**Escenarios:**

- ⏳ ET-001: Documento breve
- ⏳ ET-002: Documento extenso
- ⏳ ET-003: Múltiples archivos
- ⏳ ET-004: Con diagramas

----

.. note::
   Esta sección está en desarrollo activo. Prioridad actual: Matrices de Decisión críticas (MD-002 ✅, MD-004 ✅).
