"""
Compiladores: de la Teoría a la Práctica
Tema: Representación reducida de una gramática — solo producciones (diccionario).

En vez de guardar explícitamente T, N, S y P, se guarda únicamente el
diccionario de producciones y el resto de la cuádrupla se deriva de él:
    - N: las claves del diccionario.
    - S: se asume que es la clave de la primera producción declarada
         (en Python 3.7+ los diccionarios preservan el orden de inserción).
    - T: todo símbolo que aparece en un lado derecho y no es un no terminal.

Esta alternativa es más compacta de escribir pero exige derivar T y S por
convención, lo cual es una fuente típica de errores si no se documenta.

Fuente: adaptado de Gramaticas.ipynb (celda 15).
"""

G = {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]}

NoTerminales = [x for x in G.keys()]
Terminales = []
for lds in G.values():                        # para cada lado derecho
    for ld in lds:                            # para cada producción en el lado derecho
        if len(ld) > 0:                       # si no es regla no generativa
            for i in range(len(ld)):          # para cada símbolo del lado derecho de la producción
                if ld[i] not in NoTerminales: # si no es un No Terminal
                    if ld[i] not in Terminales:
                        Terminales.append(ld[i])  # es un terminal


if __name__ == "__main__":
    print("Te:", Terminales)
    print("NT:", NoTerminales)
    print("Ax:", NoTerminales[0])
    print("Pr:", G)

    print("\nProducciones:")
    for nt in NoTerminales:
        for p in G[nt]:
            print(nt, ":=", p)
