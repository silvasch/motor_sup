import RPi.GPIO as rpio

from manager import PinManager


def main():
    manager = PinManager(rpio.BCM)
    manager.add_pin("led", 2)


if __name__ == "__main__":
    main()

