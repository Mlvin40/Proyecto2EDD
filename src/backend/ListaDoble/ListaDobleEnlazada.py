from .NodoDoble import NodoDoble
from src.backend.entidades.Cliente import Cliente
from graphviz import Digraph
import os

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño = 0

    def agregarElemento(self, cliente: Cliente):
        nuevo = NodoDoble(cliente)

        if self.estaVacia():
            # Si la lista está vacía, el nuevo nodo es el inicio y el fin
            self.inicio = nuevo
            self.fin = nuevo
        else:
            actual = self.inicio
            # Encontrar la posición donde insertar el nuevo nodo
            while actual and actual.cliente.get_dpi() < cliente.get_dpi():
                actual = actual.siguiente

            if actual == self.inicio:  # Insertar al inicio
                nuevo.siguiente = self.inicio
                self.inicio.anterior = nuevo
                self.inicio = nuevo
            elif actual is None:  # Insertar al final
                nuevo.anterior = self.fin
                self.fin.siguiente = nuevo
                self.fin = nuevo
            else:  # Insertar en el medio
                nuevo.siguiente = actual
                nuevo.anterior = actual.anterior
                actual.anterior.siguiente = nuevo
                actual.anterior = nuevo

        self.tamaño += 1

    def estaVacia(self):
        return self.tamaño == 0

    def eliminarUltimo(self):
        if self.estaVacia():
            raise Exception("La lista está vacía")
        
        if self.tamaño == 1:
            self.inicio = None
            self.fin = None
        else:
            self.fin = self.fin.anterior
            self.fin.siguiente = None
        self.tamaño -= 1

    def obtenerContenido(self, index):
        if self.estaVacia():
            raise Exception("La lista está vacía")
        
        if index < 0 or index >= self.tamaño:
            raise Exception("Índice fuera de rango")

        actual = self.inicio
        for i in range(index):
            actual = actual.siguiente
        return actual.cliente
    
    def __str__(self):
        clientes = []
        actual = self.inicio
        while actual:
            clientes.append(str(actual.cliente))
            actual = actual.siguiente
        return " <-> ".join(clientes)
    

    #Este reporte si funciona 
    def generar_reporte_graphviz(self):
        # Creación del archivo DOT
        archivo_dot = "reporte_clientes.dot"
        with open(archivo_dot, 'w') as archivo:
            archivo.write("digraph Clientes {\n")
            archivo.write("    rankdir=LR;\n")
            archivo.write("    node [shape=record];\n")

            if self.estaVacia():
                archivo.write("    NodoVacio [label=\"Lista vacía\"];\n")
            else:
                actual = self.inicio
                while actual:
                    cliente = actual.cliente
                    # Crear cada nodo con los detalles del cliente (DPI, nombre y apellido)
                    cliente_info = f"{cliente.get_nombres()} {cliente.get_apellidos()} (DPI: {cliente.get_dpi()})"
                    archivo.write(f'    "{cliente_info}" [label="{cliente_info}"];\n')

                    # Realizar las respectivas conexiones con los nodos 
                    if actual.siguiente:
                        archivo.write(f'    "{cliente_info}" -> "{actual.siguiente.cliente.get_nombres()} {actual.siguiente.cliente.get_apellidos()} (DPI: {actual.siguiente.cliente.get_dpi()})" ;\n')
                    if actual.anterior:
                        archivo.write(f'    "{cliente_info}" -> "{actual.anterior.cliente.get_nombres()} {actual.anterior.cliente.get_apellidos()} (DPI: {actual.anterior.cliente.get_dpi()})" ;\n')
                    actual = actual.siguiente
            archivo.write("}\n")
        
        # Generar los archivos PDF y PNG
        resultadoPDF = os.system(f"dot -Tpdf {archivo_dot} -o Clientes.pdf")
        resultadoPNG = os.system(f"dot -Tpng {archivo_dot} -o Clientes.png")

        if resultadoPDF == 0 and resultadoPNG == 0:
            print("Reporte generado exitosamente en PDF y PNG.")
        else:
            if resultadoPDF != 0:
                print("Error al generar el PDF.")
            if resultadoPNG != 0:
                print("Error al generar el PNG.")