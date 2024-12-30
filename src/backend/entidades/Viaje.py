from .Cliente import Cliente
from .Vehiculo import Vehiculo
from datetime import datetime
import random

class Viaje:
    def __init__(self, origen: str, destino: str, cliente: Cliente, vehiculo: Vehiculo, camino = None):
        self.__id: int = self.generador_id();
        self.__origen: str = origen;
        self.__destino: str = destino;
        self.__fecha: str = datetime.now(); # Agarrar la fecha actual del sistema  
        self.__cliente = cliente;
        self.__camino = camino;

    # Generar los metodos get
    def get_id(self) -> int:
        return self.__id
    
    def get_origen(self) -> str:
        return self.__origen
    
    def get_destino(self) -> str:
        return self.__destino
    
    def get_fecha(self) -> str:
        return self.__fecha
    
    def get_cliente(self) -> Cliente:
        return self.__cliente   
    
    def get_camino(self):
        return self.__camino
    
    def generador_id(self):
        self.__id = random.randint(1000000, 9999999) # Generar un número aleatorio de 7 dígitos
        return self.__id