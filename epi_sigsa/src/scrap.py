import time
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .data.dicts import (
    diagnostico_negativo,
    diagnostico_pcr,
    diagnostico_positivo,
)
from .ingresos import ingreso_na, ingreso_positivo
from .paciente import Paciente

# opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# urls
consulta_url = "https://sacatepequez.mspas.gob.gt/sigsa3/sigsa3consulta.aspx"
sigsa_url = (
    "https://sacatepequez.mspas.gob.gt/Login.aspx?ReturnUrl=%2fdefault.aspx"
)
sigsa3_url = "https://sacatepequez.mspas.gob.gt/Sigsa3/default.aspx"


def cargar_pagina(user, password, responsable, mes):
    try:
        # inicializar navegador
        driver_path = "../driver/chromedriver"
        global driver
        driver = webdriver.Chrome(driver_path, chrome_options=options)
        driver.get(sigsa_url)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "Login1_UserName"))
        ).send_keys(user)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "Login1_Password"))
        ).send_keys(password)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "Login1_LoginButton"))
        ).click()

        driver.get(sigsa3_url)

        # filtro de personal
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "ctl00$MainContent$TxtMes"))
        ).send_keys(mes)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "ctl00$MainContent$TxtAno"))
        ).send_keys("2021")
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.NAME, "ctl00$MainContent$Chktodo"))
        ).click()
        time.sleep(1)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_cmb_Responsable")
            )
        ).send_keys(responsable)
        time.sleep(1)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkFiltrar"))
        ).click()
        time.sleep(1)

        # editar registros del personal
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_GrdResul_ctl02_lnkEditar")
            )
        ).click()
        time.sleep(1)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkAgregar"))
        ).click()
        time.sleep(1)
    except TimeoutException as e:
        print(e)


def buscar_registros(paciente: Paciente):
    try:
        registros_dir = Path("registros")
        registros_dir.mkdir(exist_ok=True)
        time.sleep(1)
        # input dia
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtDia"))
        ).send_keys(paciente.dia_consulta)
        # boton buscar persona
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkBuscarP"))
        ).click()
        time.sleep(1)

        # inputs nombres
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtNombre1"))
        ).send_keys(paciente.primer_nombre)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtNombre2"))
        ).send_keys(paciente.segundo_nombre)

        # inputs apellidos
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_TxtApellido1")
            )
        ).send_keys(paciente.primer_apellido)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_TxtApellido2")
            )
        ).send_keys(paciente.segundo_apellido)
        # boton filtrar
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_lnkFiltrarP")
            )
        ).click()
        time.sleep(3)

        # primer resultado dxgvDataRow_PlasticBlue
        WebDriverWait(driver, 12).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "dxgvDataRow_PlasticBlue")
            )
        ).click()
        # guarda los nombres de los encontrados
        f = open("registros/ingresados.txt", "a")
        f.write("\n" + f"{paciente} - {paciente.clasificacion}")
        f.close()
        time.sleep(2)
        return True

    except TimeoutException:
        # sale si no encuentra personas
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_btnCancelarSeleccion")
            )
        ).click()
        # guarda los nombres de los no encontrados
        f = open("registros/no-ingresados.txt", "a")
        f.write("\n" + f"{paciente} - {paciente.clasificacion}")
        f.close()
        print(f"Persona no encontrada: {paciente}")
        time.sleep(1)
        # recargar pagina para evitar errores
        driver.get(consulta_url)
        return False


def ingresar(clasificacion: str, save: bool, servicio):
    try:
        if not servicio == "(C/S) SAN JUAN ALOTENANGO":
            isPs = True
        else:
            isPs = False
        if clasificacion == "Confirmado":
            for diagnosticos in diagnostico_positivo:
                motivo = diagnosticos["motivo"]
                medicamentos = diagnosticos["medicamentos"]
                if len(medicamentos) == 0:
                    ingreso_na(driver, motivo)
                    print(f"fin de diagnostico {motivo}")
                else:
                    ingreso_positivo(driver, motivo, medicamentos, isPs)
                    time.sleep(1)
                    print(f"fin de diagnostico {motivo}")

        if clasificacion == "Descartado":
            for diagnosticos in diagnostico_negativo:
                motivo = diagnosticos["motivo"]
                medicamentos = diagnosticos["medicamentos"]
                ingreso_na(driver, motivo)
                print(f"fin de diagnostico {motivo}")

        if clasificacion == "Sospechoso":
            for diagnosticos in diagnostico_pcr:
                motivo = diagnosticos["motivo"]
                medicamentos = diagnosticos["medicamentos"]
                ingreso_na(driver, motivo)
                print(f"fin de diagnostico {motivo}")
        time.sleep(2)

        if save:
            """GUARDAR"""
            # aboton guardar ID ctl00_MainContent_LnkGrabarC
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.ID, "ctl00_MainContent_LnkGrabarC")
                )
            ).click()
            print("consulta guardada!")
            time.sleep(2)
        # recargar pagina para evitar errores
        driver.get(consulta_url)

    except TimeoutException as e:
        print(f"Persona no ingresada", e)
