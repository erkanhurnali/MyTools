import flet as ft
import time

from flet import Page, Container, IconButton, icons, ProgressRing, Stack, colors, UserControl


class MyButton(UserControl):
    def __init__(self,
                 icon: icons = None,
                 selected_icon: icons = None,
                 ipucu: str = None,
                 color: colors = None,
                 size: int = None,
                 selected: bool = None,
                 page: Page = None
                 ):
        super().__init__()
        self.icon = icon
        self.selectedIcon = selected_icon
        self.ipucu = ipucu
        self.color = color
        self.size = size
        self.is_hover = False
        self.iconButton = None
        self.keyboardClass = None
        self.scale=ft.transform.Scale(1)
        self.animate_scale=ft.animation.Animation(100,ft.AnimationCurve.BOUNCE_IN_OUT)#

    def animate(self,e):
        self.scale = 1.3
        self.update()

    @property
    def selected(self):
        return self.iconButton.selected

    @selected.setter
    def selected(self, value):
        print("selected setter")

    def hover(self, e):
        print("MyButton sınıfının hover fonksiyonu çalışıyor")
        self.is_hover = True if e.data == "true" else False
        if self.is_hover:
            self.animate(e)#
            self.page.title = self.ipucu
            self.page.update()

            self.progressRing.value = 0
            for i in range(101):
                    self.progressRing.value = 0.01*i
                    time.sleep(0.01)
                    self.update()
                    if not self.is_hover:
                        self.progressRing.value = 0
                        break
                    if i == 100: 
                        self.click(e)
                        audio3 = ft.Audio(src=f"/sounds/pop.wav", autoplay=True)
                        self.page.overlay.append(audio3)
                        self.page.update()

        else:
            self.page.title = "TiniMini"
            self.scale=ft.transform.Scale(1)#
            self.page.update()

        self.progressRing.value = 0
        self.update()

    def click(self, e):
        # audio1 = ft.Audio(
        #     # src="click.wav", autoplay=True)
        #     src="pop.wav", autoplay=True)
        # self.page.overlay.append(audio1)
        # self.page.update()

        print("MyButton click fonsiyonu çalışıyor")

    def build(self):
        self.progressRing = ProgressRing(
            value=0,
        )
        self.iconButton = IconButton(
            icon=self.icon,
            selected_icon=self.selectedIcon,
            icon_size=30,
            icon_color=self.color,
        )
        stack = Stack(
            controls=[
                Container(
                    content=self.iconButton,
                    alignment=ft.alignment.center
                ),
                Container(
                    content=self.progressRing,
                    alignment=ft.alignment.center
                ),
            ],
            width=50,
            height=50
        )
        main_container = Container(
            content=stack,
            on_hover=self.hover,
            on_click=self.click,
        )
        return main_container
