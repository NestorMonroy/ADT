# Modos de Traduccion ADT

Basado en: source/02_procedimientos/

ADT define tres modos principales de traduccion, cada uno apropiado para diferentes tipos de contenido y audiencias.

## Modo 1: Alta Fidelidad

### Cuando Usar

- Especificaciones tecnicas sensibles
- Contratos y documentacion legal
- APIs y documentacion de referencia
- Documentacion que requiere precision maxima
- Material donde cambios minimos pueden alterar significado

### Caracteristicas

PRESERVACION MAXIMA:
- Estructura original exacta
- Orden de secciones conservado
- Numeracion original mantenida
- Referencias literales preservadas

TRANSFORMACIONES MINIMAS:
- Solo cambios necesarios para medio destino
- Markdown -> RST (sintaxis)
- HTML -> RST (sintaxis)
- Ajustes de formato obligatorios

TERMINOLOGIA:
- Terminos tecnicos SIN traducir
- Nombres propios conservados
- APIs, comandos, codigo literales

### Proceso

1. Analizar estructura original
2. Mapeo directo a RST
3. Preservar jerarquia exacta
4. Validar equivalencia estructural

### Ejemplo

```
ORIGINAL (Ingles, Markdown):
## API Reference

### GET /api/users

Returns a list of users.

**Parameters:**
- limit (int): Maximum users to return

TRADUCCION ALTA FIDELIDAD (Español, RST):
Referencia API
==============

GET /api/users
--------------

Devuelve una lista de usuarios.

**Parametros:**
- limit (int): Maximo de usuarios a devolver

(Estructura identica, terminologia tecnica preservada)
```

## Modo 2: Marcado Visual

### Cuando Usar

- Tutoriales y guias educativas
- Guias de usuario
- Material que beneficia de aclaraciones
- Documentacion para principiantes
- Contenido donde navegacion es critica

### Caracteristicas

ENRIQUECIMIENTO CON ADMONICIONES:
- note: Informacion adicional
- warning: Advertencias importantes
- tip: Consejos practicos
- important: Puntos criticos
- caution: Precauciones

MEJORA DE NAVEGABILIDAD:
- TOC local con :contents:
- Cross-references explicitas
- Labels en secciones clave
- Indices y referencias

CONTEXTO VISUAL:
- Bloques destacados
- Separacion clara de secciones
- Enfasis apropiado

### Proceso

1. Traduccion base (alta fidelidad)
2. Identificar puntos de aclaracion
3. Agregar admoniciones apropiadas
4. Mejorar estructura visual
5. Validar que no altera significado

### Ejemplo

```rst
ORIGINAL (plano):
Use the API carefully. Excessive calls may result in rate limiting.

MARCADO VISUAL:
.. warning::
 Use la API con precaucion.

 Llamadas excesivas pueden resultar en rate limiting, lo que
 bloqueara su acceso temporalmente.

.. tip::
 Implemente caching local para reducir llamadas a la API.

(Explicita consecuencias, agrega consejo practico)
```

### Admoniciones Disponibles

```rst
.. note::
 Informacion adicional que enriquece comprension

.. warning::
 Advertencia sobre posibles problemas o errores

.. tip::
 Consejo practico para mejorar uso

.. important::
 Informacion critica que no debe omitirse

.. caution::
 Precaucion necesaria antes de proceder

.. danger::
 Riesgo serio, consecuencias graves si se ignora

.. seealso::
 Referencias a material relacionado
```

## Modo 3: Enriquecimiento

### Cuando Usar

- Material de referencia complejo
- Conceptos que requieren expansion
- Documentacion con contexto implicito
- Material educativo avanzado
- Contenido donde profundizacion ayuda

### Caracteristicas

EXPANSION DE CONCEPTOS:
- Explicaciones detalladas
- Contexto adicional
- Profundizacion en temas

AGREGADO DE EJEMPLOS:
- Ejemplos practicos
- Casos de uso
- Demostraciones

ENLACES A MATERIAL RELACIONADO:
- Referencias cruzadas
- Recursos externos
- Material complementario

### Proceso

1. Traduccion base
2. Identificar conceptos a expandir
3. Agregar explicaciones detalladas
4. Incluir ejemplos relevantes
5. Proporcionar referencias

### Ejemplo

```rst
ORIGINAL (breve):
The factory pattern creates objects.

ENRIQUECIMIENTO:
El patron Factory
-----------------

El patron Factory es un patron creacional que proporciona una interfaz
para crear objetos sin especificar la clase exacta a instanciar.

.. topic:: Profundizacion

 El patron Factory delega la responsabilidad de instanciacion
 a subclases, permitiendo que el codigo cliente trabaje con
 abstracciones en lugar de implementaciones concretas.

**Ejemplo practico:**

.. code-block:: python

 class AnimalFactory:
 def create_animal(self, animal_type):
 if animal_type == "dog":
 return Dog()
 elif animal_type == "cat":
 return Cat()

 # Uso
 factory = AnimalFactory()
 pet = factory.create_animal("dog")

.. seealso::

 - :doc:`patrones_creacionales`
 - :doc:`solid_principles`
 - https://refactoring.guru/design-patterns/factory-method

(Expande concepto, agrega ejemplo, proporciona referencias)
```

### Elementos de Enriquecimiento

```rst
.. topic:: Titulo

 Expansion detallada de un concepto

.. seealso::

 - :doc:`documento_relacionado`
 - https://recurso-externo.com

.. code-block:: python
 :caption: Ejemplo practico

 codigo_ejemplo()

.. glossary::

 Termino
 Definicion detallada
```

## Seleccion de Modo

### Matriz de Decision

Ver: source/04_reglas_operativas/matrices_decision/MD_001_modo_1_vs_modo_2.rst

| Criterio | Alta Fidelidad | Marcado Visual | Enriquecimiento |
|----------|----------------|----------------|-----------------|
| Naturaleza | Tecnica precisa | Educativa | Conceptual profunda |
| Audiencia | Expertos | Principiantes/Intermedios | Mixta, aprendices |
| Objetivo | Referencia exacta | Aprendizaje guiado | Comprension profunda |
| Contexto | Suficiente en original | Escaso, necesita ayuda | Implicito, expandible |
| Precision | Critica | Importante | Flexible |

### Criterios de Seleccion

USAR ALTA FIDELIDAD cuando:
- Precision es absolutamente critica
- Cambios minimos pueden alterar significado
- Documento es especificacion formal
- Audiencia espera formato exacto

USAR MARCADO VISUAL cuando:
- Audiencia necesita guia
- Navegacion es importante
- Aclaraciones mejoran comprension
- Tutorial o guia paso a paso

USAR ENRIQUECIMIENTO cuando:
- Conceptos son complejos
- Contexto ayuda a comprension
- Ejemplos son valiosos
- Audiencia beneficia de profundizacion

### Combinacion de Modos

Es posible COMBINAR modos en un mismo documento:

```rst
# Seccion de referencia: Alta Fidelidad
Referencia API
==============
[contenido preciso, minimal enriquecimiento]

# Seccion de tutorial: Marcado Visual
Tutorial de Uso
===============
[con admoniciones, tips, warnings]

# Seccion conceptual: Enriquecimiento
Conceptos Avanzados
===================
[expansion de ideas, ejemplos, profundizacion]
```

## Validacion por Modo

### Validar Alta Fidelidad

Checklist:
- [ ] Estructura original preservada
- [ ] Orden de secciones identico
- [ ] Terminologia tecnica sin traducir
- [ ] Precision mantenida
- [ ] Sin omisiones

### Validar Marcado Visual

Checklist:
- [ ] Admoniciones apropiadas
- [ ] Navegacion mejorada
- [ ] Aclaraciones sin alterar significado
- [ ] Tips relevantes
- [ ] Visual clara

### Validar Enriquecimiento

Checklist:
- [ ] Conceptos expandidos correctamente
- [ ] Ejemplos pertinentes
- [ ] Referencias utiles
- [ ] Sin introducir errores
- [ ] Profundizacion justificada

## Casos Especiales

### Codigo Fuente

REGLA: Codigo NUNCA se traduce en ningun modo

```rst
.. code-block:: python

 # Comentarios SI se traducen
 def funcion_original(): # Nombres conservar
 """Docstrings SI se traducen."""
 return resultado # Variables conservar
```

### Nombres Propios

REGLA: Nombres propios se conservan en todos los modos

Ejemplos:
- Diataxis (conservar)
- arc42 (conservar)
- Sphinx (conservar)
- Microsoft (conservar)

### Terminos Tecnicos Establecidos

REGLA: Terminos con traduccion establecida dependen del modo

ALTA FIDELIDAD: Conservar original
MARCADO VISUAL/ENRIQUECIMIENTO: Usar traduccion establecida con referencia

```rst
.. note::
 En este documento, "deployment" se refiere al proceso de
 despliegue de software en entornos de produccion.
```

## Referencias

Procedimientos:
- source/02_procedimientos/workflow_general.rst
- source/02_procedimientos/modo_alta_fidelidad/
- source/02_procedimientos/modo_marcado_visual/

Matrices de decision:
- source/04_reglas_operativas/matrices_decision/MD_001_modo_1_vs_modo_2.rst
- source/04_reglas_operativas/matrices_decision/MD_002_cuando_enriquecer.rst

Estandares:
- source/03_estandares/calidad/criterios_calidad.rst

## Notas Importantes

- Modo NO es rigido, puede adaptarse segun seccion
- Coherencia dentro de documento es importante
- Documentar modo aplicado en metadata
- Validar que modo aplicado es apropiado
- Consultar con experto en materia si hay dudas
