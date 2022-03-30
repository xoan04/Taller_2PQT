import os
from pickle import TRUE
import random
from time import strftime
#from PySide6 import QtCore, QtWidgets, QtGui
from Clases import Alfabeto, Lenguaje
from multipledispatch import dispatch
#from gtts import gTTS
def borrarPantalla(): return os.system("cls")


def menuLenguajes(list_Lenguajes):
    sw = 1
    while sw == 1:
        def borrarPantalla(): return os.system("cls")
#        speach("ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO. 1-Union. 9-Imprimir los Alfabetos. 0-Salir")
        opcion = int(input("""
    ELIJA QUE OPERACION QUIERE HACER CON SU LENGUAJE:

        1 - Union de Lenguajes
        2 - Diferencia de Lenguajes
        3 - Intersección de Lenguajes
        4 - Concatenar de Lenguajes
        5 - Calcular Potencia del Lenguaje
        6 - Calcular la inversa del Lenguaje
        7 - Calcular la Cardinalidad del Lenguaje
        8 - te la enclocho
        9 - Imprimir Lenguajes
        0 - Salir 

    Opción: """))
        borrarPantalla()
        if opcion == 1:
            #            speach("Ingrese el primer alfabeto que quiere unir: ")
            indice1 = int(
                input("Ingrese el primer Lenguaje que quiere unir: "))
#            speach("Ingrese el segundo alfabeto que quiere unir: ")
            indice2 = int(
                input("Ingrese el segundo Lenguaje que quiere unir: "))
#            speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
            print("La union de los alfabetos " +
                  str(indice1)+" y "+str(indice2)+" es: ")
            print(union(indice1-1, indice2-1))
            os.system("PAUSE")

        elif opcion == 2:
            #speach("Ingrese el primer alfabeto: ")
            indice1 = int(input("Ingrese el primer Lenguaje:"))
            #speach("Ingrese el alfabeto que quiere restar: ")
            indice2 = int(input("Ingrese el Lenguaje que quiere restar: "))

            if indice1 < 0 and indice2 < 0:
                #speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print("La union de los Lenguajes " +
                      str(indice1)+" y "+str(indice2)+" es: ")
                print(diferencia(indice1-1, indice2-1))
                os.system("PAUSE")
        elif opcion == 3:
            #speach("Ingrese el primer alfabeto: ")
            indice1 = int(input("Ingrese el primer alfabeto:"))
            #speach("Ingrese el alfabeto que quiere restar: ")
            indice2 = int(input("Ingrese el segundo alfabeto: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
             #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print("La interseccion de los alfabetos " +
                      str(indice1)+" y "+str(indice2)+" es: ")
                print(interseccion(indice1-1, indice2-1))
                os.system("PAUSE")
            else:
                print("ALFABETOS INGRESADOS INVÁLIDO")
                os.system("PAUSE")
        elif opcion == 4:
            indice1=int(input("Ingrese el primer lenguaje a concatenar: "))
            indice2=int(input("Ingrese el segundo lenguaje: "))
            concate=concatenar(list_Lenguajes[indice1-1].getcadLenguage(),list_Lenguajes[indice2-1].getcadLenguage())
            print("La concatenacion es: ")
            print(concate)
        elif opcion == 6:
            indice=int(input("Ingrese el lenguaje al que le quiere aplicar el inverso: "))
            if indice>0 and indice<=len(list_Lenguajes):
                print("El inverso de tu lenguaje "+str(indice)+" es : ")
                print(invertirLenguaje(list_Lenguajes[indice-1].getcadLenguage()))
            else:
                print("Ingrese un alfabeto valido")

            indice
            pass
        elif opcion == 7:
            indice=int(input("Ingrese el lenguaje al que le quiere aplicar cardinalidad: "))
            if indice>0 and indice<=len(list_Lenguajes):
                print("Tu lenguaje "+str(indice)+" tiene : "+str(len(list_Lenguajes[indice-1].getcadLenguage()))+" elementos")
            else:
                print("Ingrese un alfabeto valido")

        elif opcion == 9:
            for i in range(cantidadAlfb):
                #                speach("Sus alfabetos son: ")
                print("Lenguaje "+str(i+1)+": ")
                print(list_Lenguajes[i])
            os.system("PAUSE")
            os.system("cls")
        elif opcion == 0:
            #            speach("SALIDA EXITOSA")
            print("SALIDA EXITOSA ;)")
            sw = 0
        else:
            #            speach("INGRESE UN OPCIÓN CORRECTA")
            print("INGRESE UN OPCIÓN CORRECTA")
            os.system("PAUSE")


def menuAlfabetos():
    list_Lenguajes = []
    sw = 1
    while sw == 1:
        def borrarPantalla(): return os.system("cls")
#        speach("ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO. 1-Union. 9-Imprimir los Alfabetos. 0-Salir")
        opcion = int(input("""
    ELIJA QUE OPERACION QUIERE HACER CON SU ALFABETO:

        1 - Union de Alfabetos
        2 - Diferencia de Alfabetos
        3 - Intersección de Alfabetos
        4 - Clausura o cerradura de estrella de un Alfabeto
        5 - Generar Lenguaje a partir de un Alfabeto.
        6 - Ingresar al menú de lenguajes.
        7 - 
        8 - 
        9 - Imprimir los Alfabetos
        0 - Salir 

    Opción: """))
        borrarPantalla()
        if opcion == 0:
            #            speach("SALIDA EXITOSA")
            print("SALIDA EXITOSA ;)")
            sw = 0
        elif opcion == 1:

            #            speach("Ingrese el primer alfabeto que quiere unir: ")
            indice1 = int(
                input("Ingrese el primer alfabeto que quiere unir: "))
#            speach("Ingrese el segundo alfabeto que quiere unir: ")
            indice2 = int(
                input("Ingrese el segundo alfabeto que quiere unir: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
                #                speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print("La union de los alfabetos " +
                      str(indice1)+" y "+str(indice2)+" es: ")
                print(union(indice1-1, indice2-1))
                os.system("PAUSE")
        elif opcion == 2:
            #speach("Ingrese el primer alfabeto: ")
            indice1 = int(input("Ingrese el primer alfabeto:"))
            #speach("Ingrese el alfabeto que quiere restar: ")
            indice2 = int(input("Ingrese el alfabeto que quiere restar: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
             #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print("La union de los alfabetos " +
                      str(indice1)+" y "+str(indice2)+" es: ")
                print(diferencia(indice1-1, indice2-1))
                os.system("PAUSE")
        elif opcion == 3:
            #speach("Ingrese el primer alfabeto: ")
            indice1 = int(input("Ingrese el primer alfabeto:"))
            #speach("Ingrese el alfabeto que quiere restar: ")
            indice2 = int(input("Ingrese el segundo alfabeto: "))

            if indice1 <= cantidadAlfb and indice2 <= cantidadAlfb:
             #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print("La interseccion de los alfabetos " +
                      str(indice1)+" y "+str(indice2)+" es: ")
                print(interseccion(indice1-1, indice2-1))
                os.system("PAUSE")
            else:
                print("ALFABETOS INGRESADOS INVÁLIDO")
                os.system("PAUSE")
        elif opcion == 4:
            #           speach("Ingrese el primer alfabeto: ")
            indice = int(input("Ingrese el alfabeto que quiere clausurar: "))
            cantidad = int(
                input("Ingrese la cantidad de palabras que desea: "))
            if indice <= cantidadAlfb:
             #   speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                print("La clausura o cerradura de estrella del alfabeto " +
                      str(indice)+" es: ")
                print(cerradura_alfabeto(
                    main_list[indice-1].getCadenaAlfabeto(), cantidad))
                os.system("PAUSE")
        elif opcion == 5:
            #           speach("Ingrese el primer alfabeto: ")
            indice = int(
                input("Ingrese el alfabeto de donde quiere sacar el Lenguaje: "))
            if main_list[indice-1].getCadenaAlfabeto == ["λ"]:
                print("No se puede generar un lenguaje de un alfabeto vacio")
            else:
                cantidad = int(
                    input("Ingrese la cantidad de palabras que desea el Lenguaje: "))
                if indice <= cantidadAlfb:
                    #    speach("La union de los alfabetos "+str(indice1)+" y "+str(indice2)+" es: ")
                    print("El lenguaje proveniente del alfabeto " +
                          str(indice)+" es: ")
                    objeto = Lenguaje(generar_Lenguaje(
                        main_list[indice-1].getCadenaAlfabeto(), cantidad))
                    list_Lenguajes.append(objeto)
                    print(objeto)
                    os.system("PAUSE")

        elif opcion == 6:
            if len(list_Lenguajes) > 0:
                menuLenguajes(list_Lenguajes)
            else:
                print("Debe tener al menos un lenguaje generado.")

        elif opcion == 9:
            for i in range(cantidadAlfb):
                #                speach("Sus alfabetos son: ")
                print("Alfabeto "+str(i+1)+": ")
                print(main_list[i])
            os.system("PAUSE")
            os.system("cls")
        else:
            #            speach("INGRESE UN OPCIÓN CORRECTA")
            print("INGRESE UN OPCIÓN CORRECTA")
            os.system("PAUSE")


@dispatch(int, int)
def union(pos1, pos2):
    resultantList = []
    cadena1 = main_list[pos1]
    cadena2 = main_list[pos2]
    if cadena1.getCadenaAlfabeto() == ["λ"]:
        return cadena2.getCadenaAlfabeto()
    if cadena2.getCadenaAlfabeto() == ["λ"]:
        return cadena1.getCadenaAlfabeto()
    if cadena1.getCadenaAlfabeto() == ["λ"] and cadena2.getCadenaAlfabeto() == ["λ"]:
        return ["λ"]
    for element in cadena1.getCadenaAlfabeto():
        if element not in resultantList:
            resultantList.append(element)
    for element in cadena2.getCadenaAlfabeto():
        if element not in resultantList:
            resultantList.append(element)

    return resultantList


@dispatch(Lenguaje, Lenguaje)
def union(lenguaje1, lenguaje2):
    resultantList = []
    for element in lenguaje1.getCadenaAlfabeto():
        if element not in resultantList:
            resultantList.append(element)
    for element in lenguaje2.getCadenaAlfabeto():
        if element not in resultantList:
            resultantList.append(element)
    return resultantList


@dispatch(int, int)
def diferencia(pos1, pos2):
    resultantList = []
    lista1 = main_list[pos1]
    lista2 = main_list[pos2]
    for item in lista1.getCadenaAlfabeto():
        if item not in lista2.getCadenaAlfabeto():
            resultantList.append(item)
    if resultantList == []:
        return "λ"
    return resultantList


@dispatch(Lenguaje, Lenguaje)
def diferencia(lenguaje1, lenguaje2):
    resultantList = []
    for item in lenguaje1.getCadenaAlfabeto():
        if item not in lenguaje2.getCadenaAlfabeto():
            resultantList.append(item)
    if resultantList == []:
        return "λ"
    return resultantList


@dispatch(int, int)
def interseccion(pos1, pos2):
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


@dispatch(Lenguaje, Lenguaje)
def interseccion(lenguaje1, lenguaje2):
    resultantList = []
    for item1 in lenguaje1.getCadenaAlfabeto():
        for item2 in lenguaje2.getCadenaAlfabeto():
            if item1 in lenguaje2.getCadenaAlfabeto() and item2 in lenguaje1.getCadenaAlfabeto():
                resultantList.append(item1)
    if resultantList == []:
        return "λ"
    return set(resultantList)


def concatenar(listaLeng1, listaLeng2):
    concatenacion = []
    for i in listaLeng1:
        for j in listaLeng2:
            concatenacion.append(str(i)+str(j))
    return concatenacion


def invertirLenguaje(listaLenguaje):
    listaresultado=[]
    for cadena in listaLenguaje:
        cadena=cadena[::-1]
        listaresultado.append(cadena)
    return listaresultado




def cerradura_alfabeto(lista, cant_palabras):
    lista_resultado = ["λ"]
    for i in range(cant_palabras):
        palabra = ""
        for j in range(random.randint(1, 50)):
            palabra += str(lista[random.randint(0, len(lista) - 1)])
            if palabra not in lista_resultado and len(lista_resultado) <= cant_palabras:
                lista_resultado.append(palabra)
    return lista_resultado


def generar_Lenguaje(lista, cant_palabras):
    lista_resultado = []
    for i in range(cant_palabras):
        palabra = ""
        for j in range(random.randint(1, 55)):
            palabra += str(lista[random.randint(0, len(lista) - 1)])
            if palabra not in lista_resultado and len(lista_resultado) < cant_palabras:
                lista_resultado.append(palabra)
    return lista_resultado

# def speach(cadena):
#     language = 'es-us'
#     speech = gTTS(cadena,lang=language,slow=False)
#     speech.save("speach.mp3")
#     os.system("start speach.mp3")


if __name__ == "__main__":
    main_list = []
    sw = 0
#    speach("Ingrese la cantidad de alfabetos que desea")
    while sw == 0:
        cantidadAlfb = int(
            input("Ingrese la cantidad de alfabetos que desea: "))
        if cantidadAlfb > 0:
            for i in range(cantidadAlfb):
                #        speach("ingrese su cadena número "+str(i+1)+" separada por espacios:")
                cadAlfabeto = ""
                cadAlfabeto = input(
                    "ingrese su cadena número "+str(i+1)+" separada por espacios: ").split(" ")
                if cadAlfabeto.__contains__(""):
                    main_list.append(Alfabeto("λ"))
                else:
                    objeto = Alfabeto(cadAlfabeto)
                    main_list.append(objeto)
            borrarPantalla()
            break
        else:
            print("INGRESE UNA CANTIDAD VÁLIDA.")
            os.system("PAUSE")
            borrarPantalla()
    menuAlfabetos()
