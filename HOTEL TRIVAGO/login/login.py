import flet as ft
from helpers import convert_image_to_base64
import mysql.connector

#CREACION DEL LOGIN 
mensaje = ft.Text("")
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hospedaje"
    )

def verificar_login(e):
    usuario = user_field.value
    contrasena = pass_field.value

    conn = conectar_db()
    cursor = conn.cursor()
    consulta = "SELECT * FROM usuarios WHERE username=%s AND password=%s"
    cursor.execute(consulta, (usuario, contrasena))
    resultado = cursor.fetchone()

    if resultado:
        mensaje.value = "Inicio de sesión exitoso"
        mensaje.color = "green"
    else:
        mensaje.value = "Usuario o contraseña incorrectos"
        mensaje.color = "red"

    conn.close()
    page.update()


#CREACION INTERFAZ
def main(page: ft.Page):
    page.title  = "HOTEL TRIVAGO"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.appbar = ft.AppBar(
        title=ft.Text("Inicio de sesión"),
        bgcolor=ft.Colors.BLUE
    )

    image = convert_image_to_base64("hotel_tri/assets/Trivago_logo.png")
    text_sesion = ft.Text(value="Iniciando sesión...", size=20, weight="bold", text_align="center")
    text_sesion.visible = False
    def handleOnClick():
        text_sesion.visible = True
        verificar_login(None)
        page.update()
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
                                            src_base64=image, width=300
                                        ),
                                    ]),
                                    ft.Row(
                                            controls=[
                                            ft.TextField(label="Usuario", width=300),
                                            ]
                                    ),
                                    ft.Row(
                                            controls=[
                                            ft.TextField(label="Contraseña", width=300, password=True),
                                            ]
                                    ),
                                    ft.Row(
                                            controls=[
                                                ft.ElevatedButton("Iniciar sesión", on_click=lambda _: handleOnClick(), width=300)])
                                ])
                        )
                    ], expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ], expand=True
        )
    )


ft.app(main)