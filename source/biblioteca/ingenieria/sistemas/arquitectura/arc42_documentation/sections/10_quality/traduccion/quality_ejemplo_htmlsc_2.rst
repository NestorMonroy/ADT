.. _quality_ejemplo_htmlsc_2:

===============================================================
Ejemplo de Escenarios de Calidad: HTML Sanity Checker
===============================================================

:Sistema: HTML Sanity Checker (HtmlSC)
:Categoría: Herramienta de validación HTML
:Palabras clave: quality, example

----

Este ejemplo muestra **escenarios de calidad** para HTML Sanity Checker (HtmlSC), una herramienta que verifica la sanidad/validez de documentos HTML.

----

10.2 Escenarios de Calidad
===========================

.. list-table:: Escenarios de Calidad para HTML Sanity Checker
 :header-rows: 1
 :widths: 10 90

 * - **ID**
 - **Descripción**
 * - **10.2.1**
 - Cada enlace interno roto será encontrado.
 * - **10.2.2**
 - Cada imagen (local) faltante será encontrada.
 * - **10.2.3**
 - La **corrección** de todas las verificaciones está asegurada mediante pruebas automatizadas positivas y negativas.
 * - **10.2.4**
 - El reporte de resultados debe contener *todos* los resultados (también conocidos como hallazgos - findings).
 * - **10.2.5**
 - HtmlSC debe ser **extensible** con nuevos algoritmos de verificación y nuevos escenarios de uso (es decir, desde diferentes sistemas de build).
 * - **10.2.6**
 - HtmlSC deja sus archivos fuente completamente intactos: El contenido de los archivos a verificar *nunca* será modificado.
 * - **10.2.7**
 - HtmlSC realiza todas las verificaciones en un archivo HTML de 100kBytes en menos de 10 segundos.

----

Análisis de los Escenarios
===========================

**Atributos de Calidad Cubiertos:**

.. list-table::
 :header-rows: 1
 :widths: 30 40 30

 * - **Atributo Q42**
 - **Escenarios Relacionados**
 - **Prioridad**
 * - **#testable**
 - 10.2.1, 10.2.2, 10.2.3
 - Alta
 * - **#efficient**
 - 10.2.7
 - Alta
 * - **#flexible**
 - 10.2.5
 - Media
 * - **#safe**
 - 10.2.6
 - Alta
 * - **#reliable**
 - 10.2.4
 - Alta

**Características de los Escenarios:**

1. **Específicos y Medibles** (10.2.7)

 * Tamaño de archivo: 100kBytes
 * Tiempo máximo: 10 segundos
 * [OK] Fácilmente verificable

2. **Basados en Funcionalidad Core** (10.2.1, 10.2.2)

 * Detección de enlaces rotos
 * Detección de imágenes faltantes
 * [OK] Value proposition principal del sistema

3. **Consideraciones de Calidad** (10.2.3)

 * Testing automatizado
 * Cobertura positiva y negativa
 * [OK] Garantía de corrección

4. **No-Funcionales Críticos** (10.2.6)

 * Inmutabilidad de archivos fuente
 * [OK] Requisito de seguridad fundamental

----

**Lecciones Aprendidas:**

* [OK] **Escenarios concretos**: Cada uno es específico y verificable
* [OK] **Cobertura balanceada**: Mezcla de funcionales y no-funcionales
* [OK] **Métricas claras**: Tiempo, tamaño, completitud definidos
* [WARNING] **Priorización implícita**: Podría beneficiarse de prioridades explícitas

----

.. seealso::
 * **Ejemplo TPU-1** - Quality tree y escenarios más detallados
 * **Tip 10-5** - Escenarios de uso/aplicación
 * **Tip 10-8** - Usar escenarios para evaluación de arquitectura
