.. _notas-traduccion-02-restricciones:

================================================
Notas de Traducción: Sección 02 - Restricciones
================================================

:Sección: 02 - Constraints (Restricciones)
:Fecha: 2026-01-27
:Metodología: Método Peshitta + ADT Workflow v1.2.0
:Fase: FASE 3 - Traducción Inicial

----

Decisiones de Traducción
=========================

Conversiones Markdown -> RST
----------------------------

1. **DIV HTML -> .. note::**

 Original: ``<div class="arc42-example">``
 RST: ``.. note:: **Ejemplo arc42:**``

2. **Enlaces internos -> :ref:**

 Original: ``[tip 2-4](/tips/2-4)``
 RST: ``:ref:`tip-2-4```

3. **Front Matter YAML**

 NO incluir layout/permalink (específicos de Jekyll)
 SÍ incluir tags y category como metadatos

Terminología
------------

**Traducidos:**

- Constraint -> Restricción
- Build tool -> Herramienta de construcción
- Command line -> Línea de comandos
- Management -> Gerencia

**Mantenidos en inglés:**

- Framework (estándar en industria)
- Stakeholder (ampliamente usado)

Correcciones
------------

**Typo corregido:**

Archivo: 2016-03-01-t-2-4.md
Original: "contraints" -> Traducción: "restricciones"

Tácticas Aplicadas
==================

1. **Claridad:** Introducción agregada
2. **Domesticación:** Terminología apropiada
3. **Consistencia:** Glosario de 23 términos

Métricas
========

- Archivos traducidos: 6
- Tiempo FASE 3: ~60 min
- Términos en glosario: 23

Próximos Pasos
==============

- FASE 5: Validación (compilar con Sphinx)
- FASE 6: Revisión
- FASE 7: Publicación

----

:Estado: [OK] FASE 3 COMPLETADA
