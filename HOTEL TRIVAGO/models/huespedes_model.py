#Se encarga de la base de datos y las consultas SQL.
import mysql.connector

class ConexionDB:
    def conectar(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospedaje"
        )
        return conexion

    def ejecutar_consulta(self, consulta, valores=None):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(consulta, valores)
        conn.commit()

    def obtener_datos(self, consulta, valores=None):
        conn = self.conectar()
        cursor = conn.cursor()
        if valores:
            cursor.execute(consulta, valores)
        else:
            cursor.execute(consulta)
        return cursor.fetchall()

    def cerrar_conexion(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.close()
        conn.close()

    def insertar_huesped(self, ci, nom, ape, dir, ciu, email, tel):
        try:
            consulta = 'SELECT ced_hue FROM huesped WHERE nom_hue=%s AND ape_hue=%s'
            conf = self.obtener_datos(consulta, (nom, ape))
            if not conf:
                try:
                    consulta = 'INSERT INTO huesped VALUES(%s, %s, %s, %s, %s, %s, %s)'
                    self.ejecutar_consulta(consulta, (ci, nom, ape, dir, ciu, email, tel))
                    result = True
                    self.cerrar_conexion()
                    return result
                except mysql.connector.Error as e:
                    self.cerrar_conexion()
                    return e
            else:
                e = 'El huesped ya se encuentra registrado'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e