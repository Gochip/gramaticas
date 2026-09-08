# Compiladores: de la Teoría a la Práctica

Material didáctico que conecta la **definición formal de una gramática
libre de contexto** —tal como se presenta en la bibliografía clásica de
compiladores— con su **implementación concreta en Python**. El contenido
proviene de `Gramaticas.ipynb` y fue reorganizado en `codigo/` como una
colección de scripts independientes, uno por concepto, pensados para ser
citados individualmente desde artículos o apuntes de clase.

## Motivación

En la teoría, una gramática se define como una cuádrupla:

```
G = (T, N, S, P)
```

- **T**: conjunto de símbolos terminales.
- **N**: conjunto de símbolos no terminales.
- **S**: axioma (S ∈ N).
- **P**: conjunto de producciones, cada una de la forma `A → α` con `A ∈ N` y
  `α ∈ (T ∪ N)*`.

Esa definición es precisa pero no dice nada sobre *cómo representarla en
una estructura de datos* ni sobre *qué propiedades adicionales* debe
cumplir una gramática para ser útil en un compilador real (por ejemplo,
para construir a mano un analizador sintáctico predictivo). Este proyecto
recorre ambos problemas de forma incremental:

1. Cómo pasar de la cuádrupla matemática a distintas representaciones en
   Python, con sus ventajas y costos.
2. Cómo verificar mecánicamente si una gramática está **limpia**, **bien
   formada**, y si es apta para un **descenso recursivo predictivo** (sin
   recursión izquierda, factorizada por izquierda).
3. Un prototipo (deliberadamente incompleto) de generación de una
   derivación, útil como caso de estudio de los límites de un enfoque
   ingenuo.

## Estructura del repositorio

```
compiladores-teoria-y-practica/
├── Gramaticas.ipynb   # Notebook original, fuente de todo el código
├── README.md          # Este archivo
└── codigo/            # Los mismos contenidos, separados por concepto
```

## Contenido de `codigo/`

| Archivo | Tema |
|---|---|
| `p01_variables_python.py` | Tipos y estructuras de datos de Python usados en el resto del proyecto. |
| `p02_gramatica_tupla_formal.py` | Gramática como cuádrupla `(T, N, S, P)`, fiel a la definición formal. |
| `p03_gramatica_tupla_formal_condicional.py` | Segundo ejemplo con la misma representación: sentencia condicional `if/then/else`. |
| `p04_gramatica_solo_producciones_dict.py` | Representación mínima: solo `P` como diccionario; `T` y `S` se infieren. |
| `p05_gramatica_solo_producciones_lista.py` | Igual que la anterior, pero `P` como lista de pares en vez de diccionario. |
| `p06_gramatica_diccionario_nombrado.py` | `T`, `N`, `S`, `P` como claves explícitas de un diccionario. |
| `p07_resumen_alternativas_representacion.py` | Comparación lado a lado de las cuatro alternativas anteriores. |
| `p08_gramatica_modelo_quintupla.py` | Modelo canónico usado por los validadores: cuádrupla + nombre identificador. |
| `p09_validador_estructura_datos.py` | Valida que el valor Python tenga la forma esperada (tipos, aridad). |
| `p10_validador_estructura_conceptual.py` | Valida las restricciones conceptuales de una gramática (disjunción T/N, axioma, símbolos válidos). |
| `p11_validador_gramatica_limpia.py` | Detecta reglas innecesarias, símbolos inaccesibles y símbolos superfluos. |
| `p12_validador_gramatica_bien_formada.py` | Además de limpia, descarta reglas de redenominación y no generativas fuera del axioma. |
| `p13_validador_factorizacion_recursion_izquierda.py` | Detecta recursión izquierda y falta de factorización izquierda (prerrequisitos de LL(1)). |
| `p14_validador_gramatica_completo.py` | Compone todos los validadores anteriores en un único diagnóstico. |
| `p15_gramaticas_de_ejemplo.py` | Banco de nueve gramáticas de ejemplo (números, expresiones aritméticas, paréntesis balanceados, un lenguaje ensamblador simplificado, etc.). |
| `p16_probar_gramaticas_ejemplo.py` | Corre el validador integral sobre las nueve gramáticas de ejemplo. |
| `p17_derivacion_experimental.py` | Prototipo incompleto de generación de una derivación; documenta sus límites conocidos (no detecta ciclos, no explora todas las alternativas). |

Los archivos están numerados en el orden en que conviene leerlos (siguen
la progresión del notebook original) y cada uno tiene un docstring con
una explicación breve del concepto y la referencia a las celdas de origen
en `Gramaticas.ipynb`.

## Cómo ejecutar

Requieren solo Python 3 estándar (sin dependencias externas). Cada
archivo es ejecutable de forma independiente desde el directorio
`codigo/`:

```bash
cd codigo
python3 p02_gramatica_tupla_formal.py
python3 p16_probar_gramaticas_ejemplo.py
```

Los archivos que dependen de otros (por ejemplo, los validadores) usan
imports directos entre sí (`from p08_gramatica_modelo_quintupla import G1`),
por lo que deben ejecutarse desde dentro de `codigo/` o con esa carpeta en
el `PYTHONPATH`.

## Uso como referencia en papers

Cada archivo es una unidad autocontenida de un solo concepto, pensada
para citarse como listado de código. Por ejemplo, en LaTeX:

```latex
\lstinputlisting[language=Python, caption={Validador de gramática limpia}]
  {codigo/p11_validador_gramatica_limpia.py}
```

La numeración (`p01` … `p17`) es estable: si se agregan nuevos temas,
conviene continuar la numeración en vez de reordenar los existentes, para
no invalidar referencias ya publicadas.

## Origen

El contenido es una reorganización de `Gramaticas.ipynb`, un notebook de
cátedra sobre tratamiento de gramáticas formales en Python. Se preservó
la lógica original de cada función; la única corrección aplicada fue un
error de referencia de variable en el mensaje de diagnóstico de
`RevisaEstructuraConceptual` (`p10`).
