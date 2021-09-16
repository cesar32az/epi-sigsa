import fnmatch
import os
from pathlib import Path

import pandas as pd


def cargar_registros(filename, servicio):
    root_path = Path(".")
    for file in os.listdir(root_path):
        if fnmatch.fnmatch(file, filename):
            df = pd.read_excel(file, sheet_name=0, skiprows=[0, 1])
            in_servicio = df["servicio"] == servicio
            registros = df[in_servicio]
            # print(registros.head())
            registros = registros.to_dict("index")
            return registros


# registros = cargar_registros('data.xlsx', '(C/S) SAN JUAN ALOTENANGO')
