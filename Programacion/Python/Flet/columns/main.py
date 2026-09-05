import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#282c34"
    texto1 = ft.Text("BrineColumn", size=28, color=ft.Colors.WHITE)
    texto2 = ft.Text("texto2", size=18, color=ft.Colors.WHITE)
    texto3 = ft.Text("texto3", size=18, color=ft.Colors.WHITE)

    fila_textos = ft.Row(
            controls=[texto1, texto2, texto3],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
    )

    boton1 = ft.FilledButton(content="Botón 1")
    boton2 = ft.FilledButton(content="Botón 2")
    boton3 = ft.FilledButton(content="Botón 3")

    fila_botones = ft.Row(
            controls=[boton1, boton2, boton3],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
            )
    page.add(fila_textos, fila_botones)


ft.run(main)
