"""
Compiladores: de la Teoría a la Práctica
Tema: Validador integral de una gramática.

Compone todos los validadores individuales (p09 a p13) en una única
función de diagnóstico que informa, para una gramática dada, si su
estructura de datos es correcta, si es conceptualmente válida, si está
limpia, si está bien formada y si es apta para un descenso recursivo
predictivo (sin recursión izquierda y factorizada por izquierda).

Fuente: adaptado de Gramaticas.ipynb (celdas 62-63).
"""

from p08_gramatica_modelo_quintupla import G1
from p09_validador_estructura_datos import RevisaEstructuraDeDatos
from p10_validador_estructura_conceptual import RevisaEstructuraConceptual
from p11_validador_gramatica_limpia import RevisaGramaticaLimpia
from p12_validador_gramatica_bien_formada import RevisaGramaticaBienFormada
from p13_validador_factorizacion_recursion_izquierda import RevisaFaReIzquierda


def RevisaGramatica(gramatica):
    print("Revisión de " + gramatica[0] + ":")
    estado = 0
    estado = estado + RevisaEstructuraDeDatos(gramatica)
    estado = estado + RevisaEstructuraConceptual(gramatica)
    estado = estado + RevisaGramaticaLimpia(gramatica)
    estado = estado + RevisaGramaticaBienFormada(gramatica)
    estado = estado + RevisaFaReIzquierda(gramatica)
    # Resultado final de la revisión
    if estado == 0:
        print("* Gramática sin comentarios: OK\n")
    else:
        print("* Gramática con problemas.\n")
    return


if __name__ == "__main__":
    RevisaGramatica(G1)
