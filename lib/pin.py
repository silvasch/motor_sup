import RPi.GPIO as gpio


class Pin:
    def __init__(self, pin: int, is_pwm: bool = False, frequency = 100):
        self.__pin = pin
        self.__is_pwm = is_pwm
        self.__frequency = frequency

        self.__pwm = None

        gpio.setup(self.__pin, gpio.OUT)
        if self.__is_pwm:
            self.__pwm = gpio.PWM(self.__pin, self.__frequency)

    def on(self):
        gpio.output(self.__pin, True)

    def off(self):
        gpio.output(self.__pin, False)

    def set_velocity(self, velocity: float):
        if self.__is_pwm:
            self.__pwm.start(velocity)

    def __del__(self):
        self.off()

