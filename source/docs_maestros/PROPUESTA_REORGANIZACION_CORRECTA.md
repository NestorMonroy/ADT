# 🔄 REORGANIZACIÓN DEFINITIVA: /tmp/ADT COMO PROYECTO SPHINX ÚNICO
**Basada en Documentos Maestros - Versión CORRECTA**  
**Fecha:** 2026-01-26

---

## ✅ CONCEPTO CLARO

**/tmp/ADT ES y DEBE SER el ÚNICO proyecto Sphinx.**

**Acción:** Consolidar ADT42 → ADT, eliminar duplicación, estructura según docs maestros.

---

## 🎯 ESTRUCTURA FINAL DE /tmp/ADT (Proyecto Sphinx)

```
/tmp/ADT/                              ⭐ PROYECTO SPHINX ÚNICO
│
├── Makefile                           ← Para compilar (make html)
├── make.bat                           ← Para compilar en Windows
├── build/                             ← HTML generado aquí
│   └── html/
│       └── index.html
│
├── source/                            ⭐ CÓDIGO FUENTE SPHINX
│   │
│   ├── conf.py                        ← Configuración Sphinx
│   ├── index.rst                      ← Índice principal del proyecto
│   ├── _static/                       ← CSS, JS, imágenes estáticas
│   ├── _templates/                    ← Templates Jinja2
│   │
│   ├── 01_fundamentos/                📖 Sección 1: Base conceptual
│   │   ├── index.rst
│   │   ├── glosario_traduccion.rst
│   │   ├── principios_fundamentales.rst
│   │   ├── taxonomias/
│   │   │   ├── index.rst
│   │   │   ├── tipos_traduccion.rst
│   │   │   ├── tipos_documento.rst
│   │   │   └── niveles_fidelidad.rst
│   │   └── metamodelos/
│   │       ├── index.rst
│   │       ├── estructura_libro.rst
│   │       └── estructura_manual.rst
│   │
│   ├── 02_procedimientos/             📖 Sección 2: Workflows
│   │   ├── index.rst
│   │   ├── workflow_general.rst
│   │   ├── modo_alta_fidelidad/
│   │   ├── modo_marcado_visual/
│   │   └── verificacion_calidad/
│   │
│   ├── 03_estandares/                 📖 Sección 3: Normas
│   │   ├── index.rst
│   │   ├── terminologia/
│   │   ├── formato_por_medio/
│   │   └── calidad/
│   │
│   ├── 04_reglas_operativas/          📖 Sección 4: Reglas específicas
│   │   ├── index.rst
│   │   ├── reglas_traduccion/
│   │   ├── escenarios_traduccion/
│   │   └── matrices_decision/
│   │
│   ├── 05_herramientas_medios/        📖 Sección 5: LaTeX/Sphinx/Markdown
│   │   ├── index.rst
│   │   ├── latex/
│   │   ├── sphinx/
│   │   ├── markdown/
│   │   └── equivalencias/
│   │
│   ├── 06_casos_practicos/            📖 Sección 6: Ejemplos
│   │   ├── index.rst
│   │   ├── antes_despues/
│   │   ├── errores_comunes/
│   │   └── casos_exito/
│   │
│   ├── 07_guias_uso/                  📖 Sección 7: Tutoriales
│   │   ├── index.rst
│   │   ├── guia_rapida.rst
│   │   └── tutorial_completo.rst
│   │
│   ├── 08_prompts/                    📖 Sección 8: Prompts producción
│   │   ├── index.rst
│   │   ├── prompt_maestro_latex.rst
│   │   ├── prompt_maestro_sphinx.rst
│   │   └── prompt_maestro_markdown.rst
│   │
│   ├── 09_referencias/                📖 Sección 9: Bibliografía
│   │   ├── index.rst
│   │   ├── bibliografia.rst
│   │   └── cheatsheets/
│   │
│   ├── 10_apendices/                  📖 Sección 10: Info adicional
│   │   ├── index.rst
│   │   └── historia_versiones.rst
│   │
│   └── biblioteca/                    ⭐ CONTENIDO TRADUCIDO
│       │
│       ├── _metadata_biblioteca/     Metodología de clasificación
│       │   ├── META_BIB_001_Sistema_Clasificacion.rst
│       │   ├── META_BIB_002_Guia_Organizacion.rst
│       │   └── META_BIB_003_Esquema_Codificacion.rst
│       │
│       ├── arc42/                     ⭐ arc42 COMO LIBRO
│       │   │
│       │   ├── metadata_libro.rst     Info bibliográfica completa
│       │   ├── index.rst              Índice del libro arc42
│       │   ├── glosario_acumulativo.rst
│       │   │
│       │   └── sections/              12 secciones de arc42
│       │       │
│       │       ├── 01_introduction_goals/
│       │       │   ├── original/
│       │       │   │   └── section_01.html
│       │       │   ├── traduccion/
│       │       │   │   └── seccion_01_introduccion_objetivos.rst
│       │       │   ├── glosario_seccion.rst
│       │       │   └── notas_traduccion.rst
│       │       │
│       │       ├── 02_constraints/
│       │       │   ├── original/
│       │       │   ├── traduccion/
│       │       │   │   └── seccion_02_restricciones.rst
│       │       │   ├── glosario_seccion.rst
│       │       │   └── notas_traduccion.rst
│       │       │
│       │       ├── 03_context/
│       │       │   ├── original/
│       │       │   ├── traduccion/
│       │       │   │   └── seccion_03_contexto_alcance.rst
│       │       │   ├── glosario_seccion.rst
│       │       │   ├── notas_traduccion.rst
│       │       │   ├── README_SECCION_3.md
│       │       │   └── diagramas/    ⭐ 7 PlantUML + PNG
│       │       │       ├── 01_contexto_simple.puml
│       │       │       ├── 02_contexto_categorizacion.puml
│       │       │       ├── 03_contexto_negocio_tecnico.puml
│       │       │       ├── 04_flujo_datos.puml
│       │       │       ├── 05_dependencias_transitivas.puml
│       │       │       ├── 06_contexto_riesgos.puml
│       │       │       ├── 07_contexto_puertos.puml
│       │       │       ├── contexto_simple_webshop.png
│       │       │       ├── contexto_categorizacion.png
│       │       │       ├── contexto_negocio_vs_tecnico.png
│       │       │       ├── contexto_flujo_datos.png
│       │       │       ├── dependencias_transitivas.png
│       │       │       ├── contexto_con_riesgos.png
│       │       │       └── contexto_con_puertos.png
│       │       │
│       │       ├── 04_solution_strategy/
│       │       │   ├── original/
│       │       │   ├── traduccion/
│       │       │   ├── glosario_seccion.rst
│       │       │   ├── notas_traduccion.rst
│       │       │   └── diagramas/
│       │       │
│       │       ├── 05_building_blocks/
│       │       ├── 06_runtime/
│       │       ├── 07_deployment/
│       │       ├── 08_concepts/
│       │       ├── 09_decisions/
│       │       ├── 10_quality/
│       │       ├── 11_risks_tech_debt/
│       │       └── 12_glossary/
│       │
│       └── informatica/               Libros de informática
│           ├── programacion/
│           │   ├── full_stack/
│           │   │   └── Modern_Full_Stack_Development_Zammetti_2ed/
│           │   │       ├── metadata_libro.rst
│           │   │       ├── index.rst
│           │   │       ├── Chapter_01_Server_Side_Action/
│           │   │       │   ├── original/
│           │   │       │   ├── traduccion/
│           │   │       │   └── glosario_capitulo.rst
│           │   │       └── ... (14 capítulos)
│           │   ├── frontend/
│           │   ├── backend/
│           │   ├── python/
│           │   └── typescript/
│           └── inteligencia_artificial/
│
├── docs_maestros/                     📚 Documentos fundamentales
│   ├── ARQUITECTURA_DOCUMENTAL_TRADUCCION.md
│   ├── PROMPT_MAESTRO_SPHINX_TRADUCCION.md
│   ├── ESTRUCTURA_DE_BIBLIOTECA.md
│   ├── README.md
│   └── PROPUESTA_REORGANIZACION_CORRECTA.md (este archivo)
│
├── diataxis/                          Framework Diátaxis (NO Sphinx)
│   ├── tutorials/
│   ├── how_to_guides/
│   ├── reference/
│   └── explanation/
│
├── scripts/                           Automatización
│   ├── build/
│   │   ├── build_all.sh
│   │   └── build_sphinx.sh
│   ├── traduccion/
│   └── utils/
│
└── config/                            Configuraciones
    ├── sphinx/
    └── templates/
```

---

## 🔄 PLAN DE CONSOLIDACIÓN - 6 FASES

### FASE 0: Backup Completo (5 min)

```bash
# Backup ANTES de cualquier cambio
cd /tmp
tar -czf ADT_backup_final_$(date +%Y%m%d_%H%M%S).tar.gz ADT/ ADT42/

# Verificar backup
ls -lh ADT_backup_final_*.tar.gz
```

---

### FASE 1: Copiar Archivos Sphinx de ADT42 a ADT (5 min)

**Acción:** Traer Makefile, conf.py y estructura build de ADT42 a ADT

```bash
# Copiar archivos de build Sphinx
cp /tmp/ADT42/Makefile /tmp/ADT/
cp /tmp/ADT42/make.bat /tmp/ADT/

# Crear carpeta build si no existe
mkdir -p /tmp/ADT/build

# Verificar que ADT/source/ existe (ya existe según análisis)
ls -la /tmp/ADT/source/

# Si ADT/source NO tiene conf.py, copiar de ADT42
if [ ! -f /tmp/ADT/source/conf.py ]; then
    cp /tmp/ADT42/source/conf.py /tmp/ADT/source/
fi

# Si ADT/source NO tiene index.rst completo, usar el de ADT42
if [ ! -f /tmp/ADT/source/index.rst ] || [ $(wc -l < /tmp/ADT/source/index.rst) -lt 50 ]; then
    cp /tmp/ADT42/source/index.rst /tmp/ADT/source/
fi
```

**Resultado:**
```
/tmp/ADT/
├── Makefile        ✅ Copiado de ADT42
├── make.bat        ✅ Copiado de ADT42
├── build/          ✅ Creado
└── source/
    ├── conf.py     ✅ De ADT42 si faltaba
    └── index.rst   ✅ De ADT42 si faltaba
```

---

### FASE 2: Consolidar Secciones 01-10 (10 min)

**Acción:** Asegurar que /tmp/ADT/source/ tiene las 10 secciones completas

```bash
cd /tmp/ADT/source

# Verificar qué carpetas existen
existing=$(ls -d 0*_*/ 2>/dev/null | wc -l)
echo "Secciones existentes en ADT: $existing"

# Si faltan secciones, copiar de ADT42
if [ $existing -lt 10 ]; then
    echo "Copiando secciones faltantes de ADT42..."
    for dir in /tmp/ADT42/source/0*_*/; do
        dirname=$(basename "$dir")
        if [ ! -d "/tmp/ADT/source/$dirname" ]; then
            cp -r "$dir" /tmp/ADT/source/
            echo "  Copiado: $dirname"
        fi
    done
fi

# Verificar
ls -d /tmp/ADT/source/0*_*/ | sort
# Debe mostrar: 01_fundamentos/ hasta 10_apendices/
```

---

### FASE 3: Consolidar biblioteca/ (15 min)

**Acción:** Asegurar que source/biblioteca/ existe y tiene estructura correcta

```bash
cd /tmp/ADT/source

# Si biblioteca/ NO existe, copiar de ADT42
if [ ! -d "biblioteca" ]; then
    echo "Copiando biblioteca/ de ADT42..."
    cp -r /tmp/ADT42/source/biblioteca ./
fi

# Crear estructura base de biblioteca/ si está vacía
mkdir -p biblioteca/_metadata_biblioteca
mkdir -p biblioteca/informatica/programacion/{full_stack,frontend,backend,python,typescript}
mkdir -p biblioteca/ingenieria/sistemas
mkdir -p biblioteca/ciencias/biologia

# Crear estructura arc42
mkdir -p biblioteca/arc42/sections

# Crear las 12 carpetas de secciones arc42
cd biblioteca/arc42/sections
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

# Volver a raíz de biblioteca/arc42
cd /tmp/ADT/source/biblioteca/arc42

# Crear archivos raíz si no existen
touch metadata_libro.rst
touch index.rst
touch glosario_acumulativo.rst
```

**Resultado:**
```
/tmp/ADT/source/biblioteca/
├── _metadata_biblioteca/
├── arc42/
│   ├── metadata_libro.rst
│   ├── index.rst
│   ├── glosario_acumulativo.rst
│   └── sections/
│       ├── 01_introduction_goals/
│       │   ├── original/
│       │   ├── traduccion/
│       │   ├── diagramas/
│       │   ├── glosario_seccion.rst
│       │   └── notas_traduccion.rst
│       └── ... (12 secciones)
└── informatica/
```

---

### FASE 4: Mover Traducciones arc42 Existentes (10 min)

**Acción:** Mover las 3 secciones ya traducidas a su ubicación en biblioteca/arc42/

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

# README de Sección 3
cp /tmp/ADT/biblioteca/arc42_documentation/traducciones/sections/03/README_SECCION_3.md \
   /tmp/ADT/source/biblioteca/arc42/sections/03_context/
```

---

### FASE 5: Mover Diagramas PlantUML (5 min)

**Acción:** Mover 7 diagramas de Sección 3

```bash
# Copiar archivos .puml
cp /tmp/ADT/seccion3_diagramas/*.puml \
   /tmp/ADT/source/biblioteca/arc42/sections/03_context/diagramas/

# Copiar archivos .png
cp /tmp/ADT/seccion3_diagramas/*.png \
   /tmp/ADT/source/biblioteca/arc42/sections/03_context/diagramas/

# Verificar
ls -l /tmp/ADT/source/biblioteca/arc42/sections/03_context/diagramas/
# Debe mostrar: 14 archivos (7 .puml + 7 .png)
```

---

### FASE 6: Limpieza y Compilación (15 min)

**Acción:** Eliminar duplicados y compilar

```bash
# 1. Eliminar estructuras antiguas
rm -rf /tmp/ADT/biblioteca/arc42
rm -rf /tmp/ADT/biblioteca/arc42_documentation
rm -rf /tmp/ADT/seccion3_diagramas
rm -rf /tmp/ADT/traduccion  # Ya está todo en source/

# 2. Mover ADT42 como backup
mv /tmp/ADT42 /tmp/ADT42_backup_consolidado

# 3. Mover proyectos independientes
mkdir -p /tmp/proyectos_independientes
for proj in arc42_scraper_proxy arc42-vagrant arc42-vagrant-complete backend-modular-v2 arc42-scraper-project arc42_cache arc42_html_cache; do
    [ -d "/tmp/ADT/$proj" ] && mv "/tmp/ADT/$proj" /tmp/proyectos_independientes/
done

# 4. Limpiar archivos sueltos en raíz de ADT
cd /tmp/ADT
rm -f *.py *.sh *.md *.txt 2>/dev/null  # Solo si no son importantes

# 5. COMPILAR Sphinx
cd /tmp/ADT
make clean
make html

# 6. Verificar compilación
ls -la build/html/index.html
echo "✅ Compilación exitosa si se ve el archivo index.html"
```

---

## ✅ CHECKLIST DE VERIFICACIÓN FINAL

### Estructura Básica
- [ ] `/tmp/ADT/Makefile` existe
- [ ] `/tmp/ADT/make.bat` existe
- [ ] `/tmp/ADT/build/` existe
- [ ] `/tmp/ADT/source/` existe

### Configuración Sphinx
- [ ] `/tmp/ADT/source/conf.py` existe
- [ ] `/tmp/ADT/source/index.rst` existe
- [ ] `/tmp/ADT/source/_static/` existe
- [ ] `/tmp/ADT/source/_templates/` existe

### 10 Secciones Metodología
- [ ] `/tmp/ADT/source/01_fundamentos/` existe
- [ ] `/tmp/ADT/source/02_procedimientos/` existe
- [ ] ... (todas hasta 10)

### Biblioteca
- [ ] `/tmp/ADT/source/biblioteca/` existe
- [ ] `/tmp/ADT/source/biblioteca/_metadata_biblioteca/` existe
- [ ] `/tmp/ADT/source/biblioteca/arc42/` existe
- [ ] `/tmp/ADT/source/biblioteca/informatica/` existe

### arc42 como Libro
- [ ] `/tmp/ADT/source/biblioteca/arc42/metadata_libro.rst` existe
- [ ] `/tmp/ADT/source/biblioteca/arc42/index.rst` existe
- [ ] `/tmp/ADT/source/biblioteca/arc42/glosario_acumulativo.rst` existe
- [ ] `/tmp/ADT/source/biblioteca/arc42/sections/` tiene 12 carpetas

### Traducciones arc42
- [ ] Sección 01 en: `01_introduction_goals/traduccion/`
- [ ] Sección 02 en: `02_constraints/traduccion/`
- [ ] Sección 03 en: `03_context/traduccion/`
- [ ] Diagramas en: `03_context/diagramas/` (14 archivos)

### Compilación
- [ ] `cd /tmp/ADT && make html` funciona sin errores
- [ ] `/tmp/ADT/build/html/index.html` se genera
- [ ] Se puede abrir en navegador

### Limpieza
- [ ] NO existe `/tmp/ADT/arc42/` en raíz
- [ ] NO existe `/tmp/ADT/traduccion/` (movido a source/)
- [ ] NO existe `/tmp/ADT/seccion3_diagramas/`
- [ ] `/tmp/ADT42` movido a `/tmp/ADT42_backup_consolidado`
- [ ] Proyectos independientes en `/tmp/proyectos_independientes/`

---

## 📊 COMPARACIÓN ANTES/DESPUÉS

### ANTES (Desorganizado)
```
/tmp/
├── ADT/                    (NO es proyecto Sphinx)
│   ├── arc42/              (carpeta vacía en raíz)
│   ├── traduccion/source/  (sin Makefile)
│   ├── biblioteca/arc42_documentation/  (traducciones)
│   └── seccion3_diagramas/
├── ADT42/                  (proyecto Sphinx completo duplicado)
└── [Proyectos mezclados]
```

### DESPUÉS (Organizado)
```
/tmp/
├── ADT/                    ⭐ PROYECTO SPHINX ÚNICO
│   ├── Makefile
│   ├── make.bat
│   ├── build/html/
│   ├── source/
│   │   ├── conf.py
│   │   ├── 01-10/
│   │   └── biblioteca/
│   │       └── arc42/
│   │           └── sections/
│   └── docs_maestros/
├── ADT42_backup_consolidado/  (backup)
└── proyectos_independientes/  (scrapers, vagrant, etc.)
```

---

## 🚀 PRÓXIMOS PASOS DESPUÉS DE REORGANIZAR

### 1. Compilar y Verificar
```bash
cd /tmp/ADT
make html
firefox build/html/index.html  # Verificar visualmente
```

### 2. Crear metadata_libro.rst de arc42
```bash
# Usar contenido del archivo metadata que creé en propuesta anterior
# Archivo completo con progreso, estadísticas, etc.
```

### 3. Continuar con Sección 4
- Scraping de tips de Sección 4
- Crear 5-7 diagramas PlantUML
- Aplicar misma calidad que Sección 3

### 4. Poblar Metodología (Secciones 01-10)
- Migrar contenido según ARQUITECTURA_DOCUMENTAL
- Implementar prompts en 08_prompts/
- Casos prácticos en 06_casos_practicos/

---

## 💡 NOTAS IMPORTANTES

### ¿Por qué esta estructura?

1. **UN SOLO proyecto Sphinx** (/tmp/ADT)
   - Más fácil de mantener
   - Single source of truth
   - Compilación unificada

2. **biblioteca/ dentro de source/**
   - Según ESTRUCTURA_DE_BIBLIOTECA.md
   - arc42 es contenido, no estructura
   - Permite build integrado

3. **arc42 como libro**
   - Estructura sections/01-12/
   - original/ + traduccion/ + diagramas/
   - metadata_libro.rst completo
   - Igual que otros libros técnicos

4. **Limpieza de duplicados**
   - ADT42 → backup
   - Proyectos independientes → separados
   - Estructura antigua eliminada

---

## ⏱️ TIEMPO ESTIMADO

| Fase | Tiempo | Descripción |
|------|--------|-------------|
| 0 | 5 min | Backup |
| 1 | 5 min | Copiar archivos Sphinx |
| 2 | 10 min | Consolidar secciones 01-10 |
| 3 | 15 min | Consolidar biblioteca/ |
| 4 | 10 min | Mover traducciones |
| 5 | 5 min | Mover diagramas |
| 6 | 15 min | Limpieza y compilación |
| **TOTAL** | **65 min** | **~1 hora** |

---

**¿Proceder con esta reorganización?**

Una vez completada, tendrás:
- ✅ /tmp/ADT como proyecto Sphinx único
- ✅ arc42 dentro de source/biblioteca/arc42/
- ✅ Estructura correcta según docs maestros
- ✅ Proyecto compilable con `make html`
- ✅ Base sólida para Sección 4 y siguientes
