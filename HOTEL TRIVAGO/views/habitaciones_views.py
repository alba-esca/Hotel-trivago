import flet as ft
from controller.habitaciones_controller import HabitacionesController

class HabitacionesViews:
    def __init__(self, page: ft.Page):
        self.controller = HabitacionesController()
        self.page = page

        self.page.title = "Módulo de Habitaciones"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.codigo_field = ft.TextField(label="Código", width=300)
        self.numero_field = ft.TextField(label="Número", width=300)
        self.tipo_field = ft.TextField(label="Tipo", width=300)
        self.capacidad_field = ft.TextField(label="Capacidad", width=300)
        self.precio_field = ft.TextField(label="Precio", width=300)
        self.status_field = ft.TextField(label="Estado", width=300)

        self.agregar_button = ft.ElevatedButton("Agregar Habitación", on_click=self.insertar_habitaciones)
        self.editar_button = ft.ElevatedButton("Editar Habitación")
        self.eliminar_button = ft.ElevatedButton("Eliminar Habitación")
        self.listar_button = ft.ElevatedButton("Listar Habitaciones")

        self.page.add(
        ft.Column(
            [
                ft.Text("Módulo de Habitaciones", size=20),
                self.codigo_field,
                self.numero_field,
                self.tipo_field,
                self.capacidad_field,
                self.precio_field,
                self.status_field,
                self.agregar_button,
                self.editar_button,
                self.eliminar_button,
                self.listar_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def insertar_habitaciones(self, e):
        cod = self.codigo_field.value
        num = self.numero_field.value
        tip = self.tipo_field.value
        cap = self.capacidad_field.value
        pre = self.precio_field.value
        stat = self.status_field.value
        if cod != '' and num != '' and tip != '' and cap != '' and pre != '' and stat != '':
            result = self.controller.insertar_habitacion(cod, num, tip, cap, pre, stat)
            if result == True:
                print(f'Habitación número {num} registrada con exito')
                self.codigo_field.value = ""
                self.numero_field.value = ""
                self.tipo_field.value = ""
                self.capacidad_field.value = ""
                self.precio_field.value = ""
                self.status_field.value = ""
                self.page.update()
            else:
                print(result)
        else:
            print('Debe rellenar todos los campos')