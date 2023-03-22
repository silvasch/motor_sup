import RPi.GPIO as rpio
import time

from manager import PinManager


class App:
    def __init__(self):
        self.manager = PinManager(rpio.BCM)
        self.manager.add_pin("data_1", 2)
        self.manager.add_pin("data_2", 3)
        self.manager.add_pin("enable", 4)

    def let_go(self):
        self.manager.all_off()

    def back(self):
        self.manager.pin_off("data_1")
        self.manager.pin_on("data_2")
        self.manager.pin_on("enable")

    def forward(self):
        self.manager.pin_on("data_1")
        self.manager.pin_off("data_2")
        self.manager.pin_on("enable")

def main():
    app = App()

    app.forward()
    time.sleep(5)
    app.let_go()
    time.sleep(2)
    app.back()
    time.sleep(5)
    app.let_go()


if __name__ == "__main__":
    main()

