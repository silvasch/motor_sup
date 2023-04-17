import RPi.GPIO as gpio


class Pin:
    def __init__(self, pin: int):
        self.__pin = pin
        gpio.setup(self.__pin, gpio.OUT) # type: ignore

        self.__is_on: bool = False

    def on(self):
        gpio.output(self.__pin, 1) # type: ignore
        self.__is_on = True

    def off(self):
        gpio.output(self.__pin, 0) # type: ignore
        self.__is_on = False

    def is_on(self) -> bool:
        return self.__is_on

    def __del__(self):
        self.off()

