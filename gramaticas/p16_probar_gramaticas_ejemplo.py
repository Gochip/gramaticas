"""
Compiladores: de la Teoría a la Práctica
Tema: Corrida del validador integral sobre el banco de gramáticas de ejemplo.

Ejecuta RevisaGramatica (p14) sobre cada una de las nueve gramáticas de
p15, sirviendo como suite de prueba manual: cada gramática fue elegida
para poner en evidencia (o descartar) alguna de las propiedades que
verifican los validadores (limpieza, buena formación, recursión y
factorización por izquierda).

Fuente: adaptado de Gramaticas.ipynb (celda 68).
"""

from p14_validador_gramatica_completo import RevisaGramatica
from p15_gramaticas_de_ejemplo import TODAS

if __name__ == "__main__":
    for gramatica in TODAS:
        RevisaGramatica(gramatica)
