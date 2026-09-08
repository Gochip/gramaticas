"""
Compiladores: de la Teoría a la Práctica
Tema: Resumen comparativo de las alternativas de representación de una
gramática, todas modelando: S := a A b   |   A := c   |   A := d

    Alternativa 1: cuádrupla cercana a la definición formal (T, N, S, P).
    Alternativa 2: solo las producciones, en un diccionario.
    Alternativa 3: solo las producciones, en una lista de pares.
    Alternativa 4: diccionario con las cuatro componentes bajo claves nombradas.

Ninguna alternativa es "la correcta": la elección depende de si se prioriza
la fidelidad a la definición formal (1), la brevedad de escritura (2 y 3)
o la legibilidad y robustez ante errores de posición (4). El resto de este
proyecto adopta una quinta variante (ver p08_gramatica_modelo_quintupla.py)
que añade un nombre identificador a la Alternativa 1, usada como base de
los validadores.

Fuente: adaptado de Gramaticas.ipynb (celda 27).
"""

# Alternativa 1: cercana a la definición formal
graA1 = ({'a', 'b', 'c', 'd'}, {'S', 'A'}, 'S', {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]})

# Alternativa 2: solo producciones en un diccionario
graA2 = {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]}

# Alternativa 3: solo producciones en una lista
graA3 = [['S', [['a', 'A', 'b']]], ['A', [['c'], ['d']]]]

# Alternativa 4: un diccionario de cuatro claves y sus valores
graA4 = {'Terminales': ['a', 'b', 'c', 'd'],
         'NoTerminales': ['S', 'A'],
         'Axioma': 'S',
         'Producciones': {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]}}


if __name__ == "__main__":
    print("Alternativa 1 (cuádrupla formal):", graA1)
    print("Alternativa 2 (solo producciones, dict):", graA2)
    print("Alternativa 3 (solo producciones, lista):", graA3)
    print("Alternativa 4 (diccionario nombrado):", graA4)
