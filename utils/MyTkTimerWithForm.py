import os
from flet import icons, colors
import myButtons
import tkinter
import threading
import time


class MyTkTimerWithForm():
    def __init__(self,
                 ):            
        self.th = threading.Thread(
                target=self.createForm,
                args=(),
                daemon=True
            )
        self.th.start()

        super().__init__(
        )
        print(f"MyTkTimerWithForm.init() \t\t\t time={time.time()}")

    def callback(self):
        # self.settingForm.l

        self.settingForm.after(1000,self.callback)
        pass

    def createForm(self):
        self.settingForm = tkinter.Tk()
        self.settingForm.title("MyTkTimerWithForm")
        self.settingForm.geometry("100x100+300+300")
        self.settingForm.attributes("-alpha",0.5)
        # self.settingForm.wm_overrideredirect(1)
        blTime=tkinter.Label(self.settingForm, text=f"{time.strftime('%H:%M:%S')}").pack()

        self.callback()
        # self.settingForm.mainloop()
        # self.hide()

    # def show(self):
    #     self.settingForm.deiconify()

    def hide(self):
        # self.settingForm.iconify()
        self.settingForm.withdraw()
        # self.settingForm.wm_withdraw

    def click(self, e):
        super().click(e=e)
        # if self.showForm:


