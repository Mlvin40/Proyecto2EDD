from src.backend.entidades.Viaje import Viaje
from src.backend.ListaGenerica.ListaEnlazadaGenerica import ListaEnlazadaGenerica
import os

class ReporteViajes:
    def __init__(self, lista_viajes: ListaEnlazadaGenerica[Viaje]):
        self.viajes = lista_viajes;

    def mostrar_graphviz(self):
        # Creación del archivo DOT
        archivo_dot = "reporte_viajes.dot"
        with open(archivo_dot, 'w') as archivo:
            archivo.write("digraph Viajes {\n")
            archivo.write("    rankdir=LR;\n")
            archivo.write("    node [shape=record];\n")

            # Verificar si la lista está vacía
            if not self.viajes._inicio:
                archivo.write("    NodoVacio [label=\"Lista vacía\"];\n")
            else:
                actual = self.viajes._inicio
                while actual:
                    viaje = actual.get_valor()
                    # Crear nodo para el viaje con sus detalles
                    viaje_info = f"Viaje {viaje.get_id()}: {viaje.get_origen()} -> {viaje.get_destino()}"
                    archivo.write(f'    "{viaje_info}" [label="{viaje_info}"];\n')

                    # Conectar con el siguiente nodo si existe
                    if actual.get_siguiente():
                        siguiente_viaje = actual.get_siguiente().get_valor()
                        siguiente_info = f"Viaje {siguiente_viaje.get_id()}: {siguiente_viaje.get_origen()} -> {siguiente_viaje.get_destino()}"
                        archivo.write(f'    "{viaje_info}" -> "{siguiente_info}";\n')

                    actual = actual.get_siguiente()

            archivo.write("}\n")

        resultadoPDF = os.system(f"dot -Tpdf {archivo_dot} -o Viajes.pdf")
        resultadoPNG = os.system(f"dot -Tpng {archivo_dot} -o Viajes.png")

        if resultadoPDF == 0 and resultadoPNG == 0:
            print("Reporte generado exitosamente en PDF y PNG.")
        else:
            if resultadoPDF != 0:
                print("Error al generar el PDF.")
            if resultadoPNG != 0:
                print("Error al generar el PNG.")