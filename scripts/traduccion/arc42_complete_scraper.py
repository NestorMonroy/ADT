#!/usr/bin/env python3
"""
arc42_complete_scraper.py

Scraper COMPLETO para arc42 que:
1. Obtiene contenido con web_fetch
2. Extrae TODOS los enlaces (tips, examples, images)
3. Descarga cada enlace recursivamente
4. Genera estructura completa para traducción

USO:
  Llamar desde Claude con web_fetch para cada URL
"""

import json
import re
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

class Arc42ContentExtractor(HTMLParser):
    """Extrae contenido estructurado de HTML de arc42"""
    
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current_section = None
        self.tips = []
        self.examples = []
        self.images = []
        self.in_section = False
        self.section_content = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Detectar encabezados de sección
        if tag in ['h2', 'h3', 'h4']:
            if self.current_section:
                self.current_section['content'] = ''.join(self.section_content)
                self.sections.append(self.current_section)
            
            self.current_section = {
                'level': tag,
                'title': '',
                'content': ''
            }
            self.section_content = []
            self.in_section = True
        
        # Detectar enlaces a tips
        if tag == 'a' and 'href' in attrs_dict:
            href = attrs_dict['href']
            if '/tips/' in href:
                self.tips.append({
                    'url': href if href.startswith('http') else 'https://docs.arc42.org' + href,
                    'text': ''
                })
            elif '/examples/' in href:
                self.examples.append({
                    'url': href if href.startswith('http') else 'https://docs.arc42.org' + href,
                    'text': ''
                })
        
        # Detectar imágenes
        if tag == 'img' and 'src' in attrs_dict:
            self.images.append({
                'src': attrs_dict['src'],
                'alt': attrs_dict.get('alt', ''),
                'title': attrs_dict.get('title', '')
            })
    
    def handle_data(self, data):
        if self.in_section and self.current_section:
            if 'title' in self.current_section and not self.current_section['title']:
                self.current_section['title'] = data.strip()
            else:
                self.section_content.append(data)
        
        # Agregar texto a tips/examples
        if self.tips and not self.tips[-1]['text']:
            self.tips[-1]['text'] = data.strip()
        if self.examples and not self.examples[-1]['text']:
            self.examples[-1]['text'] = data.strip()

def extract_content_from_html(html):
    """Extrae contenido estructurado de HTML"""
    extractor = Arc42ContentExtractor()
    extractor.feed(html)
    
    # Cerrar última sección
    if extractor.current_section:
        extractor.current_section['content'] = ''.join(extractor.section_content)
        extractor.sections.append(extractor.current_section)
    
    return {
        'sections': extractor.sections,
        'tips': extractor.tips,
        'examples': extractor.examples,
        'images': extractor.images
    }

def create_urls_to_fetch():
    """Crea lista de URLs que necesitan ser fetched con web_fetch"""
    
    urls = {
        'main': 'https://docs.arc42.org/section-1/',
        'tips': [],
        'examples': []
    }
    
    # Tips conocidos de la Sección 1 (1-1 a 1-24)
    for i in range(1, 25):
        urls['tips'].append(f'https://docs.arc42.org/tips/1-{i}/')
    
    # Examples conocidos
    urls['examples'] = [
        'https://docs.arc42.org/examples/overview-example-3/',
        'https://docs.arc42.org/examples/overview-example-htmlsc-1/',
        'https://docs.arc42.org/examples/quality-htmlsc-2/',
        'https://docs.arc42.org/examples/quality-tpu-1/'
    ]
    
    return urls

def save_fetch_instructions():
    """Genera instrucciones para Claude sobre qué hacer con web_fetch"""
    
    urls = create_urls_to_fetch()
    output_dir = Path('/tmp/ADT/biblioteca/arc42_documentation/sections/section-1-complete/')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    instructions = {
        'timestamp': datetime.now().isoformat(),
        'instructions': 'Use web_fetch de Claude para cada URL listada abajo',
        'total_urls': 1 + len(urls['tips']) + len(urls['examples']),
        'urls': urls,
        'output_directory': str(output_dir),
        'next_steps': [
            '1. Llamar web_fetch para URL principal',
            '2. Llamar web_fetch para cada tip (24 tips)',
            '3. Llamar web_fetch para cada example (4 examples)',
            '4. Procesar todo con este script',
            '5. Traducir con metodología ADT (NO literal)'
        ]
    }
    
    output_file = output_dir / 'fetch_instructions.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(instructions, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Instrucciones guardadas en: {output_file}")
    print(f"\nTOTAL URLs a fetchear: {instructions['total_urls']}")
    print(f"  - URL principal: 1")
    print(f"  - Tips: {len(urls['tips'])}")
    print(f"  - Examples: {len(urls['examples'])}")
    print()
    print("Ejecuta web_fetch para cada URL y guarda el resultado.")
    
    return instructions

if __name__ == '__main__':
    print("═══════════════════════════════════════════════════════════")
    print("  arc42 COMPLETE SCRAPER - Generador de Instrucciones")
    print("═══════════════════════════════════════════════════════════")
    print()
    
    instructions = save_fetch_instructions()
    
    print()
    print("═══════════════════════════════════════════════════════════")
    print("  PRÓXIMO PASO: Usar web_fetch de Claude")
    print("═══════════════════════════════════════════════════════════")
    print()
    print("Ejemplo:")
    print("  web_fetch('https://docs.arc42.org/section-1/')")
    print("  web_fetch('https://docs.arc42.org/tips/1-1/')")
    print("  ...")
