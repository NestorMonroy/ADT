#!/usr/bin/env python3
"""
Script para detectar y corregir el error: "Document or section may not begin with a transition"

El problema: Cuando un archivo .rst comienza con .. meta:: directive seguido directamente
de una transición decorativa (====), Sphinx genera un error.

Solución: Reorganizar el documento para que comience con un reference label o directamente
con el título, y mover el meta directive después.

Uso:
    python fix_meta_transition.py [--dry-run] [--no-backup] [--path source] [--quiet]
"""

import re
import os
import sys
import argparse
from pathlib import Path
import shutil
from datetime import datetime


class MetaTransitionFixer:
    def __init__(self, base_path, dry_run=False, backup=True, verbose=True):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.backup = backup
        self.verbose = verbose
        self.stats = {
            'files_processed': 0,
            'files_with_issue': 0,
            'files_fixed': 0,
            'backups_created': 0,
        }
        self.changes_log = []
        self.issues_found = []
        
    def log(self, message, level='INFO'):
        """Log mensaje con nivel"""
        if self.verbose:
            prefix = f"[{level}]".ljust(10)
            print(f"{prefix} {message}")
        self.changes_log.append(f"[{level}] {message}")
    
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
    
    def detect_meta_transition_issue(self, content):
        """
        Detectar si hay el patrón problemático:
        - Comienza con .. meta::
        - Seguido de líneas de meta información
        - Luego una transición decorativa (====, ----, ****, etc)
        """
        lines = content.split('\n')
        
        # Buscar si comienza con meta directive
        meta_start_idx = None
        for i, line in enumerate(lines):
            if line.strip().startswith('.. meta::'):
                meta_start_idx = i
                break
        
        if meta_start_idx is None:
            return False, None, None
        
        # Buscar el final del meta directive
        meta_end_idx = None
        for i in range(meta_start_idx + 1, len(lines)):
            # El meta directive termina cuando encontramos una línea que no está indentada
            # (excepto líneas en blanco)
            if lines[i].strip() == '':
                continue
            elif lines[i].startswith('   '):  # Continúa la indentación del meta
                continue
            else:
                meta_end_idx = i
                break
        
        if meta_end_idx is None:
            meta_end_idx = len(lines)
        
        # Buscar transición decorativa después del meta directive
        transition_pattern = re.compile(r'^[=\-\*\~\^_]{5,}$')
        transition_idx = None
        
        for i in range(meta_end_idx, len(lines)):
            if transition_pattern.match(lines[i]):
                transition_idx = i
                break
        
        # Si encontramos transición dentro de los primeros 20 líneas después del meta,
        # es probable que sea el patrón problemático
        if transition_idx is not None and transition_idx - meta_end_idx < 5:
            return True, meta_start_idx, transition_idx
        
        return False, meta_start_idx, transition_idx
    
    def fix_meta_transition(self, content, file_path):
        """Reorganizar el documento para mover meta directive después del título"""
        has_issue, meta_idx, trans_idx = self.detect_meta_transition_issue(content)
        
        if not has_issue:
            return content, False
        
        lines = content.split('\n')
        
        # Encontrar el final del meta directive
        meta_start = meta_idx
        meta_end = meta_idx + 1
        
        for i in range(meta_idx + 1, len(lines)):
            if lines[i].strip() == '':
                meta_end = i + 1
                break
            elif lines[i].startswith('   '):
                meta_end = i + 1
            else:
                meta_end = i
                break
        
        # Extraer las secciones
        meta_lines = lines[meta_start:meta_end]  # El meta directive completo
        
        # Buscar la referencia (.. _nombre:) que viene después del meta
        ref_idx = None
        ref_lines = []
        
        for i in range(meta_end, min(meta_end + 3, len(lines))):
            if lines[i].strip().startswith('.. _'):
                ref_idx = i
                ref_lines.append(lines[i])
                break
        
        # Buscar el título (líneas de transición + título + líneas de transición)
        title_start = None
        title_end = None
        
        search_start = meta_end if ref_idx is None else ref_idx + 1
        
        for i in range(search_start, len(lines)):
            if transition_pattern := re.match(r'^[=\-\*\~\^_]{5,}$', lines[i]):
                title_start = i
                # El título está en la siguiente línea
                if i + 1 < len(lines):
                    # La línea después de la transición de arriba es el título
                    # La línea después del título es la transición de abajo
                    if i + 2 < len(lines) and re.match(r'^[=\-\*\~\^_]{5,}$', lines[i + 2]):
                        title_end = i + 3
                        break
        
        if title_start is None:
            # No hay patrón de título claro, devolver sin cambios
            return content, False
        
        # Reconstruir el documento con el orden correcto
        # Nuevo orden:
        # 1. Referencia (si existe)
        # 2. Línea en blanco
        # 3. Transición de arriba
        # 4. Título
        # 5. Transición de abajo
        # 6. Línea en blanco
        # 7. Meta directive
        # 8. Resto del contenido
        
        new_lines = []
        
        # Agregar todo lo que viene ANTES del meta directive (generalmente vacío)
        if meta_start > 0:
            new_lines.extend(lines[:meta_start])
        
        # Agregar referencia si existe
        if ref_idx is not None:
            new_lines.append(lines[ref_idx])
            new_lines.append('')  # Línea en blanco
        
        # Agregar título con sus transiciones
        new_lines.extend(lines[title_start:title_end])
        new_lines.append('')  # Línea en blanco
        
        # Agregar meta directive
        new_lines.extend(meta_lines)
        
        # Agregar el resto del contenido (después del título)
        remaining_start = title_end
        if remaining_start < len(lines):
            # Saltar líneas en blanco redundantes
            while remaining_start < len(lines) and lines[remaining_start].strip() == '':
                remaining_start += 1
            new_lines.extend(lines[remaining_start:])
        
        new_content = '\n'.join(new_lines)
        
        return new_content, True
    
    def process_file(self, file_path):
        """Procesar un archivo individual"""
        self.stats['files_processed'] += 1
        
        try:
            # Leer contenido
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Detectar issue
            has_issue, _, _ = self.detect_meta_transition_issue(content)
            
            if has_issue:
                self.stats['files_with_issue'] += 1
                rel_path = file_path.relative_to(self.base_path)
                self.issues_found.append(str(rel_path))
                self.log(f"Problema encontrado: {rel_path}", 'ISSUE')
                
                # Arreglar
                new_content, was_fixed = self.fix_meta_transition(content, file_path)
                
                if was_fixed:
                    self.stats['files_fixed'] += 1
                    
                    if self.dry_run:
                        self.log(f"[DRY-RUN] Se modificaría: {rel_path}", 'DRY-RUN')
                    else:
                        # Crear backup
                        self.create_backup(file_path)
                        
                        # Escribir nuevo contenido
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        self.log(f"Archivos corregido: {rel_path}", 'FIXED')
                else:
                    self.log(f"No se pudo corregir: {rel_path}", 'WARN')
                    
        except Exception as e:
            self.log(f"Error procesando {file_path.name}: {e}", 'ERROR')
    
    def process_directory(self):
        """Procesar todos los archivos .rst en directorio"""
        if not self.base_path.exists():
            self.log(f"Error: Directorio no existe: {self.base_path}", 'ERROR')
            return False
        
        print("\n" + "="*80)
        self.log(f"Iniciando búsqueda de errores de transición en meta directives", 'START')
        self.log(f"Directorio: {self.base_path}", 'INFO')
        self.log(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCIÓN'}", 'INFO')
        self.log(f"Backup: {'SÍ' if self.backup else 'NO'}", 'INFO')
        print("="*80 + "\n")
        
        # Encontrar todos los archivos .rst
        rst_files = list(self.base_path.rglob('*.rst'))
        self.log(f"Archivos .rst encontrados: {len(rst_files)}", 'INFO')
        print()
        
        # Procesar cada archivo
        for file_path in sorted(rst_files):
            self.process_file(file_path)
        
        print()
        return True
    
    def print_summary(self):
        """Imprimir resumen de cambios"""
        print("\n" + "="*80)
        print("RESUMEN DE EJECUCIÓN")
        print("="*80)
        print(f"Archivos procesados:     {self.stats['files_processed']}")
        print(f"Archivos con problema:   {self.stats['files_with_issue']}")
        print(f"Archivos corregidos:     {self.stats['files_fixed']}")
        print(f"Backups creados:         {self.stats['backups_created']}")
        print("="*80)
        
        if self.issues_found:
            print("\nArchivos con el problema encontrados:")
            for issue in self.issues_found:
                print(f"  • {issue}")
        
        if self.dry_run:
            print("\n[DRY-RUN] No se modificaron archivos.")
            print("Ejecuta sin --dry-run para aplicar cambios.")
        elif self.stats['files_fixed'] > 0:
            print("\nCambios aplicados exitosamente.")
            if self.backup:
                print("Backups creados con extensión .backup_TIMESTAMP")
        else:
            print("\nNo se encontraron problemas para corregir.")
    
    def save_log(self, log_path='fix_meta_transition.log'):
        """Guardar log de cambios"""
        log_file = self.base_path.parent / log_path
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("Log de corrección de transiciones en meta directives\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Directorio: {self.base_path}\n")
            f.write(f"Modo: {'DRY-RUN' if self.dry_run else 'EJECUCIÓN'}\n")
            f.write("\n" + "="*80 + "\n\n")
            f.write("CHANGELOG:\n\n")
            f.write("\n".join(self.changes_log))
            f.write("\n\n" + "="*80 + "\n")
            f.write(f"Archivos procesados:     {self.stats['files_processed']}\n")
            f.write(f"Archivos con problema:   {self.stats['files_with_issue']}\n")
            f.write(f"Archivos corregidos:     {self.stats['files_fixed']}\n")
            f.write(f"Backups creados:         {self.stats['backups_created']}\n")
        
        print(f"\nLog guardado en: {log_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Detectar y corregir el error "Document begins with transition" en archivos .rst',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  # Dry-run (no modifica archivos)
  python fix_meta_transition.py --dry-run
  
  # Ejecutar sin backup
  python fix_meta_transition.py --no-backup
  
  # Ejecutar en directorio especifico
  python fix_meta_transition.py --path /path/to/source
  python fix_meta_transition.py --path /e/Proyectos/Translate/ADT/source  --dry-run
  # Modo silencioso
  python fix_meta_transition.py --quiet
  
  # Con log de cambios
  python fix_meta_transition.py --save-log
  
  # Todas las opciones
  python fix_meta_transition.py --path source --dry-run --save-log
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
    
    # Crear fixer
    fixer = MetaTransitionFixer(
        base_path=args.path,
        dry_run=args.dry_run,
        backup=not args.no_backup,
        verbose=not args.quiet
    )
    
    # Procesar
    success = fixer.process_directory()
    
    # Resumen
    fixer.print_summary()
    
    # Guardar log si se solicita
    if args.save_log:
        fixer.save_log()
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
