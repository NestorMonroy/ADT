# Reglas de Estructura del Proyecto ADT

Basado en: source/docs_maestros/REGLAS_ESTRUCTURA_PROYECTO.rst

## Regla Fundamental

REGLA MAESTRA (OBLIGATORIA):

**Solo va a `source/` el contenido que se documenta/compila en HTML.**

**Las herramientas y scripts de proyecto quedan en la raiz.**

Esta regla es la base de toda la organizacion del proyecto y debe ser SIEMPRE respetada.

## Estructura Obligatoria

### Raiz del Proyecto

```
ADT/
+-- Makefile [OK] Herramienta de compilacion
+-- make.bat [OK] Batch de compilacion (Windows)
+-- build/ [OK] Salida compilada (HTML)
+-- source/ [OK] TODO EL CONTENIDO DOCUMENTAL
+-- config/ [OK] Configuraciones del proyecto
+-- scripts/ [OK] Scripts de automatizacion
+-- tools/ [OK] Herramientas externas
+-- .codex/ [OK] Configuracion Codex (herramienta)
+-- .mywork/ [OK] Trabajo en progreso (herramienta)
```

CRITERIO: Archivos y carpetas que son HERRAMIENTAS o UTILIDADES del proyecto, NO contenido a documentar.

### Carpeta source/

```
source/
+-- conf.py [OK] Configuracion Sphinx
+-- index.rst [OK] Indice principal
+-- _static/ [OK] Recursos estaticos
+-- _templates/ [OK] Templates Sphinx
|
+-- 01_fundamentos/ [OK] Contenido documental
+-- 02_procedimientos/ [OK] Contenido documental
+-- 03_estandares/ [OK] Contenido documental
+-- 04_reglas_operativas/ [OK] Contenido documental
+-- 05_herramientas_medios/ [OK] Contenido documental
+-- 06_casos_practicos/ [OK] Contenido documental
+-- 07_guias_uso/ [OK] Contenido documental
+-- 08_prompts/ [OK] Contenido documental
+-- 09_referencias/ [OK] Contenido documental
+-- 10_apendices/ [OK] Contenido documental
|
+-- biblioteca/ [OK] Contenido documental
+-- diataxis/ [OK] Contenido documental
+-- docs/ [OK] Contenido documental
+-- docs_maestros/ [OK] Contenido documental
```

CRITERIO: Todo lo que se COMPILA a HTML y es parte de la DOCUMENTACION.

## Arbol de Decision

Pregunta: **Esto va en `source/` o en la raiz?**

```
¿Es contenido que quieres documentar/mostrar en HTML?
|
+- SI -> Va en source/
| Ejemplos:
| • Guias de usuario (.rst, .md)
| • Tutoriales
| • Referencias
| • Documentacion de procedimientos
| • Frameworks de documentacion (Diataxis)
| • Glosarios
| • Biblioteca de traducciones
|
+- NO -> Va en la raiz (en carpeta apropiada)
 Ejemplos:
 • Scripts de build (scripts/)
 • Configuraciones de proyecto (config/)
 • Herramientas externas (tools/)
 • Makefiles
 • Archivos .tar.gz de backups
 • Configuracion Codex (.codex/)
```

## Ejemplos Especificos

### Contenido Documental (-> source/)

| Archivo/Carpeta | Razon |
|-----------------|-------|
| `diataxis/` | Framework de documentacion (se documenta) |
| `docs/` | Documentacion tecnica (se compila a HTML) |
| `docs_maestros/` | Documentos fundamentales (se compilan a HTML) |
| `biblioteca/arc42/` | Traducciones arc42 (se compilan a HTML) |
| `01_fundamentos/` | Metodologia de traduccion (se documenta) |
| `glosario.rst` | Glosario (se compila a HTML) |
| `tutorial.md` | Tutorial (se compila a HTML) |

### Herramientas/Utilidades (-> raiz)

| Archivo/Carpeta | Razon |
|-----------------|-------|
| `tools/plantuml.jar` | Herramienta para compilar diagramas |
| `scripts/deploy.sh` | Script de despliegue (automatizacion) |
| `scripts/clean.sh` | Script de limpieza (utilidad) |
| `config/` | Configuraciones del proyecto |
| `Makefile` | Herramienta de build |
| `backup.tar.gz` | Archivo de respaldo (no se documenta) |
| `.codex/` | Configuracion de Codex (herramienta) |
| `.mywork/` | Trabajo en progreso (no es contenido final) |

## Excepciones y Casos Especiales

### build/ - Salida Compilada

**Ubicacion:** Raiz del proyecto

**Razon:** Es salida/artefacto, no contenido fuente

**Reglas:**
- NO debe editarse manualmente
- Se regenera con `make html`
- Debe estar en .gitignore

### _static/ y _templates/ en source/

**Ubicacion:** source/_static/ y source/_templates/

**Razon:** Aunque no son "contenido" en si, van en source/ porque Sphinx los necesita DURANTE LA COMPILACION para generar el HTML correcto.

**Contenido:**
- _static/: CSS, JS, imagenes para la documentacion
- _templates/: Templates de Sphinx para personalizar HTML

## Validacion de la Estructura

### Checklist de Validacion

Antes de hacer commit, verifica:

```
[ ] ¿Todo en source/ se compila a HTML?
[ ] ¿Las herramientas estan en tools/?
[ ] ¿Los scripts estan en scripts/?
[ ] ¿Las configuraciones estan en config/?
[ ] ¿No hay archivos .tar.gz en source/?
[ ] ¿No hay scripts .py o .sh en source/?
[ ] ¿build/ esta en .gitignore?
[ ] ¿.codex/ esta en la raiz (no en source/)?
[ ] ¿.mywork/ esta en la raiz (no en source/)?
```

### Comando de Verificacion

```bash
# Ver estructura de raiz
ls -d ADT/*/

# Debe mostrar:
# build/ config/ scripts/ source/ tools/ .codex/ .mywork/

# Ver contenido de source/
ls -d ADT/source/*/

# Debe mostrar solo carpetas de contenido documental
```

### Script de Validacion

```bash
bash scripts/validar_estructura.sh
```

Este script verifica:
- Estructura de directorios correcta
- Nomenclatura de archivos
- Archivos en ubicaciones apropiadas
- Conformidad con reglas

## Consecuencias de NO Seguir las Reglas

Si NO se sigue esta estructura:

[ERROR] **Problemas que ocurriran:**

1. Sphinx intentara compilar herramientas como si fueran documentacion
2. La documentacion no se encontrara donde se espera
3. Los scripts no estaran accesibles desde la raiz
4. Confusion entre contenido y herramientas
5. Estructura inconsistente y dificil de mantener
6. Builds fallaran con errores confusos

## Migracion de Archivos

### Si encuentras un archivo en el lugar incorrecto

**Procedimiento:**

1. **Identificar** si es contenido o herramienta

 PREGUNTA: ¿Se compila a HTML y se muestra en la documentacion?
 - SI -> Es contenido -> Debe estar en source/
 - NO -> Es herramienta -> Debe estar en raiz

2. **Mover** a la ubicacion correcta:

 ```bash
 # Si es contenido documental:
 mv archivo.rst source/carpeta_apropiada/

 # Si es herramienta/script:
 mv script.py scripts/
 mv tool.jar tools/
 mv config.yml config/
 ```

3. **Actualizar** referencias si las hay

 Buscar y reemplazar paths en:
 - Toctrees
 - Cross-references
 - Imports (si es codigo)
 - Configuracion

4. **Recompilar** para verificar:

 ```bash
 make clean
 make html
 ```

5. **Verificar** que todo funciona

 - Build exitoso
 - Enlaces no rotos
 - Scripts ejecutables desde raiz

6. **Commit** con mensaje apropiado:

 ```bash
 git add <archivos>
 git commit -m "refactor(estructura): mover <archivo> a ubicacion correcta

 Muevo <archivo> de <origen> a <destino> para cumplir con
 REGLAS_ESTRUCTURA_PROYECTO.rst"
 ```

## Casos Comunes de Confusion

### "Mi script genera documentacion, va en source/?"

**NO.** El script es una HERRAMIENTA, va en scripts/.

La SALIDA del script (archivos .rst generados) va en source/.

Ejemplo:
```bash
# Script
scripts/generar_glosario.py

# Salida del script
source/10_apendices/glosario_generado.rst
```

### "Tengo un archivo de configuracion para Sphinx, va en config/?"

**DEPENDE.**

- conf.py de Sphinx -> source/ (Sphinx lo requiere ahi)
- Configuraciones adicionales del proyecto -> config/

### "Donde van los archivos .gitkeep?"

**DEPENDE** del directorio:

- .gitkeep en source/ -> Para mantener estructura de contenido
- .gitkeep en .mywork/ -> Para mantener estructura de trabajo
- .gitkeep en scripts/ -> Para mantener estructura de herramientas

## Reglas de Nomenclatura

### Capitulos (source/XX_nombre/)

FORMATO: `XX_nombre/`

DONDE:
- XX = Numero con cero padding (01, 02, ..., 10)
- nombre = snake_case, sin espacios

EJEMPLOS:
- [OK] 01_fundamentos/
- [OK] 10_apendices/
- [ERROR] 1_fundamentos/ (falta cero padding)
- [ERROR] 01-fundamentos/ (guion, debe ser underscore)
- [ERROR] 01 fundamentos/ (espacio)

### Archivos RST (source/.../*.rst)

FORMATO: `nombre_archivo.rst`

DONDE:
- nombre_archivo = snake_case, sin espacios
- Extension siempre .rst (no .RST ni .Rst)

EJEMPLOS:
- [OK] glosario_adt.rst
- [OK] workflow_general.rst
- [ERROR] Glosario-ADT.rst (kebab-case)
- [ERROR] Workflow General.rst (espacios)

### Directorios con Prefijo Underscore

FORMATO: `_nombre/`

DONDE:
- Prefijo _ indica directorio especial (metadata, templates, etc)
- No se incluye directamente en toctree

EJEMPLOS:
- [OK] _metadata/
- [OK] _templates/
- [OK] _static/

## Referencias

Documento completo:
- source/docs_maestros/REGLAS_ESTRUCTURA_PROYECTO.rst

Script de validacion:
- scripts/validar_estructura.sh

## Notas Finales

- Estas reglas son NORMATIVAS (obligatorias)
- Todos los colaboradores deben conocerlas
- Cualquier excepcion debe justificarse y documentarse
- En caso de duda, consultar con equipo antes de crear estructura nueva
- La coherencia estructural es critica para mantenibilidad del proyecto

**ESTE DOCUMENTO ES NORMATIVO - CUMPLIMIENTO OBLIGATORIO**
