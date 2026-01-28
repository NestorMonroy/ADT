.. _glossary_tip_1:

===============================================================
Tip 12-1: ¡Tómate el glosario en serio!
===============================================================

:Tema: Importancia del glosario
:Palabras clave: glossary, essential

----

Debes asegurar que todas las personas participantes tengan un entendimiento *común* de la terminología importante de **negocio** (y técnica) que usan en el contexto del sistema.

El **glosario** es una manifestación de la regla general de *"mejor explícito que implícito"*.

Importancia del Glosario
=========================

**Por qué es Crítico:**

.. list-table::
   :header-rows: 1
   :widths: 40 60
   
   * - **Sin Glosario**
     - **Con Glosario**
   * - ❌ Desarrolladores y negocio usan términos diferentes
     - ✅ Todos hablan el mismo idioma
   * - ❌ "Cliente" significa cosas diferentes para cada equipo
     - ✅ "Cliente" tiene definición única acordada
   * - ❌ Pérdida de tiempo aclarando términos
     - ✅ Comunicación eficiente
   * - ❌ Bugs por malentendidos
     - ✅ Implementación correcta desde inicio
   * - ❌ Onboarding lento para nuevos
     - ✅ Nuevos aprenden terminología rápidamente

**Regla: "Mejor Explícito que Implícito"**

.. code-block:: text

   ❌ Implícito (riesgoso):
   "El usuario puede cancelar la orden"
   
   Pregunta: ¿Qué es "usuario"?
   - ¿Cliente final?
   - ¿Administrador?
   - ¿Soporte técnico?
   - ¿Todos los anteriores?
   
   ✅ Explícito (claro):
   "El cliente final puede cancelar su orden dentro de 24 horas"
   
   Glosario define:
   - Cliente final: Usuario registrado que realiza compras
   - Administrador: Empleado con acceso al panel admin
   - Soporte: Empleado que asiste a clientes

----

**Ejemplos de Problemas por Falta de Glosario:**

**Caso 1: Término Ambiguo**

.. code-block:: text

   Término sin definir: "Sesión"
   
   Equipo Backend piensa:
   → JWT token válido por 1 hora
   
   Equipo Frontend piensa:
   → Pestaña del navegador abierta
   
   Equipo QA piensa:
   → Desde login hasta logout
   
   Resultado: Bug en producción
   → Frontend mantiene pestaña abierta 3 horas
   → Backend expira token después de 1 hora
   → Usuario pierde trabajo no guardado

**Caso 2: Sinónimos No Identificados**

.. code-block:: text

   Negocio dice: "Pedido"
   Desarrollo dice: "Orden"
   Documentación dice: "Solicitud"
   
   Todos hablan de lo mismo, pero usan términos diferentes.
   
   Solución en Glosario:
   - Pedido (término oficial)
     Sinónimos: Orden, Solicitud
     Definición: Conjunto de productos que un cliente...

**Caso 3: Homónimos**

.. code-block:: text

   Término: "Cliente"
   
   En contexto de ventas:
   → Empresa que compra nuestro producto
   
   En contexto técnico:
   → Software que consume nuestra API (API client)
   
   Solución:
   - Cliente (negocio): Empresa u organización compradora
   - API Client: Aplicación que consume endpoints

----

**Cómo Tomarse el Glosario en Serio:**

1. **Iniciar temprano**
   
   * ✅ Crear glosario en fase de inception/discovery
   * ✅ Agregar términos en cada reunión de requisitos
   * ❌ NO esperar a documentación final

2. **Mantener actualizado**
   
   * ✅ Revisar en cada sprint planning
   * ✅ Actualizar cuando aparezcan nuevos términos
   * ✅ Eliminar términos obsoletos

3. **Hacer accesible**
   
   * ✅ Wiki interna fácilmente buscable
   * ✅ Incluir en onboarding de nuevos
   * ✅ Referenciar desde documentación técnica

4. **Validar con stakeholders**
   
   * ✅ Revisar definiciones con expertos de dominio
   * ✅ Obtener aprobación de negocio
   * ✅ Consenso entre equipos técnicos

----

**Métricas de Éxito:**

.. list-table::
   :header-rows: 1
   :widths: 40 30 30
   
   * - **Indicador**
     - **Objetivo**
     - **Métrica**
   * - Términos definidos
     - 100% términos importantes
     - 30-50 términos en glosario
   * - Tiempo de onboarding
     - Reducción 30%
     - Nuevos entienden dominio en 2 días
   * - Bugs por malentendidos
     - Reducción 50%
     - Trackear causa raíz
   * - Reuniones de aclaración
     - Reducción 40%
     - Menos "¿qué significa X?"

----

.. seealso::
   * **Tip 12-2** - Documentar glosario como tabla
   * **Tip 12-3** - Agregar modelo gráfico
   * **Sección 8** - Conceptos Transversales (Ubiquitous Language)
