import flet as ft

# =================Aqui esta el MAIN que devuelve al menu====================
def main(page: ft.Page):
    page.title = "Hotel TRIVAGO - Administrador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centrar verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centrar horizontalmente
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
        HuespedesViews(page)

    def open_habitaciones(e):
        page.clean()
        from views.habitaciones_views import HabitacionesViews
        HabitacionesViews(page)

    def open_ingresos(e):
        page.clean()
        ingresos_module(page)

    # Estilo base para los botones
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),  # Bordes redondeados grandes
        padding=20,  # Tamaño del botón
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
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinear desde el centro
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20  # Añadir espacio entre los botones
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

class HuespedesViews:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Módulo de Huéspedes"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT

        def agregar_huesped(e):
            pass

        def editar_huesped(e):
            pass

        def eliminar_huesped(e):
            pass

        def listar_huespedes(e):
            pass

        def volver_al_menu(e):
            self.page.clean()  # Limpia la página actual
            main(self.page)  # Carga el menú principal

        self.cedula_field = ft.TextField(label="Cédula", width=300)
        self.nombres_field = ft.TextField(label="Nombres", width=300)
        self.apellidos_field = ft.TextField(label="Apellidos", width=300)
        self.direccion_field = ft.TextField(label="Dirección", width=300)
        self.ciudad_field = ft.TextField(label="Ciudad", width=300)
        self.email_field = ft.TextField(label="Email", width=300)
        self.telefono_field = ft.TextField(label="Teléfono", width=300)

        self.agregar_button = ft.ElevatedButton("Agregar Huésped", on_click=agregar_huesped)
        self.editar_button = ft.ElevatedButton("Editar Huésped", on_click=editar_huesped)
        self.eliminar_button = ft.ElevatedButton("Eliminar Huésped", on_click=eliminar_huesped)
        self.listar_button = ft.ElevatedButton("Listar Huéspedes", on_click=listar_huespedes)
        self.volver_button = ft.ElevatedButton("Volver al Menú", on_click=volver_al_menu)

        page.add(
            ft.Column(
                [
                    ft.Text("Módulo de Huéspedes", size=20),
                    self.cedula_field,
                    self.nombres_field,
                    self.apellidos_field,
                    self.direccion_field,
                    self.ciudad_field,
                    self.email_field,
                    self.telefono_field,
                    self.agregar_button,
                    self.editar_button,
                    self.eliminar_button,
                    self.listar_button,
                    self.volver_button  # Agregado el botón de volver al menú
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

if __name__ == "__main__":
    ft.app(target=main)