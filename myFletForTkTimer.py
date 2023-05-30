from flet import icons, colors, UserControl
import flet
import tkinter
import threading
import utils as utils
import time

class FletForTkTimer(UserControl):
# class FletForTkTimer(flet.Control):
    def __init__(self):
        super().__init__()
        # print(f"FletForTkTimer.init(printe yazdırılmadı) \t\t time={time.time()}")
        print(f"FletForTkTimer.init() \t\t\t time={time.time()}")
        # self.n
        self.th = threading.Thread(target=self.createForm, args=(), daemon=True)
        self.th.start()

    def did_mount(self):
        print(f"FletForTkTimer.did_mount() \t\t time={time.time()}")
        # self.running = True
        # self.th = threading.Thread(target=self.createForm, args=(), daemon=True)
        # self.th.start()

    def will_unmount(self):
        print(f"FletForTkTimer-will_unmount \t\t time={time.time()}")
        # self.running = False


    def createForm(self):
        # global self.settingsForm
        self.HiddenForm = tkinter.Tk()
        self.HiddenForm.geometry("800x500+300+300")
        self.HiddenForm.attributes("-alpha",0.5)
        # self.clickWaingForm.wm_overrideredirect(1)
        lbl_timer = tkinter.Label(self.HiddenForm,text="timer").pack()
        self.showForm()
        # self.hideForm()
        self.HiddenForm.mainloop()

    def showForm(self):
        self.HiddenForm.deiconify()
        self.showing = True

    def hideForm(self):
        # self.settingForm.iconify()
        self.HiddenForm.withdraw()
        self.showing = False
        # self.settingForm.wm_withdraw

    # def click(self, e):
    #     super().click(e=e)
    #     self.update()

    def build(self):
        super().build()
        print(f"FletForTkTimer.build() \t\t\t time={time.time()}")
        # return super().build()
        # from flet import Text
        from flet import Container
        return Container()
        # import flet
        # return Text()
        # return flet.Control()
