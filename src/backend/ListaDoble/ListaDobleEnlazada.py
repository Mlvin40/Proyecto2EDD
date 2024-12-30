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

    def obtenerContenido(self, index):
        if self.estaVacia():
            raise Exception("La lista está vacía")
        
        if index < 0 or index >= self.tamaño:
            raise Exception("Índice fuera de rango")

        actual = self.inicio
        for i in range(index):
            actual = actual.siguiente
        return actual.cliente
    
    def buscar_cliente(self, dpi: int):
        if self.estaVacia():
            raise Exception("La lista está vacía")

        actual = self.inicio
        while actual:
            if actual.cliente.get_dpi() == dpi:
                return actual.cliente  # Retorna el cliente si lo encuentra
            actual = actual.siguiente
        return None  # Si no lo encuentra, retorna None
    
    def eliminar_cliente(self, dpi: int):
        if self.estaVacia():
            raise Exception("La lista está vacía")

        actual = self.inicio

        # Si el cliente a eliminar está al inicio de la lista
        if actual.cliente.get_dpi() == dpi:
            if actual.siguiente:  # Si hay un siguiente nodo
                self.inicio = actual.siguiente
                self.inicio.anterior = None
            else:  # Si el nodo es el único en la lista
                self.inicio = None
                self.fin = None
            self.tamaño -= 1
            return

        # Buscar el cliente a eliminar en el resto de la lista
        while actual:
            if actual.cliente.get_dpi() == dpi:
                # Si lo encuentra, actualiza las referencias de los nodos adyacentes
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente

                # Si es el último nodo
                if actual == self.fin:
                    self.fin = actual.anterior

                self.tamaño -= 1
                return
            actual = actual.siguiente

        raise Exception("Cliente no encontrado")  # Si no se encuentra el cliente


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
                #apuntar el nodo inicial anterior al final y el nodo final siguiente al inicio
                archivo.write(f'    "{self.inicio.cliente.get_nombres()} {self.inicio.cliente.get_apellidos()} (DPI: {self.inicio.cliente.get_dpi()})" -> "{self.fin.cliente.get_nombres()} {self.fin.cliente.get_apellidos()} (DPI: {self.fin.cliente.get_dpi()})" ;\n')
                archivo.write(f'    "{self.fin.cliente.get_nombres()} {self.fin.cliente.get_apellidos()} (DPI: {self.fin.cliente.get_dpi()})" -> "{self.inicio.cliente.get_nombres()} {self.inicio.cliente.get_apellidos()} (DPI: {self.inicio.cliente.get_dpi()})" ;\n')

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