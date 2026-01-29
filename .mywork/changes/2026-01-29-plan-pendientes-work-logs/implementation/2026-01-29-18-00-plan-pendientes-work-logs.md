# Plan de pendientes desde work-logs

Fecha: 2026-01-29
Estado: Draft

## 1. Resumen

Este plan consolida los pendientes identificados en los work-logs de
Sphinx para priorizar bloqueos de infraestructura, deuda tecnica de
contenido y acciones de ejecucion de builds.

Objetivos del plan:
- Asegurar acceso confiable a recursos externos usados por Sphinx.
- Reducir warnings para mejorar la salud de la documentacion.
- Obtener builds reproducibles sin errores criticos en `make html` y
  `make livehtml`.

Resultado esperado:
- Inventarios intersphinx accesibles sin necesidad de proxy manual.
- Warnings documentales acotados y bajo control para QA/CI.
- Evidencia de ejecucion de builds con resultados archivados en work-logs.

## 2. Pendientes por categoria

### 2.1 Infraestructura (Prioridad Alta)

P-001: Resolver acceso a inventarios intersphinx bloqueados por proxy.
- Impacto: Warnings en `make livehtml` y `make html`.
- Acciones sugeridas:
  - Configurar proxy o mirror interno para `docs.python.org` y
    `sphinx-doc.org`.
  - Validar conectividad con `curl -I`.
  - Documentar configuracion aplicada (variables de entorno, flags o
    cambios en `conf.py`).
  - Habilitar inventarios locales (`objects.inv`) si el proxy sigue
    bloqueando el acceso remoto.
  - Ejecutar `scripts/setup_intersphinx_via_git.sh` para clonar
    inventarios via git cuando `curl` no funcione.
- Criterio de cierre:
  - Comando `curl -I` retorna `200` o `302` para ambos inventarios.
  - Warnings `intersphinx` dejan de aparecer en el build.
- Estado: En progreso (validacion de proxy realizada).
- Evidencia:
  - `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`
  - `.mywork/work-logs/2026-01-29-17-22-analisis-capacidades-entorno.md`
  - `.mywork/work-logs/2026-01-29-19-20-infra-proxy-mise.md`
  - `.mywork/work-logs/2026-01-29-19-35-clone-sphinx.md`
  - `.mywork/work-logs/2026-01-29-20-10-infra-intersphinx-local-inv.md`
  - `.mywork/work-logs/2026-01-29-20-45-infra-intersphinx-git-clone.md`
  - `.mywork/adr/ADR-2026-01-29-intersphinx-inventories-via-git.md`

P-002: Evaluar restricciones de red en repos externos (mise).
- Impacto: Potencial bloqueo de instalacion de herramientas externas.
- Acciones sugeridas:
  - Confirmar si se requiere `mise`.
  - Usar mirrors permitidos o deshabilitar repos bloqueados.
  - Registrar alternativa aprobada (por ejemplo, version fija en `tools/`).
- Criterio de cierre:
  - Dependencias externas se instalan sin errores de red.
- Estado: En progreso (repositorio sin referencias directas a `mise`).
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-22-analisis-capacidades-entorno.md`
  - `.mywork/work-logs/2026-01-29-19-20-infra-proxy-mise.md`

### 2.2 Calidad de documentacion (Prioridad Alta)

P-003: Reducir warnings por documentos fuera de toctree.
- Impacto: 1062 warnings en build `make html`.
- Acciones sugeridas:
  - Agregar documentos de `source/docs_maestros` a toctrees pertinentes.
  - Definir criterios de inclusion (por ejemplo, solo documentos activos).
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Criterio de cierre:
  - Warnings de `not in toctree` <= 10.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-004: Corregir referencias a documentos inexistentes (`ref.doc/ref.ref`).
- Impacto: Warnings constantes en builds.
- Acciones sugeridas:
  - Revisar referencias en `source/01_fundamentos`,
    `source/02_procedimientos` y `source/index.rst`.
  - Actualizar rutas o eliminar referencias obsoletas.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Criterio de cierre:
  - Warnings `ref.doc` y `ref.ref` eliminados en el build.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-005: Eliminar referencias duplicadas en toctrees.
- Impacto: Warnings de documentos referenciados en multiples toctrees.
- Acciones sugeridas:
  - Consolidar inclusion de documentos en un toctree unico.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Criterio de cierre:
  - Sin warnings de documentos duplicados en toctree.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-006: Resolver warnings de numeracion de secciones (secnum).
- Impacto: Warnings en `make livehtml` por `nested numbered toctree`.
- Acciones sugeridas:
  - Revisar configuracion de `numbered` en `source/index.rst`.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Criterio de cierre:
  - Sin warnings `nested numbered toctree` en livehtml.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`

P-007: Corregir targets de cross-reference faltantes (myst.xref_missing).
- Impacto: Warnings de enlaces rotos en `arc42_documentation`.
- Acciones sugeridas:
  - Revisar y completar targets de referencia.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Criterio de cierre:
  - Sin warnings `myst.xref_missing` en el build.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-008: Resolver fallos de highlighting por lexers desconocidos.
- Impacto: Warnings por `plantuml`, `atl`, `ocl`.
- Acciones sugeridas:
  - Definir lexers validos o usar `text`.
- Estado: Mitigado temporalmente via `pygments_lexers` en `source/conf.py`.
- Criterio de cierre:
  - Sin warnings `Could not lex` en el build.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-009: Revisar warning de `sphinx_tabs` (RemovedInSphinx90Warning).
- Impacto: Advertencia de compatibilidad futura.
- Acciones sugeridas:
  - Actualizar extension o ajustar configuracion.
- Estado: Mitigado temporalmente via `warnings.filterwarnings` en `source/conf.py`.
- Criterio de cierre:
  - Sin warnings `RemovedInSphinx90Warning` en el build.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

### 2.3 Ejecucion y operacion (Prioridad Media)

P-010: Ejecutar `make livehtml` sin timeout para validar build.
- Impacto: Validacion completa del builder livehtml.
- Acciones sugeridas:
  - Ejecutar sin `timeout` tras resolver bloqueos de proxy.
  - Archivar salida de la ejecucion en un work-log dedicado.
- Criterio de cierre:
  - Build finaliza con codigo 0 y warnings bajo control.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`

P-011: Ejecutar `make html` sin warnings criticos y confirmar salida.
- Impacto: Build limpio para QA/CI.
- Acciones sugeridas:
  - Reintentar tras reducir warnings de calidad.
  - Capturar resumen de warnings y compararlo contra baseline.
- Criterio de cierre:
  - Warnings criticos = 0 y salida reproducible.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

## 3. Dependencias y bloqueos

- Bloqueo principal: acceso a inventarios intersphinx por proxy.
- Dependencia secundaria: disponibilidad de repos externos (mise).
- Otros riesgos:
  - Cambios en extensiones Sphinx que requieran upgrades coordinados.
  - Inconsistencias entre configuraciones locales vs CI.

## 4. Secuencia sugerida

1. Resolver bloqueos de infraestructura (P-001, P-002).
2. Atacar warnings de documentacion (P-003 a P-009).
3. Ejecutar validaciones finales (P-010, P-011).

Checklist de seguimiento:
- [ ] Bloqueos de proxy resueltos y documentados.
- [ ] Warnings reducidos segun criterios definidos.
- [ ] Builds ejecutadas y archivadas en work-logs.

## 5. Criterios de cierre

- Builds `make html` y `make livehtml` sin warnings criticos.
- Inventarios intersphinx accesibles sin proxy errors.
- Warnings reducidos a un nivel aceptable para QA.

## 6. Proximos pasos

- Confirmar responsables y fechas objetivo para cada pendiente.
- Agregar mini-plan de mitigacion si algun bloqueo persiste.
- Revisar si se requiere ADR por cambios permanentes en infraestructura.

## 7. Ejecucion del plan (que sigue)

La ejecucion inicia con las tareas de infraestructura, seguido por la
limpieza documental y las validaciones finales.

### 7.1 Preparacion

- Definir responsables y fechas para P-001 a P-002.
- Abrir tickets por cada pendiente con links a los work-logs.
- Crear ADR si la solucion de proxy o mirrors se vuelve permanente.

### 7.2 Implementacion

- Resolver P-001 y P-002, documentando configuraciones aplicadas.
- Ejecutar P-003 a P-009 siguiendo los criterios de cierre definidos.
- Registrar cada ajuste en un work-log con la evidencia correspondiente.

### 7.3 Validacion

- Ejecutar P-010 y P-011 sin timeout una vez reducidos los warnings.
- Comparar el resumen de warnings contra el baseline actual.
- Confirmar que los builds son reproducibles en el entorno destino.

### 7.4 Cierre

- Marcar como completados los pendientes con criterios satisfechos.
- Compartir resumen final con QA/CI y actualizar este plan si cambian
  prioridades o bloqueos.
