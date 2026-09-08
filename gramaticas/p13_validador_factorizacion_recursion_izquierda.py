"""
Compiladores: de la Teoría a la Práctica
Tema: Detección de recursión izquierda y falta de factorización izquierda.

Estas dos condiciones son las que impiden construir un analizador
sintáctico predictivo recursivo descendente (LL(1)) directamente a partir
de la gramática:
    - Recursión izquierda:  A := A alpha   (el propio no terminal aparece
      como primer símbolo de uno de sus lados derechos; provoca bucle
      infinito en un descenso recursivo ingenuo).
    - Falta de factorización izquierda: dos producciones del mismo no
      terminal comparten el primer símbolo del lado derecho, por lo que
      un parser predictivo no puede decidir cuál aplicar mirando un solo
      símbolo de anticipación.

Fuente: adaptado de Gramaticas.ipynb (celdas 57-58).
"""

from p08_gramatica_modelo_quintupla import G1


def RevisaFaReIzquierda(gramatica):
    estado = 0
    # Arma estructuras de datos necesarias
    producciones = []  # para contener las producciones como pares [li, ld]
    for items in gramatica[4].items():  # carga las producciones
        li = items[0]
        for ld in items[1]:
            producciones.append([li, ld])

    # Revisa recursión por izquierda
    for p in producciones:
        if len(p[1]) != 0 and p[0] == p[1][0]:
            estado = 1; print("- Gramática con recursión por izquierda:", p[0], ":=", p[1])
            break

    # Revisa si la gramática está factorizada por izquierda
    for nt in gramatica[2]:                # para cada no terminal
        if nt not in gramatica[4].keys():  # que tenga producciones
            continue
        pri = []  # para guardar primer símbolo de lados derechos
        for p in gramatica[4][nt]:         # veo sus producciones
            if len(p) > 0:
                if p[0] not in pri:
                    pri.append(p[0])       # guardo primer símbolo del lado derecho
                else:                      # si ya estaba
                    estado = 1; print("- Producciones de '" + nt + "' no factorizadas por izquierda.")
    return estado


if __name__ == "__main__":
    if RevisaFaReIzquierda(G1) == 0:
        print("La gramática está factorizada por izquierda y no tiene recursión izquierda")
    else:
        print("La gramática tiene recursión por izquierda o no está factorizada por izquierda")
