# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import flet as ft


def main(page:ft.Page):
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=lambda _: None,
    )

    text = ft.Container(
                content=ft.Text(
                        "This is not a regular app, like many others. This application is the first ever created and published in the newest, revolutionary Green Cloud Technology. Our outstanding Marysia Software team found a way to connect two well-established environments - Phyton -Django- and Dart -Flutter. It's just the first step, but the journey looks very promising. Try our Reservation App Demo and find out more on www.marysia.app.",
                        font_family="Consolas",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.BLACK,    
                    ),
                padding=50,
                margin=ft.margin.symmetric(horizontal=50),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.colors.WHITE54, ft.colors.BLUE_GREY_400],
                ),
                border=ft.border.all(1, ft.colors.RED),
                width=600,
                opacity=1,
                border_radius=20,
    )
    
    column = ft.Column(alignment=ft.MainAxisAlignment.SPACE_EVENLY, 
                       horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    container = ft.Container(
        content=column,
        alignment=ft.alignment.center
    )

    image = ft.Image(
        src="/icons/logo1.png",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
        
    )

    c1 = ft.Container(
        content=ft.ElevatedButton("Reservation app DEMO"),
        padding=10,
        margin=10,
    )

    column.controls.append(image)
    column.controls.append(text)
    column.controls.append(c1)
    

    page.padding = 0
    page.add(
        ft.Container(
            image_src="/background22.png",
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=container
        )
    )

if __name__ == '__main__':
    ft.app(
        main,
        assets_dir="assets"
    )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
