from models.huespedes_model import ConexionDB

class HuespedController:
    def __init__(self):
        self.model = ConexionDB()

    def insertar_huesped(self, ci, nom, ape, dir, ciu, email, tel):
        result = self.model.insertar_huesped(ci, nom, ape, dir, ciu, email, tel)
        return result