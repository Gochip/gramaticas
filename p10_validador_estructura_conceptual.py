"""
Compiladores: de la Teoría a la Práctica
Tema: Validación de la estructura conceptual de una gramática.

Una vez confirmado el tipo de dato (ver p09), se verifican las
restricciones conceptuales que exige la definición formal de una
gramática libre de contexto:
    - Terminales y No Terminales deben ser conjuntos disjuntos.
    - El axioma debe ser un No Terminal.
    - Todo lado izquierdo de una producción debe ser un No Terminal.
    - Todo símbolo de un lado derecho debe ser Terminal o No Terminal
      (no puede haber símbolos "extraños" a la gramática).

Fuente: adaptado de Gramaticas.ipynb (celdas 42-43).
"""

from p08_gramatica_modelo_quintupla import G1


def RevisaEstructuraConceptual(gramatica):
    estado = 0
    if not gramatica[1].isdisjoint(gramatica[2]):
        estado = 1; print("- Terminales y No Terminales no son disjuntos")
    if gramatica[3] not in gramatica[2]:
        estado = 1; print("- El axioma debe ser un No Terminal")
    ## Reviso producciones
    ladosIzquierdos = gramatica[4].keys()
    ladosDerechos = gramatica[4].values()
    for li in ladosIzquierdos:
        if li not in gramatica[2]:
            estado = 1; print("- Lado izquierdo no es No Terminal: " + li)
    for ld in ladosDerechos:
        for prod in ld:
            for i in range(len(prod)):
                if not (prod[i] in gramatica[1] or prod[i] in gramatica[2]):
                    estado = 1; print("- Lado derecho con símbolo extraño: " + prod[i])
    return estado


if __name__ == "__main__":
    if RevisaEstructuraConceptual(G1) == 0:
        print("Estructura Conceptual OK")
    else:
        print("Estructura Conceptual con problemas")
