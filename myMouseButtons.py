from flet import icons, colors, Page
import myButtons

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

    def build(self):
        return super().build()
