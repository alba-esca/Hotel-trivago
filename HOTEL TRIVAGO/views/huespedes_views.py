import flet as ft
from controller.huespedes_controller import HuespedController

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
        from views.ingresos_views import IngresosViews
        IngresosViews(page)

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

#Clase principal de la vista
class HuespedesViews:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = HuespedController()
        self.page.title = "Módulo de Huéspedes"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT

        def eliminar_huesped(e):
            pass

        def listar_huespedes(e):
            pass

        def volver_al_menu(e):
            self.page.clean()  # Limpia la página actual
            main(self.page)  # Carga el menú principal

        self.cedula_field = ft.TextField(label="Cédula", width=300, max_length=8, on_change=self.validate_numbers)
        self.nombres_field = ft.TextField(label="Nombres", width=300, max_length=15)
        self.apellidos_field = ft.TextField(label="Apellidos", width=300, max_length=15)
        self.direccion_field = ft.TextField(label="Dirección", width=300, max_length=80)
        self.ciudad_field = ft.TextField(label="Ciudad", width=300, max_length=15)
        self.email_field = ft.TextField(label="Email", width=300, max_length=30)
        self.telefono_field = ft.TextField(label="Teléfono", width=300, max_length=12)

        self.agregar_button = ft.ElevatedButton("Agregar Huésped", on_click=self.insertar_huesped)
        self.editar_button = ft.ElevatedButton("Editar Huésped", on_click=self.editar_huesped)
        self.eliminar_button = ft.ElevatedButton("Eliminar Huésped", on_click=eliminar_huesped)
        self.listar_button = ft.ElevatedButton("Listar Huéspedes", on_click=listar_huespedes)
        self.volver_button = ft.ElevatedButton("Volver al Menú", on_click=volver_al_menu)

        page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Image(src="HOTEL TRIVAGO/login/logo/Trivago_logo.png", width=200, height=45),  # Imagen en la esquina superior izquierda
                            ft.Text("Módulo de Huéspedes", size=20,)  # Texto "Módulo de Habitaciones"
                        ],
                        alignment=ft.MainAxisAlignment.START,  # Alinear desde el inicio
                        vertical_alignment=ft.CrossAxisAlignment.START
                    ),
                    self.cedula_field,
                    self.nombres_field,
                    self.apellidos_field,
                    self.direccion_field,
                    self.ciudad_field,
                    self.email_field,
                    self.telefono_field,
                    ft.Row(
                        [
                            self.agregar_button,
                            self.editar_button,
                            self.eliminar_button,
                            self.listar_button,
                            self.volver_button  # Agregado el botón de volver al menú
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def insertar_huesped(self, e):
        ci = self.cedula_field.value
        nom = self.nombres_field.value
        ape = self.apellidos_field.value
        dir = self.direccion_field.value
        ciu = self.ciudad_field.value
        email = self.email_field.value
        tel = self.telefono_field.value
        if ci != '' and nom != '' and ape != '' and dir != '' and ciu != '' and email != '' and tel != '':
            result = self.controller.insertar_huesped(ci, nom, ape, dir, ciu, email, tel)
            if result == True:
                print(f'El huesped {nom} ha sido agregado correctamente')
                self.cedula_field = ''
                self.nombres_field = ''
                self.apellidos_field = ''
                self.direccion_field = ''
                self.ciudad_field = ''
                self.email_field = ''
                self.telefono_field = ''
            else:
                print(result)
        else:
            print('Debe rellenar todos los campos')

    def editar_huesped(self, e):
            edit_cedula_field = ft.TextField(label="Cédula", width=300, max_length=8, on_change=self.validate_numbers)
            edit_nombres_field = ft.TextField(label="Nombres", width=300, max_length=15)
            edit_apellidos_field = ft.TextField(label="Apellidos", width=300, max_length=15)
            edit_direccion_field = ft.TextField(label="Dirección", width=300, max_length=80)
            edit_ciudad_field = ft.TextField(label="Ciudad", width=300, max_length=15)
            edit_email_field = ft.TextField(label="Email", width=300, max_length=30)
            edit_telefono_field = ft.TextField(label="Teléfono", width=300, max_length=12)

            campos = [
                (self.cedula_field, edit_cedula_field),
                (self.nombres_field, edit_nombres_field),
                (self.apellidos_field, edit_apellidos_field),
                (self.direccion_field, edit_direccion_field), 
                (self.ciudad_field, edit_ciudad_field),
                (self.email_field, edit_email_field),
                (self.telefono_field, edit_telefono_field)
                ]

            for original, edit in campos:
                if original.value != '':
                    edit.value = original.value

            self.page.views.append(
                ft.View(
                    route='/full',
                    fullscreen_dialog=True,
                    appbar=ft.AppBar(title=ft.Text('Editar Huésped')),
                    controls=[
                        edit_cedula_field,
                        edit_nombres_field,
                        edit_apellidos_field,
                        edit_direccion_field,
                        edit_ciudad_field,
                        edit_email_field,
                        edit_telefono_field
                    ],
                )
            )
            self.page.go('/full')

    def validate_numbers(self, e):
        # Validar que solo se ingresen números
        if not e.control.value.isdigit() and e.control.value != '-':
            e.control.value = e.control.value[:-1]  # Eliminar el último carácter no numérico
            self.page.update()

if __name__ == "__main__":
    ft.app(target=main)