from src.backend.ArbolB.ArbolB import ArbolB
from .Vehiculo import Vehiculo
from .Cliente import Cliente
from src.backend.ListaDoble.ListaDobleEnlazada import ListaDobleEnlazada
from src.backend.entidades.Ruta import Ruta

class Reader:
    def __init__(self, lista_circular: ListaDobleEnlazada, arbol_b: ArbolB, lista_rutas: list[Ruta]):
        self.lista_circular = lista_circular; 
        self.arbol_b = arbol_b;     
        self.lista_rutas = lista_rutas;
        

    def carga_masiva_clientes(self, ruta_archivo: str):
        #Formato: DPI, Nombres, Apellidos, Género, Teléfono, Dirección (separados por coma y un salto de línea).
        try:
            with open(ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    linea = linea.strip()  # Eliminar espacios en blanco
                    if linea:
                        try:
                            datos = linea.split(',')  # Separar los atributos por coma
                            if len(datos) == 6:
                                dpi, nombres, apellidos, genero, telefono, direccion = map(str.strip, datos)
                                # Crear cliente y agregarlo a la lista circular
                                cliente = Cliente(int(dpi), nombres, apellidos, genero, int(telefono), direccion)
                                self.lista_circular.agregarElemento(cliente)
                            else:
                                print(f"Línea con formato inválido: {linea}")
                        except Exception as e:
                            print(f"Error al procesar la línea '{linea}': {e}")
        except FileNotFoundError:
            print(f"El archivo {ruta_archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")


    def carga_masiva_vehiculos(self, ruta_archivo: str):
        #Formato= Placa:Marca:Modelo:Precio;
        try:
            with open(ruta_archivo, 'r') as archivo:

                contenido = archivo.read()
                lineas = contenido.split(';')  # Separar los registros por ';'
                for linea in lineas:
                    linea = linea.strip()  # Eliminar espacios en blanco
                    if linea:  # Ignorar líneas vacías
                        datos = linea.split(':')  # Separar por ':'
                        if len(datos) == 4:
                            placa, marca, modelo, precio = map(str.strip, datos)

                            vehiculo = Vehiculo(placa, marca, modelo, float(precio))
                            self.arbol_b.insertar_valor(vehiculo)
                        else:
                            print(f"Línea con formato inválido: {linea}")
            print("Carga masiva de vehículos completada.")
        except FileNotFoundError:
            print(f"El archivo {ruta_archivo} no fue encontrado.")
        except ValueError as ve:
            print(f"Error al convertir los datos del archivo: {ve}")
        except Exception as e:
            print(f"Error al procesar vehículos: {e}")


    #Funciona bien
    def carga_masiva_rutas(self, ruta_archivo: str): 
        #Formato = Lugar Origen / Lugar Destino / Tiempo de Ruta en segundos
        try:
            with open(ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    if linea.strip():  # Ignorar líneas vacías
                        datos = linea.strip().split('/')
                        if len(datos) == 3:
                            origen, destino, tiempo = map(str.strip, datos)
                            tiempo = int(tiempo[:-1])  # Convertir tiempo a número (eliminar % y convertir a int)
                            
                            # Crear una instancia de la clase Ruta
                            ruta = Ruta(origen, destino, tiempo)
                            
                            # Agregar la ruta a la lista
                            self.lista_rutas.append(ruta)
            print("Carga masiva completada exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {ruta_archivo} no fue encontrado.")
        except ValueError:
            print("Error al procesar el tiempo de ruta, asegúrate de que es un número válido.")
        except Exception as e:
            print(f"Error al procesar rutas: {e}")