import time

from lib import Motor


def main():
    motor = Motor(
        data_1=2,
        data_2=3,
        enable=4,
        frequency=100
    )

    motor.forwards()
    time.sleep(3)
    motor.change_duty_cylce(20)
    time.sleep(3)
    motor.full_stop()


if __name__ == "__main__":
    main()

