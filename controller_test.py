import time

from lib.controller import Controller


def main():
    controller = Controller()

    while True:
        print(controller.left_trigger)
        time.sleep(1)


if __name__ == "__main__":
    main()

