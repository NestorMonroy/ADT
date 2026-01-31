.. _notas-traduccion-seccion-01:




Notas de Traducción - Sección 01
================================

:Sección: 01 - Introducción y Objetivos
:Archivos traducidos: 5/28 (Lote 1)
:Método: Peshitta + ADT Workflow v1.4.0
:Fecha: 2026-01-27
:Traductor: Equipo ADT




Resumen de Traducción
=====================

Estado Actual
=============

.. list-table:: Progreso de Traducción
 :header-rows: 1
 :widths: 30 15 15 40

 * - Lote
   - Archivos
   - Estado
   - Observaciones
 * - Lote 1
   - 5
   - [OK] Completado
   - 4 ejemplos + 1 tip
 * - Lote 2
   - 9
   - [RUNNING] Pendiente
   - Tips 2-10
 * - Lote 3
   - 9
   - [RUNNING] Pendiente
   - Tips 11-19
 * - Lote 4
   - 5
   - [RUNNING] Pendiente
   - Tips 20-24

**Total progreso:** 5/28 archivos (17.9%)




Archivos Traducidos - Lote 1
============================

Ejemplos
========

1. **introduccion_ejemplo-3.rst**

 - Original: ``01-overview-example-3.md``
 - Tipo: Ejemplo de Vista General (Overview)
 - Sistema: Traffic Pursuit Unit (TPU)
 - Líneas: 46 (original) -> 130 (traducido + metadata)
 - Tablas: 2 (objetivos del proyecto + requisitos funcionales)
 - Figuras: 1 (diagrama de casos de uso)
 - Notas especiales:
 * Convertida imagen Jekyll a directiva RST
 * Tabla de prioridades con 5 objetivos
 * Referencias a figura externa

2. **introduccion_ejemplo-htmlsc-1.rst**

 - Original: ``01-overview-example-htmlsc-1.md``
 - Tipo: Ejemplo de Vista General (Overview)
 - Sistema: HTML Sanity Checker (HtmlSC)
 - Líneas: 35 (original) -> 82 (traducido + metadata)
 - Enlaces externos: 2 (AsciiDoc, Markdown)
 - Figuras: 2 (diagrama general + ejemplo de reporte)
 - Notas especiales:
 * Preservados enlaces a documentación externa
 * Sistema extremadamente simple, útil como ejemplo introductorio

3. **requisitos_calidad_ejemplo-1.rst**

 - Original: ``01-quality-reqs-example-1.md``
 - Tipo: Ejemplo de Requisitos de Calidad
 - Sistema: HTML Sanity Checker (HtmlSC)
 - Líneas: 32 (original) -> 70 (traducido + metadata)
 - Tabla: 1 (6 objetivos de calidad con escenarios)
 - Footnotes: 1 (sobre duda en enlaces externos)
 - Notas especiales:
 * Tabla con prioridades 1-3
 * Convertida footnote markdown a RST
 * Atributos de calidad: Correctness, Safety, Flexibility, Performance

4. **requisitos_calidad_ejemplo-3.rst**

 - Original: ``01-quality-reqs-example-3.md``
 - Tipo: Ejemplo de Requisitos de Calidad
 - Sistema: Traffic Pursuit Unit (TPU)
 - Líneas: 22 (original) -> 53 (traducido + metadata)
 - Tabla: 1 (3 objetivos de calidad top-3)
 - Notas especiales:
 * Tabla simple con 3 prioridades
 * Atributos: Accuracy, Robustness, Ease of use

Tips y Consejos
===============

5. **introduccion_tip-1.rst**

 - Original: ``2016-03-01-t-1-1.md``
 - Tipo: Tip/Consejo
 - Tema: Resumen compacto de requisitos
 - Líneas: 29 (original) -> 78 (traducido + metadata)
 - Listas: 1 (excepciones)
 - Notas especiales:
 * Estructurado en secciones: Contexto, Recomendación, Excepciones
 * Regla de oro: menos de una página
 * Enfocado en la sección 1.1 de arc42




Decisiones de Traducción Importantes
====================================

Nombres Propios y Marcas
========================

Los siguientes términos se mantuvieron en inglés por ser nombres propios:

- **HTML Sanity Checker** (HtmlSC): Nombre del sistema
- **Traffic Pursuit Unit** (TPU): Nombre del sistema
- **MeasuringUnit**: Componente específico del TPU
- **Enterprise Architect**: Marca registrada
- **Gradle**: Nombre de herramienta

Términos Arquitectónicos (según Guía ADT)
=========================================

Aplicando la **Guía de Traducción Arquitectónica ADT**, los siguientes términos
se tradujeron contexto arquitectónico, NO literalmente:

.. list-table:: Traducción Arquitectónica
 :header-rows: 1
 :widths: 30 30 40

 * - Término Original
   - [ERROR] Literal (Incorrecto)
   - [OK] Contextual (Correcto)
 * - driving forces
   - fuerzas impulsoras
   - **factores determinantes**
 * - quality goals
   - objetivos de calidad
   - **atributos de calidad objetivo**
 * - stakeholder
   - interesado, parte interesada
   - **stakeholder** (preservar)

**Justificación:**

- **"driving forces"**: En arquitectura de software NO significa "fuerzas"
  físicas sino factores que impulsan decisiones. "Factores determinantes"
  captura mejor el concepto arquitectónico.

- **"quality goals"**: NO son simplemente "objetivos" - son ATRIBUTOS
  MEDIBLES Y ESPECÍFICOS de la arquitectura (ej: Performance < 2s,
  Availability 99.9%). Por eso se traduce como "atributos de calidad objetivo".

- **"stakeholder"**: Término técnico internacional estándar en gestión de
  proyectos y arquitectura. Se preserva en inglés.

Atributos de Calidad
====================

Los atributos de calidad se tradujeron con referencia al original:

.. list-table:: Traducción de Atributos de Calidad
 :header-rows: 1
 :widths: 40 40 20

 * - Inglés (Original)
   - Español (Traducido)
   - ISO 25010
 * - Correctness
   - Corrección
   - [OK]
 * - Safety
   - Seguridad
   - [OK]
 * - Robustness
   - Robustez
   - [OK]
 * - Flexibility
   - Flexibilidad
   - [OK]
 * - Performance
   - Rendimiento
   - [OK]
 * - Ease of use
   - Facilidad de uso
   - [OK]
 * - Accuracy
   - Precisión
   - [OK]

Estructura y Formato
====================

1. **Front matter YAML -> Metadata RST**

 Todas las directivas Jekyll (layout, title, tags, category, permalink)
 se convirtieron a directiva ``.. meta::`` de RST.

2. **Tablas Markdown -> list-table**

 Las tablas markdown se convirtieron a directiva ``.. list-table::`` de
 RST para mejor control de formato y ancho de columnas.

3. **Imágenes Jekyll -> figure**

 Las referencias ``{{ site.imageurl }}`` se convirtieron a directiva
 ``.. figure::`` con rutas absolutas al directorio de figuras.

4. **Enlaces HTML -> enlaces RST**

 Los enlaces HTML ``<a href="..." >`` se convirtieron a formato RST
 ``` `texto <url>`_ ```.

5. **Footnotes Markdown -> RST**

 Las footnotes ``[^nota]`` se convirtieron a directiva ``.. [#nota]``.




Tácticas ADT Aplicadas
======================

FASE 3: Traducción Inicial
==========================

[OK] **Método Peshitta** aplicado a todos los archivos:

- Traducción literal y fiel al original
- Preservación de estructura 1:1
- Mantenimiento de todos los elementos semánticos
- Sin interpretaciones o adaptaciones

FASE 3.5: Revisión de Literalidad
=================================

[RUNNING] **Pendiente:** Se aplicará después de completar Lote 1

Checklist a verificar:
- [ ] Todos los párrafos traducidos
- [ ] Todas las tablas preservadas
- [ ] Todas las figuras referenciadas
- [ ] Todos los enlaces funcionales
- [ ] Metadata completa




Problemas Encontrados y Soluciones
==================================

1. **Imagen TPU no disponible**

 - Problema: Referencia a ``{{ site.imageurl }}/examples/tpu/1-UseCases.jpg``
 - Solución: Ruta convertida a directorio local ``figuras/``
 - Acción pendiente: Copiar imagen del repositorio original

2. **Imágenes HtmlSC no disponibles**

 - Problema: Referencias a imágenes del sistema HtmlSC
 - Solución: Rutas convertidas a directorio local
 - Acción pendiente: Copiar imágenes del repositorio original

3. **Footnote con formato especial**

 - Problema: Footnote ``[^doubt]`` con texto largo
 - Solución: Convertida a ``.. [#duda]`` con formato RST apropiado




Lecciones Aprendidas
====================

Del Lote 1
==========

1. **Tablas complejas**: Las tablas con múltiples columnas y contenido largo
  se benefician de ``list-table`` sobre ``table`` simple.

2. **Metadata consistente**: Usar siempre la misma estructura en
  ``.. meta::`` para facilitar automatización futura.

3. **Figuras centralizadas**: Mejor usar directorio ``figuras/`` común que
  subdirectorios por archivo.

4. **Etiquetas únicas**: Cada archivo debe tener su propia etiqueta
  (``.. _nombre:``).

Comparación con Sección 02
==========================

- Sección 01 tiene **4x más archivos** que sección 02
- Mayor variedad de ejemplos (2 sistemas diferentes: TPU y HtmlSC)
- Más tablas de requisitos y objetivos de calidad
- Tips más enfocados en proceso que en contenido técnico




Próximos Pasos
==============

Inmediatos
==========

1. [OK] Ejecutar **FASE 3.5: Revisión de Literalidad** en Lote 1
2. [OK] Copiar imágenes necesarias al directorio ``figuras/``
3. [OK] Ejecutar **FASE 4: Aplicación de Tácticas**
4. [OK] Ejecutar **FASE 5: Validación** (compilar con Sphinx)

Siguiente Lote
==============

5. [RUNNING] Iniciar **Lote 2**: Tips 2-10 (9 archivos)
6. [RUNNING] Repetir FASES 3-5 para Lote 2




Referencias
===========

- :doc:`/02_procedimientos/workflow_general` (v1.4.0)
- :doc:`glosario_seccion_01`
- :doc:`seccion_01_introduccion_objetivos`




.. note::
 **Última actualización:** 2026-01-27

 **Workflow aplicado:** ADT v1.4.0

 **Siguiente revisión:** Después de completar FASE 3.5
