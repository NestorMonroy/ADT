# [TARGET] REORGANIZACIÓN DEFINITIVA: /tmp/ADT COMO PROYECTO SPHINX ÚNICO
**Versión FINAL - Correcta según Análisis Real**
**Fecha:** 2026-01-26

---

## [OK] SITUACIÓN ACTUAL VERIFICADA

```
/tmp/ADT/ [ERROR] NO es proyecto Sphinx (raíz)
+-- [muchos .md] <- Archivos sueltos
+-- traduccion/ [WARNING] Estructura Sphinx INCOMPLETA
| +-- source/ [OK] Tiene las 10 secciones
| +-- index.rst [OK]
| +-- 01-10/ [OK]
| +-- (sin conf.py, sin Makefile)
+-- biblioteca/ Traducciones antiguas
| +-- arc42_documentation/
+-- arc42/ Carpeta vacía
+-- seccion3_diagramas/ 7 PlantUML
+-- docs_maestros/ [OK] 3 documentos
+-- diataxis/ [OK] Framework
+-- scripts/ [OK]
+-- config/ [OK]
+-- [proyectos independientes] arc42_scraper_proxy, vagrant, etc.

/tmp/ADT42/ [OK] Proyecto Sphinx COMPLETO
+-- Makefile [OK]
+-- make.bat [OK]
+-- build/ [OK]
+-- source/ [OK]
 +-- conf.py [OK]
 +-- index.rst [OK]
 +-- 01-10/ [OK]
 +-- biblioteca/ [OK]
```

---

## [TARGET] ESTRUCTURA OBJETIVO FINAL

```
/tmp/ADT/ [STAR] PROYECTO SPHINX ÚNICO
|
+-- Makefile <- Copiado de ADT42
+-- make.bat <- Copiado de ADT42
+-- build/ <- HTML compilado
| +-- html/
|
+-- source/ [STAR] TODO EL CONTENIDO SPHINX
| |
| +-- conf.py <- De ADT42 o config/sphinx/
| +-- index.rst <- Consolidado mejor versión
| +-- _static/ <- CSS, JS
| +-- _templates/ <- Templates
| |
| +-- 01_fundamentos/ Metodología Sección 1
| +-- 02_procedimientos/ Metodología Sección 2
| +-- 03_estandares/ Metodología Sección 3
| +-- 04_reglas_operativas/ Metodología Sección 4
| +-- 05_herramientas_medios/ Metodología Sección 5
| +-- 06_casos_practicos/ Metodología Sección 6
| +-- 07_guias_uso/ Metodología Sección 7
| +-- 08_prompts/ Metodología Sección 8
| +-- 09_referencias/ Metodología Sección 9
| +-- 10_apendices/ Metodología Sección 10
| |
| +-- biblioteca/ [STAR] CONTENIDO TRADUCIDO
| |
| +-- _metadata_biblioteca/
| |
| +-- arc42/ [STAR] arc42 COMO LIBRO
| | +-- metadata_libro.rst
| | +-- index.rst
| | +-- glosario_acumulativo.rst
| | +-- sections/
| | +-- 01_introduction_goals/
| | | +-- original/
| | | +-- traduccion/
| | | | +-- seccion_01_introduccion_objetivos.rst
| | | +-- glosario_seccion.rst
| | | +-- notas_traduccion.rst
| | +-- 02_constraints/
| | | +-- original/
| | | +-- traduccion/
| | | | +-- seccion_02_restricciones.rst
| | | +-- glosario_seccion.rst
| | | +-- notas_traduccion.rst
| | +-- 03_context/
| | | +-- original/
| | | +-- traduccion/
| | | | +-- seccion_03_contexto_alcance.rst
| | | +-- glosario_seccion.rst
| | | +-- notas_traduccion.rst
| | | +-- README_SECCION_3.md
| | | +-- diagramas/ [STAR] 7 PlantUML
| | | +-- *.puml (7)
| | | +-- *.png (7)
| | +-- 04_solution_strategy/
| | +-- ... (hasta 12_glossary)
| |
| +-- informatica/
| +-- programacion/
| +-- full_stack/
| +-- python/
| +-- typescript/
|
+-- docs_maestros/ Documentos fundamentales
| +-- ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
| +-- PROMPT_MAESTRO_SPHINX_TRADUCCION.md
| +-- ESTRUCTURA_DE_BIBLIOTECA.md
| +-- README.md
|
+-- diataxis/ Framework (NO Sphinx)
| +-- tutorials/
| +-- how_to_guides/
| +-- reference/
| +-- explanation/
|
+-- scripts/ Automatización
| +-- build/
| +-- traduccion/
| +-- utils/
|
+-- config/ Configuraciones
 +-- sphinx/
 +-- templates/
```

---

## [PROCESSING] PLAN DE CONSOLIDACIÓN - 5 FASES

### FASE 0: Backup (5 min)

```bash
cd /tmp
tar -czf ADT_backup_definitivo_$(date +%Y%m%d_%H%M%S).tar.gz ADT/ ADT42/
ls -lh ADT_backup_definitivo_*.tar.gz
```

---

### FASE 1: Crear Estructura Sphinx en /tmp/ADT (10 min)

```bash
cd /tmp/ADT

# 1. Copiar archivos Sphinx de ADT42
cp /tmp/ADT42/Makefile ./
cp /tmp/ADT42/make.bat ./

# 2. Crear carpeta build
mkdir -p build

# 3. Mover traduccion/source/ a source/
mv traduccion/source ./

# 4. Eliminar carpeta traduccion vacía
rmdir traduccion

# 5. Copiar conf.py si no existe
if [ ! -f source/conf.py ]; then
 cp /tmp/ADT42/source/conf.py source/
fi

# 6. Usar mejor index.rst (de ADT42 si es mejor)
# Comparar primero
wc -l source/index.rst /tmp/ADT42/source/index.rst
# Si ADT42 es mejor (más líneas):
cp /tmp/ADT42/source/index.rst source/index.rst.backup
cp /tmp/ADT42/source/index.rst source/

# 7. Crear _static y _templates si no existen
mkdir -p source/_static
mkdir -p source/_templates

# Verificar
echo "[OK] Estructura creada:"
ls -la /tmp/ADT/ | grep -E "Makefile|make.bat|build|source"
```

**Resultado:**
```
/tmp/ADT/
+-- Makefile [OK]
+-- make.bat [OK]
+-- build/ [OK]
+-- source/ [OK]
 +-- conf.py [OK]
 +-- index.rst [OK]
 +-- 01-10/ [OK] (ya estaban)
 +-- _static/ [OK]
 +-- _templates/ [OK]
```

---

### FASE 2: Consolidar biblioteca/ (15 min)

```bash
cd /tmp/ADT/source

# 1. Si biblioteca/ NO existe, copiar de ADT42
if [ ! -d "biblioteca" ]; then
 echo "Creando biblioteca/ desde ADT42..."
 cp -r /tmp/ADT42/source/biblioteca ./
fi

# 2. Crear estructura base si está vacía
mkdir -p biblioteca/_metadata_biblioteca
mkdir -p biblioteca/informatica/programacion/{full_stack,frontend,backend,python,typescript}
mkdir -p biblioteca/ingenieria/sistemas
mkdir -p biblioteca/ciencias/biologia

# 3. Crear estructura arc42
mkdir -p biblioteca/arc42/sections

cd biblioteca/arc42/sections

# 4. Crear 12 secciones de arc42
for i in {01..12}; do
 case $i in
 01) name="01_introduction_goals" ;;
 02) name="02_constraints" ;;
 03) name="03_context" ;;
 04) name="04_solution_strategy" ;;
 05) name="05_building_blocks" ;;
 06) name="06_runtime" ;;
 07) name="07_deployment" ;;
 08) name="08_concepts" ;;
 09) name="09_decisions" ;;
 10) name="10_quality" ;;
 11) name="11_risks_tech_debt" ;;
 12) name="12_glossary" ;;
 esac

 mkdir -p "$name"/{original,traduccion,diagramas}
 touch "$name"/glosario_seccion.rst
 touch "$name"/notas_traduccion.rst
done

# 5. Crear archivos raíz de arc42
cd /tmp/ADT/source/biblioteca/arc42
touch metadata_libro.rst
touch index.rst
touch glosario_acumulativo.rst

# Verificar
tree -L 2 /tmp/ADT/source/biblioteca/arc42/
```

---

### FASE 3: Mover Traducciones arc42 (10 min)

```bash
# Sección 1
cp /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/01/seccion_01_CORRECTA.rst \
 /tmp/ADT/source/biblioteca/arc42/sections/01_introduction_goals/traduccion/seccion_01_introduccion_objetivos.rst

# Sección 2
cp /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/02/seccion_02_restricciones.rst \
 /tmp/ADT/source/biblioteca/arc42/sections/02_constraints/traduccion/

# Sección 3
cp /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/03/seccion_03_contexto_alcance.rst \
 /tmp/ADT/source/biblioteca/arc42/sections/03_context/traduccion/

# README Sección 3
cp /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/03/README_SECCION_3.md \
 /tmp/ADT/source/biblioteca/arc42/sections/03_context/

echo "[OK] Traducciones copiadas"
ls -la /tmp/ADT/source/biblioteca/arc42/sections/0{1,2,3}_*/traduccion/
```

---

### FASE 4: Mover Diagramas PlantUML (5 min)

```bash
# Copiar .puml y .png
cp /tmp/ADT/seccion3_diagramas/*.puml \
 /tmp/ADT/source/biblioteca/arc42/sections/03_context/diagramas/

cp /tmp/ADT/seccion3_diagramas/*.png \
 /tmp/ADT/source/biblioteca/arc42/sections/03_context/diagramas/

# Verificar
echo "[OK] Diagramas copiados:"
ls -la /tmp/ADT/source/biblioteca/arc42/sections/03_context/diagramas/
# Debe mostrar: 14 archivos (7 .puml + 7 .png)
```

---

### FASE 5: Limpieza Final (15 min)

```bash
cd /tmp/ADT

# 1. Eliminar carpetas antiguas/duplicadas
rm -rf biblioteca/arc42
rm -rf biblioteca/arc42_documentation
rm -rf seccion3_diagramas
rm -rf arc42 # carpeta vacía en raíz

# 2. Mover ADT42 como backup
mv /tmp/ADT42 /tmp/ADT42_backup

# 3. Mover proyectos independientes
mkdir -p /tmp/proyectos_independientes
for proj in arc42_scraper_proxy arc42-vagrant arc42-vagrant-complete \
 backend-modular-v2 arc42-scraper-project arc42-scraper \
 arc42_cache arc42_html_cache; do
 [ -d "$proj" ] && mv "$proj" /tmp/proyectos_independientes/
done

# 4. Limpiar archivos .md sueltos en raíz (opcional)
# mkdir -p docs_historicos
# mv *.md docs_historicos/ 2>/dev/null

# 5. COMPILAR Sphinx
cd /tmp/ADT
make clean
make html

# 6. Verificar
if [ -f "build/html/index.html" ]; then
 echo "[OK][OK][OK] COMPILACIÓN EXITOSA [OK][OK][OK]"
 ls -lh build/html/index.html
else
 echo "[ERROR] Error en compilación"
 cat build/make.log
fi
```

---

## [OK] CHECKLIST FINAL

### Proyecto Sphinx Base
- [ ] `/tmp/ADT/Makefile` existe
- [ ] `/tmp/ADT/make.bat` existe
- [ ] `/tmp/ADT/build/` existe
- [ ] `/tmp/ADT/source/conf.py` existe
- [ ] `/tmp/ADT/source/index.rst` existe

### Secciones Metodología
- [ ] `/tmp/ADT/source/01_fundamentos/` hasta `10_apendices/` (10 carpetas)
- [ ] Cada una tiene `index.rst`

### Biblioteca y arc42
- [ ] `/tmp/ADT/source/biblioteca/` existe
- [ ] `/tmp/ADT/source/biblioteca/arc42/metadata_libro.rst` existe
- [ ] `/tmp/ADT/source/biblioteca/arc42/sections/` tiene 12 carpetas
- [ ] Sección 01: `01_introduction_goals/traduccion/seccion_01...rst`
- [ ] Sección 02: `02_constraints/traduccion/seccion_02...rst`
- [ ] Sección 03: `03_context/traduccion/seccion_03...rst`
- [ ] Sección 03: `03_context/diagramas/` tiene 14 archivos

### Compilación
- [ ] `cd /tmp/ADT && make html` sin errores
- [ ] `/tmp/ADT/build/html/index.html` generado
- [ ] Se puede abrir en navegador

### Limpieza
- [ ] NO existe `/tmp/ADT/traduccion/`
- [ ] NO existe `/tmp/ADT/arc42/` en raíz
- [ ] NO existe `/tmp/ADT/seccion3_diagramas/`
- [ ] `/tmp/ADT42` movido a backup
- [ ] Proyectos independientes en `/tmp/proyectos_independientes/`

---

## [TABLE] ANTES vs DESPUÉS

### ANTES
```
/tmp/
+-- ADT/ [ERROR] NO es proyecto Sphinx
| +-- traduccion/source/ (sin Makefile)
| +-- arc42/ (vacío)
| +-- [proyectos mezclados]
+-- ADT42/ (proyecto Sphinx duplicado)
```

### DESPUÉS
```
/tmp/
+-- ADT/ [STAR] PROYECTO SPHINX ÚNICO
| +-- Makefile
| +-- build/html/
| +-- source/
| | +-- conf.py
| | +-- 01-10/
| | +-- biblioteca/arc42/
| +-- docs_maestros/
+-- ADT42_backup/
+-- proyectos_independientes/
```

---

## [START] PRÓXIMOS PASOS

### 1. Compilar y Verificar
```bash
cd /tmp/ADT
make html
firefox build/html/index.html
```

### 2. Crear metadata_libro.rst
Ver contenido en versión anterior de este documento

### 3. Continuar Sección 4
- Tips de arc42.org
- 5-7 diagramas PlantUML
- Calidad [STAR][STAR][STAR][STAR][STAR]

---

## [PENDING] TIEMPO TOTAL

- Fase 0: 5 min (backup)
- Fase 1: 10 min (estructura Sphinx)
- Fase 2: 15 min (biblioteca)
- Fase 3: 10 min (traducciones)
- Fase 4: 5 min (diagramas)
- Fase 5: 15 min (limpieza + compilar)

**TOTAL: 60 minutos (1 hora)**

---

**¿Proceder con reorganización?**
