import os
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from Alfabeto import Alfabeto




borrarPantalla = lambda: os.system ("cls")

def menu():
    main_list.pop(0)
    sw = 1
    while sw == 1:
        
        opcion=int(input("""

    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Union 
        9 - Imprimir los Alfabetos
        0 - Salir 

    Opción: """))
        borrarPantalla()

        if opcion == 1:
            print ("La union de los "+str(cantidadAlfb)+" alfabetos es: ")
            print(unionAlfabetos())
        elif opcion == 2:
            pass
        elif opcion == 9:
            for i in range(cantidadAlfb):
                print("Alfabeto "+str(i+1)+": ", end=" ")
                print(main_list[i])
        elif opcion == 0:
            print("SALIDA EXITOSA ;)")
            sw = 0
        else:
            print("INGRESE UN OPCIÓN CORRECTA")


def unionAlfabetos():
    resultantList = []
    for element in Lista_Union:
        if element not in resultantList:
            resultantList.append(element)
    return resultantList


def verificarAlfabeto(cadAlfabeto):
    cadAlfabetoToSet = set(cadAlfabeto)
    new_list = list(cadAlfabetoToSet)
    return new_list


if __name__ == "__main__":


    

    main_list = [""]
    Lista_Union=[]
    resultantList = []

    cantidadAlfb = int( input("Ingrese la cantidad de alfabetos que desea: "))
    for i in range (cantidadAlfb):
        cadAlfabeto = input("ingrese su cadena número "+str(i+1)+" separada por espacios: ").split(" ")
        cadAlfabeto = verificarAlfabeto(cadAlfabeto)
        Lista_Union += cadAlfabeto

        objeto = Alfabeto(cadAlfabeto)

        main_list.append(objeto)
    menu()



"""
    cadAlfabeto = "AAA BBB CCC"
    cadAlfabeto.split(sep=" ")
    cadAlfabeto = verificarAlfabeto(cadAlfabeto)
    main_list.append(Alfabeto(cadAlfabeto))

    cadAlfabeto = "111 222 333"
    cadAlfabeto.split(sep=" ")
    cadAlfabeto = verificarAlfabeto(cadAlfabeto)
    main_list.append(Alfabeto(cadAlfabeto))

    cadAlfabeto = "+++ +++ ---"
    cadAlfabeto.split(sep=" ")
    cadAlfabeto = verificarAlfabeto(cadAlfabeto)
    main_list.append(Alfabeto(cadAlfabeto))
"""


"""
    cadena1 = "abc def ghi jkl mno"     #str(input("Ingrese la cadena numero "+str(numero)+": ").split(sep=","))
    cadena1 = cadena1.split(" ")
    cadena2 = "123 456 789"     #str(input("Ingrese la cadena numero "+str(numero)+": ").split(sep=","))
    cadena2 = cadena2.split(" ")
    cadena3 = "+- */ ¿? !! $%"     #str(input("Ingrese la cadena numero "+str(numero)+": ").split(sep=","))
    cadena3 = cadena3.split(" ")
    main_list.append(cadena1)
    main_list.append(cadena2)
    main_list.append(cadena3)
"""

