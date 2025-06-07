import flet as ft
from controller.ingresos_controller import IngresosController
#================Aqui esta el MAIN que devuelve al menu====================
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
        from views.huespedes_views import HuespedesViews
        HuespedesViews(page)

    def open_habitaciones(e):
        page.clean()
        from views.habitaciones_views import HabitacionesViews
        HabitacionesViews(page)

    def open_ingresos(e):
        page.clean()
        IngresosViews(page)

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

    # Botones para abrir los módulos
    huespedes_button = ft.ElevatedButton("Huéspedes", on_click=open_huespedes, color="blue", bgcolor="white")
    habitaciones_button = ft.ElevatedButton("Habitaciones", on_click=open_habitaciones, color="blue", bgcolor="white")
    ingresos_button = ft.ElevatedButton("Ingresos", on_click=open_ingresos, color="red", bgcolor="white")



#===================Aqui empiza el modulo de ingresos======================================

class IngresosViews:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = IngresosController()

        self.page.title = "Módulo de Ingresos"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT

        def eliminar_ingreso(e):
            pass

        def listar_ingresos(e):
            pass

        def volver_al_menu(e):
            self.page.clean()  # Limpia la página actual
            main(page)  # Carga el menú principal

        # Listas de opciones para las listas desplegables
        ci_list = self.listar_ci()
        self.cedulas_huespedes = []  # Ejemplo de cédulas
        for i in ci_list:
            self.cedulas_huespedes.append(i)

        hab_list = self.listar_hab()
        self.codigos_habitacion = []  # Ejemplo de códigos de habitación
        for i in hab_list:
            self.codigos_habitacion.append(i)

        # Campos de entrada
        self.cedula_huesped_field = ft.Dropdown(
            label="Cédula del Huésped",
            width=300,
            options=[ft.dropdown.Option(text=cedula) for cedula in self.cedulas_huespedes]
        )
        self.codigo_habitacion_field = ft.Dropdown(
            label="Código de Habitación",
            width=300,
            options=[ft.dropdown.Option(text=codigo) for codigo in self.codigos_habitacion]
        )
        self.fecha_ingreso_field = ft.TextField(
            label="Fecha de Ingreso",
            width=300,
            text_align="center",
            hint_text="AAAA/MM/DD"
        )
        self.fecha_salida_field = ft.TextField(
            label="Fecha de Salida",
            width=300,
            text_align="center",
            hint_text="AAAA/MM/DD"
        )
        self.cantidad_personas_field = ft.TextField(
            label="Cantidad de Personas",
            width=300,
            text_align="center",
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=self.validate_numbers,
            max_length=3
        )

        # Agregar una imagen en la parte superior izquierda
        self.image = ft.Image(src="HOTEL TRIVAGO/login/logo/Trivago_logo.png", width=150, height=150)  # Reducir el tamaño de la imagen

        # Botones
        self.registrar_button = ft.ElevatedButton("Registrar Ingreso", on_click=self.insertar_ingreso, color="blue", bgcolor="white")
        self.listar_button = ft.ElevatedButton("Listar Ingresos", on_click=listar_ingresos, color="blue", bgcolor="white")
        self.eliminar_button = ft.ElevatedButton("Eliminar Ingreso", on_click=eliminar_ingreso, color="red", bgcolor="white")
        self.volver_button = ft.ElevatedButton("Volver al Menú", on_click=volver_al_menu, color="blue", bgcolor="white")

        self.page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            self.image,  # Agregar la imagen
                            ft.Text("Módulo de Ingresos", size=20, text_align="center")
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    self.cedula_huesped_field,
                    self.codigo_habitacion_field,
                    self.fecha_ingreso_field,
                    self.fecha_salida_field,
                    self.cantidad_personas_field,
                    ft.Row(
                        [
                            self.registrar_button,
                            self.listar_button,
                            self.eliminar_button,
                            self.volver_button
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10  # Reducir el espacio entre los botones
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10  # Reducir el espacio entre los elementos
            )
        )

    def insertar_ingreso(self, e=None):
        hue = self.cedula_huesped_field.value
        hab = self.codigo_habitacion_field.value
        fec_ing = self.fecha_ingreso_field.value
        fec_sal = self.fecha_salida_field.value
        can = self.cantidad_personas_field.value
        if hue != '' and hab != '' and fec_ing != '' and fec_sal != '' and can != '':
            result = self.controller.insertar_ingreso(hue, hab, fec_ing, fec_sal, can)
            if result == True:
                print('Ingrese agregado de forma exitosa')
            else:
                print(result)
        else:
            print('Debe rellenar todos los campos')

    def listar_ci(self):
        result = self.controller.listar_ci()
        return result

    def listar_hab(self):
        result = self.controller.listar_hab()
        return result

    def validate_numbers(self, e):
        # Validar que solo se ingresen números
        if not e.control.value.isdigit():
            e.control.value = e.control.value[:-1]  # Eliminar el último carácter no numérico
            self.page.update()

# Iniciar la aplicación Flet
ft.app(target=main)