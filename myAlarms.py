from flet import UserControl, Audio, icons, colors, Page
import myButtons
# from myTools import
import time



class AlarmButton(myButtons.MyButton):
    def __init__(self,
                 icon: icons,
                 selected_icon: icons,
                 ipucu: str,
                 color: colors = None,
                 page=Page
                 ):

        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            selected_icon=selected_icon,
        )

        # super().__init__(icon, ipucu, color)
        # super().__init__(icon, ipucu, color,
        #                  selected_icon=selected_icon,
        #                  )
        # super().__init__(icon, ipucu, color,on_click=self.click)
        # self.
        # super().controls
        # self.page = page

    def click(self, e):
        print("AlarmButton cilck fonksyonu çalışıyor")
        self.page.title = "alarm çalıyor"

        # super().click(e=e)
        audio1 = Audio(src="alarm.wav", autoplay=True)
        # audio1 = Audio(src="alarm.wav", autoplay=True)
        self.page.overlay.append(audio1)
        self.page.update()
        time.sleep(5)
        # audio1.pause()
        # audio1.release()
        # self.page.overlay.clear()
        self.page.overlay.remove(audio1)

        self.iconButton.selected = False

    def build(self):
        # audio1 = Audio(src="alarm.wav", autoplay=True)
        # self.page.overlay.append(audio1)
        # self.page.update()

        return super().build()

