# Plan de pendientes desde work-logs

Fecha: 2026-01-29
Estado: Draft

## 1. Resumen

Este plan consolida los pendientes identificados en los work-logs de
Sphinx para priorizar bloqueos de infraestructura, deuda tecnica de
contenido y acciones de ejecucion de builds.

## 2. Pendientes por categoria

### 2.1 Infraestructura (Prioridad Alta)

P-001: Resolver acceso a inventarios intersphinx bloqueados por proxy.
- Impacto: Warnings en `make livehtml` y `make html`.
- Acciones sugeridas:
  - Configurar proxy o mirror interno para `docs.python.org` y
    `sphinx-doc.org`.
  - Validar conectividad con `curl -I`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`
  - `.mywork/work-logs/2026-01-29-17-22-analisis-capacidades-entorno.md`

P-002: Evaluar restricciones de red en repos externos (mise).
- Impacto: Potencial bloqueo de instalacion de herramientas externas.
- Acciones sugeridas:
  - Confirmar si se requiere `mise`.
  - Usar mirrors permitidos o deshabilitar repos bloqueados.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-22-analisis-capacidades-entorno.md`

### 2.2 Calidad de documentacion (Prioridad Alta)

P-003: Reducir warnings por documentos fuera de toctree.
- Impacto: 1062 warnings en build `make html`.
- Acciones sugeridas:
  - Agregar documentos de `source/docs_maestros` a toctrees pertinentes.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-004: Corregir referencias a documentos inexistentes (`ref.doc/ref.ref`).
- Impacto: Warnings constantes en builds.
- Acciones sugeridas:
  - Revisar referencias en `source/01_fundamentos`,
    `source/02_procedimientos` y `source/index.rst`.
  - Actualizar rutas o eliminar referencias obsoletas.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-005: Eliminar referencias duplicadas en toctrees.
- Impacto: Warnings de documentos referenciados en multiples toctrees.
- Acciones sugeridas:
  - Consolidar inclusion de documentos en un toctree unico.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-006: Resolver warnings de numeracion de secciones (secnum).
- Impacto: Warnings en `make livehtml` por `nested numbered toctree`.
- Acciones sugeridas:
  - Revisar configuracion de `numbered` en `source/index.rst`.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`

P-007: Corregir targets de cross-reference faltantes (myst.xref_missing).
- Impacto: Warnings de enlaces rotos en `arc42_documentation`.
- Acciones sugeridas:
  - Revisar y completar targets de referencia.
- Estado: Mitigado temporalmente via `suppress_warnings` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-008: Resolver fallos de highlighting por lexers desconocidos.
- Impacto: Warnings por `plantuml`, `atl`, `ocl`.
- Acciones sugeridas:
  - Definir lexers validos o usar `text`.
- Estado: Mitigado temporalmente via `pygments_lexers` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

P-009: Revisar warning de `sphinx_tabs` (RemovedInSphinx90Warning).
- Impacto: Advertencia de compatibilidad futura.
- Acciones sugeridas:
  - Actualizar extension o ajustar configuracion.
- Estado: Mitigado temporalmente via `warnings.filterwarnings` en `source/conf.py`.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

### 2.3 Ejecucion y operacion (Prioridad Media)

P-010: Ejecutar `make livehtml` sin timeout para validar build.
- Impacto: Validacion completa del builder livehtml.
- Acciones sugeridas:
  - Ejecutar sin `timeout` tras resolver bloqueos de proxy.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-16-57-make-livehtml-resultados.md`

P-011: Ejecutar `make html` sin warnings criticos y confirmar salida.
- Impacto: Build limpio para QA/CI.
- Acciones sugeridas:
  - Reintentar tras reducir warnings de calidad.
- Evidencia:
  - `.mywork/work-logs/2026-01-29-17-12-make-html-sin-timeout.md`

## 3. Dependencias y bloqueos

- Bloqueo principal: acceso a inventarios intersphinx por proxy.
- Dependencia secundaria: disponibilidad de repos externos (mise).

## 4. Secuencia sugerida

1. Resolver bloqueos de infraestructura (P-001, P-002).
2. Atacar warnings de documentacion (P-003 a P-009).
3. Ejecutar validaciones finales (P-010, P-011).

## 5. Criterios de cierre

- Builds `make html` y `make livehtml` sin warnings criticos.
- Inventarios intersphinx accesibles sin proxy errors.
- Warnings reducidos a un nivel aceptable para QA.
