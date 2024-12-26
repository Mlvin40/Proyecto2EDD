from NodoArbolB import NodoArbolB

class ArbolB:
    def __init__(self, orden: int):
        self.root: NodoArbolB = NodoArbolB(True) # este es el nodo raiz
        self.orden: int = orden # este es el valor de m
    
    def insertar_clave(self, valor: int):
        root: NodoArbolB = self.root

        if len(root.valor) == self.orden - 1:
            # separacion de la hoja
            pass
        else:
            self.insertar_valor(root, valor)

    def insertar_valor(self, raiz: NodoArbolB, valor: int):
        contador = len(raiz.valor) - 1 
        
        if(raiz.hoja):
            raiz.claves.append(None);

            while contador >= 0 and valor < raiz.claves[contador][0]:
                raiz.claves[contador + 1] = raiz.claves[contador]
                contador -= 1;
            raiz.claves[contador + 1] = valor;
        else:
            #recorrer nuevamente nuestras claves para saber hacia que hijo vamos a ir
            while contador >= 0 and valor < raiz.claves[contador[0]]:
                contador -= 1 
            if len(raiz.hijos[contador].claves) == self.orden - 1:
                #separacion de la hoja
                pass
            self.insertar_valor(raiz.hijos[contador], valor)

