
class Alfabeto:    
    
    def __init__(self, cadena):
        self.cadenaAlfabeto = self.verificarAlfabeto(cadena)
        self.contenedorCadena = cadena

    def getCadenaAlfabeto(self):
        return self.contenedorCadena

    def __repr__(self):
        return str(self.cadenaAlfabeto)


    def verificarAlfabeto(self, cadenaAlfabeto):
        cadenaAlfabetoToSet = set(cadenaAlfabeto)
        newList = list(cadenaAlfabetoToSet)
        return newList


class Lenguaje:
    def __init__(self, cadena):
        self.cadLenguage = cadena
        

    def __repr__(self):
        return str(self.cadLenguage)

class Operaciones:
    def __init__(self) -> None:
        pass
