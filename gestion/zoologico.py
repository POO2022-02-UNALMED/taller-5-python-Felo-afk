class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zo):
        self.zonas.append(zo)

    def cantidadTotalAnimales(self):
        cont = 0
        for i in self.zonas:
            cont += i.cantidadAnimales()
        return cont

    def getNombre(self):
        return self.nombre

    def getUbicacion(self):
        return self.ubicacion

    def getZona(self):
        return self.zonas
