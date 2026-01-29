.. _risks_ejemplo_htmlsc:

===============================================================
Ejemplo de Riesgos: HTML Sanity Checker
===============================================================

:Sistema: HTML Sanity Checker (HtmlSC)
:Categoría: Herramienta de validación HTML
:Palabras clave: risks, example

----

Este ejemplo muestra **riesgos** y **deuda técnica** para HTML Sanity Checker (HtmlSC), una herramienta que verifica la sanidad/validez de documentos HTML.

----

11. Riesgos y Deuda Técnica

============================

.. note::
 **Observación:** En nuestro pequeño ejemplo no vemos **riesgos** *reales* para arquitectura e implementación.

 Por lo tanto, los **riesgos** mostrados a continuación son un poco artificiales...

11.1 Riesgos Técnicos
=====================

.. list-table:: Riesgos Técnicos de HtmlSC
 :header-rows: 1
 :widths: 35 65

 * - **Riesgo**
   - **Descripción**
 * - **Cuello de botella con derechos de acceso en repositorios públicos**
   - Actualmente solo un único desarrollador tiene derechos de acceso para desplegar nuevas versiones de HtmlSC en servidores públicos como Bintray o portal de plugins de Gradle.
 * - **Sistema depende de `gradle` - que puede no estar disponible en computadoras objetivo**
   - Aunque el Java Runtime está instalado en muchas computadoras, podría no estar disponible para cada usuario potencial de HtmlSC.

----

**Análisis de Riesgos Técnicos:**

**Riesgo RT-001: Single Point of Failure en Deployment**

.. code-block:: text

 ID: RT-001
 Descripción: Solo 1 desarrollador puede hacer releases

 Impacto:
 +- Si ese desarrollador no está disponible
 | -> No se pueden publicar fixes urgentes
 +- Si pierde acceso
 | -> Proyecto bloqueado
 +- Bus factor = 1
 -> Riesgo organizacional alto

 Probabilidad: Media (desarrollador puede cambiar de trabajo)
 Severidad: Alta (bloquea releases)

 Mitigación:
 1. Dar acceso a 2+ desarrolladores (inmediato)
 2. Documentar proceso de release (1 día)
 3. Automatizar con CI/CD + tokens compartidos (1 semana)
 4. Setup backup maintainer (coordinar)

 Estado: NO MITIGADO

**Riesgo RT-002: Dependencia de Gradle**

.. code-block:: text

 ID: RT-002
 Descripción: Usuarios sin Gradle no pueden usar HtmlSC

 Impacto:
 +- Reduce audiencia potencial
 +- Usuarios necesitan instalar herramienta adicional
 +- Fricción en adopción

 Probabilidad: Media (muchos usuarios sin Gradle)
 Severidad: Media (workaround existe: instalar Gradle)

 Mitigación:
 1. Proveer standalone JAR con dependencies incluidas (2 días)
 2. Crear native binaries con GraalVM (2 semanas)
 3. Dockerizar aplicación (3 días)
 4. Publicar en package managers: brew, apt (1 semana)

 Estado: [WARNING] PARCIALMENTE MITIGADO (standalone JAR existe)

----

11.2 Riesgos de Negocio o Dominio
==================================

.. list-table:: Riesgos de Negocio
 :header-rows: 1
 :widths: 35 65

 * - **Riesgo**
   - **Descripción**
 * - **Sistema podría volverse obsoleto**
   - En caso de que procesadores AsciiDoc o Markdown implementen verificación HTML nativamente, HtmlSC podría volverse obsoleto.

----

**Análisis de Riesgos de Negocio:**

**Riesgo RN-001: Obsolescencia del Sistema**

.. code-block:: text

 ID: RN-001
 Descripción: Competidores integran funcionalidad similar

 Escenarios de Obsolescencia:

 1. AsciiDoctor agrega HTML validation nativa
 -> Usuarios de AsciiDoc ya no necesitan HtmlSC

 2. Markdown processors (pandoc, etc.) agregan checks
 -> Usuarios de Markdown migran

 3. IDEs/editores agregan HTML validation mejorada
 -> Usuarios prefieren solución integrada

 Impacto: Alto (pérdida completa de usuarios)
 Probabilidad: Baja-Media (en 2-5 años)

 Estrategias de Mitigación:

 1. DIFERENCIACIÓN
 +- Agregar features únicos (accessibility checks)
 +- Mejor reporting y analytics
 +- Integraciones con herramientas populares

 2. ECOSISTEMA
 +- Plugins para editores populares (VS Code, IntelliJ)
 +- Integraciones CI/CD (GitHub Actions, Jenkins)
 +- API pública para terceros

 3. PIVOTE
 +- Expandir a validación de otros formatos (XML, JSON)
 +- Ofrecer como servicio (SaaS)
 +- Licenciar a empresas

 Estado: [WARNING] MONITOREAR (review trimestral de competencia)

----

**Resumen de Riesgos:**

.. list-table::
 :header-rows: 1
 :widths: 10 25 15 15 15 20

 * - **ID**
   - **Riesgo**
   - **Tipo**
   - **Impacto**
   - **Prob.**
   - **Estado**
 * - RT-001
   - Single point deployment
   - Técnico
   - Alto
   - Media
   - NO MITIGADO
 * - RT-002
   - Dependencia Gradle
   - Técnico
   - Medio
   - Media
   - [WARNING] PARCIAL
 * - RN-001
   - Obsolescencia
   - Negocio
   - Alto
   - Baja
   - [WARNING] MONITOREAR

----

**Lecciones Aprendidas:**

1. **Incluso proyectos pequeños** tienen riesgos significativos
2. **Bus factor = 1** es común en open source, pero arriesgado
3. **Competencia nativa** es amenaza real para herramientas standalone
4. **Diversificación** de funcionalidad protege contra obsolescencia

----

.. seealso::
 * **Ejemplo TPU** - Riesgos en sistema embebido más complejo
 * **Tip 11-1** - Buscar riesgos con stakeholders
 * **Sección 10** - Requisitos de Calidad
