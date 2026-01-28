# 🔄 PROPUESTA DE REORGANIZACIÓN COMPLETA DEL PROYECTO ADT
**Basada en Documentos Maestros**  
**Fecha:** 2026-01-26

---

## ✅ DOCUMENTOS MAESTROS COPIADOS

Los 3 documentos maestros ahora están en: `/tmp/ADT/docs_maestros/`

| Documento | Tamaño | Propósito |
|-----------|--------|-----------|
| ARQUITECTURA_DOCUMENTAL_TRADUCCION.md | 19KB | Define estructura metodología (10 secciones) |
| PROMPT_MAESTRO_SPHINX_TRADUCCION.md | 28KB | Prompts de traducción y workflow |
| ESTRUCTURA_DE_BIBLIOTECA.md | 17KB | Organización de libros traducidos |

---

## 🎯 ARQUITECTURA CORRECTA SEGÚN DOCUMENTOS MAESTROS

### Estructura CORRECTA de /tmp/ADT/

```
/tmp/ADT/
│
├── docs_maestros/                       ⭐ DOCUMENTOS FUNDAMENTALES
│   ├── ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
│   ├── PROMPT_MAESTRO_SPHINX_TRADUCCION.md
│   ├── ESTRUCTURA_DE_BIBLIOTECA.md
│   └── README.md
│
├── diataxis/                            Framework documentación por propósito
│   ├── tutorials/                       (Learning-oriented)
│   ├── how_to_guides/                   (Goal-oriented)
│   ├── reference/                       (Information-oriented)
│   └── explanation/                     (Understanding-oriented)
│
├── traduccion/                          Metodología de traducción
│   ├── Makefile
│   ├── make.bat
│   └── source/                          10 secciones según ARQUITECTURA_DOCUMENTAL
│       ├── conf.py
│       ├── index.rst
│       ├── 01_fundamentos/
│       │   ├── index.rst
│       │   ├── glosario_traduccion.rst
│       │   ├── principios_fundamentales.rst
│       │   ├── taxonomias/
│       │   └── metamodelos/
│       ├── 02_procedimientos/
│       │   ├── index.rst
│       │   ├── workflow_general.rst
│       │   ├── modo_alta_fidelidad/
│       │   ├── modo_marcado_visual/
│       │   └── verificacion_calidad/
│       ├── 03_estandares/
│       │   ├── index.rst
│       │   ├── terminologia/
│       │   ├── formato_por_medio/
│       │   └── calidad/
│       ├── 04_reglas_operativas/
│       │   ├── index.rst
│       │   ├── reglas_traduccion/
│       │   ├── escenarios_traduccion/
│       │   └── matrices_decision/
│       ├── 05_herramientas_medios/
│       │   ├── index.rst
│       │   ├── latex/
│       │   ├── sphinx/
│       │   ├── markdown/
│       │   └── equivalencias/
│       ├── 06_casos_practicos/
│       │   ├── index.rst
│       │   ├── antes_despues/
│       │   ├── errores_comunes/
│       │   └── casos_exito/
│       ├── 07_guias_uso/
│       │   ├── index.rst
│       │   ├── guia_rapida.rst
│       │   └── tutorial_completo.rst
│       ├── 08_prompts/
│       │   ├── index.rst
│       │   ├── prompt_maestro_latex.rst
│       │   ├── prompt_maestro_sphinx.rst
│       │   └── prompt_maestro_markdown.rst
│       ├── 09_referencias/
│       │   ├── index.rst
│       │   ├── bibliografia.rst
│       │   └── cheatsheets/
│       └── 10_apendices/
│           ├── index.rst
│           └── historia_versiones.rst
│
├── biblioteca/                          ⭐ TODO EL CONTENIDO TRADUCIDO
│   │
│   ├── _metadata_biblioteca/           Metodología clasificación
│   │   ├── META_BIB_001_Sistema_Clasificacion.rst
│   │   ├── META_BIB_002_Guia_Organizacion.rst
│   │   └── META_BIB_003_Esquema_Codificacion.rst
│   │
│   ├── arc42/                           ⭐ arc42 COMO LIBRO TRADUCIDO
│   │   ├── metadata_libro.rst
│   │   ├── index.rst
│   │   ├── glosario_acumulativo.rst
│   │   │
│   │   └── sections/                    12 secciones de arc42
│   │       ├── 01_introduction_goals/
│   │       │   ├── original/
│   │       │   │   └── section_01.html
│   │       │   ├── traduccion/
│   │       │   │   └── seccion_01_introduccion_objetivos.rst
│   │       │   ├── glosario_seccion.rst
│   │       │   └── notas_traduccion.rst
│   │       │
│   │       ├── 02_constraints/
│   │       │   ├── original/
│   │       │   ├── traduccion/
│   │       │   │   └── seccion_02_restricciones.rst
│   │       │   ├── glosario_seccion.rst
│   │       │   └── notas_traduccion.rst
│   │       │
│   │       ├── 03_context/
│   │       │   ├── original/
│   │       │   ├── traduccion/
│   │       │   │   └── seccion_03_contexto_alcance.rst
│   │       │   ├── glosario_seccion.rst
│   │       │   ├── notas_traduccion.rst
│   │       │   └── diagramas/           ⭐ DiagramasPerfect PlantUML
│   │       │       ├── 01_contexto_simple.puml
│   │       │       ├── 02_contexto_categorizacion.puml
│   │       │       ├── 03_contexto_negocio_tecnico.puml
│   │       │       ├── 04_flujo_datos.puml
│   │       │       ├── 05_dependencias_transitivas.puml
│   │       │       ├── 06_contexto_riesgos.puml
│   │       │       ├── 07_contexto_puertos.puml
│   │       │       └── *.png (imágenes generadas)
│   │       │
│   │       ├── 04_solution_strategy/
│   │       ├── 05_building_blocks/
│   │       ├── 06_runtime/
│   │       ├── 07_deployment/
│   │       ├── 08_concepts/
│   │       ├── 09_decisions/
│   │       ├── 10_quality/
│   │       ├── 11_risks_tech_debt/
│   │       └── 12_glossary/
│   │
│   ├── informatica/                     Categoría: Informática
│   │   ├── programacion/
│   │   │   ├── full_stack/
│   │   │   │   └── Modern_Full_Stack_Development_Zammetti_2ed/
│   │   │   │       ├── metadata_libro.rst
│   │   │   │       ├── index.rst
│   │   │   │       ├── glosario_acumulativo.rst
│   │   │   │       ├── Chapter_01_Server_Side_Action/
│   │   │   │       │   ├── original/
│   │   │   │       │   ├── traduccion/
│   │   │   │       │   ├── glosario_capitulo.rst
│   │   │   │       │   └── figuras/
│   │   │   │       ├── Chapter_02_Advanced_Node_NPM/
│   │   │   │       └── ... (14 capítulos)
│   │   │   │
│   │   │   ├── frontend/
│   │   │   ├── backend/
│   │   │   ├── python/
│   │   │   └── typescript/
│   │   │
│   │   └── inteligencia_artificial/
│   │
│   ├── ingenieria/
│   │   └── sistemas/
│   │
│   └── ciencias/
│       └── biologia/
│
├── scripts/                             Automatización
│   ├── traduccion/
│   ├── build/
│   └── utils/
│
└── config/                              Configuraciones
    ├── sphinx/
    ├── arc42/
    └── templates/
```

---

## 🔄 CAMBIOS PRINCIPALES REQUERIDOS

### 1. Mover arc42 de Raíz a biblioteca/

**ANTES (INCORRECTO):**
```
/tmp/ADT/
├── arc42/                           ❌ En raíz (INCORRECTO)
│   ├── 01_introduction_goals/
│   ├── 02_constraints/
│   └── ...
└── biblioteca/
    └── arc42/                       (vacío)
```

**DESPUÉS (CORRECTO):**
```
/tmp/ADT/
└── biblioteca/
    └── arc42/                       ✅ Dentro de biblioteca
        ├── metadata_libro.rst
        ├── index.rst
        ├── glosario_acumulativo.rst
        └── sections/
            ├── 01_introduction_goals/
            ├── 02_constraints/
            └── 03_context/
```

### 2. Consolidar Traducciones Existentes

**Traducciones actuales en:**
```
/tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/
├── 01/seccion_01_CORRECTA.rst
├── 02/seccion_02_restricciones.rst
└── 03/seccion_03_contexto_alcance.rst
```

**Deben moverse a:**
```
/tmp/ADT/biblioteca/arc42/sections/
├── 01_introduction_goals/traduccion/seccion_01_introduccion_objetivos.rst
├── 02_constraints/traduccion/seccion_02_restricciones.rst
└── 03_context/traduccion/seccion_03_contexto_alcance.rst
```

### 3. Mover Diagramas PlantUML

**Actualmente en:**
```
/tmp/ADT/seccion3_diagramas/
├── 01_contexto_simple.puml
├── ...
└── *.png
```

**Deben moverse a:**
```
/tmp/ADT/biblioteca/arc42/sections/03_context/diagramas/
├── 01_contexto_simple.puml
├── ...
└── *.png
```

### 4. Implementar Estructura de Libro

Cada sección de arc42 debe tener:
```
sections/XX_nombre_seccion/
├── original/
│   └── section_XX.html (contenido original web)
├── traduccion/
│   └── seccion_XX_nombre.rst (traducción)
├── glosario_seccion.rst
├── notas_traduccion.rst
└── diagramas/ (si aplica)
    ├── *.puml
    └── *.png
```

### 5. Crear Metadata de arc42 como Libro

Crear `/tmp/ADT/biblioteca/arc42/metadata_libro.rst`:

```rst
.. meta::
   :libro_id: LIB_ARC42_001
   :tipo: Documentacion_Arquitectonica
   :estado: En_Traduccion
   :progreso: 25%
   :clasificacion: ARC.DOC.ARQ.001

====================================
arc42 - Template de Arquitectura
====================================

Información Bibliográfica
=========================

Título Original
   arc42 Architecture Documentation Template

Título Traducido
   arc42 - Plantilla de Documentación Arquitectónica

Autores
   - Dr. Gernot Starke
   - Dr. Peter Hruschka

Fuente
   https://arc42.org
   https://docs.arc42.org

Idiomas
   - Fuente: Inglés (en)
   - Destino: Español (es-MX)

Clasificación
=============

Código Clasificación
   ARC.DOC.ARQ.001

Categoría Principal
   Arquitectura de Software

Subcategoría
   Documentación

Especialidad
   Templates y Frameworks

Estado de Traducción
====================

Progreso Global
   25% completado (3 de 12 secciones)

Secciones Completadas
   ✅ Section 01: Introduction and Goals
   ✅ Section 02: Constraints
   ✅ Section 03: Context and Scope (con 7 diagramas PlantUML)

Secciones Pendientes
   ⏳ Section 04: Solution Strategy
   ⏳ Section 05: Building Block View
   ⏳ Section 06: Runtime View
   ⏳ Section 07: Deployment View
   ⏳ Section 08: Crosscutting Concepts
   ⏳ Section 09: Architecture Decisions
   ⏳ Section 10: Quality Requirements
   ⏳ Section 11: Risks and Technical Debt
   ⏳ Section 12: Glossary

Fecha Inicio
   2026-01-25

Metodología Aplicada
====================

Workflow
   Alta Fidelidad + Marcado Visual

Formato Destino
   reStructuredText (Sphinx)

Diagramas
   PlantUML (editables)

Referencias
===========

Sitio Oficial
   https://arc42.org

Documentación
   https://docs.arc42.org

Repositorio
   /tmp/ADT/biblioteca/arc42/
```

---

## 📋 PLAN DE REORGANIZACIÓN PASO A PASO

### Fase 1: Preparación (5 min)
```bash
# 1. Crear backup
cd /tmp
tar -czf ADT_backup_$(date +%Y%m%d_%H%M%S).tar.gz ADT/

# 2. Crear nueva estructura en biblioteca/arc42
mkdir -p /tmp/ADT/biblioteca/arc42/sections
cd /tmp/ADT/biblioteca/arc42/sections
mkdir -p {01_introduction_goals,02_constraints,03_context}/{original,traduccion,diagramas}
mkdir -p {04_solution_strategy,05_building_blocks,06_runtime,07_deployment,08_concepts,09_decisions,10_quality,11_risks_tech_debt,12_glossary}/{original,traduccion}
```

### Fase 2: Mover Traducciones (10 min)
```bash
# Mover Sección 1
mv /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/01/seccion_01_CORRECTA.rst \
   /tmp/ADT/biblioteca/arc42/sections/01_introduction_goals/traduccion/seccion_01_introduccion_objetivos.rst

# Mover Sección 2
mv /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/02/seccion_02_restricciones.rst \
   /tmp/ADT/biblioteca/arc42/sections/02_constraints/traduccion/

# Mover Sección 3
mv /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/03/seccion_03_contexto_alcance.rst \
   /tmp/ADT/biblioteca/arc42/sections/03_context/traduccion/
```

### Fase 3: Mover Diagramas (5 min)
```bash
# Mover diagramas PlantUML de Sección 3
mv /tmp/ADT/seccion3_diagramas/*.puml \
   /tmp/ADT/biblioteca/arc42/sections/03_context/diagramas/
   
mv /tmp/ADT/seccion3_diagramas/*.png \
   /tmp/ADT/biblioteca/arc42/sections/03_context/diagramas/
```

### Fase 4: Crear Archivos de Metadata (15 min)
```bash
# Crear metadata_libro.rst (ver contenido arriba)
# Crear index.rst principal
# Crear glosario_acumulativo.rst
# Crear glosario_seccion.rst para cada sección
# Crear notas_traduccion.rst para cada sección
```

### Fase 5: Limpiar Estructuras Antiguas (5 min)
```bash
# Eliminar carpetas vacías/obsoletas
rm -rf /tmp/ADT/arc42  # Carpeta vacía en raíz
rm -rf /tmp/ADT/biblioteca/arc42_documentation  # Estructura antigua
rm -rf /tmp/ADT/seccion3_diagramas  # Ya movidos
```

### Fase 6: Separar Proyectos Independientes (10 min)
```bash
# Mover proyectos independientes fuera de ADT
mkdir -p /tmp/proyectos_independientes
mv /tmp/ADT/arc42_scraper_proxy /tmp/proyectos_independientes/
mv /tmp/ADT/arc42-vagrant /tmp/proyectos_independientes/
mv /tmp/ADT/arc42-vagrant-complete /tmp/proyectos_independientes/
mv /tmp/ADT/backend-modular-v2 /tmp/proyectos_independientes/
```

---

## ✅ VERIFICACIÓN POST-REORGANIZACIÓN

### Checklist de Validación

- [ ] `/tmp/ADT/docs_maestros/` contiene 3 documentos + README
- [ ] `/tmp/ADT/biblioteca/arc42/` existe y contiene:
  - [ ] metadata_libro.rst
  - [ ] index.rst
  - [ ] glosario_acumulativo.rst
  - [ ] sections/ con 12 carpetas
- [ ] Secciones 01-03 tienen:
  - [ ] traduccion/ con archivo .rst
  - [ ] glosario_seccion.rst
  - [ ] notas_traduccion.rst
- [ ] Sección 03 tiene:
  - [ ] diagramas/ con 7 .puml + 7 .png
- [ ] NO existe `/tmp/ADT/arc42/` en raíz
- [ ] NO existe `/tmp/ADT/biblioteca/arc42_documentation/`
- [ ] Proyectos independientes movidos a `/tmp/proyectos_independientes/`

---

## 🎯 PRÓXIMOS PASOS DESPUÉS DE REORGANIZAR

### 1. Continuar Traducción de arc42
- Sección 4: Solution Strategy
- Agregar diagramas PlantUML a cada sección
- Mantener estructura de libro consistente

### 2. Implementar Metodología de Traducción
- Poblar `/tmp/ADT/traduccion/source/` según ARQUITECTURA_DOCUMENTAL
- Migrar prompts a 08_prompts/
- Crear casos prácticos en 06_casos_practicos/

### 3. Compilar Documentación Sphinx
- Setup proyecto Sphinx en `/tmp/ADT/traduccion/`
- Compilar biblioteca de arc42
- Generar HTML de documentación

---

## 📊 IMPACTO DE LA REORGANIZACIÓN

### Antes
- ❌ Contenido mezclado en múltiples ubicaciones
- ❌ arc42 en raíz (conceptualmente incorrecto)
- ❌ No sigue estructura de libro
- ❌ Proyectos independientes mezclados
- ❌ Diagramas separados del contenido

### Después
- ✅ Estructura clara y organizada
- ✅ arc42 en biblioteca/ (conceptualmente correcto)
- ✅ Sigue estructura de libro según docs maestros
- ✅ Proyectos separados apropiadamente
- ✅ Diagramas junto con su sección

---

**Tiempo Estimado Total:** ~50 minutos  
**Dificultad:** Media  
**Reversible:** Sí (mediante backup)

**¿Proceder con la reorganización?**
