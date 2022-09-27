from zooAnimales.animal import Animal


class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color, largo):
        super().__init__(nombre, edad, habitat, genero)
        self.colorescamas = color
        self.largocola = largo
        Reptil.listado.append(self)

    def movimiento():
        return "reptar"

    @classmethod
    def cantidadReptiles(self):
        return len(Reptil.listado)

    @classmethod
    def crearIguana(self, nombre, edad, genero,):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(self, nombre, edad, genero,):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return serpiente

    def getColorEscamas(self):
        return self.colorescamas

    def getLargoCola(self):
        return self.largocola
