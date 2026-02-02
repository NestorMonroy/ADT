=====================================================

Ejemplo de Decisión: HTML Sanity Checker
========================================

.. meta::
   :layout: post
   :title: Ejemplo de Decisión: HTML Sanity Checker
   :tags: decisión, ejemplo
   :category: decisiones
   :permalink: /examples/decision-htmlsc/

9. Decisiones de Arquitectura




9.1 Verificación de enlaces externos pospuesta
==============================================

En la versión actual de HtmlSC no verificaremos enlaces externos.
Estas verificaciones han sido pospuestas para versiones posteriores.

9.2 Parsing de HTML con jsoup
=============================

Para verificar HTML lo parseamos en una representación interna (similar a DOM).
Para esta tarea usamos `jsoup <https://jsoup.org>`_, un parser de código abierto sin
dependencias externas.

Citando de su sitio web:

.. epigraph::

   jsoup es una librería Java para trabajar con HTML del mundo real.
   Proporciona una API muy conveniente para extraer y manipular datos,
   usando lo mejor de los métodos tipo DOM, CSS y jQuery.

**Objetivos de esta decisión:**

Verificar HTML programáticamente usando una API existente que proporcione métodos de acceso y búsqueda al árbol DOM del(los) archivo(s) a verificar.

**Criterios de decisión:**

* Pocas dependencias, para que el binario de HtmlSC permanezca tan pequeño como sea posible.
* Métodos de acceso y búsqueda para localizar fácilmente imágenes, enlaces y destinos de enlaces dentro del árbol DOM.

**Alternativas:**

* **HTTPUnit:** un framework de pruebas para aplicaciones y sitios web. Su enfoque principal son las pruebas web y sufre de un gran número de dependencias.
* **jsoup:** un parser HTML simple sin ninguna dependencia (!) y una API rica para acceder a todos los elementos HTML en sintaxis tipo DOM.

9.3 Verificación de similitud de cadenas usando Distancia Jaro-Winkler
======================================================================

La pequeña `librería java string similarity <https://github.com/rrice/java-string-similarity>`_
(por Ralph Allen Rice) contiene implementaciones de varios algoritmos de cálculo de similitud.
Como no está disponible como binario público, usamos el código fuente en su lugar, principalmente las clases en:

``net.ricecode.similarity.JaroWinklerStrategy``

.. seealso::
   `Distancia Jaro-Winkler en Wikipedia <https://wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance>`_
