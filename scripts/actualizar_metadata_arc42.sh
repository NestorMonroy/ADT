#!/bin/bash
################################################################################
# Script: actualizar_metadata_arc42.sh
# Versión: 1.0.0
# Descripción: Actualizar metadata del libro arc42 según guía metodológica
# Uso: ./scripts/actualizar_metadata_arc42.sh
################################################################################

set -e

RUTA_ARC42="source/biblioteca/arc42"
METADATA="$RUTA_ARC42/metadata_libro.rst"

echo "════════════════════════════════════════════════════════"
echo "   ACTUALIZAR METADATA ARC42 v1.0.0"
echo "════════════════════════════════════════════════════════"
echo ""

# Verificar que existe
if [ ! -d "$RUTA_ARC42" ]; then
    echo "❌ Error: $RUTA_ARC42 no existe"
    exit 1
fi

# Crear metadata_libro.rst completo
cat > "$METADATA" << 'EOF'
.. meta::
   :libro_id: LIB_ING_ARC_001
   :tipo: Template_Arquitectura
   :estado: En_Traduccion
   :progreso: 25%
   :clasificacion: ING.SIS.ARC.001
   :fecha_inicio: 2026-01-27
   :version: 1.0.0

.. _libro-arc42:

========================================
arc42 Architecture Documentation Template
========================================

Información Bibliográfica
==========================

Título Original
   arc42 Architecture Documentation Template

Título Traducido
   Plantilla de Documentación de Arquitectura arc42

Autor(es)
   Dr. Gernot Starke, Dr. Peter Hruschka

Editorial
   arc42.org

Año de Publicación
   2024 (versión 8.1)

Versión
   8.1

Idiomas
   - Fuente: Inglés (en)
   - Destino: Español (es)

Sitio Web
   https://arc42.org

Licencia
   Creative Commons (CC BY-SA 4.0)

Clasificación según Guía Metodológica
======================================

Código de Clasificación
   ING.SIS.ARC.001
   
   (Ingeniería > Sistemas > Arquitectura > Libro #001)

Categoría Principal
   Ingeniería

Subcategoría
   Sistemas

Especialidad
   Arquitectura de Software

Tipo de Documento
   Template/Framework

Nivel
   Intermedio-Avanzado

Público Objetivo
   - Arquitectos de software
   - Ingenieros de sistemas
   - Desarrolladores senior
   - Technical leads

Palabras Clave
   Arquitectura de software, Documentación técnica, arc42,
   Toma de decisiones, Vistas arquitectónicas, Patrones arquitectónicos,
   Documentación de sistemas

Estado de Traducción
=====================

Progreso Global
   25% completado (3 de 12 secciones principales)

Secciones Completadas
   ✅ Section 01: Introduction and Goals
   ✅ Section 03: Context and Scope
   ✅ Section 05: Building Block View

Secciones En Proceso
   🔄 Section 09: Architecture Decisions

Secciones Pendientes
   ⏳ Section 02: Constraints
   ⏳ Section 04: Solution Strategy
   ⏳ Section 06: Runtime View
   ⏳ Section 07: Deployment View
   ⏳ Section 08: Crosscutting Concepts
   ⏳ Section 10: Quality Requirements
   ⏳ Section 11: Risks and Technical Debt
   ⏳ Section 12: Glossary

Fecha Inicio
   2026-01-27

Fecha Estimada Finalización
   2026-03-15

Última Actualización
   2026-01-27

Equipo de Traducción
====================

Traductor Principal
   Equipo ADT

Revisores Técnicos
   - [Pendiente asignar]

Metodología
   Método Peshitta + ADT Workflow

Procedimientos Aplicados
=========================

- :doc:`/02_procedimientos/workflow_general`
- :doc:`/01_fundamentos/objetivos_tacticas`
- Objetivo principal: Claridad y Consistencia
- Modo: Alta Fidelidad

Características del Template
=============================

arc42 es un template para documentación de arquitectura de software
que consta de 12 secciones principales:

1. **Introduction and Goals** - Requisitos fundamentales
2. **Constraints** - Restricciones del sistema
3. **Context and Scope** - Contexto y alcance
4. **Solution Strategy** - Estrategia de solución
5. **Building Block View** - Vista de bloques de construcción
6. **Runtime View** - Vista de tiempo de ejecución
7. **Deployment View** - Vista de despliegue
8. **Crosscutting Concepts** - Conceptos transversales
9. **Architecture Decisions** - Decisiones arquitectónicas
10. **Quality Requirements** - Requisitos de calidad
11. **Risks and Technical Debt** - Riesgos y deuda técnica
12. **Glossary** - Glosario

Notas de Traducción
====================

Decisiones Importantes
----------------------

1. **Terminología:**
   - "Building Block" → "Bloque de Construcción" (consistente)
   - "Stakeholder" → "Parte Interesada" (español, no anglicismo)
   - "Constraint" → "Restricción" (español estándar)

2. **Estructura:**
   - Mantenemos numeración original (01-12) en metadata
   - Nombres de carpetas sin números (cumple NOM_001)
   - Ejemplo: `01_introduction_goals/` → carpeta `introduction_goals`

3. **Objetivos aplicados:**
   - **Claridad:** Explicaciones adicionales en notas
   - **Consistencia:** Terminología unificada en todas las secciones
   - **Domesticación:** Adaptar ejemplos al contexto hispanohablante

Referencias Externas
====================

- Sitio oficial: https://arc42.org
- Repositorio GitHub: https://github.com/arc42
- Documentación: https://docs.arc42.org

----

**Versión:** 1.0.0  
**Fecha Creación:** 2026-01-27  
**Estado:** En traducción activa
EOF

echo "✅ metadata_libro.rst actualizado"
echo ""
echo "Contenido generado:"
echo "  - Libro ID: LIB_ING_ARC_001"
echo "  - Clasificación: ING.SIS.ARC.001"
echo "  - Progreso: 25% (3/12 secciones)"
echo "  - Estado: En traducción"
echo ""
