import time

from lib import Motor


def main():
    motor = Motor(
        data_1=2,
        data_2=3,
        enable=4,
        frequency=100,
    )
    
    motor.forwards(50)
    time.sleep(3)
    motor.stop()
    time.sleep(2)
    motor.backwards(50)
    time.sleep(3)
    motor.full_stop()


if __name__ == "__main__":
    main()

