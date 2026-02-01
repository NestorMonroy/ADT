# Resumen: Listado Detallado de Issues

**Documento**: LISTADO_DETALLADO_archivos_issues_build_log.md  
**Tamaño**: 553 líneas  
**Fecha**: 2026-02-01

---

## ✅ CONTENIDO DEL DOCUMENTO

### 1. ARCHIVOS CON CRITICAL (5 archivos)

Cada archivo incluye:
- ✅ Nombre del archivo
- ✅ Número de línea del issue
- ✅ Tipo de mensaje (CRITICAL)
- ✅ Mensaje específico de Sphinx
- ✅ **Solución sugerida**

**Ejemplo**:

```markdown
### 1. `source/02_procedimientos/workflow_general.rst`

**Issue 1** - Línea 1363:
- **Tipo**: CRITICAL
- **Mensaje**: Missing matching underline for section title overline.
- **Solución**: Verificar que underline tenga exactamente la misma longitud que el título
```

---

### 2. ARCHIVOS CON ERROR (8+ archivos)

Formato idéntico a CRITICAL:
- Archivo
- Línea
- Mensaje
- **Solución específica** según tipo de error

---

### 3. ARCHIVOS CON WARNING

#### Resumen por tipo:
Lista de todos los tipos de WARNING con conteo:
- "document isn't included in any toctree": X issues
- "Explicit markup ends without a blank line": Y issues
- etc.

#### Top 20 archivos con más WARNING:
Formato simplificado con conteo total por archivo

---

### 4. GUÍA DE SOLUCIONES (⭐ SECCIÓN MÁS ÚTIL)

Guía completa de cómo resolver cada tipo de issue:

#### Para CRITICAL:
- ✅ "Unexpected section title" → Ejemplos de código correcto vs incorrecto
- ✅ "Missing matching underline" → Cómo alinear títulos

#### Para ERROR:
- ✅ "Unexpected indentation" → Reglas de indentación
- ✅ "Malformed table" → Formato correcto de tablas
- ✅ "Could not lex literal_block" → Lexers soportados

#### Para WARNING:
- ✅ "document isn't included in toctree" → Cómo agregar a toctree
- ✅ "Explicit markup ends" → Líneas en blanco requeridas
- ✅ "duplicate label" → Etiquetas únicas

---

### 5. ESTADÍSTICAS FINALES

Tabla resumen:
- Total issues por severidad
- Archivos únicos afectados
- Promedio issues/archivo

---

## 🎯 CÓMO USAR ESTE DOCUMENTO

### Para corregir CRITICAL:
1. Ir a la sección "🔴 ARCHIVOS CON CRITICAL"
2. Encontrar tu archivo
3. Ver línea específica
4. Aplicar solución sugerida
5. Validar con build

### Para entender un tipo de error:
1. Ir a "🔧 GUÍA DE SOLUCIONES"
2. Buscar el tipo de error
3. Ver ejemplos de código correcto vs incorrecto
4. Aplicar el patrón correcto

---

## 📊 DIFERENCIA CON OTRO LISTADO

**LISTADO_archivos_build_log_20260131.md** (463 líneas):
- Lista TODOS los archivos mencionados (386 archivos)
- Organizado por directorio
- Sin detalles de issues
- Útil para: "¿Qué archivos tengo en el proyecto?"

**LISTADO_DETALLADO_archivos_issues_build_log.md** (553 líneas):
- Lista SOLO archivos CON issues
- Incluye mensaje y línea específica
- Incluye **SOLUCIONES** ⭐
- Útil para: "¿Cómo corrijo este CRITICAL en línea 155?"

---

## 💡 RECOMENDACIÓN DE USO

**Flujo de corrección**:

1. Abrir `LISTADO_DETALLADO_archivos_issues_build_log.md`
2. Ir a sección CRITICAL
3. Para cada archivo:
   - Ver línea reportada
   - Leer solución sugerida
   - Aplicar corrección
   - Validar con build
4. Repetir para ERROR
5. Repetir para WARNING más importantes

**No necesitas hacer build para saber qué corregir** - toda la información está en el documento.

---

## ✅ FORMATO DE SOLUCIONES

Todas las soluciones incluyen:

```markdown
# ❌ INCORRECTO
[código que causa el error]

# ✅ CORRECTO
[código que lo soluciona]
```

Con explicación de POR QUÉ está mal y QUÉ hacer.

---

**El documento está listo para usar como guía de corrección.** 🎯
