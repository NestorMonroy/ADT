.. ADT - Procedimientos de Traducción Técnica documentation master file

====================================================
ADT - Procedimientos de Traducción Técnica
====================================================

**Sistema Integrado de Documentación Arquitectónica y Traducción Técnica**

Versión |release|

.. meta::
 :description: Sistema integrado que combina arc42, Diátaxis y metodología de traducción técnica
 :keywords: arc42, diataxis, traduccion tecnica, sphinx, documentacion

Bienvenida
==========

Bienvenido a la documentación completa de **ADT** (Arc42-Diátaxis-Traducción),
un sistema integrado que combina tres frameworks poderosos para la gestión
completa de documentación técnica:

1. **arc42** - Framework de documentación arquitectónica
2. **Diátaxis** - Framework de documentación por propósito
3. **Traducción** - Metodología de traducción técnica especializada

Esta documentación cubre metodologías, estándares, herramientas y casos prácticos
para traducción de alta calidad de documentación técnica.

.. note::
 Esta es la documentación del módulo de **Traducción Técnica**.

 Para ver otros módulos:

 - :doc:`../arc42/index` - Documentación Arquitectónica
 - :doc:`../diataxis/index` - Documentación por Propósito
 - :doc:`../biblioteca/index` - Gestión de Libros

Inicio Rápido
=============

Si eres nuevo en ADT, comienza aquí:

1. :doc:`07_guias_uso/guia_rapida` - Introducción de 5 minutos
2. :doc:`01_fundamentos/principios_fundamentales` - Conceptos base
3. :doc:`02_procedimientos/workflow_general` - Proceso completo
4. :doc:`06_casos_practicos/antes_despues/caso_01_latex_libro` - Ejemplo práctico

Búsqueda Rápida
===============

**¿Cómo traduzco un libro LaTeX?**
 Ver :doc:`08_prompts/prompt_maestro_latex`

**¿Qué modo uso para traducir?**
 Ver :doc:`04_reglas_operativas/matrices_decision/MD_001_modo_1_vs_modo_2`

**¿Cómo marco conceptos clave?**
 Ver :doc:`05_herramientas_medios/equivalencias/conceptos_clave`

**¿Cuáles son los errores comunes?**
 Ver :doc:`06_casos_practicos/errores_comunes/index`

Contenido Principal
===================

.. toctree::
 :maxdepth: 2
 :caption: Fundamentos
 :numbered:

 01_fundamentos/index
 01_fundamentos/glosario_traduccion
 01_fundamentos/principios_fundamentales
 01_fundamentos/taxonomias/index
 01_fundamentos/metamodelos/index

.. toctree::
 :maxdepth: 2
 :caption: Procedimientos
 :numbered:

 02_procedimientos/index
 02_procedimientos/workflow_general
 02_procedimientos/modo_alta_fidelidad/index
 02_procedimientos/modo_marcado_visual/index
 02_procedimientos/verificacion_calidad/index
 02_procedimientos/correccion_errores/index

.. toctree::
 :maxdepth: 2
 :caption: Estándares
 :numbered:

 03_estandares/index
 03_estandares/terminologia/index
 03_estandares/formato_por_medio/index
 03_estandares/calidad/index
 03_estandares/restricciones/index

.. toctree::
 :maxdepth: 2
 :caption: Reglas Operativas
 :numbered:

 04_reglas_operativas/index
 04_reglas_operativas/reglas_traduccion/index
 04_reglas_operativas/escenarios_traduccion/index
 04_reglas_operativas/matrices_decision/index

.. toctree::
 :maxdepth: 2
 :caption: Herramientas y Medios
 :numbered:

 05_herramientas_medios/index
 05_herramientas_medios/latex/index
 05_herramientas_medios/sphinx/index
 05_herramientas_medios/markdown/index
 05_herramientas_medios/equivalencias/index

.. toctree::
 :maxdepth: 2
 :caption: Casos Prácticos
 :numbered:

 06_casos_practicos/index
 06_casos_practicos/antes_despues/index
 06_casos_practicos/errores_comunes/index
 06_casos_practicos/casos_exito/index
 06_casos_practicos/ejercicios_practica/index

.. toctree::
 :maxdepth: 2
 :caption: Guías de Uso
 :numbered:

 07_guias_uso/index
 07_guias_uso/guia_rapida
 07_guias_uso/tutorial_completo
 07_guias_uso/faq
 07_guias_uso/troubleshooting

.. toctree::
 :maxdepth: 2
 :caption: Prompts
 :numbered:

 08_prompts/index
 08_prompts/prompt_maestro_latex
 08_prompts/prompt_maestro_sphinx
 08_prompts/prompt_maestro_markdown
 08_prompts/prompts_condicionales/index
 08_prompts/plantillas/index

.. toctree::
 :maxdepth: 2
 :caption: Referencias
 :numbered:

 09_referencias/index
 09_referencias/bibliografia
 09_referencias/recursos_externos
 09_referencias/documentacion_oficial/index
 09_referencias/cheatsheets/index

.. toctree::
 :maxdepth: 2
 :caption: Apéndices
 :numbered:

 10_apendices/index
 10_apendices/historia_versiones
 10_apendices/contribuidores
 10_apendices/licencia
 10_apendices/roadmap

Características Principales
============================

Alta Fidelidad
--------------

Traducción que preserva exactamente la estructura, formato y significado
del documento original.

.. admonition:: Principio Fundamental

 **Fidelidad > Elegancia**

 Una traducción perfectamente fiel es más valiosa que una traducción
 elegante pero imprecisa.

Marcado Visual
--------------

Sistema de marcado pedagógico que resalta términos técnicos en su primera
aparición: ``español (:term:`inglés`)``.

Múltiples Medios
----------------

Soporte completo para:

- **LaTeX** - Documentos académicos y libros
- **Sphinx/reStructuredText** - Documentación técnica
- **Markdown** - Tutoriales y guías ligeras

Control de Calidad
------------------

Múltiples checklists de verificación:

[OK] Checklist de contenido completo
[OK] Checklist de términos marcados
[OK] Checklist de formato preservado
[OK] Checklist de fidelidad estructural
[OK] Checklist de referencias cruzadas

Casos de Uso
============

.. grid:: 2
 :gutter: 3

 .. grid-item-card:: Traducir Libro Técnico
 :link: 06_casos_practicos/casos_exito/exito_01_libro_BPM
 :link-type: doc

 Proceso completo de traducción de un libro técnico,
 desde el PDF original hasta la versión final en Sphinx.

 .. grid-item-card:: Traducir Manual LaTeX
 :link: 06_casos_practicos/casos_exito/exito_02_manual_latex
 :link-type: doc

 Traducción de manual académico preservando toda
 la estructura LaTeX nativa.

 .. grid-item-card:: [DEBUG] Evitar Errores Comunes
 :link: 06_casos_practicos/errores_comunes/index
 :link-type: doc

 Aprende de los 7 errores más comunes y cómo evitarlos.

 .. grid-item-card:: [TARGET] Tutorial Completo
 :link: 07_guias_uso/tutorial_completo
 :link-type: doc

 Tutorial paso a paso de traducción desde cero.

Estadísticas
============

.. list-table:: Números del Proyecto ADT
 :widths: 40 60
 :header-rows: 1

 * - Elemento
 - Cantidad
 * - Secciones principales
 - 10
 * - Subcarpetas
 - 25+
 * - Procedimientos documentados
 - 9+
 * - Estándares definidos
 - 10+
 * - Reglas operativas
 - 16+
 * - Casos prácticos
 - 15+
 * - Prompts de producción
 - 3+

Idioma y Localización
=====================

**Idioma principal:** Español mexicano (es-MX)

**Convenciones de traducción:**

- Términos técnicos preservados en inglés
- Primera aparición: ``español (:term:`inglés`)``
- Usos posteriores: solo español
- Nombres propios NO se traducen
- Código fuente NO se traduce
- Comentarios de código SÍ se traducen


.. toctree::
 :maxdepth: 2
 :caption: Biblioteca
 :numbered:

 biblioteca/arc42/index

.. toctree::
 :maxdepth: 2
 :caption: Framework Diátaxis

 diataxis/index

.. toctree::
 :maxdepth: 2
 :caption: [LIST] Documentación Técnica

 docs/index

.. toctree::
 :maxdepth: 2
 :caption: Documentos Maestros

 docs_maestros/SINTESIS_METODOLOGICA_ADT
 docs_maestros/REGLAS_ESTRUCTURA_PROYECTO
 docs_maestros/ARQUITECTURA_DOCUMENTAL_TRADUCCION
 docs_maestros/ARQUITECTURA_TRADUCCION_IACT
 docs_maestros/ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta
 docs_maestros/GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL
 docs_maestros/METODO_TRADUCCION_PESHITTA_ZACHARIAS
 docs_maestros/PLAN_FINAL_REORGANIZACION
 docs_maestros/PLAN_INCREMENTAL_CON_ARCHIVADO
 docs_maestros/PLAN_CONTENIDO
 docs_maestros/PROMPT_MAESTRO_SPHINX_TRADUCCION
 docs_maestros/PROPUESTA_REORGANIZACION
 docs_maestros/PROPUESTA_REORGANIZACION_CORRECTA
 docs_maestros/README
 docs_maestros/RESUMEN_GUIA_CLASIFICACION

Índices y Búsqueda
==================

* :ref:`genindex` - Índice general
* :ref:`search` - Búsqueda en la documentación
* :doc:`01_fundamentos/glosario_traduccion` - Glosario de términos

Información del Proyecto
=========================

:Proyecto: ADT (Arc42-Diátaxis-Traducción)
:Versión: |version|
:Fecha: 2026-01-25
:Licencia: Open Source
:Autor: Equipo ADT

.. note::
 Esta documentación está en constante desarrollo.

 **Última actualización:** |today|

----

**¿Listo para empezar?** Ve a :doc:`07_guias_uso/guia_rapida`
