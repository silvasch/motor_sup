import RPIO as rpio

class PinManager:
    def __init__(self, mode: rpio.BOARD | rpio.BCM):
        self.__pins: dict[str, int] = {}
        rpio.setmode(mode)

    def add_pin(self, name: str, pin: int):
        rpio.setup(pin, rpio.OUT)
        self.__pins[name] = pin

    def remove_pin(self, name: str):
        del(self.__pins[name])

    def pin_on(self, name: str):
        rpio.output(self.__pins[name], rpio.HIGH)

    def pin_off(self, name: str):
        rpio.output(self.__pins[name], rpio.LOW)

    def __del__(self):
        rpio.cleanup()

