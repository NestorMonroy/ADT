#!/usr/bin/env python3
"""
Script para remover emojis e iconos de todos los archivos en .codex

Uso:
    python remove_emojis.py [--dry-run] [--no-backup] [--path .codex]
"""

import re
import os
import sys
import argparse
from pathlib import Path
import shutil
from datetime import datetime

# Tabla de reemplazos según referencia
EMOJI_REPLACEMENTS = {
    # Completado
    '✅': '[OK]',
    '✓': '[OK]',
    '☑': '[OK]',
    '✔': '[OK]',
    
    # Error
    '❌': '[ERROR]',
    '✗': '[FAIL]',
    '☒': '[FAIL]',
    '✘': '[FAIL]',
    
    # Advertencia
    '⚠️': '[WARNING]',
    '⚠': '[WARNING]',
    '⚡': '[WARNING]',
    '⛔': '[WARNING]',
    
    # Información
    'ℹ️': '[INFO]',
    'ℹ': '[INFO]',
    '💡': '[INFO]',
    '📢': '[INFO]',
    
    # Depuración
    '🐛': '[DEBUG]',
    '🔍': '[DEBUG]',
    
    # En proceso
    '⏳': '[RUNNING]',
    '🔄': '[PROCESSING]',
    '⌛': '[WAITING]',
    
    # Esperando
    '⏰': '[PENDING]',
    '⏱️': '[PENDING]',
    '⏱': '[PENDING]',
    
    # Inicio
    '🚀': '[START]',
    '▶️': '[START]',
    '▶': '[START]',
    
    # Fin
    '🏁': '[END]',
    '⏹️': '[STOP]',
    '⏹': '[STOP]',
    
    # Archivo
    '📁': 'DIRECTORY:',
    '📄': 'FILE:',
    '💾': 'FILE:',
    '📃': 'FILE:',
    
    # Carpeta
    '📂': 'DIRECTORY:',
    '🗂️': 'DIRECTORY:',
    '🗂': 'DIRECTORY:',
    
    # Red
    '🌐': '[NETWORK]',
    '📡': '[NETWORK]',
    
    # Usuario
    '👤': 'USER:',
    '👥': 'USERS:',
    
    # Tiempo
    '🕐': 'TIME:',
    
    # Fecha
    '📅': 'DATE:',
    '🗓️': 'DATE:',
    '🗓': 'DATE:',
    
    # Símbolos de check/cross adicionales
    '☐': '[ ]',
    '☑️': '[OK]',
    '☒️': '[FAIL]',
    
    # Otros emojis comunes en documentación
    '📦': '[PACKAGE]',
    '📋': '[LIST]',
    '📊': '[TABLE]',
    '📈': '[CHART]',
    '📉': '[CHART]',
    '🎯': '[TARGET]',
    '🎓': '[LEARN]',
    '🎉': '',  # Celebración - eliminar
    '🔗': '[LINK]',
    '🔑': '[KEY]',
    '🔒': '[LOCKED]',
    '🔓': '[UNLOCKED]',
    '💻': '[COMPUTER]',
    '⚙️': '[CONFIG]',
    '⚙': '[CONFIG]',
    '🛠️': '[TOOLS]',
    '🛠': '[TOOLS]',
    '📝': '[NOTE]',
    '✏️': '[EDIT]',
    '✏': '[EDIT]',
    '🗑️': '[DELETE]',
    '🗑': '[DELETE]',
    '⭐': '[STAR]',
    '🌟': '[STAR]',
    '💭': '[COMMENT]',
    '💬': '[COMMENT]',
    '📌': '[PIN]',
    '📍': '[LOCATION]',
    '🎨': '[DESIGN]',
    '🖼️': '[IMAGE]',
    '🖼': '[IMAGE]',
    '🔧': '[TOOL]',
    '🔨': '[BUILD]',
    '⚡️': '[FAST]',
    '🚨': '[ALERT]',
    '🔔': '[NOTIFICATION]',
    '📣': '[ANNOUNCE]',
    '🎭': '[MASK]',
    '🏷️': '[TAG]',
    '🏷': '[TAG]',
    
    # Flechas
    '→': '->',
    '←': '<-',
    '↑': '^',
    '↓': 'v',
    '⇒': '=>',
    '⇐': '<=',
    '➜': '->',
    '➡': '->',
    '⬆': '^',
    '⬇': 'v',
    '⬅': '<-',
    
    # Caracteres especiales de checkbox
    '🗹': '[X]',
    
    # Box drawing que podrían ser problemáticos (mantener algunos para tablas)
    '═': '=',
    '║': '|',
    '╔': '+',
    '╗': '+',
    '╚': '+',
    '╝': '+',
    '╠': '+',
    '╣': '+',
    '╦': '+',
    '╩': '+',
    '╬': '+',
    '─': '-',
    '│': '|',
    '┌': '+',
    '┐': '+',
    '└': '+',
    '┘': '+',
    '├': '+',
    '┤': '+',
    '┬': '+',
    '┴': '+',
    '┼': '+',
}

# Patrones de regex para detectar emojis Unicode restantes
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    "]+",
    flags=re.UNICODE
)


class EmojiRemover:
    def __init__(self, base_path, dry_run=False, backup=True, verbose=True):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.backup = backup
        self.verbose = verbose
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'emojis_replaced': 0,
            'backups_created': 0,
        }
        self.changes_log = []
        
    def log(self, message, level='INFO'):
        """Log mensaje con nivel"""
        if self.verbose:
            print(f"[{level}] {message}")
        self.changes_log.append(f"[{level}] {message}")
    
    def create_backup(self, file_path):
        """Crear backup de archivo"""
        if not self.backup or self.dry_run:
            return None
            
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = file_path.parent / f"{file_path.name}.backup_{timestamp}"
        
        shutil.copy2(file_path, backup_path)
        self.stats['backups_created'] += 1
        self.log(f"Backup creado: {backup_path.name}", 'DEBUG')
        return backup_path
    
    def replace_emojis(self, content, file_path):
        """Reemplazar emojis en contenido"""
        original_content = content
        replacements_made = []
        
        # Primero, reemplazos de la tabla
        for emoji, replacement in EMOJI_REPLACEMENTS.items():
            if emoji in content:
                count = content.count(emoji)
                content = content.replace(emoji, replacement)
                replacements_made.append(f"  {repr(emoji)} -> {replacement} ({count} veces)")
                self.stats['emojis_replaced'] += count
        
        # Luego, eliminar cualquier emoji Unicode restante
        remaining_emojis = EMOJI_PATTERN.findall(content)
        if remaining_emojis:
            unique_emojis = set(remaining_emojis)
            content = EMOJI_PATTERN.sub('', content)
            for emoji in unique_emojis:
                replacements_made.append(f"  {repr(emoji)} -> [REMOVED]")
                self.stats['emojis_replaced'] += 1
        
        # Limpiar múltiples espacios
        content = re.sub(r'  +', ' ', content)
        content = re.sub(r' +\n', '\n', content)
        
        # Log cambios si hubo
        if replacements_made and self.verbose:
            self.log(f"Cambios en {file_path.name}:")
            for rep in replacements_made:
                self.log(rep, 'DEBUG')
        
        return content, len(replacements_made) > 0
    
    def process_file(self, file_path):
        """Procesar un archivo individual"""
        self.stats['files_processed'] += 1
        
        try:
            # Leer contenido
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Reemplazar emojis
            new_content, modified = self.replace_emojis(content, file_path)
            
            if modified:
                self.stats['files_modified'] += 1
                
                if self.dry_run:
                    self.log(f"[DRY-RUN] Se modificaría: {file_path.relative_to(self.base_path)}")
                else:
                    # Crear backup
                    self.create_backup(file_path)
                    
                    # Escribir nuevo contenido
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    self.log(f"[MODIFIED] {file_path.relative_to(self.base_path)}")
                    
        except Exception as e:
            self.log(f"Error procesando {file_path.name}: {e}", 'ERROR')
    
    def process_directory(self):
        """Procesar todos los archivos en directorio"""
        if not self.base_path.exists():
            self.log(f"Error: Directorio no existe: {self.base_path}", 'ERROR')
            return False
        
        print("="*70)
        self.log(f"Iniciando proceso en: {self.base_path}", 'INFO')
        self.log(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCION'}", 'INFO')
        self.log(f"Backup: {'SI' if self.backup else 'NO'}", 'INFO')
        print("="*70)
        print()
        
        # Encontrar todos los archivos relevantes
        extensions = {'.md', '.json', '.template', '.txt', '.rst'}
        files_to_process = []
        
        for ext in extensions:
            files_to_process.extend(self.base_path.rglob(f'*{ext}'))
        
        self.log(f"Archivos encontrados: {len(files_to_process)}", 'INFO')
        print()
        
        # Procesar cada archivo
        for file_path in sorted(files_to_process):
            self.process_file(file_path)
        
        return True
    
    def print_summary(self):
        """Imprimir resumen de cambios"""
        print("\n" + "="*70)
        print("RESUMEN DE EJECUCION")
        print("="*70)
        print(f"Archivos procesados:  {self.stats['files_processed']}")
        print(f"Archivos modificados: {self.stats['files_modified']}")
        print(f"Emojis reemplazados:  {self.stats['emojis_replaced']}")
        print(f"Backups creados:      {self.stats['backups_created']}")
        print("="*70)
        
        if self.dry_run:
            print("\n[DRY-RUN] No se modificaron archivos.")
            print("Ejecuta sin --dry-run para aplicar cambios.")
        elif self.stats['files_modified'] > 0:
            print("\nCambios aplicados exitosamente.")
            if self.backup:
                print("Backups creados con extension .backup_TIMESTAMP")
        else:
            print("\nNo se encontraron emojis para reemplazar.")
    
    def save_log(self, log_path='emoji_removal.log'):
        """Guardar log de cambios"""
        log_file = self.base_path / log_path
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"Log de remocion de emojis\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Directorio: {self.base_path}\n")
            f.write(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCION'}\n")
            f.write("\n" + "="*70 + "\n\n")
            f.write("\n".join(self.changes_log))
            f.write("\n\n" + "="*70 + "\n")
            f.write(f"Archivos procesados:  {self.stats['files_processed']}\n")
            f.write(f"Archivos modificados: {self.stats['files_modified']}\n")
            f.write(f"Emojis reemplazados:  {self.stats['emojis_replaced']}\n")
        
        print(f"\nLog guardado en: {log_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Remover emojis e iconos de archivos en .codex',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  # Dry-run (no modifica archivos)
  python remove_emojis.py --dry-run
  
  # Ejecutar sin backup
  python remove_emojis.py --no-backup
  
  # Ejecutar en directorio específico
  python remove_emojis.py --path /path/to/.codex
  $ python remove_emojis.py --path /e/Proyectos/Translate/ADT/source

  # Modo silencioso
  python remove_emojis.py --quiet
  
  # Con log de cambios
  python remove_emojis.py --save-log
        """
    )
    
    parser.add_argument(
        '--path',
        default='.codex',
        help='Ruta al directorio .codex (default: .codex)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Mostrar cambios sin modificar archivos'
    )
    
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='No crear backups de archivos modificados'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (menos output)'
    )
    
    parser.add_argument(
        '--save-log',
        action='store_true',
        help='Guardar log de cambios en archivo'
    )
    
    args = parser.parse_args()
    
    # Crear remover
    remover = EmojiRemover(
        base_path=args.path,
        dry_run=args.dry_run,
        backup=not args.no_backup,
        verbose=not args.quiet
    )
    
    # Procesar
    success = remover.process_directory()
    
    # Resumen
    remover.print_summary()
    
    # Guardar log si se solicita
    if args.save_log:
        remover.save_log()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
