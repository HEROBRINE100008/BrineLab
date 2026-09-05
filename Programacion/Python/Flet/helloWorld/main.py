import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#282c34"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    texto = ft.Text("Hello World")
    texto2 = ft.Text("Hola Mundo")

    def cambiar_texto(e):
        texto2.value = "你好世界"
        page.update()

    boton = ft.FilledButton(
            content="A po yo soy chino",
            on_click=cambiar_texto
            )
    page.add(texto, texto2, boton)


ft.run(main)
