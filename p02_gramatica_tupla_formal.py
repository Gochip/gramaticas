"""
Compiladores: de la Teoría a la Práctica
Tema: Definición formal de una gramática (cuádrupla bibliográfica).

Una gramática formal se define como la cuádrupla G = (T, N, S, P):
    T: conjunto de símbolos terminales
    N: conjunto de símbolos no terminales
    S: axioma (S pertenece a N)
    P: conjunto de producciones

Aquí P se representa como un diccionario de Python donde cada clave es
un no terminal y cada valor es la lista de sus lados derechos (cada lado
derecho es, a su vez, una lista de símbolos).

Ejemplo modelado:  S := a A b   |   A := c   |   A := d

Fuente: adaptado de Gramaticas.ipynb (celdas 6 y 9).
"""

G = ({'a', 'b', 'c', 'd'}, {'S', 'A'}, 'S', {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]})
#     Terminales           NoTerminales  Axioma         Producciones


def imprimir_cuadrupla(gramatica):
    print("Te:", gramatica[0])
    print("NT:", gramatica[1])
    print("Ax:", gramatica[2])
    print("Pr:", gramatica[3])


def imprimir_producciones(gramatica):
    print("\nProducciones: (el orden no se respeta siempre por ser NT un conjunto)")
    for nt in gramatica[1]:              # para cada símbolo no terminal
        for p in gramatica[3][nt]:       # y para cada producción de ese no terminal
            print(nt, ":=", p)           # imprime la producción

    print("\nO si se quiere (aunque no se prefiere para procesos):")
    for nt in gramatica[1]:
        for p in gramatica[3][nt]:
            print(nt, ":=", end=" ")
            for simbolo in p:
                print(simbolo, end=" ")
            print()


if __name__ == "__main__":
    imprimir_cuadrupla(G)
    imprimir_producciones(G)
