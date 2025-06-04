import flet as ft
from huespedes import huespedes_module
from habitaciones import habitaciones_module
from ingresos import ingresos_module

def main(page: ft.Page):
    page.title = "Hotel TRIVAGO - Administrador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def open_huespedes(e):
        page.clean()
        huespedes_module(page)

    def open_habitaciones(e):
        page.clean()
        habitaciones_module(page)

    def open_ingresos(e):
        page.clean()
        ingresos_module(page)

    # Botones para abrir los módulos
    huespedes_button = ft.ElevatedButton("Módulo de Huéspedes", on_click=open_huespedes)
    habitaciones_button = ft.ElevatedButton("Módulo de Habitaciones", on_click=open_habitaciones)
    ingresos_button = ft.ElevatedButton("Módulo de Ingresos", on_click=open_ingresos)

    # Agregar los botones a la página
    page.add(
        ft.Column(
            [
                ft.Text("Panel de Administrador", size=20),
                huespedes_button,
                habitaciones_button,
                ingresos_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Iniciar la aplicación Flet
ft.app(target=main)