import flet as ft

def main(page: ft.Page):
    page.title = "Hotel TRIVAGO - Administrador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def open_huespedes(e):
        page.clean()
        huespedes_module(page)

    def open_habitaciones(e):
        page.clean()
        HabitacionesViews(page)

    def open_ingresos(e):
        page.clean()
        ingresos_module(page)

    # Botones para abrir los módulos
    huespedes_button = ft.ElevatedButton("Huéspedes", on_click=open_huespedes)
    habitaciones_button = ft.ElevatedButton("Habitaciones", on_click=open_habitaciones)
    ingresos_button = ft.ElevatedButton("Ingresos", on_click=open_ingresos)

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

    def volver_al_menu(e):
        page.clean()  # Limpia la página actual
        main(page)  # Carga el menú principal

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
    volver_button = ft.ElevatedButton("Volver al Menú", on_click=volver_al_menu)

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
                listar_button,
                volver_button  # Agregado el botón de volver al menú
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)