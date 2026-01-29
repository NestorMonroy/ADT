.. _prompts:

===============================================
Prompts y Plantillas
===============================================

Prompts de IA y plantillas para automatizar y mejorar la traducción con ADT.

.. contents:: Contenido
 :depth: 2
 :local:

----

Introducción
============

Esta sección contiene **prompts optimizados** para usar con modelos de lenguaje (LLMs) como Claude, ChatGPT, etc., para asistir en traducción técnica siguiendo metodología ADT.

**Uso de prompts:**
- Acelerar traducción manteniendo calidad
- Aplicar consistentemente estándares ADT
- Reducir errores comunes
- Automatizar tareas repetitivas

**Advertencia:**

.. warning::
 Los prompts son **asistentes**, NO reemplazos del traductor humano.

 SIEMPRE:
 - Revisar output del LLM
 - Verificar contra checklists ADT
 - Aplicar PASO 0 manualmente
 - Validar terminología (MD-004)

----

Prompts Disponibles
===================

Prompts Maestros
----------------

**Prompt Maestro de Traducción:**

Prompt completo que incluye toda la metodología ADT para traducción LaTeX->RST o Markdown->RST.

.. code-block:: text

 Estado: [RUNNING] En desarrollo
 Archivo: prompt_maestro_traduccion.rst
 Uso: Traducción completa de documentos

**Prompt de PASO 0:**

Prompt específico para ejecutar PASO 0 (lectura completa y análisis).

.. code-block:: text

 Estado: [RUNNING] Planeado
 Archivo: prompt_paso_0.rst
 Uso: Análisis pre-traducción

**Prompt de Verificación:**

Prompt para verificar traducción contra criterios de calidad ADT.

.. code-block:: text

 Estado: [RUNNING] Planeado
 Archivo: prompt_verificacion.rst
 Uso: QA post-traducción

Prompts Condicionales
---------------------

Prompts que se activan según condiciones específicas.

**Por tamaño de contenido:**

.. code-block:: text

 [RUNNING] prompt_tip_breve.rst (< 20 líneas)
 [RUNNING] prompt_seccion_corta.rst (20-50 líneas)
 [RUNNING] prompt_seccion_extensa.rst (> 100 líneas)

**Por tipo de contenido:**

.. code-block:: text

 [RUNNING] prompt_codigo_fuente.rst
 [RUNNING] prompt_tabla_datos.rst
 [RUNNING] prompt_diagrama.rst

Ver: :doc:`prompts_condicionales/index`

Plantillas
----------

Plantillas reutilizables para diferentes tipos de documentos.

.. code-block:: text

 [RUNNING] plantilla_manual_usuario.rst
 [RUNNING] plantilla_documentacion_api.rst
 [RUNNING] plantilla_tutorial.rst

Ver: :doc:`plantillas/index`

----

Estructura de un Prompt ADT
============================

Componentes Esenciales
-----------------------

Un prompt ADT efectivo incluye:

**1. Contexto ADT:**

.. code-block:: text

 Eres un traductor técnico experto usando metodología ADT.

 ADT garantiza:
 - Completitud 100%
 - Precisión técnica
 - Enriquecimiento apropiado
 - Compilación exitosa

**2. Reglas Específicas:**

.. code-block:: text

 REGLAS CRÍTICAS:

 1. PASO 0: Lee TODO el contenido antes de traducir
 2. MD-002: Enriquece según tamaño original
 3. MD-004: Conserva términos técnicos apropiadamente
 4. Mantén estructura isomórfica

**3. Input/Output:**

.. code-block:: text

 INPUT: [Contenido original]
 OUTPUT: Traducción en formato RST siguiendo ADT

**4. Verificación:**

.. code-block:: text

 Antes de entregar, verifica:
 [ ] Completitud 100%
 [ ] Terminología consistente
 [ ] Sintaxis RST correcta
 [ ] Enriquecimiento en rango

----

Uso de Prompts con LLMs
========================

Con Claude
----------

**Proceso recomendado:**

.. code-block:: text

 1. Cargar prompt maestro completo
 2. Incluir documento original
 3. Especificar modo (MD-001)
 4. Solicitar traducción
 5. Revisar output manualmente
 6. Aplicar checklist ADT

**Ejemplo:**

.. code-block:: text

 [Prompt maestro ADT completo]

 ---

 DOCUMENTO A TRADUCIR:

 [Pegar contenido original]

 ---

 INSTRUCCIONES:
 - Modo: 2 (Transformación LaTeX->RST)
 - Original: 45 líneas (tip)
 - Enriquecimiento esperado: +300% a +1000%

 Traduce siguiendo PASO 0 completo.

Con ChatGPT
-----------

Similar a Claude, pero:

.. code-block:: text

 [WARNING] Límites de contexto pueden ser menores
 [WARNING] Puede requerir dividir documento grande
 [OK] Bueno para traducciones iterativas

**Estrategia:**

.. code-block:: text

 1. Prompt maestro en mensaje inicial
 2. Documentos por secciones (no todo junto)
 3. Mantener conversación para consistencia
 4. Pedir explicación de decisiones

Con Modelos Locales
--------------------

Para modelos como LLaMA, Mistral, etc.:

.. code-block:: text

 [WARNING] Pueden tener menor capacidad
 [WARNING] Requieren prompts más concisos
 [OK] Mayor privacidad de datos

**Adaptación:**

.. code-block:: text

 1. Simplificar prompt (mantener esencia)
 2. Ejemplos más explícitos
 3. Dividir tareas complejas
 4. Más revisión manual

----

Mejores Prácticas
=================

DO: Buenas Prácticas
--------------------

.. code-block:: text

 [OK] Incluir ejemplos en el prompt
 [OK] Especificar formato de salida exacto
 [OK] Pedir verificación al LLM
 [OK] Usar conversación para iteraciones
 [OK] Mantener contexto de decisiones previas
 [OK] Documentar prompts exitosos

DON'T: Malas Prácticas
-----------------------

.. code-block:: text

 [ERROR] Confiar ciegamente en output
 [ERROR] Omitir revisión humana
 [ERROR] Saltarse PASO 0 manual
 [ERROR] Ignorar checklists ADT
 [ERROR] No verificar terminología
 [ERROR] Usar prompts genéricos sin ADT

Iteración y Mejora
------------------

.. code-block:: text

 1. Usar prompt inicial
 2. Evaluar calidad de output
 3. Identificar problemas recurrentes
 4. Refinar prompt específicamente
 5. Documentar mejoras
 6. Compartir con equipo

----

Limitaciones de LLMs
====================

Qué LLMs Hacen Bien
-------------------

.. code-block:: text

 [OK] Traducción fluida del texto
 [OK] Mantener estructura general
 [OK] Generar ejemplos relevantes
 [OK] Convertir sintaxis (LaTeX->RST)
 [OK] Sugerir enriquecimientos

Qué LLMs Hacen Mal
-------------------

.. code-block:: text

 [ERROR] Inventar contenido no presente
 [ERROR] Omitir secciones sin avisar
 [ERROR] Terminología inconsistente
 [ERROR] Referencias rotas
 [ERROR] Números de línea incorrectos
 [ERROR] Verificación de completitud

Por Qué Siempre Revisar
------------------------

**Errores comunes de LLMs:**

1. **Omisiones silenciosas**
 - Puede omitir párrafos sin avisar
 - Solución: PASO 0 manual + checklist

2. **Invenciones creativas**
 - Puede "mejorar" agregando contenido falso
 - Solución: Comparar línea por línea

3. **Inconsistencia terminológica**
 - Puede traducir mismo término diferente
 - Solución: Glosario + verificación MD-004

4. **Formato incorrecto**
 - Sintaxis RST puede tener errores sutiles
 - Solución: Compilar y verificar

----

Plantillas de Prompts
=====================

Plantilla Base
--------------

.. code-block:: text

 # PROMPT: [Nombre descriptivo]

 ## CONTEXTO
 Eres traductor técnico experto usando metodología ADT.

 ## METODOLOGÍA ADT
 [Incluir reglas relevantes: PASO 0, MD-002, MD-004]

 ## TAREA
 Traducir [tipo de documento] de [idioma origen] a [idioma destino]

 ## INPUT
 [Documento original]

 ## OUTPUT ESPERADO
 - Formato: [RST/LaTeX/Markdown]
 - Enriquecimiento: [según MD-002]
 - Estructura: [especificar]

 ## VERIFICACIÓN
 Antes de entregar, verifica:
 [Checklist específico]

 ## RESTRICCIONES
 [Cualquier limitación específica]

Plantilla para Tips Breves
---------------------------

.. code-block:: text

 # PROMPT: Traducir Tip Breve ADT

 ## CONTEXTO
 Traduces un tip breve (< 20 líneas) de documentación arc42.

 ## REGLAS
 1. PASO 0: Cuenta líneas exactas
 2. MD-002: Enriquece +300% a +1000%
 3. MD-004: Conserva términos técnicos

 ## ENRIQUECIMIENTO REQUERIDO
 - 2-3 ejemplos prácticos
 - Tabla comparativa
 - Checklist de aplicación
 - Casos de uso

 ## OUTPUT
 Formato RST con:
 - Título apropiado
 - Contenido traducido
 - Ejemplos agregados
 - Referencias si aplican

 ## VERIFICACIÓN
 [ ] Contenido original 100% presente
 [ ] Enriquecimiento ≥ +300%
 [ ] Compilación RST válida
 [ ] Terminología consistente

----

Próximos Desarrollos
====================

En Progreso
-----------

.. code-block:: text

 [RUNNING] Prompt Maestro Completo
 - Incluye toda metodología ADT
 - Optimizado para Claude/ChatGPT

 [RUNNING] Biblioteca de Ejemplos
 - Prompts exitosos documentados
 - Casos de uso específicos

Planeado
--------

.. code-block:: text

 [LIST] Prompts por tipo de documento
 - Manual usuario
 - Documentación API
 - Tutorial técnico

 [LIST] Prompts de verificación
 - Completitud
 - Terminología
 - Formato

 [LIST] Prompts de corrección
 - Fix de errores comunes
 - Mejora de enriquecimiento

----

Contribuir Prompts
==================

Si desarrollas prompts efectivos:

.. code-block:: text

 1. Documenta el prompt completo
 2. Incluye casos de uso
 3. Especifica limitaciones
 4. Comparte resultados
 5. Sugiere mejoras

**Formato de contribución:**

.. code-block:: text

 # Nombre: [prompt_tipo_documento]

 Descripción: [qué hace]

 Modelo probado: [Claude/ChatGPT/otro]

 Efectividad: [%]

 Prompt completo:
 [texto del prompt]

 Ejemplo de uso:
 [caso real]

 Limitaciones conocidas:
 [qué no funciona bien]

----

.. seealso::
 * :doc:`../07_guias_uso/tutorial_completo` - Tutorial ADT
 * :doc:`../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer` - Reglas de enriquecimiento
 * :doc:`../03_estandares/calidad/criterios_calidad` - Criterios de calidad

.. warning::
 Recordatorio: Los LLMs son herramientas de **asistencia**, no remplazan el criterio humano ni la verificación sistemática ADT.

----

.. toctree::
 :maxdepth: 2
 :caption: Subsecciones
 :hidden:

 prompts_condicionales/index
 plantillas/index
