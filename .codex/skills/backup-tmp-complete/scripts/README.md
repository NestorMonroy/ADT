# Backup TMP Scripts

Scripts para crear backup completo de /tmp, dividir en partes, y preparar para descarga.

---

## Uso Rapido

### Proceso Automatico (Recomendado)

```bash
bash backup_complete_auto.sh
```

Ejecuta todo el proceso:
1. Crea backup completo de /tmp
2. Divide en partes de 49MB
3. Genera checksums MD5
4. Verifica integridad
5. Copia a /mnt/user-data/outputs/

**Tiempo total**: 3-5 minutos

---

## Scripts Individuales

### 1. create_backup.sh
Crear backup completo de /tmp en formato tar.gz

```bash
bash create_backup.sh
```

**Output**: `/tmp/bk/tmp-TIMESTAMP-complete.tar.gz`

---

### 2. split_backup.sh
Dividir backup en partes de 49MB

```bash
bash split_backup.sh [prefijo]
```

**Output**: `tmp-TIMESTAMP-part00.tar`, `part01.tar`, ...

---

### 3. generate_checksums.sh
Generar checksums MD5 de las partes

```bash
bash generate_checksums.sh [prefijo]
```

**Output**: `tmp-TIMESTAMP-checksums.md5`

---

### 4. verify_backup.sh
Verificar integridad del backup

```bash
bash verify_backup.sh [prefijo]
```

Verifica:
- Checksums MD5
- Numero de partes
- Tamano total

---

### 5. copy_to_outputs.sh
Copiar backup a outputs para descarga

```bash
bash copy_to_outputs.sh [prefijo]
```

**Output**: Archivos en `/mnt/user-data/outputs/`

---

### 6. restore_backup.sh
Restaurar backup desde partes

```bash
bash restore_backup.sh [prefijo] [directorio_destino]
```

**Ejemplo**:
```bash
bash restore_backup.sh tmp-20260201-175701 /home/user/restored
```

---

## Parametros

**[prefijo]**: Opcional para scripts 2-6
- Si no se proporciona, lee de `/tmp/bk/current_prefix.txt`
- Formato: `tmp-YYYYMMDD-HHMMSS`
- Ejemplo: `tmp-20260201-175701`

---

## Ubicaciones

**Scripts**: `/tmp/ADT/.codex/skills/backup-tmp-complete/scripts/`
**Backups**: `/tmp/bk/`
**Descarga**: `/mnt/user-data/outputs/`

---

## Documentacion Completa

Ver: `../SKILL.md`
