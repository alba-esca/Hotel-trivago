import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from controller.ingresos_controller import IngresosController  

class IngresosView(tk.Tk):
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
        self.titulo_principal = tk.Label(self.container, text='Módulo de Ingresos', font=('Arial', 24), bg='white')
        self.titulo_principal.place(relx=0.5, rely=0.1, anchor='center')  # NO MOVER!!

        # Frame central para centrar la tabla y el botón NO MOVER!
        self.central_frame = tk.Frame(self.container, bg='white')
        self.central_frame.pack(expand=True)

        # Inicializar el controlador
        self.controller = IngresosController()

        # Tabla de ingresos
        self.tabla = ttk.Treeview(self.central_frame)
        self.tabla['columns'] = ('codigo', 'cedula', 'codigo_habitacion', 'fecha_ingreso', 'fecha_salida', 'ocupantes')
        self.tabla.column('#0', width=0, minwidth=0, stretch=tk.NO)
        self.tabla.column('codigo', anchor=tk.W, width=120)
        self.tabla.column('cedula', anchor=tk.W, width=120)
        self.tabla.column('codigo_habitacion', anchor=tk.W, width=120)
        self.tabla.column('fecha_ingreso', anchor=tk.W, width=120)
        self.tabla.column('fecha_salida', anchor=tk.W, width=120)
        self.tabla.column('ocupantes', anchor=tk.W, width=120)

        self.tabla.heading('codigo', text='Código', anchor=tk.W)
        self.tabla.heading('cedula', text='Cédula de Huésped', anchor=tk.W)
        self.tabla.heading('codigo_habitacion', text='Código de Habitación', anchor=tk.W)
        self.tabla.heading('fecha_ingreso', text='Fecha de Ingreso', anchor=tk.W)
        self.tabla.heading('fecha_salida', text='Fecha de Salida', anchor=tk.W)
        self.tabla.heading('ocupantes', text='Ocupantes', anchor=tk.W)

        self.lista_ingresos = self.listar_ingresos()
        if isinstance(self.lista_ingresos, list):
            for i in self.lista_ingresos:
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

#Ventana de agregar ingreso
    def abrir_ventana_agregar(self):
        self.ventana_agregar = tk.Toplevel(self.container, bg='white')
        self.ventana_agregar.title('Agregar Ingreso')
        self.ventana_agregar.geometry('800x600')
        self.ventana_agregar.resizable(width=False, height=False)

        # Marco central para centrar todos los widgets
        self.central_frame_agregar = tk.Frame(self.ventana_agregar, bg='white')
        self.central_frame_agregar.place(relx=0.5, rely=0.5, anchor='center')

        # Campos Formulario
        # Cedula de huesped
        #cambiar a lista
        #Lista desplegable para seleccionar cédula
        self.actualizaragregar_ced_label = tk.Label(self.central_frame_agregar, text='Cédula:', font=('Arial', 18), bg='white')
        self.actualizaragregar_ced_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.agregar_ced_combo = ttk.Combobox(self.central_frame_agregar, state='readonly', font=('Arial', 18))
        self.opciones_agregar = self.listar_ced()
        self.agregar_ced_combo['values'] = self.opciones_agregar
        self.agregar_ced_combo.set('Seleccione una cédula:')
        self.agregar_ced_combo.grid(row=0, column=1, padx=10, pady=10)

        # Codigo de habitacion asignada
        #Cambiar a lista
        self.actualizaragregar_cod_hab_label = tk.Label(self.central_frame_agregar, text='Código Habitación:', font=('Arial', 18), bg='white')
        self.actualizaragregar_cod_hab_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.agregar_cod_hab_combo = ttk.Combobox(self.central_frame_agregar, state='readonly', font=('Arial', 18))
        self.opciones_cod_hab_agregar = self.listar_cod_hab()
        self.agregar_cod_hab_combo['values'] = self.opciones_cod_hab_agregar
        self.agregar_cod_hab_combo.set('Seleccione una habitación:')
        self.agregar_cod_hab_combo.grid(row=1, column=1, padx=10, pady=10)

        # Fecha de ingreso
        self.agregar_fec_ing_label = tk.Label(self.central_frame_agregar, text='Fecha de ingreso:', font=('Arial', 18), bg='white')
        self.agregar_fec_ing_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.agregar_fec_ing_entry = DateEntry(self.central_frame_agregar, borderwidth=2, date_pattern='dd/mm/yyyy', state='readonly', font=('Arial', 18), bg='white')
        self.agregar_fec_ing_entry.grid(row=2, column=1, padx=10, pady=10)

        # Fecha de salida
        self.agregar_fec_sal_label = tk.Label(self.central_frame_agregar, text='Fecha de salida:', font=('Arial', 18), bg='white')
        self.agregar_fec_sal_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.agregar_fec_sal_entry = DateEntry(self.central_frame_agregar, borderwidth=2, date_pattern='dd/mm/yyyy', state='readonly', font=('Arial', 18), bg='white')
        self.agregar_fec_sal_entry.grid(row=3, column=1, padx=10, pady=10)

        # Cantidad de ocupantes
        self.agregar_ocupantes_label = tk.Label(self.central_frame_agregar, text='Cantidad de Ocupantes:', font=('Arial', 18), bg='white')
        self.agregar_ocupantes_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        vcmd_ocupantes = (self.register(self.on_validate), '%P', '4')
        self.agregar_ocupantes_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_ocupantes)
        self.agregar_ocupantes_entry.grid(row=4, column=1, padx=10, pady=10)
        self.agregar_ocupantes_entry.bind('<KeyRelease>', lambda e: self.verificar(self.agregar_ocupantes_entry))

        # Botón para agregar ingreso
        self.agregar_ingreso_boton = tk.Button(self.central_frame_agregar, text='Agregar', command=self.agregar_ingreso, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.agregar_ingreso_boton.grid(row=6, column=0, columnspan=2, pady=20)

#Ventana de ingreso agregado
    def agregar_ingreso(self):
        cedula = self.agregar_ced_combo.get()
        codigo_habitacion = self.agregar_cod_hab_combo.get()
        fecha_ingreso = self.agregar_fec_ing_entry.get_date()
        fecha_salida = self.agregar_fec_sal_entry.get_date()
        ocupantes = self.agregar_ocupantes_entry.get()
        if cedula and codigo_habitacion and fecha_ingreso and fecha_salida and ocupantes:
            result = self.controller.agregar_ingreso(cedula, codigo_habitacion, fecha_ingreso, fecha_salida, ocupantes)
            if result == True:
                messagebox.showinfo('Éxito', 'Ingreso agregado correctamente')
                self.actualizar_tabla()
                self.ventana_agregar.destroy()
            else:
                messagebox.showerror('Error', result)
                self.ventana_agregar.destroy()
        else:
            messagebox.showerror('Error', 'Todos los campos son obligatorios')

        ##Ventana de editar
    def abrir_ventana_editar(self):
        self.ventana_editar = tk.Toplevel(self.container, bg='white')
        self.ventana_editar.title('Editar Ingreso')
        self.ventana_editar.geometry('800x600')
        self.ventana_editar.resizable(width=False, height=False)

        self.central_frame_editar = tk.Frame(self.ventana_editar, bg='white')
        self.central_frame_editar.place(relx=0.5, rely=0.5, anchor='center')

        # Código de Ingreso
        self.editar_codigo_label = tk.Label(self.central_frame_editar, text='Código de Ingreso:', font=('Arial', 18), bg='white')
        self.editar_codigo_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.editar_codigo_var = tk.StringVar()
        self.editar_codigo_var.set('Elegir código de ingreso')
        self.editar_codigo_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.editar_codigo_var, font=('Arial', 18), state='readonly')
        editar_codigo_valores = self.listar_codigos_ingreso()
        self.editar_codigo_entry['values'] = editar_codigo_valores
        self.editar_codigo_entry.grid(row=0, column=1, padx=10, pady=10)

        # Cédula de Huésped
        self.editar_cedula_label = tk.Label(self.central_frame_editar, text='Cédula de Huésped:', font=('Arial', 18), bg='white')
        self.editar_cedula_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.editar_cedula_var = tk.StringVar()
        self.editar_cedula_var.set('')
        self.editar_cedula_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.editar_cedula_var, font=('Arial', 18), state='readonly')
        editar_cedula_valores = self.listar_ced()
        self.editar_cedula_entry['values'] = editar_cedula_valores
        self.editar_cedula_entry.grid(row=1, column=1, padx=10, pady=10)

        # Código de Habitación
        self.editar_codigo_habitacion_label = tk.Label(self.central_frame_editar, text='Código de Habitación:', font=('Arial', 18), bg='white')
        self.editar_codigo_habitacion_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.editar_codigo_habitacion_var = tk.StringVar()
        self.editar_codigo_habitacion_var.set('')
        self.editar_codigo_habitacion_entry = ttk.Combobox(self.central_frame_editar, textvariable=self.editar_codigo_habitacion_var, font=('Arial', 18), state='readonly')
        editar_codigo_habitacion_valores = self.listar_cod_hab()
        self.editar_codigo_habitacion_entry['values'] = editar_codigo_habitacion_valores
        self.editar_codigo_habitacion_entry.grid(row=2, column=1, padx=10, pady=10)

        # Fecha de Ingreso
        self.editar_fecha_ingreso_label = tk.Label(self.central_frame_editar, text='Fecha de Ingreso:', font=('Arial', 18), bg='white')
        self.editar_fecha_ingreso_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.editar_fecha_ingreso_entry = DateEntry(self.central_frame_editar, borderwidth=2, date_pattern='dd/mm/yyyy', state='readonly', font=('Arial', 18), bg='white')
        self.editar_fecha_ingreso_entry.grid(row=3, column=1, padx=10, pady=10)

        # Fecha de Salida
        self.editar_fecha_salida_label = tk.Label(self.central_frame_editar, text='Fecha de Salida:', font=('Arial', 18), bg='white')
        self.editar_fecha_salida_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        self.editar_fecha_salida_entry = DateEntry(self.central_frame_editar, borderwidth=2, date_pattern='dd/mm/yyyy', state='readonly', font=('Arial', 18), bg='white')
        self.editar_fecha_salida_entry.grid(row=4, column=1, padx=10, pady=10)

        # Cantidad de Ocupantes
        self.editar_ocupantes_label = tk.Label(self.central_frame_editar, text='Cantidad de Ocupantes:', font=('Arial', 18), bg='white')
        self.editar_ocupantes_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        vcmd_ed_ocupantes = (self.register(self.on_validate), '%P', '4')
        self.editar_ocupantes_entry = tk.Entry(self.central_frame_editar, font=('Arial', 18), validate='key', validatecommand=vcmd_ed_ocupantes)
        self.editar_ocupantes_entry.grid(row=5, column=1, padx=10, pady=10)
        self.editar_ocupantes_entry.bind('<KeyRelease>', lambda e: self.verificar(self.editar_ocupantes_entry))

        # Botón de Editar
        self.editar_boton = tk.Button(self.central_frame_editar, text='Editar', command=self.editar_ingreso, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.editar_boton.grid(row=6, column=0, columnspan=2, pady=20)

#confiermar ingreso 
    def editar_ingreso(self):
        codigo = self.editar_codigo_entry.get()
        cedula = self.editar_cedula_entry.get()
        codigo_habitacion = self.editar_codigo_habitacion_entry.get()
        fecha_ingreso = self.editar_fecha_ingreso_entry.get_date()
        fecha_salida = self.editar_fecha_salida_entry.get_date()
        ocupantes = self.editar_ocupantes_entry.get()
        if codigo:
            result = self.controller.editar_ingreso(codigo, cedula, codigo_habitacion, fecha_ingreso, fecha_salida, ocupantes)
            if result:
                messagebox.showinfo('Éxito', 'Ingreso editado correctamente')
                self.actualizar_tabla()
                self.ventana_editar.destroy()
            else:
                messagebox.showerror('Error', 'No se pudo editar el ingreso')
        else:
            messagebox.showerror('Error', 'Todos los campos son obligatorios')

    #Ventana eliminar
    def abrir_ventana_eliminar(self):
        self.ventana_eliminar = tk.Toplevel(self.container, bg='white')
        self.ventana_eliminar.title('Eliminar Ingreso')
        self.ventana_eliminar.geometry('800x600')
        self.ventana_eliminar.resizable(width=False, height=False)

        self.central_frame_eliminar = tk.Frame(self.ventana_eliminar, bg='white')
        self.central_frame_eliminar.place(relx=0.5, rely=0.5, anchor='center')

        self.eliminar_codigo_label = tk.Label(self.central_frame_eliminar, text='Código de Ingreso:', font=('Arial', 18), bg='white')
        self.eliminar_codigo_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.eliminar_codigo_var = tk.StringVar()
        self.eliminar_codigo_var.set('Elegir código de ingreso')
        self.eliminar_codigo_entry = ttk.Combobox(self.central_frame_eliminar, textvariable=self.eliminar_codigo_var, font=('Arial', 18), state='readonly')
        eliminar_codigo_valores = self.listar_codigos_ingreso()
        self.eliminar_codigo_entry['values'] = eliminar_codigo_valores
        self.eliminar_codigo_entry.grid(row=0, column=1, padx=10, pady=10)

        def confirmar_eliminar():
            self.bell()
            confirmacion = messagebox.askyesno('Eliminar Ingreso', '¿Desea eliminar el ingreso?')
            if confirmacion:
                self.eliminar_ingreso()

        # Botón para eliminar ingreso
        self.eliminar_ingreso_boton = tk.Button(self.central_frame_eliminar, text='Eliminar', command=confirmar_eliminar, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.eliminar_ingreso_boton.grid(row=1, column=0, columnspan=2, pady=20)

    #metodos auxiliares
    def eliminar_ingreso(self):
        codigo = self.eliminar_codigo_entry.get()
        if codigo:
            result = self.controller.eliminar_ingreso(codigo)
            if result:
                messagebox.showinfo('Éxito', 'Ingreso eliminado correctamente')
                self.actualizar_tabla()
                self.ventana_eliminar.destroy()
            else:
                messagebox.showerror('Error', 'No se pudo eliminar el ingreso')
        else:
            messagebox.showerror('Error', 'Debe seleccionar un código de ingreso')


    def listar_ingresos(self):
        # controlador para obtener la lista de ingresos
        result = self.controller.listar_ingresos()
        return result

    def listar_ced(self):
        # controlador para obtener la lista de cédulas
        result = self.controller.listar_ced()
        return result

    def listar_cod_hab(self):
        # controlador para obtener la lista de códigos de habitación
        result = self.controller.listar_cod_hab()
        return result

    def listar_codigos_ingreso(self):
        # controlador para obtener la lista de códigos de ingreso
        result = self.controller.listar_codigos_ingreso()
        return result

    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        self.lista_ingresos = self.listar_ingresos()
        if isinstance(self.lista_ingresos, list):
            for i in self.lista_ingresos:
                fila = self.tabla.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5]))

    def listar_codigos_ingreso(self):
        result = self.controller.listar_codigos_ingreso()
        return result

    def listar_ingresos(self):
        result = self.controller.listar_ingresos()
        return result

    def listar_ced(self):
        result = self.controller.listar_ced()
        return result

    def listar_cod_hab(self):
        result = self.controller.listar_cod_hab()
        return result

    def abrir_menu(self):
        from app import App
        self.destroy()
        app = App()
        app.mainloop()

    def verificar(self, entry):
        codigo = entry.get()
        for i in codigo:
            if i not in '0123456789-.':
                entry.delete(codigo.index(i), codigo.index(i)+1)

    def on_validate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True

if __name__ == '__main__':
    app = IngresosView()
    app.mainloop()