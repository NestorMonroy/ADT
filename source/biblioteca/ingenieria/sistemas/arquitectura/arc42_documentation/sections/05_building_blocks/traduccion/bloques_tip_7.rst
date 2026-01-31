.. _bloques_tip_7:




Tip 5-7: ¡Usa tablas para documentar/especificar cajas negras eficientemente!
=============================================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Una manera simple y eficiente de documentar o especificar **cajas negras** son las tablas, como se muestra en las siguientes secciones.




Una manera simple y eficiente de documentar o especificar **cajas negras** son las tablas, como se muestra en las siguientes secciones.

Plantilla Mínima de Caja Negra
==============================

.. list-table:: Plantilla Mínima
   :header-rows: 0
   :widths: 40 60
   
   * - **Propósito/Responsabilidad**
     - <breve descripción del propósito>
   * - **Interfaz(ces)**
     - <breve descripción de interfaz(ces)>

Plantilla Completa de Caja Negra
================================

.. list-table:: Plantilla Completa
   :header-rows: 0
   :widths: 40 60
   
   * - **Propósito/Responsabilidad**
     - <breve descripción del propósito>
   * - **Interfaz(ces)**
     - <breve descripción de interfaz(ces)>
   * - **(Opcional) Características de Calidad/Rendimiento**
     - <breve descripción o enlaces a requisitos de calidad>
   * - **(Opcional) Ubicación de directorio/archivo**
     - Dónde encontrar el código fuente de esta **caja negra**
   * - **(Opcional) Requisitos Cumplidos**
     - <breve descripción o enlaces a documentación de requisitos>
   * - **(Opcional) Problemas Abiertos**
     - <lista de problemas/riesgos conocidos, enlaces a sección 11 de arc42>

Observaciones
=============

* **Interfaces:** Descríbelas solo cuando **no** están extraídas como párrafos separados. Las **interfaces** pueden incluir cualidades y características de rendimiento.

* Las características de **calidad/rendimiento** podrían ser temas como disponibilidad, comportamiento en tiempo de ejecución, flexibilidad o similar.

* **Ubicación de directorio/archivo:** Esto podría ser un solo archivo/directorio, o una lista de fuentes que componen esta **caja negra**.

* Agrega requisitos cumplidos solo si **realmente** necesitas trazabilidad. Es costoso y crea un esfuerzo enorme... Piénsalo dos veces.




.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`seccion_5_1` - Plantilla de caja negra
   * :ref:`bloques_tip_5` - Responsabilidad de cajas negras




:Tip: 5-7
:Tema: Tablas para cajas negras
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
