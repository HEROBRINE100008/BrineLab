import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#282c34"
    texto1 = ft.Text("BrineColumn", size=28, color=ft.Colors.WHITE)
    texto2 = ft.Text("texto2", size=18, color=ft.Colors.WHITE)
    texto3 = ft.Text("texto3", size=18, color=ft.Colors.WHITE)

    fila_textos = ft.Row(
            controls=[texto1, texto2, texto3]
    )

    page.add(fila_textos)


ft.run(main)
