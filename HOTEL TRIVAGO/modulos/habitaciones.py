import flet as ft

def habitaciones_module(page: ft.Page):
    page.title = "Módulo de Habitaciones"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def agregar_habitacion(e):
        
        pass

    def editar_habitacion(e):
        
        pass

    def eliminar_habitacion(e):
        
        pass

    def listar_habitaciones(e):
        
        pass

    codigo_field = ft.TextField(label="Código", width=300)
    numero_field = ft.TextField(label="Número", width=300)
    tipo_field = ft.TextField(label="Tipo", width=300)
    capacidad_field = ft.TextField(label="Capacidad", width=300)
    precio_field = ft.TextField(label="Precio", width=300)
    status_field = ft.TextField(label="Estado", width=300)

    agregar_button = ft.ElevatedButton("Agregar Habitación", on_click=agregar_habitacion)
    editar_button = ft.ElevatedButton("Editar Habitación", on_click=editar_habitacion)
    eliminar_button = ft.ElevatedButton("Eliminar Habitación", on_click=eliminar_habitacion)
    listar_button = ft.ElevatedButton("Listar Habitaciones", on_click=listar_habitaciones)

    page.add(
        ft.Column(
            [
                ft.Text("Módulo de Habitaciones", size=20),
                codigo_field,
                numero_field,
                tipo_field,
                capacidad_field,
                precio_field,
                status_field,
                agregar_button,
                editar_button,
                eliminar_button,
                listar_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )