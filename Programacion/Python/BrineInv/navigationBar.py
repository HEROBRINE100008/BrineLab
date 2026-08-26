import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#121214"
    page.title = "BrineInv"

    page.add(
        ft.Row(
            controls=[
                ft.WindowDragArea(
                    width=page.width - 100,
                    height=25,
                    content=ft.Container(bgcolor="#1E1E22")
                ),
                ft.IconButton()
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
