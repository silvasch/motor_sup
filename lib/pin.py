import wiringpi


class Pin:
    def __init__(self, pin_num: int):
        self.__pin_num = pin_num

        wiringpi.pinMode(self.__pin_num, 1)

    def on(self):
        wiringpi.digitalWrite(self.__pin_num, 1)

    def off(self):
        wiringpi.digitalWrite(self.__pin_num, 0)

    def __del__(self):
        gpio.cleanup()
