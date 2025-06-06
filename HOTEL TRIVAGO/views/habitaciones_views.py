import flet as ft
from controller.habitaciones_controller import HabitacionesController

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
        from views.huespedes_views import HuespedesViews
        HuespedesViews(page)

    def open_habitaciones(e):
        page.clean()
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

#===================================================================================================
#aqui empieza los elementos de habitaciones
class HabitacionesViews:
    def __init__(self, page: ft.Page):
        self.controller = HabitacionesController()
        self.page = page

        self.page.title = "Módulo de Habitaciones"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # Campos de texto con validación de números
        self.codigo_field = ft.TextField(
            label="Código",
            width=300,
            on_change=self.validate_numbers
        )
        self.numero_field = ft.TextField(
            label="Número",
            width=300,
            on_change=self.validate_numbers
        )
        
        # Campos con listas desplegables
        self.tipo_field = ft.Dropdown(
            label="Tipo",
            width=300,
            options=[
                ft.dropdown.Option(text="normal"),
                ft.dropdown.Option(text="ejecutiva"),
                ft.dropdown.Option(text="suite")
            ]
        )
        self.capacidad_field = ft.Dropdown(
            label="Capacidad",
            width=300,
            options=[
                ft.dropdown.Option(text="individual"),
                ft.dropdown.Option(text="matrimonial"),
                ft.dropdown.Option(text="doble"),
                ft.dropdown.Option(text="triple")
            ]
        )
        # Campo de precio con signo $USD y validación de números
        self.precio_field = ft.TextField(
            label="Precio",
            width=300,
            prefix_text="$USD ",
            on_change=self.validate_numbers
        )
        self.status_field = ft.Dropdown(
            label="Estado",
            width=300,
            options=[
                ft.dropdown.Option(text="disponible"),
                ft.dropdown.Option(text="ocupada")
            ]
        )

        # Botones
        self.agregar_button = ft.ElevatedButton("Agregar Habitación", on_click=self.insertar_habitaciones)
        self.editar_button = ft.ElevatedButton("Editar Habitación")
        self.eliminar_button = ft.ElevatedButton("Eliminar Habitación")
        self.listar_button = ft.ElevatedButton("Listar Habitaciones")

        # Botón para volver al menú principal
        def volver_al_menu(e):
            page.clean()
            main(page)

        self.volver_button = ft.ElevatedButton("Volver al Menú", on_click=volver_al_menu, color="blue", bgcolor="white")

        # Agregar elementos a la página
        self.page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Image(src="HOTEL TRIVAGO/login/logo/Trivago_logo.png", width=200, height=45),  # Imagen en la esquina superior izquierda
                            ft.Text("Módulo de Habitaciones", size=20,)  # Texto "Módulo de Habitaciones"
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear desde el inicio
                        vertical_alignment=ft.CrossAxisAlignment.START
                    ),
                    self.codigo_field,
                    self.numero_field,
                    self.tipo_field,
                    self.capacidad_field,
                    self.precio_field,
                    self.status_field,
                    ft.Row(
                        [
                            self.agregar_button,
                            self.editar_button,
                            self.eliminar_button,
                            self.listar_button,
                            self.volver_button
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def validate_numbers(self, e):
        # Validar que solo se ingresen números
        if not e.control.value.isdigit():
            e.control.value = e.control.value[:-1]  # Eliminar el último carácter no numérico
            self.page.update()

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
                self.tipo_field.value = None  # Limpiar el valor del dropdown
                self.capacidad_field.value = None  # Limpiar el valor del dropdown
                self.precio_field.value = ""
                self.status_field.value = None  # Limpiar el valor del dropdown
                self.page.update()
            else:
                print(result)
        else:
            print('Debe rellenar todos los campos')