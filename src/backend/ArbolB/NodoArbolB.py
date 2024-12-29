from src.backend.entidades.Vehiculo import Vehiculo

class NodoArbolB:
    # Constructor de la clase
    def __init__(self, hoja=False):
        self.hoja: bool = hoja
        self.claves: list[Vehiculo] = []  # Lista de objetos Vehiculo
        self.hijos: list[NodoArbolB] = []  # Lista de nodos hijos

    def __str__(self):
        claves_str = ", ".join(str(clave.get_placa()) for clave in self.claves)
        return f"Hoja: {self.hoja}, Claves: [{claves_str}], Hijos: {len(self.hijos)}"

