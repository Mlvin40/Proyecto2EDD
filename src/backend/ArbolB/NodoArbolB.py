class NodoArbolB:
    # Constructor de la clase
    def __init__(self, hoja = False):
        self.hoja: bool = hoja
        self.claves: list[int] = [] # este es el orden del arbol -1 (m-1)
        self.hijos: list[NodoArbolB] = [] # orden  del arbol (m)

    def __str__(self):
        return f"Hoja: {self.hoja}, Claves: {self.claves}, Hijos: {self.hijos}"

         



    