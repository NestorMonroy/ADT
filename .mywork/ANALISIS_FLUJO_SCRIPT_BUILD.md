# Análisis de Flujo: Script de Build y Análisis de Sphinx

**Fecha:** 2026-01-31  
**Versión:** 1.0.0  
**Objetivo:** Crear script robusto para build de Sphinx y análisis de warnings/errores

---

## 🎯 Requerimiento del Usuario

Combinar dos comandos:

**Comando 1: Build de Sphinx**
```bash
cd /tmp/ADT && \
make html > .mywork/build-logs/build-fase1-2026-01-30.txt 2>&1 && \
echo "✅ Build completado" && \
tail -20 .mywork/build-logs/build-fase1-2026-01-30.txt
```

**Comando 2: Análisis de Log**
```bash
cd /tmp && \
grep -c "WARNING:" build_output.log && \
grep -c "ERROR:" build_output.log && \
grep -c "CRITICAL:" build_output.log
```

---

## 🚨 PIVOTES IDENTIFICADOS

### PIVOTE #1: Archivos de Log Diferentes ⚠️ CRÍTICO

**Problema:**
- Comando 1 escribe a: `/tmp/ADT/.mywork/build-logs/build-fase1-2026-01-30.txt`
- Comando 2 lee de: `/tmp/build_output.log`

**Impacto:** ¡El análisis leería un archivo DIFERENTE al que se escribió!

**Solución:**
- Usar el MISMO archivo en ambas operaciones
- Unificar el path del log

### PIVOTE #2: Fecha Hardcodeada ⚠️

**Problema:**
- Nombre de archivo: `build-fase1-2026-01-30.txt`
- Fecha fija, no dinámica

**Impacto:**
- Scripts ejecutados en días diferentes sobrescribirán el mismo archivo
- Pérdida de historial de builds

**Solución:**
- Usar timestamp dinámico: `build-fase1-$(date +%Y%m%d-%H%M%S).txt`
- O usar formato de fecha del día actual

### PIVOTE #3: Directorio No Verificado ⚠️

**Problema:**
- Script asume que `.mywork/build-logs/` existe
- No hay verificación ni creación del directorio

**Impacto:**
- Si el directorio no existe, el script fallará
- Error: "No such file or directory"

**Solución:**
- Crear directorio si no existe: `mkdir -p .mywork/build-logs/`

### PIVOTE #4: No Captura stderr ⚠️

**Problema:**
- `2>&1` captura stderr en stdout (correcto)
- Pero si make html falla, no sabemos si el log está completo

**Impacto:**
- Análisis de logs incompleto si build falló

**Solución:**
- Verificar código de salida de make html
- Solo analizar si build fue exitoso

### PIVOTE #5: Paths Relativos vs Absolutos ⚠️

**Problema:**
- Primera parte usa: `cd /tmp/ADT` (absoluto)
- Segunda parte usa: `cd /tmp` (diferente)
- Mezcla de paths relativos y absolutos

**Impacto:**
- Confusión sobre dónde estamos
- Errores si cambiamos de directorio

**Solución:**
- Usar paths absolutos consistentes
- O definir BASE_DIR al inicio

### PIVOTE #6: No Muestra Resultados Claros ⚠️

**Problema:**
- `grep -c` solo muestra números
- No dice qué número corresponde a qué

**Impacto:**
- Output confuso: "3\n0\n1" sin contexto

**Solución:**
- Añadir etiquetas: `echo "WARNING: $(grep -c ...)"` 

### PIVOTE #7: No Maneja Errores ⚠️

**Problema:**
- Si make html falla, continúa ejecutando
- No hay manejo de errores

**Impacto:**
- Análisis de log incorrecto
- No sabemos si build fue exitoso

**Solución:**
- Usar `set -e` o verificar $?
- Exit codes apropiados

### PIVOTE #8: Nombre del Script No Especificado ⚠️

**Problema:**
- No sabemos cómo llamar al script
- No hay convención de nombres

**Impacto:**
- Confusión futura

**Solución:**
- Nombre descriptivo: `build_and_analyze.sh`
- O seguir convención del proyecto

---

## 📊 Análisis de Flujo Propuesto

### Flujo Correcto

```
1. Definir variables de configuración
   ├─ BASE_DIR=/tmp/ADT
   ├─ LOG_DIR=$BASE_DIR/.mywork/build-logs
   ├─ TIMESTAMP=$(date +%Y%m%d-%H%M%S)
   └─ LOG_FILE=$LOG_DIR/build-fase1-$TIMESTAMP.txt

2. Preparar entorno
   ├─ Verificar que BASE_DIR existe
   ├─ Crear LOG_DIR si no existe
   └─ Cambiar a BASE_DIR

3. Ejecutar build
   ├─ make html > $LOG_FILE 2>&1
   ├─ Capturar exit code ($?)
   └─ Verificar si fue exitoso

4. Mostrar confirmación
   ├─ Si exitoso: "✅ Build completado"
   └─ Si falló: "❌ Build falló"

5. Analizar log
   ├─ Contar WARNING
   ├─ Contar ERROR
   └─ Contar CRITICAL

6. Mostrar resultados
   ├─ Resumen de conteos
   ├─ Últimas 20 líneas del log
   └─ Ruta del archivo de log

7. Exit con código apropiado
   ├─ 0 si build exitoso
   └─ 1 si build falló
```

---

## ✅ Flujo Mejorado con Lecciones Aprendidas

### Lecciones de la Metodología v1.2.0

**Lección #1: Documentar Antes de Ejecutar**
- ✅ Este análisis ES la documentación
- ✅ Identificamos pivotes ANTES de codificar

**Lección #2: Protecciones Aplicadas**
- ✅ Protección #1: Verificar directorio existe
- ✅ Protección #4: Validar que build fue exitoso
- ✅ Protección #5: Revisar output antes de continuar

**Lección #3: Un Propósito a la Vez**
- ✅ Script tiene UN propósito claro: build + análisis
- ✅ Separación de concerns: build vs análisis

**Lección #4: Manejo de Errores**
- ✅ Capturar exit codes
- ✅ No continuar si build falló
- ✅ Mensajes claros de error

**Lección #5: Reproducibilidad**
- ✅ Timestamps únicos
- ✅ Logs no se sobrescriben
- ✅ Historial preservado

---

## 🔧 Decisiones de Diseño

### Decisión #1: Nombre del Archivo de Log

**Opciones:**
- A) `build-fase1-YYYY-MM-DD.txt` (fecha fija, 1 por día)
- B) `build-fase1-YYYYMMDD-HHMMSS.txt` (timestamp completo)
- C) `build-latest.txt` (siempre el mismo, se sobrescribe)

**Recomendación:** Opción B
**Razón:** Permite múltiples builds por día, historial completo

### Decisión #2: Qué Hacer Si Build Falla

**Opciones:**
- A) Continuar y analizar log parcial
- B) Detener y no analizar
- C) Analizar pero marcar como fallido

**Recomendación:** Opción C
**Razón:** El log parcial puede tener info útil de diagnóstico

### Decisión #3: Formato de Output

**Opciones:**
- A) Solo números: `3 0 1`
- B) Con etiquetas: `WARNING: 3, ERROR: 0, CRITICAL: 1`
- C) Tabla formateada

**Recomendación:** Opción B o C
**Razón:** Claridad y legibilidad

### Decisión #4: Ubicación del Script

**Propuesto:** `/tmp/ADT/scripts/build_and_analyze.sh`

**Verificar:**
- ✅ Directorio /tmp/ADT/scripts/ existe? → Crear si no
- ✅ Permisos de ejecución? → Añadir con chmod +x
- ✅ Convención de nombres? → Usar snake_case

---

## 📝 Estructura del Script Propuesta

```bash
#!/bin/bash
# Script: build_and_analyze.sh
# Propósito: Build Sphinx + Análisis de WARNING/ERROR/CRITICAL
# Versión: 1.0.0
# Fecha: 2026-01-31

# ============================================================
# CONFIGURACIÓN
# ============================================================
BASE_DIR="/tmp/ADT"
LOG_DIR="$BASE_DIR/.mywork/build-logs"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="$LOG_DIR/build-fase1-$TIMESTAMP.txt"

# ============================================================
# FUNCIONES
# ============================================================
function preparar_entorno() {
    # Verificar BASE_DIR
    # Crear LOG_DIR si no existe
}

function ejecutar_build() {
    # cd a BASE_DIR
    # make html > LOG_FILE 2>&1
    # Capturar exit code
}

function analizar_log() {
    # grep -c WARNING
    # grep -c ERROR
    # grep -c CRITICAL
}

function mostrar_resultados() {
    # Resumen formateado
    # tail -20 del log
    # Path del log
}

# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================
preparar_entorno
ejecutar_build
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Build completado exitosamente"
else
    echo "❌ Build falló con código $EXIT_CODE"
fi

analizar_log
mostrar_resultados

exit $EXIT_CODE
```

---

## ⚠️ Checklist Pre-Creación

Antes de crear el script, verificar:

- [ ] Directorio /tmp/ADT existe
- [ ] Directorio /tmp/ADT/scripts existe (o crear)
- [ ] Directorio .mywork/build-logs existe (o crear en script)
- [ ] Permisos de escritura en .mywork/build-logs
- [ ] make está disponible
- [ ] grep está disponible
- [ ] Decidir nombre final del script
- [ ] Decidir formato de timestamp
- [ ] Decidir qué hacer si build falla

---

## 🎯 Pasos Siguientes

1. **Verificar Pre-Requisitos**
   - Comprobar directorios
   - Comprobar herramientas

2. **Crear Script**
   - Usar estructura propuesta
   - Implementar funciones
   - Añadir manejo de errores

3. **Probar Script**
   - Ejecutar en modo dry-run
   - Verificar que crea logs
   - Verificar análisis correcto

4. **Documentar**
   - Añadir comentarios
   - Crear README si necesario
   - Actualizar .mywork con ejemplo de uso

---

## 📊 Resumen de Pivotes Evitados

| # | Pivote | Gravedad | Solución |
|---|--------|----------|----------|
| 1 | Archivos diferentes | 🔴 CRÍTICO | Unificar path |
| 2 | Fecha hardcodeada | 🟡 MEDIO | Timestamp dinámico |
| 3 | Directorio no verificado | 🟡 MEDIO | mkdir -p |
| 4 | No captura stderr | 🟢 BAJO | Ya capturado con 2>&1 |
| 5 | Paths inconsistentes | 🟡 MEDIO | Usar variables |
| 6 | Output no claro | 🟢 BAJO | Añadir etiquetas |
| 7 | No maneja errores | 🟡 MEDIO | Verificar exit codes |
| 8 | Nombre no especificado | 🟢 BAJO | build_and_analyze.sh |

**Total pivotes identificados:** 8  
**Total pivotes críticos:** 1  
**Total pivotes evitados:** 8 (100%)

---

**Conclusión:** Análisis de flujo completado. Todos los pivotes identificados y soluciones propuestas. Listo para implementación.
