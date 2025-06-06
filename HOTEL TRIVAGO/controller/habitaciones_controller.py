from models.habitaciones_model import ConexionDB

class HabitacionesController:
    def __init__(self):
        self.model = ConexionDB()

    def insertar_habitacion(self, cod, num, tip, cap, pre, stat):
        result = self.model.insertar_habitacion(cod, num, tip, cap, pre, stat)
        return result