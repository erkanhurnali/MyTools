from flet import icons, colors, Page
import myButtons
from ctypes import *


class RightButton(myButtons.MyButton):
    def __init__(
        self,
        icon: icons,
        ipucu: str,
        color: colors,
        selected_icon: icons,
    ):
        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            selected_icon=selected_icon,
        )

    def click(self, e,):
        super().click(e=e)
        print("RightButton cilck fonksyonu çalışıyor")

        # c_file="./mylibl.so"
        c_file="C:/Users/erkan/OneDrive/Belgeler/GitHub/MyTools/mylibl.so"
        c_fun=CDLL(c_file)
        c_fun.swap(int(1))
        self.iconButton.selected = True

    def build(self):
        return super().build()
