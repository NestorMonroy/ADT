.. _contexto_tip_11:

===============================================================
Tip 3-11: ¡En el contexto de negocio, muestra flujos de datos (en lugar de dependencias)!
===============================================================

.. tip::
   **Consejo de Contexto arc42**
   
   Este tip es válido principalmente para sistemas de información, menos para sistemas de tiempo real, embebidos u orientados a hardware.

----

Estarás usando el **contexto** para discusiones con varios stakeholders, quienes probablemente tendrán habilidades limitadas de modelado y conocimiento limitado (o ¡ninguno!) de UML u otros lenguajes de modelado (formales).

   Intuitivamente, muchas personas entienden una flecha entre sistemas de software como **flujo de datos**.
   Las relaciones UML (dirigidas) como dependencia, asociación, etc. podrían ser bastante confusas para tales individuos.

Por lo tanto: dentro del **contexto**, usa **flujos de datos** invirtiendo la dirección de las flechas usuales de dependencia o llamada de método/servicio de UML.

Nota: este consejo es controversial en algunos equipos, porque explícitamente no cumplimos con la notación UML estándar, y además haciendo eso solo en el contexto.
Sin embargo, encontramos que los **flujos de datos** son a menudo más fáciles de comunicar con stakeholders (no técnicos).

Para los formalistas entre ustedes: usa la flecha de dependencia UML normal punteada y anótala con el estereotipo ``<< flow >>`` para indicarla como flujo de datos y no como un flujo de control.

Para usuarios UML menos puristas: inventa una nueva flecha (por ejemplo, línea sólida con punta de flecha) y declárala - como se sugirió arriba - en la leyenda como flujo de datos.

(Los veteranos de IT reconocen aquí los buenos y viejos diagramas de contexto del análisis estructurado.)

----

.. seealso::
   * :ref:`seccion_3_1` - Contexto de Negocio
   * :ref:`contexto_tip_10` - Diferenciación business/technical

----

:Tip: 3-11
:Tema: Flujos de datos en contexto de negocio
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
