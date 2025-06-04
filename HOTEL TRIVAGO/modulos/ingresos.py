import flet as ft

def ingresos_module(page: ft.Page):
    page.title = "Módulo de Ingresos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def registrar_ingreso(e):
        
        pass

    def eliminar_ingreso(e):
        
        pass

    def listar_ingresos(e):
        
        pass

    cedula_huesped_field = ft.TextField(label="Cédula del Huésped", width=300)
    codigo_habitacion_field = ft.TextField(label="Código de Habitación", width=300)
    fecha_ingreso_field = ft.TextField(label="Fecha de Ingreso", width=300)
    fecha_salida_field = ft.TextField(label="Fecha de Salida", width=300)
    cantidad_personas_field = ft.TextField(label="Cantidad de Personas", width=300)

    registrar_button = ft.ElevatedButton("Registrar Ingreso", on_click=registrar_ingreso)
    eliminar_button = ft.ElevatedButton("Eliminar Ingreso", on_click=eliminar_ingreso)
    listar_button = ft.ElevatedButton("Listar Ingresos", on_click=listar_ingresos)

    page.add(
        ft.Column(
            [
                ft.Text("Módulo de Ingresos", size=20),
                cedula_huesped_field,
                codigo_habitacion_field,
                fecha_ingreso_field,
                fecha_salida_field,
                cantidad_personas_field,
                registrar_button,
                eliminar_button,
                listar_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )