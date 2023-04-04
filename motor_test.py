import RPi.GPIO as gpio
import time

from lib import Motor


def main():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    motor = Motor(
        data_1=2,
        data_2=3,
        enable=4,
        frequency=2000,
    )

    motor.forwards(100)
    time.sleep(5)
    motor.forwards(50)
    time.sleep(5)
    motor.stop()


if __name__ == "__main__":
    main()

