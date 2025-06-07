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

    def listar_ci(self):
        try:
            ced_listSF = self.obtener_datos('SELECT ced_hue FROM huesped')
            ced_list = []
            for i in range(len(ced_listSF)):
                value = ced_listSF[i][0]
                ced_list.append(value)
            self.cerrar_conexion()
            return ced_list
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def listar_hab(self):
        try:
            hab_listSF = self.obtener_datos('SELECT cod_hab FROM habitacion')
            hab_list = []
            for i in range(len(hab_listSF)):
                value = hab_listSF[i][0]
                hab_list.append(value)
            self.cerrar_conexion()
            return hab_list
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def insertar_ingreso(self, hue, hab, fec_ing, fec_sal, can):
        try:
            try:
                hue_ci = int(hue)
                consulta = 'INSERT INTO ingreso VALUES(NULL, %s, %s, %s, %s, %s)'
                self.ejecutar_consulta(consulta, (hue_ci, hab, fec_ing, fec_sal, can))
                consulta = 'UPDATE habitacion SET sta_hab="O" WHERE cod_hab=%s'
                self.ejecutar_consulta(consulta, (hab,))
                result = True
                self.cerrar_conexion()
                return result
            except mysql.connector.Error as e:
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e