from models.ingresos_model import IngresosModel

class IngresosController:
    def __init__(self):
        self.model = IngresosModel()

    def listar_ingresos(self):
        result = self.model.listar_ingresos()
        return result

    def agregar_ingreso(self, cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes):
        result = self.model.agregar_ingreso(cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes)
        return result

    def editar_ingreso(self, cod_ingreso, cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes):
        result = self.model.editar_ingreso(cod_ingreso, cedula_huesped, cod_habitacion, fecha_ingreso, fecha_salida, ocupantes)
        return result

    def eliminar_ingreso(self, cod_ingreso):
        result = self.model.eliminar_ingreso(cod_ingreso)
        return result

    def listar_codigos_ingreso(self):
        result = self.model.listar_codigos_ingreso()
        return result

    def listar_ced(self):
        result = self.model.listar_ced()
        return result

    def listar_cod_hab(self):
        result = self.model.listar_cod_hab()
        return result