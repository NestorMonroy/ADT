---
name: backup-tmp-complete
description: "Sistema generico de backup para cualquier directorio, division en partes de 49MB, verificacion de integridad y restauracion. Organiza backups en subdirectorios segun origen (bk-tmp, bk-mnt, bk-codex)."
version: 2.0.0
created: 2026-02-01
updated: 2026-02-01
---

# Backup Complete - Sistema Generico

**Version**: 2.0.0
**Ubicacion**: `/tmp/ADT/.codex/skills/backup-tmp-complete/`

---

## Descripcion

Sistema generico de backup para cualquier directorio. Crea backups completos, los divide en partes de 49MB, verifica integridad con MD5, y prepara para descarga.

**Mejoras v2.0.0**:
- Generico para cualquier directorio
- Subdirectorios automaticos (bk-tmp, bk-mnt, bk-codex)
- Trigger patterns mejorados
- Decision framework

---

## Trigger Patterns

### Explicitos
- "crea backup de /tmp"
- "haz backup de /mnt"
- "backup de /tmp/ADT/.codex"
- "backup dividido en partes"

### Implicitos
- "voy a limpiar /tmp"
- "necesito preservar directorio"
- "antes de borrar"
- "por si acaso"

### Contextuales
- Usuario habla de "no perder datos"
- Usuario pregunta "como guardo esto"
- Usuario menciona "transferir a otro sistema"

---

## Decision Framework

```
Backup necesario?
  SI → Directorio > 100MB? → SI: Usar este skill
     → Dividir en partes? → SI: Usar este skill
     → Necesita MD5? → SI: Usar este skill
  NO → Usar cp/scp simple
```

---

## Sistema de Subdirectorios

Organizacion automatica:

```
/tmp/bk/
├── bk-tmp/      (backups de /tmp)
├── bk-mnt/      (backups de /mnt)
├── bk-codex/    (backups de /tmp/ADT/.codex)
└── bk-[nombre]/ (basado en basename)
```

---

## Scripts

### 1. create_backup.sh
```bash
bash create_backup.sh [directorio]
```
Crea backup completo de cualquier directorio.

### 2. split_backup.sh
```bash
bash split_backup.sh
```
Divide en partes de 49MB.

### 3. generate_checksums.sh
```bash
bash generate_checksums.sh
```
Genera checksums MD5.

### 4. verify_backup.sh
```bash
bash verify_backup.sh
```
Verifica integridad.

### 5. copy_to_outputs.sh
```bash
bash copy_to_outputs.sh
```
Copia a outputs/.

### 6. restore_backup.sh
```bash
bash restore_backup.sh [prefijo] [destino]
```
Restaura desde partes.

### 7. backup_complete_auto.sh (MAESTRO)
```bash
bash backup_complete_auto.sh [directorio]
```
Proceso completo automatico.

---

## Uso

### Automatico (Recomendado)
```bash
bash backup_complete_auto.sh /tmp
bash backup_complete_auto.sh /mnt
bash backup_complete_auto.sh /tmp/ADT/.codex
```

### Manual
```bash
bash create_backup.sh /directorio
bash split_backup.sh
bash generate_checksums.sh
bash verify_backup.sh
bash copy_to_outputs.sh
```

---

## Casos de Uso

**Backup de /tmp**:
```bash
bash backup_complete_auto.sh /tmp
```
Resultado: `/tmp/bk/bk-tmp/`

**Backup de .codex**:
```bash
bash backup_complete_auto.sh /tmp/ADT/.codex
```
Resultado: `/tmp/bk/bk-codex/`

**Multiples backups**:
```bash
bash backup_complete_auto.sh /tmp
bash backup_complete_auto.sh /mnt
```
Resultado: Subdirectorios separados

---

## Troubleshooting

**Recursion infinita**: Script detecta si intentas backup de /tmp/bk

**Sin espacio**: Verifica `df -h /tmp` antes de ejecutar

**Checksums fallan**: Re-descarga parte corrupta

---

## Changelog

### v2.0.0 - 2026-02-01

**BREAKING CHANGES**:
- Scripts aceptan directorio origen
- Sistema de subdirectorios automaticos

**Nuevas caracteristicas**:
- Generico para cualquier directorio
- Subdirectorios bk-tmp, bk-mnt, bk-codex
- Trigger patterns del system prompt
- Decision framework
- Deteccion recursion infinita

**Scripts actualizados**: Todos (7)

### v1.0.0 - 2026-02-01
- Release inicial
- Solo /tmp
