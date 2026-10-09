# Gestor de Carbono Corporativo

from src.organizacion.empresa import Empresa
from src.organizacion.departamento import Departamento
from src.actividades.consumo_energetico import ConsumoEnergetico
from src.actividades.transporte import Transporte
from src.actividades.residuos import Residuos


print("   GESTOR DE CARBONO CORPORATIVO")

# Crear empresa
empresa = Empresa("EMPRESA")

# Crear departamento
departamento = Departamento("Administracion")

# Crear actividades
energia = ConsumoEnergetico("Consumo electrico", 100, 0.5)
transporte = Transporte("Transporte laboral", 50, 0.2)
residuos = Residuos("Residuos generados", 20, 0.1)

# Agregar actividades al departamento
departamento.agregar_actividad(energia)
departamento.agregar_actividad(transporte)
departamento.agregar_actividad(residuos)

# Agregar departamento a la empresa
empresa.agregar_departamento(departamento)

# Calcular emisiones
total = empresa.calcular_huella()

print()
print("Empresa:", empresa.nombre)
print("Departamento:", departamento.nombre)
print("Emisiones por energia:", energia.calcular_huella())
print("Emisiones por transporte:", transporte.calcular_huella())
print("Emisiones por residuos:", residuos.calcular_huella())
print("-----------------------------------")
print("Huella de carbono total:", total)
