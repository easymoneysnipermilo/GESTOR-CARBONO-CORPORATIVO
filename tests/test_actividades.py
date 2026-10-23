# Pruebas de las clases de actividades

import unittest

from src.actividades.consumo_energetico import ConsumoEnergetico
from src.actividades.transporte import Transporte
from src.actividades.residuos import Residuos


class TestActividades(unittest.TestCase):

    def test_consumo_energetico(self):
        energia = ConsumoEnergetico("Consumo electrico", 100, 0.5)
        self.assertEqual(energia.calcular_huella(), 50.0)

    def test_transporte(self):
        transporte = Transporte("Transporte laboral", 50, 0.2)
        self.assertEqual(transporte.calcular_huella(), 10.0)

    def test_residuos(self):
        residuos = Residuos("Residuos generados", 20, 0.1)
        self.assertEqual(residuos.calcular_huella(), 2.0)


if __name__ == "__main__":
    unittest.main()

