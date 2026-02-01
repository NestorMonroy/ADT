# Actualización: Filtrado en Tiempo Real Durante Build

**Fecha:** 2026-01-31  
**Mejora sugerida por:** Usuario  
**Impacto:** Alto - Cambio significativo en eficiencia

---

## 💡 Mejora Identificada

En lugar de:
```bash
make html > log.txt 2>&1     # Paso 1: Build
grep -c "WARNING:" log.txt    # Paso 2: Análisis
```

Usar:
```bash
make html 2>&1 | tee log.txt | grep -E "WARNING|ERROR|CRITICAL"
```

---

## 🎯 Opciones de Pipeline

### OPCIÓN 1: Filtrado Simple con Resaltado

**Comando:**
```bash
make html 2>&1 | tee "$LOG_FILE" | grep --color=always -E "WARNING|ERROR|CRITICAL|$"
```

**Ventajas:**
- ✅ Muestra SOLO líneas con problemas
- ✅ Resaltado en color
- ✅ Feedback inmediato
- ✅ Guarda log completo

**Desventajas:**
- ⚠️ No muestra conteo total
- ⚠️ No muestra líneas normales (solo problemas)

**Uso:** Cuando solo quieres ver problemas en tiempo real

---

### OPCIÓN 2: Conteo en Tiempo Real con AWK

**Comando:**
```bash
make html 2>&1 | tee "$LOG_FILE" | awk '
/WARNING:/ {w++; print "\033[33m" $0 "\033[0m"}  # Amarillo
/ERROR:/ {e++; print "\033[31m" $0 "\033[0m"}    # Rojo
/CRITICAL:/ {c++; print "\033[35m" $0 "\033[0m"} # Magenta
!/WARNING:|ERROR:|CRITICAL:/ {print}              # Normal
END {
    print "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    print "📊 RESUMEN:"
    print "  WARNING:  " w
    print "  ERROR:    " e  
    print "  CRITICAL: " c
    print "  TOTAL:    " (w+e+c)
}'
```

**Ventajas:**
- ✅ Muestra TODO el output
- ✅ Resalta problemas en color
- ✅ Conteo automático al final
- ✅ Resumen formateado

**Desventajas:**
- ⚠️ Más complejo (AWK)

**Uso:** Cuando quieres ver todo + resumen automático

---

### OPCIÓN 3: Dual Stream (Log + Filtrado)

**Comando:**
```bash
make html 2>&1 | tee "$LOG_FILE" >(grep --color=always -E "WARNING|ERROR|CRITICAL" > "${LOG_FILE%.txt}_filtered.txt")
```

**Ventajas:**
- ✅ Guarda log completo
- ✅ Guarda log filtrado aparte
- ✅ Dos archivos: completo + filtrado

**Desventajas:**
- ⚠️ Crea dos archivos
- ⚠️ No muestra en terminal

**Uso:** Cuando quieres archivos separados para análisis posterior

---

### OPCIÓN 4: Pipeline Completo con Estadísticas

**Comando:**
```bash
make html 2>&1 | tee >(
    awk '
    /WARNING:/ {w++}
    /ERROR:/ {e++}
    /CRITICAL:/ {c++}
    END {
        print w > "/tmp/warnings.count"
        print e > "/tmp/errors.count"
        print c > "/tmp/critical.count"
    }
    ' > /dev/null
) | grep --line-buffered --color=always -E "WARNING|ERROR|CRITICAL|$" | tee "$LOG_FILE"
```

**Ventajas:**
- ✅ Conteos guardados en archivos
- ✅ Output coloreado en tiempo real
- ✅ Log completo guardado

**Desventajas:**
- ⚠️ Muy complejo
- ⚠️ Archivos temporales extra

**Uso:** Para análisis avanzado con scripts posteriores

---

### OPCIÓN 5: Simple y Efectivo (RECOMENDADO)

**Comando:**
```bash
make html 2>&1 | tee "$LOG_FILE" | grep --color=always -E "WARNING:|ERROR:|CRITICAL:|$"
```

Luego al final del script:
```bash
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 RESUMEN DE BUILD:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "WARNING:  $(grep -c 'WARNING:' "$LOG_FILE")"
echo "ERROR:    $(grep -c 'ERROR:' "$LOG_FILE")"
echo "CRITICAL: $(grep -c 'CRITICAL:' "$LOG_FILE")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📄 Log completo: $LOG_FILE"
echo ""
echo "📋 Últimas 20 líneas del log:"
tail -20 "$LOG_FILE"
```

**Ventajas:**
- ✅ Simple de entender
- ✅ Resaltado en tiempo real
- ✅ Resumen al final
- ✅ Log completo guardado
- ✅ Estadísticas precisas

**Desventajas:**
- Ninguna significativa

**Uso:** Balance perfecto entre simplicidad y funcionalidad

---

## 🎨 Ejemplos de Output

### Opción 2 (AWK) - Durante Build:
```
Scanning files... done
Preparing documents... done
WARNING: document isn't included in any toctree
Building documentation...
ERROR: Unknown directive type "code-block"
Done in 2.3 seconds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 RESUMEN:
  WARNING:  3
  ERROR:    1
  CRITICAL: 0
  TOTAL:    4
```

### Opción 5 (Recomendada) - Durante Build:
```
Scanning files... done
Preparing documents... done
WARNING: document isn't included in any toctree    ← (en amarillo)
Building documentation...
ERROR: Unknown directive type "code-block"         ← (en rojo)
Done in 2.3 seconds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 RESUMEN DE BUILD:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WARNING:  3
ERROR:    1
CRITICAL: 0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Log completo: /tmp/ADT/.mywork/build-logs/build-fase1-20260131-105830.txt

📋 Últimas 20 líneas del log:
[últimas 20 líneas aquí]
```

---

## 🏆 Recomendación Final

**USAR OPCIÓN 5**: Simple y Efectivo

**Razón:**
- ✅ Feedback visual inmediato (colores)
- ✅ Log completo guardado
- ✅ Resumen numérico al final
- ✅ Fácil de mantener
- ✅ No requiere AWK complejo

**Pipeline:**
```bash
make html 2>&1 | tee "$LOG_FILE" | grep --color=always -E "WARNING:|ERROR:|CRITICAL:|$"
```

**Post-procesamiento:**
```bash
echo "WARNING:  $(grep -c 'WARNING:' "$LOG_FILE")"
echo "ERROR:    $(grep -c 'ERROR:' "$LOG_FILE")"  
echo "CRITICAL: $(grep -c 'CRITICAL:' "$LOG_FILE")"
```

---

## 📊 Comparación de Performance

| Método | Tiempo Real | Guardado | Conteo | Complejidad |
|--------|-------------|----------|--------|-------------|
| Original (2 pasos) | ❌ | ✅ | ✅ | Bajo |
| Opción 1 (grep) | ✅ | ✅ | ❌ | Bajo |
| Opción 2 (AWK) | ✅ | ✅ | ✅ | Alto |
| Opción 3 (dual) | ❌ | ✅✅ | ❌ | Medio |
| Opción 4 (avanzado) | ✅ | ✅ | ✅ | Muy Alto |
| **Opción 5 (recomendada)** | **✅** | **✅** | **✅** | **Bajo** |

---

## ✅ Conclusión

La sugerencia del usuario de filtrar durante el `make html` es **EXCELENTE** y mejora significativamente el script.

**Implementación recomendada:** Opción 5
- Balance perfecto entre funcionalidad y simplicidad
- Feedback inmediato
- Estadísticas completas
- Fácil de mantener

---

**Próximo paso:** Implementar Opción 5 en el script final.
