from models.ingresos_model import ConexionDB

class IngresosController:
    def __init__(self):
        self.model = ConexionDB()

    def listar_ci(self):
        result = self.model.listar_ci()
        return result

    def listar_hab(self):
        result = self.model.listar_hab()
        return result
    
    def insertar_ingreso(self, hue, hab, fec_ing, fec_sal, can):
        result = self.model.insertar_ingreso(hue, hab, fec_ing, fec_sal, can)
        return result