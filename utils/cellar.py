

# class RepeatTimer(Timer): 
    # def __init__(self, interval=1, function=None, args= None , kwargs=  None ) -> None:
    # def __init__(self, interval: float, function: Callable[..., object], args: Iterable[Any] | None = ..., kwargs: Mapping[str, Any] | None = ...) -> None:
    #     super().__init__(interval, function, args, kwargs)
    # def __init__(
    #     self,
    #     interval,
    #     # function:callable[...,object]=None,
    #     function,
    #     # args:  None = ..., kwargs: None = ...) -> None:        
    #     # args: Iterable[Any] | None = ..., kwargs: Mapping[str, Any] | None = ...) -> None:        

        # self.interval = interval
        # self.function=function
        # self.function=self.display
        # super().__init__(interval, function, args, kwargs)

        # super().__init__(
        #     interval= self.interval,
        #     function= self.display,
        #     args=args,
        #     kwargs=kwargs,
        # )
        # pass
    # def run(self):
    #     while not self.finished.wait(self.interval):
    #         self.function(*self.args,**self.kwargs)

    # def display(self,msg):
    #     print(f'{msg} time:{time.strftime("%H:%M:%S")}')

# timer =RepeatTimer(1,self.display,["saat"])
# timer =RepeatTimer(1,self.display,["saat"])
# timer.start()

# time.sleep(10)
# timer.cancel()

 

