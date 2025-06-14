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

    """def info_huesped(self, ci):
        try:
            consulta = 'SELECT * FROM huesped WHERE ced_hue=%s'
            result = self.obtener_datos(consulta, (ci,))
            if result:
                self.cerrar_conexion()
                return result
            else:
                e = 'El huesped no se encuetra registrado'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e"""

    def actualizar_huesped(self, ci, nom, ape, dir, ciu, email, tel):
        try:
            consulta = 'SELECT nom_hue FROM huesped WHERE ced_hue=%s'
            conf = self.obtener_datos(consulta, (ci,))
            if conf:
                campos_actualizar = []
                valores_actualizar = []

                if nom:
                    campos_actualizar.append('nom_hue=%s')
                    valores_actualizar.append(nom)
                if ape:
                    campos_actualizar.append('ape_hue=%s')
                    valores_actualizar.append(ape)
                if dir:
                    campos_actualizar.append('dir_hue=%s')
                    valores_actualizar.append(dir)
                if ciu:
                    campos_actualizar.append('ciu_hue=%s')
                    valores_actualizar.append(ciu)
                if email:
                    campos_actualizar.append('email_hue=%s')
                    valores_actualizar.append(email)
                if tel:
                    campos_actualizar.append('tel_hue=%s')
                    valores_actualizar.append(tel)

                if campos_actualizar:
                    consulta = f'UPDATE huesped SET {', '.join(campos_actualizar)} WHERE ced_hue=%s'
                    valores_actualizar.append(ci)

                try:
                    self.ejecutar_consulta(consulta, valores_actualizar)
                    result = True
                    self.cerrar_conexion()
                    return result
                except mysql.connector.Error as e:
                    self.cerrar_conexion()
                    return(e)
            else:
                e = 'El huesped no existe'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return(e)