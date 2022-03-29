from imp import create_dynamic
import os
from pickle import TRUE
import sys
import random
from time import strftime
from PySide6 import QtCore, QtWidgets, QtGui
from Clases import Alfabeto,Lenguaje
from gtts import gTTS

borrarPantalla = lambda: os.system ("cls")

def menu():
    sw = 1
    while sw == 1:
        speach("ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO. 1-Union. 9-Imprimir los Alfabetos. 0-Salir")
        opcion=int(input("""        

    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Union de Alfabetos
        2 - Diferencia de Alfabetos
        3 - Intersección de Alfabetos
        9 - Imprimir los Alfabetos
        0 - Salir 

    Opción: """))

        borrarPantalla()

        if opcion == 1:

            speach("Ingrese el primer alfabeto que quiere unir: ")
            indice1 = int(input("Ingrese el primer alfabeto que quiere unir: "))
            speach("Ingrese el segundo alfabeto que quiere unir: ")
            indice2 = int(input("Ingrese el segundo alfabeto que quiere unir: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
                speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print ("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print(unionAlfabetos(indice1-1, indice2-1))
                os.system("PAUSE")

        elif opcion == 2:
            #speach("Ingrese el primer alfabeto: ")
            indice1 = int(input("Ingrese el primer alfabeto:"))
            #speach("Ingrese el alfabeto que quiere restar: ")
            indice2 = int(input("Ingrese el alfabeto que quiere restar: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
             #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print ("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print(diferenciaAlfabetos(indice1-1, indice2-1))
                os.system("PAUSE")
        elif opcion == 3:
            #speach("Ingrese el primer alfabeto: ")
            indice1 = int(input("Ingrese el primer alfabeto:"))
            #speach("Ingrese el alfabeto que quiere restar: ")
            indice2 = int(input("Ingrese el alfabeto que quiere restar: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
             #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print ("La interseccion de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print(interseccionAlfabetos(indice1-1, indice2-1))
                os.system("PAUSE")
        elif opcion == 9:
            for i in range(cantidadAlfb):
                speach("Sus alfabetos son: ")
                print("Alfabeto "+str(i+1)+": ")
                print(main_list[i])
            os.system("PAUSE")
            os.system("cls")
        elif opcion == 0:
            speach("SALIDA EXITOSA")
            print("SALIDA EXITOSA ;)")
            sw = 0
        else:
            speach("INGRESE UN OPCIÓN CORRECTA")
            print("INGRESE UN OPCIÓN CORRECTA")
            os.system("PAUSE")


def unionAlfabetos(pos1, pos2):
    resultantList = []
    cadena1 = main_list[pos1]
    cadena2 = main_list[pos2]    
    for element in cadena1.getCadenaAlfabeto():
        if element not in resultantList:
            resultantList.append(element)
    for element in cadena2.getCadenaAlfabeto():
        if element not in resultantList:
            resultantList.append(element)
    return resultantList


def diferenciaAlfabetos(pos1, pos2):
    resultantList = []
    lista1 = main_list[pos1]
    lista2 = main_list[pos2]
    for item in lista1.getCadenaAlfabeto():
        if item not in lista2.getCadenaAlfabeto():
            resultantList.append(item)
    return resultantList


def interseccionAlfabetos(pos1, pos2):
    resultantList = []
    lista1 = main_list[pos1]
    lista2 = main_list[pos2]
    for item1 in lista1.getCadenaAlfabeto():
        for item2 in lista2.getCadenaAlfabeto():
            if item1 in lista2.getCadenaAlfabeto() and item2 in lista1.getCadenaAlfabeto():
                resultantList.append(item1)
    return set(resultantList)






    # for item in lista2:
    #     if item in lista2:
    #         resultantList.append(item)
    #     elif item not in lista2:
    #         lista1


    return resultantList


def speach(cadena):
    language = 'es-us'
    speech = gTTS(cadena,lang=language,slow=False)
    speech.save("speach.mp3")
    os.system("start speach.mp3")


if __name__ == "__main__":
    main_list = []
#    Lista_Union=[]
#    resultantList = []
    speach("Ingrese la cantidad de alfabetos que desea")
    cantidadAlfb = int( input("Ingrese la cantidad de alfabetos que desea: "))
    
    for i in range (cantidadAlfb):
        speach("ingrese su cadena número "+str(i+1)+" separada por espacios:")
        cadAlfabeto = ""
        cadAlfabeto = input("ingrese su cadena número "+str(i+1)+" separada por espacios: ").split(" ")
        if cadAlfabeto.__contains__(""):
            main_list.append(Alfabeto("λ"))
        else:
            objeto = Alfabeto(cadAlfabeto)
            main_list.append(objeto)
        
    menu()

    