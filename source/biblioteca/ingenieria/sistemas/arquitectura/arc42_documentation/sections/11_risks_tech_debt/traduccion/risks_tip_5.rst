.. _risks_tip_5:




Tip 11-5: ¡Analiza los datos o estructuras de datos para problemas y riesgos!
=============================================================================

:Tema: Riesgos en datos y estructuras
:Palabras clave: risk, problem




Tanto las **estructuras de datos** *como* el **contenido de datos** pueden ser fuente de **riesgos** o problemas.

Incluso la **distribución**, **replicación**, **backup** o **sincronización** de datos pueden contener **riesgos** o problemas.

Riesgos en Estructuras de Datos
===============================

**1. Esquemas Mal Diseñados**

.. list-table::
 :header-rows: 1
 :widths: 35 35 30

 * - **Problema**
   - **Consecuencia**
   - **Mitigación**
 * - Sin normalización
   - Datos duplicados, inconsistencias
   - Normalizar a 3NF
 * - Over-normalization
   - Queries complejas, performance baja
   - Denormalizar selectivamente
 * - Tipos de datos incorrectos
   - Overflows, pérdida de precisión
   - Revisar tipos (INT vs BIGINT)
 * - Sin constraints
   - Datos inválidos en DB
   - Agregar CHECK constraints
 * - Sin índices
   - Queries lentas
   - Analizar query patterns

**2. Schemas Inflexibles**

* [ERROR] **Schema rígido que requiere migrations para cada cambio**

 *Riesgo: Deployments lentos, downtime*

 **Solución:** Schema-on-read, JSONB columns para datos variables

* [ERROR] **Sin versionado de schema**

 *Riesgo: Rollbacks rompen compatibilidad*

 **Solución:** Schema versioning + backward compatibility




Riesgos en Contenido de Datos
=============================

**1. Calidad de Datos**

.. code-block:: text

 Dimensiones de Calidad de Datos:

 [OK] Exactitud (Accuracy)
 ¿Los datos representan la realidad?
 Ejemplo: Dirección "123 Main St" existe?

 [OK] Completitud (Completeness)
 ¿Están todos los campos necesarios?
 Ejemplo: ¿Email faltante en 30% de usuarios?

 [OK] Consistencia (Consistency)
 ¿Datos coherentes entre sistemas?
 Ejemplo: ¿User ID mismo en DB vs Cache?

 [OK] Actualidad (Timeliness)
 ¿Los datos están actualizados?
 Ejemplo: ¿Precios de hace 6 meses?

 [OK] Validez (Validity)
 ¿Datos cumplen reglas de negocio?
 Ejemplo: ¿Edad negativa? ¿Email sin @?

**2. Datos Sensibles o PII**

* **Datos personales sin encriptar**

 *Riesgo: Violación de GDPR/privacidad*

 **Solución:** Encryption at-rest + at-transit

* **Sin controles de acceso granulares**

 *Riesgo: Acceso no autorizado*

 **Solución:** RBAC + column-level security

* **Logs contienen PII**

 *Riesgo: Exposición en logs, compliance*

 **Solución:** Sanitize logs, no loguear PII




Riesgos en Distribución de Datos
================================

**1. Replicación**

* [WARNING] **Lag de replicación**

 *Problema: Read replicas desactualizadas*

 *Consecuencia: Usuarios ven datos viejos*

* [WARNING] **Split brain en failover**

 *Problema: Dos nodos piensan que son master*

 *Consecuencia: Pérdida de datos, inconsistencia*

**2. Sincronización**

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Patrón**
   - **Riesgo**
 * - Sincronización síncrona
   - Performance: esperar a todos los nodos
 * - Sincronización asíncrona
   - Consistencia: eventual consistency
 * - Sin conflict resolution
   - Datos contradictorios sin resolver
 * - Manual sync
   - Error humano, datos perdidos




Riesgos en Backup y Recovery
============================

**Problemas Comunes:**

.. code-block:: text

 [ERROR] Backups no verificados
 -> Descubres que backup está corrupto cuando lo necesitas

 [ERROR] Sin testing de recovery
 -> RTO estimado: 1h, real: 6h

 [ERROR] Backups solo en misma región
 -> Disaster regional = pérdida total

 [ERROR] Sin backups incrementales
 -> Backups completos toman demasiado tiempo

 [ERROR] Retención insuficiente
 -> Bug introducido hace 8 días, backups solo 7 días

**Estrategia Robusta:**

1. [OK] **3-2-1 Rule**

 * 3 copias de datos
 * 2 tipos de media diferentes
 * 1 copia off-site

2. [OK] **Backup Verification**

 * Restaurar backup en ambiente de test
 * Validar integridad de datos
 * Automatizar verificación semanal

3. [OK] **Recovery Testing**

 * Practicar recovery scenarios
 * Medir RTO/RPO real
 * Documentar runbooks




**Ejemplo de Análisis de Datos:**

.. code-block:: text

 Área: Datos de Usuario

 Estructura:
 +- Riesgo: Emails no validados (20% inválidos)
 | Impacto: Comunicaciones fallan
 | Mitigación: Validación + verificación por email
 |
 +- Riesgo: Sin soft deletes
 | Impacto: Datos borrados permanentemente
 | Mitigación: Implementar deleted_at flag
 |
 +- Riesgo: Contraseñas con hash MD5
 Impacto: Vulnerabilidad de seguridad
 Mitigación: Migrar a bcrypt

 Contenido:
 +- Riesgo: Duplicados (5% usuarios duplicados)
 | Impacto: Métricas incorrectas
 | Mitigación: Dedup script + unique constraints
 |
 +- Riesgo: Datos obsoletos (usuarios inactivos 3+ años)
 Impacto: Compliance (GDPR), storage costs
 Mitigación: Data retention policy + archiving

 Distribución:
 +- Riesgo: DB sin read replicas
 | Impacto: Queries pesadas afectan writes
 | Mitigación: Setup read replicas
 |
 +- Riesgo: Backups solo en región primaria
 Impacto: Desastre regional = pérdida
 Mitigación: Cross-region backup replication




**Checklist de Análisis de Datos:**

.. list-table::
 :header-rows: 1
 :widths: 60 40

 * - **Pregunta**
   - **Acción si NO**
 * - [ ] ¿Hay estrategia de backup automatizada?
   - Implementar backups automáticos
 * - [ ] ¿Se verifican regularmente los backups?
   - Schedule verification tests
 * - [ ] ¿Hay plan de disaster recovery documentado?
   - Crear DR runbook
 * - [ ] ¿Datos sensibles están encriptados?
   - Implementar encryption
 * - [ ] ¿Hay validación de calidad de datos?
   - Agregar data quality checks
 * - [ ] ¿Esquema está versionado?
   - Implementar schema versioning
 * - [ ] ¿Hay monitoring de lag de replicación?
   - Configurar alertas




.. seealso::
 * **Tip 11-4** - Analizar procesos para riesgos
 * **Tip 11-6** - Analizar código fuente para riesgos
 * **Sección 5** - Building Block View (componentes de datos)
 * **Sección 8** - Conceptos Transversales (persistencia)
