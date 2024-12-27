class Cliente:
    # Todos los clientes deben de ser almacenados en una lista circular doblemente enlazada y ordenada por DPI 
    def __init__(self, dpi: int, nombres: str, apellidos: str, genero: str, telefono: int, direccion: str):
        self.dpi = dpi
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion

    

