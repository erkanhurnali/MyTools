from flet import icons, colors, Page
import myButtons
# import pyautogui
# from pynput.mouse import Button, Controller, Listener

# mouse1 = Controller()


class RightButton(myButtons.MyButton):
    def __init__(
        self,
        icon: icons,
        ipucu: str,
        color: colors,
        selected_icon: icons,
        #  page: Page
    ):
        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            #  page=page,
            selected_icon=selected_icon,
        )
        # self.sag_tus = False
        # self.page = page
        # self.selected=no

    def click(self, e,):
        super().click(e=e)
        # self.sag_tus = True
        # self.selected = not self.selected
        print("RightButton cilck fonksyonu çalışıyor")
        self.iconButton.selected = not self.iconButton.selected
        # print(f"self.selected={self.selected}")
        # self.update()
        # self.page.update()

    def build(self):
        return super().build()
