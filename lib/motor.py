from . import Pin, PinManager


class Motor:
    def __init__(self, data_1: int, data_2: int, enable: int, mode: gpio.BCM | gpio.BOARD = gpio.BCM):
        self.__pin_manager = PinManager(mode)
        self.__pin_manager.add_pin("data_1", Pin(data_1))
        self.__pin_manager.add_pin("data_2", Pin(data_2))
        self.__pin_manager.add_pin("enable", Pin(enable))

    def forwards(self):
        self.__pin_manager.on("data_1")
        self.__pin_manager.off("data_2")
        self.__pin_manager.on("enable")
    
    def backwards(self):
        self.__pin_manager.off("data_1")
        self.__pin_manager.on("data_2")
        self.__pin_manager.on("enable")

    def stop(self):
        self.__pin_manager.all_off()

    def full_stop(self):
        self.__pin_manager.all_on()

