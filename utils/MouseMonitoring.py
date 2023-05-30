from utils.MyTimer import MyTimer
from pynput.mouse import Listener
import flet as ft

import pyautogui

class MouseMonitoring(MyTimer):
    rightButton =None
    def __init__(self,rb):
        super().__init__()
        self.rightButton = rb
        with Listener(on_click=self.on_click, ) as listener:
            listener.join()

    def on_click(self,x, y, button, pressed):
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        if pressed:
            print("-----------------")
        else:
            print()
        print(f"{button} ")
        print('\bBasıldı' if pressed else 'Bırakıldı')

        if (button == button.left) and (not self.rightButton.is_hover) and (not pressed) and (self.rightButton.selected):
            print("sanal sağ tuş-pyautogui")
            button=button.right
            pyautogui.click(button='right')  # right-click the mouse

            audio2 = ft.Audio(
                src="pop_giris.wav", autoplay=True)
            self.rightButton.page.overlay.append(audio2)
            self.rightButton.page.update()
            self.rightButton.iconButton.selected = False
            self.rightButton.update()


