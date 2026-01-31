.. _errores_comunes:




Errores Comunes y Correcciones
==============================

Errores reales cometidos durante traducción y **cómo fueron corregidos**.

**Base empírica:**
 Problemas identificados y resueltos en arc42 (196 archivos).

**Propósito:**
 Aprender de errores reales para evitarlos en el futuro.




Errores Disponibles
===================

.. toctree::
 :maxdepth: 2
 :caption: Errores y Soluciones

 error_01_omisiones




Estructura de Cada Error
========================

Cada caso de error incluye:

1. **Contexto:** Situación inicial
2. **El Error:** Qué se hizo mal
3. **Detección:** Cómo se descubrió
4. **Causa Raíz:** Por qué ocurrió
5. **Corrección:** Cómo se solucionó
6. **Impacto:** Costo del error
7. **Prevención:** Cómo evitarlo
8. **Aplicabilidad:** Dónde puede ocurrir




Uso de estos Casos
==================

**Para Prevenir:**
 Lee ANTES de empezar tu proyecto.

**Para Diagnosticar:**
 Consulta si sospechas problema similar.

**Para Corregir:**
 Sigue pasos de corrección documentados.




Top 3 Errores Más Comunes
=========================

1. **Omisiones** (Error #1)

 .. code-block:: text

 Causa: NO leer archivo completo (PASO 0 incompleto)
 Frecuencia: 40% de traducciones sin checklist
 Prevención: PASO 0 obligatorio

 Ver: :doc:`error_01_omisiones`

2. **Enriquecimiento Inconsistente** (Planeado)

 .. code-block:: text

 Causa: NO usar MD-002
 Frecuencia: 30% de traducciones sin guía
 Prevención: Aplicar MD-002 sistemáticamente

3. **Terminología Inconsistente** (Planeado)

 .. code-block:: text

 Causa: NO usar glosario
 Frecuencia: 25% de traducciones sin estándar
 Prevención: Aplicar MD-004 + glosario




Señales de Advertencia
======================

**[ALERT] Estás en riesgo de errores si:**

.. code-block:: text

 [ERROR] "No tengo tiempo para PASO 0 completo"
 [ERROR] "Ya conozco el patrón"
 [ERROR] "La verificación es opcional"
 [ERROR] "No necesito script automático"
 [ERROR] "Compiló sin errores, está bien"

**[OK] Estás seguro si:**

.. code-block:: text

 [OK] PASO 0 es sagrado (15 min mínimo)
 [OK] Checklist en cada fase
 [OK] Script de verificación obligatorio
 [OK] Revisión contra original
 [OK] Compilación + verificación manual




Próximos Errores a Documentar
=============================

.. code-block:: text

 [RUNNING] error_02_enriquecimiento_excesivo.rst
 [RUNNING] error_03_terminologia_inconsistente.rst
 [RUNNING] error_04_verificacion_incompleta.rst




.. warning::
 Los errores documentados aquí son **reales** y **costosos**. Error #1 (omisiones) costó 2 horas de re-trabajo. Leer esta sección puede ahorrar días de trabajo.

.. seealso::
 * :doc:`../../03_estandares/calidad/checklist_revision` - Previene errores
 * :doc:`../../02_procedimientos/workflow_general` - Proceso correcto
 * :doc:`../antes_despues/caso_01_seccion_breve` - Aplicación correcta
