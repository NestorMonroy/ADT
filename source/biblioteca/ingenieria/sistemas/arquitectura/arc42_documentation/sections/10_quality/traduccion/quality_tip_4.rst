.. _quality_tip_4:

===============================================================
Tip 10-4: ¡Usa el quality tree como checklist!
===============================================================

:Tema: Quality tree como herramienta de verificación
:Palabras clave: quality-tree, thorough, iso-25010

----

Encontrarás una noción ligeramente diferente en :ref:`tip 1-14 (checklist para requisitos de calidad) <goals_tip_14>`.

Usa la claridad de un **quality tree** gráfico (o **mind-map**) para identificar potenciales **brechas** en los **requisitos de calidad**:

Discute **objetivos de calidad** y **requisitos** con tus stakeholders decisivos, preferiblemente en un taller conjunto.

Proceso Paso a Paso
===================

**1. Comienza con algo similar al quality tree de ISO-25010**

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/figuras/01-ISO-25010-EN.webp
   :alt: El quality tree de ISO-25010
   :align: center
   :width: 90%
   
   El quality tree de ISO-25010 como punto de partida

**2. Deja que tus stakeholders creen escenarios de calidad**

Facilita sesiones donde los stakeholders definan **escenarios de calidad** específicos y medibles.

**3. Adjunta esos escenarios a un quality tree específico**

Mapea cada **escenario** a una rama específica del árbol (por ejemplo: **Performance**, **Security**, **Usability**).

**4. Identifica ramas sin escenarios**

En caso de que algunas de las ramas principales de tu árbol no tengan escenarios, eso podría ser un indicador de **escenarios faltantes**.

.. figure:: /biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/10_quality/figuras/10-quality-tree-mindmap-example.png
   :alt: Mind-map como quality tree
   :align: center
   :width: 85%
   
   Ejemplo: ni **scalability**, ni **robustness**, ni **security** tienen escenarios

**5. Decide relevancia con stakeholders**

Deja que tus stakeholders decidan si estos temas no son relevantes o si los **escenarios** correspondientes simplemente están faltando o han sido olvidados.

----

**Beneficios del Enfoque:**

.. list-table::
   :header-rows: 1
   :widths: 40 60
   
   * - Beneficio
     - Descripción
   * - **Identificación de brechas**
     - Revela áreas de calidad sin cobertura
   * - **Completitud sistemática**
     - Asegura que todos los atributos ISO-25010 sean considerados
   * - **Facilitación de talleres**
     - Proporciona estructura para discusiones colaborativas
   * - **Trazabilidad**
     - Mapeo claro entre atributos y escenarios
   * - **Priorización visual**
     - Identifica áreas con muchos vs pocos escenarios

----

**Proceso de Taller Recomendado:**

1. **Preparación** (30 min)
   
   * Imprime quality tree ISO-25010
   * Prepara post-its de colores
   * Invita stakeholders clave

2. **Creación de escenarios** (60 min)
   
   * Cada stakeholder escribe 3-5 **escenarios** críticos
   * Un escenario por post-it
   * Formato: "Como [rol], cuando [situación], entonces [resultado medible]"

3. **Mapeo al árbol** (45 min)
   
   * Pega post-its en ramas apropiadas
   * Identifica clusters (muchos escenarios)
   * Identifica vacíos (cero escenarios)

4. **Análisis de brechas** (30 min)
   
   * ¿Por qué estas ramas no tienen escenarios?
   * ¿Es irrelevante o es gap real?
   * Crear escenarios faltantes si es necesario

5. **Priorización** (30 min)
   
   * Asignar prioridad a cada rama
   * Identificar top 3-5 para sección 1.2
   * Resto va a sección 10

----

.. seealso::
   * **Tip 1-14** - Checklist para requisitos de calidad
   * **Tip 10-3** - Usar mind-map como quality tree
   * **ISO 25010:2023** - Estándar de calidad de software
   * **Sección 10.1** - Resumen de Requisitos de Calidad
