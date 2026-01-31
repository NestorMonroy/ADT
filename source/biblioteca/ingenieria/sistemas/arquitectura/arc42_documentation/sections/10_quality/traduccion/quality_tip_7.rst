.. _quality_tip_7:




Tip 10-7: ¡¡Considera escenarios de fallo/error/failure (calidad)!!
===================================================================

:Tema: Escenarios de manejo de errores y fallos
:Palabras clave: quality, quality-scenario, scenario




Seguramente conoces la `Ley de Murphy <https://en.wikipedia.org/wiki/Murphy%27s_law>`_: **Las cosas fallarán y los errores ocurrirán.**

Usa **escenarios de calidad** para documentar o especificar qué tipos/categorías de tales fallos o excepciones tu sistema maneja o tiene que manejar.

Ejemplos
========

**Ejemplo 1: Detección de proveedor no disponible**

   El sistema reconoce dentro de 60 segundos si un proveedor de pagos externo se vuelve no disponible. Entonces notificará a un administrador dentro de 60 segundos.

**Ejemplo 2: Logging seguro de excepciones**

   En caso de excepciones de aplicación o runtime no tratables, el sistema creará eventos de logging apropiados que permitan diagnosticar el error, pero que no contengan datos personales de usuario o cuenta (de categoría de seguridad de datos 2 o superior).




**Categorías de Fault/Error/Failure Scenarios:**

.. list-table::
   :header-rows: 1
   :widths: 25 35 40
   
   * - Categoría
     - Descripción
     - Ejemplo de Escenario
   * - **Detección**
     - ¿Cuándo detecta el sistema el fallo?
     - "Detectar DB no disponible en <5s"
   * - **Notificación**
     - ¿Quién es informado y cómo?
     - "Alertar admin vía SMS en <60s"
   * - **Logging**
     - ¿Qué se registra para diagnóstico?
     - "Log con stack trace, sin datos sensibles"
   * - **Recuperación**
     - ¿Cómo se recupera el sistema?
     - "Failover automático a DB secundaria"
   * - **Degradación**
     - ¿Funcionalidad reducida disponible?
     - "Modo solo-lectura durante fallo"
   * - **Prevención**
     - ¿Cómo se previenen fallos?
     - "Validar input, rechazar datos inválidos"

**Terminología Importante:**

* **Fault (Fallo)**: Defecto latente en el sistema (bug en código)
* **Error**: Manifestación del fault durante ejecución
* **Failure (Falla)**: El sistema no cumple su especificación observable por usuario




**Estructura Recomendada:**

1. **Tipo de fallo**: ¿Qué puede fallar? (servicio externo, DB, red, validación)
2. **Detección**: ¿Cuánto tarda en detectarse? (tiempo máximo)
3. **Respuesta**: ¿Qué hace el sistema? (retry, failover, degradación)
4. **Notificación**: ¿Quién es informado? (admin, usuario, equipo ops)
5. **Logging**: ¿Qué se registra? (suficiente para diagnóstico, sin datos sensibles)
6. **Recuperación**: ¿Cómo vuelve a la normalidad?

**Ejemplo Completo:**

.. code-block:: text

   Escenario: Fallo de servicio de pagos externo
   
   Tipo: Servicio externo no disponible
   Detección: Sistema detecta timeout después de 3 intentos (15s total)
   Respuesta: 
     - Marcar transacción como "pendiente"
     - Cambiar a proveedor de pagos secundario

   Notificación:
     - Usuario: "Procesando pago, puede tardar más de lo usual"
     - Admin: Email con detalles del proveedor caído

   Logging:
     - Timestamp, proveedor, código de error, ID de transacción
     - NO incluir datos de tarjeta de crédito

   Recuperación:
     - Monitoreo cada 60s del proveedor primario
     - Volver automáticamente cuando esté disponible
     - Procesar transacciones "pendientes" en batch




**Aspectos Críticos de Seguridad:**

.. warning::
   **Al loguear errores, NUNCA incluir:**
   
   * Contraseñas o tokens de autenticación
   * Datos de tarjetas de crédito
   * Información personal sensible (SSN, dirección)
   * Datos médicos o financieros
   * Claves de encriptación
   
     **SÍ incluir:**
   
   * IDs de transacción/sesión (hasheados si necesario)
   * Stack traces (sanitizados)
   * Códigos de error
   * Timestamps
   * Información de contexto (sin PII)




.. seealso::
   * **Tip 10-5** - Escenarios de uso/aplicación
   * **Tip 10-6** - Escenarios de cambio
   * **Sección 11** - Riesgos y Deuda Técnica
   * **Modelo Q42** - Etiqueta #reliable
