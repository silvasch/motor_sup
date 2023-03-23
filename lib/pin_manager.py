import RPi.GPIO as gpio

from . import Pin


class PinManager:
    def __init__(self, mode: gpio.BOARD | gpio.BCM):
        self.__pins: dict[str, Pin] = {}
        gpio.setmode(mode)

    def add_pin(self, name: str, pin: Pin):
        self.__pins[name] = pin

    def remove_pin(self, name: str):
        del(self.__pins[name])

    def on(self, name: str):
        self.__pins[name].on()

    def off(self, name: str):
        self.__pins[name].off()

    def set_velocity(self, name: str, velocity: float):
        self.__pins[name].set_velocity(velocity)

    def all_on(self):
        for name in self.__pins:
            self.__pins[name].on()

    def all_off(self):
        for name in self.__pins:
            self.__pins[name].off()

    def __del__(self):
        self.all_off()
