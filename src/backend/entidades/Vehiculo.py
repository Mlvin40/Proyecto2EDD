class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._precio = precio

    def __str__(self):
        return f"Placa: {self._placa}, Marca: {self._marca}, Modelo: {self._modelo}, Precio: {self._precio}"
    
    # Métodos para obtener los atributos (getters)
    def get_placa(self):
        return self._placa

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_precio(self):
        return self._precio

    # Métodos para modificar los atributos (setters)
    def set_placa(self, value):
        self._placa = value

    def set_marca(self, value):
        self._marca = value

    def set_modelo(self, value):
        self._modelo = value

    def set_precio(self, value):
        self._precio = value

