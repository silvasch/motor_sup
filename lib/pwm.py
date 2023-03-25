import RPi.GPIO as gpio


class PWM:
    def __init__(self, pin_num: int, frequency: int = 100, initial_duty_cycle: int = 0) -> None:
        self.__pin_num = pin_num
        self.__frequency = frequency
        self.__duty_cycle = initial_duty_cycle

        self.__pwm = gpio.PWM(self.__pin_num, self.__frequency)

    def on(self, duty_cycle: float = 100):
        self.__duty_cycle = duty_cycle
        self.__pwm.start(self.__duty_cycle)

    def off(self):
        self.__pwm.stop()

    def set_duty_cycle(self, duty_cycle: float):
        self.__duty_cycle = duty_cycle
        self.__pwm.ChangeDutyCycle(self.__duty_cycle)

    def __del__(self):
        gpio.cleanup()
