import RPi.GPIO as rpio

from .manager import PinManager


class Motor:
    def __init__(self, data_1: int, data_2: int, enable: int):
        self.manager = PinManager(rpio.BCM)
        self.manager.add_pin("data_1", data_1)
        self.manager.add_pin("data_2", data_2)
        self.manager.add_pin("enable", enable)

    def stop(self):
        self.manager.all_off()

    def full_stop(self):
        self.manager.all_on()

    def backwards(self):
        self.manager.pin_off("data_1")
        self.manager.pin_on("data_2")
        self.manager.pin_on("enable")

    def forwards(self):
        self.manager.pin_on("data_1")
        self.manager.pin_off("data_2")
        self.manager.pin_on("enable")

