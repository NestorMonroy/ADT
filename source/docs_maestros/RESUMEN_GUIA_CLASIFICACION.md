# Guía Metodológica de Clasificación Documental - Resumen Ejecutivo

**Código:** META_BIB_001
**Versión:** 1.0.0
**Fecha:** 2026-01-28
**Estado:** NORMATIVO

---

## [TARGET] Propósito

Sistema de clasificación jerárquica para organizar libros técnicos traducidos en el proyecto ADT.

**Objetivo:** Asignar a cada libro una ubicación única y predecible en `/biblioteca`.

---

## [TABLE] Sistema de Clasificación

### Jerarquía de 4 Niveles

```
CATEGORÍA -> SUBCATEGORÍA -> ESPECIALIDAD -> NÚMERO
 3 letras 3 letras 3 letras 001-999

Ejemplo: INF.PRG.FST.001
 | | | +-- Número secuencial
 | | +----- Especialidad (Full-Stack)
 | +--------- Subcategoría (Programación)
 +------------- Categoría (Informática)
```

---

## DIRECTORY: Categorías Principales

| Código | Nombre | Ámbito |
|--------|--------|--------|
| **INF** | Informática | Programación, IA, Redes, Seguridad |
| **ING** | Ingeniería | Arquitectura, Sistemas, Metodologías |
| **CIE** | Ciencias | Matemáticas, Estadística, Física |

---

## [COMPUTER] Subcategorías Informática (INF)

| Código | Nombre | Ejemplos |
|--------|--------|----------|
| **PRG** | Programación | Python, JavaScript, Full-Stack |
| **IAR** | Inteligencia Artificial | ML, Deep Learning, NLP |
| **RED** | Redes | TCP/IP, Network Security |
| **SEG** | Seguridad | Ciberseguridad, Criptografía |
| **BDD** | Bases de Datos | SQL, NoSQL, PostgreSQL |
| **SOP** | Sistemas Operativos | Linux, Windows Administration |
| **WEB** | Desarrollo Web | HTML, CSS, Web APIs |
| **MOV** | Desarrollo Móvil | iOS, Android, React Native |
| **DVC** | DevOps y Cloud | Docker, Kubernetes, AWS |
| **ALG** | Algoritmos | Data Structures, Algorithms |

---

## [TOOL] Subcategorías Ingeniería (ING)

| Código | Nombre | Ejemplos |
|--------|--------|----------|
| **SIS** | Sistemas | System Design, Distributed Systems |
| **ARQ** | Arquitectura | Clean Architecture, Microservices |
| **MET** | Metodologías | Agile, Scrum, DevOps |
| **REQ** | Requisitos | Requirements Engineering |
| **PRU** | Pruebas | TDD, Unit Testing, QA |
| **MOD** | Modelado | UML, BPMN, Formal Methods |

---

## Subcategorías Ciencias (CIE)

| Código | Nombre | Ejemplos |
|--------|--------|----------|
| **MAT** | Matemáticas | Linear Algebra, Calculus |
| **EST** | Estadística | Statistical Analysis, Probability |
| **FIS** | Física | Computational Physics |
| **BIO** | Biología | Bioinformatics, Genomics |

---

## [LEARN] Especialidades Más Comunes

### Programación (INF.PRG)

```
FST -> Full-Stack
FRE -> Frontend
BAC -> Backend
PYT -> Python
JAV -> JavaScript
TSC -> TypeScript
REA -> React
VUE -> Vue.js
ANG -> Angular
NOD -> Node.js
DJA -> Django
FLA -> Flask
```

### IA (INF.IAR)

```
MLF -> Machine Learning Fundamentals
DLE -> Deep Learning
NLP -> Natural Language Processing
CVS -> Computer Vision
RFO -> Reinforcement Learning
```

### DevOps (INF.DVC)

```
DOC -> Docker
KUB -> Kubernetes
AWS -> Amazon Web Services
AZU -> Microsoft Azure
GCP -> Google Cloud Platform
TER -> Terraform
ANS -> Ansible
```

### Arquitectura (ING.ARQ)

```
MIC -> Microservicios
CLE -> Clean Architecture
DDD -> Domain-Driven Design
ARC -> arc42
HEX -> Hexagonal Architecture
```

---

## [WARNING] Proceso de Clasificación en 4 Pasos

### Paso 1: Determinar Categoría

```
¿El libro trata de...?

-> Programación, IA, redes, bases de datos?
 [OK] INFORMÁTICA (INF)

-> Arquitectura de software, metodologías?
 [OK] INGENIERÍA (ING)

-> Matemáticas aplicadas, física, biología computacional?
 [OK] CIENCIAS (CIE)
```

### Paso 2: Determinar Subcategoría

```
Analizar tema dominante del libro:
- ¿De qué trata principalmente?
- Revisar tabla de contenidos
- Buscar coincidencia con subcategorías existentes
```

### Paso 3: Determinar Especialidad

```
Identificar tecnología/framework principal:
- Extraer tecnologías del título
- Priorizar según peso en contenido
- Buscar coincidencia con especialidades
- Crear nueva si es necesario (y tiene demanda)
```

### Paso 4: Asignar Número Secuencial

```bash
# Verificar último número usado
ls /biblioteca/informatica/programacion/full_stack/

# Asignar siguiente número
001, 002, 003... (sin saltos)
```

---

## [NOTE] Ejemplos Completos

### Ejemplo 1: Full-Stack Development

```
Libro: "Modern Full-Stack Development: Using TypeScript, React,
 Node.js, Webpack, Python, Django, and Docker"

PASO 1: Categoría
-> Programación con frameworks -> INFORMÁTICA (INF)

PASO 2: Subcategoría
-> Múltiples lenguajes/frameworks -> PROGRAMACIÓN (PRG)

PASO 3: Especialidad
-> "Full-Stack Development" en título -> FULL-STACK (FST)

PASO 4: Número
-> Primer libro en la especialidad -> 001

RESULTADO: INF.PRG.FST.001

RUTA: /biblioteca/informatica/programacion/full_stack/
 Modern_Full_Stack_Development_Zammetti_2ed/
```

### Ejemplo 2: Machine Learning

```
Libro: "Machine Learning with Python"

PASO 1: -> INFORMÁTICA (INF)
PASO 2: -> INTELIGENCIA ARTIFICIAL (IAR)
PASO 3: -> MACHINE LEARNING FUNDAMENTALS (MLF)
PASO 4: -> 001

RESULTADO: INF.IAR.MLF.001

RUTA: /biblioteca/informatica/inteligencia_artificial/machine_learning/
 Machine_Learning_with_Python_Johnson_2025/
```

### Ejemplo 3: Software Architecture

```
Libro: "Software Architecture: The Hard Parts"

PASO 1: -> INGENIERÍA (ING)
PASO 2: -> ARQUITECTURA (ARQ)
PASO 3: -> GENERAL (GEN)
PASO 4: -> 001

RESULTADO: ING.ARQ.GEN.001

RUTA: /biblioteca/ingenieria/arquitectura/general/
 Software_Architecture_Hard_Parts_Ford_2023/
```

### Ejemplo 4: Docker

```
Libro: "Docker Deep Dive"

PASO 1: -> INFORMÁTICA (INF)
PASO 2: -> DEVOPS Y CLOUD (DVC)
PASO 3: -> DOCKER (DOC)
PASO 4: -> 001

RESULTADO: INF.DVC.DOC.001

RUTA: /biblioteca/informatica/devops/docker/
 Docker_Deep_Dive_Poulton_2024/
```

---

## DIRECTORY: Estructura de Carpetas

```
/biblioteca/
|
+-- _metadata_biblioteca/ # Metadata del sistema
| +-- META_BIB_001_Sistema_Clasificacion_1_0_0.rst
| +-- META_BIB_002_Guia_Organizacion_1_0_0.rst
| +-- catalogo_completo.rst
| +-- catalogo_numeros.txt
|
+-- informatica/ # CATEGORÍA
| +-- programacion/ # SUBCATEGORÍA
| | +-- full_stack/ # ESPECIALIDAD
| | | +-- Modern_Full_Stack_Development_Zammetti_2ed/ # LIBRO
| | | +-- metadata_libro.rst
| | | +-- index.rst
| | | +-- glosario_acumulativo.rst
| | | +-- Chapter_01_*/
| | | +-- Chapter_02_*/
| | | +-- ...
| | +-- react/
| | +-- python/
| | +-- typescript/
| |
| +-- inteligencia_artificial/
| | +-- machine_learning/
| | +-- deep_learning/
| |
| +-- devops/
| +-- docker/
| +-- kubernetes/
|
+-- ingenieria/
| +-- arquitectura/
| +-- sistemas/
|
+-- ciencias/
 +-- matematicas/
```

---

## FILE: Estructura Interna de Libro

```
Libro_Ejemplo/
+-- metadata_libro.rst # [STAR] OBLIGATORIO
+-- index.rst # [STAR] OBLIGATORIO
+-- glosario_acumulativo.rst # [STAR] OBLIGATORIO
|
+-- Chapter_01_Titulo/
| +-- original/
| | +-- chapter_01.pdf
| +-- traduccion/
| | +-- capitulo_01.rst
| +-- glosario_capitulo.rst
| +-- notas_traduccion.rst
| +-- figuras/
|
+-- Chapter_02_Titulo/
| +-- ...
|
+-- appendices/
+-- front_matter/
+-- back_matter/
```

---

## [TAG] Formato del Código

### Válido [OK]

```
INF.PRG.FST.001 [OK] Correcto
INF.IAR.MLF.023 [OK] Correcto
ING.ARQ.MIC.005 [OK] Correcto
```

### Inválido [ERROR]

```
inf.prg.fst.001 [ERROR] Minúsculas
INF.PROG.FST.001 [ERROR] Subcategoría 4 letras
INF.PRG.FS.001 [ERROR] Especialidad 2 letras
INF.PRG.FST.1 [ERROR] Número sin ceros a la izquierda
INF.PRG.FST.1000 [ERROR] Número > 999
```

---

## [LIST] Checklist de Clasificación

```
[ ] PASO 1: Categoría determinada (INF/ING/CIE)
[ ] PASO 2: Subcategoría determinada (XXX)
[ ] PASO 3: Especialidad determinada (XXX)
[ ] PASO 4: Número asignado (001-999)
[ ] Código completo generado (XXX.XXX.XXX.XXX)
[ ] Ruta de carpeta generada
[ ] Estructura de carpetas creada
[ ] metadata_libro.rst creado
[ ] Catálogo actualizado
[ ] Revisión por segundo clasificador
[ ] Clasificación finalizada
```

---

## FAQ Rápido

**P: ¿Puedo cambiar la clasificación después?**
R: SÍ, pero requiere aprobación y actualización de metadata. Evitar si es posible.

**P: ¿Qué hago si no existe la especialidad?**
R: Proponer nueva especialidad con código de 3 letras y justificación.

**P: ¿Los números deben ser consecutivos?**
R: SÍ. 001, 002, 003... sin saltos. No reutilizar números eliminados.

**P: ¿Puedo tener un libro en dos categorías?**
R: NO. Cada libro tiene UNA sola ubicación.

**P: ¿Mayúsculas o minúsculas?**
R: SIEMPRE MAYÚSCULAS.

---

## [TARGET] Reglas de Oro

1. [OK] **Un libro = Una ubicación** (no clasificación múltiple)
2. [OK] **Códigos SIEMPRE en mayúsculas**
3. [OK] **Números secuenciales sin saltos** (001, 002, 003...)
4. [OK] **No reutilizar números** de libros eliminados
5. [OK] **Exactamente 3 letras** para cada nivel
6. [OK] **Pensar bien la clasificación inicial** (evitar reclasificaciones)
7. [OK] **Documentar siempre** en metadata_libro.rst
8. [OK] **Actualizar catálogo** después de cada clasificación

---

## Tabla de Referencia Rápida

### Decisión de Categoría

| Si el libro trata principalmente de... | Categoría |
|----------------------------------------|-----------|
| Programación, frameworks, IA, redes | **INF** |
| Arquitectura, metodologías, procesos | **ING** |
| Matemáticas, física, biología computacional | **CIE** |

### Subcategorías Top 10

| Código | Nombre | Uso Típico |
|--------|--------|------------|
| **PRG** | Programación | Lenguajes, frameworks generales |
| **IAR** | Inteligencia Artificial | ML, DL, NLP, CV |
| **DVC** | DevOps y Cloud | Docker, K8s, AWS, Azure |
| **ARQ** | Arquitectura | Patrones, microservicios |
| **BDD** | Bases de Datos | SQL, NoSQL, diseño |
| **WEB** | Desarrollo Web | HTML, CSS, APIs |
| **RED** | Redes | Protocolos, seguridad de red |
| **SEG** | Seguridad | Ciberseguridad, pentesting |
| **MOV** | Desarrollo Móvil | iOS, Android, híbrido |
| **ALG** | Algoritmos | Estructuras de datos |

### Especialidades Top 15

| Código | Nombre | Subcategoría |
|--------|--------|--------------|
| **FST** | Full-Stack | PRG |
| **PYT** | Python | PRG |
| **REA** | React | PRG |
| **TSC** | TypeScript | PRG |
| **NOD** | Node.js | PRG |
| **MLF** | Machine Learning | IAR |
| **DLE** | Deep Learning | IAR |
| **DOC** | Docker | DVC |
| **KUB** | Kubernetes | DVC |
| **AWS** | Amazon Web Services | DVC |
| **MIC** | Microservicios | ARQ |
| **CLE** | Clean Architecture | ARQ |
| **DDD** | Domain-Driven Design | ARQ |
| **JAV** | JavaScript | PRG |
| **DJA** | Django | PRG |

---

## [DEBUG] Casos Especiales

### Libro Multidominio

```
Ejemplo: "AI for Web Development"

Análisis:
- ¿60% IA, 40% Web? -> INF.IAR
- ¿40% IA, 60% Web? -> INF.WEB
- ¿50/50? -> Elegir tema PRIMARIO del título
```

### Serie de Libros

```
"Python Vol 1" y "Python Vol 2"

Clasificación:
- Python_Vol1 -> INF.PRG.PYT.001
- Python_Vol2 -> INF.PRG.PYT.002
(Cada volumen = Libro independiente)
```

### Reediciones

```
"Docker 1st Ed" y "Docker 2nd Ed"

Clasificación:
- Docker_1ed -> INF.DVC.DOC.001
- Docker_2ed -> INF.DVC.DOC.002
(Cada edición = Libro NUEVO)
```

---

## [TOOLS] Herramientas

### Script de Clasificación

```python
def clasificar_libro(titulo, autor, toc):
 categoria = inferir_categoria(titulo)
 subcategoria = inferir_subcategoria(titulo, toc)
 especialidad = inferir_especialidad(titulo, toc)
 numero = obtener_siguiente_numero(categoria, subcategoria, especialidad)
 codigo = f"{categoria}.{subcategoria}.{especialidad}.{numero:03d}"
 return codigo
```

### Validación

```python
def validar_codigo(codigo):
 # Formato: XXX.XXX.XXX.NNN
 partes = codigo.split('.')
 if len(partes) != 4:
 return False
 if not all(len(p) == 3 for p in partes[:3]):
 return False
 if not partes[3].isdigit() or len(partes[3]) != 3:
 return False
 return True
```

---

## [TABLE] Estadísticas Recomendadas

Mantener en `estadisticas_biblioteca.rst`:

- Total de libros
- Distribución por categoría
- Top 5 subcategorías
- Top 5 especialidades
- Progreso de traducción
- Páginas traducidas
- Términos en glosarios

---

## [LINK] Archivos Relacionados

- **Guía completa:** `GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst` (80+ páginas)
- **Arquitectura:** `ARQUITECTURA_TRADUCCION_IACT.rst`
- **Síntesis metodológica:** `SINTESIS_METODOLOGICA_ADT.rst`
- **Plan de contenido:** `PLAN_CONTENIDO.rst`

---

## [OK] Para Empezar

1. Lee este resumen ejecutivo
2. Consulta la guía completa para detalles
3. Usa el checklist de clasificación
4. Mantén actualizado el catálogo
5. Documenta nuevas especialidades

---

**Versión:** 1.0.0
**Última actualización:** 2026-01-28
**Estado:** NORMATIVO

---

**FIN DEL RESUMEN EJECUTIVO**

 Para información detallada, casos de uso complejos, plantillas y procedimientos completos, consulta el documento completo: `GUIA_METODOLOGICA_CLASIFICACION_DOCUMENTAL.rst`
