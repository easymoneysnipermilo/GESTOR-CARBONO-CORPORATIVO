# Clase para organizar las actividades por departamento
#xd

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.actividades = []

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    def calcular_huella(self):
        total = 0

        for actividad in self.actividades:
            total = total + actividad.calcular_huella()

        return total
