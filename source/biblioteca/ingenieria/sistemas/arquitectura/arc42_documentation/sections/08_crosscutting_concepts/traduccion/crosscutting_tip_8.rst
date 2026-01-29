===============================================
Tip 8-8: ¡Documente conceptos con código fuente!
===============================================

.. meta::
   :layout: post
   :title: Tip 8-8: ¡Documente conceptos con código fuente!
   :tags: concepto
   :category: conceptos
   :permalink: /tips/8-8/

El código fuente puede ser una excelente documentación de conceptos, especialmente
para aspectos técnicos.

En lugar de escribir explicaciones largas, considere:

* **Mostrar código de ejemplo:**
  Fragmentos de código que demuestren el patrón o concepto
  
* **Referenciar implementaciones existentes:**
  Enlaces a clases o módulos que ya implementan el concepto
  
* **Usar pruebas unitarias:**
  Los tests pueden documentar cómo se debe usar un concepto

.. code-block:: python

   # Ejemplo: Concepto de Factory Pattern
   class UserFactory:
       """Fábrica para crear diferentes tipos de usuarios"""
       
       @staticmethod
       def create_user(user_type, data):
           if user_type == "admin":
               return AdminUser(data)

           elif user_type == "regular":
               return RegularUser(data)

           else:
               raise ValueError(f"Tipo de usuario desconocido: {user_type}")

.. important::
   El código debe estar bien comentado y ser autoexplicativo.
   
   La documentación en forma de código es más probable que se mantenga actualizada
   que los documentos separados.
