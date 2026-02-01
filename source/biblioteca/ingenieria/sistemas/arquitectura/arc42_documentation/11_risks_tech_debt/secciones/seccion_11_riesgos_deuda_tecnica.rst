.. _seccion_11:




Sección 11: Riesgos y Deuda Técnica (Risks and Technical Debt)
==============================================================

.. tip::
 **Riesgos y Deuda Técnica arc42**

 Los **riesgos** y la **deuda técnica** son parte inevitable de cualquier proyecto. Esta sección documenta los **riesgos técnicos** identificados y la **deuda técnica**, ordenados por prioridad, para facilitar la gestión proactiva.




Introducción
============

Esta sección contiene una lista de **riesgos técnicos** identificados o **deudas técnicas**, ordenada por prioridad.

Contenido
=========

Una lista de **riesgos técnicos** identificados o **deudas técnicas**, ordenada por prioridad.

Motivación
==========

 *"Risk management is project management for grown-ups"*

 (Gestión de riesgos es gestión de proyectos para adultos)

 — Tim Lister, `Atlantic Systems Guild <https://www.infoq.com/presentations/risk-project-management>`_

Este debería ser tu lema para la detección y evaluación sistemática de **riesgos** y **deudas técnicas** en la arquitectura, que serán necesarios para los stakeholders de gestión (por ejemplo, gerentes de proyecto, product owners) como parte del análisis de riesgos general y la planificación de mediciones.

Forma
=====

Lista de **riesgos** y/o **deudas técnicas**, probablemente incluyendo medidas sugeridas para minimizar, mitigar o evitar riesgos o reducir deudas técnicas.

**Estructura Recomendada:**

.. list-table:: Plantilla de Riesgos y Deuda Técnica
 :header-rows: 1
 :widths: 10 25 20 15 15 15

 * - **ID**
   - **Descripción**
   - **Impacto**
   - **Probabilidad**
   - **Prioridad**
   - **Mitigación**
 * - R-001
   - *< Descripción del riesgo >*
   - *< Alto/Medio/Bajo >*
   - *< Alta/Media/Baja >*
   - *< Crítica/Alta/Media >*
   - *< Medidas propuestas >*
 * - TD-001
   - *< Descripción de deuda técnica >*
   - *< Esfuerzo de mantenimiento >*
   - *< Urgencia de resolver >*
   - *< Prioridad >*
   - *< Plan de reducción >*

**Plantilla Minimalista:**

*< Inserta aquí lista o tabla de problemas conocidos, riesgos o deuda técnica >*




Relación con Otras Secciones
============================

* **Sección 1.2 (Objetivos de Calidad):** Los **riesgos** pueden amenazar los objetivos de calidad
* **Sección 9 (Decisiones de Arquitectura):** Las decisiones pueden introducir **riesgos** o **deuda técnica**
* **Sección 10.2 (Escenarios de Calidad):** Los **riesgos** pueden expresarse como escenarios negativos




Tips y Consejos
===============

.. toctree::
 :maxdepth: 1
 :caption: Tips para Riesgos y Deuda Técnica

 risks_tip_1
 risks_tip_2
 risks_tip_3
 risks_tip_4
 risks_tip_5
 risks_tip_6




Ejemplos de Aplicación
======================

.. toctree::
 :maxdepth: 1
 :caption: Ejemplos de Gestión de Riesgos

 risks_ejemplo_htmlsc
 risks_ejemplo_tpu




Referencias
===========

* `FAQ arc42 - Sección 11 <https://faq.arc42.org/category_c/#c-sec-11>`_
* Tim Lister: `"Risk Management is Project Management for Grown-Ups" <https://www.infoq.com/presentations/risk-project-management>`_
* Atlantic Systems Guild




.. note::
 **Gestión Proactiva de Riesgos**

 La detección sistemática de **riesgos técnicos** y **deuda técnica** permite:

 * [OK] **Anticipar problemas** antes de que se conviertan en crisis
 * [OK] **Priorizar esfuerzos** de refactorización
 * [OK] **Comunicar claramente** con stakeholders de negocio
 * [OK] **Justificar inversiones** en mejoras técnicas
 * [OK] **Reducir sorpresas** durante desarrollo y mantenimiento
