import flet as ft
import time, threading

import os
from flet import UserControl, Audio, icons, colors, Page
import myButtons
# from myTools import


class Countdown(ft.UserControl):
    # x = Countdown(2000)
    def __init__(self, duration:int=2000):
        super().__init__()
        self.duration = duration

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.duration and self.running:
            # mins, secs = divmod(self.duration, 60)
            # self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            # time.sleep(5)
            # time.sleep(1)
            time.sleep(.3)
            self.duration -= 1
            # self.countdown.value=self.duration
            # self.progressBar.value=self.duration
            # self.progressRing.value=self.duration
            self.text.value=f"{self.duration}"
            self.update()
            print(f"self.duration={self.duration}")
            # print(f"self.progressBar.value={self.progressBar.value}")

    def build(self):
        # self.progressBar = ft.ProgressBar(height=100,value=30)
        # self.progressRing=ft.ProgressRing(value=50)
        # self.progressBar = ft.ProgressBar(height=100,value=0)
        # return self.progressBar
        self.text=ft.Text()
        # main_col=ft.Column(controls=[self.text,self.progressBar,self.progressRing])
        return self.text
        # return main_col

# def main(page: ft.Page):
#     page.window_left=500
#     page.window_top=200
#     page.window_height=300
#     page.window_width=200
#     countdown=Countdown(duration=50)
#     # countdown=Countdown(duration=100)
#     page.add(countdown)

# ft.app(target=main)