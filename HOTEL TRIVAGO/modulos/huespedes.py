import flet as ft

def huespedes_module(page: ft.Page):
    page.title = "Módulo de Huéspedes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def agregar_huesped(e):
        
        pass

    def editar_huesped(e):
        
        pass

    def eliminar_huesped(e):
        
        pass

    def listar_huespedes(e):
        
        pass

    cedula_field = ft.TextField(label="Cédula", width=300)
    nombres_field = ft.TextField(label="Nombres", width=300)
    apellidos_field = ft.TextField(label="Apellidos", width=300)
    direccion_field = ft.TextField(label="Dirección", width=300)
    ciudad_field = ft.TextField(label="Ciudad", width=300)
    email_field = ft.TextField(label="Email", width=300)
    telefono_field = ft.TextField(label="Teléfono", width=300)

    agregar_button = ft.ElevatedButton("Agregar Huésped", on_click=agregar_huesped)
    editar_button = ft.ElevatedButton("Editar Huésped", on_click=editar_huesped)
    eliminar_button = ft.ElevatedButton("Eliminar Huésped", on_click=eliminar_huesped)
    listar_button = ft.ElevatedButton("Listar Huéspedes", on_click=listar_huespedes)

    page.add(
        ft.Column(
            [
                ft.Text("Módulo de Huéspedes", size=20),
                cedula_field,
                nombres_field,
                apellidos_field,
                direccion_field,
                ciudad_field,
                email_field,
                telefono_field,
                agregar_button,
                editar_button,
                eliminar_button,
                listar_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )