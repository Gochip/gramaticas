"""
Compiladores: de la Teoría a la Práctica
Tema: Generador experimental de una derivación (prototipo incompleto).

El notebook original titula esta sección "Otra prueba para desarrollar
(con problemas)": es un intento de generar una cadena de terminales
derivada de la gramática, siempre tomando la primera producción de cada
no terminal, con retroceso simple si esa producción da cadena vacía.

Se conserva la implementación tal cual para dejar registro del punto de
partida, junto con sus limitaciones conocidas, útiles como caso de
estudio o ejercicio de corrección:
    - No detecta ciclos: una gramática con recursión (p. ej. G5 o G7 en
      p15_gramaticas_de_ejemplo.py) provoca recursión infinita entre
      Derivar/sigo hasta agotar la pila de Python.
    - Solo explora la primera alternativa de cada no terminal en
      `Derivar`; no genera todas las cadenas del lenguaje ni una al azar.
    - No es una derivación por la izquierda ni por la derecha en sentido
      estricto: procesa los símbolos del lado derecho en orden, pero sin
      mantener una forma sentencial explícita.

Fuente: adaptado de Gramaticas.ipynb (celdas 72-75).
"""

from p08_gramatica_modelo_quintupla import G1


def Derivar(gramatica):
    if [] in gramatica[4][gramatica[3]]:
        cadena = ""
        return cadena
    for p in gramatica[4][gramatica[3]]:
        print(gramatica[3], ":=", p)
        cadena = ""
        for s in range(len(p)):
            if p[s] in gramatica[1]:
                cadena = cadena + p[s]
            else:
                cadena = cadena + sigo(gramatica, p[s])
    return cadena


def sigo(gramatica, nt):
    if [] in gramatica[4][nt]:
        cadena = ""
        return cadena
    for p in gramatica[4][nt]:
        print(nt, ":=", p)
        cadena = ""
        for s in range(len(p)):
            if p[s] in gramatica[1]:
                cadena = cadena + p[s]
            else:
                cadena = cadena + sigo(gramatica, p[s])
        if cadena != "":
            break
    return cadena


if __name__ == "__main__":
    print(Derivar(G1))
