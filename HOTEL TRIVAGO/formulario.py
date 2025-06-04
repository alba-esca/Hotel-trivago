import tkinter as tk
from tkinter import messagebox
import mysql.connector
#Formulario de tkinter de huespedes y habitaciones 
# Conectar a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="hotel"
    )

# Funciones para gestionar huéspedes
def agregar_huesped():
    cedula = cedula_entry.get()
    nombres = nombres_entry.get()
    apellidos = apellidos_entry.get()
    direccion = direccion_entry.get()
    ciudad = ciudad_entry.get()
    email = email_entry.get()
    telefono = telefono_entry.get()

    db = conectar_db()
    cursor = db.cursor()
    query = "INSERT INTO huespedes (cedula, nombres, apellidos, direccion, ciudad, email, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (cedula, nombres, apellidos, direccion, ciudad, email, telefono))
    db.commit()
    db.close()
    messagebox.showinfo("Éxito", "Huésped agregado correctamente")

# Funciones para gestionar habitaciones
def agregar_habitacion():
    codigo = codigo_entry.get()
    numero = numero_entry.get()
    tipo = tipo_var.get()
    capacidad = capacidad_var.get()
    precio = precio_entry.get()
    status = status_var.get()

    db = conectar_db()
    cursor = db.cursor()
    query = "INSERT INTO habitaciones (codigo, numero, tipo, capacidad, precio, status) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (codigo, numero, tipo, capacidad, precio, status))
    db.commit()
    db.close()
    messagebox.showinfo("Éxito", "Habitación agregada correctamente")

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Huéspedes y Habitaciones")

# Formulario para agregar huéspedes
tk.Label(root, text="Huéspedes").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Cédula:").grid(row=1, column=0)
cedula_entry = tk.Entry(root)
cedula_entry.grid(row=1, column=1)
tk.Label(root, text="Nombres:").grid(row=2, column=0)
nombres_entry = tk.Entry(root)
nombres_entry.grid(row=2, column=1)
tk.Label(root, text="Apellidos:").grid(row=3, column=0)
apellidos_entry = tk.Entry(root)
apellidos_entry.grid(row=3, column=1)
tk.Label(root, text="Dirección:").grid(row=4, column=0)
direccion_entry = tk.Entry(root)
direccion_entry.grid(row=4, column=1)
tk.Label(root, text="Ciudad:").grid(row=5, column=0)
ciudad_entry = tk.Entry(root)
ciudad_entry.grid(row=5, column=1)
tk.Label(root, text="Email:").grid(row=6, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=6, column=1)
tk.Label(root, text="Teléfono:").grid(row=7, column=0)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row=7, column=1)
tk.Button(root, text="Agregar Huésped", command=agregar_huesped).grid(row=8, column=0, columnspan=2)

# Formulario para agregar habitaciones
tk.Label(root, text="Habitaciones").grid(row=0, column=2, columnspan=2)
tk.Label(root, text="Código:").grid(row=1, column=2)
codigo_entry = tk.Entry(root)
codigo_entry.grid(row=1, column=3)
tk.Label(root, text="Número:").grid(row=2, column=2)
numero_entry = tk.Entry(root)
numero_entry.grid(row=2, column=3)
tk.Label(root, text="Tipo:").grid(row=3, column=2)
tipo_var = tk.StringVar(root)
tipo_var.set("Normal")
tipo_option = tk.OptionMenu(root, tipo_var, "Normal", "Ejecutiva", "Suite")
tipo_option.grid(row=3, column=3)
tk.Label(root, text="Capacidad:").grid(row=4, column=2)
capacidad_var = tk.StringVar(root)
capacidad_var.set("Individual")
capacidad_option = tk.OptionMenu(root, capacidad_var, "Individual", "Matrimonial", "Doble", "Triple")
capacidad_option.grid(row=4, column=3)
tk.Label(root, text="Precio:").grid(row=5, column=2)
precio_entry = tk.Entry(root)
precio_entry.grid(row=5, column=3)
tk.Label(root, text="Status:").grid(row=6, column=2)
status_var = tk.StringVar(root)
status_var.set("Disponible")
status_option = tk.OptionMenu(root, status_var, "Disponible", "Ocupada")
status_option.grid(row=6, column=3)
tk.Button(root, text="Agregar Habitación", command=agregar_habitacion).grid(row=7, column=2, columnspan=2)

root.mainloop()