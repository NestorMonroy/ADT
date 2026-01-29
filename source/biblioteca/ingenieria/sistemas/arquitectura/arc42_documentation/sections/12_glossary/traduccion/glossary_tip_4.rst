.. _glossary_tip_4:

===============================================================
Tip 12-4: ¡Incluye traducciones en el glosario!
===============================================================

:Tema: Glosario multi-idioma
:Palabras clave: glossary, i18n, translation, thorough

----

¿Conoces la situación?

* Algunos de tus requisitos están escritos en alemán
* Tu equipo de desarrollo está ubicado parcialmente en Alemania, parcialmente en países que no hablan alemán
* Tu gerencia quiere una "documentación internacionalmente comprensible"

Entonces necesitas una referencia de traducción normativa para tus términos más importantes:

Simplemente agrega una columna a tu tabla de **glosario** por cada idioma que necesites soportar. Ver el siguiente ejemplo:

.. list-table:: Glosario Bilingüe
 :header-rows: 1
 :widths: 25 40 35

 * - **Term (EN)**
   - **Definition**
   - **Translation DE**
 * - *<Term-1>*
   - *<definition-1>*
   - *<German-translation-for-term-1>*
 * - *<Term-2>*
   - *<definition-2>*
   - *<German-translation-for-term-2>*

----

Casos de Uso para Glosario Multi-idioma
========================================

**Escenario 1: Equipos Distribuidos Globalmente**

.. code-block:: text

 Situación:
 +- Requisitos: Cliente alemán -> Documentos en alemán
 +- Dev Team: India, Polonia, Brasil -> Trabajan en inglés
 +- Management: USA -> Reportes en inglés

 Problema:
 Término alemán "Versicherungsnehmer" no tiene traducción
 directa al inglés ("Policyholder" vs "Insured Person")

 Solución en Glosario:

 | Deutsch | English | Definition |
 |--------------------|---------------|-------------------------------|
 | Versicherungsnehmer| Policyholder | Person who owns the insurance |
 | | | policy and pays premiums |

**Escenario 2: Offshore Development**

.. code-block:: text

 Situación:
 +- Cliente: España
 +- Dev Team: Argentina, México
 +- QA Team: India

 Desafío:
 Términos técnicos en español latino vs español europeo

 Ejemplo:
 ES (España): "Ordenador" -> EN: "Computer"
 ES (Latam): "Computadora" -> EN: "Computer"

 Glosario resuelve ambigüedad con traducción normativa.

**Escenario 3: Documentación Legal Multi-jurisdicción**

.. code-block:: text

 Situación:
 Sistema financiero operando en EU, USA, Asia

 Requisito:
 Términos legales deben traducirse precisamente

 Ejemplo:

 | English (USA) | Deutsch (DE) | (JP) | Definition |
 |---------------|-----------------|----------------|------------------|
 | Data Privacy | Datenschutz | | Protection of... |
 | GDPR | DSGVO | GDPR | EU regulation... |

----

**Estructura de Glosario Multi-idioma:**

**Opción 1: Idioma Base + Traducciones**

.. list-table::
 :header-rows: 1
 :widths: 20 35 15 15 15

 * - **Term (EN)**
   - **Definition (EN)**
   - **Español**
   - **Deutsch**
   - ****
 * - Order
   - Purchase transaction with items, shipping, payment
   - Pedido
   - Bestellung
   -
 * - Customer
   - Registered user who makes purchases
   - Cliente
   - Kunde
   -
 * - Checkout
   - Process to finalize purchase
   - Pago
   - Kasse
   -

**Opción 2: Múltiples Definiciones (para matices)**

.. list-table::
 :header-rows: 1
 :widths: 15 40 15 30

 * - **EN**
   - **Definition (EN)**
   - **DE**
   - **Definition (DE)**
 * - Claim
   - Request for insurance payment after incident
   - Schadensmeldung
   - Meldung eines Versicherungsfalls zur Schadensregulierung
 * - Premium
   - Regular payment for insurance coverage
   - Prämie / Beitrag
   - Regelmäßige Zahlung für Versicherungsschutz

----

**Mejores Prácticas para Traducciones:**

1. **Traducción Profesional**

 .. list-table::
 :header-rows: 1
 :widths: 50 50

 * - [ERROR] **MAL**
   - [OK] **BIEN**
 * - Google Translate sin revisión
   - Traductor profesional del dominio
 * - Desarrollador traduce sin contexto
   - Experto de dominio valida traducción
 * - Una sola traducción sin alternativas
   - Mostrar sinónimos si existen

2. **Consistencia en Todo el Proyecto**

 .. code-block:: text

 [OK] HACER:
 - Usar SIEMPRE la misma traducción del glosario
 - Actualizar código, UI, docs con término consistente

 [ERROR] EVITAR:
 - Código usa "Bestellung"
 - UI usa "Auftrag"
 - Docs usan "Order"
 -> Todo debería usar término del glosario

3. **Notas Culturales/Regionales**

 .. code-block:: text

 Term: Date Format
 EN (USA): MM/DD/YYYY -> "12/31/2023"
 EN (UK): DD/MM/YYYY -> "31/12/2023"
 DE: DD.MM.YYYY -> "31.12.2023"
 JP: YYYYMMDD -> "20231231"

 Nota en glosario ayuda a developers evitar bugs.

----

**Herramientas para Glosario Multi-idioma:**

.. list-table::
 :header-rows: 1
 :widths: 30 40 30

 * - **Herramienta**
   - **Ventajas**
   - **Limitaciones**
 * - **Excel/Google Sheets**
   - Fácil, colaborativo, columnas ilimitadas
   - No integrado con docs
 * - **Confluence**
   - Búsqueda multi-idioma
   - Requiere licencia
 * - **POEditor**
   - Específico para i18n
   - Orientado a UI strings
 * - **Crowdin**
   - Traducción colaborativa
   - Overkill para solo glosario
 * - **Sphinx i18n**
   - Integrado con docs
   - Curva de aprendizaje

----

**Ejemplo Completo: Sistema Bancario Internacional**

.. list-table:: Banking System Glossary
 :header-rows: 1
 :widths: 15 30 15 15 15 10

 * - **EN**
   - **Definition**
   - **DE**
   - **ES**
   - **FR**
   - **Abbr**
 * - Account
   - Bank account holding customer funds
   - Konto
   - Cuenta
   - Compte
   - ACC
 * - Transaction
   - Money transfer between accounts
   - Transaktion
   - Transacción
   - Transaction
   - TXN
 * - Balance
   - Current amount in account
   - Saldo / Kontostand
   - Saldo
   - Solde
   - BAL
 * - Overdraft
   - Negative balance permitted by bank
   - Überziehung
   - Sobregiro
   - Découvert
   - OD
 * - IBAN
   - International Bank Account Number
   - IBAN
   - IBAN
   - IBAN
   - IBAN
 * - SWIFT
   - Society for Worldwide Interbank Financial Telecom
   - SWIFT
   - SWIFT
   - SWIFT
   - SWIFT

----

**Proceso de Mantenimiento:**

.. code-block:: text

 1. Nuevo término identificado en reunión
 v
 2. Product Owner agrega en columna idioma base (EN)
 v
 3. Notificar a traductores profesionales
 v
 4. Traductores agregan columnas DE, ES, etc.
 v
 5. Expertos de dominio de cada región validan
 v
 6. Publicar versión actualizada
 v
 7. Equipos actualizan código/UI/docs
 v
 8. QA verifica consistencia

**Ciclo: Cada 2 semanas o cuando se agreguen >5 términos**

----

.. seealso::
 * **Tip 12-2** - Documentar glosario como tabla
 * **Tip 12-5** - Mantener glosario compacto
 * **Sección 8** - Conceptos Transversales (i18n strategy)
