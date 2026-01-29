.. _risks_tip_6:

===============================================================
Tip 11-6: ¡Analiza el código fuente para problemas y riesgos!
===============================================================

:Tema: Riesgos en código fuente
:Palabras clave: risk, problem, source-code

----

Deberías aplicar **análisis de código fuente** para identificar **riesgos** y problemas:

Tanto el análisis **estático** (lines-of-code, coupling, cyclomatic complexity, etc.) como el análisis **dinámico** (es decir, cobertura de tests, análisis de performance/threads) pueden ayudar a identificar **riesgos** o problemas.

Análisis Estático de Código
============================

**Métricas de Código**

.. list-table::
 :header-rows: 1
 :widths: 30 35 35

 * - **Métrica**
   - **Qué Indica**
   - **Umbral de Riesgo**
 * - **Lines of Code (LOC)**
   - Tamaño del codebase
   - >100k LOC sin modularización
 * - **Cyclomatic Complexity**
   - Complejidad de funciones
   - >10 por función
 * - **Coupling**
   - Dependencias entre módulos
   - >5 dependencias directas
 * - **Cohesion**
   - Relacionamiento interno
   - Cohesión baja (<0.5)
 * - **Code Duplication**
   - Código duplicado
   - >5% duplicación
 * - **Comment Density**
   - Ratio comentarios/código
   - <10% o >30%

**1. Complejidad Ciclomática Alta**

.. code-block:: python

 # [ERROR] RIESGO: Cyclomatic Complexity = 15
 def process_order(order):
 if order.type == 'express':
 if order.payment == 'card':
 if order.amount > 100:
 if order.country == 'US':
 # ... 20 more nested ifs

 # [OK] MEJOR: Complexity = 2 (Strategy pattern)
 processor = OrderProcessorFactory.get(order)
 processor.process()

**2. Acoplamiento Alto**

* [WARNING] **Módulo depende de 10+ otros módulos**

 *Riesgo: Cambios en un módulo afectan muchos otros*

 **Solución:** Dependency Injection, Interfaces

**3. Duplicación de Código**

* [WARNING] **Mismo código copy-pasted en múltiples lugares**

 *Riesgo: Fix bug en un lugar, persiste en otros*

 **Solución:** DRY principle, extract method/class

----

Herramientas de Análisis Estático
==================================

**Por Lenguaje:**

.. list-table::
 :header-rows: 1
 :widths: 20 40 40

 * - **Lenguaje**
   - **Herramientas**
   - **Qué Detectan**
 * - **Java**
   - SonarQube, PMD, Checkstyle
   - Bugs, code smells, security
 * - **Python**
   - Pylint, Flake8, Bandit
   - Style, complexity, security
 * - **JavaScript**
   - ESLint, SonarJS
   - Errors, code quality
 * - **C#**
   - ReSharper, FxCop
   - Code quality, performance
 * - **Go**
   - golangci-lint, staticcheck
   - Bugs, performance
 * - **Multi-language**
   - SonarQube, CodeClimate
   - Security, maintainability

**Categorías de Issues:**

* [DEBUG] **Bugs**: Errores potenciales
* **Vulnerabilities**: Problemas de seguridad
* [INFO] **Code Smells**: Problemas de mantenibilidad
* **Coverage**: Gaps en testing

----

Análisis Dinámico de Código
============================

**1. Cobertura de Tests**

.. code-block:: text

 Test Coverage Report:

 +- controllers/ 85% [OK]
 +- services/ 72% [WARNING]
 +- models/ 95% [OK]
 +- utils/ 45% RIESGO
 +- legacy/ 0% DEUDA TÉCNICA

**Riesgos:**
- Código sin tests -> bugs no detectados
- Coverage <70% -> confianza baja en refactoring

**2. Análisis de Performance**

**Profiling Tools:**

* **Python**: cProfile, py-spy
* **Java**: JProfiler, VisualVM
* **JavaScript**: Chrome DevTools
* **.NET**: dotTrace

**Qué Buscar:**

.. list-table::
 :header-rows: 1
 :widths: 40 60

 * - **Problema**
   - **Ejemplo**
 * - **Hotspots**
   - Función consume 80% del tiempo total
 * - **Memory Leaks**
   - Memoria crece indefinidamente
 * - **N+1 Queries**
   - 1000 queries DB en un request
 * - **Blocking I/O**
   - Thread bloqueado esperando I/O

**3. Análisis de Threads/Concurrencia**

* **Race Conditions**

 *Riesgo: Resultados no determinísticos*

* **Deadlocks**

 *Riesgo: Sistema se congela*

* **Thread Starvation**

 *Riesgo: Requests nunca procesados*

**Herramientas:**

* Java: Thread Dump Analyzer
* .NET: Concurrency Visualizer
* Python: threading profiler

----

Código Legacy como Riesgo
==========================

**Características de Código Legacy:**

.. code-block:: text

 [ERROR] Sin tests automatizados
 [ERROR] Tecnología obsoleta (PHP 5.3, Python 2.7)
 [ERROR] Sin documentación
 [ERROR] Un solo desarrollador conoce el código
 [ERROR] "Nadie se atreve a tocarlo"
 [ERROR] Dependencias sin actualizar hace años

**Estrategias de Mitigación:**

1. **Characterization Tests**

 * Escribir tests que describen comportamiento actual
 * No para validar corrección, sino para detectar cambios

2. **Strangler Fig Pattern**

 * Reemplazar gradualmente funcionalidad vieja con nueva
 * No reescritura big-bang

3. **Refactoring Incremental**

 * Regla del Boy Scout: deja código mejor de como lo encontraste
 * Pequeños refactorings en cada commit

4. **Dependency Updates**

 * Automatizar con Dependabot, Renovate
 * Actualizar regularmente, no esperar años

----

**Ejemplo de Análisis de Código:**

.. code-block:: text

 Módulo: PaymentProcessor.java

 Análisis Estático:
 +- LOC: 2,500 ([WARNING] considerar split)
 +- Cyclomatic Complexity: Avg 8, Max 45 ( CRÍTICO)
 +- Coupling: Depende de 15 módulos ([WARNING] ALTO)
 +- Code Duplication: 12% ([WARNING] ALTO)
 +- Security Issues: 3 SQL injection risks ( CRÍTICO)

 Análisis Dinámico:
 +- Test Coverage: 35% ( BAJO)
 +- Performance: 200ms avg ([OK] OK)
 +- Memory: No leaks detected ([OK] OK)
 +- Concurrency: 2 potential race conditions ( RIESGO)

 Deuda Técnica Identificada:
 1. Función processPayment() tiene complexity 45
 -> Refactor usando Command pattern (5 días)

 2. 12% código duplicado
 -> Extract common logic (2 días)

 3. Coverage 35%
 -> Agregar tests (3 días)

 4. 3 SQL injection risks
 -> Usar prepared statements (1 día) [URGENTE]

 Prioridad: 4 (urgente) > 1 > 3 > 2

----

**Pipeline de Code Quality:**

.. code-block:: text

 Commit -> Pre-commit Hooks (linting) ->
 CI Build ->
 +- Unit Tests (coverage check)
 +- Static Analysis (SonarQube)
 +- Security Scan (Snyk/OWASP)
 +- Dependency Check
 +- Code Review

 [ERROR] Fail if:
 - Coverage < 70%
 - Complexity > 10
 - Security vulnerabilities
 - Code duplica > 5%

----

**Métricas de Calidad de Código:**

.. list-table::
 :header-rows: 1
 :widths: 30 25 20 25

 * - **Métrica**
   - **Target**
   - **Warning**
   - **Critical**
 * - Test Coverage
   - >80%
   - 70-80%
   - <70%
 * - Cyclomatic Complexity
   - <5
   - 5-10
   - >10
 * - Code Duplication
   - <3%
   - 3-5%
   - >5%
 * - Security Issues
   - 0
   - Low severity
   - Medium/High
 * - Tech Debt Ratio
   - <5%
   - 5-10%
   - >10%

----

.. seealso::
 * **Tip 11-4** - Analizar procesos para riesgos
 * **Tip 11-5** - Analizar datos para riesgos
 * **Sección 5** - Building Block View
 * **Sección 8** - Conceptos Transversales
