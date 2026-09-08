"""
Compiladores: de la Teoría a la Práctica
Tema: Validación de "gramática bien formada".

Una gramática bien formada es, primero, una gramática limpia (ver p11), y
además no contiene:
    - reglas de redenominación:  A := B  (un no terminal que solo renombra
                                  a otro, sin aportar estructura)
    - reglas no generativas fuera del axioma:  A := lambda  con A != S
                                  (solo el axioma puede derivar la cadena
                                  vacía)

Fuente: adaptado de Gramaticas.ipynb (celdas 52-53).
"""

from p08_gramatica_modelo_quintupla import G1
from p11_validador_gramatica_limpia import RevisaGramaticaLimpia


def RevisaGramaticaBienFormada(gramatica):
    estado = 0
    # Revisa que la gramática esté limpia
    estado = estado + RevisaGramaticaLimpia(gramatica)
    # Revisa gramática bien formada
    ## Veo regla de redenominación y no generativa
    ladosIzquierdos = gramatica[4].keys()
    for li in ladosIzquierdos:
        for ld in gramatica[4][li]:
            largo = len(ld)
            if largo == 1 and ld[0] in gramatica[2] and ld[0] != li:
                estado = 1; print("- Regla de redenominación: " + li + ":=" + ld[0])
            if largo == 0 and li != gramatica[3]:
                estado = 1; print("- Regla no generativa: " + li + ":=lambda")
    return estado


if __name__ == "__main__":
    if RevisaGramaticaBienFormada(G1) == 0:
        print("La gramática está bien formada")
    else:
        print("La gramática no está bien formada")
