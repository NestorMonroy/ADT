.. _referencias:

===============================================
Referencias y Recursos
===============================================

Documentación de referencia, recursos externos y material complementario.

.. contents:: Contenido
 :depth: 2
 :local:

----

Contenido Disponible
====================

Cheatsheets
-----------

**[OK] Cheatsheet RST**

Referencia rápida completa de reStructuredText.

Ver: :doc:`cheatsheets/cheatsheet_rst`

**Incluye:**
- Encabezados y títulos
- Formato de texto
- Listas, tablas, código
- Enlaces y referencias
- Directivas comunes
- Errores comunes
- Plantillas útiles

Comandos Útiles
---------------

**[OK] Comandos de Terminal**

Comandos más usados en proyectos ADT.

Ver: :doc:`comandos_utiles`

**Incluye:**
- Sphinx (compilación, verificación)
- Git (workflow, branches, historial)
- Búsqueda y análisis
- Pandoc (conversiones)
- Python y pip
- Automatización

Recursos Externos
-----------------

**[OK] Enlaces y Documentación**

Enlaces a recursos oficiales y herramientas externas.

Ver: :doc:`recursos_externos`

**Incluye:**
- Documentación oficial
- Tutoriales y guías
- Herramientas online
- Temas y plantillas
- Hosting y despliegue
- Comunidad y soporte

----

Contenido Planeado
==================

.. code-block:: text

 [RUNNING] Bibliografía completa
 [RUNNING] Glosario de términos técnicos
 [RUNNING] Cheatsheet Sphinx
 [RUNNING] Cheatsheet Git
 [RUNNING] Patrones de documentación
 [RUNNING] Mejores prácticas de escritura técnica

----

Uso de las Referencias
=======================

Durante el Trabajo
------------------

**Mantén abiertas:**

.. code-block:: text

 1. cheatsheet_rst.html
 -> Sintaxis RST rápida

 2. comandos_utiles.html
 -> Comandos frecuentes

 3. FAQ (Sección 07)
 -> Dudas comunes

**Para consultas específicas:**

.. code-block:: text

 ¿Sintaxis RST? -> cheatsheet_rst
 ¿Comando de Git? -> comandos_utiles
 ¿Tutorial externo? -> recursos_externos

Durante el Aprendizaje
-----------------------

**Secuencia recomendada:**

.. code-block:: text

 1. Tutorial ADT (Sección 07)
 2. Cheatsheet RST (esta sección)
 3. Recursos externos (para profundizar)
 4. Práctica con proyectos reales

----

Subsecciones
============

.. toctree::
 :maxdepth: 2

 cheatsheets/index
 comandos_utiles
 recursos_externos

----

Relación con Otras Secciones
=============================

**Referencias COMPLEMENTA:**

* **07_guias_uso** - Referencias durante aprendizaje
* **05_herramientas_medios** - Herramientas específicas
* **10_apendices** - Glosarios y material adicional

**Flujo de uso:**

.. code-block:: text

 DURANTE TRABAJO
 v
 Duda técnica específica
 v
 CONSULTAR REFERENCIAS
 +- cheatsheet_rst (sintaxis)
 +- comandos_utiles (comandos)
 +- recursos_externos (profundizar)
 v
 RESOLVER Y CONTINUAR

----

Estado de Desarrollo
====================

.. list-table::
 :header-rows: 1
 :widths: 40 30 30

 * - **Subsección**
 - **Estado**
 - **Archivos**
 * - **cheatsheets/**
 - [OK] Iniciado
 - cheatsheet_rst [OK]
 * - **comandos_utiles**
 - [OK] Completado
 - 1 archivo [OK]
 * - **recursos_externos**
 - [OK] Completado
 - 1 archivo [OK]
 * - **Otros**
 - [RUNNING] Planeado
 - Pendiente

----

Contribuir Referencias
======================

Si encuentras recursos útiles:

.. code-block:: text

 1. Verifica que el recurso es de calidad
 2. Verifica que el enlace funciona
 3. Categoriza apropiadamente
 4. Agrega descripción breve
 5. Sugiere la adición

**Criterios de inclusión:**

.. code-block:: text

 [OK] Documentación oficial
 [OK] Tutoriales de calidad verificada
 [OK] Herramientas ampliamente usadas
 [OK] Recursos gratuitos o con versión free
 [OK] Enlaces estables (no temporales)

----

.. seealso::
 * :doc:`../07_guias_uso/faq` - Preguntas frecuentes
 * :doc:`../07_guias_uso/troubleshooting` - Solución de problemas
 * :doc:`../10_apendices/glosario_adt` - Glosario ADT

.. note::
 Las referencias se actualizan periódicamente. Última revisión: 2026-01-28.
