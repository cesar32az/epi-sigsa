from pathlib import Path

from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator, PathValidator


def get_session_data():
    check = False
    while not check:
        user = inquirer.text(
            message="Ingresa tu usuario:",
            completer={"jrodriguez": None, "jgomez": None, "lmorales": None},
            multicolumn_complete=True,
        ).execute()
        password = inquirer.secret(
            message="Ingresa tu contraseña:",
            transformer=lambda _: "[hidden]",
        ).execute()
        responsable = inquirer.text(
            message="Ingresa al responsable:"
        ).execute()
        mes = inquirer.text(
            message="Ingresa el mes:",
            validate=NumberValidator(),
        ).execute()
        servicio = inquirer.select(
            message="Selecciona el servicio:",
            choices=["(C/S) SAN JUAN ALOTENANGO", "(P/S) CIUDAD VIEJA"],
            default=None,
        ).execute()
        print(f"usuario: {user}")
        print(f"responsable: {responsable}")
        print(f"mes: {mes}")
        print(f"servicio: {servicio}")
        check = inquirer.confirm(
            message="Sus datos son correctos?", default=True
        ).execute()
    return user, password, responsable, mes, servicio


def get_action() -> bool:
    print(
        "Asegurese de que todos los pacientes esten ingresados correctamente"
    )
    action = inquirer.select(
        message="Selecciona la acción que desea realizar:",
        choices=[
            {"name": "Buscar pacientes", "value": False},
            {"name": "Ingresar pacientes", "value": True},
        ],
        default=None,
    ).execute()
    return action


def get_file_name():
    p = Path(".")
    files = list(p.glob("*.xlsx"))
    file_name = inquirer.select(
        message="Selecciona el reporte:",
        choices=files,
        default=None,
    ).execute()
    return file_name
