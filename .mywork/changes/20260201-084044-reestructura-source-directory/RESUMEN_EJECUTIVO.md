# Resumen Ejecutivo - Reorganización Disruptiva

**Decisión requerida**: ¿Aprobamos esta reorganización?  
**Tiempo de ejecución**: 30 minutos  
**Impacto**: Alto (mejora claridad, facilita mantenimiento)

---

## 🎯 PROBLEMA

Actualmente tienes **3 directorios confusos** en `/tmp/ADT/source/`:
- `diataxis/` - vacío (solo 1 archivo)
- `docs/` - ¿meta-docs o pipeline?
- `docs_maestros/` - ¿arquitectura o pipeline?

**Resultado**: No está claro DÓNDE poner nuevos documentos.

---

## ✅ SOLUCIÓN

### Crear 2 zonas claras:

1. **`source/pipeline/`** → Documentación de CÓMO usar ADT (para usuarios)
   - Migrar 01-10 aquí

2. **`/docs/`** → Documentación SOBRE el proyecto (para desarrolladores)
   - Migrar docs_maestros → docs/arquitectura/
   - Migrar docs → docs/desarrollo/
   - Eliminar diataxis (vacío)

---

## 📋 ESTRUCTURA PROPUESTA

```
/tmp/ADT/
├── source/
│   ├── pipeline/           ✅ Cómo usar ADT (01-10)
│   ├── biblioteca/         ✅ Contenido traducido
│   └── _static, _templates ✅ Utilidades
│
└── docs/                   ✅ NUEVO: Meta-docs
    ├── arquitectura/       ✅ Arquitectura, metodología
    └── desarrollo/         ✅ Integraciones, status
```

---

## 🎯 REGLA SIMPLE

| Tipo de documento | Va en... |
|-------------------|----------|
| Para **usuarios** del pipeline | `source/pipeline/` |
| **Contenido** traducido | `source/biblioteca/` |
| Sobre **arquitectura** | `docs/arquitectura/` |
| Sobre **desarrollo** | `docs/desarrollo/` |

---

## 📊 BENEFICIOS

| Antes | Después |
|-------|---------|
| 16 directorios en source/ | 5 directorios |
| ❓ ¿Dónde va esto? | ✅ Ubicación obvia |
| Todo mezclado | Clara separación |

---

## ⏱️ COSTO

**30 minutos** para ejecutar migración completa.

---

## 🚦 DECISIÓN

**Opción A**: Ejecutar reorganización completa (RECOMENDADO)  
**Opción B**: Versión conservadora (solo mover docs_maestros)  
**Opción C**: No hacer nada (mantener confusión actual)

---

**¿Cuál eliges?**
