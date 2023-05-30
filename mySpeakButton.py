from flet import UserControl, Audio, icons, colors, Page, Ref, TextField, Row
import myButtons
import flet as ft
from gtts import gTTS
import os
import time
# from myTools import
from utils.CalculateToolBarSize import CalculateToolBarSize

class SpeakButton(myButtons.MyButton):
    # def __init__(self, icon: icons,  ipucu: str = None, color: colors = None, page: Page = None, speak_row: Row = None):
    def __init__(self,
                 icon: icons,
                 selected_icon: icons,
                 ipucu: str,
                 color: colors = None,
                 #  page: Page = None,
                 speak_row: Row = None,
                 ):
        # def __init__(self, icon: icons, selected_icon: icons, ipucu: str = None, color: colors = None, page: Page = None, speak_row: Row = None):
        # def __init__(self, icon: icons, selected_icon: icons = None, ipucu: str = None, color: colors = None, page: Page = None, speak_row: Row = None, selected: bool = False):
        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            #  page=page,
            selected_icon=selected_icon,
        )
        # super().__init__(icon, ipucu, color, on_click=self.click)
        # super().__init__(icon, ipucu, color, on_click=self.click, selected_icon=selected_icon, selected=selected)
        self.speakRow = speak_row
        # self.page = page

    def click(self, e):
        super().click(e=e)

        print("SpeakButton cilck fonksyonu çalışıyor")
        self.speakRow.visible = not self.speakRow.visible
        # self.selected = True
        current_pageWidth = self.page.window_width
        current_pageHeight = self.page.window_height
        # is_large_size=None if is_large_size == None else False
        # if calculateToolBarSize  is None:
        calculateToolBarSize = CalculateToolBarSize()
        # is_large_size = None
        # if calculateToolBarSize.is_large_size == None:
        #     calculateToolBarSize.is_large_size = False
        # else:
        #     calculateToolBarSize.is_large_size = not calculateToolBarSize.is_large_size

        setattr(calculateToolBarSize,"is_large_size",False)
        if calculateToolBarSize.is_large_size:
            self.page.window_height = current_pageHeight
            self.page.window_width = current_pageWidth
            self.iconButton.selected = False
            calculateToolBarSize.is_large_size = False
        else:
            self.page.window_height = 190
            self.page.window_width = 550
            self.iconButton.selected = True
            calculateToolBarSize.is_large_size = True
        self.page.update()

    def build(self):
        return super().build()


class VoiceButton(myButtons.MyButton):
    def __init__(self,
                 icon: icons,
                 selected_icon: icons,
                 ipucu: str,
                 color: colors = None,
                 textField: TextField = None,
                 #  page: Page = None,
                 ):
        # def __init__(self, icon: icons, ipucu: str = None, color: colors = None, textField: TextField = None, page: Page = None):
        # super().__init__(icon, ipucu, color)
        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            #  page=page,
            selected_icon=selected_icon,
        )
        # super().__init__(icon, ipucu, color, on_click=self.click)
        # self.page = page
        self.textField = textField

    def click(self, e):
        super().click(e=e)
        tts = gTTS(text=self.textField.value, lang="tr")
        fileName = 'erkan.mp3'
        tts.save(fileName)

        audio1 = Audio(
            src=fileName, autoplay=True)

        self.page.overlay.append(audio1)
        self.page.update()

        time.sleep(5)
        os.remove(fileName)

    def build(self):
        # super().
        return super().build()
