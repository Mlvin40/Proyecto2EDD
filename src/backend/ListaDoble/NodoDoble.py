from src.backend.entidades.Cliente import Cliente
class NodoDoble:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente 
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"Cliente: {self.cliente}, Siguiente: {self.siguiente}, Anterior: {self.anterior}"
