.. _risks_ejemplo_tpu:

===============================================================
Ejemplo de Riesgos: TrafficPursuitUnit
===============================================================

:Sistema: TrafficPursuitUnit (TPU)
:Categoría: Sistema embebido automotriz
:Palabras clave: risks, example

----

Este ejemplo muestra **riesgos** para TrafficPursuitUnit (TPU), un sistema embebido de persecución de tráfico policial, con énfasis en **riesgos de hardware** en entornos automotrices.

----

11. Riesgos y Deuda Técnica
============================

Riesgos de Hardware
===================

Dado que no teníamos ninguna experiencia extendida con la mayoría de los componentes de **hardware** usados en nuestro sistema, quedaban algunas incertidumbres respecto al comportamiento de estos componentes en el entorno automotriz, especialmente con respecto al:

* **Rango de temperatura**
* **Torsión**
* **Vibraciones**

Dependencia de Proveedores
---------------------------

.. warning::
   **Riesgo Crítico: Incapacidad de Diagnóstico Autónomo**
   
   En contraste con los componentes de **hardware** desarrollados por nuestra compañía, en el caso de componentes complejos suministrados a nosotros (por ejemplo, placa CPU), no seríamos capaces de determinar las causas de problemas por nuestra cuenta y tomar acción remedial.
   
   En su lugar, dependemos de cooperación confiable con los **proveedores** o fabricantes de los componentes.

**Consecuencias:**

.. code-block:: text

   Por esta razón, no pudimos ofrecer una garantía comprehensiva,
   ya que el riesgo involucrado no podía ser calculado.

**Análisis del Riesgo:**

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   
   * - **Aspecto**
     - **Riesgo**
     - **Impacto en Negocio**
   * - **Diagnóstico**
     - No podemos debuggear hardware de terceros
     - Tiempo de resolución impredecible
   * - **Soporte**
     - Dependencia del proveedor
     - SLAs no garantizables
   * - **Warranty**
     - No podemos ofrecer garantía completa
     - Pérdida de competitividad

----

Robustez de Discos Duros Bajo Condiciones Severas
==================================================

**Contexto Tecnológico:**

En el momento del desarrollo del sistema, los **discos de estado sólido** (SSDs) no estaban disponibles en los tamaños necesarios para grabar grandes cantidades de video HD (aproximadamente 1TB) y también eran bastante costosos.

El sistema tenía que basarse en **discos duros** (HDDs).

Discos Duros Reforzados
------------------------

Ciertamente, existían **discos duros especiales reforzados** adecuados para condiciones automotrices, pero no pudimos probarlos por adelantado durante varios miles de kilómetros bajo las condiciones de manejo ásperas que pueden ocurrir en un coche de policía.

**Escenario de Estrés Extremo:**

.. code-block:: text

   Grabación de video durante persecución:
   
   ├─ Maniobras bruscas de aceleración
   ├─ Frenado intenso
   ├─ Torsión extrema del disco
   └─ Mientras escribe videoclips a tasas de datos muy altas
   
   RESULTADO: Los discos duros podrían sufrir tensión y torsión
              extremas bajo estas condiciones.

**Análisis Detallado del Riesgo:**

.. list-table:: Riesgo de Fallo de Disco Duro
   :header-rows: 1
   :widths: 25 35 40
   
   * - **Factor de Estrés**
     - **Consecuencia Potencial**
     - **Mitigación Posible**
   * - **Vibraciones intensas**
     - Errores de lectura/escritura
     - Montaje anti-vibración
   * - **Aceleración brusca**
     - Head crash (daño físico)
     - HDDs diseñados para entorno móvil
   * - **Temperatura extrema**
     - Fallo térmico
     - Sistema de cooling activo
   * - **Escritura alta velocidad**
     - Fragmentación, wear
     - RAID 1 para redundancia
   * - **Torsión del chasis**
     - Desalineación mecánica
     - Carcasa rígida independiente

**Limitaciones del Testing:**

.. warning::
   **Gap de Validación**
   
   * ❌ No pudimos probar durante miles de kilómetros
   * ❌ No pudimos simular todas las condiciones reales
   * ❌ Condiciones de persecución son impredecibles
   
   **RIESGO:** Fallos en campo que no se manifestaron en testing

----

Riesgos de Software
===================

La complejidad del **software de terceros** usado, tal como:

* El **sistema operativo Linux**
* Los **drivers de hardware** suministrados

Algunos de los cuales solo están disponibles en **código binario**, imponen un **riesgo**:

.. code-block:: text

   RIESGO: Mal funcionamientos en estas partes podrían involucrar
           mucho esfuerzo en determinar la causa y crear una
           dependencia de asistencia de proveedores externos.

**Desglose de Riesgos de Software:**

**1. Sistema Operativo Linux**

.. list-table::
   :widths: 40 60
   
   * - **Ventajas**
     - ✅ Open source, well-tested
   * - **Riesgos**
     - ⚠️ Kernel bugs pueden afectar estabilidad
   * - 
     - ⚠️ Driver compatibility issues
   * - 
     - ⚠️ Security patches requieren actualización cuidadosa

**2. Drivers de Hardware en Binario**

.. list-table::
   :widths: 40 60
   
   * - **Problema**
     - Sin acceso a código fuente
   * - **Consecuencia**
     - Debugging imposible internamente
   * - **Dependencia**
     - Totalmente dependiente del proveedor
   * - **Riesgo**
     - Proveedor descontinúa soporte → sistema obsoleto

**3. Esfuerzo de Diagnóstico**

.. code-block:: text

   Escenario de Fallo:
   
   Síntoma observado:
   ├─ Video se corrompe intermitentemente
   │
   ¿Es problema de...?
   ├─ ¿Driver de cámara? (binario → no podemos debuggear)
   ├─ ¿Kernel Linux?    (complejo → requiere expertos)
   ├─ ¿Disco duro?      (físico → RMA, reemplazo)
   ├─ ¿Nuestro código?  (podemos debuggear)
   └─ ¿Interacción?     (peor caso → muy difícil)
   
   Tiempo de diagnóstico: IMPREDECIBLE (días a semanas)

----

**Matriz de Riesgos Consolidada:**

.. list-table::
   :header-rows: 1
   :widths: 15 30 20 15 20
   
   * - **ID**
     - **Riesgo**
     - **Categoría**
     - **Severidad**
     - **Mitigación**
   * - HW-001
     - Fallo HDD bajo vibración
     - Hardware
     - 🔴 Alta
     - Montaje anti-vibración + RAID
   * - HW-002
     - Componentes fuera de rango térmico
     - Hardware
     - 🔴 Alta
     - Cooling activo + testing climático
   * - HW-003
     - Dependencia de proveedores
     - Organizacional
     - 🟡 Media
     - Múltiples proveedores si posible
   * - SW-001
     - Drivers binarios no debuggeables
     - Software
     - 🔴 Alta
     - SLA con proveedor + drivers backup
   * - SW-002
     - Complejidad Linux kernel
     - Software
     - 🟡 Media
     - Expertise interno + comunidad
   * - BIZ-001
     - No podemos ofrecer warranty
     - Negocio
     - 🔴 Alta
     - Warranty limitada + disclaimer

----

**Estrategias de Mitigación Implementadas:**

1. **Hardware**
   
   * ✅ Usar componentes "automotive-grade" certificados
   * ✅ Testing en cámara climática (-25°C a +85°C)
   * ✅ RAID 1 para redundancia de disco
   * ⚠️ Mounting anti-vibración (parcial)

2. **Software**
   
   * ✅ Establecer SLAs con proveedores de drivers
   * ✅ Mantener versiones de kernel LTS (Long Term Support)
   * ⚠️ Expertise interno limitado en kernel
   * ⚠️ Dependencia de drivers binarios (sin alternativa)

3. **Negocio**
   
   * ✅ Warranty disclaimer en contrato
   * ✅ Expectativas claras con cliente
   * ⚠️ Puede afectar competitividad

----

**Lecciones Aprendidas:**

.. list-table::
   :header-rows: 1
   :widths: 40 60
   
   * - **Lección**
     - **Aplicación**
   * - **Dependencia de hardware de terceros**
     - Evaluar criticality vs in-house development
   * - **Testing en condiciones reales**
     - Invertir en field testing extensivo
   * - **Drivers binarios**
     - Priorizar proveedores con código abierto
   * - **Entorno automotriz**
     - Requiere certificaciones específicas
   * - **Warranty limitations**
     - Transparencia temprana con cliente

**Aplicabilidad:**

Este ejemplo es particularmente valioso para:

* 🚗 Sistemas **embebidos** automotrices
* 🏭 **IoT** en entornos industriales
* 🛡️ Sistemas **críticos** con requisitos de robustez
* 🔧 Proyectos con dependencia de **hardware de terceros**

----

.. seealso::
   * **Ejemplo HTMLSC** - Riesgos en proyecto open source
   * **Tip 11-4** - Analizar procesos para riesgos
   * **Tip 11-5** - Analizar datos para riesgos
   * **Sección 10.2** - Escenarios de Calidad (robustez)
