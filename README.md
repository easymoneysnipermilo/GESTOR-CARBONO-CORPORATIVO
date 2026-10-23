# GESTOR-CARBONO-CORPORATIVO
# Gestor de Carbono Corporativo

## 1. Descripción del proyecto

El Gestor de Carbono Corporativo es un programa desarrollado en Python que permite calcular la huella de carbono de una empresa a partir de las emisiones generadas por sus actividades.

El sistema organiza las actividades por departamento y calcula las emisiones totales de la empresa.

## 2. Objetivo

Implementar un sistema que permita calcular y organizar las emisiones de carbono de una empresa mediante la programación orientada a objetos.

## 3. Funcionalidades principales

* Crear una empresa.
* Crear departamentos.
* Registrar actividades relacionadas con el consumo energético, el transporte y los residuos.
* Calcular las emisiones de cada actividad.
* Calcular la huella de carbono de cada departamento.
* Obtener la huella de carbono total de la empresa.

## 4. Tecnologías utilizadas

* Python 3.
* Programación Orientada a Objetos (POO).
* Módulo `unittest` para las pruebas unitarias.
* Visual Studio Code como entorno de desarrollo.

## 5. Estructura del proyecto

```text
GESTOR-CARBONO-CORPORATIVO/
├── docs/
├── src/
│   ├── actividades/
│   │   ├── actividad.py
│   │   ├── consumo_energetico.py
│   │   ├── transporte.py
│   │   └── residuos.py
│   ├── organizacion/
│   │   ├── departamento.py
│   │   └── empresa.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_actividades.py
│   └── test_organizacion.py
├── main.py
└── README.md
```

## 6. Requisitos

* Tener Python 3 instalado.
* Tener el proyecto descargado o clonado en la computadora.
* Contar con Visual Studio Code o una terminal para ejecutar los comandos.

No se requieren bibliotecas externas para la versión actual del proyecto.

## 7. Instrucciones de ejecución

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir una terminal desde el menú Terminal.
3. Verificar que la terminal se encuentre en la carpeta principal del proyecto.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

El programa mostrará las emisiones calculadas para cada actividad y la huella de carbono total de la empresa.

## 8. Ejecución de las pruebas unitarias

Desde la carpeta principal del proyecto, ejecutar:

```bash
python -m unittest discover -s tests -v
```

Este comando permite ejecutar las pruebas unitarias disponibles y mostrar sus resultados en la terminal.

## 9. Ejemplo de resultados

Con los datos de prueba configurados actualmente en `main.py`, se obtienen los siguientes resultados:

* Consumo eléctrico: 50.0
* Transporte laboral: 10.0
* Residuos generados: 2.0
* Huella de carbono total: 62.0

Los resultados se expresan en las unidades correspondientes a los factores de emisión utilizados en el programa.

## 10. Estado del proyecto

El proyecto cuenta con una implementación inicial de las clases principales, el cálculo de emisiones y pruebas unitarias para las actividades y la organización de la empresa.

Las funcionalidades adicionales y las mejoras pendientes se identificarán y documentarán conforme avance el desarrollo.
