"""
Compiladores: de la Teoría a la Práctica
Tema: Fundamentos de Python usados en el resto del código.

Repasa los tipos y estructuras de datos de Python que se emplean en los
demás archivos de este proyecto para representar gramáticas formales.

Notas:
    - Las variables no se declaran explícitamente, sino implícitamente al
      asignarles un valor.
    - Hay funciones de conversión para definir el tipo explícitamente:
      str(), int(), float(), complex().
    - Los nombres de variables inician con letra o "_" y luego pueden
      seguir letras, "_" o dígitos.
    - Tipos de datos simples: str, int, float, complex, bool, bytes, ...
    - Tipos de datos secuencia: str, lista, tupla, diccionario, conjunto, range.

Fuente: adaptado de Gramaticas.ipynb (celdas 1-2).
"""

numeroEntero = 3; numeroEntero = int(3); numeroEntero = int('3')  # formas distintas de definir un entero
numeroReal = 3.0
numeroComplejo = 3 + 2j
cadena = "gramática"          # entre comillas dobles
otraCadena = 'otraGramática'   # entre comillas simples es igual
booleano = True; booleano = False
lista = [1, 2, "mate"]        # modificable, ordenada, permite duplicados, acceso por índice, iterable
tupla = (1, 2, "mate")        # no modificable, ordenada, permite duplicados, acceso por índice, iterable
conjunto = {1, 2, "mate"}     # no modificable, no ordenada, no permite duplicados, iterable
rango = range(1, 5)
# diccionario: pares (clave: valor), modificable, ordenado, no permite claves duplicadas, acceso por clave
diccionario = {'Nombre': "JCV", 'Edad': 66}


if __name__ == "__main__":
    print("entero......:", numeroEntero, type(numeroEntero))
    print("real........:", numeroReal, type(numeroReal))
    print("complejo....:", numeroComplejo, type(numeroComplejo))
    print("cadena......:", cadena, type(cadena))
    print("booleano....:", booleano, type(booleano))
    print("lista.......:", lista, type(lista))
    print("tupla.......:", tupla, type(tupla))
    print("conjunto....:", conjunto, type(conjunto))
    print("rango.......:", list(rango), type(rango))
    print("diccionario.:", diccionario, type(diccionario))
