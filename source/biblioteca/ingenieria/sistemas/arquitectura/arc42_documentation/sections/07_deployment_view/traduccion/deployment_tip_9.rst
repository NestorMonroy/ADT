.. _deployment_tip_9:

===============================================================
Tip 7-9: ¡Explica qué (más) es relevante para el uso productivo (aka operación) del sistema!
===============================================================

.. tip::
   **Consejo de Vista de Despliegue arc42**
   
   Aparte de compilar, integrar y probar (aka *construir*) un sistema, tareas adicionales necesitan completarse para poner cualquier sistema suficientemente complicado *en funcionamiento* en una plataforma objetivo.

----

Desafíos para Poner un Sistema en Producción
=============================================

Aparte de compilar, integrar y probar (aka *construir*) un sistema, tareas adicionales necesitan completarse para poner cualquier sistema suficientemente complicado *en funcionamiento* en una plataforma objetivo:

No queremos asustarte - pero queremos mostrar algunos ejemplos de actividades que (probablemente) necesitas considerar:

* Asegurar que el sistema operativo correcto (versión + parches) esté instalado
* Crear las cuentas (de usuario) requeridas, junto con derechos de acceso apropiados
* Crear directorios en el sistema operativo objetivo, junto con derechos de acceso apropiados
* Crear y configurar bases de datos, incluyendo cuentas DB requeridas más derechos de acceso
* Migración de datos de aplicación ya existentes
* Instalar y configurar middleware requerido, **servidores** de aplicación o frameworks. Eso puede incluir:

  * **Servidor** web
  * **Servidor** proxy
  * Balanceador de carga, **servidor** de alta disponibilidad
  * **Servidor** de directorio (es decir, LDAP)
  * Bus de mensajes
  * etc.

* Configuración y setup de drivers de **red**, routers, direcciones IP, hostnames, nameserver, túneles VPN
* Setup de firewalls a nivel de **red** o aplicación incluyendo reglas de firewall requeridas
* Setup y configuración de medidas de seguridad requeridas (es decir, certificados u otras claves criptográficas, encriptación de disco o base de datos)

Automatizar (Casi) Todo
=======================

Nunca quieres realizar *manualmente* todas estas tareas (y esperar realizarlas sin errores). En caso de que lo hagas - habrá errores, omisiones y pequeñas desviaciones del setup requerido - apostamos a eso.

Deberías en su lugar documentar *exhaustivamente* tu setup - de preferencia por medio de scripts de automatización.

Si tú y tu equipo todavía no son parte de ninguna experiencia *devops*, echa un vistazo a las siguientes pistas:

* `Puppet <https://puppet.com/>`_
* `Chef <https://www.chef.io/>`_
* `Ansible <https://www.ansible.com/>`_
* `Salt <https://saltstack.com/>`_
* `Rudder <https://www.normation.com/en/>`_

----

.. seealso::
   * :ref:`seccion_07` - Vista de Despliegue
   * :ref:`deployment_tip_1` - Documentar infraestructura técnica
   * :ref:`deployment_tip_3` - Documentar varios entornos

----

:Tip: 7-9
:Tema: Operación productiva del sistema
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.7.1