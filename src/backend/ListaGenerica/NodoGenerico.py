from typing import Generic, TypeVar

T = TypeVar('T')  # Declaración del tipo genérico

class NodoGenerico(Generic[T]):
    def __init__(self, valor: T):
        self._valor = valor
        self._siguiente = None

    def get_valor(self) -> T:
        return self._valor

    def set_valor(self, valor: T):
        self._valor = valor

    def get_siguiente(self) -> 'NodoGenerico[T]':
        return self._siguiente

    def set_siguiente(self, siguiente: 'NodoGenerico[T]'):
        self._siguiente = siguiente
