import tkinter as tk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Viajes")
        self.geometry("1500x700")
        self.resizable(width=False, height=False)

        self.container = tk.Frame(self, bg='white')
        self.container.pack(fill="both", expand=True)