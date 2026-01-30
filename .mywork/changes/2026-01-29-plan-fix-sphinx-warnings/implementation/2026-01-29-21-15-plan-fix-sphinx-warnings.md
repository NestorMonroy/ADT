# Plan: Correccion de warnings y errores Sphinx (lista consolidada)

Fecha: 2026-01-29
Estado: Propuesto

## 1. Objetivo

Definir un plan accionable para corregir los errores y warnings de Sphinx
reportados en los logs recientes, priorizando los bloqueantes de `-W` y
organizando el trabajo por tipo de problema.

## 2. Alcance

Incluye:
- Errores/warnings de docutils (listas, blanks, literales) y `list-table`.
- Warnings de listas (bullet/enumerated/block quote).
- Problemas de imagenes (assets faltantes o ilegibles).
- Warnings de highlighting (Pygments/PlantUML/lexers no reconocidos).
- Duplicados en toctree y labels.

Excluye:
- Cambios de infraestructura (proxy/intersphinx) fuera del scope de los
  archivos listados.

## 3. Fuentes

- `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`
- `.mywork/work-logs/2026-01-29-17-05-reintento-livehtml-spelling.md`
- `.mywork/work-logs/2026-01-29-17-09-make-html-resultados.md`
- `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`

## 4. Inventario consolidado (sin duplicados)

### 4.1 Errores / warnings de docutils (rompen `-W`)

- `source/01_fundamentos/_metodologias/metodo_por_defecto.rst`
- `source/01_fundamentos/glosario_traduccion.rst`
- `source/09_referencias/index.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_2.rst`

### 4.2 Errores de `list-table`

- `source/09_referencias/index.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_2.rst`

### 4.3 Warnings de listas (bullet/enumerated/block quote)

- `source/01_fundamentos/_metodologias/metodo_por_defecto.rst`
- `source/01_fundamentos/glosario_traduccion.rst`
- `source/09_referencias/index.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_4.rst`

### 4.4 Problemas de imagenes

- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_3.rst`

### 4.5 Warnings de highlighting (Pygments/PlantUML)

- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_5.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_6.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_7.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_8.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/06_runtime_view/traduccion/runtime_tip_9.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/08_crosscutting_concepts/traduccion/crosscutting_tip_7.rst`
- `source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/12_glossary/traduccion/glossary_tip_3.rst`

### 4.6 Duplicados en toctree

#### 01_fundamentos
- `source/01_fundamentos/glosario_traduccion.rst`
- `source/01_fundamentos/principios_fundamentales.rst`

#### 03_estandares
- `source/03_estandares/calidad/index.rst`
- `source/03_estandares/formato_por_medio/index.rst`
- `source/03_estandares/restricciones/index.rst`
- `source/03_estandares/terminologia/index.rst`

#### 04_reglas_operativas
- `source/04_reglas_operativas/escenarios_traduccion/index.rst`
- `source/04_reglas_operativas/matrices_decision/index.rst`
- `source/04_reglas_operativas/reglas_traduccion/index.rst`

#### 05_herramientas_medios
- `source/05_herramientas_medios/equivalencias/index.rst`
- `source/05_herramientas_medios/latex/index.rst`
- `source/05_herramientas_medios/markdown/index.rst`
- `source/05_herramientas_medios/sphinx/index.rst`

#### 06_casos_practicos
- `source/06_casos_practicos/antes_despues/index.rst`
- `source/06_casos_practicos/casos_exito/index.rst`
- `source/06_casos_practicos/ejercicios_practica/index.rst`
- `source/06_casos_practicos/errores_comunes/index.rst`

#### 07_guias_uso
- `source/07_guias_uso/faq.rst`
- `source/07_guias_uso/guia_rapida.rst`

### 4.7 Labels duplicados

- `source/10_apendices/glosario_adt.rst`

## 5. Plan de ejecucion por lotes

### Lote 1: Bloqueantes de `-W` (prioridad critica)

1. Revisar cada archivo bloqueante y catalogar el tipo de error exacto.
2. Corregir `list-table` mal formadas en `09_referencias/index.rst` y
   `glossary_tip_2.rst`.
3. Normalizar listas sin linea en blanco y literales inline sin cierre.
4. Validar con build `-W` solo para los archivos afectados.

### Lote 2: `list-table` batch fix

1. Definir patron correcto de `list-table` (headers, separadores y
   columnas consistentes).
2. Aplicar el patron en los dos archivos listados.
3. Re-ejecutar build parcial para confirmar ausencia de warnings.

### Lote 3: Warnings de listas

1. Corregir listas con espacios en blanco faltantes entre parrafos.
2. Validar que listas enumeradas no rompan indentacion.
3. Ajustar block quotes y bullets para cumplir docutils.

### Lote 4: Imagenes faltantes

1. Verificar ruta real del asset usado en `glossary_tip_3.rst`.
2. Si falta, restaurar o reemplazar con ruta valida.
3. Confirmar permisos y legibilidad.

### Lote 5: Highlighting / lexers

1. Decidir estrategia: registrar lexer, usar `text`, o configurar
   extensiones (p.ej. PlantUML).
2. Ajustar code blocks con lexers no reconocidos en los 7 archivos.
3. Confirmar que warnings se reducen en build.

### Lote 6: Normalizacion de toctrees

1. Identificar toctree canonico para cada archivo duplicado.
2. Eliminar referencias duplicadas y mantener una sola inclusion.
3. Revisar coherencia de navegacion para no perder contenidos.

### Lote 7: Labels duplicados

1. Localizar labels duplicados en `glosario_adt.rst`.
2. Renombrar etiquetas con prefijo unico y actualizar referencias.
3. Verificar que no queden duplicados en el proyecto.

## 6. Criterios de aceptacion

- `-W` pasa sin errores en los 4 archivos bloqueantes.
- `list-table` ya no genera warnings.
- No hay warnings de listas ni de imagenes faltantes en archivos
  listados.
- Warnings de highlighting reducidos o eliminados segun estrategia.
- No existen duplicados en toctrees ni labels.

## 7. Dependencias y riesgos

- Cambios en toctrees pueden afectar navegacion y numeracion.
- Ajustes de lexers pueden requerir configuracion global.

## 8. Entregables

- Plan consolidado en este documento.
- Lista de pendientes priorizada y lista para ejecucion por lotes.
