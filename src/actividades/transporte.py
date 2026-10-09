# Clase para calcular emisiones por transporte

from src.actividades.actividad import Actividad


class Transporte(Actividad):
    def __init__(self, nombre, distancia_km, factor_emision):
        super().__init__(nombre)
        self.distancia_km = distancia_km
        self.factor_emision = factor_emision

    def calcular_huella(self):
        return self.distancia_km * self.factor_emision
