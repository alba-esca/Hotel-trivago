from models.huespedes_model import ConexionDB

class HuespedController:
    def __init__(self):
        self.model = ConexionDB()

    def insertar_huesped(self, ci, nom, ape, dir, ciu, email, tel):
        result = self.model.insertar_huesped(ci, nom, ape, dir, ciu, email, tel)
        return result

    def listar_ci(self):
        result = self.model.listar_ci()
        return result

    def info_huesped(self, ci):
        result = self.model.info_huesped(ci)
        return result

    def actualizar_huesped(self, ci, nom, ape, dir, ciu, email, tel):
        result = self.model.actualizar_huesped(ci, nom, ape, dir, ciu, email, tel)
        return result