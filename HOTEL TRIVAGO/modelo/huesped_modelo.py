#Se encarga de la base de datos y las consultas SQL.
#lo que hizo isra en clases
import mysql.connector

class ConexionDB:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="hospedaje"
        )
        self.cursor = self.conexion.cursor()

    def ejecutar_consulta(self, consulta, valores=None):
        self.cursor.execute(consulta, valores)
        self.conexion.commit()

    def obtener_datos(self, consulta):
        self.cursor.execute(consulta)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

"""try: #Insertar informacion
    ci = input('Cedula: ')
    ape = input('Apellido: ')
    nom = input('Nombre: ')
    direc = input('Direccion: ')
    ciu = input('Ciudad: ')
    email = input('Email: ')
    tel = input('Telefono: ')
    cursor.execute(f'INSERT INTO huesped VALUES("{ci}", "{ape}", "{nom}", "{direc}", "{ciu}", "{email}", "{tel}")')
    conn.commit()
except mysql.connector.Error as e:
    print(e)"""

"""try: #Actualizar
    ced = input('Cedula: ')
    nom = input('Nuevo nombre: ')
    cursor.execute(f'UPDATE huesped SET nom_hue="{nom}" WHERE ced_hue="{ced}"')
    conn.commit()
except mysql.connector.Error as e:
    print(e)"""

try: #Borrar
    ced = input('Cedula: ')
    cursor.execute(f'DELETE FROM huesped WHERE ced_hue="{ced}"')
    conn.commit()
except mysql.connector.Error as e:
    print(e)

try: #Seleccionar informacion
    cursor.execute('SELECT * FROM huesped')
    x = cursor.fetchall()
    print(x)
except mysql.connector.Error as e:
    print(e)