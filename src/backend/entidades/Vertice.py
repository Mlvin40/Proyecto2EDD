from src.backend.Lista.Lista import Lista 

class Vertice:
    def __init__(self, valor: int):
        self.valor = valor
        self.vecinos = Lista()