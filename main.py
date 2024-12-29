from src.backend.ArbolB.ArbolB import ArbolB
from src.backend.entidades.Vehiculo import Vehiculo
from src.backend.ListaDoble.ListaDobleEnlazada import ListaDobleEnlazada
from src.backend.entidades.Cliente import Cliente
from src.backend.ListaGenerica.ListaEnlazadaGenerica import ListaEnlazadaGenerica
from src.backend.Grafo.ListaAdyacencia import ListaAdyacencia
from src.backend.entidades.Vertice import Vertice


from src.backend.entidades.Reader import Reader

def main() -> None:

    # Prueba de Arbol B

    arbol_vehiculos = ArbolB(5);
    lista_clientes = ListaDobleEnlazada();
    lector = Reader(lista_clientes, arbol_vehiculos, None)

                       
    lector.carga_masiva_vehiculos("Vehiculos.txt")
    lector.carga_masiva_clientes("Clientes.txt")

    import subprocess

    # Escribe el archivo DOT
    string = arbol_vehiculos.generar_graphviz()
    with open("arbolB.dot", "w") as file:
        file.write(string)

    # Genera el archivo PDF con Graphviz
    try:
        subprocess.run(["dot", "-Tpdf", "arbolB.dot", "-o", "arbolB.pdf"], check=True)
        print("Archivo PDF generado exitosamente: arbolB.pdf")
    except FileNotFoundError:
        print("Error: Graphviz no está instalado o no se encuentra en el PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error al generar el PDF: {e}")

if __name__ == "__main__":
    main()