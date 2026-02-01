# Procedimiento Backup /tmp - RESUMEN DE DIFERENCIAS vs /mnt

## 🚨 DIFERENCIA CRÍTICA #1: Inclusión Recursiva

**PROBLEMA /tmp**:
\`\`\`
Origen:  /tmp/          ← TODO en /tmp
Destino: /tmp/bk/       ← DENTRO de /tmp
         ↑______↓
         LOOP INFINITO ❌
\`\`\`

**SOLUCIÓN**:
\`\`\`bash
# OBLIGATORIO usar --exclude
tar --exclude=/tmp/bk --exclude=/tmp/bk_temp_* -cf - /tmp/ | xz ...
\`\`\`

**Comparación**:
| Aspecto | Backup /mnt | Backup /tmp |
|---------|-------------|-------------|
| Recursión | ❌ No hay problema | ⚠️ CRÍTICO - requiere exclude |
| Comando | \`tar -cf - /mnt/\` | \`tar --exclude=/tmp/bk -cf - /tmp/\` |
| Riesgo | Bajo | Alto (loop infinito) |

---

## 📋 COMANDOS PRINCIPALES

### Para /mnt (del documento original):
\`\`\`bash
cd / && \\
tar --ignore-failed-read -cf - mnt/ 2>/dev/null | \\
xz -3 -T0 | \\
split -b 49M --numeric-suffixes=1 --suffix-length=3 - "/tmp/bk/MNT_backup_part"
\`\`\`

### Para /tmp (ADAPTADO):
\`\`\`bash
cd / && \\
tar --exclude=/tmp/bk \\
    --exclude=/tmp/bk_temp_* \\
    --ignore-failed-read \\
    -cf - tmp/ 2>/dev/null | \\
xz -3 -T0 | \\
split -b 49M --numeric-suffixes=1 --suffix-length=3 - "/tmp/bk/TMP_backup_part"
\`\`\`

**Diferencias clave**:
1. ✅ Agregado: \`--exclude=/tmp/bk\`
2. ✅ Agregado: \`--exclude=/tmp/bk_temp_*\`
3. ✅ Nombre: TMP_backup_part (no MNT)

---

## ⚠️ PASOS CRÍTICOS ADICIONALES PARA /tmp

### PASO EXTRA: Test de Exclude (antes de crear backup)

\`\`\`bash
# Verificar que exclude funciona
echo "test" > /tmp/bk/test_exclude.txt

# Dry-run
tar --exclude=/tmp/bk -cvf /dev/null /tmp/ 2>&1 | head -50

# Verificar que /tmp/bk NO aparece
APARECE=\$(tar --exclude=/tmp/bk -cvf /dev/null /tmp/ 2>&1 | grep -c "/tmp/bk")

if [ "\$APARECE" -eq "0" ]; then
    echo "✅ Exclude OK - /tmp/bk NO será incluido"
else
    echo "❌ ERROR - /tmp/bk aparece \$APARECE veces - ABORTAR"
    exit 1
fi
\`\`\`

---

## 📝 PROCEDIMIENTO COMPLETO

**Usa el mismo procedimiento que para /mnt, con estos cambios**:

1. **PASO 0 (NUEVO)**: Test de Exclude
   - Verificar que \`--exclude\` funciona
   - Abortar si /tmp/bk aparece en dry-run

2. **PASO 3**: Crear Backup
   - ✅ Agregar \`--exclude=/tmp/bk\`
   - ✅ Agregar \`--exclude=/tmp/bk_temp_*\`

3. **Todos los demás pasos**: Idénticos a /mnt

---

## 🎯 CHECKLIST ESPECÍFICO DE /tmp

Además del checklist de /mnt, verificar:

- [ ] ⭐ PASO 0: Test de Exclude ejecutado
- [ ] ⭐ Verificado que /tmp/bk NO aparece en dry-run
- [ ] ⭐ Comando incluye \`--exclude=/tmp/bk\`
- [ ] ⭐ Durante backup, archivo NO crece sin parar (señal de loop)

---

## 🚨 SEÑALES DE LOOP INFINITO

Si ves esto, **ABORTAR INMEDIATAMENTE (Ctrl+C)**:

1. Archivo de backup crece continuamente sin parar
2. \`du -sh /tmp/bk\` muestra tamaño creciendo rápidamente
3. Espacio en /tmp se llena rápidamente
4. Proceso tar nunca termina

**Solución si ocurre**:
\`\`\`bash
# 1. Detener proceso
Ctrl+C

# 2. Limpiar archivos parciales
rm -rf /tmp/bk/*

# 3. Verificar que comando tiene --exclude
# 4. Reiniciar desde PASO 0
\`\`\`

---

## ✅ RESUMEN

| Aspecto | /mnt | /tmp |
|---------|------|------|
| Comando base | \`tar -cf - /mnt/\` | \`tar --exclude=/tmp/bk -cf - /tmp/\` |
| Riesgo recursión | ❌ No | ⚠️ Sí |
| Test previo | Opcional | **OBLIGATORIO** |
| Complejidad | Baja | Media |
| Pasos extra | 0 | 1 (test exclude) |

**Documento completo**: Sigue procedimiento de /mnt + aplica estas diferencias

---

**Creado**: 2026-02-01  
**Basado en**: PROCEDIMIENTO_backup_mnt_completo.md
