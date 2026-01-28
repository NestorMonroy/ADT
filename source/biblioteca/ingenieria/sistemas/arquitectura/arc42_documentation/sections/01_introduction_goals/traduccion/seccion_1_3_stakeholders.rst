.. meta::
   :subseccion: 1.3
   :titulo: Stakeholders
   :tipo: Plantilla arc42
   :version: 1.0.0
   :fecha: 2026-01-27

.. _seccion-1-3-stakeholders:

===================================================================
1.3 Stakeholders
===================================================================

Contenido
=========

Vista general explícita de los stakeholders del sistema, es decir, todas las personas, 
roles u organizaciones que:

- Deben conocer la arquitectura
- Deben ser convencidos de la arquitectura
- Deben trabajar con la arquitectura o con el código
- Necesitan la documentación de la arquitectura para su trabajo
- Deben tomar decisiones sobre el sistema o su desarrollo

----

Motivación
==========

Debes conocer a todas las partes involucradas en el desarrollo del sistema o 
afectadas por el sistema.

De lo contrario, podrías tener sorpresas desagradables más adelante en el proceso 
de desarrollo.

Estos stakeholders determinan el alcance y el nivel de detalle de tu trabajo y 
sus resultados.

----

Forma
=====

Tabla con nombres de roles, nombres de personas y sus expectativas con respecto 
a la arquitectura y su documentación.

----

Plantilla
=========

.. code-block:: rst

   1.3 Stakeholders
   ================
   
   .. list-table:: Tabla de Stakeholders
      :header-rows: 1
      :widths: 25 25 50
   
      * - Rol/Nombre
        - Contacto
        - Expectativas
      * - [Ej: Product Owner]
        - [Juan Pérez]
        - [Visión general de decisiones arquitectónicas,
          justificación de trade-offs principales]
      * - [Ej: Arquitecto Empresarial]
        - [María García]
        - [Alineación con estándares corporativos,
          compatibilidad con arquitectura de referencia]
      * - [Ej: Equipo de Desarrollo]
        - [Equipo Backend]
        - [Guías de implementación detalladas,
          decisiones técnicas documentadas]
      * - [Ej: Operaciones]
        - [Equipo DevOps]
        - [Vista de despliegue, requisitos de infraestructura,
          procedimientos operacionales]

----

Ejemplos de Stakeholders Comunes
=================================

**Gestión y Negocio:**

- Product Owner
- Patrocinador del proyecto
- Gerencia ejecutiva
- Líder de proyecto
- Comité directivo

**Técnicos:**

- Arquitectos (de software, empresariales, de soluciones)
- Desarrolladores (Frontend, Backend, Full-stack)
- Administradores de sistemas
- Administradores de bases de datos
- Ingenieros de DevOps
- Ingenieros de QA/Testing
- Ingenieros de seguridad

**Usuarios:**

- Usuarios finales
- Administradores del sistema
- Power users
- Usuarios de negocio

**Externos:**

- Proveedores de servicios externos
- Socios de integración
- Auditores
- Autoridades regulatorias
- Clientes corporativos

**Soporte y Mantenimiento:**

- Equipo de soporte técnico
- Equipo de mantenimiento
- Hotline/Help desk

----

Clasificación por Interés e Influencia
=======================================

Para priorizar stakeholders bajo presión de tiempo, puedes clasificarlos:

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/figuras/01-stakeholder-prio-EN.png
   :alt: Clasificación de stakeholders por interés e influencia
   :align: center
   :width: 70%

   Matriz de priorización de stakeholders

**Alto impacto, gran interés:**
   Involucra intensivamente. Comunícate proactivamente.

**Alto impacto, bajo interés:**
   Mantén satisfechos con esfuerzo mínimo necesario.

**Bajo impacto, alto interés:**
   Mantén informados. Pueden ayudar con detalles técnicos.

**Bajo impacto, bajo interés:**
   Monitorea, información mínima.

----

Ejemplos
========

Ver :ref:`introduccion-tip-21` para ejemplos detallados de tablas de stakeholders.

----

Tips Relacionados
=================

Ver:

- :ref:`introduccion-tip-19` - Busca stakeholders ampliamente
- :ref:`introduccion-tip-20` - Expectativas de stakeholders
- :ref:`introduccion-tip-21` - Tabla de stakeholders
- :ref:`introduccion-tip-22` - Evita duplicación
- :ref:`introduccion-tip-23` - Clasifica por interés e influencia

----

.. important::
   **Reglas clave para Stakeholders:**
   
   1. **Completitud** - Identifica TODOS los stakeholders relevantes
   2. **Expectativas claras** - Documenta QUÉ espera cada stakeholder
   3. **Contacto** - Incluye información de contacto actualizada
   4. **Priorización** - Identifica stakeholders críticos
   5. **Actualización** - Revisa y actualiza regularmente

----

.. note::
   **Información de traducción:**
   
   - Subsección arc42: 1.3 Stakeholder
   - Método: Peshitta + Terminología arquitectónica (Workflow v1.5.0)
   - Paso 3.4 aplicado: "stakeholder" preservado sin traducir
     (término técnico internacional estándar en arquitectura de software)
   - Fecha: 2026-01-27
