# Ejemplo de uso del controlador de habitaciones
#habitacion_controller = HabitacionesController()

# listar todas las habitaciones
#habitaciones = habitacion_controller.listar_habitaciones()
#print(habitaciones)

# agregar una habitación
#habitacion_controller.agregar_habitacion('H001', '101', 'Normal', 'Individual', '100', 'Disponible')

# actualizar una habitación
#habitacion_controller.actualizar_habitacion('H001', '101', 'Suite', 'Doble', '200', 'Ocupado')

# eliminar una habitación
#habitacion_controller.eliminar_habitacion('H001')




from models.habitaciones_model import HabitacionesModel

class HabitacionesController:
    def __init__(self):
        self.model = HabitacionesModel()

    def listar_habitaciones(self):
        result = self.model.listar_habitaciones()
        return result

    def agregar_habitacion(self, cod, num, tipo, capacidad, precio, estado):
        result = self.model.agregar_habitacion(cod, num, tipo, capacidad, precio, estado)
        return result

    def actualizar_habitacion(self, cod, num, tipo, capacidad, precio, estado):
        result = self.model.actualizar_habitacion(cod, num, tipo, capacidad, precio, estado)
        return result

    def eliminar_habitacion(self, cod):
        result = self.model.eliminar_habitacion(cod)
        return result

    def listar_codigo(self):
        result = self.model.listar_codigo()
        return result