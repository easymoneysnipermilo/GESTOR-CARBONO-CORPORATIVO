# Clase para calcular emisiones por consumo energetico
#hola :D
from src.actividades.actividad import Actividad

#HUELLA DE CARBONO= 100 X 0.5
class ConsumoEnergetico(Actividad):
    def __init__(self, nombre, consumo_kwh, factor_emision):
        super().__init__(nombre)
        self.consumo_kwh = consumo_kwh
        self.factor_emision = factor_emision

    def calcular_huella(self):
        return self.consumo_kwh * self.factor_emision
