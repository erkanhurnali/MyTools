import flet as ft
from myButtons import MyButton
from myAlarms import AlarmButton
from myMouseButtons import RightButton
import utils as utils
from mykeyboars import OskButton, TouchKButton
from mySpeakButton import SpeakButton, VoiceButton
from myShrcuts import CutButton, ToogleButton
from flet import Page, Container, IconButton, Row, icons, ProgressRing, Stack, colors, UserControl, TextField, Column
import pyautogui
from pynput.mouse import Button, Controller, Listener
import time
from tkinter import *
import mySettinnsButton
import myPanButton
from myFletForTkTimer import FletForTkTimer
from utils.MyTimer import MyTimer
from utils.MouseMonitoring import MouseMonitoring
from utils.MyTkTimerWithForm import MyTkTimerWithForm

def main(page: Page):

    # MyTimer()

    # MyTkTimerWithForm()

    page.title = "MyTools - Tiny"
    page.window_height = 87
    page.window_top = 70
    page.window_left = 120
    page.window_width = 365
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




    main_row.controls.append(AlarmButton(
        icon=icons.NOTIFICATION_IMPORTANT_OUTLINED,
        selected_icon=icons.NOTIFICATION_IMPORTANT,
        ipucu="Sound the alarm", 
        color=colors.AMBER,
    ))

    main_row.controls.append(ToogleButton(
        icon=icons.CHANGE_CIRCLE_OUTLINED,
        selected_icon=icons.CHANGE_CIRCLE,
        ipucu="Change Active Program", 
        color=colors.CYAN
    ))

    main_row.controls.append(
        mySettinnsButton.SettingButton(
            icon=icons.SETTINGS_OUTLINED,
            selected_icon=icons.SETTINGS,
            color=colors.AMBER_900,
            ipucu="Settings",
        )
    )

    main_col = Column(controls=[main_row, speakText_row])
    page.add(main_col)

    MouseMonitoring(rb=rightButton)
    

ft.app(target=main, assets_dir="assets")
