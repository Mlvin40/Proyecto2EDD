class Ruta:
    #se debe de almacenar en la lista de adyacencia de la matriz de adyacencia
    #debe de tener lugar_origen y lugar_destino, tiempo_de_ruta
    def __init__(self, lugar_origen: str, lugar_destino: str, tiempo_de_ruta: int):
        self.__lugar_origen = lugar_origen
        self.__lugar_destino = lugar_destino
        self.__tiempo_de_ruta = tiempo_de_ruta

    def get_lugar_origen(self):
        return self.__lugar_origen

    def set_lugar_origen(self, lugar_origen: str):
        self.__lugar_origen = lugar_origen

    def get_lugar_destino(self):
        return self.__lugar_destino

    def set_lugar_destino(self, lugar_destino: str):
        self.__lugar_destino = lugar_destino

    def get_tiempo_de_ruta(self):
        return self.__tiempo_de_ruta

    def set_tiempo_de_ruta(self, tiempo_de_ruta: int):
        self.__tiempo_de_ruta = tiempo_de_ruta

    def __str__(self):
        return f"Ruta: {self.__lugar_origen} -> {self.__lugar_destino}, Tiempo: {self.__tiempo_de_ruta} minutos"
