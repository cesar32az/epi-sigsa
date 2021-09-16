from .scrap import *


def ingreso_na(driver, motivo):
    try:
        # boton agregar motivo de consulta ID ctl00_MainContent_lnkNuevoD
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkNuevoD"))
        ).click()
        time.sleep(2)

        # input cie 10 set keys ID ctl00_MainContent_TxtIdCie
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtIdCie"))
        ).send_keys(motivo)

        # boton filtrar motivo ID ctl00_MainContent_lnkFiltrarD
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_lnkFiltrarD")
            )
        ).click()
        time.sleep(2)

        # motivo encontrado classname dxgvDataRow_PlasticBlue
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//table[@id='ctl00_MainContent_GrdBuscaD']/tbody/tr[1]",
                )
            )
        ).click()
        time.sleep(3)

        # boton agregar medicamento ID ctl00_MainContent_lnkNuevoM
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkNuevoM"))
        ).click()
        time.sleep(2)

        # checkbox no aplica ID ctl00_MainContent_Chk_noaplica
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.ID, "ctl00_MainContent_Chk_noaplica")
            )
        ).click()
        time.sleep(2)
        print(f"ingresado {motivo}")
        print("n/a")
    except TimeoutException as e:
        print(e)


def agregar_medicamentos(driver, medicamentos, isPs):
    for medicamento in medicamentos:
        nombre = medicamento["nombre"]
        presentacion = medicamento["presentacion"]
        concentracion = medicamento["concentracion"]
        cantidad = medicamento["cantidad"]
        try:
            # boton agregar medicamento ID ctl00_MainContent_lnkNuevoM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_lnkNuevoM")
                )
            ).click()
            time.sleep(2)

            # Buscar medicamento Id ctl00_MainContent_lnkBuscarM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_lnkBuscarM")
                )
            ).click()
            time.sleep(2)

            # input nombre medicamento ID ctl00_MainContent_TxtBusDescripcionM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_TxtBusDescripcionM")
                )
            ).send_keys(nombre)

            # input presentacion medicamento ID ctl00_MainContent_TxtBusPresentacionM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_TxtBusPresentacionM")
                )
            ).send_keys(presentacion)

            # input concentracion medicamento ID ctl00_MainContent_TxtBusConcentracionM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_TxtBusConcentracionM")
                )
            ).send_keys(concentracion)
            time.sleep(1)

            # boton filtrar medicamento ID ctl00_MainContent_lnkFiltrarM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_lnkFiltrarM")
                )
            ).click()
            time.sleep(3)

            # motivo encontrado classname dxgvDataRow_PlasticBlue
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//table[@id='ctl00_MainContent_GrdBuscaM']/tbody/tr[1]",
                    )
                )
            ).click()
            time.sleep(1)

            # input cantidad medicamento ID ctl00_MainContent_TxtCantidadM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_TxtCantidadM")
                )
            ).send_keys(cantidad)
            if isPs:
                # input cantidad medicamento ID ctl00_MainContent_TxtCantidadM
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(
                        (By.ID, "ctl00_MainContent_TxtCantNoEntM")
                    )
                ).send_keys("0")

            # boton guardar medicamento ID ctl00_MainContent_lnkGrabarM
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.ID, "ctl00_MainContent_lnkGrabarM")
                )
            ).click()
            time.sleep(2)
            print(f"fin medicamento {nombre}")
        except TimeoutException as e:
            print(f"error en el medicamento {nombre} ", e)


def ingreso_positivo(driver, motivo, medicamentos, isPs):
    try:

        # boton agregar motivo de consulta ID ctl00_MainContent_lnkNuevoD
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkNuevoD"))
        ).click()
        time.sleep(1)
        # input cie 10 set keys ID ctl00_MainContent_TxtIdCie
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtIdCie"))
        ).send_keys(motivo)
        time.sleep(1)
        # boton filtrar motivo ID ctl00_MainContent_lnkFiltrarD
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_lnkFiltrarD")
            )
        ).click()
        time.sleep(3)
        # motivo encontrado classname dxgvDataRow_PlasticBlue
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//table[@id='ctl00_MainContent_GrdBuscaD']/tbody/tr[1]",
                )
            )
        ).click()
        time.sleep(2)

        agregar_medicamentos(driver, medicamentos, isPs)

    except TimeoutException as e:
        print(e)
