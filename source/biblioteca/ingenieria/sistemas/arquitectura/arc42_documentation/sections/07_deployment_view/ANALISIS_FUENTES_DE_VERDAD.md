# ANÁLISIS DE FUENTES DE VERDAD - SECCIÓN 07

**Fecha:** 2026-01-27  
**Análisis:** Determinar fuente de verdad para traducción  

---

## 🎯 PREGUNTA A RESPONDER

¿Cuál es la FUENTE DE VERDAD para cada tipo de documento?

1. Archivo principal de sección
2. Tips individuales
3. Ejemplos

---

## 🔍 ANÁLISIS REALIZADO

### Método

Comparación entre:
- **FUENTE A:** Archivos .md en `/original/`
- **FUENTE B:** docs.arc42.org (lo mostrado por usuario)

### Caso de Estudio: Tip 7-1

**Contenido en docs.arc42.org:**
```markdown
# Tip 7-1: Document your technical infrastructure (hardware)!
 - [#deployment-view](https://docs.arc42.org/search/?t=deployment-view)
 - [#hardware](https://docs.arc42.org/search/?t=hardware)
 - [#infrastructure](https://docs.arc42.org/search/?t=infrastructure)
```

**Contenido en archivo .md:**
```yaml
---
layout: post
title: "Tip 7-1: Document your technical infrastructure (hardware)!"
tags: deployment-view hardware infrastructure
category: deployment
permalink: /tips/7-1/
---
```

---

## 📊 DIFERENCIAS IDENTIFICADAS

### 1. TAGS

| docs.arc42.org | Archivo .md |
|----------------|-------------|
| Tags como LINKS clickeables | Tags en YAML front matter |
| `[#deployment-view](URL)` | `tags: deployment-view hardware` |
| **Renderizado** | **Fuente original** |

### 2. IMÁGENES

| docs.arc42.org | Archivo .md |
|----------------|-------------|
| URLs completas y absolutas | Variable Jekyll |
| `https://docs.arc42.org/images/...` | `{{ site.imageurl }}/...` |
| **Procesado** | **Fuente original** |

### 3. CONTENIDO TEXTUAL

| docs.arc42.org | Archivo .md |
|----------------|-------------|
| Mismo texto exacto | Mismo texto exacto |
| ✅ COINCIDEN | ✅ COINCIDEN |

---

## ✅ CONCLUSIÓN

### Proceso de Publicación

```
Archivos .md (fuente)
         ↓
   Jekyll procesa
         ↓
 Genera HTML/web
         ↓
  docs.arc42.org
   (renderizado)
```

**Los archivos .md son la FUENTE ORIGINAL.**

docs.arc42.org es el **resultado procesado** por Jekyll que:
- Convierte YAML front matter → HTML
- Convierte `tags:` → Links clickeables
- Reemplaza `{{ site.imageurl }}` → URLs completas
- Renderiza Markdown → HTML

---

## 🎯 RESPUESTA A LA PREGUNTA

### ¿Cuál es la FUENTE DE VERDAD para cada tipo?

#### 1. Archivo Principal de Sección

**FUENTE:** Plantilla arc42 proporcionada por usuario

```
7. Deployment view
Content
Motivation
Form
7.1 Infrastructure Level 1
7.2 Infrastructure Level 2
...
```

✅ **Esta es una plantilla específica de arc42, NO está en archivos .md**

#### 2. Tips Individuales

**FUENTE:** ✅ **Archivos .md en `/original/`**

```
/original/2016-03-01-t-7-1.md
/original/2016-03-01-t-7-2.md
...
/original/2016-03-02-t-7-10.md
```

- Contenido completo en .md
- Front matter YAML con metadata
- Imágenes con `{{ site.imageurl }}`
- **NO usar** docs.arc42.org (es solo renderizado)

#### 3. Ejemplos

**FUENTE:** ✅ **Archivos .md en `/original/`**

```
/original/07-deployment-example-tpu-1.md
/original/07-deployment-sample-htmlsc-1.md
/original/07-deployment-sample-tpu-2.md
```

- Contenido completo en .md
- Front matter YAML con metadata
- Imágenes con `{{ site.imageurl }}`
- **NO usar** docs.arc42.org (es solo renderizado)

---

## 📋 RESUMEN FINAL

| Tipo de Documento | Fuente de Verdad | Ubicación | Nota |
|-------------------|------------------|-----------|------|
| **Archivo Principal** | Plantilla arc42 | Usuario proporciona | Documento específico |
| **Tips** | Archivos .md | `/original/*.md` | NO usar docs.arc42.org |
| **Ejemplos** | Archivos .md | `/original/*.md` | NO usar docs.arc42.org |

---

## ⚠️ IMPLICACIONES PARA TRADUCCIÓN

### LO QUE TRADUJE ESTÁ CORRECTO ✅

**Verifiqué mi traducción del Tip 7-1:**

```rst
.. _deployment_tip_1:

Tip 7-1: ¡Documenta tu infraestructura técnica (hardware)!

Describe la infraestructura técnica...
* nodos, es decir, procesadores, servidores...
* relaciones (canales)...
* elementos de hardware adicionales...

.. figure:: ../figuras/07-infrastructure-with-symbols.png

Delegar Documentación de Hardware
==================================

Intenta delegar la documentación de hardware...
```

**Comparación:**

| Elemento | Archivo .md | Mi traducción |
|----------|-------------|---------------|
| Título | "Tip 7-1: Document..." | ✅ "Tip 7-1: ¡Documenta..." |
| Lista nodos | "nodes, i.e. processors..." | ✅ "nodos, es decir, procesadores..." |
| Lista relaciones | "relations (channels)..." | ✅ "relaciones (canales)..." |
| Imagen | `{{ site.imageurl }}/07-...` | ✅ `../figuras/07-...` |
| Sección Delegate | "### Delegate hardware..." | ✅ Sección presente |
| Contenido delegate | "Try to delegate..." | ✅ "Intenta delegar..." |

**TODO el contenido traducido ✅**

---

## 🔍 VERIFICACIÓN CONTRA .md ORIGINAL

### Tips Verificados

**Todos los tips fueron traducidos desde archivos .md:**

✅ Tip 7-1: 26 líneas .md → Traducido completo
✅ Tip 7-2: 21 líneas .md → Traducido completo  
✅ Tip 7-3: 19 líneas .md → Traducido completo
✅ Tip 7-4: 14 líneas .md → Traducido completo
✅ Tip 7-5: 23 líneas .md → Traducido completo
✅ Tip 7-6: 15 líneas .md → Traducido completo
✅ Tip 7-7: 26 líneas .md → Traducido completo
✅ Tip 7-8: 18 líneas .md → Traducido completo
✅ Tip 7-9: 57 líneas .md → Traducido completo
✅ Tip 7-10: 21 líneas .md → Traducido completo

### Ejemplos Verificados

✅ TPU 1: 63 líneas .md → Traducido completo
✅ HTML SC: 41 líneas .md → Traducido completo
✅ TPU 2: 26 líneas .md → Traducido completo

---

## ✅ CONCLUSIÓN FINAL

### Fuentes de Verdad Confirmadas:

1. **Archivo Principal:** Plantilla arc42 (proporcionada por usuario)
2. **Tips:** Archivos .md en `/original/` ✅
3. **Ejemplos:** Archivos .md en `/original/` ✅

### Estado de Traducción:

✅ **TODO traducido correctamente desde fuentes .md**
✅ **Archivo principal actualizado con plantilla completa**
✅ **NO hay conflicto con docs.arc42.org** (es solo renderizado)

### El "bucle" NO era necesario

**El problema NO era la fuente:**
- Usé la fuente correcta (.md files)
- Traduje TODO el contenido

**El problema ERA el archivo principal:**
- NO leí la plantilla arc42 completa
- Omití secciones 7.1, 7.2, Content, etc.
- Ya corregido ✅

---

## 📝 LECCIÓN APRENDIDA

**NO hay dos fuentes en conflicto.**

Solo hay una fuente (archivos .md) y múltiples formas de verla:
- **Fuente original:** Archivos .md (markdown + YAML)
- **Renderizado web:** docs.arc42.org (HTML procesado)

**Para traducción:** SIEMPRE usar archivos .md originales.

---

**Documento:** ANALISIS_FUENTES_DE_VERDAD.md  
**Fecha:** 2026-01-27  
**Conclusión:** Archivos .md son fuente de verdad para tips y ejemplos