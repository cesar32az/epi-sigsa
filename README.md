# EPI-SIGSA
Ingreso automatico de fichas de epiweb a sigsa3

## Features

- Ingreso de pacientes negativos
  - cie U:07:1
- Ingreso de pacientes sospechosos
  - cie z:20:8
  - cie z:11:5
- Ingreso de pacientes positivos
  - cie U:07:1
  - cie U:07:4
  - Ingreso de medicamento

## Requisitos

- Python 3.9^
- poetry
- git
- web driver de chrome

## Instalación

### Instalar poetry
> (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

Más información sobre poetry: https://python-poetry.org/docs/#installation

### Clonar el repositorio

> git clone https://github.com/cesar32az/epi-sigsa.git

### Instalar dependencias

> poetry install


## Preparar los datos

- Descargar el reporte de epiweb
- Mover el reporte a la carpeta epi_sigsa, junto al main.py
- Eliminar los registros que no correspondan al puesto o las fechas que se van a ingresar

## Correr el proyecto

> poetry run dev

#### Nota
Asegurarse de tener el web driver de chrome en una carpeta llamada driver afuera del proyecto

```
├── driver
│   └── chromedriver
└── epi_sigsa
    └── epi_sigsa
        ├── __init__.py
        ├── main.py
        └── src
             └── data

```
