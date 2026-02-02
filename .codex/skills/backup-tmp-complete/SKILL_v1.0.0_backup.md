---
name: backup-tmp-complete
description: "Procedimiento completo para crear backup de /tmp, dividirlo en partes de 49MB, verificar integridad y preparar para descarga. Incluye scripts automatizados y procedimiento de restauracion."
version: 1.0.0
created: 2026-02-01
updated: 2026-02-01
---

# Backup TMP Complete

**Version**: 1.0.0
**Ubicacion**: `/tmp/ADT/.codex/skills/backup-tmp-complete/`
**Scripts**: `/tmp/ADT/.codex/skills/backup-tmp-complete/scripts/`

---

## Descripcion

Skill para crear backups completos de /tmp, dividirlos en partes descargables de 49MB, verificar integridad con checksums MD5, y preparar para descarga o restauracion.

---

## Cuando usar

- Necesitas backup completo de /tmp
- Quieres dividir backup grande en partes descargables
- Necesitas verificar integridad de backup
- Vas a limpiar /tmp y necesitas preservar contenido
- Necesitas transferir contenido de /tmp a otro sistema

---

## Trigger Patterns

### Senales Explicitas
- Usuario dice: "crea backup de /tmp"
- Usuario dice: "backup completo de todo /tmp"
- Usuario menciona: "dividir backup en partes"
- Usuario pide: "backup descargable"
- Usuario dice: "backup todo /tmp"

### Senales Implicitas
- Usuario va a limpiar /tmp
- Usuario necesita preservar trabajo temporal
- Usuario necesita transferir archivos grandes
- Usuario menciona reinstalacion o actualizacion

---

## Prerequisitos

1. Espacio en disco: Minimo 2x el tamano de /tmp
2. Permisos: Acceso de lectura a /tmp, escritura a /tmp/bk
3. Herramientas: tar, gzip, split, md5sum
4. Sistema: Linux (probado en Ubuntu 24)

---

## Scripts Disponibles

### 1. create_backup.sh
**Funcion**: Crear backup completo de /tmp en formato tar.gz
**Input**: Ninguno (usa timestamp automatico)
**Output**: `/tmp/bk/tmp-TIMESTAMP-complete.tar.gz`
**Tiempo estimado**: 2-3 minutos

**Uso**:
```bash
bash create_backup.sh
```

**Caracteristicas**:
- Excluye automaticamente /tmp/bk
- Ignora errores de lectura (archivos cambiando)
- Guarda prefijo generado en current_prefix.txt
- Compresion gzip (balance velocidad/tamano)

---

### 2. split_backup.sh
**Funcion**: Dividir backup completo en partes de 49MB
**Input**: Prefijo del backup (opcional, lee de current_prefix.txt)
**Output**: Multiples archivos .tar (part00, part01, ...)
**Tiempo estimado**: 30 segundos

**Uso**:
```bash
bash split_backup.sh [prefijo]
```

**Ejemplos**:
```bash
# Usar prefijo automatico
bash split_backup.sh

# Especificar prefijo
bash split_backup.sh tmp-20260201-175701
```

**Caracteristicas**:
- Divide en partes de exactamente 49MB
- Ultima parte puede ser menor
- Guarda contador de partes en archivo
- Renombra automaticamente a formato .tar

---

### 3. generate_checksums.sh
**Funcion**: Generar checksums MD5 de todas las partes
**Input**: Prefijo del backup
**Output**: Archivo .md5 con checksums
**Tiempo estimado**: 10 segundos

**Uso**:
```bash
bash generate_checksums.sh [prefijo]
```

**Caracteristicas**:
- Un checksum por cada parte
- Formato estandar md5sum
- Permite verificacion con md5sum -c

---

### 4. verify_backup.sh
**Funcion**: Verificar integridad del backup completo
**Input**: Prefijo del backup
**Output**: Reporte de verificacion
**Tiempo estimado**: 15 segundos

**Uso**:
```bash
bash verify_backup.sh [prefijo]
```

**Verificaciones**:
- Checksums MD5 de todas las partes
- Numero de partes completo
- Tamano total

---

### 5. copy_to_outputs.sh
**Funcion**: Copiar backup a /mnt/user-data/outputs para descarga
**Input**: Prefijo del backup
**Output**: Archivos en outputs/
**Tiempo estimado**: 30 segundos

**Uso**:
```bash
bash copy_to_outputs.sh [prefijo]
```

**Copia**:
- Todas las partes (.tar)
- Archivo de checksums (.md5)
- README si existe

---

### 6. restore_backup.sh
**Funcion**: Restaurar backup desde partes descargadas
**Input**: Prefijo del backup, directorio destino (opcional)
**Output**: Contenido restaurado
**Tiempo estimado**: 5-10 minutos

**Uso**:
```bash
bash restore_backup.sh [prefijo] [directorio_destino]
```

**Ejemplo**:
```bash
bash restore_backup.sh tmp-20260201-175701 /home/user/restored
```

**Proceso**:
1. Verifica checksums MD5
2. Reconstruye archivo completo
3. Crea directorio destino
4. Extrae contenido
5. Verifica archivos restaurados

---

### 7. backup_complete_auto.sh (Script Maestro)
**Funcion**: Ejecutar todo el proceso automaticamente
**Input**: Ninguno
**Output**: Backup completo listo para descarga
**Tiempo estimado**: 3-5 minutos

**Uso**:
```bash
bash backup_complete_auto.sh
```

**Fases ejecutadas**:
1. Crear backup completo
2. Dividir en partes
3. Generar checksums
4. Verificar integridad
5. Copiar a outputs

**RECOMENDADO**: Usar este script para proceso completo automatico

---

## Procedimiento Completo

### Opcion A: Automatico (Recomendado)

```bash
cd /tmp/ADT/.codex/skills/backup-tmp-complete/scripts
bash backup_complete_auto.sh
```

**Resultado**: Backup completo en outputs/ listo para descargar

---

### Opcion B: Manual (Paso a Paso)

**PASO 1: Crear backup completo**
```bash
cd /tmp/ADT/.codex/skills/backup-tmp-complete/scripts
bash create_backup.sh
```

**PASO 2: Dividir en partes**
```bash
bash split_backup.sh
```

**PASO 3: Generar checksums**
```bash
bash generate_checksums.sh
```

**PASO 4: Verificar integridad**
```bash
bash verify_backup.sh
```

**PASO 5: Copiar a outputs**
```bash
bash copy_to_outputs.sh
```

---

## Restauracion (Usuario Final)

### Desde el sistema donde se descargaron las partes

**PASO 1: Verificar que tienes todos los archivos**
```bash
ls tmp-YYYYMMDD-HHMMSS-part*.tar
ls tmp-YYYYMMDD-HHMMSS-checksums.md5
```

**PASO 2: Restaurar**
```bash
bash restore_backup.sh tmp-YYYYMMDD-HHMMSS /path/to/restore
```

**PASO 3: Verificar contenido**
```bash
ls -la /path/to/restore/tmp/
find /path/to/restore/tmp -type f | wc -l
```

---

### Restauracion manual (sin script)

**PASO 1: Verificar checksums**
```bash
md5sum -c tmp-YYYYMMDD-HHMMSS-checksums.md5
```

**PASO 2: Unir partes**
```bash
cat tmp-YYYYMMDD-HHMMSS-part*.tar > tmp-complete.tar.gz
```

**PASO 3: Extraer**
```bash
mkdir -p tmp-restored
tar -xzf tmp-complete.tar.gz -C tmp-restored
```

**Contenido**: `tmp-restored/tmp/`

---

## Estructura de Archivos

### Durante el proceso (en /tmp/bk/)

```
/tmp/bk/
├── tmp-YYYYMMDD-HHMMSS-complete.tar.gz    (backup completo)
├── tmp-YYYYMMDD-HHMMSS-part00.tar         (parte 1)
├── tmp-YYYYMMDD-HHMMSS-part01.tar         (parte 2)
├── ...
├── tmp-YYYYMMDD-HHMMSS-partNN.tar         (parte N)
├── tmp-YYYYMMDD-HHMMSS-checksums.md5      (checksums)
├── tmp-YYYYMMDD-HHMMSS-parts_count.txt    (numero de partes)
└── current_prefix.txt                      (prefijo actual)
```

### Para descarga (en outputs/)

```
/mnt/user-data/outputs/
├── tmp-YYYYMMDD-HHMMSS-part00.tar
├── tmp-YYYYMMDD-HHMMSS-part01.tar
├── ...
├── tmp-YYYYMMDD-HHMMSS-partNN.tar
├── tmp-YYYYMMDD-HHMMSS-checksums.md5
└── tmp-YYYYMMDD-HHMMSS-README.md (si existe)
```

---

## Comandos Base

### Crear backup completo
```bash
tar --exclude='/tmp/bk' \
    --ignore-failed-read \
    --warning=no-file-changed \
    -czf /tmp/bk/tmp-TIMESTAMP-complete.tar.gz \
    /tmp
```

### Dividir en partes de 49MB
```bash
split -b 49M -d backup.tar.gz backup-part
```

### Generar checksums MD5
```bash
md5sum backup-part* > checksums.md5
```

### Verificar checksums
```bash
md5sum -c checksums.md5
```

### Unir partes
```bash
cat backup-part* > backup-complete.tar.gz
```

### Extraer backup
```bash
tar -xzf backup-complete.tar.gz -C /destino
```

---

## Metricas de Referencia

Basado en backup real ejecutado el 2026-02-01:

**Input**:
- Archivos en /tmp: 16,261
- Tamano original: 844 MB
- Directorios: Todos excepto /tmp/bk

**Output**:
- Tamano comprimido: 550 MB
- Ratio compresion: 65% (35% reduccion)
- Partes generadas: 12
- Tamano parte: 49 MB (11 MB ultima)

**Tiempos**:
- Creacion backup: 2 minutos
- Division partes: 30 segundos
- Generacion checksums: 10 segundos
- Verificacion: 10 segundos
- Copia a outputs: 30 segundos
- Total: 3-4 minutos

---

## Troubleshooting

### ERROR: No hay espacio en disco

**Sintoma**: Error durante creacion de backup

**Solucion**:
```bash
# Verificar espacio disponible
df -h /tmp

# Limpiar archivos no necesarios antes de backup
rm -rf /tmp/archivos-viejos
```

---

### ERROR: Checksums no coinciden

**Sintoma**: md5sum -c falla para una o mas partes

**Solucion**:
1. Identificar que parte fallo
2. Re-generar solo esa parte:
   ```bash
   # Si parte 03 esta corrupta
   dd if=backup-complete.tar.gz of=backup-part03 \
      bs=49M skip=3 count=1
   ```
3. Verificar nuevamente

---

### ERROR: Faltan partes al restaurar

**Sintoma**: No se pueden unir las partes

**Solucion**:
1. Verificar numero de partes:
   ```bash
   ls backup-part* | wc -l
   ```
2. Comparar con numero esperado
3. Re-descargar partes faltantes

---

### ADVERTENCIA: Backup muy grande

**Sintoma**: Backup > 1 GB

**Opciones**:
1. Reducir tamano de partes:
   ```bash
   split -b 25M  # En vez de 49M
   ```
2. Backup selectivo:
   ```bash
   tar --include='/tmp/importante/*' -czf backup.tar.gz /tmp
   ```

---

## Notas Tecnicas

### Exclusiones

El backup excluye automaticamente:
- `/tmp/bk/` - Directorio donde se guardan los backups

Para excluir otros directorios, modificar create_backup.sh:
```bash
tar --exclude='/tmp/bk' \
    --exclude='/tmp/otro-dir' \
    ...
```

### Compresion

Se usa gzip (nivel default) porque:
- Velocidad: Mas rapido que xz o bzip2
- Compatibilidad: Universal en sistemas Linux
- Balance: Buen ratio compresion/velocidad

Para maxima compresion (mas lento):
```bash
tar -cJf backup.tar.xz /tmp  # xz compresion
```

### Tamano de Partes

49 MB elegido por:
- Descarga: Compatible con limites de descarga
- Manejo: No demasiadas partes
- Transferencia: Facil de enviar

Ajustar en split_backup.sh si necesario.

### Checksums MD5

MD5 usado (no SHA256) por:
- Velocidad: Mas rapido de calcular
- Compatibilidad: Disponible en todos los sistemas
- Proposito: Detectar corrupcion (no seguridad)

Para mayor seguridad, usar SHA256:
```bash
sha256sum backup-part* > checksums.sha256
```

---

## Casos de Uso

### Caso 1: Backup antes de limpiar /tmp

```bash
# Crear backup
bash backup_complete_auto.sh

# Limpiar /tmp (excluyendo backup)
find /tmp -mindepth 1 -not -path '/tmp/bk*' -delete

# Restaurar si necesario mas tarde
```

---

### Caso 2: Transferir trabajo a otro sistema

```bash
# En sistema origen
bash backup_complete_auto.sh

# Descargar todas las partes
# Transferir a sistema destino

# En sistema destino
bash restore_backup.sh tmp-YYYYMMDD-HHMMSS /home/user/trabajo
```

---

### Caso 3: Backup periodico automatizado

```bash
# Agregar a crontab
0 2 * * * cd /tmp/ADT/.codex/skills/backup-tmp-complete/scripts && bash backup_complete_auto.sh
```

---

### Caso 4: Backup selectivo de ciertos archivos

Modificar create_backup.sh para incluir solo lo necesario:

```bash
tar --include='/tmp/ADT/*' \
    --include='/tmp/*.md' \
    --include='/tmp/*.log' \
    -czf backup-selectivo.tar.gz /tmp
```

---

## Verificacion Post-Backup

Despues de crear el backup, verificar:

```bash
# 1. Numero de partes
ls /tmp/bk/tmp-*-part*.tar | wc -l

# 2. Checksums correctos
bash verify_backup.sh

# 3. Archivos en outputs
ls -lh /mnt/user-data/outputs/tmp-*

# 4. Tamano total
du -ch /mnt/user-data/outputs/tmp-* | tail -1
```

---

## Referencias

**Ubicacion scripts**: `.codex/skills/backup-tmp-complete/scripts/`
**Directorio backups**: `/tmp/bk/`
**Directorio outputs**: `/mnt/user-data/outputs/`

**Herramientas**:
- tar: Empaquetado y compresion
- split: Division en partes
- md5sum: Verificacion integridad
- gzip: Compresion

---

## Changelog

### v1.0.0 - 2026-02-01

**Release inicial**:
- 7 scripts creados
- Procedimiento completo documentado
- Basado en backup exitoso de 16,261 archivos
- Scripts probados y funcionales
- Documentacion completa

**Scripts incluidos**:
1. create_backup.sh - Crear backup
2. split_backup.sh - Dividir partes
3. generate_checksums.sh - Checksums MD5
4. verify_backup.sh - Verificar integridad
5. copy_to_outputs.sh - Copiar descarga
6. restore_backup.sh - Restaurar backup
7. backup_complete_auto.sh - Proceso automatico

---

## Workflow Visual

```
[INICIO]
    |
    v
[create_backup.sh]
    |
    v
/tmp/bk/tmp-TIMESTAMP-complete.tar.gz
    |
    v
[split_backup.sh]
    |
    v
tmp-TIMESTAMP-part00.tar
tmp-TIMESTAMP-part01.tar
...
tmp-TIMESTAMP-partNN.tar
    |
    v
[generate_checksums.sh]
    |
    v
tmp-TIMESTAMP-checksums.md5
    |
    v
[verify_backup.sh]
    |
    v
[Integridad OK?]
    |
    +-- No --> [ERROR: Revisar]
    |
    +-- Si
        |
        v
[copy_to_outputs.sh]
        |
        v
/mnt/user-data/outputs/
        |
        v
[LISTO PARA DESCARGA]
```

---

## Ejemplo de Ejecucion Completa

```bash
# Ir al directorio de scripts
cd /tmp/ADT/.codex/skills/backup-tmp-complete/scripts

# Ejecutar proceso automatico
bash backup_complete_auto.sh

# Output esperado:
# ============================================
#   BACKUP COMPLETO AUTOMATICO DE /tmp
# ============================================
#
# [FASE 1/5] Creando backup completo...
# Prefijo: tmp-20260201-180530
# Backup completo creado
# Tamano: 550M
#
# [FASE 2/5] Dividiendo en partes de 49MB...
# Total de partes: 12
#
# [FASE 3/5] Generando checksums MD5...
# Checksums generados
#
# [FASE 4/5] Verificando integridad...
# Todos los checksums correctos
# Todas las partes presentes
#
# [FASE 5/5] Copiando a outputs...
# Partes copiadas: 12
# Archivos totales: 14
#
# ============================================
#   BACKUP COMPLETADO EXITOSAMENTE
# ============================================
#
# Prefijo: tmp-20260201-180530
# Partes generadas: 12
# Tamano total: 550M
```
