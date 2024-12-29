from src.backend.Lista.Lista import Lista
#Debe de tener una lista enlazada de tipo vertices

class ListaAdyacencia:
    def __init__(self):
        self.vertices: Lista = Lista();
    
    def insertar(self, origen, destino):
        resultado = self.vertices.buscar(origen);

        if(resultado != None):
            resultado.valor.vecinos.insertar_final(destino);
        else:
            resultado= self.vertices.insertar_final(origen);

            resultado.valor.vecinos.insertar_final(destino);