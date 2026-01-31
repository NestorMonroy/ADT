# Estrategias de Optimización: Sphinx Builds

**Fecha**: 2026-01-31  
**Proyecto**: ADT Documentation  
**Problema**: `make clean && make html` es lento (especialmente con 582+ WARNING)

---

## 📊 Contexto Actual

**Estado del proyecto**:
- ~300+ archivos RST/MD
- 582 WARNING (después de rollback)
- Build completo: varios minutos
- `make clean` borra todo el cache

---

## 🚀 Estrategias de Optimización (Ordenadas por Impacto)

### **1. EVITAR `make clean` - Usar Builds Incrementales**

**Impacto**: ⭐⭐⭐⭐⭐ (MÁXIMO)

**Problema actual**:
```bash
make clean && make html  # Borra todo el cache, rebuild completo
```

**Solución**:
```bash
# NO hacer make clean a menos que sea absolutamente necesario
make html  # Build incremental (solo archivos cambiados)
```

**Cuándo SÍ usar `make clean`**:
- Cambios en `conf.py`
- Cambios en extensiones de Sphinx
- Cambios en toctree principal
- Problemas raros de cache
- **Build final para producción**

**Cuándo NO usar `make clean`**:
- Corrección de WARNING en archivos RST
- Edición de contenido normal
- Desarrollo diario
- **Corrección de 582 WARNING** (nuestro caso)

**Evidencia**:
- "The building process takes about 10 minutes if I don't change anything after the last build (i.e. everything that can be cached should be cached)"
- Sphinx caches "doctree pickles" para evitar re-parsear archivos sin cambios

---

### **2. Deshabilitar Search Index (30% más rápido)**

**Impacto**: ⭐⭐⭐⭐ (ALTO)

**Solución**:

Opción A - Temporal en comando:
```bash
# En conf.py, comentar temporalmente:
# html_use_index = False  # Deshabilita search index

make html SPHINXOPTS="-D html_use_index=false"
```

Opción B - En `Makefile`:
```makefile
# Agregar target custom
html-fast:
	@$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html -D html_use_index=false
	@echo
	@echo "Build finished (without search index). The HTML pages are in $(BUILDDIR)/html."
```

**Uso**:
```bash
make html-fast  # 30% más rápido
```

**Evidencia**:
- "One way to speed it up a bit is skipping the build of the search index. For my setup, this cut build times by roughly 30%"

**Cuándo usar**:
- Durante desarrollo/corrección de WARNING
- Testing rápido
- **Corrección de 582 WARNING** ✅

**Cuándo NO usar**:
- Build final para producción
- Testing de search functionality

---

### **3. Parallel Builds con `-j` (Efectividad Variable)**

**Impacto**: ⭐⭐⭐ (MEDIO - depende del hardware)

**Solución**:
```bash
# Usar CPUs disponibles
make html SPHINXOPTS="-j auto"

# O número específico
make html SPHINXOPTS="-j 4"
```

**Limitaciones importantes**:
- Solo paraleliza la fase de "writing output"
- NO paraleliza: parsing, cross-referencing, indexing
- Requiere sistema con "fork" (NO funciona en Windows)
- Puede ser MÁS LENTO en proyectos pequeños
- Search index NO se puede paralelizar (bug conocido en Sphinx 6.1+)

**Evidencia**:
- "The -j option only speeds the write-phase of the build"
- "with -j N (i tried N=1-4) the build is not faster, in fact it is a little bit slower"
- "I updated to 1.2b1 (from 1.1.3) and the build is 25% faster now, **without** the -j option!"

**Recomendación**:
- Probar con tu proyecto específico
- Medir tiempos con/sin `-j`
- Para ADT: probablemente NO ayude mucho (muchas cross-referencias)

---

### **4. Build Solo Archivos Específicos**

**Impacto**: ⭐⭐⭐⭐⭐ (MÁXIMO para testing específico)

**Solución**:
```bash
# Build solo archivos específicos
sphinx-build source/ _build/html/ source/path/to/file.rst
```

**Uso para corregir 582 WARNING**:
```bash
# Corregir WARNING en metadata_libro.rst
vim source/biblioteca/.../metadata_libro.rst  # hacer corrección
sphinx-build source/ _build/ source/biblioteca/.../metadata_libro.rst
# Verificar que WARNING desapareció
```

**Limitaciones**:
- Cross-referencias pueden no funcionar
- Solo para testing rápido

---

### **5. sphinx-autobuild (Desarrollo)**

**Impacto**: ⭐⭐⭐⭐ (ALTO para workflow de desarrollo)

**Instalación**:
```bash
pip install sphinx-autobuild
```

**Uso**:
```bash
sphinx-autobuild source/ _build/html/

# Con opciones
sphinx-autobuild source/ _build/html/ --open-browser --port 8000
```

**Beneficios**:
- Live reload automático
- Solo rebuild archivos cambiados
- Preview inmediato en browser

**Para corrección de WARNING**:
```bash
# Terminal 1: Servidor con live reload
sphinx-autobuild source/ _build/html/

# Terminal 2: Corregir archivos
vim source/archivo.rst

# Browser se actualiza automáticamente
```

---

### **6. Optimizaciones en `conf.py`**

**Impacto**: ⭐⭐ (BAJO-MEDIO)

```python
# conf.py - Optimizaciones

# 1. Deshabilitar extensiones no necesarias durante desarrollo
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',  # Puede ser lento
    # 'sphinx.ext.linkcheck',  # Comentar durante desarrollo
]

# 2. Deshabilitar search index temporalmente
html_use_index = False  # Descomentar para builds rápidos

# 3. Reducir niveles de toctree depth
html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}
```

---

### **7. Gestión Inteligente de Cache**

**Impacto**: ⭐⭐⭐ (MEDIO)

**Solución**:
```bash
# Limpiar solo doctrees (no static files)
rm -rf _build/.doctrees/

# O usar --fresh-env (rebuild environment, pero usa cache de parsing)
sphinx-build -E source/ _build/html/
```

**Diferencia**:
- `make clean`: Borra TODO
- `-E / --fresh-env`: Rebuild cross-references, mantiene parsed files
- Build incremental: Solo archivos cambiados

---

## 🎯 Recomendación para Corrección de 582 WARNING

### **Workflow Óptimo**:

```bash
# 1. Build inicial (UNA VEZ)
make clean && make html > build.log 2>&1

# 2. Crear Makefile target rápido
cat >> Makefile << 'EOF'

html-fast:
	@sphinx-build -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html \
	    -D html_use_index=false
	@echo
	@echo "Fast build finished. HTML pages in $(BUILDDIR)/html."

# Build para verificar correcciones (SIN search index, SIN clean)
verify:
	@sphinx-build -b html source/ _build/html/ \
	    -D html_use_index=false 2>&1 | tee _build/verify.log
	@echo ""
	@echo "WARNING count:"
	@grep "WARNING:" _build/verify.log | wc -l
EOF

# 3. Durante corrección de WARNING
make html-fast > /tmp/check.log 2>&1  # Rápido, sin clean
grep "WARNING:" /tmp/check.log | wc -l  # Contar

# 4. Build final (UNA VEZ al terminar)
make clean && make html  # Completo con search index
```

---

## 📊 Comparación de Tiempos Estimados

Para proyecto ADT (~300 archivos):

| Comando | Tiempo Estimado | Uso |
|---------|-----------------|-----|
| `make clean && make html` | 5-10 min | ❌ Evitar durante desarrollo |
| `make html` (incremental) | 30 seg - 2 min | ✅ Uso normal |
| `make html-fast` (sin search) | 20 seg - 1 min | ✅ Desarrollo/WARNING |
| `sphinx-build ... file.rst` | 5-10 seg | ✅ Testing específico |
| `sphinx-autobuild` | < 1 seg (cambios) | ✅ Live development |

---

## ✅ Implementación Inmediata

### **Paso 1: Agregar target `html-fast` al Makefile**

```bash
cd /tmp/ADT
cat >> Makefile << 'EOF'

# Fast build without search index (for development/WARNING fixing)
html-fast:
	@$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html \
	    -D html_use_index=false
	@echo
	@echo "Fast build finished. HTML in $(BUILDDIR)/html."

# Verify build with WARNING count
verify:
	@$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html \
	    -D html_use_index=false 2>&1 | tee $(BUILDDIR)/verify.log
	@echo ""
	@echo "==> WARNING count:"
	@grep "WARNING:" $(BUILDDIR)/verify.log | wc -l
	@echo ""
	@echo "Log saved to: $(BUILDDIR)/verify.log"
EOF
```

### **Paso 2: Uso durante corrección de WARNING**

```bash
# NO hacer make clean
# SÍ hacer build incremental rápido
make html-fast

# O con conteo automático
make verify
```

---

## 🚨 Reglas Críticas

1. **NUNCA** hacer `make clean` durante corrección de WARNING
2. **SIEMPRE** usar build incremental (`make html` o `make html-fast`)
3. **DESHABILITAR** search index durante desarrollo (`html_use_index=false`)
4. **PROBAR** `-j auto` en tu máquina (puede ayudar o empeorar)
5. **USAR** `sphinx-autobuild` para desarrollo iterativo
6. **BUILD FINAL** con `make clean && make html` solo al terminar

---

## 📚 Referencias

- [Sphinx Documentation: sphinx-build](https://www.sphinx-doc.org/en/master/man/sphinx-build.html)
- [Google Groups: Sphinx build painfully slow](https://groups.google.com/g/sphinx-users/c/EC7_wNtE5To)
- [sphinx-autobuild GitHub](https://github.com/sphinx-doc/sphinx-autobuild)
- [Issue #11163: Parallel search index bug](https://github.com/sphinx-doc/sphinx/issues/11163)

---

## 🎯 Aplicación a 582 WARNING

**Estrategia específica para nuestro caso**:

1. ✅ **Ya hicimos** `make clean` una vez (obtuvimos 582 WARNING)
2. ✅ **NO volver** a hacer `make clean` hasta terminar
3. ✅ **Usar** `make html-fast` para cada corrección
4. ✅ **Verificar** con `make verify` (cuenta WARNING automáticamente)
5. ✅ **Build final** con `make clean && make html` solo al terminar

**Tiempo estimado**:
- Con `make clean` cada vez: 5-10 min × 582 = **50-100 HORAS** ❌
- Con build incremental: 30 seg × 582 correcciones = **5 HORAS** ✅
- Con `html-fast`: 20 seg × 582 = **3 HORAS** ✅✅

**Ahorro**: ~95% de tiempo

---

**Conclusión**: El mayor problema NO es la velocidad de Sphinx, sino el uso innecesario de `make clean`.
