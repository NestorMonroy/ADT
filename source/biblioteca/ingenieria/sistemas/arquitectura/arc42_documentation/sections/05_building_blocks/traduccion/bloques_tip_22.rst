.. _bloques_tip_22:

===============================================================
Tip 5-22: ¡Documenta o especifica interfaces con pruebas unitarias!
===============================================================

.. tip::
   **Consejo de Vista de Bloques arc42**
   
   Implementar pruebas unitarias se ha vuelto (bastante) estándar para muchos desarrolladores. Nos gusta proponer un propósito adicional para tales pruebas: especificación o documentación de **interfaces**.

----

Implementar pruebas unitarias se ha vuelto (bastante) estándar para muchos desarrolladores. Nos gusta proponer un propósito adicional para tales pruebas: especificación o documentación de **interfaces**.

Toma las pruebas como documentación detallada (¡y altamente ágil!), y solo alternativamente como pruebas reales (para verificar el comportamiento de la aplicación).

Una prueba unitaria contiene la siguiente información:

* Prerrequisitos que tienen que ser (programáticamente) creados para usar la **interfaz** específica
* Mostrando en qué constelación o contexto la **interfaz** puede ser usada
* Qué tipo de consecuencias pueden esperarse después de que la implementación de la **interfaz** haya sido usada (por la declaración ``assert``)

En lugar de cualquier especificación o descripción gráfica o textual, puedes escribir pruebas unitarias y usar uno o varios métodos de prueba como documentación (o especificación).

En caso de que integres estas pruebas de tu repositorio de código en tu documentación, obtendrás actualización de la documentación gratis.

Ejemplo de Prueba Unitaria como Documentación de Interfaz
==========================================================

.. code-block:: java

   package joptsimple.examples;
   import joptsimple.OptionParser;
   import joptsimple.OptionSet;
   import org.junit.Test;
   import static org.junit.Assert.*;
   
   public class ShortOptionsTest {
       @Test
       public void supportsShortOptions() {
         OptionParser parser = new OptionParser( "aB?*." );
         OptionSet options = parser.parse( "-a", "-B", "-?" );
         assertTrue( options.has( "a" ) );
         assertTrue( options.has( "B" ) );
         assertTrue( options.has( "?" ) );
         assertFalse( options.has( "." ) );

      }

   }

Este ejemplo muestra cómo la prueba documenta el uso de la **interfaz** OptionParser de manera ejecutable y verificable.

Aplica Desarrollo Dirigido por Comportamiento (BDD)
====================================================

Podrías desarrollar tu sistema o partes de él de manera *dirigida por comportamiento* (BDD). Entonces la especificación del sistema funciona tanto como documentación como prueba automatizada.

Un posible framework que soporta BDD es `Cucumber <https://cucumber.io/>`_, otro es `Spockframework <https://spockframework.org/>`_.

Ventajas de Este Enfoque
=========================

* **Siempre actualizado:** Las pruebas se ejecutan regularmente y fallan si cambia la **interfaz**
* **Ejecutable:** La documentación es verificable automáticamente
* **Concreta:** Muestra ejemplos reales de uso
* **Ágil:** Se mantiene junto con el código

----

.. seealso::
   * :ref:`seccion_05` - Vista de Bloques de Construcción
   * :ref:`bloques_tip_21` - Interfaces con esfuerzo mínimo

----

:Tip: 5-22
:Tema: Interfaces documentadas con unit tests
:Traducción: Método Peshitta + Paso 3.4
:Workflow: v1.6.0
