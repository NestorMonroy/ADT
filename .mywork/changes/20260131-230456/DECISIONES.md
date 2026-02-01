# Decisiones - Sesión 20260131-230456

**Última actualización**: 2026-02-01 02:30

---

## DECISIÓN 6: 🔴 REGLA CRÍTICA - NO MÁS SCRIPTS AUTOMÁTICOS

**Fecha**: 2026-02-01 02:30  
**Severidad**: CRÍTICA  
**Contexto**: Script `fix_critical_titles.sh` dañó 5 archivos correctos

**QUÉ**: **PROHIBIR scripts automáticos de corrección RST**

**POR QUÉ**:
- Script modificó contenido dentro de `code-block` (ejemplos de código)
- Dañó 5 archivos que estaban correctos
- RST requiere entender contexto estructural, no solo patrones

**REGLA ESTABLECIDA**:

```
┌─────────────────────────────────────────────────────┐
│  ❌ PROHIBIDO: Scripts que modifican .rst           │
│  ✅ PERMITIDO: Scripts de análisis (read-only)      │
│  📋 MÉTODO: Correcciones MANUALES solamente         │
└─────────────────────────────────────────────────────┘
```

**TRADE-OFFS**:
- Más lento (manual)
- Más esfuerzo
- Pero: 0 riesgo de daño, control total

**DECISIÓN FINAL**: Solo correcciones manuales. Scripts solo para análisis.

---

## DECISIÓN 5: Revertir Script - Dañó Code-Blocks

**QUÉ**: Revertir TODOS los cambios de `fix_critical_titles.sh`

**ANÁLISIS**:
- 5 archivos DAÑADOS (espacios removidos de code-blocks)
- 1 archivo corregido (pero con underlines incorrectos)

**COMANDO**:
```bash
git restore source/01_fundamentos/_metodologias/metodo_por_defecto.rst
git restore source/01_fundamentos/index.rst
git restore source/02_procedimientos/workflow_general.rst
git restore source/06_casos_practicos/errores_comunes/error_01_omisiones.rst
git restore source/07_guias_uso/guia_rapida.rst
git restore source/biblioteca/ingenieria/sistemas/arquitectura/arc42_documentation/sections/01_introduction_goals/traduccion/seccion_1_2_quality_goals.rst
```

---

Ver archivo completo para todas las decisiones de la sesión.
