#Este modelo se usa para interactuar con la tabla habitacion en la bd

#Ejemplo de como se usa porque se me olvida jajajajaja


# uso del modelo de habitaciones
#habitacion_model = HabitacionesModel()

# agregar una habitación
#habitacion_model.agregar_habitacion('H001', '101', 'Normal', 'Individual', '100', 'Disponible')

# listar todas las habitaciones
#habitaciones = habitacion_model.listar_habitaciones()
#print(habitaciones)

# actualizar una habitación
#habitacion_model.actualizar_habitacion('H001', '101', 'Suite', 'Doble', '200', 'Ocupado')

# eliminar una habitación
#habitacion_model.eliminar_habitacion('H001')


import mysql.connector

class HabitacionesModel:
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

    def listar_habitaciones(self):
        try:
            query = 'SELECT * FROM habitacion'
            result = self.obtener_valores(query)
            self.cerrar_conexion()
            return result
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def listar_codigo(self):
        try:
            query = 'SELECT cod_hab FROM habitacion'
            result = self.obtener_valores(query)
            self.cerrar_conexion()
            return result
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def agregar_habitacion(self, cod, num, tipo, capacidad, precio, estado):
        try:
            query = 'SELECT * FROM habitacion WHERE cod_hab=%s'
            conf = self.obtener_valores(query, (cod,))
            if not conf:
                try:
                    query = 'INSERT INTO habitacion VALUES(%s, %s, %s, %s, %s, %s)'
                    self.ejecutar_consulta(query, (cod, num, tipo, capacidad, precio, estado))
                    result = True
                    self.cerrar_conexion()
                    return result
                except mysql.connector.Error as e:
                    self.cerrar_conexion()
                    return e
            else:
                e = 'Habitación ya registrada en la base de datos'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def actualizar_habitacion(self, cod, num, tipo, capacidad, precio, estado):
        try:
            query = 'SELECT cod_hab FROM habitacion WHERE cod_hab=%s'
            conf = self.obtener_valores(query, (cod,))
            if conf:
                campos_actualizar = []
                valores_actualizar = []
                #Confirmaciones para ver si los campos estan vacios
                if num:
                    campos_actualizar.append('num_hab=%s')
                    valores_actualizar.append(num)
                if tipo:
                    #Conversion de tipo
                    if tipo == 'Normal':
                        tipo = 'N'
                    elif tipo == 'Ejecutiva':
                        tipo = 'E'
                    elif tipo == 'Suite':
                        tipo = 'S'
                    campos_actualizar.append('tip_hab=%s')
                    valores_actualizar.append(tipo)
                if capacidad:
                    #Conversion de capacidad
                    if capacidad == 'Individual':
                        capacidad = 'I'
                    elif capacidad == 'Matrimonial':
                        capacidad = 'M'
                    elif capacidad == 'Doble':
                        capacidad = 'D'
                    elif capacidad == 'Triple':
                        capacidad = 'T'
                    campos_actualizar.append('cap_hab=%s')
                    valores_actualizar.append(capacidad)
                if precio:
                    campos_actualizar.append('pre_hab=%s')
                    valores_actualizar.append(precio)
                if estado:
                    #Conversion de estado
                    if estado == 'Disponible':
                        estado = 'D'
                    elif estado == 'Ocupado':
                        estado = 'O'
                    campos_actualizar.append('sta_hab=%s')
                    valores_actualizar.append(estado)
                if campos_actualizar:
                    query = f'UPDATE habitacion SET {", ".join(campos_actualizar)} WHERE cod_hab=%s'
                    valores_actualizar.append(cod)
                try:
                    self.ejecutar_consulta(query, valores_actualizar)
                    result = True
                    self.cerrar_conexion()
                    return result
                except mysql.connector.Error as e:
                    self.cerrar_conexion()
                    return e
            else:
                e = 'La habitación no se encuentra registrada'
                self.cerrar_conexion()
                return e
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e

    def eliminar_habitacion(self, cod):
        try:
            query = 'SELECT * FROM habitacion WHERE cod_hab=%s'
            conf = self.obtener_valores(query, (cod,))
            if conf:
                query = 'SELECT sta_hab FROM habitacion WHERE cod_hab=%s'
                status = self.obtener_valores(query, (cod,))
                if status[0][0] == 'D':
                    query = 'DELETE FROM habitacion WHERE cod_hab=%s'
                    self.ejecutar_consulta(query, (cod,))
                    result = True
                    self.cerrar_conexion()
                    return result
                else:
                    self.cerrar_conexion()
                    return 'La habitación se encuentra ocupada, asegurese que la estadía de los huéspedes se haya vencido antes de eliminar la habitación'
            else:
                self.cerrar_conexion()
                return 'La habitacion no se encuentra registrada'
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e