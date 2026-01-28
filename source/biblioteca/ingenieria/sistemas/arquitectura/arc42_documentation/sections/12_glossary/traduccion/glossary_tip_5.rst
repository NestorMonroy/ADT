.. _glossary_tip_5:

===============================================================
Tip 12-5: ¡Mantén el glosario compacto! Evita trivialidades.
===============================================================

:Tema: Glosario minimalista
:Palabras clave: glossary, lean

----

Mantén el número de términos en tu **glosario** bastante pequeño: En nuestra experiencia práctica, **10-30 términos** fueron a menudo suficientes para explicar las *cosas* realmente importantes.

.. warning::
   **No quieres escribir otra enciclopedia o recrear Wikipedia en tu glosario!**

Evita trivialidades, incluye términos *específicos* del espacio de problema y solución de tu sistema.

Ni "UML" (abreviatura de "Unified Modeling Language") ni "Java" (lenguaje de programación) necesitan ser explicados en un **glosario**.

Principio de Minimalismo
=========================

**El Glosario NO es:**

* ❌ **Enciclopedia técnica** de todos los acrónimos
* ❌ **Diccionario** de términos genéricos
* ❌ **Tutorial** de tecnologías usadas
* ❌ **Lista exhaustiva** de toda palabra del dominio

**El Glosario SÍ es:**

* ✅ **Referencia concisa** de términos específicos del sistema
* ✅ **Lenguaje compartido** entre stakeholders
* ✅ **Definiciones normativas** de conceptos clave
* ✅ **Disambiguación** de términos ambiguos

----

**Reglas para Incluir/Excluir Términos:**

.. list-table::
   :header-rows: 1
   :widths: 30 35 35
   
   * - **Término**
     - **¿Incluir?**
     - **Razón**
   * - **REST API**
     - ❌ NO
     - Término técnico universal, conocido
   * - **Microservicio**
     - ❌ NO (usualmente)
     - Concepto estándar
   * - **Saga Pattern**
     - ⚠️ TAL VEZ
     - Si usas de manera no-estándar
   * - **Cliente Premium**
     - ✅ SÍ
     - Específico de tu dominio
   * - **Workflow de Aprobación**
     - ✅ SÍ
     - Proceso particular de tu sistema
   * - **Java**
     - ❌ NO
     - Lenguaje conocido
   * - **Python**
     - ❌ NO
     - Lenguaje conocido
   * - **UML**
     - ❌ NO
     - Estándar conocido
   * - **GDPR**
     - ⚠️ TAL VEZ
     - Si explicas cómo LO implementas
   * - **SLA**
     - ⚠️ TAL VEZ
     - Solo si defines TUS SLAs específicos
   * - **Usuario**
     - ❌ NO
     - Demasiado genérico
   * - **Cliente VIP**
     - ✅ SÍ
     - Diferente de cliente regular

----

**Criterios de Inclusión:**

**1. ¿Es Específico del Dominio?**

.. code-block:: text

   ✅ INCLUIR:
   - "Underwriting" (en sistema de seguros)
   - "Retargeting Pixel" (en sistema de publicidad)
   - "Fulfillment" (en e-commerce)
   
   ❌ EXCLUIR:
   - "Database" (concepto general)
   - "Server" (infraestructura genérica)
   - "API" (término universal)

**2. ¿Tiene Significado Especial en Tu Sistema?**

.. code-block:: text

   ✅ INCLUIR si redefinido:
   
   "Session" en tu sistema significa:
   → Estado persistente durante navegación + 30 min post-cierre
   
   (Diferente de session estándar HTTP)
   
   ❌ EXCLUIR si es significado estándar:
   
   "HTTP Session" = concepto estándar conocido

**3. ¿Stakeholders lo Usan con Significados Diferentes?**

.. code-block:: text

   ✅ INCLUIR para disambiguar:
   
   "Cliente" puede significar:
   - Cliente (negocio): Comprador de productos
   - API Client (técnico): Aplicación que consume API
   
   Glosario define ambos explícitamente.

**4. ¿Es Crítico para Entender el Sistema?**

.. code-block:: text

   Pregunta: ¿Si elimino este término del glosario,
             un nuevo miembro podría NO entender el sistema?
   
   SI → ✅ Incluir
   NO → ❌ Excluir

----

**Tamaño Recomendado del Glosario:**

.. list-table::
   :header-rows: 1
   :widths: 30 25 45
   
   * - **Tamaño del Proyecto**
     - **# Términos**
     - **Comentario**
   * - **Pequeño** (1-5 personas)
     - 5-15
     - Solo conceptos core
   * - **Mediano** (5-20 personas)
     - 15-30
     - Balance entre completo y manejable
   * - **Grande** (20-100 personas)
     - 30-50
     - Múltiples subdominios
   * - **Enterprise** (100+ personas)
     - 40-80
     - Por bounded context, no global

.. warning::
   **Si tu glosario tiene >100 términos:**
   
   * 🔴 Probablemente incluyes trivialidades
   * 🔴 Es inmanejable para mantener
   * 🔴 Nadie lo va a leer completo
   
   **Solución:** Dividir por bounded contexts o subdominios

----

**Ejemplos de Términos a EXCLUIR:**

.. code-block:: text

   ❌ NO incluir términos como:
   
   - HTML: Hyper Text Markup Language
   - CSS: Cascading Style Sheets
   - SQL: Structured Query Language
   - JSON: JavaScript Object Notation
   - XML: eXtensible Markup Language
   - HTTP: Hypertext Transfer Protocol
   - HTTPS: HTTP Secure
   - Git: Version control system
   - Docker: Containerization platform
   - Kubernetes: Container orchestration
   - AWS: Amazon Web Services
   - CI/CD: Continuous Integration/Deployment
   
   → Todos son conceptos técnicos estándares conocidos

**Excepción:** Si usas de manera no-estándar

.. code-block:: text

   ✅ INCLUIR si redefinido:
   
   "Deployment" en nuestro sistema:
   → Blue-green deployment con feature flags y
   → Aprobación manual de Product Owner y
   → Rollback automático si error rate >0.1%
   
   (No es deployment estándar, tiene proceso específico)

----

**Ejemplo de Glosario Compacto (15 términos):**

.. list-table:: Glosario - Sistema de Reservas de Hotel
   :header-rows: 1
   :widths: 30 70
   
   * - **Término**
     - **Definición**
   * - **Availability**
     - Habitaciones no reservadas para fecha específica. Actualizado en tiempo real.
   * - **Booking**
     - Reserva confirmada con pago completado o garantía de tarjeta.
   * - **Channel**
     - Fuente de reserva (directo, OTA, GDS, corporativo).
   * - **Dynamic Pricing**
     - Algoritmo que ajusta precio basado en demanda, eventos, temporada.
   * - **Guaranteed Booking**
     - Reserva con tarjeta de crédito que cobra no-show fee.
   * - **Inventory**
     - Total de habitaciones disponibles por tipo y fecha.
   * - **No-Show**
     - Huésped con booking confirmado que no llega sin cancelar.
   * - **Occupancy Rate**
     - % de habitaciones ocupadas vs total inventario.
   * - **OTA**
     - Online Travel Agency (Booking.com, Expedia).
   * - **Overbooking**
     - Vender más habitaciones que inventario disponible (estrategia).
   * - **PMS**
     - Property Management System (software core del hotel).
   * - **Rate Plan**
     - Conjunto de reglas de pricing (BAR, corporate, promotional).
   * - **Room Type**
     - Categoría de habitación (Standard, Deluxe, Suite).
   * - **Walk-in**
     - Huésped sin reserva previa que solicita habitación.
   * - **Yield Management**
     - Estrategia de maximizar revenue via dynamic pricing y overbooking.

**Total: 15 términos**  
**Todos específicos del dominio de hotelería**  
**Ninguna trivialidad técnica**

----

**Mantenimiento del Glosario Compacto:**

**Revisión Trimestral:**

.. code-block:: text

   Preguntas a hacer:
   
   1. ¿Algún término ya no se usa?
      → ELIMINAR
   
   2. ¿Algún término es ahora obvio para todos?
      → CONSIDERAR eliminar
   
   3. ¿Nuevos términos críticos han emergido?
      → AGREGAR (máximo 3-5 por trimestre)
   
   4. ¿Algún término necesita actualizar definición?
      → ACTUALIZAR

**Proceso de Aprobación para Nuevos Términos:**

.. code-block:: text

   Propuesta de nuevo término:
   ↓
   1. ¿Es específico del dominio? [SI/NO]
   ↓
   2. ¿Es crítico para entender sistema? [SI/NO]
   ↓
   3. ¿Tiene significado especial aquí? [SI/NO]
   ↓
   Si 2+ respuestas = SI → ✅ AGREGAR
   Si <2 respuestas = SI → ❌ RECHAZAR

----

.. seealso::
   * **Tip 12-1** - Tomarse el glosario en serio
   * **Tip 12-2** - Documentar como tabla
   * **Tip 12-6** - Responsable del glosario
