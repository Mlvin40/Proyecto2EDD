from .NodoArbolB import NodoArbolB
from src.backend.entidades.Vehiculo import Vehiculo

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

    def dividir_pagina(self, nodo: NodoArbolB, posicion: int):
        posicion_media: int = (self.orden - 1) // 2

        hijo: NodoArbolB = nodo.hijos[posicion]
        nuevo_hijo: NodoArbolB = NodoArbolB(hijo.hoja)

        # Mover claves y nodos hijos
        nodo.hijos.insert(posicion + 1, nuevo_hijo)
        nodo.claves.insert(posicion, hijo.claves[posicion_media])

        nuevo_hijo.claves = hijo.claves[posicion_media + 1:]
        hijo.claves = hijo.claves[:posicion_media]

        if not hijo.hoja:
            nuevo_hijo.hijos = hijo.hijos[posicion_media + 1:]
            hijo.hijos = hijo.hijos[:posicion_media + 1]

    def generar_graphviz(self) -> str:
        """
        Genera el código Graphviz para representar el árbol B.
        """
        def recorrer_nodos(nodo: NodoArbolB, contador: list) -> (str, str):
            if nodo is None:
                return "", ""

            nodo_id = f"n{contador[0]}"
            contador[0] += 1
            etiquetas = f'{nodo_id} [label = "'

            for i, vehiculo in enumerate(nodo.claves):
                etiquetas += f'<f{i}>{vehiculo.get_placa()} | '
            etiquetas = etiquetas.rstrip(' | ') + '"];\n'

            conexiones = ""
            if not nodo.hoja:
                for i, hijo in enumerate(nodo.hijos):
                    hijo_id = f"n{contador[0]}"
                    sub_etiquetas, sub_conexiones = recorrer_nodos(hijo, contador)
                    etiquetas += sub_etiquetas
                    conexiones += sub_conexiones
                    conexiones += f'{nodo_id}:f{i} -> {hijo_id};\n'

            return etiquetas, conexiones

        contador = [0]
        etiquetas, conexiones = recorrer_nodos(self.raiz, contador)
        return f'digraph G {{\nnode [shape = record];\n{etiquetas}{conexiones}}}'