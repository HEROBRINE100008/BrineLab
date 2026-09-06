import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#121214"
    page.title = "BrineInv"
    hi = ft.Text("hola")

    page.add(hi)


ft.app(target=main)
