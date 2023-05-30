import flet as ft
import time

def main(page: ft.Page):
    audio1 = ft.Audio(
        src="alarm.wav",autoplay=True
    )
    page.overlay.append(audio1)
    # page.overlay.append(audio1)
    page.update()
    # page.update()
    # time.sleep(1)
    # audio1.pause()
    # page.add(
    #     ft.Text("This is an app with background audio."),
    #     ft.ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
    # )

ft.app(target=main)