import os
from flet import icons, colors
import myButtons
import tkinter
import threading
import time
import webbrowser


class PanButton(myButtons.MyButton):
    def __init__(self,
                 icon: icons,
                 selected_icon: icons,
                 ipucu: str,
                 color: colors,
                 ):
        super().__init__(
            icon=icon,
            ipucu=ipucu,
            color=color,
            selected_icon=selected_icon,
        )
        print(f"PanButton.init() \t\t\t time={time.time()}")

    def on_closing(self):
        self.iconButton.selected = False
        self.update()
        del self.th
        self.panInformationForm.destroy()

    def whatever(self):
        print("oi don't press that button")
        self.iconButton.selected = False
        self.update()
        del self.th
        self.panInformationForm.quit()

    def createForm(self):
        self.panInformationForm = tkinter.Tk()
        self.panInformationForm.title(
            "Invitation form to create pan property - GlassOuse")
        self.panInformationForm.geometry("800x500+300+300")
        self.panInformationForm.resizable = False

        def my_open():
            url = "https://github.com/erkanhurnali/MyTools"
            webbrowser.open_new(url)

        my_button = tkinter.Button(self.panInformationForm, text="https://github.com/erkanhurnali/MyTools", fg="blue",
                                   cursor="hand2", font=18, command=my_open)

        my_button.grid(row=1, column=1, padx=20, pady=20)
        self.panInformationForm.protocol("WM_DELETE_WINDOW", self.whatever)
        self.panInformationForm.mainloop()

    def click(self, e):
        super().click(e=e)
        if self.iconButton.selected:
            # self.hide()
            self.iconButton.selected = False
            self.panInformationForm.destroy()
            del self.th
            self.update()
        else:
            # self.show()
            self.iconButton.selected = True
            self.update()
            self.th = threading.Thread(
                target=self.createForm,
                args=(),
                daemon=True
            )
            self.th.start()

    def build(self):
        print(f"SettingButton.build() \t\t\t time={time.time()}")
        return super().build()
