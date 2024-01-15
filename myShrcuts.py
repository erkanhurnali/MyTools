import os
from flet import UserControl, Audio, icons, colors, Page
import myButtons
# from myTools import
# import keyboard
# from pynput.keyboard import Key, Controller
import time
# keyboard1 = Controller()


class ToogleButton(myButtons.MyButton):
    def __init__(self,
                 icon: icons,
                 ipucu: str,
                 color: colors,
                 selected_icon: icons,
                 #  page=Page,
                 ):
        super().__init__(
            icon=icon,
             ipucu=ipucu,
            color=color,
            #  page=page,
            selected_icon=selected_icon,
        )
    # def __init__(self, icon: icons, ipucu: str = None, color: colors = None, page=Page):
        # super().__init__(icon, ipucu, color, on_click=self.click)
        # self.page = page

    def click(self, e):
        super().click(e=e)
        keyboard.press_and_release('alt+tab', do_release=False)
        # keyboard.press('alt')
        time.sleep(5)
        keyboard.release('alt')
        # keyboard.relase('tab')
        # keyboard.release()
        print("ToogleButton click fonksiyonu çalışıyor")
        self.iconButton.selected=False
        self.update()


    def build(self):
        # super().
        return super().build()
#
