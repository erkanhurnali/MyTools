import flet as ft
from myAlarms import AlarmButton
from myMouseButtons import RightButton
# import utils as utils
from flet import Page,  Row, icons, colors
from utils.MouseMonitoring import MouseMonitoring

def main(page: Page):

    page.title = "TiniMini"
    page.window_height = 87
    page.window_top = 70
    page.window_left = 120
    page.window_width = 10
    page.window_always_on_top = True
    page.padding = 0
    page.window_resizable = False
    page.window_focused = False
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.window_maximizable=False
    page.window_minimizable=False
    page.window_maximized=False

    main_row = Row(
        spacing=0,
        alignment = ft.MainAxisAlignment.CENTER
    )
    rightButton = RightButton(
        icon=icons.MOUSE_OUTLINED,
        selected_icon=icons.MOUSE,
        ipucu="Right Click",
        color=colors.TEAL,
    )

    main_row.controls.append(
        rightButton,
    )

    main_row.controls.append(AlarmButton(
        icon=icons.NOTIFICATION_IMPORTANT_OUTLINED,
        selected_icon=icons.NOTIFICATION_IMPORTANT,
        ipucu="Sound the alarm", 
        color=colors.AMBER,
    ))

    page.add(main_row)

    MouseMonitoring(rb=rightButton)
    

ft.app(target=main, assets_dir="assets")
