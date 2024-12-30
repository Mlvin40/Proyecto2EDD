from src.backend.ArbolB.ArbolB import ArbolB
from src.backend.entidades.Vehiculo import Vehiculo
from src.backend.ListaDoble.ListaDobleEnlazada import ListaDobleEnlazada
from src.backend.entidades.Cliente import Cliente
from src.backend.ListaGenerica.ListaEnlazadaGenerica import ListaEnlazadaGenerica
from src.backend.Grafo.ListaAdyacencia import ListaAdyacencia
from src.backend.entidades.Vertice import Vertice

from src.backend.entidades.Reader import Reader
from src.backend.entidades.Ruta import Ruta

def main() -> None:

    # Prueba de Arbol B
    arbol_vehiculos = ArbolB(5);
    lista_clientes = ListaDobleEnlazada();
    lista_rutas: list[Ruta] = [];

    listaAdyacencia = ListaAdyacencia();
    lector = Reader(lista_clientes, arbol_vehiculos, lista_rutas);

    lector.carga_masiva_vehiculos("Vehiculos.txt")
    lector.carga_masiva_clientes("Clientes.txt")
    lector.carga_masiva_rutas("Rutas.txt")

    # agregar todos los objetos de la lista de rutas al grafo
    for ruta in lista_rutas:
        listaAdyacencia.insertar(ruta);
    
    # generar el archivo de graphviz
    str = listaAdyacencia.imprimir();

    print(str);
    arbol_vehiculos.generar_graphviz();
    listaAdyacencia.generar_graphviz();



if __name__ == "__main__":
    main()