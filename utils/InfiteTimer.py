import threading
import time

class InfiteTimer():
    def __init__(self, running:bool=False, interval:float=1):
        super().__init__()
        self.running = running
        self.interval=interval
        self.counter=0

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.running:
            self.counter+=1
            print(f"self.counter={self.counter}")
            time.sleep(self.interval)
    def stop(self):
        self.running=False
