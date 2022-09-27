from zooAnimales.animal import Animal


class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, color, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = color
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    def movimiento():
        return "saltar"

    @classmethod
    def cantidadAnfibios(self):
        return len(Anfibio.listado)

    @classmethod
    def crearRana(
            self, nombre, edad, genero,):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(self, n, e, g,):
        salamandra = Anfibio(n, e, "selva", g, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra

    def getColorPiel(self):
        return self.colorPiel

    def isVenenoso(self):
        return self.venenoso
