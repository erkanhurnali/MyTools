import time
from threading import Timer

class MyTimer():
    def __init__(self) -> None:
        self.rt=self.RepeatTimer(1,self.updateTimer,["myTtimer -> "]).start()
        pass

    def updateTimer(self,msg):
        # print(f'{msg} time:{time.strftime("%H:%M:%S")}')
        pass
    def __del__(self):
        self.rt.cancel()
    
    class RepeatTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args,**self.kwargs)
