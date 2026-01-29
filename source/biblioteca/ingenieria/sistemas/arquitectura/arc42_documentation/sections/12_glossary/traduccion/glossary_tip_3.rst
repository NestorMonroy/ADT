.. _glossary_tip_3:

===============================================================
Tip 12-3: ¡Enriquece el glosario con un modelo (gráfico)!
===============================================================

:Tema: Modelo gráfico de glosario
:Palabras clave: glossary

----

Podrías explicar las **relaciones** de términos importantes en un diagrama, y usar ese diagrama como base para explicación o definición textual.

Encuentras un ejemplo a continuación (tomado del proyecto open-source "HtmlSanityCheck"):

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/figuras/12-graphical-glossary.png
 :alt: Glosario gráfico (tomado del proyecto open-source "HtmlSanityCheck")
 :align: center
 :width: 90%

 Glosario gráfico - HtmlSanityCheck

(En el ejemplo omitimos la tabla con definiciones apropiadas - estamos bastante seguros de que puedes imaginar cómo debería verse...)

----

Ventajas del Modelo Gráfico
============================

**Por qué Agregar Diagramas:**

.. list-table::
 :header-rows: 1
 :widths: 45 55

 * - **Beneficio**
   - **Descripción**
 * - **Relaciones Visuales**
   - Muestra cómo términos se relacionan entre sí (composición, agregación, herencia)
 * - **Comprensión Rápida**
   - Un diagrama vale más que 1000 palabras
 * - **Onboarding Efectivo**
   - Nuevos miembros entienden dominio visualmente
 * - **Identificación de Gaps**
   - Revela términos faltantes o relaciones no documentadas
 * - **Complementa Tabla**
   - Tabla = definiciones, Diagrama = contexto y relaciones

----

**Tipos de Diagramas para Glosario:**

**1. Diagrama de Clases UML (Simplificado)**

.. code-block:: text

 +-----------------+
 | Cliente |
 +-----------------+

 | herencia
 +-------+--------+
 | |
 +---------+ +--------------+
 | Cliente | | Cliente |
 | Final | | Corporativo |
 +---------+ +--------------+
 | |
 | realiza | realiza

 +---------------------+
 | Pedido |
 +---------------------+
 | contiene

 +---------------------+
 | Line Item |
 +---------------------+
 | referencia

 +---------------------+
 | Producto |
 +---------------------+

**2. Diagrama de Entidad-Relación**

.. code-block:: text

 [Cliente] --(1:N)-- [Pedido] --(1:N)-- [LineItem] --(N:1)-- [Producto]
 | |
 +--(1:N)--- [Dirección]

 [Pedido] --(1:1)-- [Pago]
 [Pedido] --(1:1)-- [Envío]

**3. Diagrama de Dominio (DDD Style)**

.. code-block:: text

 Bounded Context: Ventas
 +----------------------------------------+
 | |
 | +--------+ +----------+ |
 | | Cliente|-----| Pedido | |
 | +--------+ +----------+ |
 | | | |
 | | |
 | | +----------+ |
 | | | LineItem | |
 | | +----------+ |
 | | | |
 | |
 | +--------+ +----------+ |
 | |Carrito | | Producto | |
 | +--------+ +----------+ |
 | |
 +----------------------------------------+

----

**Ejemplo Completo: Sistema de e-Commerce**

**Glosario Gráfico:**

.. code-block:: text

 Sistema de e-Commerce - Domain Model

 +-------------+
 | Usuario |
 +-------------+

 |
 +-----+-----+-------------+----------+
 | | | |
 +----+ +--------+ +---------+ +-------+
 |Guest| |Cliente | | Admin | |Support|
 +----+ | Final | +---------+ +-------+
 +--------+
 |
 | tiene

 +------------+
 | Carrito |------+ agrega items
 +------------+ |
 | |
 | convierte a |
 |
 +------------+ +--------+
 | Pedido |--|LineItem|
 +------------+ +--------+
 | |
 +------+ | referencia
 | |
 +--------+
 +-----++------+ |Producto|
 | Pago||Envío | +--------+
 +-----++------+ |
 | almacenado en

 +----------+
 |Fulfillment|
 | Center |
 +----------+

**Tabla de Glosario Correspondiente:**

.. list-table:: Términos del Modelo
 :header-rows: 1
 :widths: 25 75

 * - **Término**
   - **Definición**
 * - **Usuario**
   - Cualquier persona que interactúa con el sistema. Puede ser Guest, Cliente Final, Admin o Support.
 * - **Guest**
   - Usuario no autenticado que puede navegar productos pero no puede comprar.
 * - **Cliente Final**
   - Usuario registrado y autenticado que puede realizar compras. Tiene carrito persistente.
 * - **Carrito**
   - Colección temporal de productos seleccionados por un Cliente Final. Se convierte en Pedido al hacer checkout.
 * - **Pedido**
   - Transacción confirmada que incluye LineItems, Pago y Envío. Generado desde Carrito.
 * - **LineItem**
   - Línea individual en un Pedido que referencia un Producto, cantidad y precio al momento de compra.
 * - **Producto**
   - Item vendible en el catálogo. Almacenado en uno o más Fulfillment Centers.
 * - **Fulfillment Center**
   - Almacén físico donde se almacenan Productos y desde donde se envían Pedidos.

----

**Cómo Crear un Glosario Gráfico:**

**Paso 1: Identificar Entidades Principales**

.. code-block:: text

 Del dominio de negocio, extraer:
 - Sustantivos clave
 - Conceptos principales
 - Actores del sistema

**Paso 2: Identificar Relaciones**

.. code-block:: text

 Preguntarse:
 - ¿A pertenece a B?
 - ¿A contiene B?
 - ¿A crea B?
 - ¿A es un tipo de B?

**Paso 3: Dibujar el Modelo**

Herramientas recomendadas:

* **PlantUML** - Texto a diagrama
* **draw.io** - Visual, gratis
* **Lucidchart** - Profesional
* **Mermaid** - Integrado en Markdown

**Paso 4: Sincronizar con Tabla**

* [OK] Cada término en diagrama debe estar en tabla
* [OK] Cada término en tabla puede estar en diagrama (opcional)
* [OK] Definiciones consistentes

----

**Ejemplo con PlantUML:**

.. code-block:: plantuml

 @startuml

 class Cliente {
 +nombre
 +email
 }

 class Pedido {
 +id
 +fecha
 +estado
 }

 class LineItem {
 +cantidad
 +precio
 }

 class Producto {
 +sku
 +nombre
 }

 Cliente "1" -- "*" Pedido : realiza
 Pedido "1" *-- "*" LineItem : contiene
 LineItem "*" -- "1" Producto : referencia

 @enduml

----

**Cuándo Usar Glosario Gráfico:**

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Situación**
   - **Recomendación**
 * - Dominio complejo con muchas relaciones
   - [OK] **SÍ** - Diagrama ayuda mucho
 * - Dominio simple con <10 términos
   - [WARNING] **OPCIONAL** - Tabla puede ser suficiente
 * - Onboarding frecuente de nuevos
   - [OK] **SÍ** - Facilita aprendizaje
 * - Stakeholders visuales
   - [OK] **SÍ** - Prefieren diagramas a tablas
 * - Dominio muy técnico
   - [WARNING] **CUIDADO** - Puede intimidar a no-técnicos

----

**Mantenimiento del Glosario Gráfico:**

.. warning::
 **Riesgo de Obsolescencia**

 Los diagramas tienden a desactualizarse más rápido que tablas.

 **Mitigación:**

 * [PROCESSING] Revisar en cada sprint
 * [NOTE] Usar herramientas de diagramas-como-código (PlantUML, Mermaid)
 * [LINK] Automatizar generación desde modelo de datos si es posible
 * [OK] Incluir en Definition of Done

----

.. seealso::
 * **Tip 12-1** - Tomarse el glosario en serio
 * **Tip 12-2** - Documentar como tabla
 * **Sección 5** - Building Block View (diagrama de bloques)
 * **Sección 8** - Conceptos Transversales (Domain Model)
