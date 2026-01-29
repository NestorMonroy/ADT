.. _cheatsheet_rst:

===============================================
Cheatsheet reStructuredText
===============================================

:Tipo: Referencia Rápida
:Uso: Mantener abierto durante traducción
:Actualización: 2026-01-28

.. contents:: Contenido
 :depth: 2
 :local:

----

Encabezados y Títulos
=====================

Niveles de Sección
------------------

.. code-block:: rst

 #################
 Parte (Nivel 0)
 #################

 *******************
 Capítulo (Nivel 1)
 *******************

 Sección (Nivel 2)
 =================

 Subsección (Nivel 3)
 --------------------

 Sub-subsección (Nivel 4)
 ^^^^^^^^^^^^^^^^^^^^^^^^

 Párrafo (Nivel 5)
 """""""""""""""""

**Regla:** Subrayado debe tener ≥ longitud del título

----

Formato de Texto
================

Énfasis y Estilos
-----------------

.. code-block:: rst

 *cursiva* o *énfasis*

 **negrita** o **énfasis fuerte**

 ``código inline``

 `texto con rol`:role:`nombre`

**Nota:** Debe haber espacio o puntuación alrededor del marcador

----

Listas
======

Lista No Numerada
-----------------

.. code-block:: rst

 - Item 1
 - Item 2
 - Item 3

Lista Numerada
--------------

.. code-block:: rst

 1. Primero
 2. Segundo
 3. Tercero

 # O auto-numerado:
 #. Primero
 #. Segundo

Lista Anidada
-------------

.. code-block:: rst

 - Item nivel 1

 - SubItem nivel 2
 - SubItem nivel 2

 - Item nivel 1

**Regla:** Línea vacía + 2 espacios para anidar

Lista de Definiciones
---------------------

.. code-block:: rst

 Término 1
 Definición del término 1.

 Término 2
 Definición del término 2.

----

Enlaces y Referencias
=====================

Enlaces Externos
----------------

.. code-block:: rst

 # URL simple
 https://ejemplo.com

 # Con texto
 `Texto del enlace <https://ejemplo.com>`_

 # Referencia nombrada
 `Texto del enlace`_

 .. _Texto del enlace: https://ejemplo.com

Referencias Internas
--------------------

.. code-block:: rst

 # Crear label
 .. _mi_seccion:

 Mi Sección
 ==========

 # Referenciar
 Ver :ref:`mi_seccion`

 # Con texto personalizado
 Ver :ref:`el texto aquí <mi_seccion>`

Referencias a Documentos
-------------------------

.. code-block:: rst

 :doc:`archivo_sin_extension`

 :doc:`texto personalizado <archivo>`

----

Bloques de Código
=================

Código Inline
-------------

.. code-block:: rst

 Use ``código inline`` para comandos o variables.

Bloque de Código
----------------

.. code-block:: rst

 .. code-block:: python

 def funcion():
 return "Hola"

**Lenguajes comunes:**

.. code-block:: text

 python, java, javascript, bash, sql, xml, json,
 yaml, rst, latex, html, css, cpp, c, rust, go, ruby

Bloque Literal
--------------

.. code-block:: rst

 Párrafo terminando con doble colon::

 Bloque literal
 Preserva espacios
 Y formato

----

Tablas
======

Tabla Simple (ASCII)
--------------------

.. code-block:: rst

 +--------+--------+--------+
 | Col 1 | Col 2 | Col 3 |
 +========+========+========+
 | A | B | C |
 +--------+--------+--------+
 | D | E | F |
 +--------+--------+--------+

Tabla List-Table (Recomendado)
-------------------------------

.. code-block:: rst

 .. list-table:: Título opcional
 :header-rows: 1
 :widths: 30 30 40

 * - Columna 1
 - Columna 2
 - Columna 3
 * - Dato A
 - Dato B
 - Dato C

**Ventaja:** Más fácil de mantener

----

Imágenes y Figuras
==================

Imagen Simple
-------------

.. code-block:: rst

 .. image:: ruta/imagen.png
 :width: 80%
 :alt: Texto alternativo

Figura con Caption
------------------

.. code-block:: rst

 .. figure:: imagen.png
 :align: center
 :width: 600px

 Caption de la figura aquí.

----

Admonitions (Cajas de Nota)
============================

Tipos Disponibles
-----------------

.. code-block:: rst

 .. note::
 Esto es una nota.

 .. warning::
 Esto es una advertencia.

 .. important::
 Esto es importante.

 .. tip::
 Esto es un consejo.

 .. caution::
 Esto es una precaución.

 .. danger::
 Esto es peligroso.

 .. attention::
 Presta atención.

 .. error::
 Esto es un error.

Admonition Personalizado
-------------------------

.. code-block:: rst

 .. admonition:: Título Personalizado

 Contenido del admonition.

----

Directivas Comunes
==================

Contenidos (TOC)
----------------

.. code-block:: rst

 .. contents:: Título
 :depth: 3
 :local:

Toctree
-------

.. code-block:: rst

 .. toctree::
 :maxdepth: 2
 :caption: Título
 :numbered:

 archivo1
 archivo2
 directorio/archivo3

Incluir Archivo
---------------

.. code-block:: rst

 .. include:: otro_archivo.rst

Sidebar
-------

.. code-block:: rst

 .. sidebar:: Título del Sidebar

 Contenido que aparece al lado.

----

Matemáticas
===========

Inline
------

.. code-block:: rst

 Fórmula inline: :math:`E = mc^2`

Display
-------

.. code-block:: rst

 .. math::

 E = mc^2

 F = ma

----

Comentarios
===========

Comentario Simple
-----------------

.. code-block:: rst

 .. Esto es un comentario
 No aparece en la salida

Comentario Multilínea
----------------------

.. code-block:: rst

 ..
 Esto es un comentario
 de múltiples líneas

 Tampoco aparece

----

Roles Comunes
=============

Roles de Sphinx
---------------

.. code-block:: rst

 :ref:`label`
 :doc:`documento`
 :term:`término`
 :math:`fórmula`
 :file:`archivo.txt`
 :command:`comando`
 :guilabel:`Botón`
 :kbd:`Ctrl+C`
 :menuselection:`Archivo --> Guardar`

----

Caracteres Especiales
=====================

Escapar Caracteres
------------------

.. code-block:: rst

 Usar backslash para escapar: \*no cursiva\*

 Para backslash literal: \\

Espacios No-breaking
--------------------

.. code-block:: rst

 Palabra1\ |nbsp|\ Palabra2

 .. |nbsp| unicode:: 0xA0
 :trim:

----

Secciones Especiales
====================

Epígrafe (Cita)
---------------

.. code-block:: rst

 .. epigraph::

 Texto de la cita aquí.

 -- Autor

Pull-quote
----------

.. code-block:: rst

 .. pull-quote::

 Texto destacado de un párrafo.

Highlights
----------

.. code-block:: rst

 .. highlights::

 Puntos destacados del documento.

----

Campos y Metadatos
==================

Lista de Campos
---------------

.. code-block:: rst

 :Autor: Juan Pérez
 :Fecha: 2026-01-28
 :Versión: 1.0
 :Contacto: email@ejemplo.com

----

Sustituciones
=============

Definir Sustitución
-------------------

.. code-block:: rst

 .. |nombre| replace:: Texto de reemplazo

Usar Sustitución
----------------

.. code-block:: rst

 El |nombre| aparece aquí.

----

Líneas y Separadores
====================

Línea Horizontal
----------------

.. code-block:: rst

 ----

Transición
----------

.. code-block:: rst

 Párrafo antes.

 ----

 Párrafo después.

----

Consejos Rápidos
================

Sintaxis Básica
---------------

.. code-block:: rst

 [OK] Línea vacía entre bloques
 [OK] Indentación consistente (2-4 espacios)
 [OK] Subrayado = longitud del título
 [OK] Espacio después de .. en directivas
 [OK] Línea vacía antes de listas anidadas

Errores Comunes
---------------

.. code-block:: rst

 [ERROR] ..note:: (falta espacio)
 [OK] .. note::

 [ERROR] *texto*fuera (sin espacios)
 [OK] *texto* fuera

 [ERROR] ========= (subrayado corto)
 Título Largo
 =========
 [OK] ==============
 Título Largo
 ==============

----

Recursos Adicionales
====================

Documentación Oficial
---------------------

.. code-block:: text

 Quick Reference:
 https://docutils.sourceforge.io/docs/user/rst/quickref.html

 Especificación completa:
 https://docutils.sourceforge.io/rst.html

 Sphinx RST Primer:
 https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

----

Plantillas Útiles
=================

Plantilla de Documento
----------------------

.. code-block:: rst

 .. _mi_documento:

 ===============
 Título Principal
 ===============

 :Autor: Tu Nombre
 :Fecha: |today|

 .. contents:: Contenido
 :depth: 2
 :local:

 Introducción
 ============

 Contenido aquí.

 Sección 1
 =========

 Subsección 1.1
 --------------

 Contenido.

 Conclusión
 ==========

 Conclusiones finales.

 Referencias
 ===========

 .. [1] Referencia 1
 .. [2] Referencia 2

Plantilla de API
----------------

.. code-block:: rst

 .. _funcion_nombre:

 ``funcion_nombre()``
 ====================

 .. code-block:: python

 def funcion_nombre(param1, param2):
 """Descripción breve."""
 pass

 Descripción detallada de la función.

 :param param1: Descripción del parámetro 1
 :type param1: tipo
 :param param2: Descripción del parámetro 2
 :type param2: tipo
 :return: Descripción del retorno
 :rtype: tipo
 :raises ValueError: Cuándo se lanza

 Ejemplo::

 >>> funcion_nombre(1, 2)
 resultado

----

.. seealso::
 * :doc:`../05_herramientas_medios/equivalencias/latex_rst_equivalencias` - Equivalencias LaTeX->RST
 * :doc:`troubleshooting` - Solución de problemas
 * :doc:`tutorial_completo` - Tutorial completo

.. note::
 Guarda este cheatsheet como favorito para consulta rápida durante el trabajo.
