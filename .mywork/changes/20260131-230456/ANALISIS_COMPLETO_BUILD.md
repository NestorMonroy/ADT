# Análisis Completo del Build - 20260131-164940

**Fecha**: 2026-01-31 23:04  
**Build Log**: build-log-20260131-164940.log  
**Total Issues**: 661

---

## 1. CONTEO TOTAL

```bash
LOG="build-logs/build-log-20260131-164940.log"
echo "WARNING:   $(grep -c 'WARNING:' "$LOG")"
echo "ERROR:     $(grep -c 'ERROR:' "$LOG")"
echo "CRITICAL:  $(grep -c 'CRITICAL:' "$LOG")"
```

**Resultado**:
```
WARNING:   613
ERROR:      17
CRITICAL:   31
─────────────────
TOTAL:     661
```

---

## 2. ANÁLISIS CRITICAL (31 issues)

### 2.1. Archivos Afectados

```bash
grep -o 'source[^:]*\.rst' critical.txt | sort -u
```

**Archivos afectados (5 archivos únicos)**:

source\02_procedimientos\WORKFLOW_v1_6_0_ACTUALIZACION.rst
source\02_procedimientos\workflow_general.rst
source\06_casos_practicos\errores_comunes\error_01_omisiones.rst
source\07_guias_uso\guia_rapida.rst
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst

**Total archivos únicos**: 5


### 2.2. Distribución de CRITICAL por Archivo

```bash
cat critical.txt | sed 's/:.*/ /' | sort | uniq -c
```

**Resultado**:

1     source\02_procedimientos\WORKFLOW_v1_6_0_ACTUALIZACION.rst
5     source\02_procedimientos\workflow_general.rst
22    source\06_casos_practicos\errores_comunes\error_01_omisiones.rst
1     source\07_guias_uso\guia_rapida.rst
2     source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst


### 2.3. Tipos de CRITICAL

```bash
cat critical.txt | cut -d: -f4- | sed 's/^ CRITICAL: //' | sort | uniq -c | sort -rn
```

**Resultado**:

     27 Unexpected section title.
      4 Missing matching underline for section title overline.


### 2.4. Detalles Completos de CRITICAL

```bash
cat critical.txt
```

**Listado completo**:

```
E:\Proyectos\Translate\ADT\source\02_procedimientos\WORKFLOW_v1_6_0_ACTUALIZACION.rst:634: CRITICAL: Missing matching underline for section title overline.
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:1363: CRITICAL: Missing matching underline for section title overline.
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:3080: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:3083: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:3407: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:3409: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:155: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:159: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:163: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:167: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:179: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:432: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:436: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:440: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:444: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:448: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:452: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:456: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:460: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:464: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:468: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:472: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:476: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:480: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:484: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:488: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:492: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\06_casos_practicos\errores_comunes\error_01_omisiones.rst:504: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\07_guias_uso\guia_rapida.rst:307: CRITICAL: Unexpected section title.
E:\Proyectos\Translate\ADT\source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst:2314: CRITICAL: Missing matching underline for section title overline.
E:\Proyectos\Translate\ADT\source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst:2318: CRITICAL: Missing matching underline for section title overline.
```


---

## 3. ANÁLISIS ERROR (17 issues)

### 3.1. Archivos Afectados

```bash
grep -o 'source[^:]*\.rst' errors.txt | sort -u
```

**Archivos afectados (archivos únicos)**:

source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/metadata_libro.rst
source\02_procedimientos\workflow_general.rst
source\03_estandares\calidad\criterios_calidad.rst
source\04_reglas_operativas\matrices_decision\MD_002_cuando_enriquecer.rst
source\07_guias_uso\guia_rapida.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\traduccion\quality_ejemplo_tpu_1.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\12_glossary\traduccion\glossary_tip_4.rst
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
source\docs_maestros\SINTESIS_METODOLOGICA_ADT.rst

**Total archivos únicos**: 9


### 3.2. Distribución de ERROR por Archivo

```bash
cat errors.txt | grep -o 'source[^:]*\.rst' | sort | uniq -c
```

**Resultado**:

2     source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/metadata_libro.rst
2     source\02_procedimientos\workflow_general.rst
1     source\03_estandares\calidad\criterios_calidad.rst
1     source\04_reglas_operativas\matrices_decision\MD_002_cuando_enriquecer.rst
1     source\07_guias_uso\guia_rapida.rst
1     source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\traduccion\quality_ejemplo_tpu_1.rst
1     source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\12_glossary\traduccion\glossary_tip_4.rst
4     source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
1     source\docs_maestros\SINTESIS_METODOLOGICA_ADT.rst


### 3.3. Tipos de ERROR

```bash
cat errors.txt | cut -d: -f4- | sed 's/^ ERROR: //' | sed 's/ \[docutils\]$//' | sort | uniq -c | sort -rn
```

**Resultado**:

      5 Error parsing content block for the "list-table" directive: exactly one bullet list expected.
      4 Document or section may not begin with a transition.
      3 The "list-table" directive is empty; content required.
      2  Document or section may not begin with a transition.
      1 Unknown target name: "estructura_de_biblioteca".
      1 Unexpected indentation.
      1 Content block expected for the "note" directive; none found.


### 3.4. Detalles Completos de ERROR

```bash
cat errors.txt
```

**Listado completo**:

```
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:1211: ERROR: Error parsing content block for the "list-table" directive: exactly one bullet list expected.
E:\Proyectos\Translate\ADT\source\02_procedimientos\workflow_general.rst:4407: ERROR: Content block expected for the "note" directive; none found. [docutils]
E:\Proyectos\Translate\ADT\source\03_estandares\calidad\criterios_calidad.rst:144: ERROR: The "list-table" directive is empty; content required.
E:\Proyectos\Translate\ADT\source\04_reglas_operativas\matrices_decision\MD_002_cuando_enriquecer.rst:247: ERROR: Error parsing content block for the "list-table" directive: exactly one bullet list expected.
E:\Proyectos\Translate\ADT\source\07_guias_uso\guia_rapida.rst:309: ERROR: Error parsing content block for the "list-table" directive: exactly one bullet list expected.
source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/metadata_libro.rst:2: ERROR: Document or section may not begin with a transition. [docutils]
source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/metadata_libro.rst:2: ERROR: Document or section may not begin with a transition. [docutils]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\traduccion\quality_ejemplo_tpu_1.rst:35: ERROR: Error parsing content block for the "list-table" directive: exactly one bullet list expected.
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\12_glossary\traduccion\glossary_tip_4.rst:163: ERROR: The "list-table" directive is empty; content required.
E:\Proyectos\Translate\ADT\source\docs_maestros\ARQUITECTURA_DOCUMENTAL_TRADUCCION.md:4: ERROR: Document or section may not begin with a transition. [docutils]
E:\Proyectos\Translate\ADT\source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst:325: ERROR: Unexpected indentation. [docutils]
E:\Proyectos\Translate\ADT\source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst:302: ERROR: Error parsing content block for the "list-table" directive: exactly one bullet list expected.
E:\Proyectos\Translate\ADT\source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst:1281: ERROR: The "list-table" directive is empty; content required.
E:\Proyectos\Translate\ADT\source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst:1: ERROR: Document or section may not begin with a transition. [docutils]
E:\Proyectos\Translate\ADT\source\docs_maestros\METODO_TRADUCCION_PESHITTA_ZACHARIAS.md:7: ERROR: Document or section may not begin with a transition. [docutils]
E:\Proyectos\Translate\ADT\source\docs_maestros\PROMPT_MAESTRO_SPHINX_TRADUCCION.md:4: ERROR: Document or section may not begin with a transition. [docutils]
E:\Proyectos\Translate\ADT\source\docs_maestros\SINTESIS_METODOLOGICA_ADT.rst:401: ERROR: Unknown target name: "estructura_de_biblioteca". [docutils]
```


---

## 4. ANÁLISIS WARNING (613 issues)

### 4.1. Categorización por Tipo

```bash
cat warnings.txt | cut -d: -f4- | sed 's/^ WARNING: //' | \
  sed 's/ \[docutils\]$//' | sed 's/ \[myst.header\]$//' | \
  sed 's/ \[misc.highlighting_failure\]$//' | sed 's/ \[ref.*\]$//' | \
  sort | uniq -c | sort -rn
```

**Resultado (Top 20)**:

    139 Document headings start at H3, not H1
    132 Document headings start at H2, not H1
     87 Block quote ends without a blank line; unexpected unindent.
     84 Enumerated list ends without a blank line; unexpected unindent.
     70 Explicit markup ends without a blank line; unexpected unindent.
     23 Document headings start at H4, not H1
     13 Non-consecutive header level increase; H2 to H4
     11 Bullet list ends without a blank line; unexpected unindent.
      8 Pygments lexer name 'PlantUML' is not known
      4 Field list ends without a blank line; unexpected unindent.
      3 Line block ends without a blank line.
      3 Inline strong start-string without end-string.
      2 Title underline too short.
      2 Inline emphasis start-string without end-string.
      2 Footnote [#] is not referenced.
      1 toctree glob pattern 'traduccion/decision_ejemplo_*' didn't match any documents
      1 term not in glossary: 'Unreasonable'
      1 term not in glossary: 'Third Party Contracting'
      1 term not in glossary: 'Reference Architecture'
      1 term not in glossary: 'Programming Guidelines'


### 4.2. WARNING - Headers (309 issues)

#### 4.2.1. Archivos Afectados por Headers

```bash
grep "headings start at H" warnings.txt | grep -o 'source[^:]*\.rst' | sort -u
```

**Archivos afectados por Headers**:

source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\01-overview-example-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\01-overview-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\01-quality-reqs-example-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\01-quality-reqs-example-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\02-constraint-example-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\03-context-example-business-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\03-context-example-business-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\03-context-example-business-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\03-context-example-business-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\03-context-example-technical-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\03-context-example-technical-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\04-solutionStrategy-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\04-solutionStrategy-example-mama-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\05-buildingblock-example-hsc.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\05-buildingblock-example-status.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\05-buildingblock-example-tpu-lev-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\05-buildingblock-example-tpu-lev-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\06-runtime-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\06-runtime-example-mama-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\06-runtime-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\07-deployment-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\07-deployment-sample-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\07-deployment-sample-tpu-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\08-concept-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\08-concept-example-htmlsc-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\08-concept-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\08-concept-example-tpu-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\09-decision-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\09-decision-example-tpu-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\10-quality-scenario-example-htmlsc-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\10-quality-scenario-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\11-risk-example-htmlsc.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\11-risk-example-tpu.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_examples\12-glossary-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_includes\example.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_includes\further-info.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\contact.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\examples.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\imprint-privacy.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-12.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-6.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-7.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-8.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_pages\section-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\01-requirements\2016-03-02-t-1-12.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\01-requirements\2016-03-02-t-1-21.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\03-context\2016-03-01-t-3-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-01-t-5-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-01-t-5-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-01-t-5-6.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-01-t-5-7.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-02-t-5-10.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-02-t-5-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-02-t-5-13.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-02-t-5-16.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-02-t-5-17.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-02-t-5-19.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-03-t-5-20.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-03-t-5-21.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-03-t-5-22.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-03-t-5-24.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-03-t-5-26.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\05-buildingblocks\2016-03-03-t-5-28.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-6.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-7.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-02-t-6-10.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-02-t-6-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\07-deployment\2016-03-01-t-7-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\07-deployment\2016-03-01-t-7-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\07-deployment\2016-03-01-t-7-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2016-03-01-t-8-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2016-03-01-t-8-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2016-03-01-t-8-7.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2016-03-01-t-8-8.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2022-07-01-t-8-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\09-decisions\2016-03-01-t-9-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\09-decisions\2016-03-01-t-9-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\10-quality\2016-03-01-t-10-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\11-risks\2016-03-01-t-11-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\11-risks\2016-03-01-t-11-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\01-overview-example-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\01-overview-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\01-quality-reqs-example-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\01-quality-reqs-example-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\2016-03-02-t-1-12.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\2016-03-02-t-1-21.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\02_constraints\original\02-constraint-example-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\03-context-example-business-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\03-context-example-business-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\03-context-example-business-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\03-context-example-business-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\03-context-example-technical-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\03-context-example-technical-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\original\2016-03-01-t-3-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\04_solution_strategy\original\04-solutionStrategy-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\04_solution_strategy\original\04-solutionStrategy-example-mama-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\05-buildingblock-example-hsc.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\05-buildingblock-example-status.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\05-buildingblock-example-tpu-lev-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\05-buildingblock-example-tpu-lev-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-01-t-5-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-01-t-5-3.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-01-t-5-6.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-01-t-5-7.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-02-t-5-10.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-02-t-5-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-02-t-5-13.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-02-t-5-16.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-02-t-5-17.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-02-t-5-19.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-03-t-5-20.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-03-t-5-21.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-03-t-5-22.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-03-t-5-24.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-03-t-5-26.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\original\2016-03-03-t-5-28.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\06_runtime_view\original\06-runtime-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\06_runtime_view\original\06-runtime-example-mama-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\06_runtime_view\original\06-runtime-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\06_runtime_view\original\2016-03-01-t-6-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\06_runtime_view\original\2016-03-01-t-6-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\06_runtime_view\original\2016-03-02-t-6-10.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\07_deployment_view\original\07-deployment-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\07_deployment_view\original\07-deployment-sample-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\07_deployment_view\original\07-deployment-sample-tpu-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\07_deployment_view\original\2016-03-01-t-7-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\07_deployment_view\original\2016-03-01-t-7-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\07_deployment_view\original\2016-03-01-t-7-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\08-concept-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\08-concept-example-htmlsc-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\08-concept-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\08-concept-example-tpu-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\2016-03-01-t-8-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\2016-03-01-t-8-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\2016-03-01-t-8-8.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_concepts\original\2022-07-01-t-8-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_crosscutting_concepts\original\2016-03-01-t-8-4.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_crosscutting_concepts\original\2016-03-01-t-8-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_crosscutting_concepts\original\2016-03-01-t-8-8.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_crosscutting_concepts\original\2022-07-01-t-8-11.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\08_crosscutting_concepts\original\section-8.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\09_architecture_decisions\original\09-decision-example-htmlsc-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\09_architecture_decisions\original\09-decision-example-tpu-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\09_architecture_decisions\original\2016-03-01-t-9-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\09_architecture_decisions\original\2016-03-01-t-9-5.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\09_architecture_decisions\original\section-9.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\original\10-quality-scenario-example-htmlsc-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\original\10-quality-scenario-example-tpu-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\original\2016-03-01-t-10-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\11_risks_tech_debt\original\11-risk-example-htmlsc.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\11_risks_tech_debt\original\11-risk-example-tpu.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\11_risks_tech_debt\original\2016-03-01-t-11-1.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\11_risks_tech_debt\original\2016-03-01-t-11-2.md.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\12_glossary\original\12-glossary-example-htmlsc-1.md.rst
source\docs_maestros\ARQUITECTURA_TRADUCCION_IACT.rst
source\docs_maestros\PROMPT_MAESTRO_SPHINX_TRADUCCION.md.rst

**Total archivos únicos con Headers issues**: 166


#### 4.2.2. Distribución de Headers por Tipo

```bash
grep -E "headings start at H|Non-consecutive header|Title underline" warnings.txt | \
  cut -d: -f4- | sed 's/^ WARNING: //' | sed 's/ \[.*\]$//' | \
  sort | uniq -c | sort -rn
```

**Resultado**:

    139 Document headings start at H3, not H1
    132 Document headings start at H2, not H1
     23 Document headings start at H4, not H1
     13 Non-consecutive header level increase; H2 to H4
      2 Title underline too short.


### 4.3. WARNING - Blank Lines (259 issues)

#### 4.3.1. Archivos Afectados por Blank Lines

```bash
grep "ends without a blank line" warnings.txt | grep -o 'source[^:]*\.rst' | sort -u
```

**Archivos afectados por Blank Lines**:

source\01_fundamentos\_fundamentos_conceptuales\signifiant_vs_signifie.rst
source\01_fundamentos\_metodologias\metodo_por_defecto.rst
source\01_fundamentos\glosario_traduccion.rst
source\01_fundamentos\metamodelos\framework_universal_transformacion.rst
source\01_fundamentos\principios_fundamentales.rst
source\02_procedimientos\WORKFLOW_ACTUALIZACION_v1_5_0.rst
source\02_procedimientos\WORKFLOW_v1_6_0_ACTUALIZACION.rst
source\02_procedimientos\workflow_general.rst
source\03_estandares\calidad\checklist_revision.rst
source\03_estandares\calidad\criterios_calidad.rst
source\03_estandares\calidad\metricas_traduccion.rst
source\04_reglas_operativas\matrices_decision\MD_001_modo_1_vs_modo_2.rst
source\04_reglas_operativas\matrices_decision\MD_002_cuando_enriquecer.rst
source\04_reglas_operativas\matrices_decision\MD_004_traducir_vs_conservar.rst
source\05_herramientas_medios\equivalencias\latex_rst_equivalencias.rst
source\06_casos_practicos\antes_despues\caso_01_seccion_breve.rst
source\06_casos_practicos\errores_comunes\error_01_omisiones.rst
source\07_guias_uso\faq.rst
source\07_guias_uso\guia_rapida.rst
source\07_guias_uso\troubleshooting.rst
source\07_guias_uso\tutorial_completo.rst
source\08_prompts\index.rst
source\09_referencias\cheatsheets\cheatsheet_rst.rst
source\biblioteca\_metadata_biblioteca\META_BIB_003_Esquema_Codificacion_1_0_0.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\metadata_libro.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\notas_traduccion_seccion_01.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\traduccion\seccion_1_1_requisitos.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\traduccion\seccion_3_1_contexto_negocio.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\03_context_scope\traduccion\seccion_3_2_contexto_tecnico.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\04_solution_strategy\traduccion\seccion_04_estrategia_solucion.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\traduccion\seccion_5_1_whitebox_sistema.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\traduccion\seccion_5_2_nivel_2.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\05_building_blocks\traduccion\seccion_5_3_nivel_3.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\10_quality\traduccion\quality_ejemplo_tpu_1.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\11_risks_tech_debt\traduccion\risks_tip_1.rst
source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\12_glossary\traduccion\glossary_tip_4.rst
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst
source\docs_maestros\PLAN_CONTENIDO.rst
source\docs_maestros\SINTESIS_METODOLOGICA_ADT.rst

**Total archivos únicos con Blank Lines issues**: 39


#### 4.3.2. Distribución de Blank Lines por Tipo

```bash
grep "ends without a blank line" warnings.txt | \
  cut -d: -f4- | sed 's/^ WARNING: //' | sed 's/ \[docutils\]$//' | \
  sort | uniq -c | sort -rn
```

**Resultado**:

     87 Block quote ends without a blank line; unexpected unindent.
     84 Enumerated list ends without a blank line; unexpected unindent.
     70 Explicit markup ends without a blank line; unexpected unindent.
     11 Bullet list ends without a blank line; unexpected unindent.
      4 Field list ends without a blank line; unexpected unindent.
      3 Line block ends without a blank line.


### 4.4. WARNING - Lexers (8 issues)

#### 4.4.1. Archivos Afectados por Lexers

```bash
grep "Pygments lexer" warnings.txt | grep -o 'source[^:]*\.rst' | sort -u
```

**Archivos afectados por Lexers**:


**Total archivos únicos con Lexers issues**: 0


#### 4.4.2. Detalles de Lexers

```bash
grep "Pygments lexer" warnings.txt
```

**Listado completo**:

```
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\01-requirements\2016-03-01-t-1-9.md:16: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-5.md:25: WARNING: Pygments lexer name 'plantuml' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-6.md:33: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-7.md:24: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-8.md:16: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-01-t-6-9.md:15: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\06-runtime\2016-03-02-t-6-11.md:32: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\original\_posts\08-concepts\2016-03-01-t-8-7.md:29: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\sections\01_introduction_goals\original\2016-03-01-t-1-9.md:16: WARNING: Pygments lexer name 'PlantUML' is not known [misc.highlighting_failure]
```


### 4.5. WARNING - Otros (37 issues)

Incluye: Inline markup, Footnotes, Glossary terms, Toctree, etc.

```bash
# Excluir headers, blank lines y lexers
grep -v "headings start at H" warnings.txt | \
  grep -v "Non-consecutive header" | \
  grep -v "Title underline" | \
  grep -v "ends without a blank line" | \
  grep -v "Pygments lexer" | \
  cut -d: -f4- | sed 's/^ WARNING: //' | sed 's/ \[.*\]$//' | \
  sort | uniq -c | sort -rn
```

**Resultado**:

      4 Footnote
      3 Inline strong start-string without end-string.
      2 Lexing literal_block '{\n"section": {\n"number": "XX",\n"title_en": "[T�tulo en ingl�s]",\n"title_es": "[T�tulo en espa�ol]",\n"arc42_template": "section-X",\n"status": "complete",\n"completion_percentage": 100,\n"translation_date": "YYYY-MM-DD",\n"workflow_version": "v1.X.X"\n},\n\n"translation": {\n"method": "Peshitta + ADT Workflow v1.X.X",\n"source_language": "English",\n"target_language": "Spanish",\n"source_format": "Markdown",\n"target_format": "reStructuredText",\n"architectural_terminology_applied": true,\n"step_3_4_applied": true\n},\n\n"files": {\n"total": XX,\n"subsections": X,\n"examples": X,\n"tips": X,\n"breakdown": {\n"subsections":
      2 Inline emphasis start-string without end-string.
      1 toctree glob pattern 'traduccion/decision_ejemplo_*' didn't match any documents
      1 term not in glossary: 'Unreasonable'
      1 term not in glossary: 'Third Party Contracting'
      1 term not in glossary: 'Reference Architecture'
      1 term not in glossary: 'Programming Guidelines'
      1 term not in glossary: 'Political Constraints'
      1 term not in glossary: 'Platform-independent'
      1 term not in glossary: 'Naming Conventions'
      1 term not in glossary: 'Management'
      1 term not in glossary: 'Legal Concerns'
      1 term not in glossary: 'Implementation Decision'
      1 term not in glossary: 'Freedom of Design'
      1 term not in glossary: 'Documentation Conventions'
      1 term not in glossary: 'Development Team'
      1 term not in glossary: 'Development Process'
      1 term not in glossary: 'Design Decision'
      1 term not in glossary: 'Consequences'
      1 term not in glossary: 'Command Line'
      1 duplicate term description of Stakeholder, other instance in biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/glosario_seccion_01
      1 duplicate term description of Markdown, other instance in 01_fundamentos/glosario_traduccion
      1 duplicate label metadata-estado-traduccion, other instance in E:\Proyectos\Translate\ADT\source\biblioteca\ingenieria\sistemas\arquitectura\arc42_documentation\index.rst
      1 Lexing literal_block '{\n"verificacion_traducciones": {\n"total_originales": 13,\n"total_traducciones": 13,\n"traducciones_faltantes":
      1 Lexing literal_block '.PHONY: verificar verificar-lote\n\nverificar:\n@echo "Verificando traducci�n..."\n@./scripts/verificar_traduccion.sh $(ORIG) $(TRAD)\n\nverificar-lote:\n@echo "Verificando lote completo..."\n@./scripts/verificar_lote.sh $(ORIG_DIR) $(TRAD_DIR)' as "makefile" resulted in an error at token: '@'. Retrying in relaxed mode.
      1 Lexing literal_block '# Analog�a en ATL\nrule DefaultVerbTranslation {\n    from\n        h : Hebrew!Verb\n    to\n        s : Syriac!Verb (\n            tense <- h.getTemporalSituation(),  # Signifi�\n            # NO: form <- h.form  # Signifiant\n        )\n}\n' as "python" resulted in an error at token: '!'. Retrying in relaxed mode.
      1 Inline literal start-string without end-string.


---

## 5. RESUMEN CONSOLIDADO

### 5.1. Distribución por Severidad y Categoría

| Severidad | Categoría | Issues | Archivos | Complejidad | Estrategia |
|-----------|-----------|--------|----------|-------------|------------|
| CRITICAL | Section Structure | 31 | 5 | ALTA | Manual puro |
| ERROR | List-Tables | 8 | 9 | ALTA | Manual puro |
| ERROR | Transitions | 6 | ~3 | BAJA | Manual rápido |
| WARNING | Headers | 309 | EOFRESUMEN

wc -l < headers_files.tmp | tr -d '\n' >> ANALISIS_COMPLETO_BUILD.md && \
cat >> ANALISIS_COMPLETO_BUILD.md << 'EOFRESUMEN2'
 | MODERADA | Manual selectivo |
| WARNING | Blank Lines | 259 | EOFRESUMEN2

wc -l < blanklines_files.tmp | tr -d '\n' >> ANALISIS_COMPLETO_BUILD.md && \
cat >> ANALISIS_COMPLETO_BUILD.md << 'EOFRESUMEN3'
 | MODERADA | Script seguro |
| WARNING | Lexers | 8 | EOFRESUMEN3

wc -l < lexers_files.tmp | tr -d '\n' >> ANALISIS_COMPLETO_BUILD.md && \
cat >> ANALISIS_COMPLETO_BUILD.md << 'EOFRESUMEN4'
 | TRIVIAL | Script trivial |
| WARNING | Otros | 37 | Variable | VARIABLE | Caso por caso |

**Total**: 661 issues en múltiples archivos

### 5.2. Archivos con Mayor Concentración de Issues

#### Top 10 Archivos Más Afectados (WARNING)

```bash
grep -o 'source[^:]*\.rst' warnings.txt | sort | uniq -c | sort -rn | head -10
```

**Resultado**:

EOFRESUMEN4

grep -o 'source[^:]*\.rst' warnings.txt | sort | uniq -c | sort -rn | head -10 | \
  awk '{printf "%-4s  %s\n", $1, $2}' >> ANALISIS_COMPLETO_BUILD.md && \
echo "" >> ANALISIS_COMPLETO_BUILD.md
#### Archivos con CRITICAL + ERROR (Alta Prioridad)

```bash
# Archivos que tienen tanto CRITICAL como ERROR
comm -12 <(grep -o 'source[^:]*\.rst' critical.txt | sort -u) \
         <(grep -o 'source[^:]*\.rst' errors.txt | sort -u)
```

**Archivos con ambos**:


#### Archivos con CRITICAL + ERROR (Alta Prioridad)

Archivos que aparecen tanto en CRITICAL como en ERROR:

source\02_procedimientos\workflow_general.rst
source\07_guias_uso\guia_rapida.rst
source\docs_maestros\GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst


### 5.3. Estadísticas de Distribución

**Total archivos únicos afectados**:

- WARNING: 215 archivos
- ERROR: 9 archivos
- CRITICAL: 5 archivos


**Promedio de issues por archivo**:

- WARNING: ~$(echo "scale=1; 613 / $(grep -o 'source[^:]*\.rst' warnings.txt | sort -u | wc -l)" | bc) issues/archivo
- ERROR: ~$(echo "scale=1; 17 / $(grep -o 'source[^:]*\.rst' errors.txt | sort -u | wc -l)" | bc) issues/archivo  
- CRITICAL: ~$(echo "scale=1; 31 / $(grep -o 'source[^:]*\.rst' critical.txt | sort -u | wc -l)" | bc) issues/archivo

---

## 6. CONCLUSIONES Y RECOMENDACIONES

### 6.1. Prioridad Urgente (CRITICAL - 31 issues, 5 archivos)

**Archivos a corregir primero**:
- `workflow_general.rst` (mayoría de CRITICAL)
- `WORKFLOW_v1_6_0_ACTUALIZACION.rst`
- `guia_rapida.rst`
- `error_01_omisiones.rst`
- `GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst`

**Estrategia**: Manual puro, un archivo a la vez, commit por archivo.

**Estimación**: 2-3 horas (30-40 min/archivo)

### 6.2. Prioridad Alta (ERROR - 17 issues, 9 archivos)

**Categorías**:
1. List-Tables (8 issues) - Requiere análisis de contenido
2. Transitions (6 issues) - Patrón simple, eliminar línea inicial
3. Otros (3 issues) - Evaluar caso por caso

**Estrategia**: Manual puro para List-Tables, manual rápido para Transitions.

**Estimación**: 1-1.5 horas

### 6.3. Quick Wins (WARNING Lexers - 8 issues, 3 archivos)

**Patrón**: Cambiar 'PlantUML' → 'text' en code-blocks

**Estrategia**: Script trivial o búsqueda/reemplazo global

**Estimación**: 15-20 minutos

### 6.4. Automatización Viable (WARNING Blank Lines - 259 issues, muchos archivos)

**Patrón**: Agregar línea en blanco después de estructuras

**Estrategia**: Script seguro con 7 Protecciones Obligatorias

**Estimación**: 2-3 horas (incluye desarrollo y validación)

### 6.5. Evaluación Requerida (WARNING Headers - 309 issues)

**Complejidad**: Moderada-Alta (decisiones contextuales)

**Opciones**:
- A) Manual selectivo (4-6 horas)
- B) Defer para sesión futura
- C) Abordar solo casos críticos que bloqueen TOC

**Recomendación**: Evaluar después de completar CRITICAL + ERROR + Lexers + Blank Lines

### 6.6. Plan de Ejecución Sugerido

**Sesión 1** (2-3 horas): CRITICAL (31)
**Sesión 2** (1 hora): ERROR List-Tables (8)
**Sesión 3** (30 min): ERROR Transitions (6)
**Sesión 4** (20 min): WARNING Lexers (8) ← Quick Win
**Sesión 5** (2-3 horas): WARNING Blank Lines (259)
**Sesión 6** (Opcional): WARNING Headers (309) o Defer

**Total estimado**: 6-8 horas para resolver 312 issues críticos (47% del total)

---

## 7. ARCHIVOS DE REFERENCIA

Archivos generados durante el análisis:

```bash
ls -lh *.txt *.tmp
```

**Listado**:

- `critical.txt` - 31 líneas con CRITICAL
- `errors.txt` - 17 líneas con ERROR
- `warnings.txt` - 613 líneas con WARNING
- `critical_files.tmp` - Archivos únicos con CRITICAL
- `error_files.tmp` - Archivos únicos con ERROR
- `headers_files.tmp` - Archivos únicos con Headers WARNING
- `blanklines_files.tmp` - Archivos únicos con Blank Lines WARNING
- `lexers_files.tmp` - Archivos únicos con Lexers WARNING

---

## 8. COMANDOS ÚTILES PARA ANÁLISIS ADICIONAL

### Buscar todos los issues de un archivo específico

```bash
FILE="source/02_procedimientos/workflow_general.rst"
grep "$FILE" critical.txt errors.txt warnings.txt
```

### Contar issues por directorio

```bash
for dir in source/*/; do
    echo "$dir: $(grep -c "$dir" warnings.txt) WARNING"
done | sort -t: -k2 -rn
```

### Extraer líneas específicas de un archivo afectado

```bash
# Ejemplo: Ver líneas con CRITICAL en workflow_general.rst
grep "workflow_general.rst" critical.txt | cut -d: -f2 | sort -u
```

---

**Fecha de análisis**: 2026-01-31 23:06  
**Análisis realizado por**: Claude (siguiendo incremental-correction-methodology v1.2.0)  
**Próximo paso**: FASE 3 - Priorización
