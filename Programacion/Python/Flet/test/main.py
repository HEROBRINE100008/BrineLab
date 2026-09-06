import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#282c34"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
            "Mi Lista de Tareas con Flet",
            size=30, weight=ft.FontWeight.BOLD
            )
    page.add(titulo)



ft.run(main)
