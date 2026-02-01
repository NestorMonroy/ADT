# Requirements: Reestructuración de /tmp/ADT/source

**Fecha**: 2026-02-01  
**Estado**: Draft - Pendiente definición del usuario  
**Autor**: Claude + Usuario

---

## 1. Contexto

### Situación Actual

La estructura de `/tmp/ADT/source/` contiene:

**Directorios numerados** (01-10):
- 01_fundamentos/
- 02_procedimientos/
- 03_estandares/
- 04_reglas_operativas/
- 05_herramientas_medios/
- 06_casos_practicos/
- 07_guias_uso/
- 08_prompts/
- 09_referencias/
- 10_apendices/

**Frameworks**:
- diataxis/ (4 cuadrantes: tutorials, how-to, reference, explanation)
- biblioteca/ (ciencias, informatica, ingenieria)

**Otros**:
- docs/
- docs_maestros/
- _static/ (css, img, js)
- _templates/

### Problema a Resolver

**[PENDIENTE - Necesita definición del usuario]**

¿Qué aspecto específico de la estructura quieres cambiar?

Opciones posibles:
1. Reorganizar directorios numerados
2. Cambiar jerarquía de biblioteca/
3. Simplificar estructura general
4. Mejorar naming conventions
5. Consolidar directorios duplicados
6. Alinear mejor con Diataxis/arc42
7. Otro cambio específico

---

## 2. Objetivos

### Objetivo Principal

**[PENDIENTE - Definir con usuario]**

### Objetivos Secundarios

**[PENDIENTE - Definir con usuario]**

---

## 3. Stakeholders

- Usuario del proyecto ADT
- Futuros colaboradores
- Sistema de build Sphinx

---

## 4. Requisitos Funcionales

**[PENDIENTE - Depende del cambio específico]**

### RF-001: [Por definir]

**[PENDIENTE]**

---

## 5. Requisitos No Funcionales

### RNF-001: Compatibilidad con Build Sphinx

**Descripción**: La nueva estructura DEBE ser compatible con Sphinx.

**Criterio de aceptación**:
- [ ] `./scripts/build.sh` pasa sin errores
- [ ] No hay WARNING críticos
- [ ] Todos los toctrees funcionan

### RNF-002: Preservar Contenido Existente

**Descripción**: NO se debe perder contenido durante reestructuración.

**Criterio de aceptación**:
- [ ] Todos los archivos .rst preservados
- [ ] Backups creados antes de mover
- [ ] Git history intacto

### RNF-003: Mantener Convenciones ADT

**Descripción**: Respetar metodología ADT (transformación, fidelidad estructural).

**Criterio de aceptación**:
- [ ] Estructura alineada con project-context
- [ ] Naming conventions consistentes

---

## 6. Restricciones

### Técnicas
- Sphinx requiere estructura específica (conf.py, index.rst)
- toctrees deben formar DAG (no ciclos)
- Rutas relativas en referencias entre documentos

### Organizacionales
- Cambio debe ser reversible (git)
- Documentar decisión de cambio
- Validar con build completo

### Temporales
- **[PENDIENTE - Definir con usuario]**

---

## 7. Fuera de Scope

**[PENDIENTE - Definir con usuario]**

---

## 8. Preguntas Pendientes

### P1: ¿Cuál es el problema específico con la estructura actual?

**[ESPERANDO RESPUESTA DEL USUARIO]**

### P2: ¿Qué estructura ideal visualizas?

**[ESPERANDO RESPUESTA DEL USUARIO]**

### P3: ¿Hay contenido que se usa más/menos?

**[ESPERANDO RESPUESTA DEL USUARIO]**

### P4: ¿La nueva estructura debe seguir algún patrón específico?

Opciones:
- Por tipo de contenido (Diataxis)
- Por dominio (biblioteca actual)
- Por nivel de madurez
- Mixto

**[ESPERANDO RESPUESTA DEL USUARIO]**

### P5: ¿Timeline esperado para el cambio?

**[ESPERANDO RESPUESTA DEL USUARIO]**

---

## 9. Criterios de Aceptación Generales

- [ ] Build Sphinx pasa sin errores
- [ ] Estructura más clara/mantenible que actual
- [ ] Documentación actualizada (README, índices)
- [ ] Usuario satisfecho con cambio
- [ ] Cambios commiteados con mensajes claros

---

## 10. Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Romper build Sphinx | Media | Alto | Validación continua, backups |
| Perder contenido | Baja | Crítico | Git + backups explícitos |
| Referencias rotas | Alta | Medio | Actualizar todas las referencias |
| Confusión usuarios | Media | Medio | Documentar cambios claramente |

---

## 11. Siguiente Paso

**Acción requerida**: Usuario debe definir:

1. ¿Qué problema específico quieres resolver?
2. ¿Cómo visualizas la estructura ideal?
3. ¿Hay prioridades o fases?

Una vez definido, proceder a:
→ FASE 2: Design (propuesta técnica)

---

**Estado**: ⏸️ PAUSADO - Esperando input del usuario  
**Próxima fase**: Design (cuando se definan requirements)

