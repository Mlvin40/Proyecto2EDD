import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("800x600")
        
        self.initUI()

    def initUI(self):
        # Crear la etiqueta
        self.label = tk.Label(self, text="Hola Mundo", font=("Arial", 24))
        self.label.pack(pady=20)

        # Crear el botón para cambiar el texto
        self.button = tk.Button(self, text="Cambiar texto", command=self.cambiar_texto)
        self.button.pack(pady=20)

        # Crear el menú
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Crear el menú de opciones
        self.menu_clientes = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_clientes.add_command(label="Clientes", command=self.mostrar_clientes)
        self.menu_clientes.add_command(label="Vehículos", command=self.mostrar_vehiculos)
        self.menu_clientes.add_command(label="Rutas", command=self.mostrar_rutas)
        self.menu_clientes.add_command(label="Viajes", command=self.mostrar_viajes)

        self.menu_bar.add_cascade(label="Opciones", menu=self.menu_clientes)

    def cambiar_texto(self):
        self.label.config(text="Texto cambiado")

    # Métodos para manejar las opciones del menú
    def mostrar_clientes(self):
        messagebox.showinfo("Clientes", "Mostrar Clientes")

    def mostrar_vehiculos(self):
        messagebox.showinfo("Vehículos", "Mostrar Vehículos")

    def mostrar_rutas(self):
        messagebox.showinfo("Rutas", "Mostrar Rutas")

    def mostrar_viajes(self):
        messagebox.showinfo("Viajes", "Mostrar Viajes")

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
