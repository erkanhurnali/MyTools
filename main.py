import flet as ft
from myButtons import MyButton
from myAlarms import AlarmButton
from myMouseButtons import RightButton
# import utils as utils
from myShrcuts import ToogleButton
from flet import Page,  Row, icons, colors, Column
# import time
from utils.MouseMonitoring import MouseMonitoring

def main(page: Page):

    page.title = "MyTools - Tiny"
    page.window_height = 87
    page.window_top = 70
    page.window_left = 120
    page.window_width = 165
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

    main_row.controls.append(ToogleButton(
        icon=icons.CHANGE_CIRCLE_OUTLINED,
        selected_icon=icons.CHANGE_CIRCLE,
        ipucu="Change Active Program", 
        color=colors.CYAN
    ))

    main_row.controls.append(AlarmButton(
        icon=icons.NOTIFICATION_IMPORTANT_OUTLINED,
        selected_icon=icons.NOTIFICATION_IMPORTANT,
        ipucu="Sound the alarm", 
        color=colors.AMBER,
    ))


    main_col = Column(controls=[main_row,])
    page.add(main_col)

    MouseMonitoring(rb=rightButton)
    

ft.app(target=main, assets_dir="assets")
