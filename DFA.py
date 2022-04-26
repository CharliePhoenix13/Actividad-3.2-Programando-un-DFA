"""
Carlos Emilio Murillo Millan A01367816
Actividad 3.2 DFA
"""

import sys
import os.path

SYMBOLS = {
    "=" : "Asignación",
    "+ ": "Suma",
    "*" : "Multiplicación",
    "^" : "Potencia",
    "(" : "Paréntesis que abre",
    ")" : "Paréntesis que cierra"
}

NUM_ESPACIOS = 40

def lexerAritmetico(nombre_archivo):

    inputFile = open(nombre_archivo)

    open('output.txt', 'w').close()

    outputFile = open("output.txt", 'a', encoding='utf-8')

    print('Token' + (' ' * (NUM_ESPACIOS - len('Token'))) + 'Tipo', file=outputFile)

    for line in inputFile.readlines():
        processLine(line, inputFile, outputFile)
    
    outputFile.close()
    inputFile.close()

def error_sintaxis(inputFile, outputFile):
    inputFile.close()
    outputFile.close
    print('ERROR DE SINTAXIS. TERMINANDO PROGRAMA', file=outputFile)
    sys.exit()

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("USO: python -m DFA [ARCHIVO_CON_EXPRESIONES.txt]")
        sys.exit()

    archivo = sys.argv[1]

    if archivo[-4:] != ".txt":
        print("Debes proveer un archivo .txt")
        sys.exit()

    if not os.path.isfile(archivo):
        print ("Este archivo no se encuentra en el directorio actual")
        sys.exit()

    lexerAritmetico(archivo)