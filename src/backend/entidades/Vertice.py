from src.backend.Lista.Lista import Lista 

class Vertice:
    def __init__(self, valor: str, peso: int = 0):
        self.valor:str = valor;
        self.vecinos: Lista[Vertice] = Lista();
        self.peso: int = peso;

    def __str__(self):
        aux = self.vecinos.cabeza;

        dot: str = "";

        while aux != None:
            dot += f'edge[label={aux.valor.peso} fontsize = 5]; \n\t {self.valor} -> {aux.valor.valor};\n\t';
            aux = aux.siguiente;

        return dot;