import time

from lib import Motor


def main():
    motor = Motor(
        data_1=2,
        data_2=3,
        enable=4,
    )
    
    motor.forwards(100)
    time.sleep(3)
    motor.stop()
    time.sleep(2)
    motor.backwards(1)
    time.sleep(3)
    motor.full_stop()


if __name__ == "__main__":
    main()

