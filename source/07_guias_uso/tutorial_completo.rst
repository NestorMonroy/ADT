.. _tutorial_completo:

===============================================
Tutorial Completo ADT
===============================================

:Tiempo: 2-3 horas
:Nivel: Principiante a Intermedio
:Prerequisitos: Haber leído :doc:`guia_rapida`
:Resultado: Dominio completo del sistema ADT

.. contents:: Contenido
   :depth: 3
   :local:

----

Introducción
============

Este tutorial te guía **paso a paso** a través de todo el sistema ADT.

**¿En qué se diferencia de la guía rápida?**

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - **Aspecto**
     - **Guía Rápida**
     - **Tutorial Completo**
   * - Tiempo
     - 15 minutos
     - 2-3 horas
   * - Profundidad
     - Conceptos básicos
     - Todos los detalles
   * - Práctica
     - 1 ejercicio simple
     - Proyecto completo
   * - Resultado
     - Listo para empezar
     - Dominio completo

**Estructura del tutorial:**

.. code-block:: text

   Módulo 1: Fundamentos (30 min)
   Módulo 2: PASO 0 en Profundidad (30 min)
   Módulo 3: Decisiones de Traducción (45 min)
   Módulo 4: Verificación Avanzada (30 min)
   Módulo 5: Proyecto Completo (45 min)

----

Módulo 1: Fundamentos del Sistema ADT
======================================

Duración: 30 minutos

1.1 Conceptos Fundamentales
----------------------------

**El Isomorfismo Básico**

ADT se basa en que traducción de documentación técnica ES una transformación de modelos.

.. code-block:: text

   TRADUCCIÓN DE TEXTOS     ←→     TRANSFORMACIÓN DE MODELOS
   
   Texto fuente                    PIM (Platform-Independent Model)
   Texto destino                   PSM (Platform-Specific Model)
   Técnica de traducción           Reglas de transformación
   Preservar significado           Preservar semántica

**Leer:** :doc:`../01_fundamentos/_fundamentos_conceptuales/traduccion_como_transformacion`

**Signifiant vs Signifié**

La decisión fundamental en traducción:

.. code-block:: text

   SIGNIFIANT (Significante)        SIGNIFIÉ (Significado)
   La FORMA externa                 El CONTENIDO semántico
   
   Ejemplo LaTeX:
   Signifiant: \textbf{texto}       Signifié: "énfasis fuerte"
   
   Ejemplo RST:
   Signifiant: **texto**            Signifié: "énfasis fuerte"
   
   Decisión ADT: Preservar Signifié, adaptar Signifiant

**Leer:** :doc:`../01_fundamentos/_fundamentos_conceptuales/signifiant_vs_signifie`

**Ejercicio 1.1:**

.. code-block:: text

   Identifica Signifiant y Signifié:
   
   Original LaTeX: \section{Introduction}
   
   Signifiant: _______________________
   Signifié: _______________________
   
   Traducción RST: _______________________

**Respuesta:**

.. code-block:: text

   Signifiant original: \section{Introduction}
   Signifié: "Sección de nivel 1 con título 'Introduction'"
   Signifiant RST: 
   
   Introduction
   ============

1.2 Los 5 Criterios de Calidad
-------------------------------

**Repaso de** :doc:`../03_estandares/calidad/criterios_calidad`

1. **Completitud (100%)**
   
   .. code-block:: text
   
      TODO el contenido del original debe estar presente.
      
      Verificación:
      ☐ Todos los párrafos
      ☐ Todas las listas
      ☐ Todas las tablas
      ☐ Todas las imágenes
      ☐ Todas las referencias

2. **Precisión Técnica (100%)**
   
   .. code-block:: text
   
      Terminología correcta y consistente.
      
      Verificación:
      ☐ Términos técnicos correctos
      ☐ Mismo término siempre igual
      ☐ Conceptos traducidos con precisión

3. **Enriquecimiento Apropiado**
   
   .. code-block:: text
   
      Proporcional a complejidad del original.
      
      Rangos:
      < 20 líneas  → +300% a +1000%
      20-50 líneas → +100% a +300%
      50-100 líneas → +80% a +150%
      > 100 líneas  → +50% a +100%

4. **Formato y Compilación (100%)**
   
   .. code-block:: text
   
      Debe compilar exitosamente.
      
      Verificación:
      ☐ make html exitoso
      ☐ 0 errores críticos
      ☐ Warnings solo esperados

5. **Verificación Sistemática (100%)**
   
   .. code-block:: text
   
      Checklist completo contra original.
      
      Herramientas:
      - Checklist manual
      - Script automatizado
      - Comparación visual

**Ejercicio 1.2:**

.. code-block:: text

   Calcula la calidad de esta traducción:
   
   Original: 30 líneas, 5 párrafos, 2 listas
   Traducido: 90 líneas, 5 párrafos, 2 listas, 1 tabla agregada
   Compilación: Exitosa
   Verificación: Checklist 10/10
   
   Completitud: ____%
   Enriquecimiento: ____%
   Apropiado según MD-002: Sí/No
   Calidad total: ____%

**Respuesta:**

.. code-block:: text

   Completitud: 100% (todos los elementos presentes)
   Enriquecimiento: +200% ((90-30)/30 × 100)
   Apropiado: SÍ (20-50 líneas → +100% a +300%)
   Calidad total: 100% ✅

1.3 Las 2 Matrices Críticas
----------------------------

**MD-002: Cuándo Enriquecer**

Tabla de referencia rápida:

.. code-block:: text

   TAMAÑO  │ RANGO         │ PROMEDIO  │ EJEMPLO
   ────────┼───────────────┼───────────┼──────────────
   <20     │ +300% a +1000%│ +771%     │ Tips arc42
   20-50   │ +100% a +300% │ +273%     │ Section-12
   50-100  │ +80% a +150%  │ +95%      │ Section-11
   >100    │ +50% a +100%  │ +80%      │ Section-10

**Leer completo:** :doc:`../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer`

**MD-004: Traducir vs Conservar**

Árbol de decisión simplificado:

.. code-block:: text

   ¿Acrónimo técnico? (API, REST, JSON)
   ├─ SÍ → CONSERVAR
   └─ NO → ¿Patrón/Metodología? (Singleton, Scrum)
       ├─ SÍ → CONSERVAR
       └─ NO → ¿Rol establecido? (Product Owner)
           ├─ SÍ → CONSERVAR
           └─ NO → ¿Concepto general? (Quality, Risk)
               ├─ SÍ → TRADUCIR
               └─ NO → Evaluar caso por caso

**Leer completo:** :doc:`../04_reglas_operativas/matrices_decision/MD_004_traducir_vs_conservar`

**Ejercicio 1.3:**

.. code-block:: text

   Decide para cada término:
   
   1. "Stakeholder" → ____________
   2. "Calidad" → ____________
   3. "Circuit Breaker" → ____________
   4. "Decisión arquitectónica" → ____________
   5. "ATAM" → ____________

**Respuestas:**

.. code-block:: text

   1. "Stakeholder" → CONSERVAR (rol establecido)
   2. "Calidad" → Ya está en español ✅
   3. "Circuit Breaker" → CONSERVAR (patrón)
   4. "Decisión arquitectónica" → Ya está en español ✅
   5. "ATAM" → CONSERVAR (metodología/acrónimo)

----

Módulo 2: PASO 0 en Profundidad
================================

Duración: 30 minutos

2.1 Por Qué PASO 0 es Crítico
------------------------------

**Caso Real: Sección 07 de arc42**

.. code-block:: text

   ERROR (sin PASO 0 completo):
   - Solo leídas 50 de 126 líneas
   - Identificados 7 de 13 elementos
   - Resultado: 6 secciones omitidas
   - Costo: 2 horas de re-trabajo
   
   CORRECTO (con PASO 0 completo):
   - Leídas 126 de 126 líneas
   - Identificados 13 de 13 elementos
   - Resultado: 0 omisiones
   - Costo: 0 horas de re-trabajo
   
   Diferencia: 15 min en PASO 0 → Ahorro de 2 horas

**Leer:** :doc:`../06_casos_practicos/errores_comunes/error_01_omisiones`

**Estadísticas:**

.. code-block:: text

   Traducciones SIN PASO 0 completo:
   - Omisiones: 40% de proyectos
   - Re-trabajo: 30% del tiempo
   
   Traducciones CON PASO 0 completo:
   - Omisiones: 5% de proyectos
   - Re-trabajo: 10% del tiempo

2.2 PASO 0: Procedimiento Detallado
------------------------------------

**Sub-paso 1: Abrir y Verificar (2 min)**

.. code-block:: text

   ☐ 1. Abrir archivo original
   ☐ 2. Verificar codificación (UTF-8)
   ☐ 3. Contar líneas totales
   ☐ 4. Anotar: "Este archivo tiene ___ líneas"

**Sub-paso 2: Lectura Primera Pasada (5-7 min)**

.. code-block:: text

   ☐ 1. Leer desde línea 1
   ☐ 2. Marcar elementos encontrados con ✓
   ☐ 3. NO saltarse nada
   ☐ 4. Leer hasta última línea
   ☐ 5. Verificar: "Leí ___ líneas de ___ totales"

**Sub-paso 3: Inventario Exhaustivo (3-5 min)**

.. code-block:: text

   ☐ 1. Listar elementos principales:
       - Títulos de sección
       - Subsecciones
       - Párrafos importantes
       - Tablas
       - Imágenes
       - Código
       - Referencias
   
   ☐ 2. Contar: "Identifiqué ___ elementos"
   
   ☐ 3. Listar archivos asociados:
       - Tips
       - Ejemplos
       - Includes
       
   ☐ 4. Total: "___ archivos para traducir"

**Sub-paso 4: Estimación (1-2 min)**

.. code-block:: text

   ☐ 1. Clasificar por tamaño:
       < 20 líneas → Tipo A
       20-50 líneas → Tipo B
       50-100 líneas → Tipo C
       > 100 líneas → Tipo D
   
   ☐ 2. Estimar enriquecimiento según MD-002
   
   ☐ 3. Estimar tiempo:
       Tipo A: 1-2 horas/archivo
       Tipo B: 30-60 min/archivo
       Tipo C: 45-90 min/archivo
       Tipo D: 2-3 horas/archivo
   
   ☐ 4. Total estimado: "___ horas"

**Ejercicio 2.1:**

Aplica PASO 0 a este documento:

.. code-block:: text

   --- (línea 1)
   title: "Quality Scenarios"
   ---
   
   Quality scenarios are concrete examples of
   quality requirements.
   
   Types:
   - Use scenarios
   - Change scenarios
   - Failure scenarios
   
   Example:
   "System responds within 2 seconds for 95%
   of requests under normal load"
   
   See also: Quality Requirements section
   --- (línea 20)

**Tu turno:**

.. code-block:: text

   Total líneas: ___
   Elementos identificados:
   1. _______________
   2. _______________
   3. _______________
   4. _______________
   5. _______________
   
   Tipo según tamaño: ___
   Enriquecimiento objetivo: ___
   Tiempo estimado: ___

**Respuesta:**

.. code-block:: text

   Total líneas: 20
   Elementos identificados:
   1. Título "Quality Scenarios"
   2. Definición (línea 5-6)
   3. Lista de 3 tipos
   4. Ejemplo (líneas 13-14)
   5. Referencia (línea 17)
   
   Tipo según tamaño: A (<20 líneas)
   Enriquecimiento objetivo: +300% a +1000%
   Tiempo estimado: 1-2 horas

2.3 Herramientas para PASO 0
-----------------------------

**Script de Ayuda:**

.. code-block:: bash

   #!/bin/bash
   # paso_0_helper.sh
   
   ARCHIVO="$1"
   
   echo "╔══════════════════════════════════════╗"
   echo "║   ASISTENTE PASO 0                  ║"
   echo "╚══════════════════════════════════════╝"
   echo ""
   
   if [ ! -f "$ARCHIVO" ]; then
       echo "❌ Archivo no existe: $ARCHIVO"
       exit 1
   fi
   
   LINEAS=$(wc -l < "$ARCHIVO")
   SECCIONES=$(grep -c "^#" "$ARCHIVO" 2>/dev/null || echo "0")
   CODIGO=$(grep -c "^\`\`\`" "$ARCHIVO" 2>/dev/null || echo "0")
   TABLAS=$(grep -c "^|" "$ARCHIVO" 2>/dev/null || echo "0")
   
   echo "📄 Archivo: $ARCHIVO"
   echo "📊 Líneas totales: $LINEAS"
   echo "📑 Secciones (#): $SECCIONES"
   echo "💻 Bloques de código: $CODIGO"
   echo "📋 Tablas: $TABLAS"
   echo ""
   
   # Clasificar
   if [ $LINEAS -lt 20 ]; then
       TIPO="A (<20)"
       ENRIQ="+300% a +1000%"
       TIEMPO="1-2 horas"
   elif [ $LINEAS -lt 50 ]; then
       TIPO="B (20-50)"
       ENRIQ="+100% a +300%"
       TIEMPO="30-60 min"
   elif [ $LINEAS -lt 100 ]; then
       TIPO="C (50-100)"
       ENRIQ="+80% a +150%"
       TIEMPO="45-90 min"
   else
       TIPO="D (>100)"
       ENRIQ="+50% a +100%"
       TIEMPO="2-3 horas"
   fi
   
   echo "🎯 Tipo: $TIPO líneas"
   echo "📈 Enriquecimiento objetivo: $ENRIQ"
   echo "⏱️  Tiempo estimado: $TIEMPO"
   echo ""
   echo "☑️  ¿Leíste las $LINEAS líneas completas? (s/n)"
   read respuesta
   
   if [ "$respuesta" != "s" ]; then
       echo ""
       echo "⚠️  ADVERTENCIA: Lee COMPLETO antes de continuar"
       exit 1
   fi
   
   echo ""
   echo "✅ PASO 0 completado. Continúa con traducción."

**Uso:**

.. code-block:: bash

   $ bash paso_0_helper.sh document.md
   
   Archivo: document.md
   Líneas totales: 35
   ...
   Tipo: B (20-50) líneas
   Enriquecimiento objetivo: +100% a +300%

**Plantilla de Inventario:**

.. code-block:: text

   INVENTARIO - PASO 0
   ===================
   
   Archivo: _______________________
   Fecha: _______________________
   
   INFORMACIÓN BÁSICA:
   - Total líneas: _____
   - Tipo (A/B/C/D): _____
   - Complejidad: Baja / Media / Alta
   
   ELEMENTOS IDENTIFICADOS:
   
   Secciones principales:
   ☐ 1. _______________________
   ☐ 2. _______________________
   ☐ 3. _______________________
   
   Subsecciones:
   ☐ 1. _______________________
   ☐ 2. _______________________
   
   Elementos especiales:
   ☐ Tablas: _____
   ☐ Imágenes: _____
   ☐ Código: _____
   ☐ Listas: _____
   
   ARCHIVOS ASOCIADOS:
   ☐ Tips: _____
   ☐ Ejemplos: _____
   ☐ Otros: _____
   
   Total archivos: _____
   
   ESTIMACIÓN:
   - Enriquecimiento objetivo: _____
   - Tiempo estimado: _____
   - Fecha inicio: _____
   - Fecha objetivo: _____
   
   CHECKLIST PASO 0:
   ☐ Leí archivo completo
   ☐ Identifiqué todos los elementos
   ☐ Conté archivos asociados
   ☐ Estimé tiempo y enriquecimiento
   ☐ Listo para traducir

----

Módulo 3: Decisiones de Traducción
===================================

Duración: 45 minutos

3.1 Decisión de Enriquecimiento (MD-002)
-----------------------------------------

**Proceso de Decisión Detallado:**

**Paso 1: Clasificar Original**

.. code-block:: text

   Contar líneas exactas del archivo:
   
   Resultado: ___ líneas
   
   Buscar en tabla MD-002:
   ___ líneas → Tipo ___ → Rango: ___

**Paso 2: Identificar Tipo de Contenido**

.. code-block:: text

   ¿Qué tipo de contenido es?
   
   ☐ Tip/consejo breve → Enriquecimiento ALTO
   ☐ Sección principal → Enriquecimiento MEDIO
   ☐ Ejemplo con código → Enriquecimiento ALTO
   ☐ Lista extensa → Enriquecimiento BAJO
   ☐ Narrativa detallada → Enriquecimiento MEDIO-BAJO

**Paso 3: Decidir Qué Agregar**

Para tips breves (<20 líneas):

.. code-block:: text

   ✅ SIEMPRE agregar:
   - 2-3 ejemplos prácticos
   - Tabla comparativa (antes/después, con/sin)
   - Checklist accionable (3-5 items)
   - Casos de uso (cuándo aplicar)
   
   ⚠️  CONSIDERAR agregar:
   - Pasos numerados (1, 2, 3...)
   - Herramientas específicas
   - Métricas de éxito
   - Diagramas simples
   
   ❌ EVITAR agregar:
   - Teoría abstracta sin ejemplos
   - Información no relacionada
   - Divagaciones filosóficas

Para secciones medianas (20-50 líneas):

.. code-block:: text

   ✅ SIEMPRE agregar:
   - Tip contextual inicial
   - 1-2 ejemplos adicionales
   - Sección "Relación con otras secciones"
   
   ⚠️  CONSIDERAR agregar:
   - Tabla comparativa si clarifica
   - Mejores prácticas
   - Nota sobre puntos complejos
   
   ❌ EVITAR agregar:
   - Subsecciones innecesarias
   - Duplicación de contenido
   - Ejemplos redundantes

**Ejercicio 3.1:**

Decide enriquecimiento para:

.. code-block:: text

   Documento A:
   - 12 líneas
   - Tip sobre nomenclatura
   - Sin ejemplos
   
   Enriquecimiento objetivo: ___
   Qué agregar:
   1. _______________
   2. _______________
   3. _______________

**Respuesta:**

.. code-block:: text

   Enriquecimiento objetivo: +300% a +1000%
   Traducido esperado: 36 a 120 líneas
   
   Qué agregar:
   1. Tabla "Nomenclatura Buena vs Mala" (20 líneas)
   2. 3 ejemplos prácticos (30 líneas)
   3. Checklist de verificación (15 líneas)
   4. Herramientas (linters) (10 líneas)
   
   Total agregado: ~75 líneas
   Total traducido: ~87 líneas (+625%) ✅

3.2 Decisión de Terminología (MD-004)
--------------------------------------

**Proceso de Decisión Detallado:**

**Paso 1: Identificar Tipo de Término**

.. code-block:: text

   Término: _______________________
   
   Verificar categoría:
   
   ☐ ¿Es acrónimo? (API, REST, JSON, UML)
   ☐ ¿Es patrón de diseño? (Singleton, Factory)
   ☐ ¿Es metodología? (Scrum, ATAM, Kanban)
   ☐ ¿Es rol establecido? (Product Owner, Stakeholder)
   ☐ ¿Es concepto general? (Quality, Risk, Goal)
   ☐ ¿Es verbo/adjetivo? (Implement, Complex)
   ☐ ¿Tiene traducción ISO? (Technical Debt)
   ☐ ¿Es neologismo reciente? (<5 años)

**Paso 2: Aplicar Regla**

.. code-block:: text

   Si es acrónimo/patrón/metodología/rol:
   → CONSERVAR en inglés
   
   Si es concepto/verbo/adjetivo/ISO:
   → TRADUCIR al español
   
   Si es neologismo sin consenso:
   → CONSERVAR hasta establecerse traducción
   
   Si no está claro:
   → Buscar en Google (término inglés vs español)
   → Si inglés >> español (10x): CONSERVAR
   → Si español ≈ inglés: TRADUCIR

**Paso 3: Documentar Decisión**

.. code-block:: text

   Agregar al glosario del proyecto:
   
   | Término | Decisión | Razón | Secciones |
   |---------|----------|-------|-----------|
   | API | Conservar | Acrónimo | Todas |
   | Quality | Calidad | Concepto | 10 |

**Paso 4: Mantener Consistencia**

.. code-block:: text

   ANTES de usar término por primera vez:
   ☐ Buscar en glosario
   
   SI está en glosario:
   → Usar decisión documentada
   
   SI NO está en glosario:
   → Aplicar proceso de decisión
   → Agregar al glosario
   → Usar consistentemente

**Ejercicio 3.2:**

Decide para estos términos:

.. code-block:: text

   1. "Microservice"
      Categoría: _______________
      Decisión: _______________
      Razón: _______________
   
   2. "Deployment Pipeline"
      Categoría: _______________
      Decisión: _______________
      Razón: _______________
   
   3. "Arquitectura"
      Decisión: _______________

**Respuestas:**

.. code-block:: text

   1. "Microservice"
      Categoría: Estilo arquitectónico
      Decisión: Microservicio (adaptado al español)
      Razón: Ampliamente usado en español, tiene forma hispanizada
   
   2. "Deployment Pipeline"
      Categoría: Término técnico compuesto
      Decisión: Pipeline de deployment
      Razón: "Pipeline" técnico, "deployment" conservado en contexto
   
   3. "Arquitectura"
      Decisión: Ya está en español ✅

3.3 Decisiones en Tiempo Real
------------------------------

**Durante traducción surgen preguntas:**

**Pregunta Tipo 1: Enriquecimiento**

.. code-block:: text

   "Este párrafo es muy breve (3 líneas), ¿lo expando?"
   
   → Consultar MD-002
   → Si documento < 20 líneas total: SÍ, expandir
   → Si documento > 100 líneas total: NO, dejar conciso
   → Agregar ejemplo si clarifica concepto

**Pregunta Tipo 2: Terminología**

.. code-block:: text

   "¿Traduzco 'Product Owner'?"
   
   → Consultar MD-004
   → Rol Scrum oficial → CONSERVAR
   → "Product Owner" ✅

**Pregunta Tipo 3: Estructura**

.. code-block:: text

   "¿Divido esta sección larga en subsecciones?"
   
   → Si > 100 líneas: Considerar división
   → Si estructura natural existe: Sí
   → Si artificial: No
   → Objetivo: Mejorar navegabilidad sin alterar mensaje

**Pregunta Tipo 4: Formato**

.. code-block:: text

   "¿Convierto esta lista en tabla?"
   
   → Si mejora claridad: Sí
   → Si lista es simple (< 5 items): No necesario
   → Si lista tiene estructura (columnas): Sí, usar tabla

----

Módulo 4: Verificación Avanzada
================================

Duración: 30 minutos

4.1 Verificación en 3 Niveles
------------------------------

**Nivel 1: Verificación Automática (5 min)**

**Script de Verificación Básica:**

.. code-block:: bash

   #!/bin/bash
   # verificar_basico.sh
   
   ORIGINAL="$1"
   TRADUCIDO="$2"
   
   echo "Verificación Básica"
   echo "==================="
   echo ""
   
   # Contar elementos
   ORIG_LINES=$(wc -l < "$ORIGINAL")
   TRAD_LINES=$(wc -l < "$TRADUCIDO")
   
   ORIG_SECCIONES=$(grep -c "^#" "$ORIGINAL")
   TRAD_SECCIONES=$(grep -c "^=" "$TRADUCIDO")
   
   ORIG_LISTAS=$(grep -c "^-\|^*\|^[0-9]" "$ORIGINAL")
   TRAD_LISTAS=$(grep -c "^-\|^*\|^[0-9]" "$TRADUCIDO")
   
   echo "Líneas:"
   echo "  Original: $ORIG_LINES"
   echo "  Traducido: $TRAD_LINES"
   ENRIQ=$(( (TRAD_LINES - ORIG_LINES) * 100 / ORIG_LINES ))
   echo "  Enriquecimiento: +$ENRIQ%"
   echo ""
   
   echo "Secciones:"
   echo "  Original: $ORIG_SECCIONES"
   echo "  Traducido: $TRAD_SECCIONES"
   if [ $ORIG_SECCIONES -eq $TRAD_SECCIONES ]; then
       echo "  ✅ Coinciden"
   else
       echo "  ⚠️  NO coinciden - Verificar omisiones"
   fi
   echo ""
   
   echo "Listas:"
   echo "  Original: $ORIG_LISTAS"
   echo "  Traducido: $TRAD_LISTAS"
   if [ $ORIG_LISTAS -le $TRAD_LISTAS ]; then
       echo "  ✅ OK"
   else
       echo "  ⚠️  Menos listas en traducción"
   fi

**Nivel 2: Verificación Manual (15 min)**

**Checklist Exhaustivo:**

.. code-block:: text

   VERIFICACIÓN ELEMENTO POR ELEMENTO
   
   Abrir original y traducción lado a lado
   
   ☐ Línea 1 original → ¿Presente en traducción?
   ☐ Línea 2 original → ¿Presente en traducción?
   ...
   ☐ Línea N original → ¿Presente en traducción?
   
   VERIFICACIÓN POR TIPO DE ELEMENTO
   
   Títulos:
   ☐ ___________ → ☐ Traducido
   ☐ ___________ → ☐ Traducido
   
   Párrafos:
   ☐ Párrafo 1 → ☐ Presente
   ☐ Párrafo 2 → ☐ Presente
   
   Listas:
   ☐ Lista 1 (___ items) → ☐ ___ items traducidos
   ☐ Lista 2 (___ items) → ☐ ___ items traducidos
   
   Tablas:
   ☐ Tabla 1 (___ filas) → ☐ ___ filas traducidas
   
   Imágenes:
   ☐ Imagen 1 → ☐ Referenciada
   
   Código:
   ☐ Bloque 1 → ☐ Presente
   
   Referencias:
   ☐ Ref 1 → ☐ Traducida

**Nivel 3: Verificación de Calidad (10 min)**

**Checklist de Calidad:**

.. code-block:: text

   COMPLETITUD:
   ☐ 100% contenido original presente
   ☐ 0% omisiones detectadas
   ☐ Todas las secciones incluidas
   ☐ Todas las referencias incluidas
   
   PRECISIÓN:
   ☐ Terminología consistente
   ☐ Conceptos correctos
   ☐ Sin errores técnicos
   
   ENRIQUECIMIENTO:
   ☐ En rango apropiado según MD-002
   ☐ Ejemplos agregan valor
   ☐ Sin divagaciones
   
   FORMATO:
   ☐ Compilación Sphinx exitosa
   ☐ 0 errores críticos
   ☐ Warnings documentados
   ☐ HTML se ve bien
   
   VERIFICACIÓN:
   ☐ Checklist completado
   ☐ Script ejecutado
   ☐ Revisión visual hecha
   ☐ Checkpoint creado

4.2 Compilación y Depuración
-----------------------------

**Compilar Frecuentemente:**

.. code-block:: bash

   # Durante traducción (cada lote)
   make html
   
   # Si hay errores
   # 1. Leer mensaje completo
   # 2. Identificar archivo y línea
   # 3. Corregir
   # 4. Intentar de nuevo

**Errores Comunes y Soluciones:**

**Error 1: Título Mal Formado**

.. code-block:: text

   ERROR:
   Title underline too short.
   
   CAUSA:
   ===============
   Título Muy Largo
   ===============
   
   SOLUCIÓN:
   =========================
   Título Muy Largo
   =========================

**Error 2: Lista Mal Indentada**

.. code-block:: text

   ERROR:
   Unexpected indentation
   
   CAUSA:
   - Item 1
     - SubItem (mal indentado)
   
   SOLUCIÓN:
   - Item 1
   
     - SubItem (línea vacía + 2 espacios)

**Error 3: Referencia Rota**

.. code-block:: text

   ERROR:
   undefined label: seccion_5
   
   CAUSA:
   :ref:`seccion_5`
   
   SOLUCIÓN:
   1. Verificar que label existe
   2. Crear label si falta:
      .. _seccion_5:

4.3 Herramientas de Verificación Avanzadas
-------------------------------------------

**Script de Verificación Completa:**

.. code-block:: bash

   #!/bin/bash
   # verificar_completo.sh
   
   # Uso: bash verificar_completo.sh original/ traduccion/
   
   ORIGINAL_DIR="$1"
   TRADUCCION_DIR="$2"
   
   echo "╔══════════════════════════════════════╗"
   echo "║   VERIFICACIÓN COMPLETA             ║"
   echo "╚══════════════════════════════════════╝"
   echo ""
   
   # Contar archivos
   ORIG_FILES=$(find "$ORIGINAL_DIR" -name "*.md" | wc -l)
   TRAD_FILES=$(find "$TRADUCCION_DIR" -name "*.rst" | wc -l)
   
   echo "📂 Archivos:"
   echo "   Original: $ORIG_FILES archivos .md"
   echo "   Traducido: $TRAD_FILES archivos .rst"
   
   if [ $TRAD_FILES -ge $ORIG_FILES ]; then
       echo "   ✅ Todos los archivos traducidos"
   else
       echo "   ❌ FALTAN $((ORIG_FILES - TRAD_FILES)) archivos"
   fi
   echo ""
   
   # Compilar
   echo "🔨 Compilando..."
   make html > /tmp/compile.log 2>&1
   
   if [ $? -eq 0 ]; then
       echo "   ✅ Compilación exitosa"
   else
       echo "   ❌ Compilación con errores"
       echo "   Ver: /tmp/compile.log"
   fi
   echo ""
   
   # Warnings
   WARNINGS=$(grep -c "WARNING" /tmp/compile.log)
   echo "⚠️  Warnings: $WARNINGS"
   
   if [ $WARNINGS -gt 0 ]; then
       echo "   Revisar: /tmp/compile.log"
   fi
   echo ""
   
   echo "✅ Verificación completada"

----

Módulo 5: Proyecto Completo
============================

Duración: 45 minutos

5.1 Ejercicio Final: Traducir Sección Completa
-----------------------------------------------

**Contexto:**

Vas a traducir una sección completa simulada del estilo arc42.

**Documento Original:**

.. code-block:: text

   ---
   title: "Section 9: Architecture Decisions"
   ---
   
   # 9. Architecture Decisions
   
   ## Content
   
   Important architecture decisions and design decisions
   that affect the system.
   
   Document the reasoning behind your decisions to help
   future developers understand WHY things are the way
   they are.
   
   ## Motivation
   
   Architecture decisions are hard to change later.
   Documenting them prevents repeating past debates.
   
   ## Form
   
   Use Architecture Decision Records (ADR) format:
   
   - Title
   - Status (proposed/accepted/deprecated)
   - Context
   - Decision
   - Consequences
   
   ## 9.1 ADR Template
   
   Create template with sections above.
   
   [Total: 38 líneas]

**Tu Tarea (45 minutos):**

1. **PASO 0 (10 min)**
   
   .. code-block:: text
   
      ☐ Leer completo (38 líneas)
      ☐ Identificar elementos
      ☐ Estimar enriquecimiento
      ☐ Planificar traducción

2. **Traducir (25 min)**
   
   .. code-block:: text
   
      ☐ Aplicar MD-002 (20-50 líneas → +100% a +300%)
      ☐ Aplicar MD-004 para términos
      ☐ Agregar enriquecimiento apropiado
      ☐ Crear archivo .rst

3. **Verificar (10 min)**
   
   .. code-block:: text
   
      ☐ Checklist de elementos
      ☐ Compilar (si tienes Sphinx)
      ☐ Revisar resultado

**Elementos a Identificar:**

.. code-block:: text

   Elementos del original:
   
   ☐ 1. Título "9. Architecture Decisions"
   ☐ 2. Content (líneas 6-12)
   ☐ 3. Motivation (líneas 14-16)
   ☐ 4. Form (líneas 18-25)
   ☐ 5. Lista ADR format (5 items)
   ☐ 6. Subsección 9.1 (líneas 27-29)
   
   Total: 6 elementos principales

**Decisiones de Terminología:**

.. code-block:: text

   "Architecture Decisions" → _______________
   "Design decisions" → _______________
   "Architecture Decision Records" → _______________
   "ADR" → _______________
   "Template" → _______________

**Solución Sugerida (Próxima Página):**

... (continúa con solución paso a paso)

5.2 Revisión y Feedback
-----------------------

**Auto-Evaluación:**

.. code-block:: text

   Después de tu traducción, evalúate:
   
   COMPLETITUD:
   ☐ Los 6 elementos presentes: Sí/No
   ☐ 0 omisiones: Sí/No
   
   ENRIQUECIMIENTO:
   Líneas traducidas: ___
   Enriquecimiento: ____%
   ¿En rango +100% a +300%?: Sí/No
   
   TERMINOLOGÍA:
   ☐ Decisiones consistentes con MD-004: Sí/No
   ☐ Sin variaciones de términos: Sí/No
   
   FORMATO:
   ☐ Sintaxis RST correcta: Sí/No
   ☐ Compila (si probaste): Sí/No
   
   Calidad total: ____%

5.3 Próximos Pasos
------------------

**Después de este tutorial:**

.. code-block:: text

   Nivel Alcanzado: INTERMEDIO
   
   Puedes:
   ✅ Aplicar workflow completo
   ✅ Tomar decisiones objetivas
   ✅ Verificar sistemáticamente
   ✅ Documentar resultados
   
   Próximos desafíos:
   ☐ Traducir proyecto real completo
   ☐ Optimizar tu velocidad
   ☐ Crear tus propias plantillas
   ☐ Compartir casos de éxito

**Recursos Avanzados:**

1. :doc:`../02_procedimientos/workflow_general`
   
   Workflow completo v1.7.2 (126 KB)

2. :doc:`../06_casos_practicos/antes_despues/caso_01_seccion_breve`
   
   Caso real completo de arc42

3. :doc:`../03_estandares/calidad/criterios_calidad`
   
   Criterios de calidad en profundidad

----

Conclusión
==========

**Felicidades por completar el tutorial completo.**

**Has aprendido:**

✅ Fundamentos del sistema ADT  
✅ PASO 0 en profundidad  
✅ Toma de decisiones objetivas (MD-002, MD-004)  
✅ Verificación sistemática en 3 niveles  
✅ Proyecto completo de principio a fin

**Estás listo para:**

✅ Traducir proyectos reales  
✅ Lograr 100% completitud  
✅ Mantener calidad consistente  
✅ Trabajar eficientemente

**Tu próximo proyecto:**

Elige un documento técnico real y aplica todo lo aprendido.

Recuerda siempre:

.. code-block:: text

   1. PASO 0 completo (leer TODO)
   2. Decisiones basadas en MD-002 y MD-004
   3. Verificación sistemática
   4. Documentar resultado
   
   = 100% completitud garantizada

¡Éxito en tus traducciones!

----

.. seealso::
   * :doc:`guia_rapida` - Repaso rápido de 15 minutos
   * :doc:`../06_casos_practicos/index` - Más ejemplos reales
   * :doc:`../02_procedimientos/workflow_general` - Referencia completa del workflow
