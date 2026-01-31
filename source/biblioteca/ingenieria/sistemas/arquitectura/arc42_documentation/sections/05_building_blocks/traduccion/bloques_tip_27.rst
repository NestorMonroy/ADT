.. _bloques_tip_27:




Tip 5-27: ¡Refina solo unos pocos bloques de construcción!
==========================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Los diagramas de **caja blanca** dentro de la **vista de bloques de construcción** forman una estructura de árbol con el diagrama de **contexto** como raíz de esta **jerarquía**.




Los diagramas de **caja blanca** dentro de la **vista de bloques de construcción** forman una estructura de árbol con el diagrama de **contexto** como raíz de esta **jerarquía**.

Este árbol debe ser **parcial**, debes refinar solo algunos de los **bloques de construcción**.

El siguiente diagrama muestra tal árbol parcial: El sistema general se refina en el nivel 1 en **bloques de construcción** ``A``, ``B`` y ``C``.

Solo ``A`` es luego refinado y detallado en el nivel 2.

.. .. figure:: ../figuras/05-refine-only-few-blocks.webp
..       :alt: Refinamiento de solo unos pocos bloques de construcción
..       :align: center
..       :width: 85%
   
..       Árbol parcial: Solo algunos bloques se refinan a niveles más profundos

Principio de Relevancia Sobre Completitud
=========================================

No necesitas refinar todos los **bloques de construcción**:

* **Refina solo lo importante:** Bloques complejos, riesgosos o innovadores
* **Deja lo simple:** Componentes estándar, frameworks conocidos, bloques triviales
* **Enfócate en valor:** Documenta lo que ayuda a entender el sistema
* **Evita redundancia:** No documentes lo obvio o auto-explicativo

Criterios para Decidir Qué Refinar
==================================

**Sí refinar cuando:**

* El **bloque de construcción** es crítico para el sistema
* La **estructura interna** no es obvia
* Hay decisiones arquitectónicas importantes
* Los stakeholders lo necesitan para su trabajo
* Es fuente de riesgos o problemas

**No refinar cuando:**

* Es un componente estándar o framework
* La implementación es simple y directa
* No agrega valor arquitectónico
* Cambiaría frecuentemente (alto mantenimiento)




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_2` - Jerarquía de bloques
   * :ref:`bloques_tip_3` - Nivel 1 es obligatorio




:Tip: 5-27
:Tema: Refinamiento selectivo
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
