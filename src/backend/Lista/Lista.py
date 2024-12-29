from .Nodo import Nodo
class Lista:
    def __init__(self):
        self.cabeza: Nodo = None

    def insertar_final(self, valor) -> Nodo:
        
        aux: Nodo = self.cabeza;

        if aux == None:
             aux = Nodo(valor);
             self.cabeza = aux;
             return aux;

        while aux.siguiente != None:
            aux = aux.siguiente;

        aux.siguiente = Nodo(valor);
        return aux.siguiente;

    def buscar(self, valor) -> Nodo:

        aux: Nodo = self.cabeza;

        if aux == None:
            return None

        while aux != None:

            if aux.valor.valor == valor.valor:
                return aux;
        
            aux = aux.siguiente;

        return None;

