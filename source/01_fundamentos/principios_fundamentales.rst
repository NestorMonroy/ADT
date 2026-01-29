=========================================
Principios Fundamentales de ADT
=========================================

:Categoría: Fundamentos
:Ubicación: 01_fundamentos/
:Tipo: Documento Base
:Base: Método Peshitta + Translation Studies

.. contents:: Contenido
 :depth: 2
 :local:

----

Introducción
============

Este documento establece los **principios fundamentales** que guían todo el
proyecto ADT (Arc42-Diátaxis-Traducción).

**Pregunta central:**
 ¿Cómo traducimos documentación técnica con calidad profesional?

**Respuesta:**
 Siguiendo principios sistemáticos basados en 50+ años de Translation Studies.

----

Los 10 Principios Fundamentales
================================

Principio 1: Traducción como Transformación
--------------------------------------------

.. important::
 La traducción de documentación NO es "copiar y cambiar sintaxis".

 ES una transformación sistemática que preserva contenido semántico
 mientras adapta forma sintáctica.

**Fundamento teórico:**
 - Isomorfismo con transformaciones de modelos (MDA/MDE)
 - Base en Translation Studies (Nida, Toury, Micheli)

**Implicación práctica:**
 - Aplicamos método riguroso, no improvisamos
 - Cada decisión es rastreable y justificable
 - Usamos framework universal aplicable a cualquier par (fuente, destino)

**Ver:** :doc:`_fundamentos_conceptuales/traduccion_como_transformacion`

Principio 2: Preferencia por Signifié sobre Signifiant
-------------------------------------------------------

.. important::
 Cuando hay conflicto entre preservar FORMA vs CONTENIDO:

 **Preservamos CONTENIDO (Signifié), adaptamos FORMA (Signifiant)**

**Justificación:**
 - El lector necesita el CONTENIDO, no la sintaxis específica
 - LaTeX y RST son solo MEDIOS, no fines
 - La función semántica es lo que importa

**Excepción:**
 Código fuente (donde forma = contenido)

**Ejemplos:**

.. list-table::
 :widths: 30 30 40
 :header-rows: 1

 * - Situación
   - Decisión
 - Razón
 * - ``\textbf{}`` -> ``**``
   - Adaptar forma [OK]
 - Función (énfasis) preservada
 * - ``\vspace{}`` -> omitir
   - Adaptar forma [OK]
 - No semántico en RST
 * - ``def foo():`` -> igual
   - Preservar forma [OK]
 - Forma = contenido en código

**Ver:** :doc:`_fundamentos_conceptuales/signifiant_vs_signifie`

Principio 3: Método por Defecto + Divergencias
-----------------------------------------------

.. important::
 Aplicamos MÉTODO POR DEFECTO en el 80-90% de casos.

 Divergimos SOLO cuando hay objetivo específico que lo justifica.

**Método por Defecto:**

1. **Segmentación:** Nivel de sección
2. **Rendición:** Comando por comando
3. **Preferencia:** Signifié sobre Signifiant

**Divergencias permitidas:**

Solo para lograr uno de los 4 objetivos:

1. Domesticación (adaptar a RST)
2. Claridad (hacer comprensible)
3. Consistencia (resolver inconsistencias)
4. Simplificación (reducir complejidad)

**Ver:** :doc:`_metodologias/metodo_por_defecto`

Principio 4: Objetivos Explícitos
----------------------------------

.. important::
 TODA divergencia del método por defecto debe tener un objetivo explícito.

 Sin objetivo = error, no mejora.

**Los 4 Objetivos:**

**1. Domesticación:**
 Adaptar al contexto destino (RST/Sphinx)

**2. Claridad:**
 Hacer comprensible para el lector

**3. Consistencia:**
 Resolver inconsistencias del original

**4. Simplificación:**
 Reducir complejidad innecesaria

**Regla:**

.. code-block:: text

 SI vas a desviarte del método por defecto:

 1. Identifica QUÉ objetivo justifica la divergencia
 2. Selecciona táctica apropiada
 3. Documenta la decisión
 4. Valida que el objetivo se logró

Principio 5: Tácticas Catalogadas
----------------------------------

.. important::
 Usamos tácticas probadas, no inventamos ad-hoc.

 Base: 14+ tácticas identificadas en análisis Peshitta.

**Tácticas principales:**

1. Adición (agregar contenido)
2. Omisión (eliminar contenido)
3. Sustitución (reemplazar elemento)
4. Cambio de orden (reordenar)
5. Especificación (hacer más específico)
6. Generalización (hacer más general)
7. Explicación (expandir implícito)
8. Normalización (estandarizar)
9. Modulación (cambiar perspectiva)
10. Compensación (recuperar pérdida)
11. Amplificación (expandir comprimido)
12. Condensación (comprimir verboso)
13. Literalización (preservar forma exacta)
14. Adaptación cultural

**Uso:**

Para cada objetivo, hay tácticas preferidas:

.. list-table::
 :widths: 25 75
 :header-rows: 1

 * - Objetivo
   - Tácticas Comunes
 * - Domesticación
   - Sustitución, Normalización
 * - Claridad
   - Adición (notas), Explicación
 * - Consistencia
   - Normalización, Generalización
 * - Simplificación
   - Omisión, Condensación

Principio 6: Preservación Semántica
------------------------------------

.. important::
 La propiedad MÁS IMPORTANTE de una traducción:

 **Preservar el contenido semántico del original**

**Definición formal:**

.. math::

 \forall x \in \text{Fuente}: \text{Signifié}(x) = \text{Signifié}(T(x))

Donde :math:`T` es la función de transformación.

**En lenguaje simple:**

 Todo lo que el autor quiso comunicar en LaTeX
 debe estar comunicado en RST.

**Validación:**

1. **Completitud:** ¿Falta algo?
2. **Corrección:** ¿Está bien traducido?
3. **Fidelidad:** ¿Refleja el original?

**Checklist:**

.. code-block:: text

 [ ] Todas las secciones traducidas
 [ ] Todas las figuras incluidas
 [ ] Todas las tablas presentes
 [ ] Todas las ecuaciones convertidas
 [ ] Todas las referencias funcionan
 [ ] Todas las citas presentes

Principio 7: Adaptación Sintáctica
-----------------------------------

.. important::
 La forma (sintaxis) DEBE adaptarse al medio destino.

 RST no es LaTeX con otra sintaxis - es su propio lenguaje.

**Antipatrón:**

.. code-block:: rst

 # MAL: Intentar "copiar" LaTeX en RST
 \textbf{malo} # Esto no es RST válido

**Patrón correcto:**

.. code-block:: rst

 # BIEN: Usar sintaxis nativa RST
 **correcto**

**Principio:**

 Usar las herramientas que RST/Sphinx provee NATURALMENTE.

 No forzar construcciones de LaTeX en RST.

**Ejemplos:**

- Listas: Usar ``1. 2. 3.``, NO intentar recrear ``\begin{enumerate}``
- Énfasis: Usar ``**``, NO inventar directiva ``.. textbf::``
- Referencias: Usar ``:ref:``, NO tratar de usar ``\ref{}``

Principio 8: Validación Continua
---------------------------------

.. important::
 Validamos CONTINUAMENTE, no solo al final.

 Compilar Sphinx frecuentemente para detectar errores temprano.

**Workflow:**

.. code-block:: bash

 # Después de cada sección traducida:
 make html

 # Verificar:
 # 1. Compila sin errores
 # 2. HTML se ve correcto
 # 3. Enlaces funcionan

**Frecuencia:**

- **Después de cada sección:** Compilación rápida
- **Después de cada capítulo:** Revisión completa
- **Antes de commit:** Validación total

**Tipos de validación:**

1. **Sintáctica:** ¿Compila?
2. **Semántica:** ¿Preserva contenido?
3. **Visual:** ¿Se ve bien?
4. **Funcional:** ¿Enlaces/referencias funcionan?

Principio 9: Documentación de Decisiones
-----------------------------------------

.. important::
 Documentamos decisiones importantes, especialmente divergencias.

 Futuras revisiones necesitan saber POR QUÉ se hizo algo.

**Qué documentar:**

1. **Divergencias significativas** del método por defecto
2. **Decisiones de diseño** (estructura de capítulos, etc.)
3. **Problemas encontrados** y cómo se resolvieron
4. **Inconsistencias del original** y cómo se manejaron

**Dónde documentar:**

.. code-block:: rst

 # En notas de traducción
 .. note::
 **Decisión de traducción:**

 El original usa tanto \textbf como \emph para énfasis.
 Unificamos a **fuerte** y *moderado* para consistencia.

 Objetivo: Consistencia
 Táctica: Normalización

**Formato:**

- Objetivo que justifica
- Táctica aplicada
- Razonamiento breve

Principio 10: Mejora Iterativa
-------------------------------

.. important::
 La traducción NO es perfecta en el primer intento.

 Iteramos: traducir -> validar -> revisar -> mejorar.

**Proceso iterativo:**

.. code-block:: text

 Iteración 1: Traducción básica (método por defecto)
 +- Resultado: Funcional pero mejorable
 +- Tiempo: 60% del total

 Iteración 2: Aplicar tácticas para objetivos
 +- Resultado: Mejor claridad y consistencia
 +- Tiempo: 30% del total

 Iteración 3: Pulir y perfeccionar
 +- Resultado: Calidad profesional
 +- Tiempo: 10% del total

**Mentalidad:**

 "Hecho es mejor que perfecto" (para iteración 1)

 Pero: "Iteramos hasta alcanzar calidad profesional"

----

Aplicación de los Principios
=============================

Caso de Uso: Traducir una Sección
----------------------------------

**Aplicando los 10 principios:**

1. **Principio 1 (Transformación):**
 Entender que esto es transformación sistemática

2. **Principio 2 (Signifié):**
 Identificar función semántica de cada elemento

3. **Principio 3 (Método defecto):**
 Aplicar segmentación-rendición-preferencia

4. **Principio 4 (Objetivos):**
 Identificar si se necesita domesticación, claridad, etc.

5. **Principio 5 (Tácticas):**
 Seleccionar táctica apropiada al objetivo

6. **Principio 6 (Preservación):**
 Verificar que contenido está completo

7. **Principio 7 (Adaptación):**
 Usar sintaxis nativa RST

8. **Principio 8 (Validación):**
 Compilar y verificar

9. **Principio 9 (Documentación):**
 Documentar decisiones importantes

10. **Principio 10 (Iteración):**
 Revisar y mejorar

Checklist Rápida
----------------

.. code-block:: text

 Antes de empezar:
 [ ] Entiendo que es transformación sistemática (P1)
 [ ] Sé que preservo contenido, adapto forma (P2)

 Durante la traducción:
 [ ] Aplico método por defecto (P3)
 [ ] Identifico objetivos si divergo (P4)
 [ ] Uso tácticas catalogadas (P5)
 [ ] Verifico preservación semántica (P6)
 [ ] Uso sintaxis nativa RST (P7)
 [ ] Compilo frecuentemente (P8)

 Después de traducir:
 [ ] Documento decisiones importantes (P9)
 [ ] Planeo iteración de mejora (P10)

----

Relación con Otros Documentos
==============================

**Estos principios se desarrollan en:**

- :doc:`_fundamentos_conceptuales/traduccion_como_transformacion` (P1)
- :doc:`_fundamentos_conceptuales/signifiant_vs_signifie` (P2)
- :doc:`_metodologias/metodo_por_defecto` (P3)
- :doc:`objetivos_tacticas` (P4, P5)
- :doc:`/docs_maestros/SINTESIS_METODOLOGICA_ADT` (todos)

----

Conclusión
==========

**Síntesis:**

Los 10 principios fundamentales de ADT proporcionan:

1. **Base teórica** sólida (P1, P2)
2. **Método sistemático** (P3, P4, P5)
3. **Garantías de calidad** (P6, P7, P8)
4. **Sostenibilidad** (P9, P10)

**Resultado:**

 Traducciones de calidad profesional, consistentes, y mejorables.

**Próximo paso:**

 Estudiar :doc:`objetivos_tacticas` para aplicación práctica.

----

Referencias
===========

- Micheli, D. (2014). Translation Technique in Peshitta Zechariah
- Nida, E. (1964). Toward a Science of Translating
- Toury, G. (1995). Descriptive Translation Studies
- ISO 1087:2019 - Terminology work

----

**Versión:** 1.0
**Fecha:** 2026-01-27
**Estado:** Aprobado - Base metodológica del proyecto
