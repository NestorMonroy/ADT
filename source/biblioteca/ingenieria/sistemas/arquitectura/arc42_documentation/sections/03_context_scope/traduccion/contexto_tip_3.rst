.. _contexto_tip_3:

===============================================================
Tip 3-3: ¡Combina el diagrama de contexto con una tabla!
===============================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Siempre debes complementar el diagrama de contexto con una tabla. De esta manera puedes reducir la cantidad de etiquetas en el diagrama y agregar fácilmente explicaciones, razonamiento o referencias cruzadas.

----

El diagrama de contexto comprensivo requiere una explicación tabular.

Mostramos solo extractos de la tabla correspondiente, pero debes considerar algunas características de este par típico "gráfico/tabla":

* Debes usar identificadores cortos dentro del diagrama en términos de abstracciones o términos genéricos. Usamos "Services" o "Market Data" en el ejemplo, que luego se describen con más detalle en la tabla
* Referencia dentro de la tabla a explicaciones más detalladas, por ejemplo, si estás usando términos de tu lenguaje de dominio, no necesitas explicarlos en el contexto, sino referir al capítulo relevante (probablemente 8.1, modelo de dominio)

Ver el siguiente ejemplo:

.. figure:: ../figuras/03-context-user-product-service.png
   :alt: Contexto de usuario, producto y servicio
   :align: center
   :width: 80%
   
   Contexto de usuario, producto y servicio

.. list-table:: Descripción de vecinos
   :header-rows: 1
   :widths: 30 70
   
   * - Vecino
     - Descripción
   * - **UserDB**
     - Resume todos los tipos de usuarios, internos (backoffice), externos (clientes, socios)
   * - **ProductProvider**
     - El proveedor de productos mantiene datos de catálogo, figuras, así como disponibilidad, reglas de configuración, información de pedidos y entregas, y en algunos casos precios y fuentes.
   * - **PaymentService**
     - Maneja la autenticación y todos los demás pasos requeridos para el pago real. NO involucra facturación.

----

.. seealso::
   * :ref:`seccion_03` - Contexto y Alcance
   * :ref:`contexto_tip_2` - Diagrama de contexto

----

:Tip: 3-3
:Tema: Diagrama + Tabla
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
