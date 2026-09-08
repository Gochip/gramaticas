"""
Compiladores: de la Teoría a la Práctica
Tema: Banco de gramáticas de ejemplo, en el formato quíntupla (ver p08).

Cubre casos representativos usados típicamente en un curso de
compiladores:
    G1  Ejemplo mínimo de la definición formal.
    G2  Variante de G1 con dos no terminales independientes.
    G3  Números como secuencia de dígitos (recursión por derecha).
    G4  Igual que G3, pero con un no terminal auxiliar F que sí admite
        producción lambda (para ilustrar reglas no generativas).
    G5  Paréntesis balanceados (con recursión izquierda intencional,
        útil para ejercitar el detector de p13).
    G6  Expresiones aritméticas con precedencia de operadores clásica
        (gramática ambigua-recursiva por izquierda, estilo académico).
    G7  La misma expresión aritmética de G6, pero reescrita para eliminar
        la recursión izquierda (forma apta para descenso recursivo, al
        estilo de la técnica de Aho/Ullman).
    G8  Un fragmento de "español pequeño" (sujeto + predicado), para
        mostrar que las gramáticas libres de contexto no se limitan a
        lenguajes de programación.
    G9  Gramática de un lenguaje ensamblador simplificado ("graRAM"),
        de tamaño más realista que los ejemplos anteriores.

Fuente: adaptado de Gramaticas.ipynb (celda 66).
"""

G1 = ('Ejemplo1', {'a', 'b', 'c', 'd'}, {'S', 'A'}, 'S', {'S': [['a', 'A', 'b']], 'A': [['c'], ['d']]})

G2 = ('Ejemplo2', {'a', 'b'}, {'S', 'A', 'B'}, 'S', {'S': [['a', 'A', 'b']], 'A': [['a']], 'B': [['b']]})

G3 = ('Número', {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}, {'S', 'NU', 'DI'}, 'S',
      {'S': [['NU']],
       'NU': [['DI'], ['DI', 'NU']],
       'DI': [['0'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']]})

G4 = ('NúmeroFI', {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}, {'S', 'NU', 'DI', 'F'}, 'S',
      {'S': [['NU']],
       'NU': [['DI', 'F']],
       'DI': [['0'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']],
       'F': [[], ['NU']]})

G5 = ('Parentesis', {'(', ')'}, {'S'}, 'S', {'S': [['(', 'S', ')', 'S'], []]})

G6 = ('ExpArt', {'a', '+', '*'}, {'E', 'T', 'P'}, 'E',
      {'E': [['E', '+', 'T'], ['T']],
       'T': [['T', '*', 'P'], ['P']],
       'P': [['a']]})

G7 = ('ExpAho', {'id', '+', '*', '(', ')'}, {'E', 'EP', 'T', 'TP', 'F'}, 'E',
      {'E': [['T', 'EP']],
       'EP': [['+', 'T', 'EP'], []],
       'T': [['F', 'TP']],
       'TP': [['*', 'F', 'TP'], []],
       'F': [['id'], ['(', 'E', ')']]})

G8 = ('PeqEsp', {'El', 'el', 'al', 'gato', 'perro', 'persigue', 'come'},
      {'Oracion', 'SU', 'PR', 'AR', 'SS', 'VE'}, 'Oracion',
      {'Oracion': [['SU', 'PR']],
       'SU': [['AR', 'SS']],
       'PR': [['VE', 'SU']],
       'AR': [['El'], ['el'], ['al']],
       'SS': [['gato'], ['perro']],
       'VE': [['persigue'], ['come']]})

G9 = ('graRAM', {'NL', 'CO', 'II', 'ID', 'FIN', 'ALM', 'LEE', 'CAR', 'SUM', 'RES', 'MUL', 'DIV', 'IMP', 'SAL', 'SXI', 'SXM'},
      {'Programa', 'Lineas', 'algoMas', 'Sentencia', 'Identificador', 'Parametro'}, 'Programa',
      {
          'Programa': [['NL', 'algoMas']],
          'algoMas': [['Sentencia', 'Lineas'], ['FIN']],
          'Lineas': [['NL', 'algoMas']],
          'Sentencia': [['ALM', 'Identificador'], ['LEE', 'Identificador'],
                        ['CAR', 'Parametro'], ['SUM', 'Parametro'], ['RES', 'Parametro'],
                        ['MUL', 'Parametro'], ['DIV', 'Parametro'], ['IMP', 'Parametro'],
                        ['SAL', 'NL'], ['SXI', 'NL'], ['SXM', 'NL']],
          'Identificador': [['ID'], ['II']],
          'Parametro': [['ID'], ['II'], ['CO']]})

TODAS = [G1, G2, G3, G4, G5, G6, G7, G8, G9]
