#Para los componentes de interfaz grafica
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Entry, Button

#Para la logica del proyecto 
from src.backend.ArbolB.ArbolB import ArbolB
from src.backend.entidades.Vehiculo import Vehiculo
from src.backend.ListaDoble.ListaDobleEnlazada import ListaDobleEnlazada
from src.backend.entidades.Cliente import Cliente
from src.backend.Grafo.ListaAdyacencia import ListaAdyacencia
from src.backend.entidades.Vertice import Vertice
from src.backend.entidades.Reader import Reader
from src.backend.entidades.Ruta import Ruta
from src.backend.entidades.Viaje import Viaje
from src.backend.ListaGenerica.ListaEnlazadaGenerica import ListaEnlazadaGenerica
from src.backend.Utils.ReporteViajes import ReporteViajes

class Aplicacion:
    def __init__(self, root):
        #Inicializar los objetos necesarios para la logica del proyecto
        self.arbol_vehiculos = ArbolB(5);
        self.lista_clientes = ListaDobleEnlazada();
        self.lista_rutas: list[Ruta] = [];
        self.listaAdyacencia = ListaAdyacencia();

        self.lector = Reader(self.lista_clientes, self.arbol_vehiculos, self.lista_rutas);

        #Se crea la lista enlazada generica para los viajes de tipo Viaje
        self.lista_viajes = ListaEnlazadaGenerica[Viaje]();
        self.reporte_viajes = ReporteViajes(self.lista_viajes);

        self.root = root
        self.root.title("Llega Rapidito")
        self.root.geometry("800x600")

        # Crear un menú principal
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Para mostrar la imagen generada
        self.label_imagen = tk.Label(root)
        self.label_imagen.pack()

        # Menú Cliente
        cliente_menu = tk.Menu(menu_bar, tearoff=0)
        cliente_menu.add_command(label="Carga Masiva", command=self.carga_masiva_cliente) #YA IMPLEMENTADO
        cliente_menu.add_command(label="Agregar", command=self.agregar_cliente) #YA IMPLEMENTADO
        cliente_menu.add_command(label="Modificar", command=self.modificar_cliente) #Ya IMPLEMENTADO
        cliente_menu.add_command(label="Eliminar", command=self.eliminar_cliente) #Ya IMPLEMENTADO
        cliente_menu.add_command(label="Mostrar Información", command=self.mostrar_informacion_cliente) #Ya IMPLEMENTADO
        cliente_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_cliente) #Ya IMPLEMENTADO
        menu_bar.add_cascade(label="Cliente", menu=cliente_menu)


        # Menú Vehículo
        vehiculo_menu = tk.Menu(menu_bar, tearoff=0)
        vehiculo_menu.add_command(label="Carga Masiva", command=self.carga_masiva_vehiculo) # Ya implementado
        vehiculo_menu.add_command(label="Agregar", command=self.agregar_vehiculo) # Ya implementado
        vehiculo_menu.add_command(label="Modificar", command=self.modificar_vehiculo) # Ya implementado
        vehiculo_menu.add_command(label="Eliminar", command=self.eliminar_vehiculo) 
        vehiculo_menu.add_command(label="Mostrar Información", command=self.mostrar_informacion_vehiculo) # Ya implementado
        vehiculo_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_vehiculo) # Ya implementado
        menu_bar.add_cascade(label="Vehículo", menu=vehiculo_menu)

        # Menú Rutas
        rutas_menu = tk.Menu(menu_bar, tearoff=0)
        rutas_menu.add_command(label="Carga Masiva", command=self.carga_masiva_rutas) # Ya implementado
        rutas_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_rutas) # Ya implementado 
        menu_bar.add_cascade(label="Rutas", menu=rutas_menu) 

        # Menu Viajes 
        viajes_menu = tk.Menu(menu_bar, tearoff=0)
        viajes_menu.add_command(label="Agregar Viaje", command=self.agregar_viaje)
        viajes_menu.add_command(label="Mostrar Viaje", command=self.mostrar_viaje) 
        viajes_menu.add_command(label="Mostrar Reporte", command=self.mostrar_reporte_viaje)
        menu_bar.add_cascade(label="Viajes", menu=viajes_menu)

    ########################## Métodos del menú Viajes ##########################

    def agregar_viaje(self):
        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title("Agregar Viaje")
        
        # Labels y campos de entrada para los datos del viaje
        tk.Label(ventana_agregar, text="Origen:").grid(row=0, column=0, padx=10, pady=5)
        entrada_origen = tk.Entry(ventana_agregar)
        entrada_origen.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(ventana_agregar, text="Destino:").grid(row=1, column=0, padx=10, pady=5)
        entrada_destino = tk.Entry(ventana_agregar)
        entrada_destino.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(ventana_agregar, text="DPI Cliente:").grid(row=2, column=0, padx=10, pady=5)
        entrada_dpi_cliente = tk.Entry(ventana_agregar)
        entrada_dpi_cliente.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(ventana_agregar, text="Placa Vehículo:").grid(row=3, column=0, padx=10, pady=5)
        entrada_placa_vehiculo = tk.Entry(ventana_agregar)
        entrada_placa_vehiculo.grid(row=3, column=1, padx=10, pady=5)

        # Función para agregar el viaje
        def confirmar_agregar():
            origen = entrada_origen.get().strip()
            destino = entrada_destino.get().strip()
            dpi_cliente = entrada_dpi_cliente.get().strip()
            placa_vehiculo = entrada_placa_vehiculo.get().strip()

            if origen and destino and dpi_cliente and placa_vehiculo:
                try:
                    dpi_cliente = int(dpi_cliente)
                    cliente = self.lista_clientes.buscar_cliente(dpi_cliente)
                    if cliente is None:
                        messagebox.showerror("Error", f"No se encontró cliente con DPI: {dpi_cliente}.")
                        return
                    
                    vehiculo = self.arbol_vehiculos.buscar(placa_vehiculo)
                    if vehiculo is None:
                        messagebox.showerror("Error", f"No se encontró vehículo con placa: {placa_vehiculo}.")
                        return
                    
                    # Crear el objeto Viaje
                    nuevo_viaje = Viaje(origen, destino, cliente, vehiculo)
                    
                    # Agregar el viaje a la lista de viajes
                    self.lista_viajes.agregar_elemento(nuevo_viaje);
                    
                    messagebox.showinfo("Éxito", f"Viaje agregado con éxito. ID del viaje: {nuevo_viaje.get_id()}.")
                    ventana_agregar.destroy()
                except ValueError:
                    messagebox.showerror("Error", "El DPI debe ser un número válido.")
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        # Botón para confirmar la adición del viaje
        tk.Button(ventana_agregar, text="Agregar", command=confirmar_agregar).grid(row=4, column=0, columnspan=2, pady=10)

        ventana_agregar.transient(self.root)
        ventana_agregar.grab_set()
        self.root.wait_window(ventana_agregar)


    def mostrar_viaje(self):
        print("Mostrar Viaje")

    def mostrar_reporte_viaje(self):
        try:
            self.reporte_viajes.mostrar_graphviz();
            ruta_imagen = "Viajes.png" 

            # Carga y ajusta la imagen
            img = Image.open(ruta_imagen)
            img = img.resize((500, 500)) 
            img_tk = ImageTk.PhotoImage(img)

            self.label_imagen.config(image=img_tk)
            self.label_imagen.image = img_tk

            messagebox.showinfo("Reporte", "Reporte de viajes generado exitosamente y mostrado en la interfaz.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo de imagen {ruta_imagen}.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al cargar la imagen: {e}")


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
        # Se crea una nueva ventana para ingresar los datos del cliente
        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title("Agregar Cliente")
        ventana_agregar.geometry("300x400")

        # Etiquetas para la entidad Cliente
        tk.Label(ventana_agregar, text="DPI").pack(pady=5)
        entry_dpi = tk.Entry(ventana_agregar)
        entry_dpi.pack(pady=5)

        tk.Label(ventana_agregar, text="Nombres").pack(pady=5)
        entry_nombres = tk.Entry(ventana_agregar)
        entry_nombres.pack(pady=5)

        tk.Label(ventana_agregar, text="Apellidos").pack(pady=5)
        entry_apellidos = tk.Entry(ventana_agregar)
        entry_apellidos.pack(pady=5)

        tk.Label(ventana_agregar, text="Género").pack(pady=5)
        entry_genero = tk.Entry(ventana_agregar)
        entry_genero.pack(pady=5)

        tk.Label(ventana_agregar, text="Teléfono").pack(pady=5)
        entry_telefono = tk.Entry(ventana_agregar)
        entry_telefono.pack(pady=5)

        tk.Label(ventana_agregar, text="Dirección").pack(pady=5)
        entry_direccion = tk.Entry(ventana_agregar)
        entry_direccion.pack(pady=5)

        # Función para validar los campos y agregar el cliente a la lista
        def agregar():
            try:
                dpi = int(entry_dpi.get())
                nombres = entry_nombres.get()
                apellidos = entry_apellidos.get()
                genero = entry_genero.get()
                telefono = int(entry_telefono.get()) 
                direccion = entry_direccion.get()

                # Verificar que todos los campos no estén vacíos
                if not (nombres and apellidos and genero and direccion):
                    messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                    return

                nuevo_cliente = Cliente(dpi, nombres, apellidos, genero, telefono, direccion)

                # Agregar el cliente a la lista de clientes
                self.lista_clientes.agregarElemento(nuevo_cliente);
                messagebox.showinfo("Éxito", "Cliente agregado exitosamente.")
                ventana_agregar.destroy()

            except ValueError:
                messagebox.showerror("Error", "DPI y Teléfono deben ser números enteros.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        # Botón para agregar el cliente
        btn_agregar = tk.Button(ventana_agregar, text="Agregar Cliente", command=agregar)
        btn_agregar.pack(pady=20)

        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(ventana_agregar, text="Cerrar", command=ventana_agregar.destroy)
        btn_cerrar.pack()


    def modificar_cliente(self):
        ventana_modificar = tk.Toplevel(self.root)
        ventana_modificar.title("Modificar Cliente")
        ventana_modificar.geometry("300x400")

        # Etiqueta y campo de entrada para ingresar el DPI del cliente a modificar
        tk.Label(ventana_modificar, text="Ingrese el DPI del cliente a modificar").pack(pady=5)
        entry_dpi = tk.Entry(ventana_modificar)
        entry_dpi.pack(pady=5)

        # Función para buscar el cliente y cargar sus datos
        def buscar_cliente():
            try:
                dpi_buscar = int(entry_dpi.get())
                # Buscar el cliente en la lista
                cliente = self.lista_clientes.buscar_cliente(dpi_buscar)

                if cliente:
                    entry_nombres.delete(0, tk.END)
                    entry_nombres.insert(0, cliente.get_nombres())
                    entry_apellidos.delete(0, tk.END)
                    entry_apellidos.insert(0, cliente.get_apellidos())
                    entry_genero.delete(0, tk.END)
                    entry_genero.insert(0, cliente.get_genero())
                    entry_telefono.delete(0, tk.END)
                    entry_telefono.insert(0, cliente.get_telefono())
                    entry_direccion.delete(0, tk.END)
                    entry_direccion.insert(0, cliente.get_direccion())

                    # Mostrar el formulario de edición
                    btn_guardar.pack(pady=20)
                    messagebox.showinfo("Cliente encontrado", "Cliente cargado. Puede editar los campos.")
                else:
                    messagebox.showerror("Error", "Cliente no encontrado.")

            except ValueError:
                messagebox.showerror("Error", "DPI debe ser un número entero.")

        # Botón para buscar al cliente
        btn_buscar = tk.Button(ventana_modificar, text="Buscar Cliente", command=buscar_cliente)
        btn_buscar.pack(pady=20)

        # Etiquetas y campos de entrada para modificar los atributos del cliente
        tk.Label(ventana_modificar, text="Nombres").pack(pady=5)
        entry_nombres = tk.Entry(ventana_modificar)
        entry_nombres.pack(pady=5)

        tk.Label(ventana_modificar, text="Apellidos").pack(pady=5)
        entry_apellidos = tk.Entry(ventana_modificar)
        entry_apellidos.pack(pady=5)

        tk.Label(ventana_modificar, text="Género").pack(pady=5)
        entry_genero = tk.Entry(ventana_modificar)
        entry_genero.pack(pady=5)

        tk.Label(ventana_modificar, text="Teléfono").pack(pady=5)
        entry_telefono = tk.Entry(ventana_modificar)
        entry_telefono.pack(pady=5)

        tk.Label(ventana_modificar, text="Dirección").pack(pady=5)
        entry_direccion = tk.Entry(ventana_modificar)
        entry_direccion.pack(pady=5)

        def guardar_cambios():
            try:
                nombres = entry_nombres.get()
                apellidos = entry_apellidos.get()
                genero = entry_genero.get()
                telefono = int(entry_telefono.get())
                direccion = entry_direccion.get()

                # Verificar que todos los campos no estén vacíos
                if not (nombres and apellidos and genero and direccion):
                    messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                    return

                # Buscar el cliente nuevamente por DPI
                dpi_buscar = int(entry_dpi.get())
                cliente = self.lista_clientes.buscar_cliente(dpi_buscar)
                if cliente:
                    # Actualizar los atributos del cliente
                    cliente.set_nombres(nombres)
                    cliente.set_apellidos(apellidos)
                    cliente.set_genero(genero)
                    cliente.set_telefono(telefono)
                    cliente.set_direccion(direccion)

                    messagebox.showinfo("Éxito", "Cliente modificado exitosamente.")
                    ventana_modificar.destroy()
                else:
                    messagebox.showerror("Error", "Cliente no encontrado.")

            except ValueError:
                messagebox.showerror("Error", "Teléfono debe ser un número entero.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        # Botón para guardar los cambios
        btn_guardar = tk.Button(ventana_modificar, text="Guardar Cambios", command=guardar_cambios)
        btn_guardar.pack_forget() 

        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(ventana_modificar, text="Cerrar", command=ventana_modificar.destroy)
        btn_cerrar.pack()

    def eliminar_cliente(self):
        ventana_eliminar = Toplevel(self.root)
        ventana_eliminar.title("Eliminar Cliente")
        ventana_eliminar.geometry("300x200")

        Label(ventana_eliminar, text="Ingrese el DPI del cliente a eliminar:").pack(pady=10)
        entrada_dpi = Entry(ventana_eliminar)
        entrada_dpi.pack(pady=5)

        def manejar_eliminacion():
            try:
                dpi = int(entrada_dpi.get())
                cliente = self.lista_clientes.buscar_cliente(dpi)

                if cliente:
                    self.lista_clientes.eliminar_cliente(dpi) # Eliminar el cliente de la lista
                    messagebox.showinfo("Éxito", f"Cliente con DPI {dpi} eliminado correctamente.")
                    ventana_eliminar.destroy()
                else:
                    messagebox.showerror("Error", f"No se encontró un cliente con DPI {dpi}.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un DPI válido.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        Button(ventana_eliminar, text="Eliminar", command=manejar_eliminacion).pack(pady=10)
        Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy).pack(pady=5)


    def mostrar_informacion_cliente(self):
        # Crear la ventana para mostrar la información del cliente
        ventana_info = Toplevel(self.root) 
        ventana_info.title("Mostrar Información del Cliente")
        ventana_info.geometry("500x400")

        Label(ventana_info, text="Ingrese el DPI del cliente:").pack(pady=10)
        entrada_dpi = Entry(ventana_info)
        entrada_dpi.pack(pady=5)

        etiqueta_info = Label(ventana_info, text="", justify="left", font=("Arial", 12))
        etiqueta_info.pack(pady=10)

        def buscar_cliente():
            try:
                dpi = int(entrada_dpi.get())
                cliente = self.lista_clientes.buscar_cliente(dpi)

                if cliente:
                    # Mostrar la información del cliente en la etiqueta
                    info = (
                        f"Nombre: {cliente.get_nombres()}\n"
                        f"Apellidos: {cliente.get_apellidos()}\n"
                        f"Género: {cliente.get_genero()}\n"
                        f"Teléfono: {cliente.get_telefono()}\n"
                        f"Dirección: {cliente.get_direccion()}"
                    )
                    etiqueta_info.config(text=info)
                else:
                    messagebox.showerror("Error", f"No se encontró un cliente con DPI {dpi}.")
                    etiqueta_info.config(text="")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un DPI válido.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        Button(ventana_info, text="Buscar", command=buscar_cliente).pack(pady=10)
        Button(ventana_info, text="Cerrar", command=ventana_info.destroy).pack(pady=5)

    def mostrar_reporte_cliente(self):
        self.lista_clientes.generar_reporte_graphviz()

        ruta_imagen = "Clientes.png"
        try:
            img = Image.open(ruta_imagen)
            img = img.resize((500, 500))
            img_tk = ImageTk.PhotoImage(img)

            # Mostrar la imagen en la interfaz
            self.label_imagen.config(image=img_tk)
            self.label_imagen.image = img_tk 

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
            try:
                self.lector.carga_masiva_vehiculos(ruta_archivo);
                # Mostrar mensaje de éxito
                messagebox.showinfo("Éxito", "Vehículos cargados exitosamente.")
            except Exception as e:
                # Manejo de errores
                messagebox.showerror("Error", f"Hubo un problema al procesar el archivo: {e}")

    def agregar_vehiculo(self):
        # Crear una nueva ventana para ingresar datos del vehículo
        ventana_agregar = tk.Toplevel(self.root)  # Cambia self por self.root
        ventana_agregar.title("Agregar Vehículo")
        
        # Labels y campos de entrada para los datos del vehículo
        tk.Label(ventana_agregar, text="Placa:").grid(row=0, column=0, padx=10, pady=5)
        entrada_placa = tk.Entry(ventana_agregar)
        entrada_placa.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(ventana_agregar, text="Marca:").grid(row=1, column=0, padx=10, pady=5)
        entrada_marca = tk.Entry(ventana_agregar)
        entrada_marca.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(ventana_agregar, text="Modelo:").grid(row=2, column=0, padx=10, pady=5)
        entrada_modelo = tk.Entry(ventana_agregar)
        entrada_modelo.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(ventana_agregar, text="Precio:").grid(row=3, column=0, padx=10, pady=5)
        entrada_precio = tk.Entry(ventana_agregar)
        entrada_precio.grid(row=3, column=1, padx=10, pady=5)

        # Función para agregar el vehículo
        def confirmar_agregar():
            placa = entrada_placa.get().strip()
            marca = entrada_marca.get().strip()
            modelo = entrada_modelo.get().strip()
            precio = entrada_precio.get().strip()

            if placa and marca and modelo and precio:
                try:
                    precio = float(precio)
                    self.arbol_vehiculos.insertar_valor(Vehiculo(placa, marca, modelo, precio))
                    messagebox.showinfo("Éxito", "Vehículo agregado correctamente.")
                    ventana_agregar.destroy()
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un valor numérico.")
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        # Botón para confirmar la adición
        tk.Button(ventana_agregar, text="Agregar", command=confirmar_agregar).grid(row=4, column=0, columnspan=2, pady=10)

        ventana_agregar.transient(self.root)
        ventana_agregar.grab_set()
        self.root.wait_window(ventana_agregar)
    
    def modificar_vehiculo(self):
        ventana_modificar = tk.Toplevel(self.root)
        ventana_modificar.title("Modificar Vehículo")
        ventana_modificar.geometry("300x400")

        # Etiqueta y campo de entrada para ingresar la placa del vehículo a modificar
        tk.Label(ventana_modificar, text="Ingrese la Placa del vehículo a modificar").pack(pady=5)
        entry_placa = tk.Entry(ventana_modificar)
        entry_placa.pack(pady=5)

        # Función para buscar el vehículo y cargar sus datos
        def buscar_vehiculo():
            placa_buscar = entry_placa.get().strip()

            if placa_buscar:
                # Buscar el vehículo en el árbol
                vehiculo = self.arbol_vehiculos.buscar(placa_buscar)

                if vehiculo:
                    entry_marca.delete(0, tk.END)
                    entry_marca.insert(0, vehiculo.get_marca())
                    entry_modelo.delete(0, tk.END)
                    entry_modelo.insert(0, vehiculo.get_modelo())
                    entry_precio.delete(0, tk.END)
                    entry_precio.insert(0, vehiculo.get_precio())

                    # Se muestra el botón de guardar cambios y el formulario de edición
                    btn_guardar.pack(pady=20)
                    messagebox.showinfo("Vehículo encontrado", "Vehículo cargado. Puede editar los campos.")
                else:
                    messagebox.showerror("Error", "Vehículo no encontrado.")
            else:
                messagebox.showerror("Error", "Debe ingresar una placa válida.")

        # Botón para buscar el vehículo
        btn_buscar = tk.Button(ventana_modificar, text="Buscar Vehículo", command=buscar_vehiculo)
        btn_buscar.pack(pady=20)

        # Etiquetas y campos de entrada para modificar los atributos del vehículo
        tk.Label(ventana_modificar, text="Marca").pack(pady=5)
        entry_marca = tk.Entry(ventana_modificar)
        entry_marca.pack(pady=5)

        tk.Label(ventana_modificar, text="Modelo").pack(pady=5)
        entry_modelo = tk.Entry(ventana_modificar)
        entry_modelo.pack(pady=5)

        tk.Label(ventana_modificar, text="Precio").pack(pady=5)
        entry_precio = tk.Entry(ventana_modificar)
        entry_precio.pack(pady=5)

        # Función para guardar los cambios
        def guardar_cambios():
            try:
                marca = entry_marca.get().strip()
                modelo = entry_modelo.get().strip()
                precio = entry_precio.get().strip()

                if not (marca and modelo and precio):
                    messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                    return

                precio = float(precio)

                # Buscar el vehículo nuevamente por placa
                placa_buscar = entry_placa.get().strip()
                vehiculo = self.arbol_vehiculos.buscar(placa_buscar);
                if vehiculo:
                    # Actualizar los atributos del vehículo
                    vehiculo.set_marca(marca)
                    vehiculo.set_modelo(modelo)
                    vehiculo.set_precio(precio)

                    messagebox.showinfo("Éxito", "Vehículo modificado exitosamente.")
                    ventana_modificar.destroy()
                else:
                    messagebox.showerror("Error", "Vehículo no encontrado.")
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        btn_guardar = tk.Button(ventana_modificar, text="Guardar Cambios", command=guardar_cambios)
        btn_guardar.pack_forget()

        btn_cerrar = tk.Button(ventana_modificar, text="Cerrar", command=ventana_modificar.destroy)
        btn_cerrar.pack()

    def eliminar_vehiculo(self):
        print("Eliminar Vehículo")

    def mostrar_informacion_vehiculo(self):
        ventana_info = tk.Toplevel(self.root)
        ventana_info.title("Mostrar Información del Vehículo")
        ventana_info.geometry("500x400")

        # Etiqueta y entrada para ingresar la placa del vehículo
        tk.Label(ventana_info, text="Ingrese la Placa del vehículo:").pack(pady=10)
        entrada_placa = tk.Entry(ventana_info)
        entrada_placa.pack(pady=5)

        # Etiqueta para mostrar la información del vehículo
        etiqueta_info = tk.Label(ventana_info, text="", justify="left", font=("Arial", 12))
        etiqueta_info.pack(pady=10)

        # Función para buscar y mostrar la información del vehículo
        def buscar_vehiculo():
            placa = entrada_placa.get().strip() 

            if placa:
                # Buscar el vehículo en el árbol
                vehiculo = self.arbol_vehiculos.buscar(placa)

                if vehiculo:
                    # Mostrar la información del vehículo en la etiqueta
                    info = (
                        f"Placa: {vehiculo.get_placa()}\n"
                        f"Marca: {vehiculo.get_marca()}\n"
                        f"Modelo: {vehiculo.get_modelo()}\n"
                        f"Precio: {vehiculo.get_precio()}"
                    )
                    etiqueta_info.config(text=info)
                else:
                    messagebox.showerror("Error", f"No se encontró un vehículo con la placa {placa}.")
                    etiqueta_info.config(text="")
            else:
                messagebox.showerror("Error", "Por favor, ingrese una placa válida.")

        tk.Button(ventana_info, text="Buscar", command=buscar_vehiculo).pack(pady=10)
        tk.Button(ventana_info, text="Cerrar", command=ventana_info.destroy).pack(pady=5)


    def mostrar_reporte_vehiculo(self):
        try:
            self.arbol_vehiculos.generar_graphviz();
            ruta_imagen = "ArbolB.png"

            # Aqui se carga la imagen generada por Graphviz usando PIL
            img = Image.open(ruta_imagen)
            img = img.resize((400, 400))
            img_tk = ImageTk.PhotoImage(img)

            # Mostrar la imagen en la interfaz
            self.label_imagen.config(image=img_tk)
            self.label_imagen.image = img_tk

            messagebox.showinfo("Reporte", "Reporte de vehículos generado exitosamente y mostrado en la interfaz.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de reporte de vehículos.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al mostrar el reporte: {e}")


    ########################## Métodos del menú Rutas ##########################
    def carga_masiva_rutas(self):
        # limpiar la lista de rutas antes de cargar nuevas rutas
        self.lista_rutas.clear();
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de rutas",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta_archivo:
            try:
                self.lector.carga_masiva_rutas(ruta_archivo)
                # Agregar todos los objetos de la lista de rutas al grafo
                for ruta in self.lista_rutas:
                    self.listaAdyacencia.insertar(ruta);

                messagebox.showinfo("Carga Masiva", "Rutas cargadas exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema al cargar las rutas: {str(e)}")
        else:
            messagebox.showerror("Error", "No se seleccionó ningún archivo.")

    def mostrar_reporte_rutas(self):
        try:
            self.listaAdyacencia.generar_graphviz();
            ruta_imagen = "Grafo.png"

            img = Image.open(ruta_imagen)
            img = img.resize((500, 500))
            img_tk = ImageTk.PhotoImage(img)

            # Mostrar la imagen en la interfaz
            self.label_imagen.config(image=img_tk)
            self.label_imagen.image = img_tk 

            messagebox.showinfo("Reporte", "Reporte de rutas generado exitosamente y mostrado en la interfaz")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al cargar la imagen: {e}")
