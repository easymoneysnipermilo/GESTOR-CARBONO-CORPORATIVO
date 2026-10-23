# Pruebas de las clases de organizacion

import unittest

from src.organizacion.empresa import Empresa
from src.organizacion.departamento import Departamento
from src.actividades.consumo_energetico import ConsumoEnergetico


class TestOrganizacion(unittest.TestCase):

    def test_departamento(self):
        departamento = Departamento("Administracion")
        energia = ConsumoEnergetico("Consumo electrico", 100, 0.5)

        departamento.agregar_actividad(energia)

        self.assertEqual(departamento.calcular_huella(), 50.0)

    def test_empresa(self):
        empresa = Empresa("EMPRESA")
        departamento = Departamento("Administracion")
        energia = ConsumoEnergetico("Consumo electrico", 100, 0.5)

        departamento.agregar_actividad(energia)
        empresa.agregar_departamento(departamento)

        self.assertEqual(empresa.calcular_huella(), 50.0)


if __name__ == "__main__":
    unittest.main()
