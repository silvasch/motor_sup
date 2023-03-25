import time

from lib import Motor


def main():
    motor = Motor(
        data_1=2,
        data_2=3,
        enable=4,
        frequency=10,
    )
    
    motor.forwards(100)
    time.sleep(10)
    motor.stop()
    time.sleep(1)
    motor.forwards(20)
    time.sleep(10)
    motor.full_stop()


if __name__ == "__main__":
    main()

