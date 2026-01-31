
Reglas de Estructura del Proyecto ADT
=====================================

:Autor: Sistema de Documentación
:Fecha: 2026-01-27
:Versión: 1.0
:Estado: NORMATIVO - CUMPLIMIENTO OBLIGATORIO

.. important::
 Este documento define las reglas **OBLIGATORIAS** de organización del proyecto ADT.
 Todo cambio estructural debe seguir estas directrices.

Regla Fundamental de Ubicación
==============================

**REGLA MAESTRA:**

.. note::
 
 **Solo va a** ``source/`` **el contenido que se documenta/compila en HTML.**

 **Las herramientas y scripts de proyecto quedan en la raíz.**

Esta regla es la base de toda la organización del proyecto y debe ser **SIEMPRE** respetada.

Estructura Obligatoria
======================

Raíz del Proyecto (``/tmp/ADT/``)
=================================

**QUÉ VA EN LA RAÍZ:**

.. code-block:: text

 /tmp/ADT/
 +-- Makefile [OK] Herramienta de compilación
 +-- make.bat [OK] Batch de compilación (Windows)
 +-- build/ [OK] Salida compilada (HTML)
 +-- source/ [OK] TODO EL CONTENIDO DOCUMENTAL
 +-- config/ [OK] Configuraciones del proyecto
 +-- scripts/ [OK] Scripts de automatización
 +-- tools/ [OK] Herramientas externas

**CRITERIO:** Archivos y carpetas que son **herramientas** o **utilidades** del proyecto,
NO contenido a documentar.

Carpeta source/ (``/tmp/ADT/source/``)
======================================

**QUÉ VA EN source/:**

.. code-block:: text

 /tmp/ADT/source/
 +-- conf.py [OK] Configuración Sphinx
 +-- index.rst [OK] Índice principal
 +-- _static/ [OK] Recursos estáticos
 +-- _templates/ [OK] Templates Sphinx
 |
 +-- 01_fundamentos/ [OK] Contenido documental
 +-- 02_procedimientos/ [OK] Contenido documental
 +-- ... [OK] Contenido documental
 +-- 10_apendices/ [OK] Contenido documental
 |
 +-- biblioteca/ [OK] Contenido documental
 +-- diataxis/ [OK] Contenido documental
 +-- docs/ [OK] Contenido documental
 +-- docs_maestros/ [OK] Contenido documental

**CRITERIO:** Todo lo que se **compila a HTML** y es parte de la **documentación**.

Casos de Uso: Dónde Ubicar Archivos
===================================

Pregúntate: ¿Esto va en ``source/`` o en la raíz?
=================================================

**Usa este árbol de decisión:**

.. code-block:: text

 ¿Es contenido que quieres documentar/mostrar en HTML?
 |
 +- SÍ -> Va en source/
 | Ejemplos:
 | • Guías de usuario (.rst, .md)
 | • Tutoriales
 | • Referencias
 | • Documentación de procedimientos
 | • Frameworks de documentación (Diátaxis)
 | • Glosarios
 | • Biblioteca de traducciones
 |
 +- NO -> Va en la raíz (en carpeta apropiada)
 Ejemplos:
 • Scripts de build (scripts/)
 • Configuraciones de proyecto (config/)
 • Herramientas externas (tools/)
 • Makefiles
 • Archivos .tar.gz de backups

Ejemplos Específicos
====================

Contenido Documental (-> ``source/``)
=====================================

.. list-table::
 :header-rows: 1
 :widths: 30 70

 * - Archivo/Carpeta
   - Razón
 * - ``diataxis/``
   - Framework de documentación (se documenta)
 * - ``docs/``
   - Documentación técnica (se compila a HTML)
 * - ``docs_maestros/``
   - Documentos fundamentales (se compilan a HTML)
 * - ``biblioteca/arc42/``
   - Traducciones arc42 (se compilan a HTML)
 * - ``01_fundamentos/``
   - Metodología de traducción (se documenta)
 * - ``glosario.rst``
   - Glosario (se compila a HTML)
 * - ``tutorial.md``
   - Tutorial (se compila a HTML)

Herramientas/Utilidades (-> raíz)
=================================

.. list-table::
 :header-rows: 1
 :widths: 30 70

 * - Archivo/Carpeta
   - Razón
 * - ``tools/plantuml.jar``
   - Herramienta para compilar diagramas
 * - ``scripts/deploy.sh``
   - Script de despliegue (automatización)
 * - ``scripts/clean.sh``
   - Script de limpieza (utilidad)
 * - ``config/``
   - Configuraciones del proyecto
 * - ``Makefile``
   - Herramienta de build
 * - ``backup.tar.gz``
   - Archivo de respaldo (no se documenta)

Excepciones y Casos Especiales
==============================

build/ - Salida Compilada
=========================

.. note::
 ``build/`` contiene el HTML generado por Sphinx.

 - **Ubicación:** Raíz del proyecto
 - **Razón:** Es salida/artefacto, no contenido fuente
 - **NO** debe editarse manualmente
 - Se regenera con ``make html``

_static/ y _templates/ en source/
=================================

.. note::
 Estas carpetas van en ``source/`` aunque no son "contenido" en sí:

 
 - ``_static/``: Recursos estáticos (CSS, JS, imágenes) para la documentación
 - ``_templates/``: Templates de Sphinx para personalizar HTML

 Van en ``source/`` porque Sphinx los necesita **durante la compilación**
 para generar el HTML correcto.

Validación de la Estructura
===========================

Checklist de Validación
=======================

Antes de hacer commit, verifica:

.. code-block:: text

 [ ] ¿Todo en source/ se compila a HTML?
 [ ] ¿Las herramientas están en tools/?
 [ ] ¿Los scripts están en scripts/?
 [ ] ¿Las configuraciones están en config/?
 [ ] ¿No hay archivos .tar.gz en source/?
 [ ] ¿No hay scripts .py o .sh en source/?
 [ ] ¿build/ está en .gitignore?

Comando de Verificación
=======================

Para verificar la estructura:

.. code-block:: bash

 # Ver estructura de raíz
 ls -d /tmp/ADT/*/

 # Debe mostrar:
 # build/ config/ scripts/ source/ tools/

 # Ver contenido de source/
 ls -d /tmp/ADT/source/*/

 # Debe mostrar solo carpetas de contenido documental

Consecuencias de NO Seguir las Reglas
=====================================

Si NO se sigue esta estructura:

[ERROR] **Problemas que ocurrirán:**

1. Sphinx intentará compilar herramientas como si fueran documentación
2. La documentación no se encontrará donde se espera
3. Los scripts no estarán accesibles desde la raíz
4. Confusión entre contenido y herramientas
5. Estructura inconsistente y difícil de mantener

Migración de Archivos
=====================

Si encuentras un archivo en el lugar incorrecto
===============================================

**Procedimiento:**

1. **Identifica** si es contenido o herramienta
2. **Mueve** a la ubicación correcta:

 .. code-block:: bash

 # Si es contenido documental:
 mv archivo.rst source/carpeta_apropiada/

 # Si es herramienta/script:
 mv script.py scripts/
 mv tool.jar tools/

3. **Actualiza** referencias si las hay
4. **Recompila** para verificar:

 .. code-block:: bash

 make clean
 make html

5. **Verifica** que todo funciona

Historial de Cambios
====================

.. list-table::
 :header-rows: 1
 :widths: 15 15 70

 * - Versión
   - Fecha
   - Cambios
 * - 1.0
   - 2026-01-27
   - Creación del documento. Establecimiento de reglas fundamentales.

Referencias
===========

- `Documentación Sphinx <https://www.sphinx-doc.org/>`_
- Estructura estándar de proyectos Sphinx
- :doc:`ARQUITECTURA_DOCUMENTAL_TRADUCCION`
- :doc:`ESTRUCTURA_DE_BIBLIOTECA`

.. important::
 
 **ESTE DOCUMENTO ES NORMATIVO**

 Todas las personas que trabajen en el proyecto ADT deben conocer y
 seguir estas reglas sin excepción.




:Documento: REGLAS_ESTRUCTURA_PROYECTO.rst
:Ubicación: ``source/docs_maestros/``
:Tipo: Normativo
:Cumplimiento: Obligatorio
