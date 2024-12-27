class Ruta:
    #se debe de almacenar en la lista de adyacencia de la matriz de adyacencia
    #debe de tener lugar_origen y lugar_destino, tiempo_de_ruta
    def __init__(self, lugar_origen: str, lugar_destino: str, tiempo_de_ruta: int):
        self.lugar_origen = lugar_origen
        self.lugar_destino = lugar_destino
        self.tiempo_de_ruta = tiempo_de_ruta

    