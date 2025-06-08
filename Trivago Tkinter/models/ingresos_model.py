import mysql.connector

#no se si esta bien 
class IngresosModel:
    def conectar(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', db='hospedaje')
        return conn

    def ejecutar_consulta(self, query, values=None):
        conn = self.conectar()
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def obtener_valores(self, query, values=None):
        conn = self.conectar()
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def cerrar_conexion(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.close()
        conn.close()

    def listar_ingresos(self):
        try:
            query = 'SELECT * FROM ingreso'
            result = self.obtener_valores(query)
            return result
        except mysql.connector.Error as e:
            return e

    def listar_codigos_ingreso(self):
        try:
            query = 'SELECT cod_ing FROM ingreso'
            result = self.obtener_valores(query)
            return result
        except mysql.connector.Error as e:
            return e

    def listar_ced(self):
        try:
            query = 'SELECT ced_hue FROM huesped'
            result = self.obtener_valores(query)
            return result
        except mysql.connector.Error as e:
            return e

    def listar_cod_hab(self):
        try:
            query = 'SELECT cod_hab FROM habitacion'
            result = self.obtener_valores(query)
            return result
        except mysql.connector.Error as e:
            return e

    def agregar_ingreso(self, cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes):
        try:
            query = 'SELECT * FROM ingreso WHERE ced_hue=%s AND cod_hab=%s AND fec_ing=%s'
            conf = self.obtener_valores(query, (cedula_huesped, cod_habitacion, fecha_ingreso))
            if not conf:
                try:
                    query = 'SELECT sta_hab FROM habitacion WHERE cod_hab=%s'
                    status = self.obtener_valores(query, (cod_habitacion,))
                    if not status:
                        self.cerrar_conexion()
                        return 'Habitacion no encontrada'
                    query = 'SELECT cap_hab FROM habitacion WHERE cod_hab=%s'
                    cap_raw = self.obtener_valores(query, (cod_habitacion,))
                    if not cap_raw:
                        self.cerrar_conexion()
                        return 'Capacidad de la habitación no encontrada'
                    if cap_raw[0][0] == 'I':
                        cap = 1
                    elif cap_raw[0][0] == 'M':
                        cap = 2
                    elif cap_raw[0][0] == 'D':
                        cap = 4
                    elif cap_raw[0][0] == 'T':
                        cap = 6
                    else:
                        e = 'Capacidad de la habitación inválida'
                        self.cerrar_conexion()
                        return e
                    print(f'{status[0][0]}\nTipo: {type(status[0][0])}')
                    if status[0][0] == 'D':
                        if int(ocupantes) <= cap:
                            query = 'INSERT INTO ingreso VALUES (NULL, %s, %s, %s, %s, %s)'
                            self.ejecutar_consulta(query, (cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes))
                            query = 'UPDATE habitacion SET sta_hab=%s WHERE cod_hab=%s'
                            self.ejecutar_consulta(query, ('O', cod_habitacion))
                            self.cerrar_conexion()
                            return True
                        else:
                            e = f'Capacidad de la habitación excedida\nCapacidad de la habitación: {cap}\nCantidad de ocupantes a registrar: {ocupantes}'
                            self.cerrar_conexion()
                            return e
                    elif status[0][0] == 'O':
                        e = 'La habitación se encuentra ocupada'
                        self.cerrar_conexion()
                        return e
                except mysql.connector.Error as e:
                    print("Error MySQL:", e)
                    return e
            else:
                return 'Ingreso ya registrado en la base de datos'
        except mysql.connector.Error as e:
            print("Error MySQL:", e)  # Para depuración
            return e

    def editar_ingreso(self, cod_ingreso, cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes):
        try:
            query = 'SELECT ced_hue FROM ingreso WHERE cod_ing=%s'
            conf = self.obtener_valores(query, (cod_ingreso,))
            if conf:
                campos_actualizar = []
                valores_actualizar = []
                if cedula_huesped:
                    campos_actualizar.append('ced_hue=%s')
                    valores_actualizar.append(cedula_huesped)
                if cod_habitacion:
                    query = 'SELECT sta_hab FROM habitacion WHERE cod_hab=%s'
                    hab = self.obtener_valores(query, (cod_habitacion,))
                    if hab[0][0] == 'D':
                        campos_actualizar.append('cod_hab=%s')
                        valores_actualizar.append(cod_habitacion)
                    else:
                        self.cerrar_conexion()
                        return f'La habitación con el código {cod_habitacion} ya se encuentra ocupada'
                if fecha_ingreso:
                    campos_actualizar.append('fec_ing=%s')
                    valores_actualizar.append(fecha_ingreso)
                if fecha_salida:
                    campos_actualizar.append('fec_sal=%s')
                    valores_actualizar.append(fecha_salida)
                if ocupantes:
                    query = 'SELECT cap_hab FROM habitacion WHERE cod_hab=%s'
                    cap_raw = self.obtener_valores(query, (cod_habitacion,))
                    if cap_raw[0][0] == 'I':
                        cap = 1
                    elif cap_raw[0][0] == 'M':
                        cap = 2
                    elif cap_raw[0][0] == 'D':
                        cap = 4
                    elif cap_raw[0][0] == 'T':
                        cap = 6
                    else:
                        self.cerrar_conexion()
                        return 'capacidad de habitacion no valida'
                    if int(ocupantes) <= cap:
                        campos_actualizar.append('can_per=%s')
                        valores_actualizar.append(ocupantes)
                    else:
                        self.cerrar_conexion()
                        return f'La cantidad de huéspedes a actualizar es mayor a la capacidad de la habitación\nCapacidad de la habitación: {cap}\nCantidad de huéspedes ingresado: {ocupantes}'
                else:
                    if cod_habitacion:
                        query = 'SELECT can_per FROM ingreso WHERE cod_ing=%s'
                        ocupantes_actual = self.obtener_valores(query, (cod_ingreso,))
                        query = 'SELECT cap_hab FROM habitacion WHERE cod_hab=%s'
                        cap_raw = self.obtener_valores(query, (cod_habitacion,))
                        if cap_raw[0][0] == 'I':
                            cap = 1
                        elif cap_raw[0][0] == 'M':
                            cap = 2
                        elif cap_raw[0][0] == 'D':
                            cap = 4
                        elif cap_raw[0][0] == 'T':
                            cap = 6
                        else:
                            self.cerrar_conexion()
                            return 'capacidad de habitacion no valida'
                        if int(ocupantes_actual[0][0]) >= cap:
                            self.cerrar_conexion()
                            return f'La cantidad de ocupantes excede la capacidad de la habitación\nCapacidad de la habitación: {cap}\nOcupantes actuales: {ocupantes_actual[0][0]}'
                if campos_actualizar:
                    query = f'UPDATE ingreso SET {", ".join(campos_actualizar)} WHERE cod_ing=%s'
                    valores_actualizar.append(cod_ingreso)
                    self.ejecutar_consulta(query, valores_actualizar)
                if cod_habitacion:
                    query = 'UPDATE habitacion SET sta_hab="O" WHERE cod_hab=%s'
                    self.ejecutar_consulta(query, (cod_habitacion,))
                    return True
                else:
                    return 'No se han proporcionado campos para actualizar'
            else:
                return 'El ingreso no se encuentra registrado'
        except mysql.connector.Error as e:
            return e

    def eliminar_ingreso(self, cod_ingreso):
        try:
            query = 'DELETE FROM ingreso WHERE cod_ing=%s'
            self.ejecutar_consulta(query, (cod_ingreso,))
            return True
        except mysql.connector.Error as e:
            return e