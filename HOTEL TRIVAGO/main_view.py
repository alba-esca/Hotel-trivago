import flet as ft
from views.huespedes_views import huespedes_module
from views.habitaciones_views import HabitacionesViews
from views.ingresos_views import ingresos_module

def main(page: ft.Page):

    page.title = "Hotel TRIVAGO - Administrador"
    page.vertical_alignment = ft.MainAxisAlignment.START  # Alinear desde el inicio
    page.theme_mode = ft.ThemeMode.LIGHT  # Fondo blanco
    page.appbar = ft.AppBar(
        title=ft.Text("Panel Administrador"),
        bgcolor=ft.Colors.BLUE
    )

    # Cargar fuente personalizada
    page.fonts = {
        "Roboto": "path/to/Roboto-Regular.ttf"
    }

    def open_huespedes(e):
        page.clean()
        huespedes_module(page)

    def open_habitaciones(e):
        page.clean()
        HabitacionesViews(page)

    def open_ingresos(e):
        page.clean()
        ingresos_module(page)

    # Estilo base para los botones
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),  # Bordes redondeados grandes
        padding=40,  # Tamaño más grande del botón
        elevation=5,  # Profundidad
        text_style=ft.TextStyle(size=20)  # Tamaño de la fuente de los botones
    )

    # Botones para abrir los módulos con fondo blanco y borde de colores específicos
    huespedes_button = ft.ElevatedButton(
        "Huéspedes", 
        on_click=open_huespedes, 
        style=button_style,
        bgcolor=ft.Colors.WHITE,  # Fondo blanco
    )
    habitaciones_button = ft.ElevatedButton(
        "Habitaciones", 
        on_click=open_habitaciones, 
        style=button_style,
        bgcolor=ft.Colors.WHITE,  # Fondo blanco
    )
    ingresos_button = ft.ElevatedButton(
        "Ingresos", 
        on_click=open_ingresos, 
        style=button_style,
        bgcolor=ft.Colors.WHITE,  # Fondo blanco
    )

    # Agregar los botones y la imagen a la página
    page.add(
        ft.Column(
            [
                ft.Image(src="HOTEL TRIVAGO/image/modelo trivago (1).png", width=650, height=300),  # Ajustar el tamaño de la imagen
                ft.Row(
                    [
                        huespedes_button,
                        habitaciones_button,
                        ingresos_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,#alignment=ft.MainAxisAlignment.CENTER en el ft.Column a alignment=ft.MainAxisAlignment.START. Esto asegura que los elementos se alineen desde el inicio del contenedor :)
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=50  # Añadir espacio entre los botones
                )
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinear desde el inicio 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Iniciar la aplicación Flet
ft.app(target=main)