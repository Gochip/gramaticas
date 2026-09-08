"""
Compiladores: de la Teoría a la Práctica
Tema: Validación de "gramática limpia".

Una gramática se considera limpia cuando no tiene:
    - reglas innecesarias:     A := A (un no terminal que se produce a sí mismo)
    - símbolos inaccesibles:   símbolos que nunca aparecen en ninguna forma
                               derivable desde el axioma
    - símbolos superfluos:     no terminales que nunca terminan de derivar
                               una cadena de terminales

La detección de inaccesibles se resuelve con un algoritmo de punto fijo
(propagación de alcanzabilidad desde el axioma); la de superfluos, con
otro punto fijo (propagación de "quién ya deriva en terminales").

Fuente: adaptado de Gramaticas.ipynb (celdas 47-48).
"""

from p08_gramatica_modelo_quintupla import G1


def RevisaGramaticaLimpia(gramatica):
    estado = 0
    ## Reviso reglas innecesarias
    for items in gramatica[4].items():
        li = items[0]
        for ld in items[1]:
            if len(ld) == 1 and li == ld[0]:  # lado derecho igual al lado izquierdo
                estado = 1; print("- Hay regla innecesaria: " + li + ":=" + ld[0])

    ## Arma estructuras de datos para revisar símbolos inaccesibles y superfluos
    simbolos = []      # para contener símbolos no terminales y terminales
    accesible = []     # para marcar si cada símbolo es accesible (1) o no (0)
    producciones = []  # para contener las producciones como pares [li, ld]
    puntos = []        # para marcar producciones al revisar superfluos
    [simbolos.append(nt) for nt in gramatica[2]]  # carga no terminales
    [simbolos.append(t) for t in gramatica[1]]    # carga terminales
    [accesible.append(0) for s in simbolos]       # marca símbolos como no accesibles
    accesible[simbolos.index(gramatica[3])] = 1   # axioma es accesible por defecto
    for items in gramatica[4].items():            # carga las producciones
        li = items[0]
        for ld in items[1]:
            producciones.append([li, ld])
    [puntos.append(0) for p in producciones]      # marca inicialmente producciones como no vistas

    ## Veo símbolos inaccesibles
    cambios = 1
    while cambios == 1:
        cambios = 0
        for i in range(len(accesible)):
            # Si es un no terminal accesible, se revisan sus producciones
            # para marcar los símbolos del lado derecho como accesibles
            if accesible[i] > 0 and simbolos[i] in gramatica[2]:
                for p in producciones:
                    if p[0] == simbolos[i]:
                        for s in p[1]:
                            if s in simbolos and accesible[simbolos.index(s)] == 0:
                                accesible[simbolos.index(s)] = 1
                                cambios = 1
            if 0 in accesible:
                continue
            else:
                break
    for i in range(len(accesible)):
        if accesible[i] == 0:
            estado = 1; print("- El símbolo:", simbolos[i], "es inaccesible")

    ## Revisa símbolos no terminales superfluos
    ### Primera iteración: no terminales que producen terminales o lambda
    i = 0
    yaEsta = []  # símbolos no superfluos
    for p in producciones:
        if len(p[1]) == 0:
            if p[0] not in yaEsta:
                yaEsta.append(p[0])  # agrego no terminal que produce lambda
            puntos[i] = 1
            i = i + 1
            continue
        l = len(p[1])
        for ld in p[1]:
            if ld in gramatica[1]:
                l = l - 1
                continue
        if l == 0:  # todo el lado derecho son terminales
            if p[0] not in yaEsta:
                yaEsta.append(p[0])  # agrego no terminal que produce terminales
            puntos[i] = 1
        i = i + 1

    ### Otras iteraciones
    cambios = 1
    while cambios == 1:
        cambios = 0
        i = 0
        for p in producciones:
            if puntos[i] == 1:  # producción ya vista
                i = i + 1
                continue
            l = len(p[1])
            for ld in p[1]:
                if ld in gramatica[1] or ld in yaEsta:
                    l = l - 1
                    continue
            if l == 0:
                if p[0] not in yaEsta:
                    yaEsta.append(p[0])  # agrego no terminal que deriva en terminales
                puntos[i] = 1
                cambios = 1
            i = i + 1

    ### Los no terminales que no están en yaEsta son superfluos
    for nt in gramatica[2]:
        if nt not in yaEsta:
            estado = 1; print("- El símbolo '" + nt + "' es superfluo.")
    return estado


if __name__ == "__main__":
    if RevisaGramaticaLimpia(G1) == 0:
        print("La gramática está limpia")
    else:
        print("La gramática no está limpia")
