.. _glosario_adt:




Glosario ADT
============

Glosario completo de términos usados en el sistema ADT.

.. contents:: Contenido
 :depth: 2
 :local:




A
=

ADT
===
**Arquitectura de Documentación Técnica**. Sistema completo para traducción de documentación técnica con garantía de calidad.

Admonition
==========
Caja de nota especial en RST (note, warning, tip, etc.) que resalta información importante.

arc42
=====
Framework de documentación arquitectónica. Base empírica del sistema ADT (196 archivos traducidos).

Artifact
========
Componente resultante de un proceso de traducción (archivo RST, HTML, PDF).




C
=

Checklist
=========
Lista de verificación sistemática para asegurar completitud y calidad.

Compilación
===========
Proceso de generar HTML/PDF desde archivos fuente RST usando Sphinx.

Completitud
===========
Criterio de calidad que mide que 100% del contenido original esté presente en la traducción. Umbral: 100%.




E
=

Enriquecimiento
===============
Proceso de agregar contenido adicional (ejemplos, tablas, checklists) a la traducción. Nivel apropiado definido por MD-002.

Equivalencia
============
Correspondencia entre construcción en un formato (LaTeX) y otro (RST). Documentadas en tablas de equivalencias.




F
=

Fidelidad
=========
Grado en que la traducción preserva el significado del original. ADT prioriza fidelidad sobre elegancia.




L
=

Label
=====
Marcador de referencia en RST (``.. _nombre:``). Permite crear referencias cruzadas.

LaTeX
=====
Sistema de composición de documentos científicos y académicos. Uno de los formatos fuente soportados por ADT.




M
=

Markdown
========
Lenguaje de marcado ligero. Formato fuente común para documentación técnica.

Matriz de Decisión
==================
Herramienta que provee guía objetiva para decisiones frecuentes. Ejemplos: MD-001, MD-002, MD-004.

MD-001
======
Matriz de decisión: Modo 1 vs Modo 2. Decide qué modo de traducción usar.

MD-002
======
Matriz de decisión: Cuándo enriquecer. Define nivel apropiado de enriquecimiento según tamaño del original.

MD-004
======
Matriz de decisión: Traducir vs conservar. Define qué términos traducir y cuáles conservar en inglés.

Modo 1
======
**Alta Fidelidad**. Modo de traducción que preserva formato original (LaTeX->LaTeX). Ideal para documentos académicos.

Modo 2
======
**Transformación**. Modo de traducción que convierte a nuevo formato (LaTeX->RST). Ideal para documentación técnica web.




P
=

PASO 0
======
Fase crítica de pre-traducción donde se lee el documento COMPLETO antes de traducir. Previene omisiones.

Pandoc
======
Herramienta de conversión entre formatos de documento. Útil para conversiones automáticas LaTeX->RST.

Precisión Técnica
=================
Criterio de calidad que mide corrección de terminología y conceptos. Umbral: 100%.

Pygments
========
Librería de syntax highlighting usada por Sphinx para colorear código.




R
=

reStructuredText (RST)
======================
Lenguaje de marcado usado por Sphinx. Formato destino principal en ADT Modo 2.




S
=

Signifiant
==========
**Significante**. La forma externa/sintáctica de una construcción. Ejemplo: ``\textbf{}`` en LaTeX.

Signifié
========
**Significado**. El contenido semántico que debe preservarse. Ejemplo: "énfasis fuerte" independiente de la forma.

Sphinx
======
Generador de documentación basado en RST. Crea HTML, PDF y otros formatos desde archivos RST.




T
=

Toctree
=======
Directiva de Sphinx para crear tabla de contenidos jerárquica enlazando múltiples documentos.

Traducción Isomórfica
=====================
Traducción que preserva la estructura del original 1:1. Concepto base del Modo 1.

Transformación de Modelos
=========================
Proceso de convertir de un modelo (formato) a otro preservando semántica. Base conceptual de ADT.




V
=

Verificación Sistemática
========================
Proceso estructurado de verificar traducción contra checklist. Previene errores y omisiones.




W
=

Workflow
========
Secuencia definida de pasos para completar traducción. ADT define workflow v1.7.2 con 7 pasos.




Términos Técnicos de Traducción
===============================

Terminología
============
Conjunto de términos técnicos usados en un dominio. ADT requiere terminología consistente (MD-004).

Glosario de Proyecto
====================
Lista de decisiones de terminología para un proyecto específico. Asegura consistencia entre traductores.

Omisión
=======
Contenido del original que no aparece en la traducción. ADT busca 0% omisiones mediante PASO 0.

Re-trabajo
==========
Trabajo adicional para corregir errores u omisiones. Costoso; prevenible con proceso sistemático.




Métricas ADT
============

Velocidad de Traducción
=======================
Archivos procesados por hora. Promedio ADT: 3.3 arch/h. Mejora con experiencia hasta 4.5+ arch/h.

Tasa de Enriquecimiento
=======================
``((Traducido - Original) / Original) × 100``. Varía según tamaño del original (ver MD-002).

Completitud
===========
``(Contenido presente / Contenido original) × 100``. Meta ADT: 100%.

Calidad Total
=============
Promedio de 5 criterios de calidad. Umbral de aprobación ADT: ≥95%.




Acrónimos y Siglas
==================

ADT
===
Arquitectura de Documentación Técnica

API
===
Application Programming Interface

HTML
====
HyperText Markup Language

ISO
===
International Organization for Standardization

PDF
===
Portable Document Format

QA
--
Quality Assurance

REST
====
Representational State Transfer

RST
===
reStructuredText

UML
===
Unified Modeling Language

URL
===
Uniform Resource Locator




Convenciones ADT
================

Conservar en Inglés
===================
Términos que NO se traducen según MD-004:

- Acrónimos técnicos: API, REST, JSON
- Patrones de diseño: Singleton, Factory
- Metodologías: Scrum, ATAM
- Roles establecidos: Product Owner, Stakeholder

Traducir al Español
===================
Términos que SÍ se traducen según MD-004:

- Conceptos generales: Quality -> Calidad
- Verbos: Implement -> Implementar
- Adjetivos: Complex -> Complejo
- Sustantivos comunes: Risk -> Riesgo

Marcado de Primera Aparición
============================
Convención pedagógica: ``español (:term:`inglés')`` en primera aparición del término.




Roles en Traducción
===================

Traductor
=========
Persona que ejecuta la traducción aplicando workflow ADT.

Revisor
=======
Persona que verifica calidad de traducción contra checklists.

Project Manager
===============
Coordina proyecto de traducción, asigna archivos, monitorea progreso.

Subject Matter Expert (SME)
===========================
Experto en el dominio que valida precisión técnica de terminología.




Fases de Proyecto
=================

Fase de Análisis
================
Análisis inicial del proyecto: PASO 0 global, inventario, planificación.

Fase de Ejecución
=================
Traducción activa por lotes aplicando workflow ADT.

Fase de Integración
===================
Compilación global, verificación de referencias cruzadas, ajustes finales.

Fase de QA
==========
Revisión final de calidad antes de entrega.




Tipos de Documentos
===================

Documentación Académica
=======================
Papers, tesis, libros académicos. Típicamente usan LaTeX. Mejor con Modo 1.

Documentación Técnica
=====================
Manuales, APIs, guías técnicas. Típicamente Markdown/RST. Mejor con Modo 2.

Documentación de Usuario
========================
Manuales de usuario final, tutoriales. Típicamente web. Mejor con Modo 2.

Especificaciones
================
ISO, RFC, estándares formales. Requiere fidelidad absoluta. Mejor con Modo 1.




Herramientas
============

Sphinx
======
Generador de documentación. Convierte RST a HTML/PDF.

Pandoc
======
Conversor universal de formatos. Automatiza conversiones iniciales.

Git
===
Control de versiones. Esencial para proyectos de traducción colaborativos.

VS Code
=======
Editor recomendado para RST con extensión reStructuredText.

Make
====
Herramienta de build. Compila proyecto Sphinx con ``make html``.




Conceptos Avanzados
===================

Isomorfismo Semántico
=====================
Preservación del significado a través de transformación de forma. Concepto base de ADT.

Transformación MDA
==================
Model-Driven Architecture. Inspiración teórica para traducción como transformación de modelos.

Fidelidad vs Elegancia
======================
Principio ADT: Fidelidad > Elegancia. Traducción fiel es más valiosa que traducción "bonita".

Enriquecimiento Apropiado
=========================
Balance entre agregar valor y mantener concisión. Definido objetivamente por MD-002.




Estados de Documento
====================

Borrador
========
Primera versión de traducción. Requiere revisión.

En Revisión
===========
Traducción siendo verificada contra checklists.

Aprobado
========
Traducción cumple todos los criterios de calidad (≥95%).

Publicado
=========
Traducción entregada y disponible para audiencia final.




Errores Comunes
===============

Omisión
=======
Falta de contenido del original. Prevenible con PASO 0 completo.

Enriquecimiento Excesivo
========================
Agregar demasiado contenido no relacionado. Evitable con MD-002.

Terminología Inconsistente
==========================
Mismo término traducido diferente en distintos lugares. Evitable con glosario de proyecto.

Referencia Rota
===============
Link a label que no existe. Verificable durante compilación.




.. seealso::
 
 * :doc:`../01_fundamentos/glosario_traduccion` - Glosario original de traducción
 * :doc:`../04_reglas_operativas/matrices_decision/MD_004_traducir_vs_conservar` - Decisiones de terminología
 * :doc:`../07_guias_uso/faq` - Preguntas frecuentes

.. note::
 Este glosario evoluciona con el proyecto. Versión actual: 2026-01-28.
