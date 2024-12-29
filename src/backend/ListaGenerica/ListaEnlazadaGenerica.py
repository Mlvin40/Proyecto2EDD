from typing import Generic, TypeVar
from .NodoGenerico import NodoGenerico

T = TypeVar('T') 

class ListaEnlazadaGenerica(Generic[T]):
    def __init__(self):
        self._inicio = None
        self._fin = None
        self._tamaño = 0

    # Método para agregar un elemento al final
    def agregar_elemento(self, valor: T):
        nuevo = NodoGenerico(valor)
        if self.esta_vacia():
            self._inicio = nuevo
            self._fin = nuevo
        else:
            self._fin.set_siguiente(nuevo)
            self._fin = nuevo
        self._tamaño += 1

    def agregar_elemento_en(self, index: int, valor: T):
        if index < 0 or index > self._tamaño:
            raise IndexError("Índice fuera de rango")

        nuevo = NodoGenerico(valor)
        if index == 0:  # Insertar al inicio
            nuevo.set_siguiente(self._inicio)
            self._inicio = nuevo
            if self._tamaño == 0:  # Si la lista estaba vacía
                self._fin = nuevo
        else:
            anterior = self.obtener_nodo(index - 1)
            nuevo.set_siguiente(anterior.get_siguiente())
            anterior.set_siguiente(nuevo)
            if nuevo.get_siguiente() is None:  # Si se inserta al final
                self._fin = nuevo
        self._tamaño += 1

    # Método para obtener el valor en un índice específico
    def obtener_valor(self, index: int) -> T:
        return self.obtener_nodo(index).get_valor()

    # Método para obtener el nodo en un índice específico
    def obtener_nodo(self, index: int) -> NodoGenerico[T]:
        if index < 0 or index >= self._tamaño:
            raise IndexError("Índice fuera de rango")
        actual = self._inicio
        for _ in range(index):
            actual = actual.get_siguiente()
        return actual

    # Método para eliminar el último elemento
    def eliminar_ultimo(self) -> T:
        if self.esta_vacia():
            raise Exception("La lista está vacía")
        if self._tamaño == 1:  # Si solo hay un elemento
            valor = self._inicio.get_valor()
            self._inicio = None
            self._fin = None
        else:
            penultimo = self.obtener_nodo(self._tamaño - 2)
            valor = self._fin.get_valor()
            penultimo.set_siguiente(None)
            self._fin = penultimo
        self._tamaño -= 1
        return valor

    # Método para verificar si la lista está vacía
    def esta_vacia(self) -> bool:
        return self._tamaño == 0

    def get_tamaño(self) -> int:
        return self._tamaño
