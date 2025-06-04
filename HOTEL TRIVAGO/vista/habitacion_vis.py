#Son las interfaces gráficas con Tkinter . Son las interfaces gráficas con Tkinter .
#no se si utilizar este 
import tkinter as tk
from tkinter import ttk, messagebox

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Hotelera - TRIVAGO")
        self.root.geometry("600x400")

        ttk.Label(root, text="Bienvenido al sistema de gestión Hotel Trivago", font=("Arial", 14)).pack(pady=10)

        # Botones de acceso a módulos
        ttk.Button(root, text="Administrar Huéspedes", command=self.abrir_huespedes).pack(pady=5)
        ttk.Button(root, text="Administrar Habitaciones", command=self.abrir_habitaciones).pack(pady=5)
        ttk.Button(root, text="Registrar Ingresos", command=self.abrir_ingresos).pack(pady=5)

    def abrir_huespedes(self):
        messagebox.showinfo("Info", "Se abrirá el módulo de huéspedes.")

    def abrir_habitaciones(self):
        messagebox.showinfo("Info", "Se abrirá el módulo de habitaciones.")

    def abrir_ingresos(self):
        messagebox.showinfo("Info", "Se abrirá el módulo de ingresos.")

root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()