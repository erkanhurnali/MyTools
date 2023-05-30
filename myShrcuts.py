import os
from flet import UserControl, Audio, icons, colors, Page
import myButtons
# from myTools import
import keyboard
from pynput.keyboard import Key, Controller
import time
keyboard1 = Controller()


class CutButton(myButtons.MyButton):
    def __init__(self,
                 icon: icons,
                #  ipucu: str,
                 color: colors,
                 selected_icon: icons,

                 #  page=Page,
                 ):
        super().__init__(
            icon=icon,
            #  ipucu,
            color=color,
            #  page=page,
            selected_icon=selected_icon,
        )
        # super().__init__(icon, ipucu, color, on_click=self.click)
        # self.page = page

    def click(self, e):
        # keyboard.press_and_release('ctrl+x', do_release=False)
        # time.sleep(1)
        # keyboard.release('ctrl+x')
        # keyboard.press_and_release('ctrl+a')
        # keyboard.press_and_release('ctrl+A')
        # keyboard.press_and_release(hotkey='alt+F4')
        # keyboard.send('ctrl+alt+del')
        # keyboard.press_and_release('alt+tab',do_release=False)
        print("CutButton click fonksiyonu çalışıyor")
        keyboard1.press(Key.ctrl)
        # keyboard1.press('x')
        # keyboard1.release('x')
        # keyboard1.press(Key.x)
        # keyboard1.release(Key.x)
        keyboard1.release(Key.ctrl)

    def build(self):
        # super().
        return super().build()


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
