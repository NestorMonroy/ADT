.. _comandos_utiles:




Comandos Útiles
===============

Comandos de terminal más usados en proyectos ADT.

.. contents:: Contenido
   :depth: 2
   :local:




Sphinx
======

Compilación
===========

.. code-block:: bash

   # Compilar a HTML
   make html
   
   # Compilar a PDF
   make latexpdf
   
   # Limpiar build anterior
   make clean
   
   # Limpiar y recompilar
   make clean && make html

Verificación
============

.. code-block:: bash

   # Ver warnings y errores
   make html 2>&1 | grep WARNING
   
   # Ver solo errores
   make html 2>&1 | grep ERROR
   
   # Verificar links rotos
   make linkcheck
   
   # Ver estadísticas de build
   make html | tail -20

Live Reload
===========

.. code-block:: bash

   # Instalar sphinx-autobuild
   pip install sphinx-autobuild
   
   # Servidor con auto-reload
   sphinx-autobuild source build/html
   
   # Abrir en navegador
   # http://127.0.0.1:8000




Git
===

Workflow Básico
===============

.. code-block:: bash

   # Estado del repositorio
   git status
   
   # Ver cambios
   git diff
   
   # Agregar archivos
   git add source/archivo.rst
   
   # Commit
   git commit -m "Traducir sección X"
   
   # Push
   git push origin main

Branches
========

.. code-block:: bash

   # Crear branch
   git checkout -b traduccion-seccion-05
   
   # Cambiar de branch
   git checkout main
   
   # Mergear branch
   git merge traduccion-seccion-05
   
   # Eliminar branch
   git branch -d traduccion-seccion-05

Historial
=========

.. code-block:: bash

   # Ver log
   git log --oneline
   
   # Ver cambios de commit
   git show <commit-hash>
   
   # Ver quién cambió qué
   git blame archivo.rst




Búsqueda y Análisis
===================

Buscar en Archivos
==================

.. code-block:: bash

   # Buscar término en todos los RST
   grep -r "término" source/*.rst
   
   # Buscar con contexto
   grep -C 3 "término" archivo.rst
   
   # Buscar y contar
   grep -c "término" source/*.rst
   
   # Buscar ignorando mayúsculas
   grep -i "término" source/*.rst

Contar Elementos
================

.. code-block:: bash

   # Contar archivos RST
   find source -name "*.rst" | wc -l
   
   # Contar líneas en archivo
   wc -l archivo.rst
   
   # Contar palabras
   wc -w archivo.rst
   
   # Contar ocurrencias de término
   grep -o "término" archivo.rst | wc -l

Estadísticas
============

.. code-block:: bash

   # Tamaño de directorios
   du -sh source/*
   
   # Listar archivos por tamaño
   du -h source/*.rst | sort -h
   
   # Archivos más grandes
   find source -name "*.rst" -exec du -h {} \; | sort -rh | head -10




Edición en Masa
===============

Reemplazar Texto
================

.. code-block:: bash

   # Reemplazar en un archivo
   sed -i 's/viejo/nuevo/g' archivo.rst
   
   # Reemplazar en múltiples archivos
   find source -name "*.rst" -exec sed -i 's/viejo/nuevo/g' {} \;
   
   # Vista previa antes de reemplazar
   sed 's/viejo/nuevo/g' archivo.rst

Renombrar Archivos
==================

.. code-block:: bash

   # Renombrar con patrón
   rename 's/old/new/' *.rst
   
   # Cambiar extensión
   rename 's/\.txt$/.rst/' *.txt

Convertir Line Endings
======================

.. code-block:: bash

   # Windows (CRLF) a Unix (LF)
   dos2unix archivo.rst
   
   # Unix (LF) a Windows (CRLF)
   unix2dos archivo.rst




Pandoc
======

Conversiones Básicas
====================

.. code-block:: bash

   # LaTeX a RST
   pandoc input.tex -f latex -t rst -o output.rst
   
   # Markdown a RST
   pandoc input.md -f markdown -t rst -o output.rst
   
   # HTML a RST
   pandoc input.html -f html -t rst -o output.rst

Opciones Avanzadas
==================

.. code-block:: bash

   # Sin wrapping de líneas
   pandoc input.tex -f latex -t rst --wrap=none -o output.rst
   
   # Documento standalone
   pandoc input.tex -f latex -t rst --standalone -o output.rst
   
   # Con tabla de contenidos
   pandoc input.md --toc -o output.html




Validación y QA
===============

Validar RST
===========

.. code-block:: bash

   # Validar sintaxis RST
   rst2html archivo.rst > /dev/null
   
   # Validar todos los archivos
   find source -name "*.rst" -exec rst2html {} \; > /dev/null 2>&1

Spell Check
===========

.. code-block:: bash

   # Instalar aspell
   sudo apt-get install aspell aspell-es
   
   # Verificar ortografía
   aspell check archivo.rst
   
   # Listar palabras mal escritas
   aspell list < archivo.rst

Detectar Problemas Comunes
==========================

.. code-block:: bash

   # Encontrar títulos sin subrayado
   grep -A 1 "^[A-Z]" archivo.rst | grep -v "^[-=~]"
   
   # Encontrar líneas muy largas (>120 caracteres)
   grep -n ".\{120,\}" archivo.rst
   
   # Encontrar espacios al final de línea
   grep -n " $" archivo.rst




Python y pip
============

Gestión de Entornos
===================

.. code-block:: bash

   # Crear entorno virtual
   python -m venv venv
   
   # Activar entorno (Linux/Mac)
   source venv/bin/activate
   
   # Activar entorno (Windows)
   venv\Scripts\activate
   
   # Desactivar
   deactivate

Instalación de Paquetes
=======================

.. code-block:: bash

   # Instalar Sphinx
   pip install sphinx
   
   # Instalar múltiples paquetes
   pip install sphinx sphinx-rtd-theme myst-parser
   
   # Desde requirements.txt
   pip install -r requirements.txt
   
   # Actualizar paquete
   pip install --upgrade sphinx

Gestión de Dependencias
=======================

.. code-block:: bash

   # Listar paquetes instalados
   pip list
   
   # Guardar dependencias
   pip freeze > requirements.txt
   
   # Ver información de paquete
   pip show sphinx




Productividad
=============

Alias Útiles
============

.. code-block:: bash

   # Agregar a ~/.bashrc o ~/.zshrc
   
   # Compilación rápida
   alias build='make html'
   alias clean='make clean && make html'
   
   # Servidor local
   alias serve='python -m http.server -d build/html 8000'
   
   # Git rápido
   alias gs='git status'
   alias ga='git add'
   alias gc='git commit -m'
   alias gp='git push'

Scripts Útiles
==============

**Contador de líneas por archivo:**

.. code-block:: bash

   #!/bin/bash
   for file in source/*.rst; do
       echo "$(wc -l < $file) $file"

   done | sort -rn

**Compilador con notificación:**

.. code-block:: bash

   #!/bin/bash
   make html && \
   echo "Build exitoso!" || \
   echo "Build falló!"

**Buscar y reemplazar interactivo:**

.. code-block:: bash

   #!/bin/bash
   grep -rl "término_viejo" source/ | \
   xargs sed -i 's/término_viejo/término_nuevo/g'




Troubleshooting
===============

Build Muy Lento
===============

.. code-block:: bash

   # Ver qué archivos toman más tiempo
   time make html
   
   # Build incremental (solo cambios)
   make html
   
   # Limpiar cache si problemas
   make clean

Problemas de Encoding
=====================

.. code-block:: bash

   # Ver encoding actual
   file -i archivo.rst
   
   # Convertir a UTF-8
   iconv -f ISO-8859-1 -t UTF-8 archivo.rst > archivo_utf8.rst
   
   # Detectar caracteres problemáticos
   grep -P "[^\x00-\x7F]" archivo.rst

Espacio en Disco
================

.. code-block:: bash

   # Ver uso de disco
   du -sh build/
   
   # Limpiar builds antiguos
   make clean
   
   # Encontrar archivos grandes
   find build -type f -size +10M




Automatización
==============

Makefile Personalizado
======================

.. code-block:: makefile

   # Agregar a Makefile
   
   .PHONY: watch
   watch:
       sphinx-autobuild source build/html
   
   .PHONY: stats
   stats:
       @echo "Archivos RST:" `find source -name "*.rst" | wc -l`
       @echo "Líneas totales:" `find source -name "*.rst" -exec wc -l {} \; | awk '{sum += $1} END {print sum}'`
   
   .PHONY: deploy
   deploy: clean html
       rsync -av build/html/ usuario@servidor:/ruta/docs/

Pre-commit Hooks
================

.. code-block:: bash

   # .git/hooks/pre-commit
   #!/bin/bash
   
   # Verificar que todo compila
   make html > /dev/null 2>&1
   if [ $? -ne 0 ]; then
       echo "Build falló. Commit abortado."
       exit 1

   fi
   
   echo "Build exitoso."
   exit 0




Recursos Adicionales
====================

Documentación Oficial
=====================

.. code-block:: text

   Sphinx: https://www.sphinx-doc.org/
   Git: https://git-scm.com/doc
   Pandoc: https://pandoc.org/
   RST: https://docutils.sourceforge.io/rst.html

Herramientas Online
===================

.. code-block:: text

   RST Preview: https://livesphinx.herokuapp.com/
   Table Generator: https://www.tablesgenerator.com/text_tables
   Regex Tester: https://regex101.com/




.. seealso::
   
   * :doc:`cheatsheets/cheatsheet_rst` - Cheatsheet RST
   * :doc:`../07_guias_uso/troubleshooting` - Solución de problemas
   * :doc:`../05_herramientas_medios/index` - Herramientas y medios

.. note::
   Estos comandos están probados en Linux/Mac. En Windows, puede requerir WSL o adaptaciones.
