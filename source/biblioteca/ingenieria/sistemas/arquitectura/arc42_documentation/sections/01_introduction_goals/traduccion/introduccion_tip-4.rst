.. meta::
   :layout: post
   :title: Consejo 1-4: ¡Crea una vista general agrupando o clusterizando requisitos!
   :tags: requirement cluster functional-requirement
   :category: requirements
   :permalink: /tips/1-4/

.. _introduccion-tip-4:

===================================================================
Consejo 1-4: ¡Crea una vista general agrupando requisitos!
===================================================================

:Tema: Agrupación de requisitos
:Categoría: Requisitos
:Audiencia: Arquitectos, Analistas

----

Recomendación
=============

Agrupa o clusteriza casos de uso similares, historias de usuario, procedimientos, 
funciones, procesos, tareas u otros requisitos funcionales.

Para proporcionar una vista general de las funciones de tu sistema, describe en 
tu documentación de arquitectura solo la importancia de estos grupos sin entrar 
en requisitos individuales detallados.

----

Ejemplo
=======

La figura a continuación muestra un ejemplo: algunas elipses agrupan (clusterizan) 
múltiples requisitos, características o casos de uso. Algunos de ellos se pueden 
encontrar en la tabla.

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/01-requirements-cluster.webp
   :alt: Cluster de requisitos
   :align: center
   :width: 70%

   Cluster de requisitos

.. list-table:: Clusters de Requisitos
   :header-rows: 1
   :widths: 40 60

   * - Cluster de requisitos
     - Descripción
   * - Manejo de Importación
     - Import-from-Mandator, Import-von-PrintShop, Import-from-Scanner, 
       Import-from-CallCenter, Import-from-CAMS, ...
   * - Configuración
     - Configure-Person, Configure-PrintJob, Configure-ScanOCR, 
       Configure-Reports, ...

----

.. note::
   **Información de traducción:**
   
   - Archivo original: 2016-03-01-t-1-4.md
   - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
   - Fecha: 2026-01-27
