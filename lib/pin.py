import RPi.GPIO as gpio


class Pin:
    def __init__(self, pin_num: int):
        self.__pin_num = pin_num

        gpio.setup(self.__pin_num, gpio.OUT)

    def on(self):
        gpio.output(self.__pin_num, gpio.HIGH)

    def off(self):
        gpio.output(self.__pin_num, gpio.LOW)

    def __del__(self):
        gpio.cleanup()
