from time import time

from epi_sigsa.src.session import get_action, get_file_name, get_session_data

from .src.data.handle_data import cargar_registros
from .src.paciente import Paciente
from .src.scrap import buscar_registros, cargar_pagina, ingresar


def main():
    """user = "jrodriguez"
    password = "3124"
    responsable = "YESI CRISTINA BARRUTIA"
    mes = "8"
    servicio = "(C/S) SAN JUAN ALOTENANGO" """

    # Obtener datos de la sesion
    user, password, responsable, mes, servicio = get_session_data()
    file_name = get_file_name()
    save_action = get_action()

    # cargar los registros
    registros = cargar_registros(file_name, servicio)

    # iniciar sigsa
    cargar_pagina(user, password, responsable, mes)

    for i in registros:
        paciente = Paciente(registros[i])
        print(paciente, paciente.clasificacion)
        encontrado = buscar_registros(paciente)
        if save_action and encontrado:
            ingresar(paciente.clasificacion, save=True, servicio=servicio)


if __name__ == "__main__":
    start = time()
    main()
    print(f"Elapsed time: {round((time() - start)/60, 4)} mins.")
