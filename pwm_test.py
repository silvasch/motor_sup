import RPi.GPIO as gpio
import time


DATA_1 = 2
DATA_2 = 3
ENABLE = 4


def main():
    gpio.setmode(gpio.BCM)
    
    gpio.setup(DATA_1, gpio.OUT)
    gpio.setup(DATA_2, gpio.OUT)
    gpio.setup(ENABLE, gpio.OUT)

    enable = gpio.PWM(ENABLE, 50)
    enable.start(0)

    gpio.output(DATA_1, gpio.HIGH)
    gpio.output(DATA_2, gpio.LOW)

    try:
        while True:
            for dc in range(0, 101, 5):
                enable.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                enable.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        enable.stop()
        gpio.cleanup()


if __name__ == "__main__":
    main()

