from zooAnimales.animal import Animal


class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = color
        Ave.listado.append(self)

    def movimiento():
        return "volar"

    @classmethod
    def cantidadAves(self):
        return len(Ave.listado)

    @classmethod
    def crearHalcon(self, nombre, edad, genero,):
        nuevo = Ave(nombre, edad, "monatanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return nuevo

    @classmethod
    def crearAguila(self, nombre, edad, genero,):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return aguila

    def getColorPlumas(self):
        return self.colorPlumas
