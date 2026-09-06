import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#121214"
    page.title = "BrineInv"
    page.window.min_width = 600
    page.window.min_height = 400

    rail = ft.NavigationRail(
        selected_index=0,
        bgcolor="#1E1E22",
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        on_change=lambda e: print("Selected destination:",
                                  e.control.selected_index),
        leading=ft.FloatingActionButton(
            icon=ft.Icons.CREATE,
            content="Add",
            on_click=lambda e: print("FAB clicked!"),
        ),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="First",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label=ft.Text("Settings"),
            ),
        ],
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Row(
                expand=True,
                controls=[
                    ft.SelectionArea(content=rail),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                        controls=[ft.Text("Body!")],
                    ),
                ],
            ),
        )
    )


if __name__ == "__main__":
     ft.run(main)
