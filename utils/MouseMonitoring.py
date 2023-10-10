from utils.MyTimer import MyTimer
from pynput.mouse import Listener
import flet as ft
from ctypes import *



class MouseMonitoring(MyTimer):
    rightButton =None
    sagTiklandi = False
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
        if (button == button.right) and (self.rightButton.iconButton.selected == True) and (self.sagTiklandi==False):
            self.sagTiklandi = True
            audio2 = ft.Audio(src=f"/sounds/pop_giris.wav", autoplay=True)
            self.rightButton.page.overlay.append(audio2)
            self.rightButton.page.update()

        else:

            if (button == button.right) and (self.rightButton.iconButton.selected == True) and (self.sagTiklandi):
                # print("sanal sağ tuş-pyautogui")
                c_fun=CDLL("./mylibl.so")
                # c_fun=CDLL(f"/c_lib/mylibl.so")
                c_fun.swap(int(1))


                self.rightButton.iconButton.selected = False
                
                self.rightButton.update()
                self.sagTiklandi = False


