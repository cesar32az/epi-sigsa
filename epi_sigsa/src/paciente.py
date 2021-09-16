class Paciente:
    def __init__(self, data):
        self.data = data
        self.fecha = data["fecha_tomo_muestra"]
        self.no_reg = data["ficha_registro"]
        self.direccion = data["direccion"]
        self.municipio = data["municipio"]
        self.clasificacion = data["clasificacion"]
        self.edad = data["edad_anios"]
        self.municipio = data["municipio"]
        self.direccion = data["direccion"]

    def get_full_nombres(self):
        return list(filter(lambda x: x, self.data["nombres"].split(" ")))

    @property
    def primer_nombre(self):
        return self.get_full_nombres()[0]

    @property
    def segundo_nombre(self):
        full_names = self.get_full_nombres()
        if len(full_names) > 1:
            segundo_nombre = full_names[-1]
        else:
            segundo_nombre = ""
        return segundo_nombre

    def get_full_apellidos(self):
        return list(filter(lambda x: x, self.data["apellidos"].split(" ")))

    @property
    def primer_apellido(self):
        return self.get_full_apellidos()[0]

    @property
    def segundo_apellido(self):
        full_apellidos = self.get_full_apellidos()
        if len(full_apellidos) > 1:
            segundo_apellido = full_apellidos[-1]
        else:
            segundo_apellido = ""
        return segundo_apellido

    @property
    def dia_consulta(self):
        return self.fecha.split("/")[0]

    def __str__(self) -> str:
        return f"{self.primer_nombre} {self.segundo_nombre}, {self.primer_apellido} {self.segundo_apellido} - Edad: {self.edad}, direccion: {self.direccion} {self.municipio}"
