import flet as ft
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

    # Botones para abrir los módulos
    huespedes_button = ft.ElevatedButton("Huéspedes", on_click=open_huespedes, color="blue", bgcolor="white")
    habitaciones_button = ft.ElevatedButton("Habitaciones", on_click=open_habitaciones, color="blue", bgcolor="white")
    ingresos_button = ft.ElevatedButton("Ingresos", on_click=open_ingresos, color="red", bgcolor="white")



#===================Aqui empiza el modulo de ingresos======================================

def ingresos_module(page: ft.Page):
    page.title = "Módulo de Ingresos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def registrar_ingreso(e):
        pass

    def eliminar_ingreso(e):
        pass

    def listar_ingresos(e):
        pass

    def volver_al_menu(e):
        page.clean()  # Limpia la página actual
        main(page)  # Carga el menú principal

    def only_numbers(e):
        if not e.control.value.isdigit():
            e.control.value = e.control.value[:-1]
            page.update()

    def format_date(e):
        # Remove any non-digit characters
        cleaned_value = ''.join(filter(str.isdigit, e.control.value))
        # Format the date as dd/mm/aaaa while typing
        if len(cleaned_value) > 2:
            cleaned_value = f"{cleaned_value[:2]}/{cleaned_value[2:]}"
        if len(cleaned_value) > 5:
            cleaned_value = f"{cleaned_value[:5]}/{cleaned_value[5:]}"
        e.control.value = cleaned_value
        page.update()

    # Campos de entrada
    codigo_ingreso_field = ft.TextField(
        label="Código de Ingreso",
        width=300,
        text_align="center",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=only_numbers
    )
    cedula_huesped_field = ft.TextField(
        label="Cédula del Huésped",
        width=300,
        text_align="center",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=only_numbers
    )
    codigo_habitacion_field = ft.TextField(
        label="Código de Habitación",
        width=300,
        text_align="center",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=only_numbers
    )
    fecha_ingreso_field = ft.TextField(
        label="Fecha de Ingreso",
        width=300,
        text_align="center",
        hint_text="dd/mm/aaaa",
        on_change=format_date
    )
    fecha_salida_field = ft.TextField(
        label="Fecha de Salida",
        width=300,
        text_align="center",
        hint_text="dd/mm/aaaa",
        on_change=format_date
    )
    cantidad_personas_field = ft.TextField(
        label="Cantidad de Personas",
        width=300,
        text_align="center",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=only_numbers
    )

    # Agregar una imagen en la parte superior izquierda
    image = ft.Image(src="HOTEL TRIVAGO/login/logo/Trivago_logo.png", width=150, height=150)  # Reducir el tamaño de la imagen

    # Botones
    registrar_button = ft.ElevatedButton("Registrar Ingreso", on_click=registrar_ingreso, color="blue", bgcolor="white")
    listar_button = ft.ElevatedButton("Listar Ingresos", on_click=listar_ingresos, color="blue", bgcolor="white")
    eliminar_button = ft.ElevatedButton("Eliminar Ingreso", on_click=eliminar_ingreso, color="red", bgcolor="white")
    volver_button = ft.ElevatedButton("Volver al Menú", on_click=volver_al_menu, color="blue", bgcolor="white")

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        image,  # Agregar la imagen
                        ft.Text("Módulo de Ingresos", size=20, text_align="center")
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                codigo_ingreso_field,  # Nuevo campo agregado
                cedula_huesped_field,
                codigo_habitacion_field,
                fecha_ingreso_field,
                fecha_salida_field,
                cantidad_personas_field,
                ft.Row(
                    [
                        registrar_button,
                        listar_button,
                        eliminar_button,
                        volver_button
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

# Iniciar la aplicación Flet
ft.app(target=main)