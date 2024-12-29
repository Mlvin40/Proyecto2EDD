from .NodoDoble import NodoDoble
from src.backend.entidades.Cliente import Cliente

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño = 0

    def agregarElemento(self, cliente: Cliente):
        nuevo = NodoDoble(cliente)

        if self.estaVacia():
            self.inicio = nuevo
            self.fin = nuevo
        else:
            # Insertar manteniendo el orden por DPI
            actual = self.inicio
            while actual and actual.cliente.get_dpi() < cliente.get_dpi():
                actual = actual.siguiente

            if actual is None:
                self.fin.siguiente = nuevo
                nuevo.anterior = self.fin
                self.fin = nuevo
            else:
                # Insertar antes del nodo actual
                if actual == self.inicio:
                    nuevo.siguiente = self.inicio
                    self.inicio.anterior = nuevo
                    self.inicio = nuevo
                else:
                    actual.anterior.siguiente = nuevo
                    nuevo.anterior = actual.anterior
                    nuevo.siguiente = actual
                    actual.anterior = nuevo
        self.tamaño += 1

    def estaVacia(self):
        return self.tamaño == 0

    def eliminarUltimo(self):
        if self.estaVacia():
            raise Exception("La lista está vacía")
        
        if self.tamaño == 1:
            self.inicio = None
            self.fin = None
        else:
            self.fin = self.fin.anterior
            self.fin.siguiente = None
        self.tamaño -= 1

    def obtenerContenido(self, index):
        if self.estaVacia():
            raise Exception("La lista está vacía")
        
        if index < 0 or index >= self.tamaño:
            raise Exception("Índice fuera de rango")

        actual = self.inicio
        for i in range(index):
            actual = actual.siguiente
        return actual.cliente
    
    def __str__(self):
        clientes = []
        actual = self.inicio
        while actual:
            clientes.append(str(actual.cliente))
            actual = actual.siguiente
        return " <-> ".join(clientes)
    

    