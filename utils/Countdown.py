import time
import threading
import flet as ft

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
            # time.sleep(5)
            # time.sleep(1)
            time.sleep(.3)
            self.duration -= 1
            self.text.value=f"{self.duration}"
            # self.text.radius=self.duration
            # self.text.value=self.duration
            self.update()
            print(f"self.duration={self.duration}")

    def build(self):
        self.text=ft.Text(color=ft.colors.CYAN_900)
        # self.text=ft.CircleAvatar(bgcolor=ft.colors.CYAN_900,radius=20)
        # self.text=ft.ProgressBar()
        return self.text

