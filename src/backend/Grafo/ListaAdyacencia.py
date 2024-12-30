from src.backend.Lista.Lista import Lista
from src.backend.entidades.Vertice import Vertice
from src.backend.entidades.Ruta import Ruta
from src.backend.Lista.Nodo import Nodo
import os 
from graphviz import Digraph

#Debe de tener una lista enlazada de tipo vertices
#Debe de tener un metodo insertar que reciba una ruta

class ListaAdyacencia:
    def __init__(self):
        self.vertices: Lista[Vertice] = Lista();
    
    # metodo get de vertices
    def get_vertices(self):
        return self.vertices;
    
    def insertar(self, ruta: Ruta):

        origen: Vertice = Vertice(ruta.get_lugar_origen());
        destino: Vertice = Vertice(ruta.get_lugar_destino(), ruta.get_tiempo_de_ruta());

        resultado: Nodo[Vertice] = self.vertices.buscar(origen);

        if(resultado != None):
            resultado.valor.vecinos.insertar_final(destino);
        else:
            resultado= self.vertices.insertar_final(origen);
            resultado.valor.vecinos.insertar_final(destino);

    def imprimir(self):
        dot = 'digraph G {\n\t edge[arrowhead=none fontcolor=black color ="ff5400"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style =filled, fillcolor="#313638", fontcolor=yellow;\n\t'
        dot += 'color=transparent];\n\t';

        aux: Nodo[Vertice] = self.vertices.cabeza;

        while aux != None:
            if aux != None:
                dot += str(aux.valor);

            aux = aux.siguiente;

        dot += "}";

        return dot;

    def generar_graphviz(self):
        dot: str = self.imprimir()
        ruta_dot = 'Grafo.txt'

        # Guardar el contenido DOT en un archivo en el directorio actual
        with open(ruta_dot, 'w') as file:
            file.write(dot)

        resultadoPNG = os.system(f"neato -Tpng {ruta_dot} -o Grafo.png")
        resultadoPDF = os.system(f"neato -Tpdf {ruta_dot} -o Grafo.pdf")

        if resultadoPNG == 0 and resultadoPDF == 0:
            print("Reporte generado exitosamente!!!")
        else:
            print("Hubo un error al generar el reporte.")

