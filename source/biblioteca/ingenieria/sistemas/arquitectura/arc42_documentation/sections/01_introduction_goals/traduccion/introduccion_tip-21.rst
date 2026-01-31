.. meta::
 :layout: post
 :title: Consejo 1-21: ¡Mantén una tabla de stakeholders!
 :tags: stakeholder essential thorough
 :category: requirements
 :permalink: /tips/1-21/

.. _introduccion-tip-21:




Consejo 1-21: ¡Mantén una tabla de stakeholders!
================================================

:Tema: Documentación de stakeholders
:Categoría: Requisitos
:Audiencia: Arquitectos, Gestores de proyecto




Recomendación
=============

Debes representar explícitamente las expectativas de estos stakeholders (ver arriba)
con respecto a la arquitectura y su documentación en forma de tabla.




Tabla Mínima de Stakeholders
============================

Puedes encontrar una versión mínima en la tabla a continuación, que solo describe
las expectativas o artefactos requeridos.

.. list-table:: Tabla de stakeholders con roles y expectativas
   :header-rows: 1
   :widths: 30 70

   * - Rol
     - Expectativa
   * - Administrador
     - Vista general de despliegue, detalles de instalación y operaciones, firewalls
   * - Departamento de QA
     - Descripción de las interfaces para pruebas de carga, posibles puntos de medición para pruebas de rendimiento, concepto técnico para seguridad y confiabilidad




Tabla Detallada de Stakeholders
===============================

La tabla a continuación muestra una versión más detallada que incluye la relevancia
para aprobación e información de contacto.

Presta atención a cualquier cambio en los equipos del proyecto y agrega junto a
las personas concretas, si es necesario, también su reemplazo y áreas de trabajo /
departamentos / organización respectivamente.

.. list-table:: Tabla de stakeholders detallada
 :header-rows: 1
 :widths: 25 25 20 30

 * - Rol
   - Contacto
   - Relevancia para aprobación
   - Expectativa
 * - Líder de proyecto
   - Ms. Foobar, Ph.D.
   - Alta
   - Vista general de riesgo técnico, interfaces externas
 * - Patrocinador del proyecto
   - Mrs. Lovelace, Ph.D.
   - Alta
   - Prueba de que se pueden lograr los top-3 atributos de calidad objetivo
 * - Desarrollador Backend
   - Bruno Batch
   - Ninguna
   - Concepto de persistencia y reporting, Detalles interfaz DWH




.. note::
 **Información de traducción:**

 - Archivo original: 2016-03-02-t-1-21.md
 - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
 - Paso 3.4 aplicado: "stakeholders" preservado, "quality goals" -> "atributos de calidad objetivo"
 - Fecha: 2026-01-27
