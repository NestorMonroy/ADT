.. _MD_005_estructura_salida:

===============================================
MD-005: Estructura de Salida
===============================================

:ID: MD-005
:Tipo: Matriz de Decisión
:Pregunta: ¿Cómo debo organizar los directorios del proyecto?
:Frecuencia: Una vez al inicio del proyecto
:Impacto: Medio (afecta mantenibilidad a largo plazo)

.. contents:: Contenido
 :depth: 2
 :local:

----

Pregunta Central
================

**¿Cuál es la mejor estructura de directorios para organizar mi proyecto de traducción?**

**Impacto:**
- Facilidad de encontrar archivos
- Escalabilidad del proyecto
- Claridad para colaboradores
- Mantenimiento a largo plazo

----

Las Tres Estructuras
====================

Estructura 1: Plana
-------------------

**Descripción:** Todos los archivos en un solo directorio.

.. code-block:: text

 proyecto/
 +- conf.py
 +- index.rst
 +- capitulo_01.rst
 +- capitulo_02.rst
 +- capitulo_03.rst
 +- anexo_a.rst
 +- referencias.rst

**Ventajas:**
- [OK] Muy simple
- [OK] Fácil de configurar
- [OK] Búsqueda rápida de archivos

**Desventajas:**
- [ERROR] Difícil escalar (>20 archivos)
- [ERROR] Sin agrupación lógica
- [ERROR] Confuso para proyectos grandes

**Cuándo usar:**
- Proyectos pequeños (< 20 archivos)
- Documentación simple
- Prototipos o POCs

Estructura 2: Por Temas
------------------------

**Descripción:** Directorios por tema o sección.

.. code-block:: text

 proyecto/
 +- conf.py
 +- index.rst
 +- introduccion/
 | +- index.rst
 | +- que_es.rst
 | +- requisitos.rst
 +- instalacion/
 | +- index.rst
 | +- linux.rst
 | +- windows.rst
 +- uso/
 | +- index.rst
 | +- basico.rst
 | +- avanzado.rst
 +- referencia/
 +- index.rst
 +- api.rst

**Ventajas:**
- [OK] Organización lógica
- [OK] Escala bien (hasta 100+ archivos)
- [OK] Fácil navegar
- [OK] Clara para colaboradores

**Desventajas:**
- [WARNING] Requiere planificación inicial
- [WARNING] Múltiples niveles de índices

**Cuándo usar:**
- **Mayoría de proyectos**
- Documentación técnica estándar
- Proyectos medianos a grandes

Estructura 3: Numerada
-----------------------

**Descripción:** Directorios numerados por orden.

.. code-block:: text

 proyecto/
 +- conf.py
 +- index.rst
 +- 01_fundamentos/
 | +- index.rst
 | +- conceptos.rst
 | +- principios.rst
 +- 02_instalacion/
 | +- index.rst
 | +- pasos.rst
 +- 03_uso/
 | +- index.rst
 | +- basico.rst
 | +- avanzado.rst
 +- 04_referencia/
 +- index.rst
 +- api.rst

**Ventajas:**
- [OK] Orden explícito garantizado
- [OK] Fácil añadir entre secciones (01.5_)
- [OK] Clara secuencia de lectura

**Desventajas:**
- [WARNING] Renombrar si cambia orden
- [WARNING] Números en URLs

**Cuándo usar:**
- Libros técnicos (orden importante)
- Tutoriales paso a paso
- Cursos o training materials

----

Matriz de Decisión
==================

Por Tamaño del Proyecto
-----------------------

.. list-table::
 :header-rows: 1
 :widths: 30 25 25 20

 * - **Archivos**
 - **Plana**
 - **Por Temas**
 - **Numerada**
 * - < 10
 - [OK] Óptimo
 - [WARNING] Excesivo
 - [WARNING] Excesivo
 * - 10-50
 - [WARNING] Aceptable
 - [OK] Óptimo
 - [OK] Óptimo
 * - 50-100
 - [ERROR] Difícil
 - [OK] Óptimo
 - [OK] Óptimo
 * - > 100
 - [ERROR] Inmanejable
 - [OK] Recomendado
 - [WARNING] Posible

Por Tipo de Contenido
----------------------

.. list-table::
 :header-rows: 1
 :widths: 35 25 25 15

 * - **Tipo**
 - **Plana**
 - **Por Temas**
 - **Numerada**
 * - README simple
 - [OK] Ideal
 - [ERROR] Excesivo
 - [ERROR] Excesivo
 * - Documentación API
 - [ERROR] Difícil
 - [OK] Ideal
 - [WARNING] Posible
 * - Manual de usuario
 - [WARNING] Posible
 - [OK] Ideal
 - [OK] Ideal
 * - Libro técnico
 - [ERROR] No viable
 - [OK] Bueno
 - [OK] Ideal
 * - Tutorial paso a paso
 - [WARNING] Posible
 - [OK] Bueno
 - [OK] Ideal

----

Convenciones de Nomenclatura
=============================

Para Directorios
----------------

**Recomendaciones:**

.. code-block:: text

 [OK] Minúsculas
 [OK] Guiones bajos (snake_case)
 [OK] Nombres descriptivos
 [OK] Sin espacios
 [OK] Sin caracteres especiales

**Ejemplos:**

.. code-block:: text

 [OK] introduccion/
 [OK] guia_usuario/
 [OK] api_referencia/
 [OK] 01_fundamentos/

 [ERROR] Introducción/
 [ERROR] Guía Usuario/
 [ERROR] API-Referencia/
 [ERROR] 01.Fundamentos/

Para Archivos
-------------

**Recomendaciones:**

.. code-block:: text

 [OK] Minúsculas
 [OK] Guiones bajos
 [OK] Extensión .rst
 [OK] Nombres descriptivos cortos

**Ejemplos:**

.. code-block:: text

 [OK] introduccion.rst
 [OK] instalacion_linux.rst
 [OK] api_referencia.rst
 [OK] faq.rst

 [ERROR] Introducción.rst
 [ERROR] Instalación Linux.rst
 [ERROR] API-Referencia.rst
 [ERROR] FAQ.RST

----

Estructura Recomendada ADT
===========================

Para Proyecto ADT
-----------------

.. code-block:: text

 ADT/
 +- source/
 | +- conf.py
 | +- index.rst
 | +- 01_fundamentos/
 | | +- index.rst
 | | +- ...
 | +- 02_procedimientos/
 | | +- index.rst
 | | +- ...
 | +- 03_estandares/
 | | +- index.rst
 | | +- calidad/
 | | | +- ...
 | | +- terminologia/
 | | +- ...
 | +- 04_reglas_operativas/
 | | +- index.rst
 | | +- matrices_decision/
 | | +- ...
 | +- 05_herramientas_medios/
 | | +- index.rst
 | | +- equivalencias/
 | | +- ...
 | +- 06_casos_practicos/
 | | +- index.rst
 | | +- antes_despues/
 | | +- errores_comunes/
 | +- 07_guias_uso/
 | | +- index.rst
 | | +- ...
 | +- 08_prompts/
 | +- 09_referencias/
 | +- 10_apendices/
 +- build/
 +- Makefile

**Razones:**
- Numeración para orden claro
- Subdirectorios por subsección
- Escalable hasta 100+ archivos
- Clara para colaboradores

----

Directorios Especiales
=======================

_static/
--------

**Propósito:** Archivos estáticos (CSS, JS, imágenes)

.. code-block:: text

 source/_static/
 +- css/
 | +- custom.css
 +- js/
 | +- custom.js
 +- images/
 +- logo.png
 +- diagrams/

_templates/
-----------

**Propósito:** Plantillas personalizadas de Sphinx

.. code-block:: text

 source/_templates/
 +- layout.html
 +- page.html

images/
-------

**Propósito:** Imágenes del contenido

.. code-block:: text

 source/images/
 +- arquitectura/
 | +- diagrama_01.png
 | +- diagrama_02.png
 +- capturas/
 +- screenshot_01.png

----

Checklist de Estructura
========================

Al Inicio del Proyecto
-----------------------

.. code-block:: text

 [ ] Decidí estructura (plana/temas/numerada)
 [ ] Creé directorio raíz
 [ ] Configuré conf.py
 [ ] Creé index.rst principal
 [ ] Creé subdirectorios necesarios
 [ ] Establecí convención de nombres
 [ ] Documenté estructura para equipo

Durante el Proyecto
--------------------

.. code-block:: text

 [ ] Mantengo consistencia de nombres
 [ ] Nuevos directorios siguen convención
 [ ] Índices actualizados (toctrees)
 [ ] Sin archivos huérfanos

Al Finalizar
------------

.. code-block:: text

 [ ] Estructura clara y lógica
 [ ] Fácil navegar
 [ ] Sin directorios vacíos
 [ ] Documentación de estructura actualizada

----

.. seealso::
 * :doc:`MD_003_nivel_segmentacion` - Nivel de segmentación
 * :doc:`../../02_procedimientos/workflow_general` - Workflow general
 * :doc:`../../07_guias_uso/guia_rapida` - Guía rápida

.. note::
 Esta matriz refleja las mejores prácticas de proyectos Sphinx. Adapta según necesidades específicas.
