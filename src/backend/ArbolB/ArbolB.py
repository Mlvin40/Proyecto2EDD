from .NodoArbolB import NodoArbolB

class ArbolB:
    # Constructor de la clase   
    def __init__(self, orden: int):
        self.root: NodoArbolB = NodoArbolB(True)  # este es el nodo raíz
        self.orden: int = orden  # este es el valor de m
    
    def insertar_clave(self, valor: int):
        root: NodoArbolB = self.root

        if len(root.claves) == self.orden - 1:
            nodo: NodoArbolB = NodoArbolB(False)
            self.root = nodo
            nodo.hijos.insert(0, root)  # prácticamente esto inserta a la izquierda
            self.dividir_hijo(nodo, 0)
            self.insertar_valor_no_completo(nodo, valor)
        else:
            self.insertar_valor_no_completo(root, valor)

    def insertar_valor_no_completo(self, raiz: NodoArbolB, valor: int):
        contador: int = len(raiz.claves) - 1

        if raiz.hoja:
            raiz.claves.append(None)

            # si contador = 2 ; claves = [2, 4, 6]; valor = 5;
            while contador >= 0 and valor < raiz.claves[contador]:  # 1. true
                raiz.claves[contador + 1] = raiz.claves[contador]
                contador -= 1
            raiz.claves[contador + 1] = valor  # claves = [2, 4, 5, 6] <- de esta forma se inserta el valor en la hoja
        else:
            # recorrer nuevamente nuestras claves para saber hacia qué hijo vamos a ir
            while contador >= 0 and valor < raiz.claves[contador]:
                contador -= 1
            contador += 1

            if len(raiz.hijos[contador].claves) == self.orden - 1:
                # separar los nodos
                self.dividir_hijo(raiz, contador)
                if valor > raiz.claves[contador]:
                    contador += 1

            self.insertar_valor_no_completo(raiz.hijos[contador], valor)

    def dividir_hijo(self, raiz: NodoArbolB, posicion: int):
        posicion_media: int = (self.orden - 1) // 2  # Castear a entero
        hijo: NodoArbolB = raiz.hijos[posicion]
        nodo: NodoArbolB = NodoArbolB(hijo.hoja)  # Crear un nuevo nodo

        raiz.hijos.insert(posicion + 1, nodo)
        raiz.claves.insert(posicion, hijo.claves[posicion_media])
        nodo.claves = hijo.claves[posicion_media + 1:]
        hijo.claves = hijo.claves[:posicion_media]

        if not hijo.hoja:  # si el hijo no es una hoja
            nodo.hijos = hijo.hijos[posicion_media + 1:]
            hijo.hijos = hijo.hijos[:posicion_media + 1]

    def imprimir_usuario(self) -> str:
        # Este método simplemente llama al método imprimir con la raíz.
        return self.imprimir(self.root)

    def imprimir(self, nodo: NodoArbolB) -> str:
        # Este método recursivo recorre todo el árbol.
        arbol = "["

        # Recorrer las claves de este nodo
        for item in nodo.claves:
            arbol += f"{item}, "

        arbol += "]"

        # Recursivamente recorrer los hijos si los tiene
        for item in nodo.hijos:
            arbol += self.imprimir(item)  # Llamada recursiva

        return arbol

    

    def __str__(self):
        return f"{self.root}"
