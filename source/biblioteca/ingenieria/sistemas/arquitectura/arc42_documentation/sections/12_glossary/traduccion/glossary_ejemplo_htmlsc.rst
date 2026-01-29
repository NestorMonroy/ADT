.. _glossary_ejemplo_htmlsc:

===============================================================
Ejemplo de Glosario: HTML Sanity Checker (Tabular)
===============================================================

:Sistema: HTML Sanity Checker (HtmlSC)
:Categoría: Herramienta de validación HTML
:Palabras clave: glossary, example

----

Aquí encuentras un ejemplo de un **glosario**.

Glosario Tabular
================

En el caso de este pequeño ejemplo, los términos dados aquí deberían ser buenos amigos para la mayoría de los desarrolladores.

Otra versión se puede encontrar en la sección de conceptos (ya que los términos de dominio son un tipo de conceptos transversales...).

----

Glosario del Sistema
====================

.. list-table:: Glosario - HTML Sanity Checker
 :header-rows: 1
 :widths: 30 70

 * - **Término**
 - **Definición**
 * - **Link**
 - Una referencia dentro de una HTMLPage. Apunta a LinkTarget.
 * - **Cross Reference**
 - Link de una parte de un documento a otra parte dentro del mismo documento.
 * - **External Hyperlink**
 - Link a otra página HTML o a un recurso dentro de otro dominio o sitio.
 * - **Run Result**
 - Resultados de verificación combinados para múltiples páginas (HTMLPages).
 * - **SinglePageResults**
 - Resultados combinados de todas las instancias `Checker` para una sola página HTML.

----

Análisis del Ejemplo
=====================

**Características de este Glosario:**

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Característica**
 - **Observación**
 * - **Tamaño**
 - Compacto (5 términos) [OK]
 * - **Especificidad**
 - Todos específicos del dominio de validación HTML [OK]
 * - **Claridad**
 - Definiciones concisas (1 oración) [OK]
 * - **Relaciones**
 - Términos se referencian entre sí (Link -> LinkTarget) [OK]
 * - **Audiencia**
 - Orientado a desarrolladores [OK]

----

**Expansión Recomendada del Glosario:**

**Términos Adicionales Sugeridos:**

.. list-table:: Glosario Expandido - HtmlSC
 :header-rows: 1
 :widths: 30 70

 * - **Término**
 - **Definición**
 * - **Link**
 - Una referencia dentro de una HTMLPage. Apunta a LinkTarget.
 * - **Cross Reference**
 - Link de una parte de un documento a otra parte dentro del mismo documento.
 * - **External Hyperlink**
 - Link a otra página HTML o a un recurso dentro de otro dominio o sitio.
 * - **Run Result**
 - Resultados de verificación combinados para múltiples páginas (HTMLPages).
 * - **SinglePageResults**
 - Resultados combinados de todas las instancias `Checker` para una sola página HTML.
 * - **Checker**
 - Componente que realiza una verificación específica en HTMLPage (ej: BrokenLinkChecker, ImageChecker).
 * - **HTMLPage**
 - Documento HTML individual que es analizado y validado por HtmlSC.
 * - **LinkTarget**
 - Destino al que apunta un Link. Puede ser anchor dentro de mismo documento o URL externo.
 * - **Finding**
 - Problema detectado por un Checker (ej: link roto, imagen faltante).
 * - **Severity**
 - Nivel de criticidad de un Finding (ERROR, WARNING, INFO).

----

**Alternativa: Glosario con Categorías**

.. list-table:: Glosario Categorizado
 :header-rows: 1
 :widths: 15 25 60

 * - **Categoría**
 - **Término**
 - **Definición**
 * - **Navegación**
 - Link
 - Referencia dentro de HTMLPage que apunta a LinkTarget
 * - **Navegación**
 - Cross Reference
 - Link interno dentro del mismo documento
 * - **Navegación**
 - External Hyperlink
 - Link a otro dominio o sitio
 * - **Navegación**
 - LinkTarget
 - Destino de un Link (anchor o URL)
 * - **Resultados**
 - Run Result
 - Resultados combinados para múltiples páginas
 * - **Resultados**
 - SinglePageResults
 - Resultados para una sola página HTML
 * - **Resultados**
 - Finding
 - Problema detectado por verificación
 * - **Core**
 - Checker
 - Componente que realiza verificación específica
 * - **Core**
 - HTMLPage
 - Documento HTML individual analizado

----

**Relación con Sección 8 (Conceptos Transversales):**

.. note::
 **Glosario vs Ubiquitous Language**

 El ejemplo menciona que "otra versión se puede encontrar en la sección de conceptos (ya que los términos de dominio son un tipo de conceptos transversales...)".

 **Esto ilustra:**

 * [OK] Glosario puede duplicarse en Sección 8 si términos son conceptos transversales
 * [OK] Domain Model en Sección 8 complementa glosario tabular
 * [OK] Ambas secciones trabajan juntas para definir lenguaje del sistema

**Ejemplo de Domain Model (Sección 8):**

.. code-block:: text

 Domain Model - HtmlSC

 +-------------+
 | HTMLPage |
 +-------------+
 | contiene

 +-------------+
 | Link |------+------------+
 +-------------+ | LinkTarget |
 | +------------+
 | es verificado por

 +-------------+
 | Checker |
 +-------------+
 | genera

 +-------------+
 | Finding |
 +-------------+
 | agregado a

 +------------------+
 |SinglePageResults |
 +------------------+
 | consolidado en

 +-------------+
 | Run Result |
 +-------------+

----

**Versión Multi-idioma:**

.. list-table:: Glosario Bilingüe - HtmlSC
 :header-rows: 1
 :widths: 25 50 25

 * - **Term (EN)**
 - **Definition**
 - **Deutsch**
 * - Link
 - Reference within HTMLPage pointing to LinkTarget
 - Verweis
 * - Cross Reference
 - Link within same document
 - Querverweis
 * - External Hyperlink
 - Link to another domain/site
 - Externer Link
 * - Run Result
 - Combined results for multiple pages
 - Laufergebnis
 * - SinglePageResults
 - Results for single HTML page
 - Einzelseitenergebnis

----

**Lecciones Aprendidas del Ejemplo:**

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Lección**
 - **Aplicación**
 * - **Mantener compacto**
 - 5 términos core son suficientes para sistema pequeño
 * - **Específico del dominio**
 - No incluir términos genéricos (HTML, URL ya conocidos)
 * - **Relaciones claras**
 - Link -> LinkTarget muestra dependencia
 * - **Una oración por definición**
 - Conciso y claro
 * - **Orientado a audiencia**
 - "Términos deberían ser buenos amigos para desarrolladores"
 * - **Integración con otras secciones**
 - Referencia a Sección 8 para Domain Model

----

**Expansión para Equipos Más Grandes:**

Si HtmlSC crece, el glosario podría expandirse:

.. list-table:: Glosario Expandido para Proyecto Grande
 :header-rows: 1
 :widths: 20 40 20 20

 * - **Término**
 - **Definición**
 - **Sinónimo**
 - **Ver También**
 * - Link
 - Referencia dentro de HTMLPage que apunta a LinkTarget
 - Hyperlink, Anchor
 - LinkTarget
 * - Checker
 - Componente que realiza verificación específica
 - Validator, Analyzer
 - Finding
 * - HTMLPage
 - Documento HTML individual analizado
 - Document, Page
 - Run Result
 * - Finding
 - Problema detectado (ERROR, WARNING, INFO)
 - Issue, Problem
 - Severity

----

.. seealso::
 * **Tip 12-2** - Documentar glosario como tabla
 * **Tip 12-5** - Mantener glosario compacto
 * **Sección 8** - Conceptos Transversales (Domain Model)
