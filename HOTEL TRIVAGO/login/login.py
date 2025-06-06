import flet as ft
import os

def main(page: ft.Page):
    page.title = "HOTEL TRIVAGO"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.appbar = ft.AppBar(
        title=ft.Text("Inicio de sesión"),
        bgcolor=ft.Colors.BLUE
    )

    # Ruta de la imagen del logo
    relative_image_path = "HOTEL TRIVAGO/login/logo/Trivago_logo.png"
    absolute_image_path = os.path.abspath(relative_image_path)

    if not os.path.exists(absolute_image_path):
        print(f"La imagen no existe en la ruta especificada: {absolute_image_path}")
        absolute_image_path = None

    text_sesion = ft.Text(value="Iniciando sesión...", size=20, weight="bold", text_align="center")
    text_sesion.visible = False
    text_error = ft.Text(value="", size=14, color=ft.Colors.RED, text_align="center")
    text_error.visible = False

    def handleOnClick(e):
        username = user_field.value
        password = password_field.value
        if username == "admin" and password == "1234":
            text_sesion.value = "Inicio de sesión exitoso"
            text_sesion.color = ft.Colors.GREEN
            text_error.visible = False
            text_sesion.visible = True
        else:
            text_error.value = "Usuario o contraseña incorrectos"
            text_error.visible = True
            text_sesion.visible = False
        page.update()

    user_field = ft.TextField(label="Usuario", width=300)
    password_field = ft.TextField(label="Contraseña", width=300, password=True)

    # Footer
    footer = ft.Container(
        width=page.width,
        height=50,
        bgcolor=ft.Colors.BLUE,
        alignment=ft.alignment.center,
        content=ft.Text("© 2025 Trivago", color=ft.Colors.WHITE)
    )

    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            width=350,
                            height=400,
                            padding=20,
                            border_radius=10,
                            bgcolor=ft.Colors.GREY_200,
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                controls=[
                                    ft.Row(controls=[
                                        ft.Image(
                                            src=absolute_image_path,  # Cargar la imagen directamente desde la ruta absoluta
                                            width=300
                                        ) if absolute_image_path else ft.Text("Imagen no encontrada"),
                                    ]),
                                    ft.Row(
                                        controls=[
                                            user_field,
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            password_field,
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton("Iniciar sesión", on_click=handleOnClick, width=300)
                                        ]
                                    )
                                ] + [text_sesion, text_error]
                            )
                        )
                    ], expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ], expand=True, vertical_alignment=ft.MainAxisAlignment.CENTER
        ),
        footer  # Agregar el footer al final de la página
    )

ft.app(main)