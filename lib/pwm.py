import wiringpi


class PWM:
    def __init__(self, pin_num: int) -> None:
        self.__pin_num = pin_num

        wiringpi.pinMode(self.__pin_num, 1)

    def on(self, duty_cycle: float = 100):
        duty_cycle = int((duty_cycle / 100) * 1024)
        print(duty_cycle)
        wiringpi.pwmWrite(self.__pin_num, duty_cycle)

    def off(self):
        wiringpi.pwmWrite(self.__pin_num, 0)
