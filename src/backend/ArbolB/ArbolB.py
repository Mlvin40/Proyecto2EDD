from .NodoArbolB import NodoArbolB

class ArbolB:
    # Constructor de la clase   
    def __init__(self, orden: int):
        self.raiz: NodoArbolB = NodoArbolB(True)  # este es el nodo raíz
        self.orden: int = orden  # este es el valor de m
    
    def insertar_valor(self, valor: int):
        raiz : NodoArbolB = self.raiz;
        self.insertar_valor_no_completo(raiz, valor);
        if (len(raiz.claves) > self.orden - 1): # Si la raíz se llena, se divide
            nodo: NodoArbolB = NodoArbolB();   
            self.raiz = nodo;
            nodo.hijos.insert(0, raiz);
            self.dividir_pagina(nodo, 0);

    def insertar_valor_no_completo(self, raiz: NodoArbolB, valor: int):
        posicion: int = len(raiz.claves) - 1; # Esto es para recorrer las claves del nodo
    
        if (raiz.hoja):
            # Si es una hoja, se inserta la clave en la posición correcta
            raiz.claves.append(None);
            while (posicion >= 0 and valor < raiz.claves[posicion]):
                raiz.claves[posicion + 1] = raiz.claves[posicion];
                posicion -= 1;
            raiz.claves[posicion + 1] = valor;

        else:
            # Si no es una hoja, se busca la hoja donde se debe insertar la clave
            while (posicion >= 0 and valor < raiz.claves[posicion]):
                posicion -= 1;
    
            posicion += 1;
            self.insertar_valor_no_completo(raiz.hijos[posicion], valor);
            if (len(raiz.hijos[posicion].claves) > self.orden - 1):
                self.dividir_pagina(raiz, posicion);

    def dividir_pagina(self, raiz: NodoArbolB, posicion: int):
        posicion_media: int = int((self.orden -1) // 2);

        hijo: NodoArbolB = raiz.hijos[posicion];
        nodo: NodoArbolB = NodoArbolB(hijo.hoja);

        raiz.hijos.insert(posicion + 1,  nodo);

        raiz.claves.insert(posicion, hijo.claves[posicion_media]);

        nodo.claves = hijo.claves[posicion_media + 1: posicion_media * 2 + 1];
        hijo.claves = hijo.claves[0: posicion_media];

        #Si el nodo que estamos dividiendo no es una hoja, se deben mover los hijos
        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media + 1: posicion_media * 2 + 2];
            hijo.hijos = hijo.hijos[0: posicion_media + 1];

    def generar_graphviz(self) -> str:
        """
        Genera el código Graphviz para representar el árbol B.
        """
        def recorrer_nodos(nodo: NodoArbolB, contador: list) -> (str, str):
            """
            Recorre los nodos de forma recursiva para generar etiquetas y conexiones.
            """
            if nodo is None:
                return "", ""

            nodo_id = f"n{contador[0]}"
            contador[0] += 1
            etiquetas = f'{nodo_id} [label = "'

            # Crear etiquetas para las claves
            for i, clave in enumerate(nodo.claves):
                etiquetas += f'<f{i}>{clave} | '
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

        # Contador inicial como una lista para pasarlo por referencia
        contador = [0]
        etiquetas, conexiones = recorrer_nodos(self.raiz, contador)

        return f'digraph G {{\nnode [shape = record];\n{etiquetas}{conexiones}}}'



