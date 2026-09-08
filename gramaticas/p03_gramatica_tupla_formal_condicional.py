"""
Compiladores: de la Teoría a la Práctica
Tema: Segundo ejemplo bibliográfico de gramática formal (cuádrupla).

Modela la sintaxis de una sentencia condicional simple:
    <Condicional> := if <Sentencia> then <Sentencia>
    <Condicional> := if <Sentencia> then <Sentencia> else <Sentencia>
    <Sentencia>   := x | y

Reutiliza las funciones de impresión definidas para la representación en
cuádrupla, mostrando que la misma estructura de datos y el mismo código
sirven para gramáticas de distinto dominio.

Fuente: adaptado de Gramaticas.ipynb (celda 12).
"""

from p02_gramatica_tupla_formal import imprimir_cuadrupla, imprimir_producciones

G = ({'if', 'then', 'else', 'x', 'y'}, {'<Condicional>', '<Sentencia>'}, '<Condicional>',
     {'<Condicional>': [['if', '<Sentencia>', 'then', '<Sentencia>'],
                         ['if', '<Sentencia>', 'then', '<Sentencia>', 'else', '<Sentencia>']],
      '<Sentencia>': [['x'], ['y']]})


if __name__ == "__main__":
    imprimir_cuadrupla(G)
    imprimir_producciones(G)
