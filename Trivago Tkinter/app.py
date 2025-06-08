import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación de Gestión Trivago")
        self.geometry("1200x800")
        self.configure(bg='white')
        self.state('zoomed')

        # Banda de color con logo 
        self.header_frame = tk.Frame(self, bg="blue", height=100)
        self.header_frame.pack(fill="x")

        # Logo de trivago
        self.logo_frame = tk.Frame(self.header_frame, bg="blue")
        self.logo_frame.pack(side="left", padx=20, pady=20)
        self.logo_image = Image.open("image/2.png")  # Reemplaza con la ruta de tu logo
        self.logo_image = self.logo_image.resize((170, 80), Image.Resampling.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.logo_frame, image=self.logo_photo, bg="blue")
        self.logo_label.pack(side="left")

        # Título en la banda superior
        self.header_label = tk.Label(self.header_frame, text="Panel de Usuario", font=("Arial", 24), bg="blue", fg="white")
        self.header_label.pack(side="left", padx=20, pady=20)

        # Título principal
        self.titulo_principal = tk.Label(self, text='Aplicación de Gestión Trivago', font=('Arial', 24), bg='white')
        self.titulo_principal.pack(pady=20)

        # Frame para los botones
        self.buttons_frame = tk.Frame(self, bg="white")
        self.buttons_frame.pack(pady=20)

        # Estilo para los botones
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 20), padding=20)  # Aumentar el tamaño del botón

        # Botón de Huéspedes
        self.huespedes_button = ttk.Button(self.buttons_frame, text='Huéspedes', style='TButton', command=self.ver_huespedes)
        self.huespedes_button.pack(side="left", padx=20)

        # Botón de Habitaciones
        self.habitaciones_button = ttk.Button(self.buttons_frame, text='Habitaciones', style='TButton', command=self.ver_habitaciones)
        self.habitaciones_button.pack(side="left", padx=20)

        # Botón de Ingresos
        self.ingresos_button = ttk.Button(self.buttons_frame, text='Ingresos', style='TButton', command=self.ver_ingresos)
        self.ingresos_button.pack(side="left", padx=20)

        # Frame para la imagen debajo de los botones
        self.image_below_buttons_frame = tk.Frame(self, bg="white")
        self.image_below_buttons_frame.pack(pady=20)

        # Imagen debajo de los botones
        self.image_below_buttons = Image.open("image/1.png")  # Reemplaza con la ruta de tu imagen
        self.image_below_buttons = self.image_below_buttons.resize((800, 300), Image.Resampling.LANCZOS)
        self.image_below_buttons_photo = ImageTk.PhotoImage(self.image_below_buttons)
        self.image_below_buttons_label = tk.Label(self.image_below_buttons_frame, image=self.image_below_buttons_photo, bg="white")
        self.image_below_buttons_label.pack()

    def ver_huespedes(self):
        from views.huespedes_view import HuespedesView
        self.destroy()
        app = HuespedesView()
        app.mainloop()

    def ver_habitaciones(self):
        from views.habitaciones_view import HabitacionesView
        self.destroy()
        app = HabitacionesView()
        app.mainloop()

    def ver_ingresos(self):
        print("Mostrando módulo de Ingresos")
        # vista de Ingresos

# Bucle principal para la ejecución de la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()