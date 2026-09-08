"""
Compiladores: de la Teoría a la Práctica
Tema: Representación reducida de una gramática — solo producciones (lista).

Variante de la representación mínima que usa una lista de pares
[no_terminal, lados_derechos] en lugar de un diccionario. Es equivalente
en expresividad a la variante con diccionario, pero no depende de que las
claves sean hasheables ni de la garantía de orden de inserción de dict,
a costa de una búsqueda por no terminal más costosa (lineal en vez de O(1)).

Fuente: adaptado de Gramaticas.ipynb (celda 19).
"""

G = [['S', [['a', 'A', 'b']]], ['A', [['c'], ['d']]]]
#          Producción de S             Producciones de A

NoTerminales = []
for p in G:
    NoTerminales.append(p[0])

Terminales = []
for p in G:
    for ld in p[1]:
        if len(ld) > 0:
            for i in range(len(ld)):
                if ld[i] not in NoTerminales:
                    if ld[i] not in Terminales:
                        Terminales.append(ld[i])


if __name__ == "__main__":
    print("Te:", Terminales)
    print("NT:", NoTerminales)
    print("Ax:", NoTerminales[0])
    print("Pr:", G)

    print("\nProducciones:")
    for prods in G:
        li = prods[0]
        for ld in prods[1]:
            print(li, ":=", ld)
