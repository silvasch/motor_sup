from .pin import Pin


class Motor:
    def __init__(self, data_1: int, data_2: int, enable: int):
        self.__data_1 = Pin(data_1)
        self.__data_2 = Pin(data_2)
        self.__enable = Pin(enable)

    def forwards(self):
        self.__data_1.on()
        self.__data_2.off()
        self.__enable.on()

    def backwards(self):
        self.__data_1.off()
        self.__data_2.on()
        self.__enable.on()

    def stop(self):
        self.__data_1.off()
        self.__data_2.off()
        self.__enable.off()

    def full_stop(self):
        self.__data_1.on()
        self.__data_2.on()
        self.__enable.on()

    def __del__(self):
        pass

