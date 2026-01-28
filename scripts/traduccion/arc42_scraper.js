/**
 * ADT - Arc42 Documentation Scraper
 * Script PhantomJS para obtener todas las secciones de arc42.org
 * 
 * Uso: phantomjs arc42_scraper.js
 */

"use strict";

var page = require('webpage').create();
var fs = require('fs');
var system = require('system');

// Configuración
var config = {
    baseUrl: 'https://docs.arc42.org',
    sections: [
        'section-1',  // Introduction & Goals
        'section-2',  // Constraints
        'section-3',  // Context & Scope
        'section-4',  // Solution Strategy
        'section-5',  // Building Block View
        'section-6',  // Runtime View
        'section-7',  // Deployment View
        'section-8',  // Crosscutting Concepts
        'section-9',  // Architecture Decisions
        'section-10', // Quality Requirements
        'section-11', // Risks & Technical Debt
        'section-12'  // Glossary
    ],
    outputDir: '/tmp/ADT/biblioteca/arc42_documentation/sections/',
    timeout: 10000
};

// Configurar página
page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36';
page.viewportSize = { width: 1920, height: 1080 };

/**
 * Guardar contenido a archivo
 */
function saveToFile(filename, content) {
    try {
        fs.write(filename, content, 'w');
        console.log('✓ Guardado: ' + filename);
        return true;
    } catch(e) {
        console.log('✗ Error guardando ' + filename + ': ' + e);
        return false;
    }
}

/**
 * Scrape una sección específica
 */
function scrapeSection(sectionIndex) {
    if (sectionIndex >= config.sections.length) {
        console.log('\n=== SCRAPING COMPLETADO ===');
        console.log('Total secciones: ' + config.sections.length);
        phantom.exit(0);
        return;
    }
    
    var section = config.sections[sectionIndex];
    var url = config.baseUrl + '/' + section + '/';
    
    console.log('\n[' + (sectionIndex + 1) + '/' + config.sections.length + '] Scraping: ' + url);
    
    page.open(url, function(status) {
        if (status !== 'success') {
            console.log('✗ Error abriendo: ' + url);
            scrapeSection(sectionIndex + 1);
            return;
        }
        
        // Esperar a que cargue el contenido
        setTimeout(function() {
            // Extraer contenido de la página
            var pageData = page.evaluate(function() {
                var data = {
                    title: '',
                    content: '',
                    headings: [],
                    links: []
                };
                
                // Obtener título
                var h1 = document.querySelector('h1');
                if (h1) data.title = h1.textContent.trim();
                
                // Obtener contenido principal
                var article = document.querySelector('article') || 
                              document.querySelector('.content') ||
                              document.querySelector('main');
                
                if (article) {
                    data.content = article.innerText;
                    
                    // Obtener encabezados
                    var headers = article.querySelectorAll('h1, h2, h3, h4');
                    for (var i = 0; i < headers.length; i++) {
                        data.headings.push({
                            level: headers[i].tagName,
                            text: headers[i].textContent.trim()
                        });
                    }
                    
                    // Obtener enlaces
                    var anchors = article.querySelectorAll('a[href]');
                    for (var j = 0; j < anchors.length; j++) {
                        data.links.push({
                            text: anchors[j].textContent.trim(),
                            href: anchors[j].href
                        });
                    }
                }
                
                return data;
            });
            
            // Guardar datos
            var outputFile = config.outputDir + section + '.json';
            var jsonData = JSON.stringify(pageData, null, 2);
            saveToFile(outputFile, jsonData);
            
            // Guardar HTML completo
            var htmlFile = config.outputDir + section + '.html';
            saveToFile(htmlFile, page.content);
            
            // Capturar screenshot
            var screenshotFile = config.outputDir + section + '.png';
            page.render(screenshotFile);
            console.log('✓ Screenshot: ' + screenshotFile);
            
            // Procesar siguiente sección
            scrapeSection(sectionIndex + 1);
            
        }, config.timeout);
    });
}

// Iniciar scraping
console.log('╔════════════════════════════════════════════════╗');
console.log('║   ADT - Arc42 Documentation Scraper          ║');
console.log('║   PhantomJS 2.1.1                             ║');
console.log('╚════════════════════════════════════════════════╝');
console.log('');
console.log('Base URL: ' + config.baseUrl);
console.log('Secciones: ' + config.sections.length);
console.log('Output: ' + config.outputDir);
console.log('');

// Crear directorio de salida si no existe
if (!fs.isDirectory(config.outputDir)) {
    fs.makeTree(config.outputDir);
    console.log('✓ Directorio creado: ' + config.outputDir);
}

// Comenzar scraping
scrapeSection(0);
