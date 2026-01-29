# 2026-01-29-11-58 - Notas de instalacion PyEnchant

Fecha: 2026-01-29 11:58
Timestamp: 2026-01-29 11:58
Autor: AI Assistant
Proyecto: ADT Documentation
Version: 1.7.1

## Resumen Ejecutivo

Se registro una guia operativa para instalar PyEnchant y la libreria C
`enchant` en diferentes plataformas, junto con notas sobre diccionarios
y troubleshooting. El objetivo es contar con referencia inmediata para
resolver el error de `sphinxcontrib.spelling` en entornos variados.

## Contexto

### Situacion Inicial
El build de Sphinx falla por falta de la libreria C `enchant`.

### Motivacion
Disponer de un instructivo claro para instalar `enchant` y configurar
PyEnchant segun la plataforma.

### Objetivo
Documentar pasos y consideraciones por plataforma, incluyendo
troubleshooting y manejo de diccionarios.

## Trabajo Realizado

### Paso 1: Consolidacion de notas de instalacion
Se recopilaron las indicaciones oficiales de instalacion y requisitos
para PyEnchant, incluyendo dependencias del sistema, diccionarios y
verificacion de providers.

### Paso 2: Instalacion y verificacion en Ubuntu 24.04
Se instalaron los paquetes necesarios y se valido la deteccion de
providers y diccionarios en el entorno actual.

```bash
apt-get update
apt-get install -y libenchant-2-2 python3-enchant hunspell-en-us
python3 - <<'PY'
import enchant
broker = enchant.Broker()
print(broker.describe())
print(sorted(broker.list_languages())[:5])
PY
```

Resultado: `enchant` y `python3-enchant` quedaron instalados, con
providers Aspell/Hunspell disponibles y lenguajes `en` detectados.

## Notas de Instalacion (Referencia)

### Requisitos generales
- PyEnchant es compatible con Python 3.7+.
- Necesita encontrar la libreria C `enchant` y los diccionarios
  adecuados por idioma.

### Instalacion de la libreria C `enchant`

#### FreeBSD
```bash
pkg install enchant-2
```

#### Linux
Instalar `libenchant` con el package manager de la distribucion.
PyEnchant usa `ctypes.util.find_library()` y requiere herramientas como
`ldconfig`, `gcc`, `objdump` o `ld` para detectar la libreria.

#### macOS (Homebrew)
```bash
brew update
brew install enchant
```

#### macOS (MacPorts)
```bash
sudo port install enchant2 +aspell +hunspell +applespell
```

#### Windows
Opciones:
- **Binary wheel** (pip): incluye enchant precompilado.
  - Pros: funciona en la mayoria de casos.
  - Cons: solo hunspell + diccionario ingles + incluye glib2.dll.
- **MinGW**: instalar MinGW y usar `pacman` para enchant y dependencias.
  - Instalar PyEnchant sin wheel:

```bash
pip install --no-binary pyenchant
```

### Instalacion de diccionarios
1. Listar providers y lenguajes:

```python
import enchant
broker = enchant.Broker()
broker.describe()
broker.list_languages()
```

2. Si falta el idioma, instalar el diccionario del provider disponible
   (ej: hunspell).

- FreeBSD/Linux/macOS: instalar paquetes como `hunspell-de`.
- Windows (wheel): copiar `.dic` y `.aff` a
  `/path/to/enchant/data/mingw<bits>/enchant/share/hunspell`.

### Troubleshooting
- Definir `PYENCHANT_VERBOSE_FIND` y ejecutar:

```bash
python -c 'import enchant'
```

- Si persiste, abrir issue con el output del comando.

## Archivos Afectados

### Creados
- `.mywork/work-logs/2026-01-29-11-58-notas-instalacion-pyenchant.md`
  - Log con referencia de instalacion y troubleshooting.

## Resultados

### Validacion
- [x] Libreria `enchant` instalada y verificada en Ubuntu 24.04.

## Proximos Pasos

1. Reintentar builds de Sphinx con `sphinxcontrib.spelling`.
2. Instalar diccionarios adicionales si se requieren otros idiomas.

---

**Tags:** #sphinx #pyenchant #dependencias #instalacion
**Estado:** Completado
