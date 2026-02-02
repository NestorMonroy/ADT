---
name: backup-tmp
description: "Procedimiento completo para crear, dividir, verificar y restaurar backups de /tmp. Incluye scripts automatizados para backup en partes de 49MB."
version: 1.0.0
created: 2026-02-01
updated: 2026-02-01
---

# Backup TMP - Procedimiento Completo

**Version**: 1.0.0
**Ubicacion**: `/tmp/ADT/.codex/skills/backup-tmp/`
**Scripts**: `/tmp/ADT/scripts/backup/`

---

## Cuando usar

- Necesitas backup completo de /tmp
- Dividir backup grande en partes descargables
- Verificar integridad de backup dividido
- Restaurar backup desde partes

---

## Trigger Patterns

### Senales Explicitas

- Usuario dice: "crea backup de /tmp"
- Usuario dice: "backup completo"
- Usuario menciona: "dividir en partes"
- Usuario pide: "backup descargable"

### Senales Implicitas

- Usuario quiere preservar trabajo temporal
- Usuario va a limpiar /tmp
- Usuario necesita transferir archivos grandes
- Antes de reinstalar o actualizar sistema

---

## Prerequisitos

1. Espacio disponible en disco (minimo 2x el tamano de /tmp)
2. Permisos de escritura en destino
3. tar, gzip, split, md5sum instalados
4. Directorio /tmp/bk para backups (se crea automaticamente)

---

## Procedimiento Completo

### FASE 1: Crear Backup Completo

**Objetivo**: Crear archivo tar.gz de todo /tmp excluyendo /tmp/bk

**Script**: `scripts/backup/crear_backup_completo.sh`

**Uso manual**:
```bash
cd /tmp
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
PREFIX="tmp-${TIMESTAMP}"

tar --exclude='/tmp/bk' \
    --ignore-failed-read \
    --warning=no-file-changed \
    -czf /tmp/bk/${PREFIX}-complete.tar.gz \
    /tmp
```

**Parametros**:
- `--exclude='/tmp/bk'`: Excluir directorio de backups
- `--ignore-failed-read`: Continuar si archivos cambian
- `--warning=no-file-changed`: No advertir cambios durante backup
- `-czf`: Crear, comprimir gzip, archivo

**Output**:
- `/tmp/bk/tmp-YYYYMMDD-HHMMSS-complete.tar.gz`

**Tamano esperado**: 
- Original: ~844 MB
- Comprimido: ~550 MB

---

### FASE 2: Dividir en Partes

**Objetivo**: Dividir backup grande en partes de 49MB para descarga

**Script**: `scripts/backup/dividir_backup.sh`

**Uso manual**:
```bash
cd /tmp/bk
PREFIX="tmp-20260201-175701"

split -b 49M -d ${PREFIX}-complete.tar.gz ${PREFIX}-part

# Renombrar partes
for file in ${PREFIX}-part*; do
  mv "$file" "${file}.tar"
done
```

**Parametros**:
- `-b 49M`: Tamano de cada parte (49 megabytes)
- `-d`: Usar sufijos numericos (00, 01, 02...)

**Output**:
- `tmp-YYYYMMDD-HHMMSS-part00.tar` (49 MB)
- `tmp-YYYYMMDD-HHMMSS-part01.tar` (49 MB)
- ...
- `tmp-YYYYMMDD-HHMMSS-partNN.tar` (ultimo, variable)

**Numero de partes**: Depende del tamano, aproximadamente:
- 550 MB / 49 MB = ~12 partes

---

### FASE 3: Generar Checksums

**Objetivo**: Crear archivo MD5 para verificar integridad

**Script**: `scripts/backup/generar_checksums.sh`

**Uso manual**:
```bash
cd /tmp/bk
PREFIX="tmp-20260201-175701"

md5sum ${PREFIX}-part*.tar > ${PREFIX}-checksums.md5
```

**Output**:
- `tmp-YYYYMMDD-HHMMSS-checksums.md5`

**Contenido del archivo**:
```
b193a9b374aae91697e860404ff59079  tmp-20260201-175701-part00.tar
d9ac582a7eb5d6eea460540de31a4302  tmp-20260201-175701-part01.tar
...
```

---

### FASE 4: Crear README

**Objetivo**: Documentar el backup para restauracion

**Script**: `scripts/backup/crear_readme.sh`

**Contenido minimo**:
- Fecha de creacion
- Numero de partes
- Tamano total
- Instrucciones de restauracion
- Checksums

**Output**:
- `tmp-YYYYMMDD-HHMMSS-README.md`

---

### FASE 5: Verificar Backup

**Objetivo**: Confirmar integridad de todas las partes

**Script**: `scripts/backup/verificar_backup.sh`

**Uso manual**:
```bash
cd /tmp/bk
PREFIX="tmp-20260201-175701"

# Verificar checksums
md5sum -c ${PREFIX}-checksums.md5

# Verificar numero de partes
EXPECTED=12
ACTUAL=$(ls ${PREFIX}-part*.tar | wc -l)
if [ "$ACTUAL" -eq "$EXPECTED" ]; then
  echo "OK: Todas las partes presentes"
else
  echo "ERROR: Faltan partes"
fi
```

**Verificaciones**:
1. Checksums MD5 correctos
2. Numero de partes completo
3. Tamano total esperado

---

### FASE 6: Copiar a Outputs

**Objetivo**: Hacer disponible para descarga

**Script**: `scripts/backup/copiar_outputs.sh`

**Uso manual**:
```bash
cd /tmp/bk
PREFIX="tmp-20260201-175701"

# Copiar todas las partes
for file in ${PREFIX}-part*.tar; do
  cp "$file" /mnt/user-data/outputs/
done

# Copiar auxiliares
cp ${PREFIX}-checksums.md5 /mnt/user-data/outputs/
cp ${PREFIX}-README.md /mnt/user-data/outputs/
```

**Resultado**:
- Todas las partes en `/mnt/user-data/outputs/`
- Listas para descarga

---

## Restauracion (Usuario final)

### Paso 1: Descargar Archivos

Descargar TODOS los archivos:
- Todas las partes (.tar)
- Archivo checksums (.md5)
- README (opcional)

### Paso 2: Verificar Integridad

```bash
md5sum -c tmp-YYYYMMDD-HHMMSS-checksums.md5
```

Todas deben mostrar "OK".

### Paso 3: Reconstruir Archivo

```bash
cat tmp-YYYYMMDD-HHMMSS-part*.tar > tmp-complete.tar.gz
```

### Paso 4: Extraer

```bash
mkdir -p tmp-restored
tar -xzf tmp-complete.tar.gz -C tmp-restored
```

Contenido en: `tmp-restored/tmp/`

---

## Scripts Disponibles

### 1. crear_backup_completo.sh

**Funcion**: Crear backup tar.gz de /tmp
**Input**: Ninguno (usa timestamp automatico)
**Output**: `/tmp/bk/tmp-TIMESTAMP-complete.tar.gz`

**Uso**:
```bash
bash scripts/backup/crear_backup_completo.sh
```

---

### 2. dividir_backup.sh

**Funcion**: Dividir backup en partes de 49MB
**Input**: Ruta al archivo .tar.gz
**Output**: Multiples archivos .tar

**Uso**:
```bash
bash scripts/backup/dividir_backup.sh /tmp/bk/tmp-TIMESTAMP-complete.tar.gz
```

---

### 3. generar_checksums.sh

**Funcion**: Crear archivo MD5 de checksums
**Input**: Prefijo del backup
**Output**: Archivo .md5

**Uso**:
```bash
bash scripts/backup/generar_checksums.sh tmp-20260201-175701
```

---

### 4. crear_readme.sh

**Funcion**: Generar README del backup
**Input**: Prefijo del backup, numero de partes
**Output**: Archivo README.md

**Uso**:
```bash
bash scripts/backup/crear_readme.sh tmp-20260201-175701 12
```

---

### 5. verificar_backup.sh

**Funcion**: Verificar integridad del backup
**Input**: Prefijo del backup
**Output**: Reporte de verificacion

**Uso**:
```bash
bash scripts/backup/verificar_backup.sh tmp-20260201-175701
```

---

### 6. copiar_outputs.sh

**Funcion**: Copiar backup a outputs para descarga
**Input**: Prefijo del backup
**Output**: Archivos en /mnt/user-data/outputs/

**Uso**:
```bash
bash scripts/backup/copiar_outputs.sh tmp-20260201-175701
```

---

### 7. backup_completo_automatico.sh

**Funcion**: Ejecutar todo el proceso automaticamente
**Input**: Ninguno
**Output**: Backup completo listo para descarga

**Uso**:
```bash
bash scripts/backup/backup_completo_automatico.sh
```

Este script ejecuta todas las fases:
1. Crear backup completo
2. Dividir en partes
3. Generar checksums
4. Crear README
5. Verificar integridad
6. Copiar a outputs

---

## Flujo de Trabajo Recomendado

### Opcion A: Automatico (Recomendado)

```bash
# Un solo comando hace todo
bash scripts/backup/backup_completo_automatico.sh
```

### Opcion B: Manual (Control total)

```bash
# FASE 1: Crear backup
bash scripts/backup/crear_backup_completo.sh

# FASE 2: Dividir
bash scripts/backup/dividir_backup.sh /tmp/bk/tmp-TIMESTAMP-complete.tar.gz

# FASE 3: Checksums
bash scripts/backup/generar_checksums.sh tmp-TIMESTAMP

# FASE 4: README
bash scripts/backup/crear_readme.sh tmp-TIMESTAMP 12

# FASE 5: Verificar
bash scripts/backup/verificar_backup.sh tmp-TIMESTAMP

# FASE 6: Copiar
bash scripts/backup/copiar_outputs.sh tmp-TIMESTAMP
```

---

## Casos de Uso

### Caso 1: Backup antes de limpiar /tmp

```bash
# Crear backup automatico
bash scripts/backup/backup_completo_automatico.sh

# Limpiar /tmp
rm -rf /tmp/*

# Restaurar si necesario
# (seguir instrucciones de restauracion)
```

---

### Caso 2: Backup para transferir a otro sistema

```bash
# Crear backup dividido
bash scripts/backup/backup_completo_automatico.sh

# Descargar archivos de outputs/
# Transferir a otro sistema
# Restaurar siguiendo procedimiento
```

---

### Caso 3: Backup selectivo (solo ciertos archivos)

```bash
# Modificar crear_backup_completo.sh para incluir solo:
tar --include='/tmp/ADT/*' \
    --include='/tmp/*.md' \
    -czf backup-selectivo.tar.gz /tmp
```

---

## Troubleshooting

### Problema: Backup muy grande

**Sintoma**: Archivo .tar.gz > 1 GB

**Solucion**:
```bash
# Reducir tamano de partes
split -b 25M  # En vez de 49M
```

---

### Problema: Checksums no coinciden

**Sintoma**: md5sum -c falla para una parte

**Solucion**:
1. Identificar parte corrupta
2. Re-descargar solo esa parte
3. Verificar nuevamente

---

### Problema: Faltan archivos al restaurar

**Sintoma**: Menos archivos de los esperados

**Solucion**:
1. Verificar que todas las partes esten presentes
2. Verificar checksums antes de unir
3. Revisar que no haya errores al unir partes

---

### Problema: No hay espacio en disco

**Sintoma**: Error durante creacion de backup

**Solucion**:
```bash
# Verificar espacio
df -h /tmp

# Limpiar archivos no necesarios
rm -rf /tmp/archivos-viejos

# O usar otro destino
tar -czf /mnt/otro-disco/backup.tar.gz /tmp
```

---

## Metricas de Ejemplo

Basado en backup real (2026-02-01):

- Archivos totales: 16,261
- Tamano original: 844 MB
- Tamano comprimido: 550 MB
- Ratio compresion: 65% (35% de reduccion)
- Partes generadas: 12
- Tiempo creacion: ~2 minutos
- Tiempo division: ~30 segundos
- Tiempo verificacion: ~10 segundos

---

## Notas Importantes

### Exclusiones

El backup excluye automaticamente:
- `/tmp/bk/` (directorio de backups)

Para excluir otros directorios, modificar en scripts:
```bash
tar --exclude='/tmp/bk' \
    --exclude='/tmp/otro-dir' \
    ...
```

### Compresion

Se usa gzip (nivel default) por:
- Rapidez (mas rapido que xz)
- Compatibilidad universal
- Balance compresion/velocidad

Para maxima compresion:
```bash
tar -cJf  # xz (mas lento, mas compresion)
```

### Tamano de Partes

49 MB elegido por:
- Compatible con limites de descarga
- No demasiadas partes
- Facil de transferir

Ajustar segun necesidades.

---

## Referencias

**Scripts**: `scripts/backup/`
**Ejemplos**: Ver backups en `/tmp/bk/`
**Logs**: Cada script genera output descriptivo

---

## Changelog

### v1.0.0 - 2026-02-01
- Version inicial
- 7 scripts creados
- Procedimiento completo documentado
- Basado en backup exitoso de /tmp (16,261 archivos)

---

## Workflow Completo (Diagrama)

```
INICIO
  |
  v
Crear backup completo (/tmp -> .tar.gz)
  |
  v
Dividir en partes (49MB cada una)
  |
  v
Generar checksums MD5
  |
  v
Crear README con instrucciones
  |
  v
Verificar integridad
  |
  v
Copiar a outputs/ para descarga
  |
  v
FIN (Backup listo)
```

---

## Ejemplo Completo

```bash
# Ejecutar backup automatico
bash scripts/backup/backup_completo_automatico.sh

# Output esperado:
# [FASE 1] Creando backup completo...
# [FASE 2] Dividiendo en partes...
# [FASE 3] Generando checksums...
# [FASE 4] Creando README...
# [FASE 5] Verificando integridad...
# [FASE 6] Copiando a outputs...
# 
# BACKUP COMPLETO:
#   Prefijo: tmp-20260201-175701
#   Partes: 12
#   Tamano: 550 MB
#   Ubicacion: /mnt/user-data/outputs/
#   Archivos: 14 (12 partes + checksums + README)
```
