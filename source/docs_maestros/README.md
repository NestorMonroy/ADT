# DOCUMENTOS MAESTROS DEL PROYECTO ADT

Esta carpeta contiene los **3 documentos maestros fundamentales** que definen la arquitectura, metodología y organización del proyecto ADT (Arc42-Diátaxis-Traducción).

---

## [LIST] Documentos Incluidos

### 1. ARQUITECTURA_DOCUMENTAL_TRADUCCION.md (19KB)
**Propósito:** Define la estructura documental para procedimientos de traducción técnica.

**Contenido:**
- Estructura completa de 10 secciones para documentar traducción
- 01_fundamentos -> 10_apendices
- Justificación de cada sección
- Mapeo de contenido existente
- Configuración Sphinx recomendada
- Comparación con estructura IACT

**Aplica a:** `/tmp/ADT/traduccion/source/`

---

### 2. PROMPT_MAESTRO_SPHINX_TRADUCCION.md (28KB)
**Propósito:** Prompts de producción para traducción técnica Sphinx.

**Contenido:**
- Workflow completo de traducción (6 pasos)
- Casos de uso identificados (A-E)
- Prompt maestro de configuración inicial
- Prompts condicionales por caso
- Plantillas de verificación y reporte
- Integración con arquitectura IACT

**Aplica a:** Proceso de traducción de cualquier contenido técnico

---

### 3. ESTRUCTURA_DE_BIBLIOTECA_-_Versión_Correcta.md (17KB)
**Propósito:** Define cómo organizar libros traducidos en la biblioteca.

**Contenido:**
- Estructura jerárquica: categoría/subcategoría/especialidad
- Ejemplo completo: Modern Full-Stack Development (Zammetti)
- Estructura por capítulo: original/traducción/glosario/figuras
- Metadata de libro (progreso, clasificación, equipo)
- Glosario acumulativo y por capítulo
- Sistema de códigos de clasificación (ej: INF.PRG.FST.001)

**Aplica a:** `/tmp/ADT/biblioteca/`

---

## [TARGET] Relación entre Documentos

```
ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
 v
 Define: /tmp/ADT/traduccion/source/
 +-- 10 secciones de metodología

PROMPT_MAESTRO_SPHINX_TRADUCCION.md
 v
 Aplica: Proceso de traducción
 +-- Usa metodología de ARQUITECTURA_DOCUMENTAL

ESTRUCTURA_DE_BIBLIOTECA.md
 v
 Define: /tmp/ADT/biblioteca/
 +-- Organización de contenido traducido
 +-- arc42/ (libro traducido)
 +-- informatica/programacion/
 +-- ingenieria/ciencias/
```

---

## [KEY] Conceptos Clave

### arc42 es un "Libro" que están Traduciendo

**IMPORTANTE:** arc42 NO es una carpeta raíz del proyecto, es **contenido traducido** (como un libro técnico) y debe estar en:

```
/tmp/ADT/biblioteca/arc42/
```

### Estructura Correcta del Proyecto

```
/tmp/ADT/
+-- docs_maestros/ <- [STAR] ESTOS DOCUMENTOS
| +-- ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
| +-- PROMPT_MAESTRO_SPHINX_TRADUCCION.md
| +-- ESTRUCTURA_DE_BIBLIOTECA.md
|
+-- diataxis/ <- Framework documentación por propósito
+-- traduccion/ <- Metodología (10 secciones)
+-- biblioteca/ <- TODO el contenido traducido
| +-- arc42/ <- arc42 como libro traducido
+-- scripts/
+-- config/
```

---

## Cómo Usar Estos Documentos

### Paso 1: Leer ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
- Entender las 10 secciones de metodología
- Ver estructura de `/tmp/ADT/traduccion/source/`
- Conocer justificación de cada sección

### Paso 2: Revisar ESTRUCTURA_DE_BIBLIOTECA.md
- Entender cómo organizar libros traducidos
- Ver ejemplo completo (Modern Full-Stack Development)
- Aplicar a arc42 y otros contenidos

### Paso 3: Consultar PROMPT_MAESTRO_SPHINX_TRADUCCION.md
- Al traducir contenido técnico
- Usar workflow de 6 pasos
- Aplicar prompts condicionales según caso

---

## [OK] Próximos Pasos Recomendados

1. **Reorganizar /tmp/ADT/** según arquitectura correcta
2. **Mover arc42** de raíz a `/tmp/ADT/biblioteca/arc42/`
3. **Aplicar estructura de libro** (según ESTRUCTURA_DE_BIBLIOTECA.md)
4. **Implementar metodología** (según ARQUITECTURA_DOCUMENTAL.md)
5. **Usar prompts** para siguientes traducciones

---

## [ALERT] Notas Importantes

### arc42 Debe Estar en biblioteca/

[ERROR] **INCORRECTO:**
```
/tmp/ADT/
+-- arc42/ <- MAL, en raíz
+-- biblioteca/
```

[OK] **CORRECTO:**
```
/tmp/ADT/
+-- biblioteca/
 +-- arc42/ <- BIEN, dentro de biblioteca
 +-- metadata_libro.rst
 +-- index.rst
 +-- sections/
 +-- 01_introduction/
 | +-- original/
 | +-- traduccion/
 | +-- glosario_seccion.rst
 +-- 02_constraints/
 +-- 03_context/
```

### Estructura Similar a Libros Regulares

arc42 se organiza **igual** que cualquier otro libro técnico traducido:
- Metadata de libro
- Capítulos/Secciones con original + traducción
- Glosarios por sección
- Glosario acumulativo
- Progreso de traducción

---

**Creado:** 2026-01-26
**Ubicación:** /tmp/ADT/docs_maestros/
**Propósito:** Guía maestra del proyecto ADT
