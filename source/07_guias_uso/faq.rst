.. _faq:

===============================================
Preguntas Frecuentes (FAQ)
===============================================

Respuestas a las preguntas más comunes sobre el sistema ADT.

.. contents:: Contenido
 :depth: 2
 :local:

----

Preguntas Generales
===================

¿Qué es ADT?
------------

**Respuesta:**

ADT (Arquitectura de Documentación Técnica) es un **sistema completo** para traducción de documentación técnica con garantía de calidad.

**Incluye:**
- Estándares de calidad claros
- Reglas de decisión objetivas
- Casos prácticos reales
- Sistema de capacitación
- Herramientas de referencia

**Basado en:** 196 archivos reales traducidos (arc42)

¿Para quién es ADT?
-------------------

**Respuesta:**

ADT es para:

[OK] **Traductores técnicos** que buscan calidad consistente
[OK] **Equipos de documentación** que necesitan estándares
[OK] **Empresas** que requieren traducciones profesionales
[OK] **Proyectos open source** con documentación multilingüe
[OK] **Estudiantes** aprendiendo traducción técnica

¿Cuánto tiempo toma aprender ADT?
----------------------------------

**Respuesta:**

Depende del nivel que busques:

.. list-table::
 :header-rows: 1
 :widths: 30 20 50

 * - **Nivel**
   - **Tiempo**
   - **Resultado**
 * - Básico
   - 15 min
   - Primera traducción simple
 * - Intermedio
   - 2-3 horas
   - Dominio de fundamentos
 * - Avanzado
   - 6-8 horas
   - Experto completo

**Recomendado:** Invertir 3 horas (guía + tutorial)

¿ADT funciona para cualquier idioma?
-------------------------------------

**Respuesta:**

**Sí**, los principios son universales:

[OK] **Fundamentos:** Aplican a cualquier par de idiomas
[OK] **Workflow:** Independiente del idioma
[OK] **Reglas:** Adaptables a cualquier contexto

**Nota:** Los ejemplos actuales son Inglés->Español, pero la metodología es aplicable a cualquier dirección.

----

Preguntas sobre Inicio
======================

¿Por dónde empiezo?
-------------------

**Respuesta:**

**Ruta recomendada:**

.. code-block:: text

 1. Lee guia_rapida.rst (15 min)
 -> Entiendes el sistema básico

 2. Haz el ejercicio práctico incluido
 -> Primera traducción

 3. Lee tutorial_completo.rst (2-3h)
 -> Dominas fundamentos

 4. Estudia un caso práctico (1h)
 -> Ves aplicación real

 5. Aplica a documento real
 -> ¡Listo para producción!

**Total:** 4-5 horas hasta estar productivo

¿Necesito experiencia previa?
------------------------------

**Respuesta:**

**No necesitas:**
- [ERROR] Experiencia en traducción profesional
- [ERROR] Conocimiento de Sphinx/RST
- [ERROR] Programación

**Sí necesitas:**
- [OK] Dominio de ambos idiomas (origen y destino)
- [OK] Conocimiento del dominio técnico
- [OK] Disposición para seguir proceso sistemático

**El sistema te enseña todo lo demás.**

¿Qué herramientas necesito?
----------------------------

**Respuesta:**

**Mínimo indispensable:**
- Editor de texto (VS Code, Sublime, etc.)
- Python 3.7+ (para Sphinx)
- Sphinx instalado

**Recomendado:**
- Git (para control de versiones)
- Pandoc (para conversiones)
- Navegador web (para ver HTML)

**Instalación básica:**

.. code-block:: bash

 pip install sphinx
 # Ya estás listo

----

Preguntas sobre Workflow
=========================

¿Cuánto tiempo toma traducir un documento?
-------------------------------------------

**Respuesta:**

**Basado en datos reales de 196 archivos:**

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Tipo**
   - **Original**
   - **Tiempo**
   - **Velocidad**
 * - Tip breve
   - < 20 líneas
   - 1-2 horas
   - Lento (alto enriq.)
 * - Sección corta
   - 20-50 líneas
   - 30-60 min
   - Media
 * - Sección mediana
   - 50-100 líneas
   - 1-1.5 horas
   - Media-Alta
 * - Sección extensa
   - > 100 líneas
   - 2-3 horas
   - Alta

**Promedio:** 3.3 archivos/hora
**Tu velocidad mejorará con práctica:** 2x-3x después de 10-20 archivos

¿Qué es PASO 0 y por qué es tan importante?
--------------------------------------------

**Respuesta:**

**PASO 0** es la fase de **pre-traducción** donde lees TODO el documento antes de empezar a traducir.

**Por qué es crítico:**

.. code-block:: text

 Caso real: Sección 07 de arc42

 SIN PASO 0:
 - Solo leyó 50 de 126 líneas
 - Resultado: 6 secciones omitidas
 - Costo: 2 horas de re-trabajo

 CON PASO 0:
 - Leyó 126 de 126 líneas
 - Resultado: 0 omisiones
 - Costo: 0 re-trabajo

 15 minutos de PASO 0 = Ahorro de 2 horas

**Conclusión:** PASO 0 no es opcional, es **crítico**.

¿Cuánto debo enriquecer el contenido?
--------------------------------------

**Respuesta:**

**Usa la matriz MD-002:**

.. code-block:: text

 < 20 líneas -> +300% a +1000%
 20-50 líneas -> +100% a +300%
 50-100 líneas -> +80% a +150%
 > 100 líneas -> +50% a +100%

**Ejemplo práctico:**

.. code-block:: text

 Original: 15 líneas (tip breve)
 Objetivo: +300% a +1000%
 Traducido esperado: 45 a 150 líneas

 Agregar:
 - 2-3 ejemplos prácticos
 - Tabla comparativa
 - Checklist
 - Casos de uso

**Ver completo:** :doc:`../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer`

¿Qué términos debo traducir y cuáles conservar?
------------------------------------------------

**Respuesta:**

**Usa la matriz MD-004:**

**SIEMPRE CONSERVAR:**
- Acrónimos: API, REST, JSON, UML
- Patrones: Singleton, Factory, Observer
- Metodologías: Scrum, ATAM, Kanban
- Roles: Product Owner, Stakeholder

**SIEMPRE TRADUCIR:**
- Conceptos: Quality -> Calidad
- Verbos: Implement -> Implementar
- Adjetivos: Complex -> Complejo

**Ver completo:** :doc:`../04_reglas_operativas/matrices_decision/MD_004_traducir_vs_conservar`

----

Preguntas sobre Calidad
========================

¿Cómo sé si mi traducción es de calidad?
-----------------------------------------

**Respuesta:**

**Evalúa contra los 5 criterios:**

.. code-block:: text

 1. Completitud: 100% contenido presente
 [ ] Todos los párrafos
 [ ] Todas las listas
 [ ] Todas las tablas
 [ ] Todas las referencias

 2. Precisión: Terminología correcta
 [ ] Términos técnicos precisos
 [ ] Consistencia 100%

 3. Enriquecimiento: Apropiado según tamaño
 [ ] En rango MD-002

 4. Compilación: Exitosa
 [ ] make html sin errores

 5. Verificación: Sistemática
 [ ] Checklist completo

**Umbral de aprobación:** ≥95%

**Ver completo:** :doc:`../03_estandares/calidad/criterios_calidad`

¿Qué hago si omití contenido?
------------------------------

**Respuesta:**

**Proceso de corrección:**

.. code-block:: text

 1. PASO 0 retrospectivo:
 [ ] Leer archivo completo ahora
 [ ] Identificar TODO el contenido
 [ ] Crear checklist exhaustivo

 2. Comparar con traducción actual:
 [ ] Marcar qué falta
 [ ] Priorizar omisiones

 3. Agregar contenido faltante:
 [ ] Insertar en posición correcta
 [ ] Mantener coherencia

 4. Verificar completitud:
 [ ] Checklist 100%
 [ ] Compilar y verificar

**Prevención futura:** NUNCA saltarse PASO 0

**Ver caso real:** :doc:`../06_casos_practicos/errores_comunes/error_01_omisiones`

¿Puedo usar traductores automáticos?
-------------------------------------

**Respuesta:**

**Sí, PERO con precauciones:**

.. code-block:: text

 [OK] USAR para:
 - Borrador inicial rápido
 - Terminología técnica
 - Estructuras repetitivas

 [WARNING] SIEMPRE revisar:
 - Precisión técnica
 - Contexto adecuado
 - Fluidez natural

 [ERROR] NUNCA confiar ciegamente
 - Errores técnicos frecuentes
 - Contexto mal interpretado
 - Frases poco naturales

**Regla de oro:** Traductor automático = Asistente, NO reemplazo

----

Preguntas sobre Herramientas
=============================

¿Cómo convierto LaTeX a RST?
-----------------------------

**Respuesta:**

**Opción 1: Manual (recomendado para calidad)**

Usa la tabla de equivalencias:

.. code-block:: text

 \textbf{texto} -> **texto**
 \section{Título} -> Título con ===
 \begin{itemize} -> Lista con -

**Ver completo:** :doc:`../05_herramientas_medios/equivalencias/latex_rst_equivalencias`

**Opción 2: Automática (punto de partida)**

.. code-block:: bash

 pandoc input.tex -f latex -t rst -o output.rst

**[WARNING] Requiere revisión manual completa**

¿Qué editor recomiendas para RST?
----------------------------------

**Respuesta:**

**Top 3:**

1. **VS Code** (recomendado)
 - Extensión: reStructuredText
 - Preview en vivo
 - Gratis y potente

2. **Sublime Text**
 - Rápido y ligero
 - Paquete: Restructured​Text

3. **PyCharm**
 - Soporte RST nativo
 - Ideal si ya lo usas

**Mínimo:** Cualquier editor de texto plano

¿Cómo compilo la documentación?
--------------------------------

**Respuesta:**

**Proceso básico:**

.. code-block:: bash

 # Instalar Sphinx
 pip install sphinx

 # Compilar
 cd tu_proyecto
 make html

 # Ver resultado
 firefox build/html/index.html

**Si hay errores:**

.. code-block:: bash

 # Ver errores completos
 make html 2>&1 | less

 # Limpiar y recompilar
 make clean && make html

----

Preguntas sobre Casos Específicos
==================================

¿Cómo traduzco código fuente?
------------------------------

**Respuesta:**

**Regla fundamental:** Código NO se traduce, comentarios SÍ

.. code-block:: python

 # ORIGINAL (inglés)
 def calculate_total(items):
 """Calculate the total price of items"""
 return sum(item.price for item in items)

.. code-block:: python

 # TRADUCIDO (español)
 def calculate_total(items):
 """Calcula el precio total de los items"""
 return sum(item.price for item in items)

**Qué traducir:**
- [OK] Comentarios
- [OK] Docstrings
- [OK] Mensajes de error
- [OK] Strings de UI

**Qué NO traducir:**
- [ERROR] Nombres de variables
- [ERROR] Nombres de funciones
- [ERROR] Palabras clave del lenguaje
- [ERROR] Imports

¿Cómo manejo las imágenes?
---------------------------

**Respuesta:**

**Opción 1: Conservar imágenes originales**

.. code-block:: rst

 .. figure:: imagen_original.png
 :alt: Descripción traducida

 Caption traducido

**Opción 2: Traducir imágenes (si necesario)**

.. code-block:: text

 1. Editar imagen (Photoshop, GIMP, etc.)
 2. Traducir texto dentro de imagen
 3. Guardar como imagen_es.png
 4. Referenciar nueva imagen

**Recomendación:** Conservar originales si el texto no es crítico

¿Cómo traduzco diagramas?
--------------------------

**Respuesta:**

**Para diagramas editables (PlantUML, Mermaid, etc.):**

.. code-block:: text

 1. Modificar código fuente del diagrama
 2. Traducir textos/labels
 3. Regenerar diagrama
 4. Incluir en documentación

**Para diagramas de imagen:**

.. code-block:: text

 1. Traducir caption/descripción
 2. Opcionalmente: Recrear diagrama con textos traducidos
 3. Incluir nueva versión

**Nota:** Diagramas claros trascienden idiomas

----

Preguntas sobre Proyectos Reales
=================================

¿Puedo usar ADT en proyectos comerciales?
------------------------------------------

**Respuesta:**

**Sí, completamente.** ADT es para uso libre en cualquier contexto:

[OK] Proyectos comerciales
[OK] Proyectos open source
[OK] Uso personal
[OK] Uso educativo
[OK] Uso en empresas

**No hay restricciones de licencia para el uso del método.**

¿Cómo empiezo un proyecto grande?
----------------------------------

**Respuesta:**

**Proceso recomendado:**

.. code-block:: text

 Fase 1: Preparación (1 día)
 [ ] PASO 0 global del proyecto
 [ ] Inventario completo de archivos
 [ ] Estimación de tiempo
 [ ] Planificación de lotes

 Fase 2: Traducción por lotes (variable)
 [ ] 5-10 archivos por lote
 [ ] Checkpoint después de cada lote
 [ ] Verificación sistemática

 Fase 3: Integración (1-2 días)
 [ ] Compilación global
 [ ] Verificación de referencias
 [ ] Ajustes finales

 Fase 4: QA (1 día)
 [ ] Revisión completa
 [ ] Checklist global
 [ ] Entrega final

**Ver ejemplo:** :doc:`../06_casos_practicos/antes_despues/caso_01_seccion_breve`

¿Puedo trabajar en equipo?
---------------------------

**Respuesta:**

**Sí, ADT es ideal para equipos:**

**Preparación:**

.. code-block:: text

 1. Todos leen guia_rapida (15 min)
 2. Todos leen tutorial_completo (2-3h)
 3. Sesión de alineación (1h)
 4. Crear glosario compartido

**Durante proyecto:**

.. code-block:: text

 1. Asignar archivos por persona
 2. Aplicar MD-002 y MD-004 consistentemente
 3. Checkpoints compartidos
 4. Revisión cruzada entre miembros
 5. Glosario actualizado continuamente

**Resultado:** Calidad consistente entre traductores

----

Preguntas sobre Problemas Comunes
==================================

Mi traducción es muy larga, ¿está bien?
----------------------------------------

**Respuesta:**

**Depende del tamaño original:**

.. code-block:: text

 Verifica contra MD-002:

 Original < 20 líneas:
 [OK] +300% a +1000% es CORRECTO
 [ERROR] Solo +50% es POCO

 Original 20-50 líneas:
 [OK] +100% a +300% es CORRECTO
 [ERROR] +500% es EXCESIVO

 Original > 100 líneas:
 [OK] +50% a +100% es CORRECTO
 [ERROR] +300% es EXCESIVO

**Si estás fuera de rango:** Revisa qué agregaste y ajusta

La compilación da muchos warnings, ¿es grave?
----------------------------------------------

**Respuesta:**

**NO si son warnings esperados:**

.. code-block:: text

 [OK] WARNINGS NORMALES:
 - Lexers desconocidos (plantuml, etc.)
 - Referencias a documentos futuros
 - Imágenes no encontradas (placeholders)

 [ERROR] ERRORES CRÍTICOS:
 - Title underline too short
 - Unexpected indentation
 - Unknown directive

**Regla:** 0 errores críticos = [OK] OK

**Ver:** :doc:`troubleshooting` para soluciones

¿Cómo manejo referencias rotas?
--------------------------------

**Respuesta:**

**Causas comunes:**

.. code-block:: rst

 # INCORRECTO
 :ref:`seccion-5`

 # Label no existe o tiene nombre diferente

**Solución:**

.. code-block:: text

 1. Buscar label en archivo destino:
 grep "_seccion" archivo.rst

 2. Usar nombre exacto:
 :ref:`seccion_5` (con underscore)

 3. Crear label si falta:
 .. _seccion_5:

**Prevención:** Mantener lista de labels durante traducción

----

Preguntas sobre Mejora Continua
================================

¿Cómo mejoro mi velocidad?
---------------------------

**Respuesta:**

**Velocidad natural con práctica:**

.. code-block:: text

 Archivos 1-10: 2.5 arch/hora (aprendizaje)
 Archivos 11-30: 3.5 arch/hora (competencia)
 Archivos 30+: 4.5 arch/hora (experto)

**Técnicas para acelerar:**

.. code-block:: text

 [OK] Plantillas reutilizables
 [OK] Snippets de editor
 [OK] Glosario exhaustivo
 [OK] Scripts de verificación
 [OK] Atajos de teclado

**[WARNING] NO sacrifiques calidad por velocidad**

¿Cómo contribuyo al proyecto ADT?
----------------------------------

**Respuesta:**

**Formas de contribuir:**

.. code-block:: text

 1. Documentar tus casos de uso
 2. Reportar errores encontrados
 3. Sugerir mejoras
 4. Compartir nuevas matrices de decisión
 5. Traducir ADT a otros idiomas
 6. Crear nuevas tablas de equivalencias

**El proyecto ADT crece con la comunidad.**

----

¿No encuentras tu pregunta?
============================

**Recursos adicionales:**

- :doc:`troubleshooting` - Solución de problemas
- :doc:`tutorial_completo` - Tutorial detallado
- :doc:`../06_casos_practicos/index` - Casos reales

**¿Aún tienes dudas?**

Consulta la documentación completa en :doc:`../index`

----

.. seealso::
 * :doc:`troubleshooting` - Solución de problemas
 * :doc:`guia_rapida` - Inicio rápido
 * :doc:`tutorial_completo` - Tutorial completo
 * :doc:`../06_casos_practicos/errores_comunes/index` - Errores comunes

.. note::
 Este FAQ se actualiza continuamente con nuevas preguntas de usuarios reales.
