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
                #Conversion de tipo
                if tipo == 'Normal':
                    tipo = 'N'
                elif tipo == 'Ejecutiva':
                    tipo = 'E'
                elif tipo == 'Suite':
                    tipo = 'S'
                #Conversion de capacidad
                if capacidad == 'Individual':
                    capacidad = 'I'
                elif capacidad == 'Matrimonial':
                    capacidad = 'M'
                elif capacidad == 'Doble':
                    capacidad = 'D'
                elif capacidad == 'Triple':
                    capacidad = 'T'
                #Conversion de estado
                if estado == 'Disponible':
                    estado = 'D'
                elif estado == 'Ocupado':
                    estado = 'O'
                query = 'SELECT tip_hab WHERE cod_hab=%s'
                tipo_old = self.obtener_valores(query, (tipo,))
                query = 'SELECT cap_hab FROM habitacion WHERE cod_hab=%s'
                capacidad_old = self.obtener_valores(query, (capacidad,))
                query = 'SELECT sta_hab FROM habitacion WHERE cod_hab=%s'
                estado_old = self.obtener_valores(query, (estado,))
                if num:
                    campos_actualizar.append('num_hab=%s')
                    valores_actualizar.append(num)
                if tipo != tipo_old:
                    campos_actualizar.append('tipo_hab=%s')
                    valores_actualizar.append(tipo)
                if capacidad != capacidad_old:
                    campos_actualizar.append('capacidad_hab=%s')
                    valores_actualizar.append(capacidad)
                if precio:
                    campos_actualizar.append('precio_hab=%s')
                    valores_actualizar.append(precio)
                if estado != estado_old:
                    campos_actualizar.append('estado_hab=%s')
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
            query = 'DELETE FROM habitacion WHERE cod_hab=%s'
            self.ejecutar_consulta(query, (cod,))
            result = True
            self.cerrar_conexion()
            return result
        except mysql.connector.Error as e:
            self.cerrar_conexion()
            return e