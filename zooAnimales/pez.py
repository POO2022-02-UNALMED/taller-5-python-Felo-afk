from zooAnimales.animal import Animal


class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, color, aletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = color
        self.cantidadAletas = aletas
        Pez.listado.append(self)

    def movimiento():
        return "nadar"

    @classmethod
    def cantidadPeces(self):
        return len(Pez.listado)

    @classmethod
    def crearSalmon(self, nombre, edad, genero,):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(self, nombre, edad, genero,):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return bacalao

    def getColorEscamas(self):
        return self.colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas
