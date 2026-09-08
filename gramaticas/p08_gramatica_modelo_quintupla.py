"""
Compiladores: de la Teoría a la Práctica
Tema: Modelo de gramática usado por los validadores (quíntupla con nombre).

Se extiende la Alternativa 1 (cuádrupla formal, ver
p02_gramatica_tupla_formal.py) con un nombre identificador como primer
elemento de la tupla:

    G = (nombre, Terminales, NoTerminales, Axioma, Producciones)

Este es el formato canónico que consumen todos los validadores de
p09 a p17.

Fuente: adaptado de Gramaticas.ipynb (celdas 31-33).
"""

G1 = ('Ejemplo1', {'a', 'b', 'c', 'd'}, {'S', 'A'}, 'S', {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]})


def ImprimeGramatica(gramatica):
    print("Nombre.......:", gramatica[0])
    print("Terminales...:", gramatica[1])
    print("No Terminales:", gramatica[2])
    print("Axioma.......:", gramatica[3])
    print("Producciones.:", gramatica[4])
    return


if __name__ == "__main__":
    ImprimeGramatica(G1)
