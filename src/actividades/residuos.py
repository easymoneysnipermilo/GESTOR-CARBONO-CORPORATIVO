# Clase para calcular emisiones por residuos

from src.actividades.actividad import Actividad


class Residuos(Actividad):
    def __init__(self, nombre, cantidad_kg, factor_emision):
        super().__init__(nombre)
        self.cantidad_kg = cantidad_kg
        self.factor_emision = factor_emision

    def calcular_huella(self):
        return self.cantidad_kg * self.factor_emision
