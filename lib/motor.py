from .pin import Pin
from .pwm import PWM


class Motor:
    def __init__(self, data_1: int, data_2: int, enable: int, frequency: int = 100):
        self.__data_1 = Pin(data_1)
        self.__data_2 = Pin(data_2)
        self.__enable = PWM(enable, frequency)

    def forwards(self, duty_cycle: float = 100):
        self.__enable.on(duty_cycle)
        self.__data_1.on()
        self.__data_2.off()

    def backwards(self, duty_cycle: float = 100):
        self.__enable.on(duty_cycle)
        self.__data_1.off()
        self.__data_2.on()

    def stop(self):
        self.__data_1.off()
        self.__data_2.off()
        self.__enable.off()

    def full_stop(self):
        self.__data_1.on()
        self.__data_2.on()
        self.__enable.on()

    def change_duty_cylce(self, duty_cycle: float):
        self.__enable.set_duty_cycle(duty_cycle)
