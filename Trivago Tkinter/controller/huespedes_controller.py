from models.huespedes_model import HuespedesModel

class HuespedesController:
    def __init__(self):
        self.model = HuespedesModel()

    def listar_huespedes(self):
        result = self.model.listar_huespedes()
        return result

    def agregar_huesped(self, ced, ape, nom, dir, ciu, email, tel):
        result = self.model.agregar_huesped(ced, ape, nom, dir, ciu, email, tel)
        return result

    def listar_nom(self):
        result = self.model.listar_nom()
        return result

    def listar_ced(self):
        result = self.model.listar_ced()
        return result
    
    def actualizar_huesped(self, ced, ape, nom, dir, ciu, email, tel):
        result = self.model.actualizar_huesped(ced, ape, nom, dir, ciu, email, tel)
        return result

    def eliminar_huesped(self, ced):
        result = self.model.eliminar_huesped(ced)
        return result