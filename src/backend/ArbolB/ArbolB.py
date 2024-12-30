from .NodoArbolB import NodoArbolB
from src.backend.entidades.Vehiculo import Vehiculo
import os

class ArbolB:
    # Constructor de la clase
    def __init__(self, orden: int):
        self.raiz: NodoArbolB = NodoArbolB(True)  # Nodo raíz inicial
        self.orden: int = orden  # Orden del árbol B

    def insertar_valor(self, vehiculo: Vehiculo):
        raiz: NodoArbolB = self.raiz
        self.insertar_valor_no_completo(raiz, vehiculo)
        if len(raiz.claves) > self.orden - 1:  # Si la raíz se llena, se divide
            nodo: NodoArbolB = NodoArbolB()
            self.raiz = nodo
            nodo.hijos.insert(0, raiz)
            self.dividir_pagina(nodo, 0)

    def insertar_valor_no_completo(self, nodo: NodoArbolB, vehiculo: Vehiculo):
        posicion: int = len(nodo.claves) - 1

        if nodo.hoja:
            # Insertar en la posición correcta
            nodo.claves.append(None)
            while posicion >= 0 and vehiculo.get_placa() < nodo.claves[posicion].get_placa():
                nodo.claves[posicion + 1] = nodo.claves[posicion]
                posicion -= 1
            nodo.claves[posicion + 1] = vehiculo
        else:
            # Buscar hijo adecuado
            while posicion >= 0 and vehiculo.get_placa() < nodo.claves[posicion].get_placa():
                posicion -= 1

            posicion += 1
            self.insertar_valor_no_completo(nodo.hijos[posicion], vehiculo)
            if len(nodo.hijos[posicion].claves) > self.orden - 1:
                self.dividir_pagina(nodo, posicion)

    def dividir_pagina(self, raiz: NodoArbolB, posicion: int):
        posicion_media: int = int((self.orden - 1) / 2);

        hijo: NodoArbolB = raiz.hijos[posicion]
        nodo: NodoArbolB = NodoArbolB(hijo.hoja)

        # Mover claves y nodos hijos
        raiz.hijos.insert(posicion + 1, nodo);
        raiz.claves.insert(posicion, hijo.claves[posicion_media]);

        nodo.claves = hijo.claves[posicion_media +1: posicion_media* 2 + 1:];
        hijo.claves = hijo.claves[0:posicion_media];

        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media + 1: posicion_media *2 + 2]
            hijo.hijos = hijo.hijos[:posicion_media + 1];
    
    def buscar(self, placa: str, nodo: NodoArbolB = None) -> Vehiculo:
        #Busca un vehículo en el árbol B por su placa.
        if nodo is None:
            nodo = self.raiz

        # Buscar la placa en las claves del nodo actual
        for clave in nodo.claves:
            if clave.get_placa() == placa:
                return clave
            
        # Si el nodo es una hoja, no se encontró la placa
        if nodo.hoja:
            return None

        # Buscar en el hijo correspondiente
        i = 0
        while i < len(nodo.claves) and placa > nodo.claves[i].get_placa():
            i += 1

        return self.buscar(placa, nodo.hijos[i])
    
    # Métodos de reporte
    def generar_graphviz(self) -> None:
        # Generacion del reporte del arbol

        dot: str = '''digraph G {
                fontcolor=white;
                nodesep=0.5;
                splines=false;
                node [shape=record width=1.2 style=filled fillcolor="#313638" fontcolor=white];
                edge [fontcolor=white color="#0070c9"];
        '''
        dot += self.__imprimir_contenido(self.raiz)
        dot += "\n}"
        ruta_dot = 'ArbolB.txt'

        with open(ruta_dot, 'w') as file:
            file.write(dot)

        resultadoPNG = os.system(f"dot -Tpng {ruta_dot} -o ArbolB.png")
        resultadoPDF = os.system(f"dot -Tpdf {ruta_dot} -o ArbolB.pdf")

        if resultadoPNG == 0 and resultadoPDF == 0:
            print("Reporte generado exitosamente!!!")
        else:
            print("Hubo un error al generar el reporte.")

    def __imprimir_contenido(self, nodo: NodoArbolB, id: list[int] = [0]) -> str:
        """
        Genera la representación en formato DOT del árbol B.
        """
        raiz_sub_arbol: NodoArbolB = nodo
        contenido_arbol = f'n{id[0]}[label="'
        contador: int = 0
        for clave in raiz_sub_arbol.claves:
            if contador == len(raiz_sub_arbol.claves) - 1:
                contenido_arbol += f"<f{contador}>|{clave.get_placa()}|<f{contador + 1}>"
                break
            contenido_arbol += f"<f{contador}>|{clave.get_placa()}|"
            contador += 1
        contenido_arbol += '"];\n\t'

        contador = 0
        id_padre = id[0]
        for sub_nodo in raiz_sub_arbol.hijos:
            contenido_arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
            id[0] += 1
            contenido_arbol += self.__imprimir_contenido(sub_nodo, id)
            contador += 1

        return contenido_arbol