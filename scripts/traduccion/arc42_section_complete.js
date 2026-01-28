/**
 * arc42_section_complete.js
 * Captura COMPLETA de una sección de arc42 incluyendo:
 * - Contenido principal
 * - Todos los tips expandidos
 * - Todos los ejemplos enlazados
 * - Todas las imágenes
 * - TODO el contenido dinámico
 */

"use strict";

var page = require('webpage').create();
var fs = require('fs');
var system = require('system');

// Configuración
var config = {
    sectionUrl: 'https://docs.arc42.org/section-1/',
    outputDir: '/tmp/ADT/biblioteca/arc42_documentation/sections/section-1-complete/',
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
};

// Crear directorio de salida
if (!fs.isDirectory(config.outputDir)) {
    fs.makeTree(config.outputDir);
}

// Configurar página
page.settings.userAgent = config.userAgent;
page.settings.loadImages = true;
page.settings.javascriptEnabled = true;
page.viewportSize = { width: 1920, height: 1080 };

// Arrays para almacenar datos
var tipsData = [];
var examplesData = [];
var imagesData = [];

console.log('═══════════════════════════════════════════════');
console.log('  arc42 Section 1 - COMPLETE SCRAPER');
console.log('═══════════════════════════════════════════════');
console.log('');
console.log('URL: ' + config.sectionUrl);
console.log('Output: ' + config.outputDir);
console.log('');

// Capturar recursos (imágenes)
page.onResourceReceived = function(response) {
    if (response.stage === 'end') {
        var url = response.url;
        
        // Detectar imágenes
        if (url.match(/\.(png|jpg|jpeg|gif|webp|svg)$/i)) {
            imagesData.push({
                url: url,
                contentType: response.contentType,
                status: response.status
            });
        }
    }
};

// Log de errores
page.onResourceError = function(error) {
    console.log('⚠ Resource error: ' + error.url + ' - ' + error.errorString);
};

// Abrir página principal
page.open(config.sectionUrl, function(status) {
    if (status !== 'success') {
        console.log('✗ Error abriendo página principal');
        phantom.exit(1);
        return;
    }
    
    console.log('✓ Página principal cargada');
    
    // Esperar a que se cargue completamente
    setTimeout(function() {
        
        // 1. EXTRAER CONTENIDO PRINCIPAL
        var mainContent = page.evaluate(function() {
            var data = {
                title: '',
                sections: [],
                tips: [],
                examples: [],
                images: []
            };
            
            // Título
            var h1 = document.querySelector('h1');
            if (h1) data.title = h1.textContent.trim();
            
            // Todas las secciones (h2, h3)
            var headers = document.querySelectorAll('h2, h3, h4');
            for (var i = 0; i < headers.length; i++) {
                var header = headers[i];
                var nextContent = '';
                var sibling = header.nextElementSibling;
                
                // Obtener contenido hasta el siguiente header
                while (sibling && !sibling.matches('h2, h3, h4')) {
                    nextContent += sibling.innerText + '\n\n';
                    sibling = sibling.nextElementSibling;
                }
                
                data.sections.push({
                    level: header.tagName,
                    title: header.textContent.trim(),
                    content: nextContent.trim()
                });
            }
            
            // Tips (enlaces con /tips/)
            var tipLinks = document.querySelectorAll('a[href*="/tips/"]');
            for (var j = 0; j < tipLinks.length; j++) {
                var tipLink = tipLinks[j];
                data.tips.push({
                    title: tipLink.textContent.trim(),
                    url: tipLink.href,
                    number: tipLink.href.match(/tips\/(\d+-\d+)/)?.[1] || ''
                });
            }
            
            // Examples (enlaces con /examples/)
            var exampleLinks = document.querySelectorAll('a[href*="/examples/"]');
            for (var k = 0; k < exampleLinks.length; k++) {
                var exLink = exampleLinks[k];
                data.examples.push({
                    title: exLink.textContent.trim(),
                    url: exLink.href
                });
            }
            
            // Imágenes
            var imgs = document.querySelectorAll('img');
            for (var m = 0; m < imgs.length; m++) {
                var img = imgs[m];
                data.images.push({
                    src: img.src,
                    alt: img.alt || '',
                    title: img.title || ''
                });
            }
            
            return data;
        });
        
        console.log('');
        console.log('═══ CONTENIDO EXTRAÍDO ═══');
        console.log('Título: ' + mainContent.title);
        console.log('Secciones: ' + mainContent.sections.length);
        console.log('Tips: ' + mainContent.tips.length);
        console.log('Examples: ' + mainContent.examples.length);
        console.log('Imágenes: ' + mainContent.images.length);
        console.log('');
        
        // Guardar contenido principal
        fs.write(config.outputDir + 'main-content.json', 
                 JSON.stringify(mainContent, null, 2), 'w');
        console.log('✓ Guardado: main-content.json');
        
        // Guardar HTML completo
        fs.write(config.outputDir + 'page.html', page.content, 'w');
        console.log('✓ Guardado: page.html');
        
        // Screenshot
        page.render(config.outputDir + 'page.png');
        console.log('✓ Guardado: page.png');
        
        // Función para descargar página
        function downloadPage(url, filename, callback) {
            var subPage = require('webpage').create();
            subPage.settings.userAgent = config.userAgent;
            
            subPage.open(url, function(status) {
                if (status === 'success') {
                    var content = subPage.evaluate(function() {
                        var article = document.querySelector('article') || 
                                    document.querySelector('.content') ||
                                    document.querySelector('main');
                        
                        return {
                            title: document.querySelector('h1')?.textContent || '',
                            html: article?.innerHTML || '',
                            text: article?.innerText || ''
                        };
                    });
                    
                    fs.write(config.outputDir + filename, 
                             JSON.stringify(content, null, 2), 'w');
                    console.log('  ✓ ' + filename);
                    subPage.close();
                    callback();
                } else {
                    console.log('  ✗ Error: ' + url);
                    subPage.close();
                    callback();
                }
            });
        }
        
        // Descargar todos los tips
        console.log('');
        console.log('═══ DESCARGANDO TIPS ═══');
        var tipIndex = 0;
        
        function downloadNextTip() {
            if (tipIndex >= mainContent.tips.length) {
                // Tips completados, descargar ejemplos
                downloadExamples();
                return;
            }
            
            var tip = mainContent.tips[tipIndex];
            console.log('[' + (tipIndex + 1) + '/' + mainContent.tips.length + '] ' + tip.title);
            
            downloadPage(tip.url, 'tip-' + tip.number + '.json', function() {
                tipIndex++;
                downloadNextTip();
            });
        }
        
        // Descargar todos los ejemplos
        var exampleIndex = 0;
        
        function downloadExamples() {
            console.log('');
            console.log('═══ DESCARGANDO EXAMPLES ═══');
            downloadNextExample();
        }
        
        function downloadNextExample() {
            if (exampleIndex >= mainContent.examples.length) {
                // Ejemplos completados, descargar imágenes
                downloadImages();
                return;
            }
            
            var example = mainContent.examples[exampleIndex];
            console.log('[' + (exampleIndex + 1) + '/' + mainContent.examples.length + '] ' + example.title);
            
            var filename = 'example-' + example.url.split('/').pop() + '.json';
            downloadPage(example.url, filename, function() {
                exampleIndex++;
                downloadNextExample();
            });
        }
        
        // Descargar imágenes
        function downloadImages() {
            console.log('');
            console.log('═══ DESCARGANDO IMÁGENES ═══');
            
            var imgIndex = 0;
            
            function downloadNextImage() {
                if (imgIndex >= mainContent.images.length) {
                    finalize();
                    return;
                }
                
                var img = mainContent.images[imgIndex];
                console.log('[' + (imgIndex + 1) + '/' + mainContent.images.length + '] ' + img.src);
                
                var imgPage = require('webpage').create();
                imgPage.open(img.src, function(status) {
                    if (status === 'success') {
                        // No podemos descargar binarios fácilmente con PhantomJS
                        // Guardar solo la referencia
                        console.log('  ✓ Referencia guardada');
                    }
                    imgPage.close();
                    imgIndex++;
                    downloadNextImage();
                });
            }
            
            if (mainContent.images.length > 0) {
                downloadNextImage();
            } else {
                finalize();
            }
        }
        
        // Finalizar
        function finalize() {
            console.log('');
            console.log('═══════════════════════════════════════════════');
            console.log('  ✅ SCRAPING COMPLETO');
            console.log('═══════════════════════════════════════════════');
            console.log('');
            console.log('Archivos generados en:');
            console.log(config.outputDir);
            console.log('');
            console.log('Contenido:');
            console.log('  - main-content.json (contenido principal)');
            console.log('  - page.html (HTML completo)');
            console.log('  - page.png (screenshot)');
            console.log('  - tip-*.json (' + mainContent.tips.length + ' tips)');
            console.log('  - example-*.json (' + mainContent.examples.length + ' ejemplos)');
            console.log('');
            
            phantom.exit(0);
        }
        
        // Iniciar descarga de tips
        downloadNextTip();
        
    }, 3000); // Esperar 3 segundos para JavaScript
});
