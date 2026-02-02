.. _glossary_tip_2:




Tip 12-2: ¡Documenta el glosario como una tabla!
================================================

:Tema: Formato de glosario
:Palabras clave: glossary, lean




Documenta el **glosario** como una tabla ordenada alfabéticamente de los términos más importantes que se usan en arquitectura y desarrollo.

Incluye terminología recurrente de **negocio** o **requisitos**, si estos no están definidos en otro lugar.

Puedes incluir traducciones normativas a otros idiomas, si los **stakeholders** trabajan en varios idiomas.

El **glosario** podría ser idéntico o similar al "**ubiquitous language**" del Domain-Driven-Design (y por lo tanto también puede estar contenido en la `sección 8 de arc42 (conceptos transversales) </section-8>`_).

Estructura de Tabla Recomendada
===============================

**Tabla Básica (Un Idioma):**

.. list-table:: Glosario del Sistema
 :header-rows: 1
 :widths: 25 75

 * - **Término**
   - **Definición**
 * - **API Client**
   - Aplicación externa que consume nuestros endpoints REST. Requiere autenticación vía API key.
 * - **Carrito de Compra**
   - Colección temporal de productos seleccionados por un cliente antes de completar la orden. Expira después de 24 horas de inactividad.
 * - **Cliente Final**
   - Usuario registrado con cuenta activa que realiza compras en la plataforma. Diferente de "Cliente Corporativo" que representa organizaciones.

**Tabla Multi-idioma (Proyectos Internacionales):**

.. list-table:: Glosario Tri-lingüe
 :header-rows: 1
 :widths: 20 40 20 20

 * - **English**
   - **Definition**
   - **Español**
   - **Deutsch**
 * - **Order**
   - Collection of products a customer wants to purchase, including shipping and payment details
   - **Pedido**
   - **Bestellung**
 * - **Shopping Cart**
   - Temporary collection of selected items before checkout
   - **Carrito**
   - **Warenkorb**
 * - **Checkout**
   - Process of finalizing a purchase and providing payment
   - **Pago**
   - **Kasse**




**Qué Incluir en el Glosario:**

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - **Tipo de Término**
   - **Incluir**
   - **Ejemplo**
 * - Términos de negocio específicos del dominio
   - [OK] SÍ
   - "Policy", "Premium", "Claim"
 * - Términos técnicos específicos del sistema
   - [OK] SÍ
   - "Event Bus", "Saga Pattern"
 * - Términos técnicos genéricos
   - [WARNING] SOLO si usados de forma especial
   - "Microservicio" (si definición difiere)
 * - Términos obvios o universales
   - [ERROR] NO
   - "Usuario", "Base de datos"
 * - Acrónimos
   - [OK] SÍ
   - "SLA", "API", "GDPR"




**Ejemplo Completo de Glosario:**

.. list-table:: Glosario - Sistema de e-Commerce
 :header-rows: 1
 :widths: 25 75

 * - **Término**
   - **Definición**
 * - **API Key**
   - Token de autenticación alfanumérico de 32 caracteres usado por API Clients para autenticarse. Válido por 1 año desde creación.
 * - **Backorder**
   - Pedido de producto actualmente sin stock que será enviado cuando el inventario se reponga. Cliente es notificado del delay estimado.
 * - **Carrito de Compra**
   - Colección temporal de productos seleccionados. Expira después de 24 horas de inactividad. Máximo 100 items por carrito.
 * - **Cliente Corporativo**
   - Organización con cuenta empresarial que realiza compras al por mayor. Tiene términos de pago neto-30 y descuentos por volumen.
 * - **Cliente Final**
   - Usuario individual registrado que realiza compras para uso personal. Paga al momento del checkout.
 * - **Fulfillment Center**
   - Almacén físico donde se almacenan productos y desde donde se envían pedidos. Identificado por código de 3 letras (ej: LAX, NYC).
 * - **Inventory**
   - Cantidad actual de unidades disponibles de un producto en un Fulfillment Center específico. Actualizado en tiempo real.
 * - **Pedido** (Order)
   - Transacción confirmada que incluye productos, dirección de envío, método de pago y fecha estimada de entrega. Tiene estado lifecycle.
 * - **RMA** (Return Merchandise Authorization)
   - Número de autorización de devolución de 10 dígitos emitido al cliente para retornar productos. Válido por 30 días.
 * - **SKU** (Stock Keeping Unit)
   - Identificador único alfanumérico de 8 caracteres asignado a cada variante de producto (ej: color, tamaño).




**Relación con Domain-Driven Design:**

.. note::
 **Ubiquitous Language**

 En DDD, el **Ubiquitous Language** es el lenguaje compartido entre desarrolladores y expertos de dominio. El **glosario de arc42** es una implementación práctica de este concepto.

 **Diferencias sutiles:**

  * **Ubiquitous Language:** Vivo, evoluciona en conversaciones, código, tests
  * **Glosario arc42:** Documentado, formal, referencia escrita

 **Recomendación:** Mantener ambos sincronizados.




**Mejores Prácticas:**

1. **Orden Alfabético**

   * [OK] Facilita búsqueda rápida
   * [OK] Convención estándar

2. **Definiciones Concisas**

   * [OK] 1-3 oraciones por término
   * [OK] Evitar definiciones circulares
   * [ERROR] NO: "Cliente es un tipo de usuario"
   * [OK] SÍ: "Cliente es una persona u organización que compra productos"

3. **Incluir Sinónimos**

   .. code-block:: text

     Pedido (Order, Solicitud)
     -> Indicar sinónimos comunes
     -> Ayuda en búsquedas

4. **Marcar Términos Deprecated**

   .. code-block:: text

     Cliente Premium (DEPRECATED - usar "Cliente VIP")

5. **Cross-referencias**

   .. code-block:: text

     Carrito de Compra
     -> Ver también: Checkout, Pedido




**Herramientas para Glosario:**

.. list-table::
 :header-rows: 1
 :widths: 30 40 30

 * - **Herramienta**
   - **Ventajas**
   - **Uso**
 * - **Markdown Table**
   - Simple, versionable con Git
   - Proyectos pequeños
 * - **Confluence**
   - Búsqueda, colaboración
   - Equipos medianos
 * - **Sphinx Glossary**
   - Auto-linking en docs
   - Proyectos con Sphinx
 * - **Google Sheets**
   - Colaboración real-time
   - Equipos distribuidos

**Ejemplo con Sphinx Glossary:**

.. code-block:: rst

 .. glossary::

 API Client
 Aplicación externa que consume nuestros endpoints.

 Carrito de Compra
 Colección temporal de productos seleccionados.

 Cliente Final
 Usuario registrado que realiza compras.




.. seealso::
 * **Tip 12-1** - Tomarse el glosario en serio
 * **Tip 12-3** - Agregar modelo gráfico
 * **Sección 8** - Conceptos Transversales (Ubiquitous Language)
