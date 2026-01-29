.. _glossary_tip_6:

===============================================================
Tip 12-6: Haz a tu 'product owner' o 'project manager' responsable del glosario
===============================================================

:Tema: Responsabilidad del glosario
:Palabras clave: glossary, lean

----

En configuraciones de proyecto *ágiles*, el *product owner* puede ser responsable de mantener el **glosario**.

En configuraciones más tradicionales, esto podría ser el project manager.

Asignación de Responsabilidad
==============================

**Por qué Necesitas un Responsable:**

.. list-table::
 :header-rows: 1
 :widths: 45 55

 * - **Sin Responsable Claro**
   - **Con Responsable Asignado**
 * - [ERROR] Nadie actualiza el glosario
   - [OK] Glosario se mantiene actualizado
 * - [ERROR] "Alguien debería hacerlo"
   - [OK] Accountability clara
 * - [ERROR] Glosario se vuelve obsoleto
   - [OK] Revisión regular programada
 * - [ERROR] Inconsistencias no resueltas
   - [OK] Arbitraje de conflictos
 * - [ERROR] Nuevos términos no documentados
   - [OK] Proceso de adición definido

----

**Responsable Ideal por Tipo de Proyecto:**

.. list-table::
 :header-rows: 1
 :widths: 30 35 35

 * - **Metodología**
   - **Responsable Ideal**
 - **Razón**
 * - **Scrum**
   - Product Owner
 - Owner del dominio de negocio, decide prioridades
 * - **Kanban**
   - Product Manager / Team Lead
 - Visión holística del sistema
 * - **SAFe**
   - Product Manager (nivel team)
 - Define features y requisitos
 * - **Waterfall**
   - Project Manager
 - Gestiona documentación
 * - **Startup**
   - Tech Lead / CTO
 - Conoce negocio y tecnología
 * - **Open Source**
   - Maintainer Principal
 - Dueño del proyecto

----

**Responsabilidades del Responsable del Glosario:**

**1. Mantenimiento Continuo**

.. code-block:: text

 Tareas semanales:
 +- Revisar nuevos términos mencionados en reuniones
 +- Agregar definiciones para términos aprobados
 +- Actualizar definiciones que cambiaron
 +- Eliminar términos obsoletos

**2. Facilitación de Consenso**

.. code-block:: text

 Cuando hay conflicto sobre definición:

 1. Convocar mini-taller con stakeholders clave
 2. Presentar diferentes interpretaciones
 3. Facilitar discusión
 4. Llegar a consenso
 5. Documentar definición acordada
 6. Comunicar a todos

**3. Evangelización**

.. code-block:: text

 [OK] Promover uso del glosario:

 - Referenciar glosario en reuniones
 - Incluir en onboarding de nuevos
 - Agregar links en documentación
 - Corregir uso inconsistente de términos

**4. Revisión Periódica**

.. code-block:: text

 Cada sprint/mes:
 +- Revisar términos con >30 días sin uso
 +- Validar definiciones con expertos
 +- Buscar gaps (términos no definidos)
 +- Presentar métricas (# términos, adiciones, etc.)

----

**Delegación y Colaboración:**

**El Responsable NO tiene que:**

* [ERROR] Escribir TODAS las definiciones solo
* [ERROR] Ser experto en todos los términos
* [ERROR] Tomar decisiones unilaterales

**El Responsable SÍ debe:**

* [OK] **Coordinar** el proceso de actualización
* [OK] **Facilitar** consenso entre expertos
* [OK] **Asegurar** que glosario se mantenga
* [OK] **Delegar** definiciones a expertos apropiados

**Modelo de Colaboración:**

.. code-block:: text

 Product Owner (Responsable)
 +- Identifica término nuevo: "Circuit Breaker Pattern"
 +- Delega a: Arquitecto de Software
 | +- Arquitecto escribe definición técnica
 | +- Envía propuesta al Product Owner
 +- Product Owner revisa: ¿Es comprensible para negocio?
 +- Si muy técnico -> Pide simplificar
 +- Si OK -> Aprueba y publica
 +- Notifica a equipo

----

**Herramientas para el Responsable:**

.. list-table::
 :header-rows: 1
 :widths: 30 40 30

 * - **Herramienta**
   - **Uso**
 - **Ventaja**
 * - **Confluence**
   - Editar y colaborar
 - Notificaciones automáticas
 * - **Google Sheets**
   - Tracking multi-idioma
 - Fácil compartir
 * - **Notion**
   - Glosario interactivo
 - Búsqueda rápida
 * - **Wiki interna**
   - Documentación centralizada
 - Versionado Git
 * - **JIRA**
   - Crear tickets para definiciones
 - Integrado con workflow

----

**Proceso de Gestión del Glosario:**

**Sprint Planning:**

.. code-block:: text

 Product Owner:
 1. Revisa backlog de términos pendientes
 2. Prioriza top 3-5 para definir este sprint
 3. Asigna a expertos de dominio
 4. Agrega a sprint goals (5-10% capacity)

**Daily Standup:**

.. code-block:: text

 Opcional: Cada Viernes
 "¿Alguien encontró término nuevo esta semana?"
 -> Product Owner lo agrega a backlog

**Sprint Review:**

.. code-block:: text

 Product Owner:
 - Presenta nuevas definiciones agregadas
 - Solicita feedback de stakeholders
 - Actualiza basado en comentarios

**Sprint Retrospective:**

.. code-block:: text

 Revisar:
 - ¿Glosario fue útil este sprint?
 - ¿Qué términos causaron confusión?
 - ¿Proceso de actualización funciona?

----

**Métricas para el Responsable:**

**Dashboard del Glosario:**

.. code-block:: text

 Términos Totales: 27
 +- Agregados este mes: 4
 +- Actualizados este mes: 2
 +- Eliminados este mes: 1
 +- Pendientes de definir: 3

 Uso:
 +- Referencias en docs: 156
 +- Referencias en código comments: 23
 +- Búsquedas último mes: 47

 Calidad:
 +- Términos con >1 sinónimo: 5 [WARNING]
 +- Términos sin ejemplo: 8 [WARNING]
 +- Términos obsoletos (>6 meses sin uso): 2

----

**Ejemplo de RACI para Glosario:**

.. list-table:: RACI Matrix - Glosario
 :header-rows: 1
 :widths: 35 15 15 15 20

 * - **Actividad**
   - **PO**
 - **Arch**
 - **Dev**
 - **Stakeholders**
 * - Identificar nuevos términos
   - A
 - C
 - C
 - C
 * - Escribir definición técnica
   - I
 - R
 - C
 - I
 * - Escribir definición de negocio
   - R
 - C
 - I
 - C
 * - Aprobar definición final
   - A
 - C
 - I
 - C
 * - Publicar y comunicar
   - R
 - I
 - I
 - I
 * - Mantener actualizado
   - A
 - C
 - C
 - I
 * - Revisar periódicamente
   - R
 - C
 - I
 - C

**Leyenda:**
- **R** = Responsible (ejecuta)
- **A** = Accountable (responsable último)
- **C** = Consulted (consultado)
- **I** = Informed (informado)

----

**Señales de que el Glosario Necesita Responsable:**

.. warning::
 **Red Flags (Banderas Rojas):**

 * Glosario no actualizado en >2 meses
 * Nuevos miembros preguntan "¿dónde está el glosario?"
 * Stakeholders usan términos diferentes para mismo concepto
 * Definiciones conflictivas en docs vs código
 * Términos obsoletos aún en glosario
 * Nadie sabe quién puede agregar términos

 **Solución:** Asignar responsable AHORA

----

**Transición de Responsabilidad:**

**Cuando el Responsable Cambia:**

.. code-block:: text

 Handover Checklist:

 [ ] Revisar glosario completo con nuevo responsable
 [ ] Explicar proceso de actualización
 [ ] Transferir accesos a herramientas
 [ ] Presentar backlog de términos pendientes
 [ ] Compartir contactos de expertos de dominio
 [ ] Documentar lecciones aprendidas
 [ ] Programar primera revisión conjunta
 [ ] Anunciar cambio a equipo

**Tiempo estimado de handover:** 2-4 horas

----

**Ejemplo de Anuncio de Responsabilidad:**

.. code-block:: text

 Subject: [TEAM] Sarah es ahora responsable del Glosario

 Hola equipo,

 A partir de hoy, Sarah (Product Owner) es la responsable
 oficial del Glosario del Sistema.

 Esto significa:
 [OK] Sarah coordinará actualizaciones del glosario
 [OK] Si encuentras término nuevo -> notifica a Sarah
 [OK] Si término necesita clarificación -> pregunta a Sarah
 [OK] Sarah facilitará consenso en definiciones

 El glosario está aquí: [link]

 ¡Gracias Sarah por tomar esta responsabilidad!

 - Tech Lead

----

.. seealso::
 * **Tip 12-1** - Tomarse el glosario en serio
 * **Tip 12-2** - Documentar como tabla
 * **Tip 12-5** - Mantener compacto
