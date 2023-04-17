import RPi.GPIO as gpio
import time

import lib


def main():
    gpio.setmode(gpio.BOARD) # type: ignore

    motor = lib.Motor(
        data_1=2,
        data_2=3,
        enable=4,
    )

    motor.forwards()
    time.sleep(5)
    motor.stop()
    time.sleep(2)
    motor.forwards()
    time.sleep(5)
    motor.stop()


if __name__ == "__main__":
    main()

