# Clase para representar una empresa


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def calcular_huella(self):
        total = 0

        for departamento in self.departamentos:
            total = total + departamento.calcular_huella()

        return total
