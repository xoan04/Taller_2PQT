import os
from pickle import TRUE
import random
from time import strftime
#from PySide6 import QtCore, QtWidgets, QtGui
from Clases import Alfabeto
from Clases import Lenguaje
#from gtts import gTTS

borrarPantalla = lambda: os.system ("cls")

def menu():
    sw = 1
    while sw == 1:
        borrarPantalla = lambda: os.system ("cls")
#        speach("ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO. 1-Union. 9-Imprimir los Alfabetos. 0-Salir")
        opcion=int(input("""        

    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Union de Alfabetos
        2 - Diferencia de Alfabetos
        3 - Intersección de Alfabetos
        4 - Clausura del Lenguaje
        5 - Generar Lenguaje
        9 - Imprimir los Alfabetos
        0 - Salir 

    Opción: """))

        borrarPantalla()
        match opcion:
    

            case 1:

    #            speach("Ingrese el primer alfabeto que quiere unir: ")
                indice1 = int(input("Ingrese el primer alfabeto que quiere unir: "))
    #            speach("Ingrese el segundo alfabeto que quiere unir: ")
                indice2 = int(input("Ingrese el segundo alfabeto que quiere unir: "))

                if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
    #                speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print ("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print(unionAlfabetos(indice1-1, indice2-1))
                    os.system("PAUSE")

            case 2:
                #speach("Ingrese el primer alfabeto: ")
                indice1 = int(input("Ingrese el primer alfabeto:"))
                #speach("Ingrese el alfabeto que quiere restar: ")
                indice2 = int(input("Ingrese el alfabeto que quiere restar: "))

                if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
                #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print ("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print(diferenciaAlfabetos(indice1-1, indice2-1))
                    os.system("PAUSE")
            case 3:
                #speach("Ingrese el primer alfabeto: ")
                indice1 = int(input("Ingrese el primer alfabeto:"))
                #speach("Ingrese el alfabeto que quiere restar: ")
                indice2 = int(input("Ingrese el segundo alfabeto: "))

                if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
                #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print ("La interseccion de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print(interseccionAlfabetos(indice1-1, indice2-1))
                    os.system("PAUSE")
                else:
                    print("ALFABETOS INGRESADOS INVÁLIDO")
                    os.system("PAUSE")
            case 4:
    #           speach("Ingrese el primer alfabeto: ")
                indice = int(input("Ingrese el alfabeto que quiere clausurar: "))
                cantidad = int(input("Ingrese la cantidad de palabras que desea: "))
                if indice <= cantidadAlfb:
                #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print ("La clausura o cerradura de estrella del alfabeto "+str(indice)+" es: ")
                    print(cerradura_alfabeto(main_list[indice-1].getCadenaAlfabeto(), cantidad))
                    os.system("PAUSE")
            case 5:
    #           speach("Ingrese el primer alfabeto: ")
                indice = int(input("Ingrese el alfabeto sobre el que quiere generear el lenguaje: "))
                cantidad = int(input("Ingrese la cantidad de palabras que desea generar en el lenguaje: "))
    
                    
                #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print ("El lenguaje "+str(indice)+" es: ")
                print(generar_lenguage(main_Lenguaje[indice-1].getcadLenguage(),cantidad))
                os.system("PAUSE")

            case 9:
                for i in range(cantidadAlfb):
    #                speach("Sus alfabetos son: ")
                    print("Alfabeto "+str(i+1)+": ")
                    print(main_list[i])
                os.system("PAUSE")
                os.system("cls")
            case  0:
    #            speach("SALIDA EXITOSA")
                print("SALIDA EXITOSA ;)")
                sw = 0
            case _:
    #            speach("INGRESE UN OPCIÓN CORRECTA")
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
    if resultantList == []:
        return "λ"
    return resultantList


def interseccionAlfabetos(pos1, pos2):
    resultantList = []
    lista1 = main_list[pos1]
    lista2 = main_list[pos2]
    for item1 in lista1.getCadenaAlfabeto():
        for item2 in lista2.getCadenaAlfabeto():
            if item1 in lista2.getCadenaAlfabeto() and item2 in lista1.getCadenaAlfabeto():
                resultantList.append(item1)
    if resultantList == []:
        return "λ"
    return set(resultantList)


def cerradura_alfabeto(lista,cant_palabras):
    lista_resultado = ["λ"]
    for i in range(cant_palabras-1):
        palabra = ""
        for j in range(random.randint(2, 5)):
            palabra += str(lista[random.randint(0, len(lista) - 1)])
            if palabra not in lista_resultado and len(lista_resultado) < cant_palabras:
                lista_resultado.append(palabra)
    return lista_resultado

# def speach(cadena):
#     language = 'es-us'
#     speech = gTTS(cadena,lang=language,slow=False)
#     speech.save("speach.mp3")
#     os.system("start speach.mp3")

def generar_lenguage(lista,Cant_PalabrasLeng):
    Lista_Lenguaje=[]
    for i in range(Cant_PalabrasLeng-1):
        palabra = ""
        for j in range(random.randint(2, 55)):
            palabra += str(lista[random.randint(0, len(lista)-1)])
            if palabra not in Lista_Lenguaje and len(Lista_Lenguaje) < Cant_PalabrasLeng:
                Lista_Lenguaje.append(palabra)
        
    return Lista_Lenguaje
   


if __name__ == "__main__":
    main_list = []
    main_Lenguaje=[]
    bandera=0
    bandera2=0
#    Lista_Union=[]
#    resultantList = []
#    speach("Ingrese la cantidad de alfabetos que desea")
    
    while bandera == 0:
        cantidadAlfb = int( input("Ingrese la cantidad de alfabetos que desea: "))
        while cantidadAlfb<1:
            print("Error ingrese minimo 1")
            cantidadAlfb = int( input("Ingrese la cantidad de alfabetos que desea: "))
        for i in range (cantidadAlfb):
            #speach("ingrese su cadena número "+str(i+1)+" separada por espacios:")
            cadAlfabeto = ""
            cadAlfabeto = input("ingrese su cadena número "+str(i+1)+" separada por espacios: ").split(" ")
            cadLenguaje=""
            cadLenguaje=cadAlfabeto
            if cadAlfabeto.__contains__(""):
                main_list.append(Alfabeto("λ"))
            else:
                objeto = Alfabeto(cadAlfabeto)
                objeto2 = Lenguaje(cadLenguaje)
                objeto2=objeto
                main_list.append(objeto)
                main_Lenguaje.append(objeto2)
            
        borrarPantalla = lambda: os.system ("cls")
        bandera=1
        menu()
    

    