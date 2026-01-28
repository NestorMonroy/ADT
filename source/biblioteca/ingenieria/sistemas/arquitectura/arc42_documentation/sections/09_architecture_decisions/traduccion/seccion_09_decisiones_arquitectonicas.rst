.. meta::
   :category: arc42-doc-section
   :layout: seccion
   :title: 9 - Decisiones
   :permalink: /seccion-9/
   :order: 13

.. _seccion-9:

================================
9. Decisiones de Arquitectura
================================

.. rst-class:: arc42-help

Contenido
=========

Decisiones de arquitectura importantes, costosas, de gran escala o riesgosas, incluyendo su justificación. Con "decisiones" nos referimos a seleccionar una alternativa basándose en criterios dados.

Por favor use su juicio para decidir si una decisión arquitectónica debe documentarse aquí en esta sección central o si es mejor documentarla localmente (por ejemplo, dentro de la plantilla de caja blanca de un bloque de construcción). Evite textos redundantes. Refiérase a la sección 4, donde ya capturó las decisiones más importantes de su arquitectura.

Motivación
==========

Los stakeholders de su sistema deben ser capaces de comprender y rastrear sus decisiones.

Forma
=====

* ADR (`architecture decision record <https://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions>`_) para cada decisión importante
* lista o tabla, ordenada por importancia y consecuencias, o
* más detallado en forma de secciones separadas por decisión

Antecedentes (sobre ADRs)
=========================

Pequeñas piezas de documentación son más fáciles de leer, crear y mantener.
Cuando se trata de decisiones de arquitectura, los equipos de desarrollo a menudo:

* *conocen* la decisión, ya que es visible por ejemplo en el código fuente, pero
* *pierden* la motivación detrás de esa decisión (ver `Nygard 2011 <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>`_)

Por lo tanto, debe documentar algunas decisiones importantes junto con su motivación y razonamiento.

Nuestra propuesta concerniente a las decisiones
================================================

Mantenga una colección de decisiones *arquitectónicamente significativas*,
aquellas decisiones que afectan la estructura, características de calidad, dependencias importantes (especialmente externas) e interfaces, o técnicas de construcción (gracias a Michael Nygard por `esta propuesta <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions>`_).

Podría seguir la estructura Nygard, que funciona de la siguiente manera:

.. list-table:: Estructura Nygard para ADR
   :widths: 20 80
   :header-rows: 1

   * - Sección
     - Descripción
   * - Title (Título)
     - Las decisiones deben tener un nombre apropiado. Por ejemplo, "ADR 42: Patrón Strategy para múltiples algoritmos de verificación" o "ADR 9: Keycloak para gestión de secretos"
   * - Context (Contexto)
     - Describa la situación, incluyendo aspectos técnicos, políticos, sociales y del proyecto. Estas fuerzas podrían estar en tensión.
   * - Decision (Decisión)
     - Cuál es nuestra decisión (*respuesta* a las fuerzas descritas en el contexto)
   * - Status (Estado)
     - Una decisión puede estar "proposed" (propuesta) si los stakeholders importantes aún no han estado de acuerdo con ella, o "accepted" (aceptada) una vez que se acepta. También podría estar "deprecated" (obsoleta) o "superseded" (reemplazada), con suerte con una referencia a su reemplazo.
   * - Consequences (Consecuencias)
     - Qué ocurrirá o puede ocurrir como consecuencia de esta decisión. Todas las consecuencias deben listarse aquí, no solo las "positivas". Una decisión particular puede tener consecuencias positivas, negativas y neutrales, pero todas ellas afectan al equipo y proyecto en el futuro.

Puede encontrar estructuras adicionales de ADR en la `colección de ADR en Github <https://adr.github.io/>`_.

.. toctree::
   :maxdepth: 1
   :caption: Ejemplos
   :glob:

   traduccion/decision_ejemplo_*

.. note::
   **Información adicional**
   
   Para más información sobre decisiones fundamentales de arquitectura y diseño, consulte:
   
   * FAQ de arc42: https://faq.arc42.org/category_c/#c-sec-9

_<describa decisiones importantes de arquitectura aquí>_
