#!/usr/bin/env python3
"""
Script para convertir todos los archivos a LF (Unix/Linux line endings)

Convierte automáticamente:
- CRLF (Windows: \r\n) → LF (Unix: \n)
- CR (Mac antiguo: \r) → LF (Unix: \n)
- Mezclas CRLF/LF → LF puro

Uso:
    python convert_to_lf.py [--dry-run] [--no-backup] [--path source] [--quiet] [--extensions .rst,.md,.txt]
"""

import os
import sys
import argparse
from pathlib import Path
import shutil
from datetime import datetime


class LFConverter:
    def __init__(self, base_path, dry_run=False, backup=True, verbose=True, extensions=None):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.backup = backup
        self.verbose = verbose
        
        # Extensions por defecto
        if extensions is None:
            self.extensions = {'.rst', '.md', '.txt', '.json', '.py', '.sh', '.template', '.cfg', '.ini', '.yaml', '.yml'}
        else:
            self.extensions = set(extensions)
        
        self.stats = {
            'files_processed': 0,
            'files_converted': 0,
            'already_lf': 0,
            'had_crlf': 0,
            'had_mixed': 0,
            'backups_created': 0,
        }
        self.changes_log = []
        self.converted_files = []
        
    def log(self, message, level='INFO'):
        """Log mensaje con nivel"""
        if self.verbose:
            prefix = f"[{level}]".ljust(12)
            print(f"{prefix} {message}")
        self.changes_log.append(f"[{level}] {message}")
    
    def detect_line_ending(self, content):
        """
        Detectar el tipo de line ending en el contenido.
        Retorna: ('CRLF', 'LF', 'CR', 'MIXED')
        """
        crlf_count = content.count(b'\r\n')
        lf_count = content.count(b'\n') - crlf_count  # Restar CRLF porque contiene \n
        cr_count = content.count(b'\r') - crlf_count  # Restar CRLF porque contiene \r
        
        if crlf_count > 0 and lf_count > 0:
            return 'MIXED'
        elif crlf_count > 0:
            return 'CRLF'
        elif lf_count > 0:
            return 'LF'
        elif cr_count > 0:
            return 'CR'
        else:
            return 'NONE'  # No tiene saltos de línea
    
    def convert_to_lf(self, content):
        """Convertir cualquier tipo de line ending a LF"""
        # Primero, reemplazar CRLF con LF
        content = content.replace(b'\r\n', b'\n')
        # Luego, reemplazar CR con LF
        content = content.replace(b'\r', b'\n')
        return content
    
    def create_backup(self, file_path):
        """Crear backup de archivo"""
        if not self.backup or self.dry_run:
            return None
            
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = file_path.parent / f"{file_path.name}.backup_{timestamp}"
        
        shutil.copy2(file_path, backup_path)
        self.stats['backups_created'] += 1
        self.log(f"Backup creado: {backup_path.name}", 'BACKUP')
        return backup_path
    
    def process_file(self, file_path):
        """Procesar un archivo individual"""
        self.stats['files_processed'] += 1
        rel_path = file_path.relative_to(self.base_path)
        
        try:
            # Leer contenido en modo binario para preservar exactamente los bytes
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Detectar line ending
            line_ending = self.detect_line_ending(content)
            
            # Si ya está en LF, no hacer nada
            if line_ending == 'LF' or line_ending == 'NONE':
                self.stats['already_lf'] += 1
                self.log(f"Ya está en LF: {rel_path}", 'OK')
                return
            
            # Contar el tipo de conversión
            if line_ending == 'CRLF':
                self.stats['had_crlf'] += 1
                ending_type = "CRLF → LF"
            elif line_ending == 'CR':
                ending_type = "CR → LF"
            elif line_ending == 'MIXED':
                self.stats['had_mixed'] += 1
                ending_type = "MIXED → LF"
            
            # Convertir a LF
            new_content = self.convert_to_lf(content)
            
            self.stats['files_converted'] += 1
            self.converted_files.append((str(rel_path), line_ending))
            
            if self.dry_run:
                self.log(f"[DRY-RUN] Se convertiría: {rel_path} ({ending_type})", 'DRY-RUN')
            else:
                # Crear backup
                self.create_backup(file_path)
                
                # Escribir nuevo contenido
                with open(file_path, 'wb') as f:
                    f.write(new_content)
                
                self.log(f"Convertido a LF: {rel_path} ({ending_type})", 'CONVERTED')
                    
        except Exception as e:
            self.log(f"Error procesando {file_path.name}: {e}", 'ERROR')
    
    def process_directory(self):
        """Procesar todos los archivos en directorio"""
        if not self.base_path.exists():
            self.log(f"Error: Directorio no existe: {self.base_path}", 'ERROR')
            return False
        
        print("\n" + "="*80)
        self.log("Iniciando conversión a LF (Unix line endings)", 'START')
        self.log(f"Directorio: {self.base_path}", 'INFO')
        self.log(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCIÓN'}", 'INFO')
        self.log(f"Backup: {'SÍ' if self.backup else 'NO'}", 'INFO')
        self.log(f"Extensiones: {', '.join(sorted(self.extensions))}", 'INFO')
        print("="*80 + "\n")
        
        # Encontrar todos los archivos con extensiones especificadas
        files_to_process = []
        
        for ext in self.extensions:
            files_to_process.extend(self.base_path.rglob(f'*{ext}'))
        
        self.log(f"Archivos encontrados: {len(files_to_process)}", 'INFO')
        print()
        
        # Procesar cada archivo
        for file_path in sorted(files_to_process):
            self.process_file(file_path)
        
        print()
        return True
    
    def print_summary(self):
        """Imprimir resumen de cambios"""
        print("\n" + "="*80)
        print("RESUMEN DE EJECUCIÓN")
        print("="*80)
        print(f"Archivos procesados:      {self.stats['files_processed']}")
        print(f"Ya estaban en LF:         {self.stats['already_lf']}")
        print(f"Convertidos a LF:         {self.stats['files_converted']}")
        print(f"  ├─ Tenían CRLF:         {self.stats['had_crlf']}")
        print(f"  ├─ Tenían CR:           {0}")  # No contamos CR específicamente
        print(f"  └─ Tenían MIXED:        {self.stats['had_mixed']}")
        print(f"Backups creados:          {self.stats['backups_created']}")
        print("="*80)
        
        if self.converted_files and self.verbose:
            print("\nDetalles de archivos convertidos:")
            for file_path, ending in self.converted_files[:10]:
                print(f"  • {file_path} ({ending})")
            if len(self.converted_files) > 10:
                print(f"  ... y {len(self.converted_files) - 10} más")
        
        if self.dry_run:
            print("\n[DRY-RUN] No se modificaron archivos.")
            print("Ejecuta sin --dry-run para aplicar cambios.")
        elif self.stats['files_converted'] > 0:
            print("\nConversión completada exitosamente.")
            if self.backup:
                print("Backups creados con extensión .backup_TIMESTAMP")
        else:
            print("\nTodos los archivos ya estaban en LF.")
    
    def save_log(self, log_path='convert_to_lf.log'):
        """Guardar log de cambios"""
        log_file = self.base_path.parent / log_path
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("Log de conversión a LF (Unix line endings)\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Directorio: {self.base_path}\n")
            f.write(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCIÓN'}\n")
            f.write("\n" + "="*80 + "\n\n")
            f.write("CHANGELOG:\n\n")
            f.write("\n".join(self.changes_log))
            f.write("\n\n" + "="*80 + "\n")
            f.write(f"Archivos procesados:      {self.stats['files_processed']}\n")
            f.write(f"Ya estaban en LF:         {self.stats['already_lf']}\n")
            f.write(f"Convertidos a LF:         {self.stats['files_converted']}\n")
            f.write(f"  ├─ Tenían CRLF:         {self.stats['had_crlf']}\n")
            f.write(f"  └─ Tenían MIXED:        {self.stats['had_mixed']}\n")
            f.write(f"Backups creados:          {self.stats['backups_created']}\n")
        
        print(f"\nLog guardado en: {log_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Convertir todos los archivos a LF (Unix line endings)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  # Dry-run (no modifica archivos)
  python convert_to_lf.py --dry-run
  
  # Ejecutar sin backup
  python convert_to_lf.py --no-backup
  
  # Ejecutar en directorio específico
  python convert_to_lf.py --path /ruta/a/source
  
  # Solo archivos .rst
  python convert_to_lf.py --extensions .rst
  
  # Múltiples extensiones
  python convert_to_lf.py --extensions .rst,.md,.py
  
  # Modo silencioso con log
  python convert_to_lf.py --quiet --save-log
  
  # Todas las opciones
  python convert_to_lf.py --path source --dry-run --save-log
        """
    )
    
    parser.add_argument(
        '--path',
        default='source',
        help='Ruta al directorio a procesar (default: source)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Ver cambios sin modificar archivos (RECOMENDADO primero)'
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
    
    parser.add_argument(
        '--extensions',
        default=None,
        help='Extensiones a procesar (separadas por coma, ej: .rst,.md,.py). Default: .rst,.md,.txt,.json,.py,.sh,.template,.cfg,.ini,.yaml,.yml'
    )
    
    args = parser.parse_args()
    
    # Parsear extensiones si se especificaron
    extensions = None
    if args.extensions:
        extensions = [f".{ext.lstrip('.')}" for ext in args.extensions.split(',')]
    
    # Crear converter
    converter = LFConverter(
        base_path=args.path,
        dry_run=args.dry_run,
        backup=not args.no_backup,
        verbose=not args.quiet,
        extensions=extensions
    )
    
    # Procesar
    success = converter.process_directory()
    
    # Resumen
    converter.print_summary()
    
    # Guardar log si se solicita
    if args.save_log:
        converter.save_log()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
