# Configuracion Codex para Proyecto ADT

Sistema de skills y comandos para asistir en desarrollo del proyecto ADT (Arquitectura Documental de Traduccion).

## Estructura

```
.codex/
+-- config.json - Configuracion del proyecto
+-- skills/ - Skills oficiales (7 skills)
| +-- project-context/
| +-- sphinx-expert/
| +-- translation-workflow/
| +-- validation-suite/
| +-- commit-helper/
| +-- spec-driven-dev/
| +-- work-logger/
+-- commands/ - Comandos complejos (4 comandos)
| +-- sphinx-init-chapter.md
| +-- sphinx-translate-section.md
| +-- sphinx-validate-build.md
| +-- sphinx-analyze-progress.md
+-- README.md - Este archivo
```

## Skills Disponibles

### 1. project-context
Proporciona contexto metodologico completo del proyecto ADT.

CUANDO USAR:
- Entender metodologia ADT
- Conocer frameworks (Diataxis, arc42)
- Comprender estructura del proyecto
- Onboarding de colaboradores

### 2. sphinx-expert
Experto en Sphinx, RST y arquitectura documental.

CUANDO USAR:
- Problemas de build
- Optimizacion de RST
- Configuracion Sphinx
- Troubleshooting

### 3. translation-workflow
Workflow completo de traduccion siguiendo metodologia ADT.

CUANDO USAR:
- Traducir documentos
- Aplicar modos de traduccion
- Generar metadata
- Integrar contenido

### 4. validation-suite
Suite completa de validacion para Sphinx y contenido RST.

CUANDO USAR:
- Antes de commits
- Despues de traducciones
- Validar estructura
- Asegurar calidad

### 5. commit-helper
Ayuda a crear commits siguiendo Conventional Commits.

CUANDO USAR:
- Hacer commits
- Estandarizar mensajes
- Seguir convenciones

### 6. spec-driven-dev
Desarrollo guiado por especificaciones en 4 fases.

CUANDO USAR:
- Features complejas
- Cambios arquitectonicos
- Planificacion estructurada

### 7. work-logger
Sistema de logging estructurado de trabajo.

CUANDO USAR:
- Documentar tareas importantes
- Registrar decisiones
- Mantener historial

## Comandos Disponibles

### 1. sphinx-init-chapter
Inicializa estructura completa de un nuevo capitulo.

USO:
```
sphinx-init-chapter <numero> <nombre> [--framework diataxis|arc42]
```

### 2. sphinx-translate-section
Orquesta proceso completo de traduccion de una seccion.

USO:
```
sphinx-translate-section <url-o-archivo> <destino> [opciones]
```

### 3. sphinx-validate-build
Ejecuta suite completa de validacion.

USO:
```
sphinx-validate-build [--level basic|full|release]
```

### 4. sphinx-analyze-progress
Analiza progreso de traduccion/documentacion del proyecto.

USO:
```
sphinx-analyze-progress [--book <nombre>] [--section <ruta>]
```

## Uso con Codex

Los skills se cargan automaticamente por Codex cuando son relevantes al contexto de la conversacion.

Para invocar un skill manualmente:
```
[En conversacion con Codex]
Usa el skill project-context para explicarme la metodologia ADT
```

Para ejecutar un comando:
```
[En conversacion con Codex]
Ejecuta sphinx-init-chapter 11 nuevos_conceptos
```

## Directorio de Trabajo (.mywork/)

Ubicacion: ADT/.mywork/

Estructura:
```
.mywork/
+-- changes/ - Specs en desarrollo
+-- specs/ - Specs completadas
+-- work-logs/ - Logs de trabajo
 +-- archive/ - Logs archivados
```

NOTA: .mywork/changes/ NO se versiona (trabajo temporal)
 .mywork/specs/ y work-logs/ SI se versionan

## Documentacion

Para detalles completos de cada skill:
- Ver .codex/skills/<nombre>/SKILL.md

Para uso detallado de comandos:
- Ver .codex/commands/<nombre>.md

Para referencias metodologicas:
- Ver .codex/skills/project-context/references/

## Integracion con Proyecto

Este sistema .codex se integra con la estructura existente del proyecto:

SCRIPTS:
- Skills usan scripts existentes en scripts/
- No duplican funcionalidad

DOCUMENTACION:
- Skills referencian docs en source/docs_maestros/
- No duplican contenido

WORKFLOWS:
- Skills codifican workflows de source/02_procedimientos/
- Automatizan procesos manuales

## Reglas del Proyecto

IMPORTANTE: Todo trabajo debe seguir REGLAS_ESTRUCTURA_PROYECTO.rst

REGLA MAESTRA:
- source/ contiene SOLO contenido documental (se compila a HTML)
- Raiz contiene herramientas, scripts, configuraciones

Por eso .codex/ esta en la raiz (es configuracion/herramienta)

## Version

Version: 1.0
Fecha: 2026-01-28
Proyecto: ADT Documentation v1.7.1

## Licencia

Parte del proyecto ADT Documentation.
Uso interno del proyecto.
