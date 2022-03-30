
class Alfabeto:    
    
    def __init__(self, cadena):
        self.cadenaAlfabeto = self.verificarAlfabeto(cadena)

    def getCadenaAlfabeto(self):
        return self.cadenaAlfabeto

    def __repr__(self):
        return str(self.cadenaAlfabeto)


    def verificarAlfabeto(self, cadenaAlfabeto):
        cadenaAlfabetoToSet = set(cadenaAlfabeto)
        newList = list(cadenaAlfabetoToSet)
        return newList


class Lenguaje:
    def __init__(self, cadena):
        self.cadLenguage = self.verificarLenguage(cadena)
        
    def __repr__(self):
        return str(self.cadLenguage)
    def getcadLenguage(self):
        return self.cadLenguage
    def verificarLenguage(self, cadLenguage):
        cadenaAlfabetoToSet = set(cadLenguage)
        newList = list(cadenaAlfabetoToSet)
        return newList

class Operaciones:
    def __init__(self) -> None:
        pass
