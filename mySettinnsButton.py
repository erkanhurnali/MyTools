import os
from flet import icons, colors
import myButtons
import tkinter as tk
import threading
import time
import webbrowser


class SettingButton(myButtons.MyButton):
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
        print(f"SettingButton.init() \t\t\t time={time.time()}")
        # self.showForm = False
        # self.iconButton.selected = False
        # self.settingForm=None

    # def did_mount(self):
    #     print(f"SettingButton.did_mount() \t\t time={time.time()}")
    #     # self.running = True
    #     # self.th = threading.Thread(target=self.createForm, args=(), daemon=True)
    #     # self.th.start()

    # def will_unmount(self):
    #     # self.running = False
    #     print(f"SettingButton.will_unmount() \t\t time={time.time()}")

    def on_closing(self):
        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.iconButton.selected = False
        self.update()
        del self.th
        self.settingForm.destroy()

    def whatever(self):
        # Replace this with your own event for example:
        print("oi don't press that button")
        self.iconButton.selected = False
        self.update()
        del self.th
        # self.settingForm.destroy()
        # self.settingForm.withdraw()
        self.settingForm.quit()

    def createForm(self):
        # global self.settingsForm
        self.settingForm = tk.Tk()
        self.settingForm.title("Settings - GlassOut")
        self.settingForm.geometry("800x500+300+300")
        # self.settingForm.attributes("-alpha",0.5)
        # self.settingForm.wm_overrideredirect(1)
        self.settingForm.resizable=False
        # self.settingForm.protocol("WM_DELETE_WINDOW", self.on_closing)
        # self.settingForm.protocol("WM_DELETE_WINDOW",self.settingForm.iconify())
        # self.settingForm.protocol("WM_DELETE_WINDOW",self.settingForm.withdraw())

        def handle_selection():
            selected_value = self.selected_option.get()
            if selected_value == "option1":
                pass
            elif selected_value == "option2":
                pass
            else:
                pass


        self.selected_option = tk.StringVar()
        self.selected_option.set("option1") 
        self.option_frame = tk.Frame(self.settingForm)
        self.option_frame.pack()

        textLbl= "Your keyboard choice (Klavye tercihiniz)"
        self.lblKeyboardChoice= tk.Label(self.option_frame, text=textLbl)
        self.option2 = tk.Radiobutton(self.option_frame, text="On-Screen Keyboard (Ekran Klavyesi)", variable=self.selected_option, value="option2", justify="left")
        self.option1 = tk.Radiobutton(self.option_frame, text="Touch Keyboard (Dokunmatik Klavye)", variable=self.selected_option, value="option1", justify="left")
        self.btnOnay = tk.Button(self.option_frame, text="OK", command=handle_selection)

        self.lblKeyboardChoice.pack()  
        self.option1.pack(anchor="w")  
        self.option2.pack(anchor="w")
        self.btnOnay.pack()


        def my_open():
            url = "https://mytools.com.tr"
            webbrowser.open_new(url)

        btnWebSite = tk.Button(self.settingForm,text="https://mytools.com.tr", fg="blue",
                      cursor="hand2",font=18,command=my_open)
        
        # btnWebSite.grid(row=2, column=0, sticky="w")

        btnWebSite.pack()
# my_w.mainloop()
        self.settingForm.protocol("WM_DELETE_WINDOW",self.whatever)
        self.settingForm.mainloop()
        # self.iconButton.selected = True
        # self.hide()
        # self.showForm = True

    # def show(self):
    #     self.settingForm.deiconify()
    #     self.showing = True

    # def hide(self):
    #     # self.settingForm.iconify()
    #     self.settingForm.withdraw()
    #     self.showing = False
    #     # self.settingForm.wm_withdraw

    def click(self, e):
        super().click(e=e)
        # if self.showForm:
        if self.iconButton.selected:
            # self.hide()
            # self.closeForm()
            self.iconButton.selected = False
            self.settingForm.destroy()
            # self.settingForm.quit()
            # self.settingForm.withdraw()
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
            # self.createForm()
            # self.iconButton.selected = False

            # self.update()

    def build(self):
        print(f"SettingButton.build() \t\t\t time={time.time()}")
        return super().build()

    # def closeForm(self):
    #     self.settingForm.destroy()
        # self.showForm = False
        # self.iconButton.selected = False

        # del self.th
