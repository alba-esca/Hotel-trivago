import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from views.base_view import MainView
from PIL import Image, ImageTk
from controller.habitaciones_controller import HabitacionesController

class HabitacionesView(MainView):
    def __init__(self):
        super().__init__()
        self.state('zoomed')

    # Banda de color con logo y título
        self.header_frame = tk.Frame(self, bg="blue", height=100)
        self.header_frame.place(x=0, y=0, relwidth=1)  # encabazado en la parte superior

        # Logo de trivago
        self.logo_frame = tk.Frame(self.header_frame, bg="blue")
        self.logo_frame.pack(side="left", padx=20, pady=20)
        self.logo_image = Image.open("image/2.png")  # reemplazar ruta del logo
        self.logo_image = self.logo_image.resize((170, 80), Image.Resampling.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.logo_frame, image=self.logo_photo, bg="blue")
        self.logo_label.pack(side="left")

        # Título en la banda superior
        self.header_label = tk.Label(self.header_frame, text="Panel Administrador", font=("Arial", 24), bg="blue", fg="white")
        self.header_label.pack(side="left", padx=20, pady=20)

        # Configuración de la ventana principal
        self.geometry("1200x800")  # tamaño de la ventana
        self.configure(bg='white')

        # Contenedor principal para todos los widgets
        self.container = tk.Frame(self, bg='white')
        self.container.pack(fill="both", expand=True)

        # Título principal
        self.titulo_principal = tk.Label(self.container, text='Módulo de Habitaciones', font=('Arial', 24), bg='white')
        self.titulo_principal.place(relx=0.5, rely=0.1, anchor='center')  # NO MOVER!!

        # Frame central para centrar la tabla y el botón NO MOVER!
        self.central_frame = tk.Frame(self.container, bg='white')
        self.central_frame.pack(expand=True)

        # Inicializar el controlador
        self.controller = HabitacionesController()

        # Tabla de habitaciones
        self.tabla = ttk.Treeview(self.central_frame)
        self.tabla['columns'] = ('codigo', 'numero', 'tipo', 'capacidad', 'precio', 'estado')
        self.tabla.column('#0', width=0, minwidth=0, stretch=tk.NO)
        self.tabla.column('codigo', anchor=tk.W, width=120)
        self.tabla.column('numero', anchor=tk.W, width=120)
        self.tabla.column('tipo', anchor=tk.W, width=120)
        self.tabla.column('capacidad', anchor=tk.W, width=120)
        self.tabla.column('precio', anchor=tk.W, width=120)
        self.tabla.column('estado', anchor=tk.W, width=120)

        self.tabla.heading('codigo', text='Código', anchor=tk.W)
        self.tabla.heading('numero', text='Número', anchor=tk.W)
        self.tabla.heading('tipo', text='Tipo', anchor=tk.W)
        self.tabla.heading('capacidad', text='Capacidad', anchor=tk.W)
        self.tabla.heading('precio', text='Precio por Noche', anchor=tk.W)
        self.tabla.heading('estado', text='Estado', anchor=tk.W)

        self.lista_habitaciones = self.listar_habitaciones()
        if isinstance(self.lista_habitaciones, list):
            for i in self.lista_habitaciones:
                fila = self.tabla.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5]))

        # Centrar la tabla en el frame central
        self.tabla.pack(pady=20)

        # Contenedor intermedio para los botones
        self.botones_frame = tk.Frame(self.central_frame)
        self.botones_frame.pack()

        # Botones de abajo
        self.agregar_boton = tk.Button(self.botones_frame, text='Agregar', font=('Arial', 12), command=self.abrir_ventana_agregar)
        self.agregar_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.agregar_boton.grid(row=0, column=0, padx=10, pady=10)

        self.editar_boton = tk.Button(self.botones_frame, text='Editar', font=('Arial', 12), command=self.abrir_ventana_editar)
        self.editar_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.editar_boton.grid(row=0, column=1, padx=10, pady=10)

        self.eliminar_boton = tk.Button(self.botones_frame, text='Eliminar', font=('Arial', 12), command=self.abrir_ventana_eliminar)
        self.eliminar_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.eliminar_boton.grid(row=0, column=2, padx=10, pady=10)

        self.menu_boton = tk.Button(self.botones_frame, text='Menú', font=('Arial', 12), command=self.abrir_menu)
        self.menu_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.menu_boton.grid(row=0, column=3, padx=10, pady=10)

        # Centrar el frame central en la ventana
        self.central_frame.pack(expand=True)

    def abrir_ventana_agregar(self):
        self.ventana_agregar = tk.Toplevel(self.container, bg='white')
        self.ventana_agregar.title('Agregar Habitación')
        self.ventana_agregar.geometry('800x600')
        self.ventana_agregar.resizable(width=False, height=False)

        # Marco central para centrar todos los widgets
        self.central_frame_agregar = tk.Frame(self.ventana_agregar, bg='white')
        self.central_frame_agregar.place(relx=0.5, rely=0.5, anchor='center')

        #Campos Formulario

        #codigo
        self.agregar_codigo_label = tk.Label(self.central_frame_agregar, text='Código:', font=('Arial', 18), bg='white')
        self.agregar_codigo_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        vcmd_codigo = (self.register(self.on_validate), '%P', '4')
        self.agregar_codigo_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_codigo)
        self.agregar_codigo_entry.grid(row=0, column=1, padx=10, pady=10)
        self.agregar_codigo_entry.bind('<KeyRelease>', lambda e: self.verificar(self.agregar_codigo_entry))
        self.agregar_codigo_entry.focus_set()

        #numero
        self.agregar_numero_label = tk.Label(self.central_frame_agregar, text='Número:', font=('Arial', 18), bg='white')
        self.agregar_numero_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        vcmd_numero = (self.register(self.on_validate), '%P', '4')
        self.agregar_numero_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_numero)
        self.agregar_numero_entry.grid(row=1, column=1, padx=10, pady=10)
        self.agregar_numero_entry.bind('<KeyRelease>', lambda e: self.verificar(self.agregar_numero_entry))

        #tipo(normal, ejecutiva, suite)
        self.agregar_tipo_label = tk.Label(self.central_frame_agregar, text='Tipo:', font=('Arial', 18), bg='white')
        self.agregar_tipo_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.agregar_tipo_label = tk.Label(self.central_frame_agregar, text='Tipo:', font=('Arial', 18), bg='white')
        self.agregar_tipo_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.tipo_var = tk.StringVar()
        self.tipo_var.set("Normal")  #valor por defecto
        self.agregar_tipo_entry = ttk.Combobox(self.central_frame_agregar, textvariable=self.tipo_var, font=('Arial', 18), values=("Normal", "Ejecutiva", "Suite"), state='readonly')
        self.agregar_tipo_entry.grid(row=2, column=1, padx=10, pady=10)

        #capacidad(individual, matrimonial, doble, triple)
        self.agregar_capacidad_label = tk.Label(self.central_frame_agregar, text='Capacidad:', font=('Arial', 18), bg='white')
        self.agregar_capacidad_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.capacidad_var = tk.StringVar()
        self.capacidad_var.set("Individual")  # valor por defecto
        self.agregar_capacidad_entry = ttk.Combobox(self.central_frame_agregar, textvariable=self.capacidad_var, font=('Arial', 18), values=("Individual", "Matrimonial", "Doble", "Triple"), state='readonly')
        self.agregar_capacidad_entry.grid(row=3, column=1, padx=10, pady=10)

        #precio por noche en $USD
        self.agregar_precio_label = tk.Label(self.central_frame_agregar, text='Precio por Noche:', font=('Arial', 18), bg='white')
        self.agregar_precio_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        vcmd_precio = (self.register(self.on_validate), '%P', '12')
        self.agregar_precio_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_precio)
        self.agregar_precio_entry.grid(row=4, column=1, padx=10, pady=10)
        self.agregar_precio_entry.bind('<KeyRelease>', lambda e: self.verificar(self.agregar_precio_entry))

        #estado (ocupado/disponible)
        self.agregar_estado_label = tk.Label(self.central_frame_agregar, text='Estado:', font=('Arial', 18), bg='white')
        self.agregar_estado_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.estado_var = tk.StringVar()
        self.estado_var.set("Disponible")  #por defecto
        self.agregar_estado_entry = ttk.Combobox(self.central_frame_agregar, textvariable=self.estado_var, font=('Arial', 18), values=("Disponible", "Ocupado"), state='readonly')
        self.agregar_estado_entry.grid(row=5, column=1, padx=10, pady=10)

        # Botón para agregar habitación
        self.agregar_habitacion_boton = tk.Button(self.central_frame_agregar, text='Agregar', command=self.agregar_habitacion, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.agregar_habitacion_boton.grid(row=6, column=0, columnspan=2, pady=20)

    def agregar_habitacion(self):
        codigo = self.agregar_codigo_entry.get()
        numero = self.agregar_numero_entry.get()
        tipo = self.tipo_var.get()
        capacidad = self.capacidad_var.get()
        precio = self.agregar_precio_entry.get()
        estado = self.estado_var.get()
        if codigo and numero and tipo and capacidad and precio and estado:
            result = self.controller.agregar_habitacion(codigo, numero, tipo, capacidad, precio, estado)
            if result:
                messagebox.showinfo('Éxito', 'Habitación agregada correctamente')
                self.actualizar_tabla()
                self.ventana_agregar.destroy()
            else:
                messagebox.showerror('Error', 'No se pudo agregar la habitación')
        else:
            messagebox.showerror('Error', 'Todos los campos son obligatorios')


    #esto no se si esta bien es la ventana de editar 
    def abrir_ventana_editar(self):
        self.ventana_editar = tk.Toplevel(self.container, bg='white')
        self.ventana_editar.title('Editar Habitación')
        self.ventana_editar.geometry('800x600')
        self.ventana_editar.resizable(width=False, height=False)

        self.central_frame_editar = tk.Frame(self.ventana_editar, bg='white')
        self.central_frame_editar.place(relx=0.5, rely=0.5, anchor='center')

        self.editar_codigo_label = tk.Label(self.central_frame_editar, text='Código:', font=('Arial', 18), bg='white')
        self.editar_codigo_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.editar_codigo_var = tk.StringVar()
        self.editar_codigo_var.set('Elegir cod habitacion')
        self.editar_codigo_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.editar_codigo_var, font=('Arial', 18), state='readonly')
        editar_codigo_valores = self.listar_cod()
        self.editar_codigo_entry['values'] = editar_codigo_valores
        self.editar_codigo_entry.grid(row=0, column=1, padx=10, pady=10)

        self.editar_numero_label = tk.Label(self.central_frame_editar, text='Número:', font=('Arial', 18), bg='white')
        self.editar_numero_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        vcmd_ed_num = (self.register(self.on_validate), '%P', '4')
        self.editar_numero_entry = tk.Entry(self.central_frame_editar, font=('Arial', 18), validate='key', validatecommand=vcmd_ed_num)
        self.editar_numero_entry.grid(row=1, column=1, padx=10, pady=10)
        self.editar_numero_entry.bind('<KeyRelease>', lambda e: self.verificar(self.editar_numero_entry))

        self.tipo_var_editar = tk.StringVar()
        self.tipo_var_editar.set("Normal")
        self.editar_tipo_label = tk.Label(self.central_frame_editar, text='Tipo:', font=('Arial', 18), bg='white')
        self.editar_tipo_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.editar_tipo_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.tipo_var_editar, font=('Arial', 18), values=("Normal", "Ejecutiva", "Suite"))
        self.editar_tipo_entry.grid(row=2, column=1, padx=10, pady=10)

        self.capacidad_var_editar = tk.StringVar()
        self.capacidad_var_editar.set("Individual")
        self.editar_capacidad_label = tk.Label(self.central_frame_editar, text='Capacidad:', font=('Arial', 18), bg='white')
        self.editar_capacidad_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.editar_capacidad_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.capacidad_var_editar, font=('Arial', 18), values=("Individual", "Matrimonial", "Doble", "Triple"))
        self.editar_capacidad_entry.grid(row=3, column=1, padx=10, pady=10)

        self.editar_precio_label = tk.Label(self.central_frame_editar, text='Precio por Noche:', font=('Arial', 18), bg='white')
        self.editar_precio_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        vcmd_ed_pre = (self.register(self.on_validate), '%P', '12')
        self.editar_precio_entry = tk.Entry(self.central_frame_editar, font=('Arial', 18), validate='key', validatecommand=vcmd_ed_pre)
        self.editar_precio_entry.grid(row=4, column=1, padx=10, pady=10)
        self.editar_precio_entry.bind('<KeyRelease>', lambda e: self.on_validate(self.editar_precio_entry))

        self.estado_var_editar = tk.StringVar()
        self.estado_var_editar.set("Disponible")
        self.editar_estado_label = tk.Label(self.central_frame_editar, text='Estado:', font=('Arial', 18), bg='white')
        self.editar_estado_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        self.editar_estado_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.estado_var_editar, font=('Arial', 18), values=("Disponible", "Ocupado"), state='readonly')
        self.editar_estado_entry.grid(row=5, column=1, padx=10, pady=10)

        self.editar_habitacion_boton = tk.Button(self.central_frame_editar, text='Editar', command=self.actualizar_habitacion, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.editar_habitacion_boton = tk.Button(self.central_frame_editar, text='Editar', command=self.actualizar_habitacion, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.editar_habitacion_boton.grid(row=6, column=0, columnspan=2, pady=20)

#Crea una lista con los codigos de las habitaciones
    def listar_cod(self):
        result = self.controller.listar_codigo()
        return result

    def actualizar_habitacion(self):
        codigo = self.editar_codigo_entry.get()
        numero = self.editar_numero_entry.get()
        tipo = self.tipo_var_editar.get()
        capacidad = self.capacidad_var_editar.get()
        precio = self.editar_precio_entry.get()
        estado = self.estado_var_editar.get()
        if codigo:
            result = self.controller.actualizar_habitacion(codigo, numero, tipo, capacidad, precio, estado)
            if result:
                messagebox.showinfo('Éxito', 'Habitación editada correctamente')
                self.actualizar_tabla()
                self.ventana_editar.destroy()
            else:
                messagebox.showerror('Error', 'No se pudo editar la habitación')
        else:
            messagebox.showerror('Error', 'Todos los campos son obligatorios')

    def abrir_ventana_eliminar(self):
        self.ventana_eliminar = tk.Toplevel(self.container, bg='white')
        self.ventana_eliminar.title('Eliminar Habitación')
        self.ventana_eliminar.geometry('800x600')
        self.ventana_eliminar.resizable(width=False, height=False)

        #Marco central
        self.central_frame_eliminar = tk.Frame(self.ventana_eliminar, bg='white')
        self.central_frame_eliminar.place(relx=0.5, rely=0.5, anchor='center')

        #Lista desplegable para seleccionar cédula
        self.eliminar_cod_label = tk.Label(self.central_frame_eliminar, text='Cédula:', font=('Arial', 18), bg='white')
        self.eliminar_cod_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.eliminar_cod_combo = ttk.Combobox(self.central_frame_eliminar, state='readonly', font=('Arial', 18))
        self.opciones_eliminar = self.listar_cod()
        self.eliminar_cod_combo['values'] = self.opciones_eliminar
        self.eliminar_cod_combo.set('Seleccione un código:')
        self.eliminar_cod_combo.grid(row=0, column=1, padx=10, pady=10)

        def confirmar_eliminar():
            self.bell()
            confirmacion = messagebox.askyesno('Eliminar Huésped', '¿Desea eliminar la habitación seleccionada?')
            if confirmacion:
                self.eliminar_habitacion()
            else:
                self.eliminar_ventana()

        #Boton
        self.eliminar_habitacion_boton = tk.Button(self.central_frame_eliminar, text='Eliminar', command=confirmar_eliminar, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.eliminar_habitacion_boton.grid(row=1, column=0, columnspan=2, pady=20)

    def eliminar_habitacion(self):
        cod = self.eliminar_cod_combo.get()
        if cod != '':
            result = self.controller.eliminar_habitacion(cod)
            if result == True:
                messagebox.showinfo('¡Eliminación Exitosa!', 'La habitación ha sido eliminado de forma exitosa')
                self.actualizar_tabla()
            else:
                messagebox.showerror('Eliminación Fallida', result)
        else:
            messagebox.showerror('Eliminación Fallida', 'Debe seleccionar una cédula')

#actualizar
    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        self.lista_habitaciones = self.listar_habitaciones()
        if isinstance(self.lista_habitaciones, list):
            for i in self.lista_habitaciones:
                fila = self.tabla.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5]))

#listar
    def listar_habitaciones(self):
        result = self.controller.listar_habitaciones()
        return result

#volver al main
    def abrir_menu(self):
        from app import App
        self.destroy()
        app = App()
        app.mainloop()

    #Métodos que valida que la entrada sea numerica
    def verificar(self, entry):
        codigo = entry.get()
        for i in codigo:
            if i not in '0123456789-.':
                entry.delete(codigo.index(i), codigo.index(i)+1)

#validar longitud
    def on_validate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True

if __name__ == '__main__':
    app = HabitacionesView()
    app.mainloop()

"""selected_item = self.tabla.selection()
        if selected_item:
            item_values = self.tabla.item(selected_item, 'values')
            codigo = item_values[0]
            result = messagebox.askyesno('Confirmación', f'¿Estás seguro de eliminar la habitación con código {codigo}?')
            if result:
                if self.controller.eliminar_habitacion(codigo):
                    messagebox.showinfo('Éxito', 'Habitación eliminada correctamente')
                    self.actualizar_tabla()
                else:
                    messagebox.showerror('Error', 'No se pudo eliminar la habitación')
        else:
            messagebox.showerror('Error', 'Selecciona una habitación para eliminar')"""