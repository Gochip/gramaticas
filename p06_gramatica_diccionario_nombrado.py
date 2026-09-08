"""
Compiladores: de la Teoría a la Práctica
Tema: Representación de una gramática como diccionario con claves nombradas.

En vez de usar posiciones (como en la tupla formal) o inferir T y S por
convención (como en las variantes de "solo producciones"), esta variante
declara explícitamente los cuatro componentes de la gramática bajo claves
textuales. Es más verbosa, pero más legible y menos propensa a errores por
orden de posición: T, N y S se colocan como listas (en vez de conjuntos)
para conservar un orden de presentación estable.

Fuente: adaptado de Gramaticas.ipynb (celda 23).
"""

G = {
    'Terminales': ['a', 'b', 'c', 'd'],
    'NoTerminales': ['S', 'A'],
    'Axioma': 'S',
    'Producciones': {
        'S': [['a', 'A', 'b']],
        'A': [['c'], ['d']]
    }
}


if __name__ == "__main__":
    print("Te:", G['Terminales'])
    print("NT:", G['NoTerminales'])
    print("Ax:", G['Axioma'])
    print("Pr:", G['Producciones'])

    print("\nProducciones:")
    for nt in G['NoTerminales']:         # para cada no terminal
        for p in G['Producciones'][nt]:  # para cada producción de ese no terminal
            print(nt, ":=", p)           # imprime la producción
