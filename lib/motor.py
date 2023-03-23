import RPi.GPIO as gpio

from .pin import Pin
from .pin_manager import PinManager


class Motor:
    def __init__(self, data_1: int, data_2: int, enable: int, mode: gpio.BCM | gpio.BOARD = gpio.BCM):
        self.__pin_manager = PinManager(mode)
        self.__pin_manager.add_pin("data_1", Pin(data_1))
        self.__pin_manager.add_pin("data_2", Pin(data_2))
        self.__pin_manager.add_pin("enable", Pin(enable, is_pwm=True))

    def forwards(self, velocity: float):
        self.__pin_manager.on("data_1")
        self.__pin_manager.off("data_2")
        self.__pin_manager.set_velocity("enable", velocity)
    
    def backwards(self, velocity):
        self.__pin_manager.off("data_1")
        self.__pin_manager.on("data_2")
        self.__pin_manager.set_velocity("enable", velocity)

    def stop(self):
        self.__pin_manager.all_off()

    def full_stop(self):
        self.__pin_manager.all_on()

