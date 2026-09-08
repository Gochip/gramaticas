"""
Compiladores: de la Teoría a la Práctica
Tema: Validación de la estructura de datos de una gramática.

Antes de razonar sobre las propiedades lingüísticas de una gramática (si
es limpia, bien formada, factorizada, etc.) hay que verificar que el valor
Python que la representa efectivamente respeta el "contrato" esperado por
p08_gramatica_modelo_quintupla.py: una quíntupla (nombre, T, N, S, P) con
los tipos correctos en cada posición.

Fuente: adaptado de Gramaticas.ipynb (celdas 37-38).
"""

from p08_gramatica_modelo_quintupla import G1


def RevisaEstructuraDeDatos(gramatica):
    estado = 0
    if len(gramatica) != 5:
        estado = 1; print("- La definición no es una quintupla.")
    else:
        if not (isinstance(gramatica[0], str)):
            estado = 1; print("- La definición tiene mal Nombre.")
        if not (isinstance(gramatica[1], set) and gramatica[1] != {}):
            estado = 1; print("- Terminales no es un conjunto válido.")
        if not (isinstance(gramatica[2], set) and gramatica[2] != {}):
            estado = 1; print("- No Terminales no es un conjunto válido.")
        if not (isinstance(gramatica[3], str) and gramatica[3] in gramatica[2]):
            estado = 1; print("- El Axioma no es válido.")
        if not (isinstance(gramatica[4], dict)):
            estado = 1; print("- Las Producciones no son un diccionario.")
    return estado


if __name__ == "__main__":
    if RevisaEstructuraDeDatos(G1) == 0:
        print("Estructura de Datos OK")
    else:
        print("Estructura de Datos con problemas")
