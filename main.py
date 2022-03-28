import os
from pickle import TRUE
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from Clases import Alfabeto,Lenguaje
from gtts import gTTS




borrarPantalla = lambda: os.system ("cls")

def menu():
    main_list.pop(0)
    sw = 1
    while sw == 1:
        textmenu="""

    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Union 
        9 - Imprimir los Alfabetos
        0 - Salir 

     """
        speech=gTTS(textmenu,lang=language,slow=False)
        speech.save("textmenu.mp3")
        os.system("start textmenu.mp3")
        opcion=int(input("""
        

    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Union 
        9 - Imprimir los Alfabetos
        0 - Salir 

    Opción: """))

        borrarPantalla()

        if opcion == 1:
            opcion1text="La union de los "+str(cantidadAlfb)+" alfabetos es: "
            speech=gTTS(opcion1text,lang=language,slow=TRUE)
            speech.save("opcion1text.mp3")
            os.system("start opcion1text.mp3")
            print ("La union de los "+str(cantidadAlfb)+" alfabetos es: ")
            uniontext=str(unionAlfabetos())
            os.system("PAUSE")
            speech=gTTS(uniontext,lang=language,slow=TRUE)
            speech.save("uniontext.mp3")
            os.system("start uniontext.mp3")
            print(unionAlfabetos())
            os.system("PAUSE")
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
            incorrectatext="INGRESE UN OPCIÓN CORRECTA"
            speech=gTTS(incorrectatext,lang=language,slow=TRUE)
            speech.save("incorrecta.mp3")
            os.system("start incorrecta.mp3")
            print("INGRESE UN OPCIÓN CORRECTA")
            os.system("PAUSE")


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
    textcant="Ingrese la cantidad de alfabetos que desea"
    language= 'es-us'
    speech=gTTS(textcant,lang=language,slow=False)
    speech.save("textcant.mp3")
    os.system("start textcant.mp3")
    cantidadAlfb = int( input("Ingrese la cantidad de alfabetos que desea: "))

    for i in range (cantidadAlfb):
        textcadenanro="ingrese su cadena número "+str(i+1)+" separada por espacios:"
        speech=gTTS(textcadenanro,lang=language,slow=False)
        speech.save("cadnro.mp3")
        os.system("start cadnro.mp3")
        cadAlfabeto = input("ingrese su cadena número "+str(i+1)+" separada por espacios: ").split(" ")
        cadAlfabeto = verificarAlfabeto(cadAlfabeto)
        Lista_Union += cadAlfabeto

        objeto = Alfabeto(cadAlfabeto)

        main_list.append(objeto)
    menu()

