import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from views.base_view import MainView
from PIL import Image, ImageTk
from controller.huespedes_controller import HuespedesController

class HuespedesView(MainView):
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
        self.titulo_principal = tk.Label(self.container, text='Módulo de huéspedes', font=('Arial', 24), bg='white')
        self.titulo_principal.place(relx=0.5, rely=0.1, anchor='center')#NO MOVER!!

        # Frame central para centrar la tabla y el botón NO MOVER!
        self.central_frame = tk.Frame(self.container, bg='white')
        self.central_frame.pack(expand=True)

        # Inicializar el controlador
        self.controller = HuespedesController()

        # Tabla de huéspedes
        self.tabla = ttk.Treeview(self.central_frame)
        self.tabla['columns'] = ('ced', 'ape', 'nom', 'dir', 'ciu', 'email', 'tel')
        self.tabla.column('#0', width=0, minwidth=0, stretch=tk.NO)
        self.tabla.column('ced', anchor=tk.W, width=120)
        self.tabla.column('ape', anchor=tk.W, width=120)
        self.tabla.column('nom', anchor=tk.W, width=120)
        self.tabla.column('dir', anchor=tk.W, width=220)
        self.tabla.column('ciu', anchor=tk.W, width=120)
        self.tabla.column('email', anchor=tk.W, width=120)
        self.tabla.column('tel', anchor=tk.W, width=120)

        self.tabla.heading('ced', text='Cédula', anchor=tk.W)
        self.tabla.heading('ape', text='Apellido', anchor=tk.W)
        self.tabla.heading('nom', text='Nombre', anchor=tk.W)
        self.tabla.heading('dir', text='Dirección', anchor=tk.W)
        self.tabla.heading('ciu', text='Ciudad', anchor=tk.W)
        self.tabla.heading('email', text='Email', anchor=tk.W)
        self.tabla.heading('tel', text='Teléfono', anchor=tk.W)

        self.lista_huespedes = self.listar_huespedes()
        if isinstance(self.lista_huespedes, list):
            for i in self.lista_huespedes:
                fila = self.tabla.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

        # Centrar la tabla en el frame central
        self.tabla.pack(pady=20)

        # Contenedor intermedio para los botones
        self.botones_frame = tk.Frame(self.central_frame)
        self.botones_frame.pack()

        # Botones de abajo
        self.agregar_boton = tk.Button(self.botones_frame, text='Agregar', font=('Arial', 12), command=self.abrir_ventana_agregar)
        self.agregar_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.agregar_boton.grid(row=0, column=0, padx=10, pady=10)

        self.actualizar_boton = tk.Button(self.botones_frame, text='Actualizar', font=('Arial', 12), command=self.actualizar_ventana)
        self.actualizar_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.actualizar_boton.grid(row=0, column=1, padx=10, pady=10)

        self.eliminar_boton = tk.Button(self.botones_frame, text='Eliminar', font=('Arial', 12), command=self.eliminar_ventana)
        self.eliminar_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.eliminar_boton.grid(row=0, column=2, padx=10, pady=10)

        self.menu_boton = tk.Button(self.botones_frame, text='Menú', font=('Arial', 12), command=self.abrir_menu)
        self.menu_boton.config(height=2, width=10, relief=tk.GROOVE, borderwidth=4, bg='blue', fg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=2, bd=0, activebackground='skyblue', activeforeground='white')
        self.menu_boton.grid(row=0, column=3, padx=10, pady=10)

        # Centrar el frame central en la ventana
        self.central_frame.pack(expand=True)


        #Ventana de agregar huespedes
    def abrir_ventana_agregar(self):
        self.ventana_agregar = tk.Toplevel(self.container, bg='white')
        self.ventana_agregar.title('Agregar Huesped')
        self.ventana_agregar.geometry('800x600')
        self.ventana_agregar.resizable(width=False, height=False)

        # Marco central para centrar todos los widgets
        self.central_frame_agregar = tk.Frame(self.ventana_agregar, bg='white')
        self.central_frame_agregar.place(relx=0.5, rely=0.5, anchor='center')

        self.agregar_ced_label = tk.Label(self.central_frame_agregar, text='Cédula:', font=('Arial', 18), bg='white')
        self.agregar_ced_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        vcmd_ced = (self.register(self.on_validate), '%P', '8')
        self.agregar_ced_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_ced)
        self.agregar_ced_entry.grid(row=0, column=1, padx=10, pady=10)
        self.agregar_ced_entry.bind('<KeyRelease>', lambda e:self.verificar(self.agregar_ced_entry))
        self.agregar_ced_entry.focus_set()

        self.agregar_ape_label = tk.Label(self.central_frame_agregar, text='Apellido:', font=('Arial', 18), bg='white')
        self.agregar_ape_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        vcmd_ape = (self.register(self.on_validate), '%P', '15')
        self.agregar_ape_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_ape)
        self.agregar_ape_entry.grid(row=1, column=1, padx=10, pady=10)

        self.agregar_nom_label = tk.Label(self.central_frame_agregar, text='Nombre:', font=('Arial', 18), bg='white')
        self.agregar_nom_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        vcmd_nom = (self.register(self.on_validate), '%P', '15')
        self.agregar_nom_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_nom)
        self.agregar_nom_entry.grid(row=2, column=1, padx=10, pady=10)

        self.agregar_dir_label = tk.Label(self.central_frame_agregar, text='Dirección:', font=('Arial', 18), bg='white')
        self.agregar_dir_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        vcmd_dir = (self.register(self.on_validate), '%P', '30')
        self.agregar_dir_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_dir)
        self.agregar_dir_entry.grid(row=3, column=1, padx=10, pady=10)

        self.agregar_ciu_label = tk.Label(self.central_frame_agregar, text='Ciudad:', font=('Arial', 18), bg='white')
        self.agregar_ciu_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        vcmd_ciu = (self.register(self.on_validate), '%P', '15')
        self.agregar_ciu_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_ciu)
        self.agregar_ciu_entry.grid(row=4, column=1, padx=10, pady=10)

        self.agregar_email_label = tk.Label(self.central_frame_agregar, text='Email:', font=('Arial', 18), bg='white')
        self.agregar_email_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        vmcd_email = (self.register(self.on_validate), '%P', '20')
        self.agregar_email_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vmcd_email)
        self.agregar_email_entry.grid(row=5, column=1, padx=10, pady=10)

        self.agregar_tel_label = tk.Label(self.central_frame_agregar, text='Teléfono:', font=('Arial', 18), bg='white')
        self.agregar_tel_label.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        vcmd_tel = (self.register(self.on_validate), '%P', '12')
        self.agregar_tel_entry = tk.Entry(self.central_frame_agregar, font=('Arial', 18), validate='key', validatecommand=vcmd_tel)
        self.agregar_tel_entry.grid(row=6, column=1, padx=10, pady=10)
        self.agregar_tel_entry.bind('<KeyRelease>', lambda e: self.verificar(self.agregar_tel_entry))
        #Boton
        self.agregar_huesped_boton = tk.Button(self.central_frame_agregar, text='Agregar', command=self.agregar_huesped, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.agregar_huesped_boton.grid(row=7, column=0, columnspan=2, pady=20)

    #Ventana de actualizar huespedes
    def actualizar_ventana(self):
        self.ventana_actualizar = tk.Toplevel(self.container, bg='white')
        self.ventana_actualizar.title('Actualizar Huesped')
        self.ventana_actualizar.geometry('800x600')
        self.ventana_actualizar.resizable(width=False, height=False)

        #Marco central
        self.central_frame_actualizar = tk.Frame(self.ventana_actualizar, bg='white')
        self.central_frame_actualizar.place(relx=0.5, rely=0.5, anchor='center')

        #Lista desplegable para seleccionar cédula
        self.actualizar_ced_label = tk.Label(self.central_frame_actualizar, text='Cédula:', font=('Arial', 18), bg='white')
        self.actualizar_ced_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.ced_combo = ttk.Combobox(self.central_frame_actualizar, state='readonly', font=('Arial', 18))
        self.opciones_actualizar = self.listar_ced()
        self.ced_combo['values'] = self.opciones_actualizar
        self.ced_combo.set('Seleccione una cédula:')
        self.ced_combo.grid(row=0, column=1, padx=10, pady=10)

        self.actualizar_ape_label = tk.Label(self.central_frame_actualizar, text='Apellido:', font=('Arial', 18), bg='white')
        self.actualizar_ape_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        vcmd_ape = (self.register(self.on_validate), '%P', '15')
        self.actualizar_ape_entry = tk.Entry(self.central_frame_actualizar, font=('Arial', 18), validate='key', validatecommand=vcmd_ape)
        self.actualizar_ape_entry.grid(row=1, column=1, padx=10, pady=10)

        self.actualizar_nom_label = tk.Label(self.central_frame_actualizar, text='Nombre:', font=('Arial', 18), bg='white')
        self.actualizar_nom_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        vcmd_nom = (self.register(self.on_validate), '%P', '15')
        self.actualizar_nom_entry = tk.Entry(self.central_frame_actualizar, font=('Arial', 18), validate='key', validatecommand=vcmd_nom)
        self.actualizar_nom_entry.grid(row=2, column=1, padx=10, pady=10)

        self.actualizar_dir_label = tk.Label(self.central_frame_actualizar, text='Dirección:', font=('Arial', 18), bg='white')
        self.actualizar_dir_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        vcmd_dir = (self.register(self.on_validate), '%P', '30')
        self.actualizar_dir_entry = tk.Entry(self.central_frame_actualizar, font=('Arial', 18), validate='key', validatecommand=vcmd_dir)
        self.actualizar_dir_entry.grid(row=3, column=1, padx=10, pady=10)

        self.actualizar_ciu_label = tk.Label(self.central_frame_actualizar, text='Ciudad:', font=('Arial', 18), bg='white')
        self.actualizar_ciu_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        vcmd_ciu = (self.register(self.on_validate), '%P', '15')
        self.actualizar_ciu_entry = tk.Entry(self.central_frame_actualizar, font=('Arial', 18), validate='key', validatecommand=vcmd_ciu)
        self.actualizar_ciu_entry.grid(row=4, column=1, padx=10, pady=10)

        self.actualizar_email_label = tk.Label(self.central_frame_actualizar, text='Email:', font=('Arial', 18), bg='white')
        self.actualizar_email_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
        vcmd_email = (self.register(self.on_validate), '%P', '20')
        self.actualizar_email_entry = tk.Entry(self.central_frame_actualizar, font=('Arial', 18), validate='key', validatecommand=vcmd_email)
        self.actualizar_email_entry.grid(row=5, column=1, padx=10, pady=10)

        self.actualizar_tel_label = tk.Label(self.central_frame_actualizar, text='Teléfono:', font=('Arial', 18), bg='white')
        self.actualizar_tel_label.grid(row=6, column=0, padx=10, pady=10, sticky='e')
        vcmd_tel = (self.register(self.on_validate), '%P', '12')
        self.actualizar_tel_entry = tk.Entry(self.central_frame_actualizar, font=('Arial', 18), validate='key', validatecommand=vcmd_tel)
        self.actualizar_tel_entry.grid(row=6, column=1, padx=10, pady=10)
        self.actualizar_tel_entry.bind('<KeyRelease>', lambda e: self.verificar(self.actualizar_tel_entry))

        #Boton
        self.actualizar_huesped_boton = tk.Button(self.central_frame_actualizar, text='Actualizar', command=self.actualizar_huesped, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.actualizar_huesped_boton.grid(row=7, column=0, columnspan=2, pady=20)

    #Ventana para eliminar
    def eliminar_ventana(self):
        self.ventana_eliminar = tk.Toplevel(self.container, bg='white')
        self.ventana_eliminar.title('Eliminar Huesped')
        self.ventana_eliminar.geometry('800x600')
        self.ventana_eliminar.resizable(width=False, height=False)

        #Marco central
        self.central_frame_eliminar = tk.Frame(self.ventana_eliminar, bg='white')
        self.central_frame_eliminar.place(relx=0.5, rely=0.5, anchor='center')

        #Lista desplegable para seleccionar cédula
        self.eliminar_ced_label = tk.Label(self.central_frame_eliminar, text='Cédula:', font=('Arial', 18), bg='white')
        self.eliminar_ced_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.eliminar_ced_combo = ttk.Combobox(self.central_frame_eliminar, state='readonly', font=('Arial', 18))
        self.opciones_eliminar = self.listar_ced()
        self.eliminar_ced_combo['values'] = self.opciones_eliminar
        self.eliminar_ced_combo.set('Seleccione una cédula:')
        self.eliminar_ced_combo.grid(row=0, column=1, padx=10, pady=10)

        def confirmar_eliminar():
            self.bell()
            confirmacion = messagebox.askyesno('Eliminar Huésped', '¿Desea eliminar el huésped seleccionado?')
            if confirmacion:
                self.eliminar_huesped()
            else:
                self.eliminar_ventana()

        #Boton
        self.eliminar_huesped_boton = tk.Button(self.central_frame_eliminar, text='Eliminar', command=confirmar_eliminar, bg='blue', fg='white', font=('Arial', 12, 'bold'))
        self.eliminar_huesped_boton.grid(row=1, column=0, columnspan=2, pady=20)

    def listar_huespedes(self):
        result = self.controller.listar_huespedes()
        return result

    def listar_ced(self):
        result = self.controller.listar_ced()
        return result

    def agregar_huesped(self):
        ced = self.agregar_ced_entry.get()
        ape = self.agregar_ape_entry.get()
        nom = self.agregar_nom_entry.get()
        dir = self.agregar_dir_entry.get()
        ciu = self.agregar_ciu_entry.get()
        email = self.agregar_email_entry.get()
        tel = self.agregar_tel_entry.get()
        if ced != '' and ape !='' and nom != '' and dir != '' and ciu != '' and email != '' and tel != '':
            result = self.controller.agregar_huesped(ced, ape, nom, dir, ciu, email, tel)
            if result == True:
                messagebox.showinfo('¡Registro Exitoso!', f'El huesped {nom} ha sido registrado de forma exitosa')
                self.agregar_ced_entry.delete(0, tk.END)
                self.agregar_ape_entry.delete(0, tk.END)
                self.agregar_nom_entry.delete(0, tk.END)
                self.agregar_dir_entry.delete(0, tk.END)
                self.agregar_ciu_entry.delete(0, tk.END)
                self.agregar_email_entry.delete(0, tk.END)
                self.agregar_tel_entry.delete(0, tk.END)
                self.actualizar_tabla()
            else:
                messagebox.showerror('Registro Fallido', result)
        else:
            messagebox.showerror('Registro Fallido', 'Debe rellenar todos los campos')

    def actualizar_huesped(self):
        ced = self.ced_combo.get()
        ape = self.actualizar_ape_entry.get()
        nom = self.actualizar_nom_entry.get()
        dir = self.actualizar_dir_entry.get()
        ciu = self.actualizar_ciu_entry.get()
        email = self.actualizar_email_entry.get()
        tel = self.actualizar_tel_entry.get()
        if ced != '':
            result = self.controller.actualizar_huesped(ced, ape, nom, dir, ciu, email, tel)
            if result == True:
                messagebox.showinfo('¡Actualización Exitosa!', f'Huésped con la cédula {ced} actualizado de forma exitosa')
                self.actualizar_ape_entry.delete(0, tk.END)
                self.actualizar_nom_entry.delete(0, tk.END)
                self.actualizar_dir_entry.delete(0, tk.END)
                self.actualizar_ciu_entry.delete(0, tk.END)
                self.actualizar_email_entry.delete(0, tk.END)
                self.actualizar_tel_entry.delete(0, tk.END)
                self.actualizar_tabla()
            else:
                messagebox.showerror('Actualización Fallida', result)
        else:
            messagebox.showerror('Actualización Fallida', 'Debe seleccionar una cédula')

    def eliminar_huesped(self):
        ced = self.eliminar_ced_combo.get()
        if ced != '':
            result = self.controller.eliminar_huesped(ced)
            if result == True:
                messagebox.showinfo('¡Eliminación Exitosa!', 'El huésped ha sido eliminado de forma exitosa')
                self.actualizar_tabla()
            else:
                messagebox.showerror('Eliminación Fallida', result)
        else:
            messagebox.showerror('Eliminación Fallida', 'Debe seleccionar una cédula')

    #actualizar
    def actualizar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        self.lista_huespedes = self.listar_huespedes()
        if isinstance(self.lista_huespedes, list):
            for i in self.lista_huespedes:
                fila = self.tabla.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    def abrir_menu(self):
        from app import App
        self.destroy()
        app = App()
        app.mainloop()

    def recargar(self):
        self.destroy()
        app = HuespedesView()
        app.mainloop()

    #Métodos que valida que la entrada sea numerica
    def verificar(self, entry):
        codigo = entry.get()
        for i in codigo:
            if i not in '0123456789-':
                entry.delete(codigo.index(i), codigo.index(i)+1)

    def on_validate(self, P, L):
        if len(P) > int(L):
            self.bell()
            return False
        return True

if __name__ == '__main__':
    app = HuespedesView()
    app.mainloop()