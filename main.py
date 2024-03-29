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

    page.title = "MyTools - GlassOuse"
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
    main_row.controls.append(
        myPanButton.PanButton(icon=icons.PAN_TOOL_OUTLINED,
                 selected_icon=icons.PAN_TOOL_ROUNDED,
                 ipucu="Pan", 
                 color=colors.PURPLE),
    )

    # main_row.controls.append(
    #     MyButton(icon=icons.ADS_CLICK_OUTLINED,
    #              selected_icon=icons.ADS_CLICK,
    #              ipucu="Click on it while waiting", 
    #              color=colors.PURPLE),
    # )
    rightButton = RightButton(
        icon=icons.MOUSE_OUTLINED,
        selected_icon=icons.MOUSE,
        ipucu="Right Click",
        color=colors.TEAL,
    )

    main_row.controls.append(
        rightButton,
    )


    # from clickWaiting import ClickWatingHiddenForm
    # main_row.controls.append(ClickWatingHiddenForm())
    # main_row.controls.append(FletForTkTimer())

    # main_row.controls.append(
    #     TouchKButton(icon=icons.KEYBOARD_HIDE_OUTLINED,
    #              selected_icon=icons.KEYBOARD_HIDE,
    #              ipucu="Touch keyboard", 
    #              color=colors.PURPLE),
    # )



    main_row.controls.append(AlarmButton(
        icon=icons.NOTIFICATION_IMPORTANT_OUTLINED,
        selected_icon=icons.NOTIFICATION_IMPORTANT,
        ipucu="Sound the alarm", 
        color=colors.AMBER,
    ))
    # main_row.controls.append(OskButton(
    #     icon=icons.KEYBOARD_OUTLINED,
    #     selected_icon=icons.KEYBOARD,
    #     ipucu="On-Screen Keyboard",
    #     color=colors.PINK_ACCENT
    # ))
    main_row.controls.append(
        TouchKButton(icon=icons.KEYBOARD_OUTLINED,
                 selected_icon=icons.KEYBOARD,
                 ipucu="Touch keyboard", 
                 color=colors.PINK_ACCENT),
    )

    main_row.controls.append(ToogleButton(
        icon=icons.CHANGE_CIRCLE_OUTLINED,
        selected_icon=icons.CHANGE_CIRCLE,
        ipucu="Change Active Program", 
        color=colors.CYAN
    ))

    textField = TextField(
        text_size=30,
        width=450,
        hint_text="Please enter the text...",
        color=colors.CYAN_ACCENT,
    )
    voiceButton = VoiceButton(
        icon=icons.VOLUME_UP_OUTLINED,
        ipucu="Read",
        selected_icon=icons.VOLUME_UP,
        color=colors.CYAN_ACCENT,
        textField=textField
    )
    speakText_row = Row(controls=[textField, voiceButton],)

    speakText_row.visible = False

    main_row.controls.append(SpeakButton(
        icon=icons.RECORD_VOICE_OVER_OUTLINED,
        selected_icon=icons.RECORD_VOICE_OVER,
        ipucu="Read the post", 
        color=colors.CYAN_ACCENT,
        speak_row=speakText_row,
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
