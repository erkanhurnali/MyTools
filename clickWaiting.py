from flet import icons, colors, UserControl
import myButtons
import tkinter
import threading
import utils as utils

# class ClickWatingHiddenForm(UserControl):
class ClickWatingHiddenForm(myButtons.MyButton):
    def __init__(self):
    # def __init__(self,
                #  icon: icons,
                #  selected_icon: icons,
                #  ipucu: str,
                #  color: colors,
                #  ):
        # super().__init__(
        #     icon=icon,
        #     ipucu=ipucu,
        #     color=color,
        #     selected_icon=selected_icon,
        # )
        super().__init__()
        import time
        print(f"ClickWatingHiddenForm.init(printe yazdırılmadı) \t\t time={time.time()}")

    def did_mount(self):
        print("ClickWatingButton-did_mount")
        # self.running = True
        self.th = threading.Thread(target=self.createForm, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        # self.running = False
        print("SettingsButton2-will_unmount")


    def createForm(self):
        # global self.settingsForm
        self.clickWaingForm = tkinter.Tk()
        self.clickWaingForm.geometry("800x500+300+300")
        self.clickWaingForm.attributes("-alpha",0.9)
        # self.clickWaingForm.wm_overrideredirect(1)
        self.hide()
        self.clickWaingForm.mainloop()

    def show(self):
        self.clickWaingForm.deiconify()
        self.showing = True

    def hide(self):
        # self.settingForm.iconify()
        self.clickWaingForm.withdraw()
        self.showing = False
        # self.settingForm.wm_withdraw

    def click(self, e):
        super().click(e=e)
        self.update()

    def build(self):
        return super().build()
        # super().build()
        # from flet import Text
        # return Text()
