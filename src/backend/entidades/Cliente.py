class Cliente:
    def __init__(self, dpi: int, nombres: str, apellidos: str, genero: str, telefono: int, direccion: str):
        self._dpi = dpi
        self._nombres = nombres
        self._apellidos = apellidos
        self._genero = genero
        self._telefono = telefono
        self._direccion = direccion

    # Métodos getter
    def get_dpi(self):
        return self._dpi

    def get_nombres(self):
        return self._nombres

    def get_apellidos(self):
        return self._apellidos

    def get_genero(self):
        return self._genero

    def get_telefono(self):
        return self._telefono

    def get_direccion(self):
        return self._direccion

    # Métodos setter
    def set_dpi(self, dpi: int):
        self._dpi = dpi

    def set_nombres(self, nombres: str):
        self._nombres = nombres

    def set_apellidos(self, apellidos: str):
        self._apellidos = apellidos

    def set_genero(self, genero: str):
        self._genero = genero

    def set_telefono(self, telefono: int):
        self._telefono = telefono

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def __str__(self):
        return f"{self._nombres} {self._apellidos} (DPI: {self._dpi})"
