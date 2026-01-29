# README_ins_setup_java_portable.md

## 1. Propósito

Este documento define el flujo reproducible para instalar y usar **Java portable** dentro del proyecto, con el objetivo de ejecutar **PlantUML** (vía `tools/plantuml.jar`) desde Sphinx, sin requerir instalación global de Java.

El flujo está diseñado para:
- Entornos Windows + Git Bash/MSYS/WSL (shell `sh`)
- Ejecución determinística por proyecto
- Idempotencia
- Soporte de simulación (`--dry-run`) y reinstalación (`--force`)
- Logs explícitos en pantalla (sin silencios)

El repositorio contiene `tools/plantuml.jar` y la estructura de Sphinx (Makefile/make.bat/source/conf.py), por lo que este flujo completa la capa runtime requerida por PlantUML. :contentReference[oaicite:0]{index=0}

---

## 2. Alcance y componentes

### 2.1 Componentes del proyecto involucrados

- `scripts/setup_java.sh`  
  Script de bootstrap para instalar Java portable en el proyecto.

- `tools/plantuml.jar`  
  Runtime de PlantUML versionado dentro del repo.

- `config/sphinx/conf.py`  
  Configuración de Sphinx. Debe apuntar a Java portable y al JAR.

- `make.bat` / `Makefile`  
  Wrappers de build para Sphinx (Windows/Unix). :contentReference[oaicite:1]{index=1}

---

## 3. Diagrama del flujo (ASCII)

### 3.1 Flujo end-to-end: setup + build

```text
+--------------------------------------------------------------------------------------+
|                                      PROYECTO ADT                                     |
|                                                                                      |
|  Repo root                                                                           |
|  /e/Proyectos/Translate/ADT                                                          |
|                                                                                      |
|  +-------------------+         +-----------------------------+                        |
|  |  Python (.venv)   |         |  Java portable (project)     |                        |
|  |                   |         |  tools/java/jdk-17/           |                        |
|  |  - Sphinx          |         |  - bin/java.exe              |                        |
|  |  - myst-parser     |         |                             |                        |
|  |  - sphinx-tabs     |         +-----------------------------+                        |
|  |  - sphinx-design   |                          |                                     |
|  |  - copybutton      |                          |                                     |
|  |  - sphinxcontrib-  |                          v                                     |
|  |    plantuml        |         +-----------------------------+                        |
|  +-------------------+         |   PlantUML runtime           |                        |
|            |                   |   tools/plantuml.jar         |                        |
|            |                   +-----------------------------+                        |
|            |                                 |                                       |
|            v                                 v                                       |
|  +----------------------------------------------------------------------------------+ |
|  |                                  SPHINX BUILD                                     | |
|  |                                                                                  | |
|  |  config/sphinx/conf.py                                                           | |
|  |                                                                                  | |
|  |  extensions += sphinxcontrib.plantuml                                             | |
|  |  plantuml = "tools/java/jdk-17/bin/java.exe -jar tools/plantuml.jar"              | |
|  |                                                                                  | |
|  +-----------------------------------+----------------------------------------------+ |
|                                      |                                                |
|                                      v                                                |
|                         +------------------------------+                               |
|                         |  build/html (salida docs)    |                               |
|                         |  - HTML generado             |                               |
|                         |  - Diagramas PlantUML        |                               |
|                         +------------------------------+                               |
+--------------------------------------------------------------------------------------+
````

### 3.2 Flujo del script `scripts/setup_java.sh` (idempotente)

```text
+---------------------------+
| scripts/setup_java.sh     |
+---------------------------+
             |
             v
+---------------------------+
| PASO 1: detectar Java     |
| tools/java/jdk-17/bin/... |
+---------------------------+
   |                     |
   | existe y funciona   | no existe / no funciona
   | (y no --force)      |
   v                     v
+-------------------+   +----------------------------+
| SALIR (OK)        |   | PASO 2: crear directorios  |
| no hace cambios   |   | tools/_downloads, tools/java|
+-------------------+   +----------------------------+
                               |
                               v
                     +----------------------------+
                     | PASO 3: descargar ZIP      |
                     | aka.ms -> tools/_downloads |
                     +----------------------------+
                               |
                               v
                     +----------------------------+
                     | PASO 4: unzip en /tmp      |
                     | /tmp/java_portable_<pid>   |
                     +----------------------------+
                               |
                               v
                     +----------------------------+
                     | detectar carpeta real JDK  |
                     | (contiene bin/java.exe)    |
                     +----------------------------+
                               |
                               v
                     +----------------------------+
                     | PASO 5: copiar a ruta fija |
                     | tools/java/jdk-17          |
                     +----------------------------+
                               |
                               v
                     +----------------------------+
                     | PASO 6: validar java -ver  |
                     +----------------------------+
                               |
                               v
                     +----------------------------+
                     | limpiar /tmp               |
                     +----------------------------+
                               |
                               v
                     +----------------------------+
                     | FIN (OK)                   |
                     +----------------------------+
```

---

## 4. Ruta de instalación (contrato)

El script instala Java portable en la ruta estable:

* Java Home: `tools/java/jdk-17/`
* Java ejecutable: `tools/java/jdk-17/bin/java.exe`
* ZIP cache (descarga): `tools/_downloads/microsoft-jdk-17-windows-x64.zip`

Este contrato permite que `conf.py` apunte a una ruta fija y evita depender de `PATH` o `JAVA_HOME` global.

---

## 5. Flujo operativo

### 5.1 Precondiciones

Requisitos del shell (para ejecutar el script):

* `bash`
* `curl`
* `unzip`

Notas:

* El script no instala `curl` ni `unzip`. Solo los usa si están disponibles.
* Si el entorno corporativo restringe descargas (proxy/TLS), el paso de descarga puede fallar y debe ajustarse (ver sección 8).

---

### 5.2 Paso 1: Simulación (sin cambios)

Ejecutar siempre primero:

```bash
./scripts/setup_java.sh --dry-run
```

Salida esperada:

* Muestra PASO 1/6 a PASO 6/6
* No crea carpetas reales
* No descarga ZIP real
* No intenta inspeccionar /tmp (la detección se simula)

Objetivo:

* Validar rutas, variables, comandos y narrativa sin modificar el repo.

---

### 5.3 Paso 2: Instalación real (idempotente)

Ejecutar:

```bash
./scripts/setup_java.sh
```

Comportamiento:

* Si ya existe `tools/java/jdk-17/bin/java.exe` y responde a `-version`, el script no reinstala.
* Si no existe, descarga el ZIP, descomprime a `/tmp`, detecta el `java.exe` dentro del ZIP y copia al destino estable del proyecto.
* Al final ejecuta una validación: `tools/java/jdk-17/bin/java.exe -version`

---

### 5.4 Paso 3: Reinstalación (forzada)

Usar solo cuando:

* La instalación quedó corrupta
* Se desea reemplazar por una descarga nueva
* Se cambió el ZIP o se requiere regenerar la carpeta

Ejecutar:

```bash
./scripts/setup_java.sh --force
```

---

## 6. Integración con Sphinx + PlantUML

### 6.1 Dependencia Python (extensión Sphinx)

En el entorno Python del proyecto (por ejemplo `.venv`) debe existir:

* `sphinxcontrib-plantuml`

Instalación típica:

```bash
python -m pip install sphinxcontrib-plantuml
```

---

### 6.2 Configuración en `config/sphinx/conf.py`

Debe existir (o agregarse) lo siguiente:

1. La extensión:

```python
extensions.append("sphinxcontrib.plantuml")
```

2. La definición explícita del ejecutable Java portable y el JAR:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # raíz del repo
JAVA = BASE_DIR / "tools" / "java" / "jdk-17" / "bin" / "java.exe"
PLANTUML_JAR = BASE_DIR / "tools" / "plantuml.jar"

plantuml = f'"{JAVA}" -jar "{PLANTUML_JAR}"'
```

Esto garantiza:

* Reproducibilidad
* No dependencia de Java global
* Rutas robustas (espacios, rutas absolutas)

---

## 7. Build de documentación

Una vez instalado Java portable y configurado PlantUML:

### Opción A (directa, sin Makefile)

```bash
python -m sphinx -b html source build/html
```

### Opción B (Makefile / make.bat)

* En Windows: `.\make.bat html`
* En Unix/WSL: `make html`

Nota:

* Si tu `make` está usando `/usr/bin/sh`, asegúrate que tu entorno Python y Sphinx estén accesibles en ese contexto.

---

## 8. Manejo de fallos y diagnóstico

### 8.1 Verificar Java portable

```bash
./tools/java/jdk-17/bin/java.exe -version
```

### 8.2 Verificar PlantUML con el JAR del repo

```bash
./tools/java/jdk-17/bin/java.exe -jar tools/plantuml.jar -version
```

### 8.3 Fallo de descarga (proxy/TLS corporativo)

Síntomas típicos:

* `curl` falla con errores TLS
* `curl` no puede resolver DNS
* `curl` recibe HTML de portal cautivo

Acciones:

* Configurar `HTTPS_PROXY` / `HTTP_PROXY` en el entorno del shell
* Descargar el ZIP manualmente y colocarlo en:
  `tools/_downloads/microsoft-jdk-17-windows-x64.zip`
  Luego reejecutar:
  `./scripts/setup_java.sh --force`

---

## 9. Política recomendada de versionado

Recomendación para repositorios:

* No versionar `tools/java/jdk-17/` (carpeta grande)
* Sí versionar el script `scripts/setup_java.sh`
* Sí versionar `tools/plantuml.jar` (control explícito de versión)

El script permite reproducir localmente el runtime en cada entorno sin “setup global”.

---

## 10. Referencias internas del repo

* Estructura de Sphinx y presencia de `tools/plantuml.jar`, `Makefile`, `make.bat`: 
* Estilo base de scripts con `--dry-run` y pasos: `scripts/clonar_repo_arc42.sh` 

```
::contentReference[oaicite:4]{index=4}
```
