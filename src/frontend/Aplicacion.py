# Para los componentes de interfaz grafica
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

#Para la logica del proyecto 
from src.backend.ArbolB.ArbolB import ArbolB
from src.backend.entidades.Vehiculo import Vehiculo
from src.backend.ListaDoble.ListaDobleEnlazada import ListaDobleEnlazada
from src.backend.entidades.Cliente import Cliente
from src.backend.Grafo.ListaAdyacencia import ListaAdyacencia
from src.backend.entidades.Vertice import Vertice
from src.backend.entidades.Reader import Reader
from src.backend.entidades.Ruta import Ruta

class Aplicacion:
    def __init__(self, root):
        #Inicializar los objetos necesarios para la logica del proyecto
        self.arbol_vehiculos = ArbolB(5);
        self.lista_clientes = ListaDobleEnlazada();
        self.lista_rutas: list[Ruta] = [];
        self.listaAdyacencia = ListaAdyacencia();
        self.lector = Reader(self.lista_clientes, self.arbol_vehiculos, self.lista_rutas);       

        self.root = root
        self.root.title("Llega Rapidito")
        self.root.geometry("600x400")

        # Crear un menú principal
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Para mostrar la imagen generada
        self.label_imagen = tk.Label(root)
        self.label_imagen.pack()


        # Menú Cliente
        cliente_menu = tk.Menu(menu_bar, tearoff=0)
        cliente_menu.add_command(label="Carga Masiva", command=self.carga_masiva_cliente)
        cliente_menu.add_command(label="Agregar", command=self.agregar_cliente)
        cliente_menu.add_command(label="Modificar", command=self.modificar_cliente)
        cliente_menu.add_command(label="Eliminar", command=self.eliminar_cliente)
        cliente_menu.add_command(label="Mostrar Información", command=self.mostrar_informacion_cliente)
        cliente_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_cliente)
        menu_bar.add_cascade(label="Cliente", menu=cliente_menu)



        # Menú Vehículo
        vehiculo_menu = tk.Menu(menu_bar, tearoff=0)
        vehiculo_menu.add_command(label="Carga Masiva", command=self.carga_masiva_vehiculo)
        vehiculo_menu.add_command(label="Agregar", command=self.agregar_vehiculo)
        vehiculo_menu.add_command(label="Modificar", command=self.modificar_vehiculo)
        vehiculo_menu.add_command(label="Eliminar", command=self.eliminar_vehiculo)
        vehiculo_menu.add_command(label="Mostrar Información", command=self.mostrar_informacion_vehiculo)
        vehiculo_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_vehiculo)
        menu_bar.add_cascade(label="Vehículo", menu=vehiculo_menu)

        # Menú Rutas
        rutas_menu = tk.Menu(menu_bar, tearoff=0)
        rutas_menu.add_command(label="Carga Masiva", command=self.carga_masiva_rutas)
        rutas_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_rutas)
        menu_bar.add_cascade(label="Rutas", menu=rutas_menu)

    ########################## Métodos del menú Cliente ##########################
    def carga_masiva_cliente(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de clientes",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta_archivo:
            self.lector.carga_masiva_clientes(ruta_archivo);
            messagebox.showinfo("Carga Masiva", "Clientes cargados exitosamente");

        else:
            messagebox.showerror("Error", "No se seleccionó ningún archivo");

    def agregar_cliente(self):
        print("Agregar Cliente")

    def modificar_cliente(self):
        print("Modificar Cliente")

    def eliminar_cliente(self):
        print("Eliminar Cliente")

    def mostrar_informacion_cliente(self):
        print("Mostrar Información Cliente")

    def mostrar_reporte_cliente(self):
        self.lista_clientes.generar_reporte_graphviz()

        # Ruta de la imagen generada
        ruta_imagen = "Clientes.png"

        # Cargar la imagen usando Pillow
        try:
            img = Image.open(ruta_imagen)
            img = img.resize((400, 400))  # Redimensionar si es necesario
            img_tk = ImageTk.PhotoImage(img)

            # Mostrar la imagen en la interfaz
            self.label_imagen.config(image=img_tk)
            self.label_imagen.image = img_tk  # Necesario para evitar que la imagen se elimine

            messagebox.showinfo("Reporte", "Reporte de clientes generado exitosamente y mostrado en la interfaz")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al cargar la imagen: {e}")


    ########################## Métodos del menú Vehículo ##########################
    def carga_masiva_vehiculo(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de vehículos",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta_archivo:
            messagebox.showinfo("Carga Masiva", f"Carga masiva de vehículos desde: {ruta_archivo}")

    def agregar_vehiculo(self):
        print("Agregar Vehículo")

    def modificar_vehiculo(self):
        print("Modificar Vehículo")

    def eliminar_vehiculo(self):
        print("Eliminar Vehículo")

    def mostrar_informacion_vehiculo(self):
        print("Mostrar Información Vehículo")

    def mostrar_reporte_vehiculo(self):
        print("Generar Reporte Vehículo")

    ########################## Métodos del menú Rutas ##########################
    def carga_masiva_rutas(self):
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de rutas",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta_archivo:
            messagebox.showinfo("Carga Masiva", f"Carga masiva de rutas desde: {ruta_archivo}")

    def mostrar_reporte_rutas(self):
        print("Generar Reporte Rutas")