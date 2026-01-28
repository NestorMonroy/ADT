#!/usr/bin/env python3
"""
ADT - Sistema de Traducción Web
Traduce contenido web a español mexicano preservando términos técnicos
Versión: 1.0.0
"""

import re
import sys
from datetime import datetime
from pathlib import Path

class ADTTranslator:
    """
    Traductor web siguiendo metodología ADT:
    - Alta fidelidad
    - Marcado visual de términos
    - Preservación de términos técnicos
    """
    
    # Términos técnicos comunes que NO se traducen
    TECH_TERMS = {
        'arc42', 'template', 'framework', 'software', 'API', 'REST', 'HTTP',
        'JavaScript', 'Python', 'Node.js', 'React', 'Docker', 'TypeScript',
        'quality goals', 'stakeholders', 'whitebox', 'blackbox', 
        'cross-cutting', 'deployment', 'runtime', 'rationale',
        'technical debt', 'ADR', 'TDR', 'DevOps', 'CI/CD',
        'frontend', 'backend', 'full-stack', 'microservices'
    }
    
    # Mapeo de traducciones comunes (español → inglés original)
    TRANSLATIONS = {
        'introducción': 'introduction',
        'restricciones': 'constraints',
        'contexto': 'context',
        'alcance': 'scope',
        'estrategia': 'strategy',
        'solución': 'solution',
        'bloques': 'blocks',
        'construcción': 'building',
        'tiempo de ejecución': 'runtime',
        'despliegue': 'deployment',
        'conceptos transversales': 'crosscutting concepts',
        'decisiones': 'decisions',
        'calidad': 'quality',
        'requisitos': 'requirements',
        'riesgos': 'risks',
        'deuda técnica': 'technical debt',
        'glosario': 'glossary'
    }
    
    def __init__(self, output_dir='.'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.terms_found = set()
    
    def clean_html_text(self, html_text):
        """Limpia texto HTML básico"""
        # Remover tags HTML
        text = re.sub(r'<[^>]+>', '', html_text)
        # Decodificar entidades HTML comunes
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        # Remover espacios múltiples
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def identify_tech_terms(self, text):
        """Identifica términos técnicos en el texto"""
        found = set()
        for term in self.TECH_TERMS:
            if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE):
                found.add(term)
        return found
    
    def mark_first_appearance(self, text, term):
        """
        Marca la primera aparición de un término técnico
        Formato: español (:term:`inglés`)
        """
        # Buscar primera aparición
        pattern = r'\b' + re.escape(term) + r'\b'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if match:
            # Marcar solo la primera aparición
            original = match.group(0)
            marked = f"{original} (en su :term:`primera aparición <{term}>`)"
            text = text[:match.start()] + marked + text[match.end():]
        
        return text
    
    def generate_rst_header(self, title, url, mode="Alta Fidelidad + Marcado Visual"):
        """Genera encabezado RST con metadata"""
        separator = "=" * len(title)
        header = f""".. meta::
   :fuente: {url}
   :traducido: {datetime.now().strftime('%Y-%m-%d')}
   :idioma: es-MX
   :modo: {mode}

{separator}
{title}
{separator}

.. contents:: Contenido
   :depth: 3
   :local:

----

"""
        return header
    
    def generate_glossary(self, terms):
        """Genera sección de glosario con términos encontrados"""
        if not terms:
            return ""
        
        glossary = """
----

Glosario de Términos
====================

Términos técnicos identificados en este documento:

.. glossary::
   :sorted:

"""
        for term in sorted(terms):
            glossary += f"""   {term}
      Término técnico preservado en inglés.
      Ver documentación original para definición completa.

"""
        return glossary
    
    def add_translation_notes(self, source_url):
        """Agrega notas sobre el proceso de traducción"""
        notes = f"""
----

Notas de Traducción
===================

Esta traducción sigue los principios de **Alta Fidelidad + Marcado Visual**:

✓ **Términos técnicos preservados:**
   - Términos especializados mantenidos en inglés original
   - Primera aparición marcada con ``:term:``

✓ **Estructura preservada:**
   - Jerarquía de títulos idéntica
   - Enlaces a documentación original preservados

✓ **Estilo:**
   - Tú informal (coherente con material técnico moderno)
   - Voz activa preferida
   - Lenguaje claro y directo

----

**Fuente:** {source_url}  
**Traducido:** {datetime.now().strftime('%Y-%m-%d')}  
**Modo:** Alta Fidelidad + Marcado Visual  
**Framework:** ADT (Arc42-Diátaxis-Traducción)
"""
        return notes
    
    def create_chapter_structure(self, book_path, chapter_num, chapter_name):
        """Crea estructura de carpetas para un capítulo"""
        chapter_dir = Path(book_path) / f"Chapter_{chapter_num:02d}_{chapter_name}"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        
        # Crear subdirectorios
        (chapter_dir / "original").mkdir(exist_ok=True)
        (chapter_dir / "traduccion").mkdir(exist_ok=True)
        (chapter_dir / "figuras").mkdir(exist_ok=True)
        
        return chapter_dir
    
    def translate_content(self, content, source_url, title):
        """
        Traduce contenido aplicando reglas ADT
        NOTA: Esta es una versión simplificada
        Para traducción real, se requiere API de traducción o proceso manual
        """
        # Por ahora, solo estructura el contenido
        # La traducción real debe hacerse manualmente o con API
        
        # Limpiar texto
        clean_text = self.clean_html_text(content)
        
        # Identificar términos técnicos
        terms = self.identify_tech_terms(clean_text)
        self.terms_found.update(terms)
        
        # Generar documento RST
        rst_content = self.generate_rst_header(title, source_url)
        
        # Agregar contenido (marcador para traducción manual)
        rst_content += f"""
Introducción
============

.. note::
   **CONTENIDO PENDIENTE DE TRADUCCIÓN**
   
   Este es un template generado automáticamente.
   El contenido debe ser traducido manualmente siguiendo las reglas ADT:
   
   1. Preservar términos técnicos en inglés
   2. Marcar primera aparición de cada término
   3. Mantener estructura original
   4. Usar español mexicano informal (tú)
   5. Preferir voz activa

Contenido Original (para referencia)
=====================================

.. code-block:: text

   {clean_text[:500]}...
   
   [CONTENIDO TRUNCADO - Ver fuente original]

"""
        # Agregar glosario
        rst_content += self.generate_glossary(terms)
        
        # Agregar notas de traducción
        rst_content += self.add_translation_notes(source_url)
        
        return rst_content

def main():
    """Función principal"""
    if len(sys.argv) < 4:
        print("""
Uso: python3 adt_translator.py <URL> <TITULO> <ARCHIVO_SALIDA>

Ejemplo:
  python3 adt_translator.py \\
      'https://arc42.org/overview' \\
      'Visión General de arc42' \\
      'arc42_overview.rst'
        """)
        sys.exit(1)
    
    url = sys.argv[1]
    title = sys.argv[2]
    output_file = sys.argv[3]
    
    print(f"=== ADT Traductor Web ===")
    print(f"URL: {url}")
    print(f"Título: {title}")
    print(f"Salida: {output_file}")
    print()
    
    translator = ADTTranslator()
    
    # Nota: En uso real, aquí se llamaría a web_fetch
    # Por ahora, creamos un template
    print("⚠️  NOTA: Esto genera un TEMPLATE para traducción manual")
    print("    El contenido real debe obtenerse con web_fetch y traducirse")
    print()
    
    content = f"Template para traducción de {title}"
    
    rst_content = translator.translate_content(content, url, title)
    
    # Guardar archivo
    output_path = Path(output_file)
    output_path.write_text(rst_content, encoding='utf-8')
    
    print(f"✓ Template RST generado: {output_file}")
    print(f"✓ Términos técnicos identificados: {len(translator.terms_found)}")
    print()
    print("Próximos pasos:")
    print("1. Obtener contenido con web_fetch")
    print("2. Traducir manualmente siguiendo reglas ADT")
    print("3. Marcar términos técnicos en primera aparición")
    print("4. Compilar con Sphinx (make html)")

if __name__ == '__main__':
    main()
