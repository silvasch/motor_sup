import RPi.GPIO as rpio
import time

from lib import PinManager


def main():
    manager = PinManager(rpio.BCM)
    manager.add_pin("led", 2)
    manager.pin_on("led")
    time.sleep(5)
    manager.pin_off("led")


if __name__ == "__main__":
    main()

