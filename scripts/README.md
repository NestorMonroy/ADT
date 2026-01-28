# Scripts de Automatización ADT v1.0.0

Scripts para automatizar el workflow de traducción siguiendo la Guía Metodológica de Clasificación Documental.

## 📋 Índice de Scripts

### 1. init_libro.sh
**Inicializar un libro nuevo en biblioteca/**

```bash
./scripts/init_libro.sh
```

**Qué hace:**
- Solicita información del libro (título, autor, editorial, etc.)
- Calcula clasificación documental automáticamente (CAT.SUB.ESP.NUM)
- Crea estructura completa de directorios
- Genera `metadata_libro.rst` con toda la información
- Genera `index.rst` del libro
- Genera `glosario_acumulativo.rst`

**Ejemplo:**
```
Título: Modern Full Stack Development
Autor: Frank Zammetti
Categoría: informatica
Subcategoría: programacion
Especialidad: full_stack

→ Crea: biblioteca/informatica/programacion/full_stack/
        Modern_Full_Stack_Development_Zammetti_2ed/
→ Código: INF.PRG.FST.001
```

---

### 2. init_capitulo.sh
**Crear estructura de un capítulo nuevo**

```bash
./scripts/init_capitulo.sh <ruta_libro> [nombre_capitulo]
```

**Qué hace:**
- Crea estructura: `original/`, `traduccion/`, `figuras/`, `diagramas/`
- Genera `glosario_capitulo.rst`
- Genera `notas_traduccion.rst` con plantilla
- Genera plantilla de traducción en `traduccion/capitulo.rst`

**Ejemplo:**
```bash
./scripts/init_capitulo.sh biblioteca/arc42 introduction_goals

→ Crea: biblioteca/arc42/introduction_goals/
        ├── original/
        ├── traduccion/capitulo.rst
        ├── figuras/
        ├── diagramas/
        ├── glosario_capitulo.rst
        └── notas_traduccion.rst
```

---

### 3. progreso_libro.sh
**Calcular progreso de traducción**

```bash
./scripts/progreso_libro.sh <ruta_libro>
```

**Qué hace:**
- Cuenta capítulos totales
- Identifica capítulos traducidos
- Calcula porcentaje de progreso
- Muestra barra de progreso visual
- Actualiza `metadata_libro.rst` automáticamente

**Ejemplo:**
```bash
./scripts/progreso_libro.sh biblioteca/arc42

Salida:
  ✅ introduction_goals - Traducido (1 archivos)
  ✅ context_scope - Traducido (1 archivos)
  🔄 solution_strategy - En proceso (sin contenido)
  
  Total: 12 capítulos
  Traducidos: 3
  Progreso: 25%
  [█████░░░░░░░░░░░░░░░] 25%
```

---

### 4. validar_estructura.sh
**Validar conformidad con Guía Metodológica**

```bash
./scripts/validar_estructura.sh <ruta_libro>
```

**Qué hace:**
- Verifica `metadata_libro.rst` existe y tiene campos obligatorios
- Valida que capítulos no tengan números (cumple NOM_001)
- Verifica nomenclatura `snake_case`
- Valida estructura `original/`, `traduccion/`
- Verifica formato de clasificación (XXX.XXX.XXX.NNN)
- Genera reporte detallado

**Ejemplo:**
```bash
./scripts/validar_estructura.sh biblioteca/arc42

Salida (si pasa):
✅ VALIDACIÓN EXITOSA - Sin errores ni advertencias

Salida (si falla):
❌ introduction_goals_01 - tiene números (viola NOM_001)
❌ VALIDACIÓN FALLIDA - 12 errores
```

---

### 5. actualizar_metadata_arc42.sh
**Actualizar metadata específico de arc42**

```bash
./scripts/actualizar_metadata_arc42.sh
```

**Qué hace:**
- Genera `metadata_libro.rst` completo para arc42
- Establece clasificación: ING.SIS.ARC.001
- Establece progreso: 25%
- Agrega toda la información bibliográfica

---

### 6. corregir_nombres_arc42.sh
**Corregir nombres de carpetas de arc42**

```bash
./scripts/corregir_nombres_arc42.sh
```

**Qué hace:**
- Renombra carpetas para cumplir con NOM_001
- Elimina números del inicio
- Preserva orden en metadata
- Ejemplo: `01_introduction_goals` → `introduction_goals`

---

## 🔄 Workflow Típico

### Crear un libro nuevo:

```bash
# 1. Inicializar libro
./scripts/init_libro.sh

# 2. Crear primer capítulo
./scripts/init_capitulo.sh biblioteca/informatica/programacion/python/Python_Essentials_2024 basics_syntax

# 3. [Traducir contenido manualmente]

# 4. Verificar progreso
./scripts/progreso_libro.sh biblioteca/informatica/programacion/python/Python_Essentials_2024

# 5. Validar estructura
./scripts/validar_estructura.sh biblioteca/informatica/programacion/python/Python_Essentials_2024
```

### Trabajar con libro existente:

```bash
# 1. Verificar estado actual
./scripts/progreso_libro.sh biblioteca/arc42

# 2. Validar estructura
./scripts/validar_estructura.sh biblioteca/arc42

# 3. Si hay problemas, corregir
./scripts/corregir_nombres_arc42.sh

# 4. Crear capítulo nuevo
./scripts/init_capitulo.sh biblioteca/arc42 deployment_view

# 5. Verificar progreso después de traducir
./scripts/progreso_libro.sh biblioteca/arc42
```

---

## 📊 Interpretación de Salidas

### progreso_libro.sh

- **✅ Verde**: Capítulo traducido con contenido
- **🔄 Amarillo**: Capítulo con estructura pero sin contenido
- **❌ Rojo**: Capítulo sin traducir

### validar_estructura.sh

- **✅ Verde**: Validación exitosa
- **⚠️ Amarillo**: Advertencias (no críticas)
- **❌ Rojo**: Errores que deben corregirse

---

## 🛠️ Solución de Problemas

### Error: "La ruta no existe"
```bash
# Verificar que estás en la raíz del proyecto
cd /tmp/ADT
./scripts/validar_estructura.sh biblioteca/arc42
```

### Error: "Permiso denegado"
```bash
# Dar permisos de ejecución
chmod +x scripts/*.sh
```

### Error: "Nombres con números"
```bash
# Usar script de corrección
./scripts/corregir_nombres_arc42.sh
```

---

## 📝 Notas Importantes

1. **Siempre ejecutar desde raíz del proyecto** (`/tmp/ADT`)
2. **Nombres de capítulos**: Sin números, en `snake_case`
3. **Validar frecuentemente** con `validar_estructura.sh`
4. **Actualizar progreso** después de cada capítulo traducido

---

## 🔗 Referencias

- Workflow completo: `02_procedimientos/workflow_general.rst`
- Guía Metodológica: `biblioteca/_metadata_biblioteca/`
- Arquitectura: `docs_maestros/ARQUITECTURA_TRADUCCION_IACT.rst`

---

**Versión:** 1.0.0  
**Fecha:** 2026-01-27  
**Estado:** Producción
