import mysql.connector

class HuespedesModel:
    def conectar(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', db='hospedaje')
        return conn

    def ejecutar_consulta(self, query, values=None):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

    def obtener_valores(self, query, values=None):
        conn = self.conectar()
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def cerrar_conexion(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.close()
        conn.close()

    def listar_huespedes(self):
        try:
            query = 'SELECT * FROM huesped'
            result = self.obtener_valores(query)
            self.cerrar_conexion()
            return result
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def listar_nom(self):
        try:
            query = 'SELECT nom_hue FROM huesped'
            result = self.obtener_valores(query)
            self.cerrar_conexion()
            return result
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def listar_ced(self):
        try:
            query = 'SELECT ced_hue FROM huesped'
            result = self.obtener_valores(query)
            self.cerrar_conexion()
            return result
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def agregar_huesped(self, ced, ape, nom, dir, ciu, email, tel):
        try:
            query = 'SELECT * FROM huesped WHERE ced_hue=%s'
            conf = self.obtener_valores(query, (ced,))
            if not conf:
                try:
                    query = 'INSERT INTO huesped VALUES(%s, %s, %s, %s, %s, %s, %s)'
                    self.ejecutar_consulta(query, (ced, ape, nom, dir, ciu, email, tel))
                    result = True
                    self.cerrar_conexion()
                    return result
                except mysql.connector.Error as e:
                    self.cerrar_conexion()
                    return e
            else:
                e = 'Huesped ya registrado en la base de datos'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def actualizar_huesped(self, ced, ape, nom, dir, ciu, email, tel):
        try:
            query = 'SELECT nom_hue FROM huesped WHERE ced_hue=%s'
            conf = self.obtener_valores(query, (ced,))
            if conf:
                campos_actualizar = []
                valores_actualizar = []  
                if ape:
                    campos_actualizar.append('ape_hue=%s')
                    valores_actualizar.append(ape)
                if nom:
                    campos_actualizar.append('nom_hue=%s')
                    valores_actualizar.append(nom)
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
                    query = f'UPDATE huesped SET {', '.join(campos_actualizar)} WHERE ced_hue=%s'
                    valores_actualizar.append(ced)
                try:
                    self.ejecutar_consulta(query, valores_actualizar)
                    result = True
                    self.cerrar_conexion()
                    return result
                except mysql.connector.Error as e:
                    self.cerrar_conexion()
                    return(e)
            else:
                e = 'El huesped no se encuentra registrado'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return(e)

    def eliminar_huesped(self, ced):
        try:
            query = 'SELECT * FROM huesped WHERE ced_hue=%s'
            conf = self.obtener_valores(query, (ced,))
            if conf:
                query = 'SELECT cod_ing FROM ingreso WHERE ced_hue=%s'
                hue = self.obtener_valores(query, (ced,))
                if not hue:
                    query = 'DELETE FROM huesped WHERE ced_hue=%s'
                    self.ejecutar_consulta(query, (ced,))
                    result = True
                    self.cerrar_conexion()
                    return result
                else:
                    self.cerrar_conexion()
                    return 'El huésped ya se encuentra asociado a un registro, elimine el registro asociado al huésped antes de eliminarlo'
            else:
                e = 'El huesped no se encuentra registrado'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e