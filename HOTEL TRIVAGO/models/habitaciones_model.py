#Se encarga de la base de datos y las consultas SQL.
import mysql.connector

class ConexionDB:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
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

    def insertar_habitacion(self, cod, num, tip, cap, pre, stat):
        try:
            consulta = f'SELECT * FROM habitacion WHERE num_hab={num}'
            conf = self.obtener_datos(consulta)
            if conf != None:
                try:
                    consulta = 'INSERT INTO habitacion VALUES(%s, %s, "%s", "%s", %s, "%s")'
                    self.ejecutar_consulta(consulta, (cod, num, tip, cap, pre, stat))
                    self.cerrar_conexion()
                    result = True
                    return result
                except mysql.connector.Error as e:
                    return e
            else:
                e = f'La habitación número {num} ya se encuentra registrada'
                return e
        except mysql.connector.Error as e:
            return e