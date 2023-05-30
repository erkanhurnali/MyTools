import os
from flet import icons, colors
import myButtons


class OskButton(myButtons.MyButton):
    def __init__(self,
                 icon: icons = None,
                 selected_icon: icons = None,
                 ipucu: str = None,
                 color: colors = None,
                 ):
        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            selected_icon=selected_icon,
        )

    def click(self, e):
        super().click(e=e)
        if self.iconButton.selected:
            self.iconButton.selected = False
            # os.system('wmic process where name="osk" delete') 
            # os.system('wmic process where name="TabTip.exe" delete') 
            os.system('wmic process where name="osk.exe" delete') 
            # os.system('wmic process where name="TabTip.exe" delete') 

        else:
            self.iconButton.selected = True
            os.system("osk")
            # os.system("TabTip")
            # os.system("TabTip.exe")
            self.iconButton.selected = False

        self.update()

    def build(self):
        return super().build()
