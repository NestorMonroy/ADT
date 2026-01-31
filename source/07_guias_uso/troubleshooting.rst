.. _troubleshooting:




Solución de Problemas (Troubleshooting)
=======================================

Soluciones a los problemas más comunes al usar ADT.

.. contents:: Contenido
 :depth: 3
 :local:




Problemas de Compilación
========================

Error: "Title underline too short"
==================================

**Problema:**

.. code-block:: text

 ERROR: Title underline too short

 /path/to/file.rst:12:
 WARNING: Title underline too short.

**Causa:**

El subrayado del título es más corto que el texto.

**Ejemplo incorrecto:**

.. code-block:: rst




 Título Muy Largo Que No Calza
==============================

**Solución:**

.. code-block:: rst




 Título Muy Largo Que No Calza
==============================

**Regla:** El subrayado debe tener **exactamente** la misma longitud o más que el título.

**Tip rápido:**

.. code-block:: python

 # Script para generar subrayado correcto
 titulo = "Mi Título Aquí"
 print("=" * len(titulo))
 print(titulo)
 print("=" * len(titulo))

Error: "Unexpected indentation"
===============================

**Problema:**

.. code-block:: text

 ERROR: Unexpected indentation
 /path/to/file.rst:25

**Causa más común:** Listas anidadas mal indentadas

**Ejemplo incorrecto:**

.. code-block:: rst

 - Item nivel 1
 - SubItem nivel 2 # [ERROR] Falta línea vacía

**Solución:**

.. code-block:: rst

 - Item nivel 1

 - SubItem nivel 2 # [OK] Línea vacía + indentación

**Regla:** Entre niveles de lista siempre incluir **línea vacía** + **2 espacios de indentación**.

Error: "Unknown directive type"
===============================

**Problema:**

.. code-block:: text

 WARNING: Unknown directive type "note"

**Causa:** Directiva mal escrita o espacios incorrectos

**Ejemplo incorrecto:**

.. code-block:: rst

 ..note:: # [ERROR] Falta espacio
 Contenido

**Solución:**

.. code-block:: rst

 .. note:: # [OK] Espacio después de ..
 Contenido

Error: "Pygments lexer not known"
=================================

**Problema:**

.. code-block:: text

 WARNING: Pygments lexer name 'plantuml' is not known

**Causa:** Lenguaje de código no soportado por Pygments

**Solución 1 - Usar lenguaje genérico:**

.. code-block:: rst

   .. code-block:: text # En lugar de plantuml

   @startuml
   ==========
   @enduml

**Solución 2 - Ignorar warning:**

Este warning no es crítico. El código se mostrará sin syntax highlighting.

**Solución 3 - Instalar extensión:**

.. code-block:: bash

 pip install sphinxcontrib-plantuml

Error: "undefined label"
========================

**Problema:**

.. code-block:: text

 WARNING: undefined label: 'seccion_5'

**Causa:** La referencia apunta a un label que no existe

**Solución 1 - Verificar que label existe:**

.. code-block:: bash

 grep "_seccion_5" *.rst

**Solución 2 - Crear el label:**

.. code-block:: rst

 .. _seccion_5:

 Sección 5
==========

**Solución 3 - Corregir nombre:**

.. code-block:: rst

 # Si label es "seccion_05" con cero
 :ref:`seccion_05` # No seccion_5




Problemas de Contenido
======================

He omitido contenido, ¿cómo lo recupero?
========================================

**Síntomas:**

.. code-block:: text

 - Compilación exitosa
 - Pero faltan secciones del original
 - Documento incompleto

**Causa raíz:** NO aplicar PASO 0 correctamente

**Solución paso a paso:**

.. code-block:: text

 1. PASO 0 Retrospectivo:
   [ ] Abrir archivo original
   [ ] Leer COMPLETO (línea 1 a N)
   [ ] Crear checklist de TODO el contenido

 2. Comparar contra traducción actual:
   [ ] Marcar qué está presente
   [ ] Identificar qué falta
   [ ] Listar omisiones

 3. Agregar contenido faltante:
   [ ] En posición correcta del documento
   [ ] Mantener coherencia
   [ ] Aplicar mismo nivel de enriquecimiento

 4. Verificar completitud:
   [ ] Checklist 100% completo
   [ ] Recompilar
   [ ] Revisar HTML

**Ver caso completo:** :doc:`../06_casos_practicos/errores_comunes/error_01_omisiones`

Mi traducción es muy corta/larga
================================

**Problema:** Enriquecimiento fuera de rango

**Diagnóstico:**

.. code-block:: text

 Original: X líneas
 Traducido: Y líneas
 Enriquecimiento = ((Y - X) / X) × 100

 ¿Está en rango apropiado según MD-002?

**Si es muy corto:**

.. code-block:: text

 Original: 15 líneas (< 20)
 Traducido: 20 líneas (+33%)
 Esperado: +300% a +1000%

 Problema: Enriquecimiento insuficiente [ERROR]

 Solución:
 [ ] Agregar 2-3 ejemplos prácticos
 [ ] Agregar tabla comparativa
 [ ] Agregar checklist
 [ ] Agregar casos de uso

**Si es muy largo:**

.. code-block:: text

 Original: 120 líneas (> 100)
 Traducido: 500 líneas (+317%)
 Esperado: +50% a +100%

 Problema: Enriquecimiento excesivo [ERROR]

 Solución:
 [ ] Eliminar divagaciones
 [ ] Eliminar contenido no relacionado
 [ ] Condensar ejemplos redundantes

**Ver completo:** :doc:`../04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer`

Terminología inconsistente
==========================

**Problema:** Mismo término traducido de formas diferentes

**Ejemplo:**

.. code-block:: text

 Archivo 1: "Stakeholder" -> Stakeholder
 Archivo 2: "Stakeholder" -> Parte interesada
 Archivo 3: "Stakeholder" -> Interesado

 Resultado: Inconsistencia [ERROR]

**Solución:**

.. code-block:: text

 1. Crear glosario del proyecto:
   | Término | Decisión | Razón |
   |---------|----------|-------|
   | Stakeholder | Stakeholder | Rol establecido |

 2. Buscar todas las instancias:
   grep -r "Stakeholder\|Parte interesada" *.rst

 3. Unificar todas a decisión del glosario:
   sed -i 's/Parte interesada/Stakeholder/g' *.rst

 4. Verificar consistencia:
   grep -r "Stakeholder" *.rst | wc -l

**Prevención:** Usar MD-004 desde el inicio




Problemas de Formato
====================

Tablas no se ven correctamente
==============================

**Problema:** Tabla mal formada o alineación incorrecta

**Solución - Usar list-table:**

.. code-block:: rst

 .. list-table::
 :header-rows: 1
 :widths: 30 30 40

 * - Columna 1
   - Columna 2
   - Columna 3
 * - Dato A
   - Dato B
   - Dato C

**Ventajas de list-table:**
- Más fácil de escribir
- Más fácil de mantener
- Menos errores de formato

Código no tiene syntax highlighting
===================================

**Problema:** Bloque de código sin colores

**Causa:** Falta directiva code-block

**Incorrecto:**

.. code-block:: rst

 ::

 def funcion():
 return True

**Correcto:**

.. code-block:: rst

 .. code-block:: python

 def funcion():
 return True

**Lenguajes comunes:**

.. code-block:: text

 python, java, javascript, bash, sql, xml, json,
 yaml, rst, latex, html, css, cpp, c, rust, go

Imágenes no se muestran
=======================

**Problema:** Imagen no aparece en HTML

**Causas posibles:**

1. **Ruta incorrecta:**

.. code-block:: rst

 # [ERROR] Ruta absoluta
 .. image:: /home/user/imagen.png

 # [OK] Ruta relativa
 .. image:: ../images/imagen.png

2. **Imagen no existe:**

.. code-block:: bash

 # Verificar
 ls -la source/images/imagen.png

3. **Falta directiva:**

.. code-block:: rst

 # [ERROR] Solo texto
 imagen.png

 # [OK] Directiva image
 .. image:: imagen.png




Problemas de Workflow
=====================

¿Por dónde empiezo un proyecto grande?
======================================

**Solución - Proceso sistemático:**

.. code-block:: text

 Fase 1: Análisis (1 día)
=========================

 1. PASO 0 Global:
   [ ] Listar TODOS los archivos
   [ ] Contar total de páginas/líneas
   [ ] Identificar archivos complejos

 2. Planificación:
   [ ] Dividir en lotes de 5-10 archivos
   [ ] Estimar tiempo por lote
   [ ] Crear calendario

 3. Preparación:
   [ ] Configurar proyecto Sphinx
   [ ] Crear glosario inicial
   [ ] Preparar herramientas

 Fase 2: Ejecución (variable)
=============================

 Por cada lote:
 [ ] PASO 0 del lote
 [ ] Traducir aplicando MD-002, MD-004
 [ ] Verificar con checklist
 [ ] Crear checkpoint
 [ ] Commit a Git

 Fase 3: Integración (1-2 días)
===============================

 [ ] Compilación global
 [ ] Verificar referencias cruzadas
 [ ] Ajustar índices
 [ ] QA completo

Tardé mucho en un archivo, ¿es normal?
======================================

**Respuesta:** Depende del tipo

**Velocidades normales:**

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Tipo**
   - **Original**
   - **Tiempo**
   - **Normal?**
 * - Tip breve
   - < 20 líneas
   - 1-2 horas
   - [OK] Sí
 * - Sección corta
   - 20-50
   - 30-60 min
   - [OK] Sí
 * - Sección mediana
   - 50-100
   - 1-1.5 horas
   - [OK] Sí
 * - Sección extensa
   - > 100
   - 2-3 horas
   - [OK] Sí

**Si tardas más:** Identificar causa

.. code-block:: text

 Causas comunes de lentitud:

 [ERROR] No aplicar PASO 0 -> Omisiones -> Re-trabajo
 [ERROR] No usar MD-002 -> Indecisión sobre enriquecimiento
 [ERROR] No usar MD-004 -> Dudar en cada término
 [ERROR] Perfeccionismo excesivo -> Ciclos infinitos

 [OK] Solución: Seguir proceso sistemáticamente

Mi equipo tiene velocidades diferentes
======================================

**Normal y esperado**

**Factores que afectan velocidad:**

.. code-block:: text

 [OK] Experiencia en traducción
 [OK] Conocimiento del dominio
 [OK] Familiaridad con herramientas
 [OK] Complejidad de archivos asignados

**Solución - Asignación inteligente:**

.. code-block:: text

 Traductor Experto:
 -> Archivos complejos (secciones extensas)
 -> Tips que requieren mucho enriquecimiento
 -> Velocidad esperada: 4-5 arch/hora

 Traductor Intermedio:
 -> Secciones medianas
 -> Tips estándar
 -> Velocidad esperada: 3-4 arch/hora

 Traductor Junior:
 -> Secciones simples con supervisión
 -> Ejemplos directos
 -> Velocidad esperada: 2-3 arch/hora




Problemas de Herramientas
=========================

Pandoc genera salida incorrecta
===============================

**Problema:** Conversión LaTeX->RST con errores

**Solución - Post-procesamiento manual:**

.. code-block:: bash

 # 1. Convertir
 pandoc input.tex -f latex -t rst -o output.rst

 # 2. Revisar SIEMPRE:
 # - Títulos (longitud de subrayado)
 # - Listas (indentación)
 # - Tablas (estructura)
 # - Código (directivas)

**Regla de oro:** Pandoc = 70% del trabajo, 30% manual

Sphinx no encuentra archivos
============================

**Problema:**

.. code-block:: text

 WARNING: document isn't included in any toctree

**Causa:** Archivo no incluido en ningún toctree

**Solución:**

.. code-block:: rst

 # En archivo padre (index.rst)

 .. toctree::
 :maxdepth: 2

 archivo_huérfano

Git merge conflicts en RST
==========================

**Problema:** Conflictos al mergear ramas

**Solución:**

.. code-block:: bash

 # 1. Identificar conflictos
 git status

 # 2. Abrir archivo con conflicto
 # Buscar marcadores:
 # <<<<<<< HEAD
 # ...
 # =======
 # ...
 # >>>>>>> branch

 # 3. Resolver manualmente
 # Mantener sintaxis RST válida

 # 4. Compilar para verificar
 make html

 # 5. Si compila OK, commit
 git add archivo.rst
 git commit -m "Resolve merge conflict"




Problemas de Calidad
====================

¿Cómo sé si mi calidad es suficiente?
=====================================

**Evaluar contra criterios:**

.. code-block:: text

 Checklist de calidad:

 1. Completitud:
   [ ] 100% contenido original presente
   Score: ____%

 2. Precisión:
   [ ] Terminología correcta y consistente
   Score: ____%

 3. Enriquecimiento:
   [ ] En rango apropiado según MD-002
   Score: ____%

 4. Compilación:
   [ ] make html exitoso (0 errores críticos)
   Score: ____%

 5. Verificación:
   [ ] Checklist completo aplicado
   Score: ____%

 TOTAL: Promedio de los 5 criterios

 [OK] ≥ 95% = Calidad aprobada
 [WARNING] 85-94% = Revisar y mejorar
 [ERROR] < 85% = No aprobar, re-hacer

La revisión indica muchos problemas
===================================

**Normal en primeras traducciones**

**Proceso de mejora:**

.. code-block:: text

 Iteración 1:
 - Primera traducción
 - Problemas encontrados: Muchos
 - Aprendizaje: Alto

 Iteración 2:
 - Aplicar correcciones
 - Problemas: Menos
 - Aprendizaje: Continúa

 Iteración 3+:
 - Calidad mejora consistentemente
 - Problemas: Pocos
 - Dominio del sistema

**Curva de aprendizaje típica:**

.. code-block:: text

 Archivos 1-5: Muchos errores (aprendizaje)
 Archivos 6-15: Errores moderados (mejora)
 Archivos 16+: Pocos errores (dominio)




Solución Rápida (Quick Fix)
===========================

Tabla de Referencia
===================

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Problema**
   - **Solución Rápida**
 * - Title underline too short
   - Igualar longitud de === con título
 * - Unexpected indentation
   - Línea vacía + 2 espacios en listas anidadas
 * - Unknown directive
   - Espacio después de .. en directivas
 * - Undefined label
   - Verificar que label existe con grep
 * - Imagen no aparece
   - Usar ruta relativa, verificar archivo existe
 * - Tabla mal formada
   - Usar list-table en lugar de tabla ASCII
 * - Código sin colores
   - Agregar .. code-block:: lenguaje
 * - Terminología inconsistente
   - Crear y usar glosario del proyecto
 * - Enriquecimiento incorrecto
   - Consultar MD-002 para rango apropiado
 * - Omisiones
   - Aplicar PASO 0 completo retrospectivamente

Comandos Útiles
===============

.. code-block:: bash

 # Compilar y ver errores
 make html 2>&1 | less

 # Limpiar y recompilar
 make clean && make html

 # Buscar término en todos los archivos
 grep -r "término" source/

 # Contar archivos RST
 find source -name "*.rst" | wc -l

 # Verificar referencias rotas
 make linkcheck

 # Ver warnings específicos
 make html 2>&1 | grep "WARNING"




Cuando Todo Falla
=================

Reiniciar Proyecto Limpio
=========================

**Último recurso:**

.. code-block:: bash

 # 1. Backup completo
 cp -r proyecto proyecto_backup

 # 2. Limpiar builds
 make clean
 rm -rf build/

 # 3. Verificar configuración
 cat source/conf.py

 # 4. Rebuild desde cero
 make html

 # 5. Si falla, comparar con backup
 diff -r proyecto proyecto_backup

Pedir Ayuda
===========

**Información a proveer:**

.. code-block:: text

 Al pedir ayuda, incluir:

 [OK] Mensaje de error completo
 [OK] Comando ejecutado
 [OK] Versión de Sphinx
 [OK] Sistema operativo
 [OK] Fragmento de código problemático
 [OK] Qué has intentado ya

 NO incluir:
 [ERROR] Solo "no funciona"
 [ERROR] Screenshots de texto (copiar texto)
 [ERROR] Proyecto completo (solo archivo problemático)




.. seealso::
 
 * :doc:`faq` - Preguntas frecuentes
 * :doc:`../03_estandares/calidad/checklist_revision` - Checklists de verificación
 * :doc:`../06_casos_practicos/errores_comunes/index` - Errores comunes documentados

.. note::
 Este troubleshooting se actualiza con problemas reales encontrados por usuarios. Si encuentras un problema no listado aquí, documéntalo para ayudar a otros.
